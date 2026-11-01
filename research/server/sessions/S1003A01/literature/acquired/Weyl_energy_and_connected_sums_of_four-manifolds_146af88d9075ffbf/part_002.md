---
retention_scope: session
part: 2
total_parts: 3
---

[Part 2/3 of: Weyl energy and connected sums of four-manifolds]

In both cases, the system has the same coefficient matrix $A_{\gamma}$ and one has $\operatorname{det}\left(A_{\gamma}\right) \neq 0 \forall \gamma \in(0,1)$. In particular, letting $\mathbf{v}=\left(v_{1}, v_{2}, v_{3}, v_{4}\right)$, one can see that the solution $\mathbf{c}=\left(c_{1}, c_{2}, c_{3}, c_{4}\right)$ to (4.10) is given by:
$$\begin{aligned}
& c_{1}=a^{2} \frac{2 v_{1}\left(1+\gamma^{2}+4 \gamma^{4}\right)+v_{2}\left(1+\gamma^{2}-2 \gamma^{4}\right)-\gamma^{6}\left(2 v_{3}\left(4+\gamma^{2}+\gamma^{4}\right)+v_{4}\left(-2+\gamma^{2}+\gamma^{4}\right)\right)}{2\left(\gamma^{2}-1\right)^{3}\left(1+4 \gamma^{2}+\gamma^{4}\right)} \\
& c_{2}=a^{2} \frac{-4 v_{1}\left(1+\gamma^{2}+\gamma^{4}+3 \gamma^{6}\right)+v_{2}\left(\gamma^{2}-1\right)\left(1+2 \gamma^{2}+3 \gamma^{4}\right)+\gamma^{6}\left(3\left(4 v_{3}-v_{4}\right)+\left(4 v_{3}+v_{4}\right)\left(\gamma^{2}+\gamma^{4}+\gamma^{6}\right)\right)}{2 \gamma^{2}\left(\gamma^{2}-1\right)^{3}\left(1+4 \gamma^{2}+\gamma^{4}\right)} \\
& c_{3}=a^{2} \frac{4 v_{1}\left(3+\gamma^{2}+\gamma^{4}+\gamma^{6}\right)-v_{2}\left(-3+\gamma^{2}+\gamma^{4}+\gamma^{6}\right)+\gamma^{2}\left(\left(-4 v_{3}+v_{4}\right)\left(1+\gamma^{2}+\gamma^{4}\right)-3 \gamma^{6}\left(v_{3}+v_{4}\right)\right)}{2 \gamma^{2}\left(\gamma^{2}-1\right)^{3}\left(1+4 \gamma^{2}+\gamma^{4}\right)} \\
& c_{4}=a^{2} \frac{-2 v_{1}\left(4+\gamma^{2}+\gamma^{4}\right)+v_{2}\left(-2+\gamma^{2}+\gamma^{4}\right)+\gamma^{2}\left(2 v_{3}\left(1+\gamma^{2}+4 \gamma^{4}\right)+v_{4}\left(-1-\gamma^{2}+2 \gamma^{4}\right)\right)}{2 \gamma^{2}\left(\gamma^{2}-1\right)^{3}\left(1+4 \gamma^{2}+\gamma^{4}\right)}
\end{aligned}$$
In other words, we get an explicit formula for $f_{\alpha, \beta}$ and $\tilde{f}_{\alpha, \beta}$ in terms of $\gamma$ and the boundary datum $\mathbf{v}$ given by (4.12) and (4.13) respectively.
\begin{itemize}
\item[-] if $i \neq j$, for $(\alpha, \beta) \in\{(j, i),(j, s),(j, t),(s, i),(t, i)\}$ one has
$$\left\{\begin{array}{l}
f_{\alpha, \beta}(\gamma)=-\frac{1}{3} a^{2} \gamma^{-2} W_{\alpha i j \beta}^{M} \\
f_{\alpha, \beta}^{\prime}(\gamma)=\frac{2}{3} a^{2} \gamma^{-3} W_{\alpha i j \beta}^{M} \\
f_{\alpha, \beta}(1)=-\frac{1}{3} b^{2} W_{\alpha i j \beta}^{Z} \\
f_{\alpha, \beta}^{\prime}(1)=-\frac{2}{3} b^{2} W_{\alpha i j \beta}^{Z}
\end{array}\right.$$
while
$$\left\{\begin{array} { l } 
{ f _ { s , t } ( \gamma ) = - \frac { 1 } { 3 } a ^ { 2 } \gamma ^ { - 2 } ( W _ { s i j t } ^ { M } + W _ { t i j s } ^ { M } ) } \\
{ f _ { s , t } ^ { \prime } ( \gamma ) = \frac { 2 } { 3 } a ^ { 2 } \gamma ^ { - 3 } ( W _ { s i j t } ^ { M } + W _ { t i j s } ^ { M } ) } \\
{ f _ { s , t } ( 1 ) = - \frac { 1 } { 3 } b ^ { 2 } ( W _ { s i j t } ^ { Z } + W _ { t i j s } ^ { Z } ) } \\
{ f _ { s , t } ^ { \prime } ( 1 ) = - \frac { 2 } { 3 } b ^ { 2 } ( W _ { s i j t } ^ { Z } + W _ { t i j s } ^ { Z } ) , }
\end{array} \quad \text { and } \quad \left\{\begin{array}{l}
\tilde{f}_{s, t}(\gamma)=-\frac{1}{3} a^{2} \gamma^{-2} W_{s i j s}^{M} \\
\tilde{f}_{s, t}^{\prime}(\gamma)=\frac{2}{3} a^{2} \gamma^{-3} W_{s i j s}^{M} \\
\tilde{f}_{s, t}(1)=-\frac{1}{3} b^{2} W_{s i j s}^{Z} \\
\tilde{f}_{s, t}^{\prime}(1)=-\frac{2}{3} b^{2} W_{s i j s}^{Z} .
\end{array}\right.\right.$$
Then, as in the previous case (we get a system with matrix $A_{\gamma}$ as in (4.11)), one obtains an explicit expression of $f_{\alpha, \beta}, \tilde{f}_{\alpha, \beta}$ (which are of the form (4.8), (4.9)) where the constants $c_{d, \alpha, \beta}$, $\tilde{c}_{d, \alpha, \beta}$ are as in (4.14) and $\mathbf{v}=\left(v_{1}, v_{2}, v_{3}, v_{4}\right)$ is given by (4.15), (4.16). In particular, for $(\alpha, \beta) \in$ $\{(j, i),(j, s),(j, t),(s, i),(t, i)\}$, we get
$$\mathbf{v}_{\alpha, \beta}=\left(\begin{array}{c}
-\frac{1}{3} \gamma^{2} W_{\alpha i j \beta}^{M} \\
\frac{2}{3} \gamma^{2} W_{\alpha i j \beta}^{M} \\
-\frac{1}{3} b^{2} a^{-2} W_{\alpha i j \beta}^{Z} \\
-\frac{2}{3} b^{2} a^{-2} W_{\alpha i j \beta}^{Z}
\end{array}\right),$$
\end{itemize}
while
$$\mathbf{v}_{s, t}=\left(\begin{array}{c}
-\frac{1}{3} \gamma^{2}\left(W_{s i j t}^{M}+W_{t i j s}^{M}\right) \\
\frac{2}{3} \gamma^{2}\left(W_{s i j t}^{M}+W_{t i j s}^{M}\right) \\
-\frac{1}{3} b^{2} a^{-2}\left(W_{s i j t}^{Z}+W_{t i j s}^{Z}\right) \\
-\frac{2}{3} b^{2} a^{-2}\left(W_{s i j t}^{Z}+W_{t i j s}^{Z}\right)
\end{array}\right), \quad \tilde{\mathbf{v}}_{s, t}=\left(\begin{array}{c}
-\frac{1}{3} \gamma^{2} W_{s i j s}^{M} \\
\frac{2}{3} \gamma^{2} W_{s i j s}^{M} \\
-\frac{1}{3} b^{2} a^{-2} W_{s i j s}^{Z} \\
-\frac{2}{3} b^{2} a^{-2} W_{s i j s}^{Z}
\end{array}\right) .$$

Remark 4.1. In both cases $i=j$ and $i \neq j$, the boundary datum $\mathbf{v}=\left(v_{1}, v_{2}, v_{3}, v_{4}\right)$ (which is given by (4.12), (4.13) and (4.17), (4.18) respectively) always satisfies the relations $v_{2}=-2 v_{1}$ and $v_{4}=2 v_{3}$; using these formulae and expanding with respect to $\gamma \rightarrow 0$ (later on, we will fix the value of $b^{2} a^{-2}$ before fixing $\gamma$, so this is allowed), (4.14) turns into
$$\begin{aligned}
& \hat{c}_{1}:=a^{-2} c_{1}=-6 v_{1} \gamma^{4}+2 v_{3} \gamma^{6}+6 v_{1} \gamma^{6}+O\left(\gamma^{10}\left(1+b^{2} a^{-2}\right)\right) \\
& \hat{c}_{2}:=a^{-2} c_{2}=\frac{v_{1}}{\gamma^{2}}+9 v_{1} \gamma^{2}-3 v_{3} \gamma^{4}+O\left(\gamma^{6}\left(1+b^{2} a^{-2}\right)\right) \\
& \hat{c}_{3}:=a^{-2} c_{3}=-\frac{3 v_{1}}{\gamma^{2}}+v_{3}-27 v_{1} \gamma^{2}+9 v_{3} \gamma^{4}+O\left(\gamma^{6}\left(1+b^{2} a^{-2}\right)\right) \\
& \hat{c}_{4}:=a^{-2} c_{4}=\frac{2 v_{1}}{\gamma^{2}}+18 v_{1} \gamma^{2}-6 v_{3} \gamma^{4}+O\left(\gamma^{6}\left(1+b^{2} a^{-2}\right)\right) .
\end{aligned}$$

\section*{5 Comparison of Weyl energies}

We now want to compute the difference between the Weyl energy of $\left(X, g_{X}\right)$ defined at the end of Section 3 and the sum of the Weyl energies of $\left(M, g_{M}\right)$ and $\left(Z, g_{Z}\right)$.

To begin we notice that, by definition of $\left(X, g_{X}\right)$ and by conformal invariance of the Weyl energy, it holds
$$\begin{aligned}
\mathcal{W}^{X}\left(g_{X}\right)-\mathcal{W}^{M} & \left(g_{M}\right)-\mathcal{W}^{Z}\left(g_{Z}\right)=\mathcal{W}^{X}\left(g_{X}\right)-\mathcal{W}^{N}\left(g_{a}\right)-\mathcal{W}^{Z}\left(g_{b}\right) \\
& =\int_{B_{1+\sqrt{a}} \backslash B_{\gamma-\sqrt{a}}}\left|W^{g_{X}}\right|^{2} d V_{g_{X}}-\int_{\mathbb{R}^{4} \backslash B_{\gamma-\sqrt{a}}}\left|W^{g_{a}}\right|^{2} d V_{g_{a}}-\int_{B_{1+\sqrt{a}}}\left|W^{g_{b}}\right|^{2} d V_{g_{b}}
\end{aligned}$$
where the domains of each integral are to be understood with respect to the coordinates $\left\{x^{i}\right\}$ defined on $Z$ (and more generally on the gluing region) in Section 3. In order to prove Theorem 1.1, we would like to estimate the three integrals above and show that (5.1) has negative sign for a suitable choice of the parameters $a, b, \gamma$, of the basepoints $p \in M, q \in Z$, and of the normal coordinate systems.

We start by computing the Weyl energies of $g_{b}$ and $g_{a}$ and then we will focus on the Weyl energy of $g_{X}$. We consider for now the contributions inside the regions $B_{1}$ and $\mathbb{R}^{4} \backslash B_{\gamma}$ (for $g_{b}$ and $g_{a}$ respectively) and on the annulus $B_{1} \backslash B_{\gamma}$ (for $g_{X}$ ); lastly, at the end of the section, we will show that the integrals on the remaining cutoff regions generate an higher order contribution (cf. Lemma 5.14).

Define the (0, 2)-symmetric tensors $H$ and $F$ by:
$$H_{i j}(x):=-\frac{1}{3} W_{k i j l}^{Z}(q) x^{k} x^{l}, \quad F_{i j}(x):=-\frac{1}{3} W_{k i j l}^{M}(p) \frac{x^{k} x^{k}}{|x|^{4}} .$$

Remark 5.1. One has
$$\Delta H_{i j} \equiv 0 \quad \text { in } \mathbb{R}^{4}, \quad \Delta^{2} F_{i j} \equiv 0 \quad \text { in } \mathbb{R}^{4} \backslash\{0\}, \forall i, j ;$$
the first formula follows from the trace free-property of Weyl's tensor, while the second one follows from a direct computation. Moreover, by using again the trace-free property together with the symmetries of $W^{M}$ and $W^{Z}$, it is easy to check (see the proof of Lemma 5.5 in the Appendix) that both $F=F_{i j}$ and $H=H_{i j}$ are TT-tensors (transverse-traceless).

We can now state the following:
Lemma 5.2. One has
$$\begin{aligned}
& \int_{B_{1}}\left|W^{g_{b}}\right|^{2} d V_{g_{b}}=-\frac{b^{4}}{2} \sum_{i, j, \beta} \int_{\partial B_{1}} H_{i j} \partial_{\alpha \beta \beta}^{3} H_{i j} \nu^{\alpha} d \sigma \\
& \quad+b^{4} \sum_{i, j, \beta} \int_{\partial B_{1}}\left[\left(\partial_{i j}^{2} H_{\alpha \beta}-2 \partial_{\beta j}^{2} H_{i \alpha}+\partial_{\alpha \beta}^{2} H_{i j}\right) \partial_{\beta} H_{i j}-\frac{1}{2} \partial_{\beta \beta}^{2} H_{i j} \partial_{\alpha} H_{i j}\right] \nu^{\alpha} d \sigma+O\left(b^{6}\right)
\end{aligned}$$
$$\begin{aligned}
& \int_{\mathbb{R}^{4} \backslash B_{\gamma}}\left|W^{g_{a}}\right|^{2} d V_{g_{a}}=-\frac{a^{4}}{2} \sum_{i, j, \beta} \int_{\partial B_{\gamma}} F_{i j} \partial_{\alpha \beta \beta}^{3} F_{i j} \nu^{\alpha} d \sigma \\
& \quad+a^{4} \sum_{i, j, \beta} \int_{\partial B_{\gamma}}\left[\left(\partial_{i j}^{2} F_{\alpha \beta}-2 \partial_{\beta j}^{2} F_{i \alpha}+\partial_{\alpha \beta}^{2} F_{i j}\right) \partial_{\beta} F_{i j}-\frac{1}{2} \partial_{\beta \beta}^{2} F_{i j} \partial_{\alpha} F_{i j}\right] \nu^{\alpha} d \sigma+O\left(a^{6}\right)
\end{aligned}$$
Proof. By (3.4), (3.5) and (3.9), (3.10) we immediately see that, letting $s:=b^{2}, t:=a^{2}$, then $\left.\frac{d}{d s}\right|_{s=0}\left(g_{b}\right)_{i j}=H_{i j}$ and $\left.\frac{d}{d t}\right|_{t=0}\left(g_{a}\right)_{i j}=F_{i j}$ respectively. At this point, (5.4) follows from (2.20) (take $\Omega=B_{1}$ ) once we recall (5.3) and the fact that $H$ is TT.

The same argument also works for (5.5): indeed, even if the domain is unbounded this time, by definition of $F_{i j}$ it holds
$$\left|\nabla^{2} F_{i j}(x)\right|\left|\nabla^{k} F_{i j}(x)\right|=O\left(|x|^{-6-k}\right) \quad \text { as } \quad|x| \rightarrow \infty,$$
so that we can still perform all the integration by parts leading to (2.20). \(\square\)

We can now turn our attention to the computation of Weyl's energy for the interpolating metric $g_{X}$ in $B_{1} \backslash B_{\gamma}$, where it holds $\left(g_{X}\right)_{i j}=w_{i j}$ by construction.

Remark 5.3. From now on we assume that $b=\lambda a$, where $\lambda>0$ will be specified later; notice however that, in the end, the constants $\lambda, a, \gamma$ will be chosen such that $0<a \ll \gamma \ll \lambda^{-1}<1$, so we will implicitly assume this while performing the various expansions.

By the results in Section 4, we know that each $w_{i j}$ writes as
$$w_{i j}(x)=\delta_{i j}+\sum_{\alpha} f_{\alpha, i, j}(r) \varphi_{\alpha}(\vartheta),$$
where $r=|x|$ and $\vartheta=\frac{x}{|x|}$, see (4.3) and (4.5). Moreover, each $f_{\alpha}$ is of the form
$$f(r)=\frac{c_{1}}{r^{4}}+\frac{c_{2}}{r^{2}}+c_{3} r^{2}+c_{4} r^{4},$$
where $c_{1}, c_{2}, c_{3}, c_{4}$ are given by (4.19). By (4.12), (4.13), (4.17) and (4.18) we see that one always has $v_{1}=O\left(\gamma^{2}\right)$ and $v_{3}=O\left(b^{2} a^{-2}\right)=O\left(\lambda^{2}\right)$, so, if we let $t:=a^{2}$ and consider $w=\left(w_{i j}\right)=\left(w_{i j}\right)(t)$ as a family of metrics on $B_{1} \backslash B_{\gamma}$ depending on $t$, then $w_{i j}(0)=\delta_{i j}$ and, letting
$$\dot{w}_{i j}:=\left.\frac{d}{d t}\right|_{t=0} w_{i j}(t),$$
then $\dot{w}_{i j}$ takes the general form
$$\dot{w}_{i j}=a^{-2} \sum_{\alpha} f_{\alpha, i, j}(r) \varphi_{\alpha}(\vartheta)=a^{-2}\left(w_{i j}-\delta_{i j}\right) .$$

Remark 5.4. (5.6) is in fact an equality. In other words, $w_{i j}$ is precisely of the form Euclidean metric + linear error in $t$ because of our choice of (exact) boundary data in (3.13).

We also have the following fact:
Lemma 5.5. $\dot{w}$ is a TT tensor.
The proof is a long but trivial check and is postponed to the Appendix. As a consequence, we can apply (2.20) to the metric $w(t)$ in $\Omega=B_{1} \backslash B_{\gamma}$ : recalling (5.6) and that $w$ is harmonic by construction (see (3.13)), we get
$$\begin{aligned}
\mathcal{W}(w) & :=\int_{B_{1} \backslash B_{\gamma}}\left|W_{g_{X}}\right|^{2} d V_{g_{X}}=-\frac{a^{4}}{2} \sum_{i, j, \beta} \int_{\partial\left(B_{1} \backslash B_{\gamma}\right)} \dot{w}_{i j} \partial_{\alpha \beta \beta}^{3} \dot{w}_{i j} \nu^{\alpha} d \sigma \\
& +a^{4} \sum_{i, j, \beta} \int_{\partial\left(B_{1} \backslash B_{\gamma}\right)}\left[\left(\partial_{i j}^{2} \dot{w}_{\alpha \beta}-2 \partial_{\beta j}^{2} \dot{w}_{i \alpha}+\partial_{\alpha \beta}^{2} \dot{w}_{i j}\right) \partial_{\beta} \dot{w}_{i j}-\frac{1}{2} \partial_{\beta \beta}^{2} \dot{w}_{i j} \partial_{\alpha} \dot{w}_{i j}\right] \nu^{\alpha} d \sigma+O\left(a^{6}\right)
\end{aligned}$$

We thus have an expression involving products of mixed derivatives of $\dot{w}_{i j}$; in order to estimate this quantity, we first look at the general formula of $\dot{w}_{i j}$ and try to isolate the type of terms which generate the biggest contributions with respect to the parameter $\gamma$.

By definition of $\dot{w}_{i j}$ one sees that, for $x \in B_{1} \backslash B_{\gamma}$,
$$\begin{aligned}
\dot{w}_{i j} & \simeq \hat{c}_{1}|x|^{-4}+\hat{c}_{2}|x|^{-2}+\hat{c}_{3}|x|^{2}+\hat{c}_{4}|x|^{4} \\
\partial_{\alpha} \dot{w}_{i j} & \simeq \hat{c}_{1}|x|^{-5}+\hat{c}_{2}|x|^{-3}+\hat{c}_{3}|x|+\hat{c}_{4}|x|^{3} \\
\partial_{\alpha \beta}^{2} \dot{w}_{i j} & \simeq \hat{c}_{1}|x|^{-6}+\hat{c}_{2}|x|^{-4}+\hat{c}_{3}+\hat{c}_{4}|x|^{2} \\
\partial_{\alpha \beta \tau}^{3} \dot{w}_{i j} & \simeq \hat{c}_{1}|x|^{-7}+\hat{c}_{2}|x|^{-5}+\hat{c}_{3}|x|^{-1}+\hat{c}_{4}|x|
\end{aligned}$$
where $\hat{c}_{1}, \ldots, \hat{c}_{4}$ are given by (4.19).
- If $|x|=\gamma$ (i.e. we are considering the integrals on $\partial B_{\gamma}$ ), then from (5.8) and (4.19) (recall that $v_{1}=O\left(\gamma^{2}\right)$ and $\left.v_{3}=O\left(\lambda^{2}\right)\right)$ we see that the main contribution comes from the $c_{2} /|x|^{2}$-terms, which generate integrals of order $\gamma^{-4}$ in (5.7). Indeed, for $1 \ll \gamma \ll \lambda^{-1}$ one has
$$\hat{c}_{1}=O\left(\gamma^{6}\left(1+\lambda^{2}\right)\right), \quad \hat{c}_{2}=O(1), \quad \hat{c}_{3}=O\left(1+\lambda^{2}\right), \quad \hat{c}_{4}=O(1),$$
so that
$$\dot{w}_{i j}=O\left(|x|^{-2}\right)=O\left(\gamma^{-2}\right), \quad \partial_{\alpha} \dot{w}_{i j}=O\left(\gamma^{-3}\right), \quad \partial_{\alpha \beta}^{2} \dot{w}_{i j}=O\left(\gamma^{-4}\right), \quad \partial_{\alpha \beta \tau}^{3} \dot{w}_{i j}=O\left(\gamma^{-5}\right),$$
and therefore
$$\int_{\partial B_{\gamma}} \partial_{\alpha} \dot{w}_{i j} \partial_{\beta \tau}^{2} \dot{w}_{i j} d \sigma=O\left(\gamma^{-4}\right)=\int_{\partial B_{\gamma}} \dot{w}_{i j} \partial_{\alpha \beta \tau}^{3} \dot{w}_{i j} d \sigma$$
We now want to write an explicit expression for the main term.
If $i=j$, then, from (5.6), (4.3), (4.1), (4.8), (4.9) and the above discussion we get
$$\begin{aligned}
a^{2} \dot{w}_{i i}(x) & =f_{s, t}(|x|) \varphi_{s, t}+f_{s, u}(|x|) \varphi_{s, u}+f_{t, u}(|x|) \varphi_{t, u}+\tilde{f}_{s, u}(|x|) \psi_{s, u}+\tilde{f}_{t, u}(|x|) \psi_{t, u} \\
& =\frac{c_{2, s, t}}{|x|^{2}} \frac{x_{s} x_{t}}{|x|^{2}}+\frac{c_{2, s, u}}{|x|^{2}} \frac{x_{s} x_{u}}{|x|^{2}}+\frac{c_{2, t, u}}{|x|^{2}} \frac{x_{t} x_{u}}{|x|^{2}}+\frac{\tilde{c}_{2, s, u}}{|x|^{2}} \frac{x_{s}^{2}-x_{u}^{2}}{|x|^{2}}+\frac{\tilde{c}_{2, t, u}}{|x|^{2}} \frac{x_{t}^{2}-x_{u}^{2}}{|x|^{2}}+\text { h.o.t. }
\end{aligned}$$
By (4.19), we have $c_{2}=a^{2}\left(v_{1} / \gamma^{2}+O\left(\gamma^{4}\left(1+\lambda^{2}\right)\right)\right)$, so, taking from (4.12), (4.13) the values of $v_{1}$ for each term, one gets
$$\dot{w}_{i i}=-\frac{2}{3} W_{s i i t}^{M} \frac{x_{s} x_{t}}{|x|^{4}}-\frac{2}{3} W_{s i i u}^{M} \frac{x_{s} x_{u}}{|x|^{4}}-\frac{2}{3} W_{t i i u}^{M} \frac{x_{t} x_{u}}{|x|^{4}}-\frac{1}{3} W_{s i i s}^{M} \frac{x_{s}^{2}-x_{u}^{2}}{|x|^{4}}-\frac{1}{3} W_{t i i t}^{M} \frac{x_{t}^{2}-x_{u}^{2}}{|x|^{4}}+\text { h.o.t. }$$

Using now the trace-free property of Weyl's tensor we finally obtain
$$\dot{w}_{i i}=-\frac{1}{3} W_{k i i l}^{M} \frac{x^{k} x^{l}}{|x|^{4}}+\text { h.o.t. }=F_{i i}(x)+\text { h.o.t. }$$

If $i \neq j$, we can proceed in the exact same way using instead (4.5), (4.17) and (4.18); in the end we find
$$\dot{w}_{i j}=-\frac{1}{3} W_{k i j l}^{M} \frac{x^{k} x^{l}}{|x|^{4}}+\text { h.o.t. }=F_{i j}(x)+\text { h.o.t. }$$

By (5.10), (5.11) we see that, at the main order, the Weyl energy of $w$ in $B_{1} \backslash B_{\gamma}$ coincides with the Weyl energy of $g_{a}$ in $\mathbb{R}^{4} \backslash B_{\gamma}$ (just compare (5.7) to (5.5)); as a consequence, the two contributions cancel out in the energy balance (5.1).
- If $|x|=1$ instead, then by (5.8) and (4.19) we see that the main contribution comes from the products of $c_{3}|x|^{2}$-terms, which will generate integrals of order $\lambda^{4}$ in (5.7). Indeed, by (5.8) and (5.9) we have in this case
$$\dot{w}_{i j}=O\left(\lambda^{2}\right), \quad \partial_{\alpha} \dot{w}_{i j}=O\left(\lambda^{2}\right), \quad \partial_{\alpha \beta}^{2} \dot{w}_{i j}=O\left(\lambda^{2}\right), \quad \partial_{\alpha \beta \tau}^{3} \dot{w}_{i j}=O\left(\lambda^{2}\right),$$
therefore
$$\int_{\partial B_{1}} \partial_{\alpha} \dot{w}_{i j} \partial_{\beta \tau}^{2} \dot{w}_{i j} d \sigma=O\left(\lambda^{4}\right)=\int_{\partial B_{1}} \dot{w}_{i j} \partial_{\alpha \beta \tau}^{3} \dot{w}_{i j} d \sigma$$
As in the previous case, we can write down explicitly the main order term of $\dot{w}_{i j}$ by using (5.6), (4.3), (4.5), (4.8), (4.9), (4.19) and the explicit values of $v_{3}$ given by the formulae in Section 4. We end up finding that
$$\dot{w}_{i j}=-\frac{1}{3} \lambda^{2} W_{k i j l}^{Z} x^{k} x^{l}+\text { h.o.t. }=\lambda^{2} H_{i j}(x)+\text { h.o.t. }$$
In particular, we see that, at order $a^{4} \lambda^{4}=b^{4}$, the Weyl energy of $w$ in $B_{1} \backslash B_{\gamma}$ coincides with the Weyl energy of $g_{b}$ in $B_{1}$ (just compare (5.7) to (5.4)), therefore the two contributions cancel out in the energy balance (5.1).

As a consequence of the previous computations, in order to get the sign of energy balance we need to look at higher order terms in the expansion of $\dot{w}_{i j}$ at $|x|=1$ and $|x|=\gamma$ respectively. This will be carried out in the next subsections.

\subsection*{5.1 Higher order terms in energy balance: inner boundary component}

We now want to compute the higher order contributions coming from the integrals over $\partial B_{\gamma}$ of the Weyl energy expansion (5.7). By looking at (5.8), (5.9), (4.19), one sees that such contributions come from products of derivatives of $\hat{c}_{1}|x|^{-4}, \hat{c}_{2}|x|^{-2}$ and $\hat{c}_{3}|x|^{2}$-terms times derivatives of $\hat{c}_{2}|x|^{-2}$-terms, which generate integrals of order $\lambda^{2}$ and integrals of order 1. Next, we have contributions of higher order $\gamma^{2} \lambda^{2}$. To be more precise, if we look at the definition of $\dot{w}_{i j}$, then, using (4.1), (4.3), (4.5), (4.19) and the values of $v_{1}, v_{3}$ obtained in (4.12), (4.13), (4.17), (4.18) (look also at the proof of Lemma 5.5
in the Appendix), we can write $\dot{w}_{i j}$ as follows in $|x|=\gamma$ :
$$\begin{aligned}
\dot{w}_{i j}= & \frac{1}{|x|^{4}}\left(2 \gamma^{6} W_{k i j l}^{M} \frac{x^{k} x^{l}}{|x|^{2}}-\frac{2}{3} \lambda^{2} \gamma^{6} W_{k i j l}^{Z} \frac{x^{k} x^{l}}{|x|^{2}}\right)+O^{(3)}\left(\gamma^{8}\left(1+\lambda^{2}\right)|x|^{-4}\right) \\
& +\frac{1}{|x|^{2}}\left(-\frac{1}{3} W_{k i j l}^{M} \frac{x^{k} x^{l}}{|x|^{2}}-3 \gamma^{4} W_{k i j l}^{M} \frac{x^{k} x^{l}}{|x|^{2}}+\lambda^{2} \gamma^{4} W_{k i j l}^{Z} \frac{x^{k} x^{l}}{|x|^{2}}\right)+O^{(3)}\left(\gamma^{6}\left(1+\lambda^{2}\right)|x|^{-2}\right) \\
& +|x|^{2}\left(W_{k i j l}^{M} \frac{x^{k} x^{l}}{|x|^{2}}-\frac{1}{3} \lambda^{2} W_{k i j l}^{Z} \frac{x^{k} x^{l}}{|x|^{2}}\right)+O^{(3)}\left(\gamma^{4}\left(1+\lambda^{2}\right)|x|^{2}\right)+O^{(3)}\left(\left(1+\gamma^{4} \lambda^{2}\right)|x|^{4}\right) \\
= & -\frac{1}{3} W_{k i j l}^{M} \frac{x^{k} x^{l}}{|x|^{4}}+\left(\frac{2 \gamma^{6}}{|x|^{6}}-\frac{3 \gamma^{4}}{|x|^{4}}+1\right) W_{k i j l}^{M} x^{k} x^{l}+\lambda^{2}\left(-\frac{2 \gamma^{6}}{3|x|^{6}}+\frac{\gamma^{4}}{|x|^{4}}-\frac{1}{3}\right) W_{k i j l}^{Z} x^{k} x^{l}+\Psi_{\lambda, \gamma}(x),
\end{aligned}$$
where $\Psi_{\lambda, \gamma}(x)$ is a higher order error term satisfying $\left|\nabla^{k} \Psi_{\lambda, \gamma}(x)\right| \leq C \lambda^{2} \gamma^{4-k}$ for $|x|=\gamma$ and $k=0,1,2,3$. Looking at (5.13), we clearly see that the main term is given by $-\frac{1}{3} W_{k i j l}^{M} \frac{x^{k} x^{l}}{|x|^{4}}=F_{i j}(x)$ as already pointed out in (5.10), (5.11). It follows that the biggest terms in the expansion of integrals on $\partial B_{\gamma}$ of (5.7) will be given by products of derivatives of such term and it will be equal to (5.5). On the other hand, the next biggest term on $\partial B_{\gamma}$ is given by mixed terms and is of order $\lambda^{2}$ as in the following example:
Example 5.6. Consider for instance the integral
$$\int_{\partial B_{\gamma}} \partial_{\alpha \beta}^{2} \dot{w}_{i j} \partial_{\beta} \dot{w}_{i j} \nu^{\alpha} d \sigma,$$
which is one of the terms in (5.7). Then $\dot{w}_{i j}$ expands as in (5.13) and one has
$$\begin{aligned}
\int_{\partial B_{\gamma}} \partial_{\alpha \beta}^{2} \dot{w}_{i j} \partial_{\beta} \dot{w}_{i j} \nu^{\alpha} d \sigma & =\underbrace{\int_{\partial B_{\gamma}} \partial_{\alpha \beta}^{2}\left(-\frac{1}{3} W_{k i j l}^{M} \frac{x^{k} x^{l}}{|x|^{4}}\right) \partial_{\beta}\left(-\frac{1}{3} W_{k i j l}^{M} \frac{x^{k} x^{l}}{|x|^{4}}\right) \nu^{\alpha}}_{=C_{1} \gamma^{-4}} \\
& +\underbrace{\int_{\partial B_{\gamma}} \partial_{\alpha \beta}^{2}\left(-\frac{1}{3} W_{k i j l}^{M} \frac{x^{k} x^{l}}{|x|^{4}}\right) \partial_{\beta}\left(\lambda^{2}\left(-\frac{2 \gamma^{6}}{3|x|^{6}}+\frac{\gamma^{4}}{|x|^{4}}-\frac{1}{3}\right) W_{k i j l}^{Z} x^{k} x^{l}\right) \nu^{\alpha}}_{=C_{2} \lambda^{2}} \\
& +\underbrace{\int_{\partial B_{\gamma}} \partial_{\alpha \beta}^{2}\left(\lambda^{2}\left(-\frac{2 \gamma^{6}}{3|x|^{6}}+\frac{\gamma^{4}}{|x|^{4}}-\frac{1}{3}\right) W_{k i j l}^{Z} x^{k} x^{l}\right) \partial_{\beta}\left(-\frac{1}{3} W_{k i j l}^{M} \frac{x^{k} x^{l}}{|x|^{4}}\right) \nu^{\alpha}}_{=C_{3} \lambda^{2}} \\
& +\underbrace{\int_{\partial B_{\gamma}} \partial_{\alpha \beta}^{2}\left(-\frac{1}{3} W_{k i j l}^{M} \frac{x^{k} x^{l}}{|x|^{4}}\right) \partial_{\beta}\left(\left(\frac{2 \gamma^{6}}{|x|^{6}}-\frac{3 \gamma^{4}}{|x|^{4}}+1\right) W_{k i j l}^{M} x^{k} x^{l}\right) \nu^{\alpha}}_{=C_{4}} \\
& +\underbrace{\int_{\partial B_{\gamma}}}_{\partial_{\alpha \beta}^{2}\left(\left(\frac{2 \gamma^{6}}{|x|^{6}}-\frac{3 \gamma^{4}}{|x|^{4}}+1\right) W_{k i j l}^{M} x^{k} x^{l}\right) \partial_{\beta}\left(-\frac{1}{3} W_{k i j l}^{M} \frac{x^{k} x^{l}}{|x|^{4}}\right) \nu^{\alpha}}+O\left(\gamma^{2} \lambda^{2}\right),
\end{aligned}$$
where $C_{1}, \ldots, C_{5}$ are constants which depend on $i, j, \alpha, \beta$ and $W^{M}, W^{Z}$ (but not on $\gamma$ and $\lambda$ !). Similarly, if we consider the other type of integral in (5.7),
$$\int_{\partial B_{\gamma}} \dot{w}_{i j} \partial_{\alpha \beta \beta}^{3} \dot{w}_{i j} \nu^{\alpha} d \sigma$$
we obtain an expression which is similar to the one above (we only need to change the derivatives).

Remark 5.7. As it is clear from (5.14), the mixed terms of order $\lambda^{2}$ depend upon the interaction between the two Weyl tensors $W^{M}(p)$ and $W^{Z}(q)$ evaluated at their respective basepoints with respect to our choice of coordinates. On the other hand, the terms of order 1 only depend upon $W^{M}(p)$.

We now want to explicitly compute the term of order $\lambda^{2}$ for the inner integral
$$\begin{aligned}
\Phi_{\gamma}(w): & =\frac{1}{2} \sum_{i, j, \beta} \int_{\partial B_{\gamma}} \dot{w}_{i j} \partial_{\alpha \beta \beta}^{3} \dot{w}_{i j} \nu^{\alpha} d \sigma \\
& -\sum_{i, j, \beta} \int_{\partial B_{\gamma}}\left[\left(\partial_{i j}^{2} \dot{w}_{\alpha \beta}-2 \partial_{\beta j}^{2} \dot{w}_{i \alpha}+\partial_{\alpha \beta}^{2} \dot{w}_{i j}\right) \partial_{\beta} \dot{w}_{i j}-\frac{1}{2} \partial_{\beta \beta}^{2} \dot{w}_{i j} \partial_{\alpha} \dot{w}_{i j}\right] \nu^{\alpha} d \sigma
\end{aligned}$$
here we are assuming that the unit normal $\nu=\left(\nu^{1}, \ldots, \nu^{4}\right)$ is outward pointing.
To begin, we derive an expression for a generic term in the second line of (5.15):
Lemma 5.8. It holds
$$\begin{aligned}
\int_{\partial B_{\gamma}} \partial_{\alpha} \dot{w}_{i j} & \partial_{\beta \tau}^{2} \dot{w}_{s t} \nu^{\eta} d \sigma=\int_{\partial B_{\gamma}} \partial_{\alpha} F_{i j} \partial_{\beta \tau}^{2} F_{s t} \nu^{\eta} d \sigma \\
& +\frac{8}{3} \lambda^{2} \int_{\mathbb{S}^{3}} W_{\mu i j \nu}^{M} W_{k s t l}^{Z}\left(\delta_{\alpha}^{\mu} x^{\nu}+x^{\mu} \delta_{\alpha}^{\nu}-4 x^{\mu} x^{\nu} x_{\alpha}\right) x^{k} x^{l} x_{\beta} x_{\tau} x^{\eta} d \sigma+C+O\left(\gamma^{2} \lambda^{2}\right)
\end{aligned}$$
where $F_{i j}$ is given by (5.2) and $C=C\left(\alpha, \beta, \tau, i, j, s, t, \eta, W^{M}\right)$.
Proof. We start by computing the derivatives of the interacting terms of $\dot{w}_{i j}$ (cf. (5.13)): to begin, one has
$$\begin{aligned}
\partial_{\alpha}\left[\left(-\frac{2 \gamma^{6}}{3|x|^{6}}\right.\right. & \left.\left.+\frac{\gamma^{4}}{|x|^{4}}-\frac{1}{3}\right) W_{k i j l}^{Z} x^{k} x^{l}\right] \\
& =\left(4 \gamma^{6} \frac{x_{\alpha}}{|x|^{8}}-4 \gamma^{4} \frac{x_{\alpha}}{|x|^{6}}\right) W_{k i j l}^{Z} x^{k} x^{l}+\left(-\frac{2 \gamma^{6}}{3|x|^{6}}+\frac{\gamma^{4}}{|x|^{4}}-\frac{1}{3}\right) W_{k i j l}^{Z}\left(\delta_{\alpha}^{k} x^{l}+x^{k} \delta_{\alpha}^{l}\right) .
\end{aligned}$$

Remark 5.9. We notice that
$$\left.\left(-\frac{2 \gamma^{6}}{3|x|^{6}}+\frac{\gamma^{4}}{|x|^{4}}-\frac{1}{3}\right)\right|_{|x|=\gamma}=0, \quad \text { and }\left.\quad \partial_{\alpha}\left[\left(-\frac{2 \gamma^{6}}{3|x|^{6}}+\frac{\gamma^{4}}{|x|^{4}}-\frac{1}{3}\right) W_{k i j l}^{Z} x^{k} x^{l}\right]\right|_{|x|=\gamma}=0 .$$
As a consequence, we do not need to compute $\partial_{\alpha \beta}^{2}\left(-\frac{1}{3} W_{k i j l}^{M} \frac{x^{k} x^{l}}{|x|^{4}}\right)$ and $\partial_{\alpha \beta \beta}^{3}\left(-\frac{1}{3} W_{k i j l}^{M} \frac{x^{k} x^{l}}{|x|^{4}}\right)$ since these quantities will always be multiplied by zero in the end, cf. (5.14).

We then compute
$$\begin{aligned}
\partial_{\alpha \beta}^{2}\left[\left(-\frac{2 \gamma^{6}}{3|x|^{6}}\right.\right. & \left.\left.+\frac{\gamma^{4}}{|x|^{4}}-\frac{1}{3}\right) W_{k i j l}^{Z} x^{k} x^{l}\right]=\left(4 \gamma^{6} \frac{\delta_{\alpha \beta}}{|x|^{8}}-32 \gamma^{6} \frac{x_{\alpha} x_{\beta}}{|x|^{10}}-4 \gamma^{4} \frac{\delta_{\alpha \beta}}{|x|^{6}}+24 \gamma^{4} \frac{x_{\alpha} x_{\beta}}{|x|^{8}}\right) W_{k i j l}^{Z} x^{k} x^{l} \\
& +\left(4 \gamma^{6} \frac{x_{\alpha}}{|x|^{8}}-4 \gamma^{4} \frac{x_{\alpha}}{|x|^{6}}\right) W_{k i j l}^{Z}\left(\delta_{\beta}^{k} x^{l}+x^{k} \delta_{\beta}^{l}\right)+\left(4 \gamma^{6} \frac{x_{\beta}}{|x|^{8}}-4 \gamma^{4} \frac{x_{\beta}}{|x|^{6}}\right) W_{k i j l}^{Z}\left(\delta_{\alpha}^{k} x^{l}+x^{k} \delta_{\alpha}^{l}\right) \\
& +\left(-\frac{2 \gamma^{6}}{3|x|^{6}}+\frac{\gamma^{4}}{|x|^{4}}-\frac{1}{3}\right) W_{k i j l}^{Z}\left(\delta_{\alpha}^{k} \delta_{\beta}^{l}+\delta_{\beta}^{k} \delta_{\alpha}^{l}\right)
\end{aligned}$$
so that
$$\left.\partial_{\alpha \beta}^{2}\left[\left(-\frac{2 \gamma^{6}}{3|x|^{6}}+\frac{\gamma^{4}}{|x|^{4}}-\frac{1}{3}\right) W_{k i j l}^{Z} x^{k} x^{l}\right]\right|_{|x|=\gamma}=-8 \frac{x_{\alpha} x_{\beta}}{\gamma^{4}} W_{k i j l}^{Z} x^{k} x^{l} .$$

Since we will need it later on, we also compute the third derivative:
$$\begin{aligned}
\partial_{\alpha \beta \beta}^{3}\left[\left(-\frac{2 \gamma^{6}}{3|x|^{6}}\right.\right. & \left.\left.+\frac{\gamma^{4}}{|x|^{4}}-\frac{1}{3}\right) W_{k i j l}^{Z} x^{k} x^{l}\right]\left.\right|_{|x|=\gamma}=\left(-16 \frac{x_{\beta} \delta_{\alpha \beta}}{\gamma^{4}}-8 \frac{x_{\alpha}}{\gamma^{4}}+128 \frac{x_{\alpha}\left(x_{\beta}\right)^{2}}{\gamma^{6}}\right) W_{k i j l}^{Z} x^{k} x^{l} \\
& -16 \frac{x_{\alpha} x_{\beta}}{\gamma^{4}} W_{k i j l}^{Z}\left(\delta_{\beta}^{k} x^{l}+x^{k} \delta_{\beta}^{l}\right)-8 \frac{\left(x_{\beta}\right)^{2}}{\gamma^{4}} W_{k i j l}^{Z}\left(\delta_{\alpha}^{k} x^{l}+x^{k} \delta_{\alpha}^{l}\right)
\end{aligned}$$
Finally, one has
$$\partial_{\alpha}\left(-\frac{1}{3} W_{k i j l}^{M} \frac{x^{k} x^{l}}{|x|^{4}}\right)=-\frac{1}{3} W_{k i j l}^{M}\left(\frac{\delta_{\alpha}^{k} x^{l}+x^{k} \delta_{\alpha}^{l}}{|x|^{4}}-4 \frac{x^{k} x^{l} x_{\alpha}}{|x|^{6}}\right) .$$

Arguing now as in (5.14) and using (5.13), (5.17), (5.18) and (5.20) one has
$$\begin{aligned}
\int_{\partial B_{\gamma}} \partial_{\alpha} \dot{w}_{i j} \partial_{\beta \tau}^{2} \dot{w}_{s t} \nu^{\eta} d \sigma & =\int_{\partial B_{\gamma}} \partial_{\alpha}\left(-\frac{1}{3} W_{\mu i j \nu}^{M} \frac{x^{\mu} x^{\nu}}{|x|^{4}}\right) \partial_{\beta \tau}^{2}\left(-\frac{1}{3} W_{k s t l}^{M} \frac{x^{k} x^{l}}{|x|^{4}}\right) \nu^{\eta} d \sigma \\
+\lambda^{2} \int_{\partial B_{\gamma}} \partial_{\alpha} & \left(-\frac{1}{3} W_{\mu i j \nu}^{M} \frac{x^{\mu} x^{\nu}}{|x|^{4}}\right) \partial_{\beta \tau}^{2}\left[\left(-\frac{2 \gamma^{6}}{3|x|^{6}}+\frac{\gamma^{4}}{|x|^{4}}-\frac{1}{3}\right) W_{k s t l}^{Z} x^{k} x^{l}\right] \nu^{\eta} d \sigma+C+O\left(\lambda^{2} \gamma^{2}\right) \\
& =\int_{\partial B_{\gamma}} \partial_{\alpha} F_{i j} \partial_{\beta \tau}^{2} F_{s t} \nu^{\eta} d \sigma \\
+ & \frac{8}{3} \lambda^{2} \int_{\partial B_{\gamma}} W_{\mu i j \nu}^{M} W_{k s t l}^{Z}\left(\frac{\delta_{\alpha}^{\mu} x^{\nu}+x^{\mu} \delta_{\alpha}^{\nu}}{\gamma^{4}}-4 \frac{x^{\mu} x^{\nu} x_{\alpha}}{\gamma^{6}}\right) \gamma^{-4} x_{\beta} x_{\tau} x^{k} x^{l} \nu^{\eta} d \sigma+C+O\left(\lambda^{2} \gamma^{2}\right)
\end{aligned}$$
and now a change of variables in the second integral gives us (5.16). \(\square\)

We can now expand (5.15):
Lemma 5.10. Let $\Phi_{\gamma}(w)$ be defined as in (5.15); then:
$$\Phi_{\gamma}(w)=a^{-4} \int_{\mathbb{R}^{4} \backslash B_{\gamma}}\left|W^{g_{a}}\right|^{2} d V_{g_{a}}-\frac{2}{9} \pi^{2} \lambda^{2} W^{M}(p) \circledast W^{Z}(q)+C+O\left(\lambda^{2} \gamma^{2}\right)+O\left(a^{2}\right)$$
where $C=C\left(W^{M}(p)\right)$ and $W^{M}(p) \circledast W^{Z}(q)$ is defined in (1.7) (here with $M$ in place of $\bar{M}$ ).
Proof. As in the proof of Lemma 5.8, we can use (5.13), (5.17) and (5.19) and argue as in (5.14) to obtain
$$\begin{aligned}
& \int_{\partial B_{\gamma}} \dot{w}_{i j} \partial_{\alpha \beta \beta}^{3} \dot{w}_{i j} \nu^{\alpha} d \sigma=\int_{\partial B_{\gamma}} F_{i j} \partial_{\alpha \beta \beta}^{3} F_{i j} \nu^{\alpha} d \sigma \\
&+\lambda^{2} \int_{\partial B_{\gamma}} F_{i j} \partial_{\alpha \beta \beta}^{3}\left[\left(-\frac{2 \gamma^{6}}{3|x|^{6}}+\frac{\gamma^{4}}{|x|^{4}}-\frac{1}{3}\right) W_{k i j l}^{Z} x^{k} x^{l}\right] \nu^{\alpha} d \sigma+C+O\left(\lambda^{2} \gamma^{2}\right) \\
&= \int_{\partial B_{\gamma}} F_{i j} \partial_{\alpha \beta \beta}^{3} F_{i j} \nu^{\alpha} d \sigma+\lambda^{2} \int_{\partial B_{\gamma}} F_{i j}\left[\left(-16 \frac{x_{\beta} \delta_{\alpha \beta}}{\gamma^{4}}-8 \frac{x_{\alpha}}{\gamma^{4}}+128 \frac{x_{\alpha}\left(x_{\beta}\right)^{2}}{\gamma^{6}}\right) W_{k i j l}^{Z} x^{k} x^{l}\right. \\
&\left.-16 \frac{x_{\alpha} x_{\beta}}{\gamma^{4}} W_{k i j l}^{Z}\left(\delta_{\beta}^{k} x^{l}+x^{k} \delta_{\beta}^{l}\right)-8 \frac{\left(x_{\beta}\right)^{2}}{\gamma^{4}} W_{k i j l}^{Z}\left(\delta_{\alpha}^{k} x^{l}+x^{k} \delta_{\alpha}^{l}\right)\right] \nu^{\alpha} d \sigma+C+O\left(\lambda^{2} \gamma^{2}\right) \\
&= \int_{\partial B_{\gamma}} F_{i j} \partial_{\alpha \beta \beta}^{3} F_{i j} \nu^{\alpha} d \sigma+\frac{8}{3} \lambda^{2} \int_{\partial B_{\gamma}} W_{\mu i j \nu}^{M} W_{k i j l}^{Z} \frac{x^{\mu} x^{\nu}}{\gamma^{8}}\left[\left(2 x_{\beta} \delta_{\alpha \beta}+x_{\alpha}-16 \frac{x_{\alpha}\left(x_{\beta}\right)^{2}}{\gamma^{2}}\right) x^{k} x^{l}\right. \\
&\left.+2 x_{\alpha} x_{\beta}\left(\delta_{\beta}^{k} x^{l}+x^{k} \delta_{\beta}^{l}\right)+\left(x_{\beta}\right)^{2}\left(\delta_{\alpha}^{k} x^{l}+x^{k} \delta_{\alpha}^{l}\right)\right] \nu^{\alpha} d \sigma+C+O\left(\lambda^{2} \gamma^{2}\right) \\
&= \int_{\partial B_{\gamma}} F_{i j} \partial_{\alpha \beta \beta}^{3} F_{i j} \nu^{\alpha} d \sigma+\frac{8}{3} \lambda^{2} \Xi_{i, j, \beta}+C+O\left(\lambda^{2} \gamma^{2}\right)
\end{aligned}$$
where $C=C\left(i, j, \beta, W^{M}\right)$. Now, being $\nu^{\alpha}=x^{\alpha} \gamma^{-1}$ and $|x|=\gamma$, summing over $\alpha$ we got
$$\begin{aligned}
\Xi_{i, j, \beta} & =\int_{\partial B_{\gamma}} W_{\mu i j \nu}^{M} W_{k i j l}^{Z} \frac{x^{\mu} x^{\nu}}{\gamma^{9}}\left[\left(2\left(x_{\beta}\right)^{2}+\gamma^{2}-16\left(x_{\beta}\right)^{2}\right) x^{k} x^{l}+2 \gamma^{2} x_{\beta}\left(\delta_{\beta}^{k} x^{l}+x^{k} \delta_{\beta}^{l}\right)+2\left(x_{\beta}\right)^{2} x^{k} x^{l}\right] d \sigma \\
& =\int_{\partial B_{\gamma}} W_{\mu i j \nu}^{M} W_{k i j l}^{Z} \frac{x^{\mu} x^{\nu}}{\gamma^{9}}\left[-12\left(x_{\beta}\right)^{2} x^{k} x^{l}+\gamma^{2} x^{k} x^{l}+2 \gamma^{2} x_{\beta}\left(\delta_{\beta}^{k} x^{l}+x^{k} \delta_{\beta}^{l}\right)\right] d \sigma
\end{aligned}$$
Summing now over $i, j, \beta$ and changing variables we find
$$\sum_{i, j, \beta} \Xi_{i, j, \beta}=-\frac{4}{\gamma^{7}} \sum_{i, j} \int_{\partial B_{\gamma}} W_{\mu i j \nu}^{M} W_{k i j l}^{Z} x^{\mu} x^{\nu} x^{k} x^{l} d \sigma=-4 \sum_{i, j} \int_{\mathbb{S}^{3}} W_{\mu i j \nu}^{M} W_{k i j l}^{Z} z^{\mu} z^{\nu} z^{k} z^{l} d \sigma_{\mathbb{S}^{3}}(z)$$
Using the identity (see e.g. [Bre08, Corollary 29])
$$\int_{\mathbb{S}^{3}} z^{\mu} z^{\nu} z^{k} z^{l} d \sigma=\frac{\pi^{2}}{12}\left(\delta^{\mu \nu} \delta^{k l}+\delta^{\mu k} \delta^{\nu l}+\delta^{\mu l} \delta^{\nu k}\right)$$
one gets
$$\begin{aligned}
\sum_{i, j, \beta} \Xi_{i, j, \beta} & =-\frac{\pi^{2}}{3}\left[\sum_{i, j, \mu, k} W_{\mu i j \mu}^{M} W_{k i j k}^{Z}+\sum_{i, j, k, l}\left(W_{k i j l}^{M} W_{k i j l}^{Z}+W_{l i j k}^{M} W_{k i j l}^{Z}\right)\right] \\
& =-\frac{\pi^{2}}{3} W^{M} \circledast W^{Z},
\end{aligned}$$
where in the last step we used the definition (1.7) of $\circledast$ and the trace-free property of $W$. From this last equation and (5.21) we thus have
$$\sum_{i, j, \beta} \int_{\partial B_{\gamma}} \dot{w}_{i j} \partial_{\alpha \beta \beta}^{3} \dot{w}_{i j} \nu^{\alpha} d \sigma=\sum_{i, j, \beta} \int_{\partial B_{\gamma}} F_{i j} \partial_{\alpha \beta \beta}^{3} F_{i j} \nu^{\alpha} d \sigma-\frac{8}{9} \pi^{2} \lambda^{2} W^{M} \circledast W^{Z}+C+O\left(\lambda^{2} \gamma^{2}\right)$$
where $C=C\left(W^{M}\right)$.
We now compute the terms in the second line of (5.15). Using (5.16), we see that:
$$\begin{aligned}
\sum_{i, j, \beta} \int_{\partial B_{\gamma}} \partial_{\beta} \dot{w}_{i j} \partial_{i j}^{2} \dot{w}_{\alpha \beta} \nu^{\alpha} d \sigma= & \sum_{i, j, \beta} \int_{\partial B_{\gamma}} \partial_{\beta} F_{i j} \partial_{i j}^{2} F_{\alpha \beta} \nu^{\alpha} d \sigma \\
& +\frac{8}{3} \lambda^{2} \sum_{i, j, \beta} \int_{\mathbb{S}^{3}}\left(W_{\beta i j \nu}^{M} W_{k \alpha \beta l}^{Z} x^{\nu}+W_{\mu i j \beta}^{M} W_{k \alpha \beta l}^{Z} x^{\mu}\right) x^{k} x^{l} x_{i} x_{j} x^{\alpha} d \sigma \\
& -\frac{32}{3} \lambda^{2} \sum_{i, j, \beta} \int_{\mathbb{S}^{3}} W_{\mu i j \nu}^{M} W_{k \alpha \beta l}^{Z} x^{\mu} x^{\nu} x_{\beta} x^{k} x^{l} x_{i} x_{j} x^{\alpha} d \sigma+C+O\left(\lambda^{2} \gamma^{2}\right) \\
= & \sum_{i, j, \beta} \int_{\partial B_{\gamma}} \partial_{\beta} F_{i j} \partial_{i j}^{2} F_{\alpha \beta} \nu^{\alpha} d \sigma+C+O\left(\lambda^{2} \gamma^{2}\right)
\end{aligned}$$
Here in the last step we used the symmetries of curvature type tensors, e.g., for $\beta, i$ fixed one has $\sum_{j, \nu} W_{\beta i j \nu}^{M} x_{j} x_{\nu}=W^{M}\left(\partial_{\beta}, \partial_{i}, x, x\right)=0$, where $x=\left(x_{1}, \ldots, x_{4}\right)$.

Arguing in the same way, we also see that
$$\sum_{i, j, \beta} \int_{\partial B_{\gamma}} \partial_{\beta} \dot{w}_{i j} \partial_{\beta j}^{2} \dot{w}_{i \alpha} \nu^{\alpha} d \sigma=\sum_{i, j, \beta} \int_{\partial B_{\gamma}} \partial_{\beta} F_{i j} \partial_{\beta j}^{2} F_{i \alpha} \nu^{\alpha} d \sigma+C+O\left(\lambda^{2} \gamma^{2}\right)$$

Using again (5.16) one has
$$\begin{aligned}
\sum_{i, j, \beta} \int_{\partial B_{\gamma}} \partial_{\beta} \dot{w}_{i j} \partial_{\alpha \beta}^{2} \dot{w}_{i j} \nu^{\alpha} d \sigma & =\sum_{i, j, \beta} \int_{\partial B_{\gamma}} \partial_{\beta} F_{i j} \partial_{\alpha \beta}^{2} F_{i j} \nu^{\alpha} d \sigma \\
& -\frac{16}{3} \lambda^{2} \sum_{i, j} \int_{\mathbb{S}^{3}} W_{\mu i j \nu}^{M} W_{k i j l}^{Z} x^{\mu} x^{\nu} x^{k} x^{l} d \sigma+C+O\left(\lambda^{2} \gamma^{2}\right)
\end{aligned}$$
so that, after recalling (5.22), we get
$$\sum_{i, j, \beta} \int_{\partial B_{\gamma}} \partial_{\beta} \dot{w}_{i j} \partial_{\alpha \beta}^{2} \dot{w}_{i j} \nu^{\alpha} d \sigma=\sum_{i, j, \beta} \int_{\partial B_{\gamma}} \partial_{\beta} F_{i j} \partial_{\alpha \beta}^{2} F_{i j} \nu^{\alpha} d \sigma-\frac{4}{9} \pi^{2} \lambda^{2} W^{M} \circledast W^{Z}+C+O\left(\lambda^{2} \gamma^{2}\right)$$
Using the same method, one also sees that
$$\sum_{i, j, \beta} \int_{\partial B_{\gamma}} \partial_{\alpha} \dot{w}_{i j} \partial_{\beta \beta}^{2} \dot{w}_{i j} \nu^{\alpha} d \sigma=\sum_{i, j, \beta} \int_{\partial B_{\gamma}} \partial_{\alpha} F_{i j} \partial_{\beta \beta}^{2} F_{i j} \nu^{\alpha} d \sigma-\frac{4}{9} \pi^{2} \lambda^{2} W^{M} \circledast W^{Z}+C+O\left(\lambda^{2} \gamma^{2}\right)$$

Finally, substituting (5.23), (5.24), (5.25), (5.26) and (5.27) inside (5.15), the conclusion follows after recalling (5.5). \(\square\)

\subsection*{5.2 Higher order terms in energy balance: outer boundary component}

It remains to compute the contribution to the expansion of $\mathcal{W}(w)$ coming from the integrals over $\partial B_{1}$ of (5.7). The procedure is the same adopted in the previous subsection.

Looking at the definition of $\dot{w}_{i j}$ (5.6) and using (4.1), (4.3), (4.5), (4.8), (4.9), (4.19) and the values of $v_{1}, v_{3}$ coming from (4.12), (4.13), (4.17), (4.18) we can write $\dot{w}_{i j}(x)$ as follows for $|x|=1$ :
$$\begin{aligned}
\dot{w}_{i j}= & \frac{1}{|x|^{2}}\left(-\frac{1}{3} W_{k i j l}^{M} \frac{x^{k} x^{l}}{|x|^{2}}\right)+|x|^{2}\left(W_{k i j l}^{M} \frac{x^{k} x^{l}}{|x|^{2}}-\frac{1}{3} \lambda^{2} W_{k i j l}^{Z} \frac{x^{k} x^{l}}{|x|^{2}}\right) \\
& +|x|^{4}\left(-\frac{2}{3} W_{k i j l}^{M} \frac{x^{k} x^{l}}{|x|^{2}}\right)+\Upsilon_{\lambda, \gamma}(x) \\
= & \left(-\frac{1}{3|x|^{4}}+1-\frac{2}{3}|x|^{2}\right) W_{k i j l}^{M} x^{k} x^{l}-\frac{1}{3} \lambda^{2} W_{k i j l}^{Z} x^{k} x^{l}+\Upsilon_{\lambda, \gamma}(x)
\end{aligned}$$
where $\Upsilon_{\lambda, \gamma}(x)$ is an higher order error term such that $\left|\nabla^{k} \Upsilon_{\lambda, \gamma}(x)\right| \leq C \gamma^{4} \lambda^{2}$ for $|x|=1$ and $k=0,1,2,3$.

We now want to use (5.28) in order to compute
$$\begin{aligned}
\Phi_{1}(w): & =-\frac{1}{2} \sum_{i, j, \beta} \int_{\partial B_{1}} \dot{w}_{i j} \partial_{\alpha \beta \beta}^{3} \dot{w}_{i j} \nu^{\alpha} d \sigma \\
& +\sum_{i, j, \beta} \int_{\partial B_{1}}\left[\left(\partial_{i j}^{2} \dot{w}_{\alpha \beta}-2 \partial_{\beta j}^{2} \dot{w}_{i \alpha}+\partial_{\alpha \beta}^{2} \dot{w}_{i j}\right) \partial_{\beta} \dot{w}_{i j}-\frac{1}{2} \partial_{\beta \beta}^{2} \dot{w}_{i j} \partial_{\alpha} \dot{w}_{i j}\right] \nu^{\alpha} d \sigma ;
\end{aligned}$$
here we are always assuming the unit normal $\nu=\left(\nu^{1}, \ldots, \nu^{4}\right)$ to be outward pointing.
First, we need an analogue of Lemma 5.8:

Lemma 5.11. It holds
$$\begin{aligned}
\int_{\partial B_{1}} \partial_{\alpha} \dot{w}_{i j} \partial_{\beta \tau}^{2} \dot{w}_{s t} \nu^{\eta} d \sigma & =\lambda^{4} \int_{\partial B_{1}} \partial_{\alpha} H_{i j} \partial_{\beta \tau}^{2} H_{s t} \nu^{\eta} d \sigma \\
& +\frac{8}{3} \lambda^{2} \int_{\mathbb{S}^{3}} W_{\mu i j \nu}^{Z} W_{k s t l}^{M}\left(\delta_{\alpha}^{\mu} x^{\nu}+x^{\mu} \delta_{\alpha}^{\nu}\right) x^{k} x^{l} x_{\beta} x_{\tau} x^{\eta} d \sigma+O\left(\lambda^{4} \gamma^{4}\right)
\end{aligned}$$
where $H_{i j}$ is given by (5.2).
Proof. Differentiating the components of $\dot{w}_{i j}$ given by (5.28) and evaluating at $|x|=1$ we see that:
$$\begin{aligned}
\partial_{\alpha}\left[\left(-\frac{1}{3|x|^{4}}+1-\frac{2}{3}|x|^{2}\right)\right. & \left.W_{k i j l}^{M} x^{k} x^{l}\right]=\left(\frac{4}{3} \frac{x_{\alpha}}{|x|^{6}}-\frac{4}{3} x_{\alpha}\right) W_{k i j l}^{M} x^{k} x^{l} \\
& +\left(-\frac{1}{3|x|^{4}}+1-\frac{2}{3}|x|^{2}\right) W_{k i j l}^{M}\left(\delta_{\alpha}^{k} x^{l}+x_{k} \delta_{\alpha}^{l}\right)
\end{aligned}$$
so in particular
$$\left.\left(-\frac{1}{3|x|^{4}}+1-\frac{2}{3}|x|^{2}\right) W_{k i j l}^{M} x^{k} x^{l}\right|_{|x|=1}=0,\left.\quad \partial_{\alpha}\left[\left(-\frac{1}{3|x|^{4}}+1-\frac{2}{3}|x|^{2}\right) W_{k i j l}^{M} x^{k} x^{l}\right]\right|_{|x|=1}=0 .$$
We then have
$$\begin{aligned}
\partial_{\alpha \beta}^{2}\left[\left(-\frac{1}{3|x|^{4}}+\right.\right. & \left.\left.1-\frac{2}{3}|x|^{2}\right) W_{k i j l}^{M} x^{k} x^{l}\right]=\left(\frac{4}{3} \frac{\delta_{\alpha \beta}}{|x|^{6}}-8 \frac{x_{\alpha} x_{\beta}}{|x|^{8}}-\frac{4}{3} \delta_{\alpha \beta}\right) W_{k i j l}^{M} x^{k} x^{l} \\
& +\left(\frac{4}{3} \frac{x_{\alpha}}{|x|^{6}}-\frac{4}{3} x_{\alpha}\right) W_{k i j l}^{M}\left(\delta_{\beta}^{k} x^{l}+x^{k} \delta_{\beta}^{l}\right)+\left(\frac{4}{3} \frac{x_{\beta}}{|x|^{6}}-\frac{4}{3} x_{\beta}\right) W_{k i j l}^{M}\left(\delta_{\alpha}^{k} x^{l}+x^{k} \delta_{\alpha}^{l}\right) \\
& +\left(-\frac{1}{3|x|^{4}}+1-\frac{2}{3}|x|^{2}\right) W_{k i j l}^{M}\left(\delta_{\alpha}^{k} \delta_{\beta}^{l}+\delta_{\beta}^{k} \delta_{\alpha}^{l}\right)
\end{aligned}$$
from which one gets
$$\left.\partial_{\alpha \beta}^{2}\left[\left(-\frac{1}{3|x|^{4}}+1-\frac{2}{3}|x|^{2}\right) W_{k i j l}^{M} x^{k} x^{l}\right]\right|_{|x|=1}=-8 W_{k i j l}^{M} x^{k} x^{l} x_{\alpha} x_{\beta},$$
and
$$\begin{gathered}
\left.\partial_{\alpha \beta \beta}^{3}\left[\left(-\frac{1}{3|x|^{4}}+1-\frac{2}{3}|x|^{2}\right) W_{k i j l}^{M} x^{k} x^{l}\right]\right|_{|x|=1}=\left(-16 \delta_{\alpha \beta} x_{\beta}-8 x_{\alpha}+64 x_{\alpha}\left(x_{\beta}\right)^{2}\right) W_{k i j l}^{M} x^{k} x^{l} \\
-16 x_{\alpha} x_{\beta} W_{k i j l}^{M}\left(\delta_{\beta}^{k} x^{l}+x^{k} \delta_{\beta}^{l}\right)-8\left(x_{\beta}\right)^{2} W_{k i j l}^{M}\left(\delta_{\alpha}^{k} x^{l}+x^{k} \delta_{\alpha}^{l}\right)
\end{gathered}$$
Finally, using (5.28), (5.31) and (5.32), one obtains (5.30). \(\square\)

We can now compute the expansion of (5.29):
Lemma 5.12. Let $\Phi_{1}(w)$ be as in (5.29); then
$$\Phi_{1}(w)=a^{-4} \int_{B_{1}}\left|W^{g_{b}}\right|^{2} d V_{g_{b}}-\frac{2}{9} \pi^{2} \lambda^{2} W^{M}(p) \circledast W^{Z}(q)+O\left(\lambda^{4} \gamma^{4}\right)+O\left(b^{2}\right)$$
where $W^{M}(p) \circledast W^{Z}(q)$ is defined in (1.7).

Proof. Using (5.28) and (5.33), we can compute
$$\begin{gathered}
\int_{\partial B_{1}} \dot{w}_{i j} \partial_{\alpha \beta \beta}^{3} \dot{w}_{i j} \nu^{\alpha} d \sigma=\lambda^{4} \int_{\partial B_{1}} H_{i j} \partial_{\alpha \beta \beta}^{3} H_{i j} \nu^{\alpha} d \sigma+\lambda^{2} \int_{\partial B_{1}} H_{i j}\left[-8\left(x_{\beta}\right)^{2} W_{k i j l}^{M}\left(\delta_{\alpha}^{k} x^{l}+x^{k} \delta_{\alpha}^{l}\right)\right. \\
\left.\left(-16 \delta_{\alpha \beta} x_{\beta}-8 x_{\alpha}+64 x_{\alpha}\left(x_{\beta}\right)^{2}\right) W_{k i j l}^{M} x^{k} x^{l}-16 x_{\alpha} x_{\beta} W_{k i j l}^{M}\left(\delta_{\beta}^{k} x^{l}+x^{k} \delta_{\beta}^{l}\right)\right] x^{\alpha} d \sigma+O\left(\lambda^{4} \gamma^{4}\right) \\
=\lambda^{4} \int_{\partial B_{1}} H_{i j} \partial_{\alpha \beta \beta}^{3} H_{i j} \nu^{\alpha} d \sigma+\frac{8}{3} \lambda^{2} \int_{\mathbb{S}^{3}} W_{\mu i j \nu}^{Z} W_{k i j l}^{M} x^{\mu} x^{\nu}\left[2\left(x_{\beta}^{2}\right) x^{k} x^{l}\right. \\
\left.+\left(2\left(x_{\beta}\right)^{2}+1-8\left(x_{\beta}\right)^{2}\right) x^{k} x^{l}+2 x_{\beta}\left(\delta_{\beta}^{k} x^{l}+x^{k} \delta_{\beta}^{l}\right)\right] d \sigma+O\left(\lambda^{4} \gamma^{4}\right) \\
=: \lambda^{4} \int_{\partial B_{1}} H_{i j} \partial_{\alpha \beta \beta}^{3} H_{i j} \nu^{\alpha} d \sigma+\frac{8}{3} \lambda^{2} \Theta_{i, j, \beta}+O\left(\lambda^{4} \gamma^{4}\right)
\end{gathered}$$
Summing over $i, j, \beta$, one has
$$\sum_{i, j, \beta} \Theta_{i, j, \beta}=4 \sum_{i, j} \int_{\mathbb{S}^{3}} W_{\mu i j \nu}^{Z} W_{k i j l}^{M} x^{\mu} x^{\nu} x^{k} x^{l} d \sigma=\frac{\pi^{2}}{3} W^{M} \circledast W^{Z}$$
where the last equality follows from (5.22). Hence
$$\sum_{i, j, \beta} \int_{\partial B_{1}} \dot{w}_{i j} \partial_{\alpha \beta \beta}^{3} \dot{w}_{i j} \nu^{\alpha} d \sigma=\lambda^{4} \sum_{i, j, \beta} \int_{\partial B_{1}} H_{i j} \partial_{\alpha \beta \beta}^{3} H_{i j} \nu^{\alpha} d \sigma+\frac{8}{9} \pi^{2} \lambda^{2} W^{M} \circledast W^{Z}+O\left(\lambda^{4} \gamma^{4}\right)$$
Now, by applying Lemma 5.11 we see that
$$\begin{aligned}
\sum_{i, j, \beta} \int_{\partial B_{1}} \partial_{\beta} \dot{w}_{i j} \partial_{i j}^{2} \dot{w}_{\alpha \beta} \nu^{\alpha} d \sigma & =\lambda^{4} \sum_{i, j, \beta} \int_{\partial B_{1}} \partial_{\beta} H_{i j} \partial_{i j}^{2} H_{\alpha \beta} \nu^{\alpha} d \sigma \\
+\frac{8}{3} \lambda^{2} & \sum_{i, j, \beta} \int_{\partial B_{1}}\left(W_{\beta i j \nu}^{Z} W_{k \alpha \beta l}^{M} x^{\nu}+W_{\mu i j \beta}^{Z} W_{k \alpha \beta l}^{M} x^{\mu}\right) x^{k} x^{l} x_{i} x_{j} x^{\alpha} d \sigma+O\left(\lambda^{4} \gamma^{4}\right) \\
& =\lambda^{4} \sum_{i, j, \beta} \int_{\partial B_{1}} \partial_{\beta} F_{i j} \partial_{i j}^{2} F_{\alpha \beta} \nu^{\alpha} d \sigma+O\left(\lambda^{4} \gamma^{4}\right)
\end{aligned}$$
where in the last step we used the skew-symmetry of $W$. Similarly,
$$\sum_{i, j, \beta} \int_{\partial B_{1}} \partial_{\beta} \dot{w}_{i j} \partial_{\beta j}^{2} \dot{w}_{i \alpha} \nu^{\alpha} d \sigma=\lambda^{4} \sum_{i, j, \beta} \int_{\partial B_{1}} \partial_{\beta} H_{i j} \partial_{\beta j}^{2} H_{i \alpha} \nu^{\alpha} d \sigma+O\left(\lambda^{4} \gamma^{4}\right)$$
Moreover, by Lemma 5.11 and (5.22) we also have
$$\begin{aligned}
\sum_{i, j, \beta} \int_{\partial B_{1}} \partial_{\beta} \dot{w}_{i j} \partial_{\alpha \beta}^{2} \dot{w}_{i j} \nu^{\alpha} d \sigma= & \lambda^{4} \sum_{i, j, \beta} \int_{\partial B_{1}} \partial_{\beta} H_{i j} \partial_{\alpha \beta}^{2} H_{i j} \nu^{\alpha} d \sigma \\
& +\frac{16}{3} \lambda^{2} \sum_{i, j} \int_{\mathbb{S}^{3}} W_{\mu i j \nu}^{Z} W_{k i j l}^{M} x^{\mu} x^{\nu} x^{k} x^{l} d \sigma+O\left(\lambda^{4} \gamma^{4}\right) \\
= & \lambda^{4} \sum_{i, j, \beta} \int_{\partial B_{1}} \partial_{\beta} H_{i j} \partial_{\alpha \beta}^{2} H_{i j} \nu^{\alpha} d \sigma+\frac{4}{9} \pi^{2} \lambda^{2} W^{M} \circledast W^{Z}+O\left(\lambda^{4} \gamma^{4}\right)
\end{aligned}$$
and
$$\sum_{i, j, \beta} \int_{\partial B_{1}} \partial_{\alpha} \dot{w}_{i j} \partial_{\beta \beta}^{2} \dot{w}_{i j} \nu^{\alpha} d \sigma=\lambda^{4} \sum_{i, j, \beta} \int_{\partial B_{1}} \partial_{\alpha} H_{i j} \partial_{\beta \beta}^{2} H_{i j} \nu^{\alpha} d \sigma+\frac{4}{9} \pi^{2} \lambda^{2} W^{M} \circledast W^{Z}+O\left(\lambda^{4} \gamma^{4}\right)$$
Finally, substituting (5.34), (5.35), (5.36), (5.37) and (5.38) inside (5.29) and recalling (5.4) we conclude our proof. \(\square\)

\subsection*{5.3 Computation of the energy balance}

We now want to prove the following result:
Proposition 5.13. Assume $0<a \ll \gamma \ll \lambda^{-1}<1$. Then
$$\mathcal{W}^{X}\left(g_{X}\right)-\mathcal{W}^{M}\left(g_{M}\right)-\mathcal{W}^{Z}\left(g_{Z}\right)=a^{4}\left(-\frac{4}{9} \pi^{2} \lambda^{2} W^{M}(p) \circledast W^{Z}(q)+C+O\left(\lambda^{2} \gamma^{2}\right)\right)+O\left(a^{\frac{9}{2}} \gamma^{-5}\right),$$
where $C$ is a constant depending on $W^{M}(p)$.
Proof. By definition of $g_{X}$ (cf. (3.14)) we have $g_{X} \equiv w$ in $B_{1} \backslash B_{\gamma}$. Moreover, it holds
$$\mathcal{W}(w)=\int_{B_{1} \backslash B_{\gamma}}\left|W^{g_{X}}\right|^{2} d V_{g_{X}}=a^{4}\left(\Phi_{\gamma}(w)+\Phi_{1}(w)\right)+O\left(a^{6}\right)$$
see (5.7), (5.15), (5.29). As a consequence, by virtue of (5.4), (5.5), Lemma 5.10 and Lemma 5.12, formula (5.1) turns into
$$\begin{aligned}
& \mathcal{W}^{X}\left(g_{X}\right)-\mathcal{W}^{M}\left(g_{M}\right)-\mathcal{W}^{Z}\left(g_{Z}\right)=a^{4}\left(-\frac{4}{9} \pi^{2} \lambda^{2} W^{M}(p) \circledast W^{Z}(q)+C+O\left(\lambda^{2} \gamma^{2}\right)\right)+O\left(a^{6}\right) \\
& +\int_{\left(B_{1+\sqrt{a}} \backslash B_{1}\right) \cup\left(B_{\gamma} \backslash B_{\gamma-\sqrt{a}}\right)}\left|W^{g_{X}}\right|^{2} d V_{g_{X}}-\int_{B_{1+\sqrt{a}} \backslash B_{1}}\left|W^{g_{b}}\right|^{2} d V_{g_{b}}-\int_{B_{\gamma} \backslash B_{\gamma-\sqrt{a}}}\left|W^{g_{a}}\right|^{2} d V_{g_{a}}
\end{aligned}$$
The Proposition now follows from the next Lemma. \(\square\)

Lemma 5.14. Assume $0<a \ll \gamma \ll \lambda^{-1}<1$. Then
$$\int_{\left(B_{1+\sqrt{a}} \backslash B_{1}\right) \cup\left(B_{\gamma} \backslash B_{\gamma-\sqrt{a}}\right)}\left|W^{g_{X}}\right|^{2} d V_{g_{X}}+\int_{B_{1+\sqrt{a}} \backslash B_{1}}\left|W^{g_{b}}\right|^{2} d V_{g_{b}}+\int_{B_{\gamma} \backslash B_{\gamma-\sqrt{a}}}\left|W^{g_{a}}\right|^{2} d V_{g_{a}} \leq C \frac{a^{\frac{9}{2}}}{\gamma^{5}},$$
for a suitable constant $C>0$ which does not depend upon $a, \gamma, \lambda$.
Proof. To begin recall that, in local coordinates, one has
$$R_{i j k l}=\left(\partial_{i} \Gamma_{j k}^{s}-\partial_{j} \Gamma_{i k}^{s}\right) g_{s l}+\left(\Gamma_{j k}^{s} \Gamma_{i s}^{t}-\Gamma_{i k}^{s} \Gamma_{j s}^{t}\right) g_{t l},$$
where
$$\begin{gathered}
\Gamma_{i j}^{k}=\frac{1}{2} g^{k s}\left(\partial_{i} g_{j s}+\partial_{j} g_{i s}-\partial_{s} g_{i j}\right) \\
\partial_{l} \Gamma_{i j}^{k}=\frac{1}{2}\left(\partial_{l} g^{k s}\right)\left(\partial_{i} g_{j s}+\partial_{j} g_{i s}-\partial_{s} g_{i j}\right)+\frac{1}{2} g^{k s}\left(\partial_{i l}^{2} g_{j s}+\partial_{j l}^{2} g_{i s}-\partial_{s l}^{2} g_{i j}\right) .
\end{gathered}$$
As a consequence, one has $\left|R_{i j k l}\right| \leq C\left(\left|\nabla g^{-1}\right||\nabla g|+|\nabla g|^{2}+\left|\nabla^{2} g\right|\right)$, where the gradients and norms are taken with respect to the Euclidean metric, and $C=C\left(|g|,\left|g^{-1}\right|\right)$. Moreover, by writing the Weyl tensor in local coordinates (see (2.9)), one also has the same type of estimate for $W^{g}$. Hence
$$\left|W^{g}\right|_{g}^{2}=W^{i j k l} W_{i j k l} \leq C\left(\left|\nabla g^{-1}\right|^{2}|\nabla g|^{2}+|\nabla g|^{4}+\left|\nabla^{2} g\right|^{2}\right),$$
always with a suitable $C=C\left(|g|,\left|g^{-1}\right|\right)$. Taking now as $\left\{x^{i}\right\}$ the (conformal) normal coordinates at $q$ for the scaled metric $b^{-2} g_{Z}$, then the metrics $g_{b}$ and $g_{a}$ expand as in (3.4) and (3.9) respectively, so that (5.41) holds (for both $g_{a}$ and $g_{b}$ ) in the region $\{\gamma / 2 \leq|x| \leq 2\}$ with a constant $C$ which does not depend on $a, b \ll 1$ (we need $a, b$ small in order for the expansions to hold in such region).

Now, by (3.9), (3.10) one has that
$$\left|\nabla g_{a}\right| \leq C \frac{a^{2}}{|x|^{3}}, \quad \quad\left|\nabla g_{a}^{-1}\right| \leq C \frac{a^{2}}{|x|^{3}}, \quad\left|\nabla^{2} g_{a}\right| \leq C \frac{a^{2}}{|x|^{4}}, \quad \text { for }|x| \geq \frac{\gamma}{2}$$
(the second estimate actually follows by writing $g_{a}^{-1}$ as a Neumann series and noticing that it has an expansion similar to that of $g_{a}$ ). Applying (5.42) together with (5.41), one has
$$\begin{aligned}
\int_{B_{\gamma} \backslash B_{\gamma-\sqrt{a}}}\left|W^{g_{a}}\right|^{2} d V_{g_{a}} & \leq C \int_{B_{\gamma} \backslash B_{\gamma-\sqrt{a}}}\left(\frac{a^{8}}{|x|^{12}}+\frac{a^{4}}{|x|^{8}}\right) d x \leq C a^{4} \int_{B_{\gamma} \backslash B_{\gamma-\sqrt{a}}}|x|^{-8} d x \\
& =-\frac{\tilde{C}}{4} a^{4}\left(\frac{1}{\gamma^{4}}-\frac{1}{\gamma^{4}\left(1-\frac{\sqrt{a}}{\gamma}\right)^{4}}\right)=-\frac{\tilde{C}}{4} a^{4}\left(-4 \frac{\sqrt{a}}{\gamma^{5}}+O\left(\frac{a}{\gamma^{6}}\right)\right) \leq C \frac{a^{\frac{9}{2}}}{\gamma^{5}}
\end{aligned}$$
where we used the fact that $a \ll \gamma$.
Similarly, by (3.4), (3.5) one has
$$\left|\nabla g_{b}\right| \leq C b^{2}|x|, \quad\left|\nabla g_{b}^{-1}\right| \leq C b^{2}|x|, \quad\left|\nabla^{2} g_{b}\right| \leq C b^{2}, \quad \text { for }|x| \leq 2,$$
and coupling those estimates with (5.41) one gets
$$\int_{B_{1+\sqrt{a}} \backslash B_{1}}\left|W^{g_{b}}\right|^{2} d V_{g_{b}} \leq C \int_{B_{1+\sqrt{a}} \backslash B_{1}}\left(b^{8}|x|^{4}+b^{4}\right) d x \leq C b^{4}\left((1+\sqrt{a})^{4}-1\right) \leq C b^{4} \sqrt{a}=C a^{\frac{9}{2}} \lambda^{4}$$

We now turn our attention to the error term of $g_{X}$; by (3.12) we know that, in $\gamma-\sqrt{a} \leq|x| \leq \gamma$ one has
$$\begin{aligned}
\nabla\left(\left(g_{X}\right)_{i j}\right)(x) & =-\frac{1}{3} a^{2} W_{k i j l}^{M} \nabla\left(\frac{x^{k} x^{l}}{|x|^{4}}\right)-\chi_{a}^{\prime}(\gamma-|x|) \frac{x}{|x|} \zeta_{i j}^{a}(x)+\chi_{a}(\gamma-|x|) \nabla \zeta_{i j}^{a}(x), \\
\nabla^{2}\left(\left(g_{X}\right)_{i j}\right)(x) & =-\frac{1}{3} a^{2} W_{k i j l}^{M} \nabla^{2}\left(\frac{x^{k} x^{l}}{|x|^{4}}\right)+\left(\chi_{a}^{\prime \prime}(\gamma-|x|) \frac{x \otimes x}{|x|^{2}}-\chi_{a}^{\prime}(\gamma-|x|) \nabla^{2}(|x|)\right) \zeta_{i j}^{a}(x) \\
& -\chi_{a}^{\prime}(\gamma-|x|)\left(\frac{x}{|x|} \otimes \nabla \zeta_{i j}^{a}(x)+\nabla \zeta_{i j}^{a}(x) \otimes \frac{x}{|x|}\right)+\chi_{a}(\gamma-|x|) \nabla^{2} \zeta_{i j}^{a}(x) .
\end{aligned}$$
Moreover, writing $g_{X}^{-1}$ as a Neumann series one finds that, for $\gamma-\sqrt{a} \leq|x| \leq \gamma$,
$$\left(g_{X}^{-1}\right)_{i j}(x)=\delta_{i j}+\frac{1}{3} a^{2} W_{k i j l}^{M} \frac{x^{k} x^{l}}{|x|^{4}}-\zeta_{i j}^{a}(x) \chi_{a}(\gamma-|x|)+\vartheta_{i j}^{a}(x),$$
where
$$\left|\vartheta_{i j}^{a}(x)\right||x|^{3}+\left|\nabla \vartheta_{i j}^{a}(x)\right||x|^{4}+\left|\nabla^{2} \vartheta_{i j}^{a}(x)\right||x|^{5} \leq C a^{3},$$
(recall that $a \ll \gamma$ ). Using these formulae together with (3.10), (3.11), one finds, for $\gamma-\sqrt{a} \leq|x| \leq \gamma$,
$$\left|\nabla g_{X}\right| \leq C \frac{a^{2}}{|x|^{3}}, \quad \quad\left|\nabla g_{X}^{-1}\right| \leq C \frac{a^{2}}{|x|^{3}}, \quad \quad\left|\nabla^{2} g_{X}\right| \leq C \frac{a^{2}}{|x|^{4}}$$
We can now argue as for (5.43) to conclude that
$$\int_{B_{\gamma} \backslash B_{\gamma-\sqrt{a}}}\left|W^{g_{X}}\right|^{2} d V_{g_{X}} \leq C \frac{a^{\frac{9}{2}}}{\gamma^{5}}$$
Finally, a similar argument in the region $1 \leq|x| \leq 1+\sqrt{a}$ also shows that
$$\int_{B_{1+\sqrt{a}} \backslash B_{1}}\left|W^{g_{X}}\right|^{2} d V_{g_{X}} \leq C b^{4} \sqrt{a}=C a^{\frac{9}{2}} \lambda^{4}$$
This concludes our proof. \(\square\)

\section*{6 Proof of Theorem 1.1}

We now want to employ Proposition 5.13 to prove Theorem 1.1. This amounts to study the sign of (5.39) and hence the sign of the interaction term (1.7), which we recall is
$$W^{M}(p) \circledast W^{Z}(q)=\sum_{i, j, k, l} W_{k i j l}^{Z}(q)\left(W_{k i j l}^{M}(p)+W_{l i j k}^{M}(p)\right) .$$
To begin, we show that, by using our freedom to relatively rotate the normal coordinate systems, we can rewrite (6.1) as a multiple of the scalar product between $W^{M}(p)$ and $W^{Z}(q)$ :

Lemma 6.1. For a suitable choice of (conformal) normal coordinates at $p$ and $q$, one has
$$W^{M}(p) \circledast W^{Z}(q)=\frac{3}{2} \sum_{i, j, k, l} W_{k i j l}^{M}(p) W_{k i j l}^{Z}(q) .$$
Proof. $W^{M}(p)$ can be regarded as a trace-free symmetric endomorphism $\widehat{W}^{M}(p)$ on $\Lambda^{2}\left(T_{p}^{*} M\right)$ which preserves the spaces $\Lambda_{ \pm}^{2}\left(T_{p}^{*} M\right)$ (see Section 2). As a consequence, we can diagonalize $\widehat{W}^{M}(p)$ by choosing an orthogonal basis of eigenforms $\left\{\omega^{+}, \eta^{+}, \vartheta^{+}, \omega^{-}, \eta^{-}, \vartheta^{-}\right\}$, such that $\left\{\omega^{+}, \eta^{+}, \vartheta^{+}\right\}$is a basis for $\Lambda_{+}^{2}\left(T_{p}^{*} M\right)$ and $\left\{\omega^{-}, \eta^{-}, \vartheta^{-}\right\}$is a basis for $\Lambda_{-}^{2}\left(T_{p}^{*} M\right)$. Even more, by [Der83, Lemma 2] we know that, given any oriented orthogonal basis $\left\{\omega^{+}, \eta^{+}, \vartheta^{+}\right\}$for $\Lambda_{+}^{2}\left(T_{p}^{*} M\right)$ and any oriented orthogonal basis $\left\{\omega^{-}, \eta^{-}, \vartheta^{-}\right\}$for $\Lambda_{-}^{2}\left(T_{p}^{*} M\right)$ whose vectors have all length $\sqrt{2}$, then there exists an oriented orthonormal basis $\left\{e_{1}, \ldots, e_{4}\right\}$ for $T_{p} M$ such that
$$\begin{array}{ll}
\omega^{+}=e^{1} \wedge e^{2}+e^{3} \wedge e^{4} & \omega^{-}=e^{1} \wedge e^{2}-e^{3} \wedge e^{4} \\
\eta^{+}=e^{1} \wedge e^{3}+e^{4} \wedge e^{2} & \eta^{-}=e^{1} \wedge e^{3}-e^{4} \wedge e^{2} \\
\vartheta^{+}=e^{1} \wedge e^{4}+e^{2} \wedge e^{3} & \vartheta^{-}=e^{1} \wedge e^{4}-e^{2} \wedge e^{3} .
\end{array}$$
Here $\left\{e^{1}, \ldots e^{4}\right\}$ is the dual basis and the orientation on $\Lambda_{ \pm}^{2}$ is the one induced by $M$. If we now choose normal coordinates in $p$ such that $\left.\partial_{i}\right|_{p}=e_{i} \forall i=1, \ldots, 4$, then $\widehat{W}_{ \pm}^{M}(p)$ are diagonalized with respect to the associated bases (6.3) for $\Lambda_{ \pm}^{2}\left(T_{p}^{*} M\right)$.

Clearly, we can do the exact same thing for $W^{Z}(q)$.
As a consequence, when we identify the orthonormal bases for $T_{p} M$ and $T_{q} Z$ during the gluing procedure (i.e. we implicitly have $\left.\partial_{i}^{M}\right|_{p}=e_{i}=\left.\partial_{i}^{Z}\right|_{q}$ from (3.8)), we then find out that $\widehat{W}_{ \pm}^{M}(p)$ and $\widehat{W}_{ \pm}^{Z}(q)$ are simultaneously diagonalized by the bases (6.3). We are now in position to apply [GV16, Lemma 12.2] (the assumption about simultaneous diagonalization is stated at the beginning of Section 12.1), which readily implies (6.2). \(\square\)

It is now possible to study the sign of (6.1):
Lemma 6.2. Consider normal coordinates at $p \in M$ and $q \in Z$ as in the proof of Lemma 6.1. Then, if $M$ and $Z$ are not locally conformally flat and not one self-dual and the other anti-self-dual, one has
$$W^{M}(p) \circledast W^{Z}(q)>0$$
for a suitable choice of the basepoints $p \in M$ and $q \in Z$.
Proof. In the orthogonal eigenbases for $T_{p} M$ and $T_{q} Z$ (6.3) given by the previous lemma,
$\widehat{W}^{M}:=\widehat{W}^{M}(p)$ and $\widehat{W}^{Z}:=\widehat{W}^{Z}(q)$ write down as follows:
$$\begin{aligned}
\widehat{W} M=\frac{1}{2}\left(\lambda_{M}^{+} \omega^{+} \otimes \omega_{b}^{+}+\right. & \left.\mu_{M}^{+} \eta^{+} \otimes \eta_{b}^{+}+\nu_{M}^{+} \vartheta^{+} \otimes \vartheta_{b}^{+}\right) \\
& \quad+\frac{1}{2}\left(\lambda_{M}^{-} \omega^{-} \otimes \omega_{b}^{-}+\mu_{M}^{-} \eta^{-} \otimes \eta_{b}^{-}+\nu_{M}^{-} \vartheta^{-} \otimes \vartheta_{b}^{-}\right) \\
\widehat{W}^{Z}=\frac{1}{2}\left(\lambda_{Z}^{+} \omega^{+} \otimes \omega_{b}^{+}+\right. & \left.\mu_{Z}^{+} \eta^{+} \otimes \eta_{b}^{+}+\nu_{Z}^{+} \vartheta^{+} \otimes \vartheta_{b}^{+}\right) \\
& \quad+\frac{1}{2}\left(\lambda_{Z}^{-} \omega^{-} \otimes \omega_{b}^{-}+\mu_{Z}^{-} \eta^{-} \otimes \eta_{b}^{-}+\nu_{Z}^{-} \vartheta^{-} \otimes \vartheta_{b}^{-}\right)
\end{aligned}$$
where $\lambda_{M}^{ \pm}, \mu_{M}^{ \pm}, \nu_{M}^{ \pm}$and $\lambda_{Z}^{ \pm}, \mu_{Z}^{ \pm}, \nu_{Z}^{ \pm}$denote the corresponding eigenvalues and, e.g., $\omega_{b}$ is the 2-vector corresponding to $\omega$ through the scalar product on the tangent (that is, the Euclidean one). In virtue of the trace-free property of $W_{ \pm}^{M}$ and $W_{ \pm}^{Z}$, one has
$$\lambda_{M}^{ \pm}+\mu_{M}^{ \pm}+\nu_{M}^{ \pm}=0 \quad \text { and } \quad \lambda_{Z}^{ \pm}+\mu_{Z}^{ \pm}+\nu_{Z}^{ \pm}=0$$
moreover,
$$\begin{gathered}
\left(\lambda_{M}^{ \pm}\right)^{2}+\left(\mu_{M}^{ \pm}\right)^{2}+\left(\nu_{M}^{ \pm}\right)^{2}=\left\|\widehat{W}_{ \pm}^{M}\right\|^{2}=\frac{1}{4}\left|W_{ \pm}^{M}\right|^{2} \\
\left(\lambda_{Z}^{ \pm}\right)^{2}+\left(\mu_{Z}^{ \pm}\right)^{2}+\left(\nu_{Z}^{ \pm}\right)^{2}=\left\|\widehat{W}_{ \pm}^{Z}\right\|^{2}=\frac{1}{4}\left|W_{ \pm}^{Z}\right|^{2}
\end{gathered}$$
where $\|\cdot\|$ denotes the induced operator norm on 2-forms. Without loss of generality, assume also that the eigenvalues satisfy
$$\lambda_{M}^{ \pm} \geq \mu_{M}^{ \pm} \geq \nu_{M}^{ \pm}, \quad \lambda_{Z}^{ \pm} \geq \mu_{Z}^{ \pm} \geq \nu_{Z}^{ \pm} ;$$
this is due to the fact that we can generate all possible permutations of each triple of eigenvalues by a orientation-preserving change of basis (we first permute the basis of 2-forms and then apply [Der83, Lemma 2] as in the previous Lemma in order to get the basis for the tangent).

By (6.2),
$$\begin{aligned}
W^{M}(p) \circledast W^{Z}(q) & =\frac{3}{2} \sum_{i, j, k, l} W_{k i j l}^{M}(p) W_{k i j l}^{Z}(q)=\frac{3}{2}\left\langle W^{M}, W^{Z}\right\rangle=6\left\langle\widehat{W}^{M}, \widehat{W}^{Z}\right\rangle \\
& =6\left(\lambda_{M}^{+} \lambda_{Z}^{+}+\mu_{M}^{+} \mu_{Z}^{+}+\nu_{M}^{+} \nu_{Z}^{+}+\lambda_{M}^{-} \lambda_{Z}^{-}+\mu_{M}^{-} \mu_{Z}^{-}+\nu_{M}^{-} \nu_{Z}^{-}\right) .
\end{aligned}$$
Consider then
$$\lambda_{M}^{ \pm} \lambda_{Z}^{ \pm}+\mu_{M}^{ \pm} \mu_{Z}^{ \pm}+\nu_{M}^{ \pm} \nu_{Z}^{ \pm}=\left(\lambda_{M}^{ \pm}, \mu_{M}^{ \pm}, \nu_{M}^{ \pm}\right) \cdot\left(\lambda_{Z}^{ \pm}, \mu_{Z}^{ \pm}, \nu_{Z}^{ \pm}\right)=: v_{1} \cdot v_{2}=\left|v_{1} \| v_{2}\right| \cos (\vartheta),$$
where $\vartheta$ is the angle between the two vectors. By (6.5), $v_{1}$ and $v_{2}$ belong to the plane $\pi=\left\{x_{1}+x_{2}+x_{3}=\right.$ $0\}$, while, by virtue of (6.7), we further have that $v_{1}$ and $v_{2}$ lie inside the cone sector of $\pi$ whose edges are given by the lines of directions $\frac{1}{\sqrt{6}}(1,1,-2)$ and $\frac{1}{\sqrt{6}}(2,-1,-1)$ respectively. Thus the opening angle of the cone is equal to $\arccos \left(\frac{1}{2}\right)=\frac{\pi}{3}$. As a consequence of this and (6.6) one has
$$\left.\lambda_{M}^{ \pm} \lambda_{Z}^{ \pm}+\mu_{M}^{ \pm} \mu_{Z}^{ \pm}+\nu_{M}^{ \pm} \nu_{Z}^{ \pm} \geq \frac{1}{2}\left|\left(\lambda_{M}^{ \pm}, \mu_{M}^{ \pm}, \nu_{M}^{ \pm}\right)\right|\left|\left(\lambda_{Z}^{ \pm}, \mu_{Z}^{ \pm}, \nu_{Z}^{ \pm}\right)\right|=\frac{1}{2} \right\rvert\,\left\|\widehat{W}_{ \pm}^{M}\right\|\left\|\widehat{W}_{ \pm}^{Z}\right\| .$$
Now, inasmuch as $M$ and $Z$ are not locally conformally flat and not one self-dual and the other anti-self-dual, by the previous equation, (6.8) and a suitable choice of $p$ and $q$, we immediately get (6.4). \(\square\)

Proof of Theorem 1.1. As already pointed out in Remark 3.5, the manifold $X$ defined in Section 3 is diffeomorphic to $Z \# \bar{M}$. Conversely, if we perform the same gluing procedure with $\bar{M}$ in place of $M$, we end up with a manifold $Y$ satisfying $Y \stackrel{\text { diff }}{\cong} Z \# M$. Applying now Proposition 5.13 in this setting, we have
$$\begin{aligned}
\mathcal{W}^{Y}\left(g_{Y}\right)-\mathcal{W}^{M}\left(g_{M}\right)-\mathcal{W}^{Z}\left(g_{Z}\right) & =\mathcal{W}^{Y}\left(g_{Y}\right)-\mathcal{W}^{\bar{M}}\left(g_{M}\right)-\mathcal{W}^{Z}\left(g_{Z}\right) \\
& =a^{4} \underbrace{\left(C-\frac{4}{9} \pi^{2} \lambda^{2} W^{\bar{M}}(p) \circledast W^{Z}(q)+O\left(\lambda^{2} \gamma^{2}\right)\right)}_{:=E_{\lambda, \gamma}}+O\left(a^{\frac{9}{2}} \gamma^{-5}\right),
\end{aligned}$$
where $C=C\left(W^{\bar{M}}(p)\right)$. Being $W_{ \pm}^{M}=W_{\mp}^{\bar{M}}$, if $M$ and $Z$ are not both self-dual or both anti-self-dual, then $\bar{M}$ and $Z$ are not one self-dual and the other anti-self-dual; hence we can apply Lemma 6.2 to get
$$W^{\bar{M}}(p) \circledast W^{Z}(q)>0 .$$
We can now fix $\lambda>0$ large enough to have e.g.
$$C-\frac{4}{9} \pi^{2} \lambda^{2} W^{\bar{M}}(p) \circledast W^{Z}(q)<-2 .$$
It is then possible to fix $0<\gamma \ll \lambda$ such that ((4.19) holds and) $E_{\lambda, \gamma}<-1$. After that, we fix $0<a<\gamma$ such that the RHS of (6.9) is negative. This shows that $g_{Y}$ satisfies (1.5).

Finally, by a density argument we also get a smooth metric $\tilde{g}_{Y}$ still satisfying (1.5). \(\square\)

\section*{A Appendix}

Proof of (3.2). Letting $I(z)=\frac{z}{|z|^{2}}=: y$ denote the inversion map and $y=\left(y^{1}, \ldots, y^{4}\right)$ the inverted conformal normal coordinates, from (3.1) and the definition of $F$ we got
$$\begin{aligned}
g_{N} & =(F \circ I)^{2} I^{*}\left(\left[\delta_{\alpha \beta}-\frac{1}{3} W_{k \alpha \beta l} z^{k} z^{l}+O^{(3)}\left(|z|^{3}\right)\right] d z^{\alpha} d z^{\beta}\right) \\
& =\left(|y|^{2}\right)^{2}\left(\delta_{\alpha \beta}-\frac{1}{3} W_{k \alpha \beta l} \frac{y^{k} y^{l}}{|y|^{4}}+O^{(3)}\left(|y|^{-3}\right)\right) \frac{1}{|y|^{2}}\left(\delta_{s}^{\alpha}-2 \frac{y^{\alpha} y_{s}}{|y|^{2}}\right) d y^{s} \frac{1}{|y|^{2}}\left(\delta_{t}^{\beta}-2 \frac{y^{\beta} y_{t}}{|y|^{2}}\right) d y^{t}
\end{aligned}$$
where we used
$$I^{*}\left(d z^{\alpha}\right)=d\left(\frac{y^{\alpha}}{|y|^{2}}\right)=\frac{d y^{\alpha}}{|y|^{2}}-2 \frac{y^{\alpha}(y \cdot d y)}{|y|^{4}}=\frac{1}{|y|^{2}}\left(\delta_{s}^{\alpha}-2 \frac{y^{\alpha} y_{s}}{|y|^{2}}\right) d y^{s} .$$
From the above expression, we see that
$$\begin{gathered}
\left(g_{N}\right)_{i j}=\delta_{i j}-\frac{1}{3} W_{k i j l} \frac{y^{k} y^{l}}{|y|^{4}}-\frac{2}{|y|^{2}}\left(\delta_{\alpha j} y^{\alpha} y^{i}+\delta_{i \beta} y^{\beta} y^{j}\right)+\frac{4}{|y|^{4}} \delta_{\alpha \beta} y^{\alpha} y^{\beta} y^{i} y^{j}+\frac{2}{3} W_{k \alpha j l} \frac{y^{k} y^{l}}{|y|^{6}}\left(y^{\alpha} y^{i}\right) \\
+\frac{2}{3} W_{k i \beta l} \frac{y^{k} y^{l}}{|y|^{6}}\left(y^{\beta} y^{j}\right)-\frac{4}{3} W_{k \alpha \beta l} \frac{y^{k} y^{l}}{|y|^{8}}\left(y^{\alpha} y^{\beta} y^{i} y^{j}\right)+O^{(3)}\left(|y|^{-3}\right) .
\end{gathered}$$
However, the third term in the above expression simplifies with the fourth one and the last three terms are all zero due to the symmetries of curvature type tensors. \(\square\)

Proof of Lemma 5.5. The proof is straightforward but tedious: all we have to do is rewrite each $\dot{w}_{i j}$ as a linear combination of terms similar to those of $H_{i j}$ or $F_{i j}$ defined in (5.2).

Case $i=j$ : by (5.6), the expression (4.3) for $w_{i i}$ and formulae (4.8), (4.9) for the radial functions, we see that $\dot{w}_{i i}$ is equal to
$$\dot{w}_{i i}=a^{-2} \sum_{\sigma=1}^{4}\left(\frac{c_{\sigma, s, t}}{|x|^{e(\sigma)}} \varphi_{s, t}+\frac{c_{\sigma, s, u}}{|x|^{e(\sigma)}} \varphi_{s, u}+\frac{c_{\sigma, t, u}}{|x|^{e(\sigma)}} \varphi_{t, u}+\frac{\tilde{c}_{\sigma, s, u}}{|x|^{e(\sigma)}} \psi_{s, u}+\frac{\tilde{c}_{\sigma, t, u}}{|x|^{e(\sigma)}} \psi_{t, u}\right),$$
where $e(1)=4, e(2)=2, e(3)=-2, e(4)=-4$ and $\{s, t, u\}$ are the other three distinct indices in $\{1,2,3,4\}$ which are different from $i$. Moreover, by (4.14) we know that $\forall \sigma, \alpha, \beta$ one has
$$\begin{aligned}
& a^{-2} c_{\sigma, \alpha, \beta}=C_{1, \sigma, \gamma} v_{1, \alpha, \beta}+C_{2, \sigma, \gamma} v_{2, \alpha, \beta}+C_{3, \sigma, \gamma} v_{3, \alpha, \beta}+C_{4, \sigma, \gamma} v_{4, \alpha, \beta} \\
& a^{-2} \tilde{c}_{\sigma, \alpha, \beta}=C_{1, \sigma, \gamma} \tilde{v}_{1, \alpha, \beta}+C_{2, \sigma, \gamma} \tilde{v}_{2, \alpha, \beta}+C_{3, \sigma, \gamma} \tilde{v}_{3, \alpha, \beta}+C_{4, \sigma, \gamma} \tilde{v}_{4, \alpha, \beta}
\end{aligned}$$
where the $C_{d, \sigma, \gamma}$ are constants which do not depend upon the indices $\alpha, \beta$ (and do not depend upon the tilde). Hence $\dot{w}_{i i}$ is a linear combination of terms $T_{i i}=T_{i i}(\sigma, d, \gamma)$ of the following type:
$$T_{i i}=\frac{v_{d, s, t}}{|x|^{m}} \varphi_{s, t}+\frac{v_{d, s, u}}{|x|^{m}} \varphi_{s, u}+\frac{v_{d, t, u}}{|x|^{m}} \varphi_{t, u}+\frac{\tilde{v}_{d, s, u}}{|x|^{m}} \psi_{s, u}+\frac{\tilde{v}_{d, t, u}}{|x|^{m}} \psi_{t, u},$$
where $d=1, \ldots, 4$ and $m=m(\sigma) \in\{4,2,-2,-4\}$. Taking the values of $v_{d, \alpha, \beta}$ from (4.12), (4.13) and writing up the spherical harmonics in polynomial form, one finds the following expression:
$$T_{i i}=\bar{C}\left(2 W_{s i i t} \frac{x_{s} x_{t}}{|x|^{m+2}}+2 W_{s i i u} \frac{x_{s} x_{u}}{|x|^{m+2}}+2 W_{t i i u} \frac{x_{t} x_{u}}{|x|^{m+2}}+W_{s i i s} \frac{x_{s}^{2}-x_{u}^{2}}{|x|^{m+2}}+W_{t i i t} \frac{x_{t}^{2}-x_{u}^{2}}{|x|^{m+2}}\right),$$
where $\bar{C}=\bar{C}\left(\sigma, d, \gamma, \lambda^{2}\right)$ is a multiplicative constant (notice that it does not depend on $i$ ). Using the trace-free property of Weyl tensor we can write $T_{i i}$ as
$$T_{i i}=\bar{C} W_{k i i l} \frac{x^{k} x^{l}}{|x|^{m+2}}$$

Case $i \neq j$ : similarly to the previous case, by (5.6), the expression (4.5) for $w_{i j}$ and (4.8), (4.9), (4.14), one sees that $\dot{w}_{i j}$ can be written as a linear combination of terms $T_{i j}=T_{i j}(\sigma, d, \gamma)$ of type
$$T_{i j}=\frac{v_{d, j, i}}{|x|^{m}} \varphi_{j, i}+\frac{v_{d, j, s}}{|x|^{m}} \varphi_{j, s}+\frac{v_{d, j, t}}{|x|^{m}} \varphi_{j, t}+\frac{v_{d, s, i}}{|x|^{m}} \varphi_{s, i}+\frac{v_{d, t, i}}{|x|^{m}} \varphi_{t, i}+\frac{v_{d, s, t}}{|x|^{m}} \varphi_{s, t}+\frac{\tilde{v}_{d, s, t}}{|x|^{m}} \psi_{s, t},$$
where $s, t$ denote the remaining two indices in $\{1,2,3,4\}$ distinct from $i, j$, and, again, $d=1, \ldots, 4$ and $m=m(\sigma) \in\{4,2,-2,-4\}$. Taking the values of $v_{s, \alpha, \beta}$ from (4.17), (4.18) and using the trace-free property of $W$ one finds that
$$T_{i j}=\bar{C} W_{k i j l} \frac{x^{k} x^{l}}{|x|^{m+2}},$$
where the $\bar{C}$ 's are the same constants of above.
By (A.1) and (A.2), we see that $\dot{w}$ can be written as a linear combination of tensors of type $T(m)$, where
$$T(m)_{i j}:=W_{k i j l} \frac{x^{k} x^{l}}{|x|^{m+2}}, \quad m \in\{4,2,-2,-4\} .$$
As a consequence, if we show that $T(m)$ is TT for any choice of $m$, then $\dot{w}$ will also be TT by linearity of the trace and divergence. The trace-free property of $T(m)$ follows from that of the Weyl tensor.

For the divergence, one has
$$\begin{aligned}
\delta(T(m))_{j} & =\sum_{i} \partial_{i}\left(W_{k i j l} \frac{x^{k} x^{l}}{|x|^{m+2}}\right)=\sum_{i} W_{k i j l} \frac{\delta_{i}^{k} x^{l}+x^{k} \delta_{i}^{l}}{|x|^{m+2}}-(m+2) \sum_{i} W_{k i j l} \frac{x^{k} x^{l} x_{i}}{|x|^{m+4}} \\
& =\frac{1}{|x|^{m+2}} \sum_{i}\left(W_{i i j l} x^{l}+W_{k i j i} x^{k}\right)-\frac{m+2}{|x|^{m+4}} W_{k i j l} x^{k} x^{i} x^{l}=0 .
\end{aligned}$$
This concludes the proof. \(\square\)