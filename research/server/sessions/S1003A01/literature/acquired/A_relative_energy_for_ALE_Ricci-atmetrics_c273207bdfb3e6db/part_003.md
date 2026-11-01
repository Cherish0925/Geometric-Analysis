---
retention_scope: session
part: 3
total_parts: 4
---

[Part 3/4 of: A relative energy for ALE Ricci-atmetrics]

Remark 6.8. This is the first order version of the inequality
$$\left|\lambda_{\mathrm{ALE}}(g)\right| \leq C\left\|\nabla \lambda_{\mathrm{ALE}}(g)\right\|_{L_{\frac{n}{2}+1}^{2}}^{2},$$
which is an $L_{\frac{n}{2}+1}^{2}$-Lojasiewicz inequality with optimal exponent $\theta=1$.

Proof. Let us prove inequality (6.18) for functions on $\left(N^{n}, g_{b}\right)$ first. Let $u \in C_{\tau}^{2}(N)$ which implies in particular that for any $\tau^{\prime}<\tau, \Delta_{g_{b}} u \in L_{\tau^{\prime}+2}^{2}$ and $u \in L_{\tau^{\prime}}^{2}$. Let us now assume that $\tau>\frac{n}{2}-1$ which naturally implies that $u \in L_{\frac{n}{2}-1}^{2}, \nabla^{g_{b}} u \in L_{\frac{n}{2}}^{2}$ and $\Delta_{g_{b}} u \in L_{\frac{n}{2}+1}^{2}$. By Cauchy-Schwarz inequality, we have $\left\langle-\Delta_{g_{b}} u, u\right\rangle_{L^{2}} \leq\left\|\Delta_{g_{b}} u\right\|_{L_{\frac{n}{2}+1}^{2}}\|u\|_{L_{\frac{n}{2}-1}^{2}}$. Now, by Hardy's inequality from Theorem 1.7, we get
$$\|u\|_{L_{\frac{n}{2}-1}^{2}}^{2}=\left\|\rho_{g_{b}}^{-1} u\right\|_{L_{\frac{n}{2}}^{2}}^{2} \leq C\left\|\nabla^{g_{b}} u\right\|_{L^{2}}^{2}=C\left\langle-\Delta_{g_{b}} u, u\right\rangle_{L^{2}} .$$

Therefore,
$$\left\langle-\Delta_{g_{b}} u, u\right\rangle_{L^{2}} \leq C\left(n, \tau, g_{b}\right)\left\|\Delta_{g_{b}} u\right\|_{L_{\frac{n}{2}+1}^{2}}\left\langle-\Delta_{g_{b}} u, u\right\rangle_{L^{2}}^{\frac{1}{2}} .$$

Now, notice that the proof goes almost verbatim for symmetric 2-tensors $h \in C_{\tau}^{2}\left(S^{2} T^{*} N\right)$ such that $\|h\|_{C_{\tau}^{0}} \leq 1$. Notice also that it is sufficient to restrict to tensors orthogonal to $\operatorname{ker}_{L^{2}} L_{g_{b}}$.

Indeed, by Cauchy-Schwarz inequality, $\left\langle-L_{g_{b}} h, h\right\rangle_{L^{2}} \leq\left\|L_{g_{b}} h\right\|_{L_{\frac{n}{2}+1}^{2}}\|h\|_{L_{\frac{n}{2}-1}^{2}}$. On the one hand, by following the same reasoning as in the proof of (6.14), one then gets:
$$\left\langle-L_{g_{b}} h, h\right\rangle_{L^{2}} \leq C\left(n, \tau, g_{b}\right)\left\|L_{g_{b}} h\right\|_{L_{\frac{n}{2}+1}^{2}}\left\langle-\Delta_{g_{b}} h, h\right\rangle_{L^{2}}^{\frac{1}{2}} .$$
On the other hand, by Theorem 3.19, if $h \in C_{\tau}^{2}\left(S^{2} T^{*} N\right)$ and if $h \perp \operatorname{ker}_{L^{2}} L_{g_{b}}$ (which is well-defined because $\tau>0$ and $\operatorname{ker}_{L^{2}} L_{g_{b}} \subset C_{n}^{0}$ ), one gets thanks to (6.15),
$$\left\langle-L_{g_{b}} h, h\right\rangle_{L^{2}} \leq C\left(n, \tau, g_{b}\right)\left\|L_{g_{b}} h\right\|_{L_{\frac{n}{2}+1}^{2}}\left\langle-L_{g_{b}} h, h\right\rangle_{L^{2}}^{\frac{1}{2}} .$$ \(\square\)

We now state and prove an interpolation inequality between weighted Sobolev spaces. By definition of our weighted norms, we have $\|.\|_{L^{2}} \leq\|.\|_{L_{\frac{n}{2}+1}^{2}}$. We will show that assuming that our tensors decay at infinity, we have a weaker reverse inequality.

Lemma 6.9. Let $T$ be in $L^{2}\left(S^{2} T^{*} N\right) \cap L_{\beta}^{2}\left(S^{2} T^{*} N\right)$ for $\beta>\frac{n}{2}+1$. Then, for $\delta \in(0,1)$ such that $\beta=\frac{n}{2}+\frac{1}{1-\delta}$ we have the following control :
$$\|T\|_{L_{\frac{n}{2}+1}^{2}} \leq\|T\|_{L^{2}}^{\delta}\|T\|_{L_{\beta}^{2}}^{1-\delta} .$$

In particular, if $T$ is small enough in norm $C_{\tau+2}^{0}$ for $\tau>\frac{n-2}{2}$, we have
$$\|T\|_{L_{\frac{n}{2}+1}^{2}} \leq\|T\|_{L^{2}}^{\delta},$$
for any $\delta$ such that $\tau+2>\frac{n}{2}+\frac{1}{1-\delta}$, that is $\delta<\frac{2 \tau-(n-2)}{2 \tau-(n-4)}$.

Proof. For this, let us choose $0<\delta<1$ such that $\beta=\frac{n}{2}+\frac{1}{1-\delta}$ which always exists since $\beta>\frac{n}{2}+1$. We then have,
$$\begin{aligned}
\|T\|_{L_{\frac{n}{2}+1}^{2}}^{2} & =\int_{N}|T|_{g_{b}}^{2 \delta} \cdot|T|_{g_{b}}^{2(1-\delta)} \rho_{g_{b}}^{2} d \mu_{g_{b}} \\
& \leq\left(\int_{N}|T|_{g_{b}}^{2} d \mu_{g_{b}}\right)^{\delta} \cdot\left(\int_{N}|T|_{g_{b}}^{2} \rho_{g_{b}}^{\frac{2}{1-\delta}} d \mu_{g_{b}}\right)^{1-\delta} \\
& =\left(\int_{N}|T|_{g_{b}}^{2} d \mu_{g_{b}}\right)^{\delta} \cdot\left(\int_{N}|T|_{g_{b}}^{2} \rho_{g_{b}}^{2 \beta-n} d \mu_{g_{b}}\right)^{1-\delta} \\
& =\|T\|_{L^{2}}^{2 \delta}\|T\|_{L_{\beta}^{2}}^{2(1-\delta)}
\end{aligned}$$
Here we have made use of the assumption $\frac{2}{1-\delta}=2 \beta-n$ together with the definition of the space $L_{\beta}^{2}\left(S^{2} T^{*} N\right)$. \(\square\)

We use this inequality in order to find a Lojasiewicz inequality with an $L^{2}$ norm of $\nabla \lambda_{\text {ALE }}$ on the right-hand side.

Proposition 6.10. Let $\left(N^{n}, g_{b}\right), n \geq 5$, be a linearly stable ALE Ricci-flat metric asymptotic to $\mathbb{R}^{n} / \Gamma$, for some finite subgroup $\Gamma$ of $S O(n)$ acting freely on $\mathbb{S}^{n-1}$. Let $\tau \in\left(\frac{n}{2}, n-2\right)$. Then for any $0<\delta<\frac{2 \tau-(n-2)}{2 \tau-(n-4)}$, there exists $C>0$ such that for all the following Lojasiewicz inequality holds true for any sufficiently small symmetric 2-tensor $h \in C_{\tau}^{2}\left(S^{2} T^{*} N\right)$ :
$$\left\langle-L_{g_{b}} h, h\right\rangle_{L^{2}}^{2-\theta_{L^{2}}} \leq C\left\|L_{g_{b}} h\right\|_{L^{2}}^{2}, \quad \theta_{L^{2}}:=2-\frac{1}{\delta},$$
for some positive constant $C=C\left(n, \theta_{L^{2}}, \tau, g_{b}\right)$.

Proof. Let us use the interpolation inequality [(6.17), Lemma 6.9] on the $L_{\frac{n}{2}+1^{-}}^{2}$ norm on the right-hand side of the inequality (6.13). This leads to the desired inequality (6.18) with $\theta>0$ such that $1-\frac{\theta}{2}=\frac{1}{2 \delta}$ by considering $T:=L_{g_{b}} h$. Note however that this leads to $\theta>0$ only if $\delta>\frac{1}{2}$ which is only possible when $\tau>\frac{n}{2}$. \(\square\)

Remark 6.11. The proof above works in all dimensions and yields a nontrivial infinitesimal Lojasiewicz inequality (that is with $0<\theta<1$ ) assuming that $\tau>\frac{n}{2}$. However, in dimension 3 and 4, this imposes $\tau>n-2$ and induces several difficulties later on. We will also see in a forthcoming work that we cannot expect a $C_{\tau}^{2, \alpha}$-convergence for $\tau>n-2$ along the Ricci flow: this shows that we crucially need a Lojasiewicz inequality adapted to the case $\tau<n-2$.

Both of the exponents obtained for the $L_{\frac{n}{2}+1}^{2}$ and the $L^{2}$-Lojasiewicz inequalities of Propositions 6.7 and 6.10 are moreover optimal as one can see in the following example on functions which obviously extends to conformal deformations.

Example 6.12. Let $A \gg 1$ and $\tau>0$. Consider the cut off function $\chi_{A}$ of Example 3.1. Let us define $u_{A, \tau}=\chi_{A} \rho_{g_{b}}^{-\tau} \in C_{\tau}^{2, \alpha}$.

Then, denoting $f\left(u_{A, \tau}\right) \sim g(A, \tau)$ if there exists $C>0$ independent of $A$ large enough such that $C^{-1} g(A, \tau)<f\left(u_{A, \tau}\right)<C g(A, \tau)$, we have the following controls:
\begin{itemize}
\item[-] $-\int_{N} u_{A, \tau} \Delta_{g_{b}} u_{A, \tau} d v_{g_{b}}=\int_{N}\left|\nabla^{g_{b}} u_{A, \tau}\right|^{2} d v_{g_{b}} \sim A^{(n-2)-2 \tau}$,
\item[-] $\left\|\Delta_{g_{b}} u_{A, \tau}\right\|_{L^{2}}^{2}=\int_{N}\left|\Delta_{g_{b}} u\right|^{2} d v_{g_{b}} \sim A^{(n-4)-2 \tau}$, and
\end{itemize}
$$\text { - }\left\|\Delta_{g_{b}} u_{A, \tau}\right\|_{L_{\frac{n}{2}+1}^{2}}^{2}=\int_{N} \rho_{g_{b}}^{2}\left|\Delta_{g_{b}} u\right|^{2} d v_{g_{b}} \sim A^{(n-2)-2 \tau} \text {. }$$
We therefore see that we exactly have
$$-\int_{N} u_{A, \tau} \Delta_{g_{b}} u_{A, \tau} d v_{g_{b}} \sim\left\|\Delta_{g_{b}} u_{A, \tau}\right\|_{L_{\frac{n}{2}+1}^{2}}^{2},$$
and
$$-\int_{N} u_{A, \tau} \Delta_{g_{b}} u_{A, \tau} d v_{g_{b}} \sim\left\|\Delta_{g_{b}} u_{A, \tau}\right\|_{L^{2}}^{2 \delta}$$
with $\delta=\frac{2 \tau-(n-2)}{2 \tau-(n-4)}$.
Remark 6.13. Notice that the exponent $2-\theta$ is smaller than 1 and is asymptotically 1 as the dimension $n$ increases. This is in contrast with the case where $\left(N^{n}, g_{b}\right)$ is a closed Riemannian manifold endowed with an integrable Ricci-flat metric $g_{b}$.

By bounding from above the nonlinear terms of $\left\|\nabla \lambda_{\text {ALE }}\left(g_{b}+h\right)\right\|_{L^{2}}$ by $\frac{1}{2}\left\|L_{g_{b}} h\right\|_{L^{2}}$ and by bounding the higher order terms of $\left|\lambda_{\text {ALE }}\left(g_{b}+h\right)\right|$ by $\frac{1}{2}\left|\left\langle-L_{g_{b}} h, h\right\rangle_{L^{2}}\right|$ in an analogous way to the proof of Proposition 6.6, we get an $L^{2}$-Łojasiewicz inequality. Note that controlling these nonlinear terms at this point is far from being an easy task, and in particular it does not seem to be possible to do so in dimension 3 and 4, see the discussion below Remark 6.13. For these reasons, we do not state it and refer the reader to Theorem 7.12.

There are several difficulties to develop a similar argument in dimension $n=4$.
\begin{itemize}
\item[-] The exponent given in (6.18) does not provide a Lojasiewicz inequality with $\theta>0$.
\item[-] In the proof of the bounds for the nonlinear terms, a reason is that $2=n-2=\frac{n}{2}$ as well as $0=\frac{n}{2}-2$ are exceptional values of the Laplacian in this dimension, which complicates the use of Fredholm theory. In particular, the space $\left(\operatorname{ker}_{L^{2}} L_{g_{b}}\right)^{\perp}$ is not closed for the norms $H_{0}^{2}$ (or $H_{-\epsilon}^{2}$ ).
\item[-] There are also asymptotically constant 2-tensors in the kernel of the Lichnerowicz Laplacian which have to be dealt with to obtain informations on the $L^{2}=L_{2}^{2}$-norm of the Hessian of functions. Indeed an inequality
$$\left\|\nabla^{g_{b}, 2} h\right\|_{L^{2}} \leq C\left\|L_{g_{b}} h\right\|_{L^{2}}$$
for $h \perp \operatorname{ker}_{L^{2}} L_{g_{b}}$ is contradicted by the elements of $\operatorname{ker}_{C^{0}} L_{g_{b}} \cap\left(\operatorname{ker}_{L^{2}} L_{g_{b}}\right)^{\perp}$.
\end{itemize}
A priori, on this last point, the orthogonality is not well defined because the elements of $\operatorname{ker}_{L^{2}} L_{g_{b}}$ are $O\left(r^{-4}\right)$ while the elements of $\operatorname{ker}_{C^{0}} L_{g_{b}}$ are $O(1)$ and this might lead to a nonconvergent integral. However, the elements of $\operatorname{ker}_{L^{2}} L_{g_{b}}$ are asymptotic to $H_{2} \cdot \rho_{g_{b}}^{-4}$ for $H_{2}$ a 2-tensor whose coefficients are eigenfunctions of the spherical Laplacian for the second eigenvalue while the elements of $\operatorname{ker}_{C^{0}} L_{g_{b}}$ are asymptotic to some constant 2-tensor $H_{0}$. Since $\int_{\mathbb{S}^{3}}\left\langle H_{0}, H_{2}\right\rangle_{\mathbb{S}^{3}} d \mu_{\mathbb{S}^{3}}=0$, the $L^{2}$-product of an element of $\operatorname{ker}_{L^{2}} L_{g_{b}}$ and an element of $\operatorname{ker}_{C^{0}} L_{g_{b}}$ is well-defined.

\section*{7. A Łojasiewicz inequality for $\lambda_{\text {ale }}$ : the general case}

In this section, we check that the classical proof of the Lojasiewicz-Simon inequality, and in particular its version summarized in [CM14], holds in the context of weighted spaces. We will then deduce a Lojasiewicz-Simon inequality for $\lambda_{\text {ALE }}$ in the neighborhood of a given Ricci-flat ALE metric.

\subsection*{7.1. A general $L_{\frac{n}{2}+1}^{2}$-Lojasiewicz inequality for functionals on ALE metrics.}

The scheme of proof of Lojasiewicz-Simon inequality by Lyapunov-Schmidt reduction summarized in [CM14] extends to the setting of weighted norms. Indeed, the fact that the function spaces are modeled on Hölder spaces $C^{k, \alpha}$ is not so essential in Colding-Minicozzi's proof, the crucial properties of these spaces being that they are Banach and that the linearization of the gradient is Fredholm between them.

Before we state the main result of this section, we discuss the notion of the gradient of functionals in the setting of ALE metrics when defined on $C_{\tau}^{2, \alpha}$ or on $C_{\tau+2}^{0, \alpha}, \tau \in\left(\frac{n-2}{2}, n-2\right)$, $\alpha \in(0,1)$. If $F: \mathcal{O} \rightarrow \mathbb{R}$ is a $C^{1}$ functional defined on an open subset $\mathcal{O}$ of $C_{\tau}^{2, \alpha}$ then it admits a unique gradient denoted by $\nabla F$ defined on $\mathcal{O}$ with values into $L_{\frac{n}{2}+1}^{2}$ such that $D_{h} F(v)=\langle\nabla F(h), v\rangle_{L^{2}}$ for all $h \in \mathcal{O}$ and $v \in L_{\frac{n}{2}-1}^{2}$. Similarly, we use the same notation to denote the gradient of any $C^{1}$ functional defined on $C_{\tau+2}^{0, \alpha} \subset L_{\frac{n}{2}+1}^{2}$, the only difference here being that the gradient belongs to $L_{\frac{n}{2}-1}^{2}$.
Proposition 7.1. Let $\tau \in\left(\frac{n-2}{2}, n-2\right), \alpha \in(0,1)$ and let $\left(N^{n}, g_{b}\right)$ be an ALE Ricciflat metric. Let $E$ (respectively $F$ ) be a closed subspace of $L_{\frac{n}{2}-1}^{2}\left(S^{2} T^{*} N\right)$ (respectively of $\left.L_{\frac{n}{2}+1}^{2}\left(S^{2} T^{*} N\right)\right)$ such that $C_{\tau}^{2, \alpha}\left(S^{2} T^{*} N\right) \cap E$ and $C_{\tau+2}^{0, \alpha}\left(S^{2} T^{*} N\right) \cap F$ are respectively a closed subset of $C_{\tau}^{2, \alpha}\left(S^{2} T^{*} N\right)$ and a closed subset of $C_{\tau+2}^{0, \alpha}\left(S^{2} T^{*} N\right)$. Let $G: \mathcal{O} \subset C_{\tau}^{2, \alpha}\left(S^{2} T^{*} N\right) \rightarrow \mathbb{R}$ be an analytic functional in the sense of Definition A. 1 defined on $\mathcal{O}$, a neighborhood of 0 in $C_{\tau}^{2, \alpha}\left(S^{2} T^{*} N\right) \cap E$.

If it satisfies,
\begin{itemize}
\item[(1)] the gradient of $G, \nabla G: \mathcal{O} \rightarrow C_{\tau+2}^{0, \alpha}$ has a Fréchet derivative at each point which varies continuously, with $\nabla G(0)=0$, and
$$\|\nabla G(x)-\nabla G(y)\|_{L_{\frac{n}{2}+1}^{2}} \leq C\|x-y\|_{H_{\frac{n}{2}-1}^{2}},$$
\item[(2)] the Fréchet derivative of $\nabla G: \mathcal{O} \rightarrow C_{\tau}^{0, \alpha}$ is continuous when interpreted as a map from $H_{\frac{n}{2}-1}^{2}$ to $L_{\frac{n}{2}+1}^{2}$,
\item[(3)] the linearization $L$ of (the extension to $H_{\frac{n}{2}-1}^{2}$ of) $\nabla G$ at 0 ,
\begin{itemize}
\item[(a)] is bounded from $H_{\frac{n}{2}-1}^{2}$ to $L_{\frac{n}{2}+1}^{2}$ and Fredholm $H_{\frac{n}{2}-1}^{2} \cap E$ to $L_{\frac{n}{2}+1}^{2} \cap F$,
\item[(b)] its kernel K on $H_{\frac{n}{2}-1}^{2} \cap E$ equals its $L^{2}$-cokernel on $L_{\frac{n}{2}+1}^{2} \cap F$,
\item[(c)] is bounded from $C_{\tau}^{2, \alpha}$ to $C_{\tau+2}^{0, \alpha}$,
\item[(d)] is Fredholm from $C_{\tau}^{2, \alpha} \cap E$ to $C_{\tau+2}^{0, \alpha} \cap F$,
\item[(e)] its kernel on $C_{\tau}^{2, \alpha} \cap E$ equals its $L^{2}$-cokernel on $C_{\tau+2}^{0, \alpha} \cap F$ and is equal to $\mathbf{K}$,
\end{itemize}
\end{itemize}
then, there exist $\theta \in(0,1]$ and $C>0$ such that for all sufficiently small $x$ in $C_{\tau}^{2, \alpha}\left(S^{2} T^{*} N\right) \cap E$,
$$|G(x)-G(0)|^{2-\theta} \leq C\|\nabla G(x)\|_{L_{\frac{n}{2}+1}^{2}}^{2} .$$
Moreover, the constant $\theta$ is independent of $\alpha \in(0,1)$ and is a monotone nondecreasing function of $\tau \in\left(\frac{n-2}{2}, n-2\right)$.

Remark 7.2. We will use this quite general statement with
\begin{itemize}
\item[-] the closed subspaces $E=\operatorname{ker~}_{\operatorname{div}_{g_{b}}} \subset C_{\tau}^{2, \alpha}$ and $F:=\operatorname{div}_{g_{b}}^{*}\left(C_{c}^{\infty}(T N)\right)^{\perp}$.
\end{itemize}
\begin{itemize}
\item[-] the functional $G=\lambda_{A L E}\left(g_{b}+.\right)$ defined on a $C_{\tau}^{2, \alpha}$-neighborhood of 0 by Section 3,
\item[-] its $L^{2}\left(e^{-f_{g}} d \mu_{g}\right)$-gradient,
$$h \mapsto \operatorname{Ric}\left(g_{b}+h\right)+\nabla^{g_{b}+h, 2} f_{g_{b}+h},$$
\item[-] the linearization of $h \mapsto \operatorname{Ric}\left(g_{b}+h\right)+\nabla^{g_{b}+h, 2} f_{g_{b}+h}$ at 0 on $E$ is $\frac{1}{2} L_{g_{b}}$.
\end{itemize}

Remark 7.3. Proposition 7.1 is stated in terms of function spaces modelled on symmetric 2 -tensors, the only reason for this restriction being its main application to the functional $\lambda_{\mathrm{ALE}}$ defined on metrics. The condition $\frac{n-2}{2}<\tau<n-2$ is assumed to ensure the Fredholmness of the linearization of the gradient in the particular case of $\lambda_{\text {ALE }}$.

\subsection*{7.2. Proof of Proposition 7.1.}

Let us consider $G$ satisfying the assumptions of Proposition 7.1 and let us prove that we can reduce our context to the finite-dimensional case by Lyapunov-Schmidt reduction by following the scheme of proof of [CM14, Section 7]. We first have to find a replacement for [CM14, Lemma 7.5] which generally does not hold in the setting of weighted Hölder spaces because of the following remark.

Remark 7.4. Even if $L$ is selfadjoint, its kernel and its $L^{2}$-cokernel might be different because we are dealing with weighted Hölder spaces. For example, the $L^{2}$-cokernel of the Lichnerowicz operator $L_{g_{b}}: C_{\tau}^{2, \alpha}\left(S^{2} T^{*} N\right) \rightarrow C_{\tau+2}^{0, \alpha}\left(S^{2} T^{*} N\right)$, that is the space $\mathbf{C}$ such that $L_{g_{b}}\left(C_{\tau}^{2, \alpha}\right)=$ $\mathbf{C}^{\perp} \cap C_{\tau+2}^{0, \alpha}$ is the kernel of $L$ on $C_{n-(\tau+2)}^{k, \alpha}\left(S^{2} T^{*} N\right)$ where $-2<n-(\tau+2)<\frac{n}{2}-1$ (see Note 5.3) which is larger than $\mathbf{K}$ if $\tau>n-2$. We therefore always have $\mathbf{K} \subset \mathbf{C}$ here and the inclusion can be strict in our applications because there are asymptotically constant 2-tensors in the kernel of the Lichnerowicz operator on a Ricci-flat ALE metrics if we do not impose a decay at infinity.

Denote by K the finite dimensional kernel (and $L^{2}$-cokernel for $0<\tau<n-2$ ) of $L$ : $C_{\tau}^{2, \alpha}\left(S^{2} T^{*} N\right) \cap E \rightarrow C_{\tau+2}^{0, \alpha}\left(S^{2} T^{*} N\right) \cap F$, and define $\Pi_{\mathbf{K}}$ to be the associated $L^{2}$-projection onto K. Define the mapping:
$$\mathcal{N}=\nabla G+\Pi_{\mathbf{K}} .$$

Lemma 7.5. There is an open subset
$$\mathcal{U} \subset C_{\tau+2}^{0, \alpha}\left(S^{2} T^{*} N\right) \cap F,$$
about 0 and a map $\Phi: \mathcal{U} \rightarrow C_{\tau}^{2, \alpha}\left(S^{2} T^{*} N\right) \cap E$ with $\Phi(0)=0$, and $C>0$, so that for any $x, y \in \mathcal{U}$ and $z \in C_{\tau}^{2, \alpha}\left(S^{2} T^{*} N\right) \cap E$ sufficiently small,
\begin{itemize}
\item[-] $\Phi \circ \mathcal{N}(z)=z$ and $\mathcal{N} \circ \Phi(x)=x$,
\item[-] $\|\Phi(x)\|_{C_{\tau}^{2, \alpha}} \leq C\|x\|_{C_{\tau+2}^{0, \alpha}}$ and $\|\Phi(x)-\Phi(y)\|_{H_{\frac{n}{2}-1}^{2}} \leq C\|x-y\|_{L_{\frac{n}{2}+1}^{2}}$,
\item[-] the function $f:=G \circ \Phi$ is analytic on $\mathcal{U}$. In particular, it is analytic on K.
\end{itemize}
Proof. By assumptions (1) and (3e), the mapping $\mathcal{N}: C_{\tau}^{2, \alpha} \cap E \rightarrow C_{\tau+2}^{0, \alpha} \cap F$ is $C^{1}$ and its Fréchet derivative at 0 is
$$D_{0} \mathcal{N}=L+\Pi_{\mathbf{K}} .$$
Note that since $L$ is Fredholm of index 0 by assumptions (3d) and (3e), it is enough to prove that $D_{0} \mathcal{N}$ is injective and Fredholm in order to use the implicit function theorem to define $\Phi$. The kernel K being finite dimensional, the projection $\Pi_{\mathbf{K}}$ is a compact operator which implies that $D_{0} \mathcal{N}$ is Fredholm. Now, by assumption (3e), the $L^{2}$-cokernel of $L$ is K. Therefore, if
$L(x)+\Pi_{\mathbf{K}}(x)=0$, then, by projecting on $\mathbf{K}^{\perp}$, we have $L(x)=0$, hence $x \in \mathbf{K}$ and $\Pi_{\mathbf{K}}(x)=0$, thus, finally $x=0$. We can then conclude like in [CM14, Lemma 7.5] by using the implicit function theorem, Lemma A.2.

The bound $\|\Phi(x)\|_{C_{\tau}^{2, \alpha}} \leq C\|x\|_{C_{\tau+2}^{0, \alpha}}$ comes from the integral mean value theorem in Banach spaces and the fact that
$$D_{y} \Phi=\left(D_{\Phi(y)} \mathcal{N}\right)^{-1}$$
is continuous and bounded from $\mathcal{U} \subset C_{\tau+2}^{0, \alpha} \cap F$ to $C_{\tau}^{2, \alpha}$.
The Lipschitz bound $\|\Phi(x)-\Phi(y)\|_{H_{\frac{n}{2}-1}^{2}} \leq C\|x-y\|_{L_{\frac{n}{2}+1}^{2}}$ for sufficiently small $x, y \in \mathcal{U}$ is equivalent to $\|x-y\|_{H_{\frac{n}{2}-1}^{2}} \leq C\|\mathcal{N}(x)-\mathcal{N}(y)\|_{L_{\frac{n}{2}+1}^{2}}$ for sufficiently small $x, y \in \mathcal{O}$. This in turn is implied if $\|x-y\|_{H_{\frac{n}{2}-1}^{2}} \leq C\left\|D_{0} \mathcal{N}(x-y)\right\|_{L_{\frac{n}{2}+1}^{2}}$ for sufficiently small $x, y \in \mathcal{O}$ by assumption (2). Now, the same reasoning that led us to prove that $\mathcal{N}$ is a local diffeomorphism at 0 between weighted Hölder spaces, $L+\Pi_{\mathbf{K}}: H_{\frac{n}{2}-1}^{2} \cap E \rightarrow L_{\frac{n}{2}+1}^{2} \cap F$ is an isomorphism of Banach spaces by assumptions (3a) and (3b): this implies the desired lower bound on $\left\|D_{0} \mathcal{N}(x-y)\right\|_{L_{\frac{n}{2}+1}^{2}}$ since $L+\Pi_{\mathbf{K}}=D_{0} \mathcal{N}$ on $C_{\tau}^{2, \alpha} \cap E$.

The analyticity of $f$ on $\mathcal{U}$ (and therefore on K by assumption (3e)) comes from the analyticity of $G$ and that of $\Phi$ ensured by the analytic implicit function theorem stated in Lemma A.2. \(\square\)

Remark 7.6. In case the $L^{2}$-cokernel $\mathbf{C}$ and the kernel $\mathbf{K}$ are different, one can instead define
$$\mathcal{N}:=\Pi_{\mathbf{C}^{\perp}} \circ \nabla G+\Pi_{\mathbf{K}},$$
and define $\Phi$ on its image. This however induces some technical difficulties in weighted spaces. Since we do not need it presently we only considered the case when $\mathbf{C}=\mathbf{K}$.

Let us now adapt [CM14, Lemma 7.10] to our slightly different case.
Lemma 7.7. There exists $C>0$ such that for any $x$ in a small enough neighborhood of 0 in $C_{\tau}^{2, \alpha}\left(S^{2} T^{*} N\right) \cap E$, we have
$$\left\|\nabla f\left(\Pi_{\mathbf{K}}(x)\right)\right\|_{L_{\frac{n}{2}-1}^{2}} \leq C\|\nabla G(x)\|_{L_{\frac{n}{2}+1}^{2}} .$$
More generally, if $y_{t}:=\Pi_{\mathbf{K}}(x)+t \nabla G(x), t \in[0,1]$, for $x$ in a small enough neighborhood of 0 in $C_{\tau}^{2, \alpha}\left(S^{2} T^{*} N\right) \cap E$, then:
$$\left\|\nabla f\left(y_{t}\right)\right\|_{L_{\frac{n}{2}-1}^{2}} \leq C\|\nabla G(x)\|_{L_{\frac{n}{2}+1}^{2}},$$
for some positive constant $C$ independent of $x$ and $t$.
Proof. For $y \in \mathcal{U}$ sufficiently small, since $f=G \circ \Phi$, we have $D_{y} f(v)=D_{\Phi(y)} G \circ D_{y} \Phi(v)$ for $v \in L_{\frac{n}{2}+1}^{2}$. In particular, if $v \in L_{\frac{n}{2}+1}^{2}$
$$\begin{aligned}
\left|D_{y} f(v)\right| & \leq\|\nabla G(\Phi(y))\|_{L_{\frac{n}{2}+1}^{2}}\left\|D_{y} \Phi(v)\right\|_{H_{\frac{n}{2}-1}^{2}} \\
& \leq C\|\nabla G(\Phi(y))\|_{L_{\frac{n}{2}+1}^{2}}\|v\|_{L_{\frac{n}{2}+1}^{2}},
\end{aligned}$$
where $C$ is a positive constant independent of $v \in L_{\frac{n}{2}+1}^{2}$. Here, we have used the Lipschitz bound on $\Phi$ established in Lemma 7.5. By definition of the gradient of $f$, one gets:
$$\|\nabla f(y)\|_{L_{\frac{n}{2}-1}^{2}} \leq C\|\nabla G \circ \Phi(y)\|_{L_{\frac{n}{2}+1}^{2}},$$

In particular, for any $x \in C_{\tau}^{2, \alpha} \cap E$ sufficiently small, we have
$$\left\|\nabla f\left(\Pi_{\mathbf{K}}(x)\right)\right\|_{L_{\frac{n}{2}-1}^{2}} \leq C\left\|\nabla G \circ \Phi\left(\Pi_{\mathbf{K}}(x)\right)\right\|_{L_{\frac{n}{2}+1}^{2}} .$$
Now, since $x=\Phi\left(\Pi_{\mathbf{K}}(x)+\nabla G(x)\right)$, the Lipschitz bound (7.1) for $\nabla G$ and the one obtained in Lemma 7.5 for $\Phi$ yield
$$\begin{aligned}
\left\|\nabla G\left(\Phi \circ \Pi_{\mathbf{K}}(x)\right)-\nabla G(x)\right\|_{L_{\frac{n}{2}+1}^{2}} & =\left\|\nabla G\left(\Phi\left(\Pi_{\mathbf{K}}(x)\right)\right)-\nabla G\left(\Phi\left(\Pi_{\mathbf{K}}(x)+\nabla G(x)\right)\right)\right\|_{L_{\frac{n}{2}+1}^{2}} \\
& \leq C\left\|\Phi\left(\Pi_{\mathbf{K}}(x)\right)-\Phi\left(\Pi_{\mathbf{K}}(x)+\nabla G(x)\right)\right\|_{H_{\frac{n}{2}-1}^{2}} \\
& \leq C\|\nabla G(x)\|_{L_{\frac{n}{2}+1}^{2}} .
\end{aligned}$$
This ends the proof of the desired estimate (7.3) by the triangular inequality.
In order to prove (7.4), notice that since $f=G \circ \Phi$ and consequently $\Phi \circ \mathcal{N}=\mathrm{Id}$, we have $G=f \circ \mathcal{N}$ which by differentiation implies that we have
$$D_{\Phi\left(y_{t}\right)} G=D_{y_{t}} f \circ D_{\Phi\left(y_{t}\right)} \mathcal{N} .$$
Now, since $\nabla_{\Phi\left(y_{t}\right)} \mathcal{N}$ is invertible with a bounded inverse by Lemma 7.5, we deduce from (7.6) that $D_{y_{t}} f=D_{\Phi\left(y_{t}\right)} G \circ\left(D_{\Phi\left(y_{t}\right)} \mathcal{N}\right)^{-1}$ and therefore that
$$\left\|D_{y_{t}} f\right\|_{1} \leq C\left\|D_{\Phi\left(y_{t}\right)} G\right\|_{2},$$
where the norm $\|.\|_{1}$ is that of operators from $L_{n+1}^{2}$ to $\mathbb{R}$ and the norm $\|.\|_{2}$ is that of operators from $H_{\frac{n}{2}-1}^{2}$ to $\mathbb{R}$. Since for the $L^{2}\left(g_{b}\right)$ scalar product, the dual of $L_{\frac{n}{2}+1}^{2}$ is identified with $L_{\frac{n}{2}-1}^{2}$ and that of $L_{\frac{n}{2}-1}^{2}$ with $L_{\frac{n}{2}+1}^{2}$, (7.7) rewrites in the following way thanks to the $L^{2}\left(g_{b}\right)$ gradients:
$$\left\|\nabla f\left(y_{t}\right)\right\|_{L_{\frac{n}{2}-1}^{2}} \leq C\left\|\nabla G\left(\Phi\left(y_{t}\right)\right)\right\|_{L_{\frac{n}{2}+1}^{2}} .$$

Now, we invoke (7.8) to observe that it remains to control $\left\|\nabla G\left(\Phi\left(y_{t}\right)\right)\right\|_{L_{\frac{n}{2}+1}^{2}}$ from above by $\|\nabla G(x)\|_{L_{\frac{n}{2}+1}^{2}}$. For this, we use (7.1) which yields
$$\begin{aligned}
\left\|\nabla G\left(\Phi\left(y_{t}\right)\right)-\nabla G(x)\right\|_{L_{\frac{n}{2}+1}^{2}} & \leq C\left\|\Phi\left(y_{t}\right)-x\right\|_{H_{\frac{n}{2}-1}^{2}} \\
& =C\left\|\Phi\left(y_{t}\right)-\Phi\left(y_{1}\right)\right\|_{H_{\frac{n}{2}-1}^{2}} \\
& \leq C\left\|y_{t}-y_{1}\right\|_{L_{\frac{n}{2}+1}^{2}} \\
& =C(1-t)\|\nabla G(x)\|_{L_{\frac{n}{2}+1}^{2}} .
\end{aligned}$$
This implies that $\left\|\nabla G\left(\Phi\left(y_{t}\right)\right)\right\|_{L_{\frac{n}{2}+1}^{2}} \leq(1+C)\|\nabla G(x)\|_{L_{\frac{n}{2}+1}^{2}}$ by the triangular inequality and therefore by (7.8),
$$\left\|\nabla f\left(y_{t}\right)\right\|_{L_{\frac{n}{2}-1}^{2}} \leq C\|\nabla G(x)\|_{L_{\frac{n}{2}+1}^{2}} .$$
This ends the proof of the desired estimate. \(\square\)

Let us now show that an adaptation of [CM14, Lemma 7.15] to our situation yields a control in $L_{\frac{n}{2}+1}^{2}$ only.
Lemma 7.8. There exists $C>0$ such that for sufficiently small $x \in C_{\tau}^{2, \alpha}\left(S^{2} T^{*} N\right) \cap E$, we have
$$\left|G(x)-f\left(\Pi_{\mathbf{K}}(x)\right)\right| \leq C\|\nabla G(x)\|_{L_{\frac{n}{2}+1}^{2}}^{2} .$$

Proof. Define for all $t \in[0,1]$,
$$y_{t}:=\Pi_{\mathbf{K}}(x)+t \nabla G(x),$$
for which we have $\Phi\left(y_{1}\right)=x, y_{0}=\Pi_{\mathbf{K}}(x)$ and $\frac{d}{d t} y_{t}=\nabla G(x)$.
By integration, we have
$$\begin{aligned}
G(x)-f\left(\Pi_{\mathbf{K}}(x)\right) & =f\left(y_{1}\right)-f\left(y_{0}\right) \\
& =\int_{0}^{1}\left\langle\nabla f\left(y_{t}\right), \nabla G(x)\right\rangle_{L^{2}} d t
\end{aligned}$$
where $\nabla f\left(y_{t}\right)$ (respectively $\nabla G(x)$ ) is interpreted as an element of $L_{\frac{n}{2}-1}^{2}$ (respectively $L_{\frac{n}{2}+1}^{2}$ ). Thanks to [(7.4), Lemma 7.7], there exists $C>0$ such that for all $t \in[0,1]$, we have
$$\left\|\nabla f\left(y_{t}\right)\right\|_{L_{\frac{n}{2}-1}^{2}} \leq C\|\nabla G(x)\|_{L_{\frac{n}{2}+1}^{2}} .$$

The estimate (7.10) then comes from Cauchy-Schwarz inequality. \(\square\)

We can then conclude exactly like in the end of the proof of [CM14, Theorem 7.3], by using the finite dimensional Lojasiewicz inequality on K. Note that this is the only step for which the analyticity of the functional is used.

Denote $f_{\mathbf{K}}$ the restriction of $f$ to the finite-dimensional space $\mathbf{K}$ which is an analytic function. Let $x \in C_{\tau}^{2, \alpha} \cap E$ be small enough. Thanks to the estimate (7.3), and thanks to the finite-dimensional Lojasiewicz inequality [Lo65], we have for some $0<\theta \leq 1$,
$$\begin{aligned}
C^{2}\|\nabla G(x)\|_{L_{\frac{n}{2}+1}^{2}}^{2} & \geq C\left\|\nabla f\left(\Pi_{\mathbf{K}}(x)\right)\right\|_{L_{\frac{n}{2}-1}^{2}}^{2} \\
& \geq\left\|\nabla f_{\mid \mathbf{K}}\left(\Pi_{\mathbf{K}}(x)\right)\right\|_{L_{\frac{n}{2}-1}^{2}}^{2} \\
& \geq\left|f_{\mathbf{K}}\left(\Pi_{\mathbf{K}}(x)\right)-f_{\mathbf{K}}(0)\right|^{2-\theta} \\
& =\left|f\left(\Pi_{\mathbf{K}}(x)\right)-G(0)\right|^{2-\theta},
\end{aligned}$$
where $C$ denotes the positive constant of (7.3). Here, we see K equipped with the $L_{\frac{n}{2}-1}^{2}$-norm (but any other norm would just change the constants as the dimension is finite). We can then finally use the estimate (7.10) together with the triangular inequality to obtain a general Łojasiewicz inequality :
$$|G(x)-G(0)|^{2-\theta} \leq C\|\nabla G(x)\|_{L_{\frac{n}{2}+1}^{2}}^{2},$$
with $0<\theta \leq 1$. We therefore obtain a Lojasiewicz inequality with a $L_{\frac{n}{2}+1}^{2}$-norm for the gradient. The above constant $\theta$ moreover does not depend on $\alpha$ or $\tau$.

\subsection*{7.3. Proof of a general Lojasiewicz inequality for $\lambda_{\text {ALE }}$ on ALE metrics.}

Let us now ensure that our functional $G=\lambda_{\text {ALE }}$ satisfies the assumptions of Proposition 7.1. We start by defining the set $E=\operatorname{ker} \operatorname{div}_{g_{b}}$. Let us spend some time understanding the image $L_{g_{b}}\left(C_{\tau}^{2, \alpha} \cap \operatorname{ker} \operatorname{div}_{g_{b}}\right)$ which intuitively is $C_{\tau+2}^{0, \alpha} \cap \operatorname{ker}_{\operatorname{div}_{g_{b}}}$. However, strictly speaking, we a priori cannot see $C_{\tau+2}^{0, \alpha} \cap \operatorname{ker} \operatorname{div}_{g_{b}}$ as a closed subset of $C_{\tau+2}^{0, \alpha}$ since the equation $\operatorname{div}_{g_{b}} h=0$ is not well-defined as it takes one derivative. It has to be understood in the weak sense. Let us be more precise about this in order to define the set $F:=\operatorname{div}_{g_{b}}^{*}\left(C_{c}^{\infty}(T N)\right)^{\perp}$.

Lemma 7.9. Let us define $E:=\operatorname{ker}_{\operatorname{div}_{g_{b}}}, \mathbf{K}:=\operatorname{ker}_{L^{2}} L_{g_{b}}$ and define $\Pi_{\mathbf{K}}$ the $L^{2}\left(g_{b}\right)$-projection on $\mathbf{K}$. Then the image $\left(L_{g_{b}}+\Pi_{\mathbf{K}}\right)\left(C_{\tau}^{2, \alpha} \cap E\right)$ is $C_{\tau+2}^{0, \alpha} \cap \operatorname{div}_{g_{b}}^{*}\left(C_{c}^{\infty}(T N)\right)^{\perp}$.

Proof. Consider $h \in C_{\tau}^{2, \alpha} \cap \operatorname{ker} \operatorname{div}_{g_{b}}$ and a smooth compactly supported vector field $X$ and denote the $L^{2}$-adjoint of $\operatorname{div}_{g_{b}}$ by $\operatorname{div}_{g_{b}}^{*}$. Notice that for such a vector field $X$, we have $\operatorname{div}_{g_{b}}^{*} X=-\frac{1}{2} \mathscr{L}_{X}\left(g_{b}\right)$. Now, similarly to the proof of Lemma 3.18, observe that,
$$\begin{aligned}
\left\langle L_{g_{b}} h, \operatorname{div}_{g_{b}}^{*} X\right\rangle_{g_{b}} & =\left\langle h, L_{g_{b}}\left(\operatorname{div}_{g_{b}}^{*} X\right)\right\rangle_{g_{b}} \\
& =\left\langle h, \operatorname{div}_{g_{b}}^{*} B_{g_{b}} \operatorname{div}_{g_{b}}^{*} X\right\rangle_{g_{b}} \\
& =\left\langle\operatorname{div}_{g_{b}} h, B_{g_{b}} \operatorname{div}_{g_{b}}^{*} X\right\rangle_{g_{b}}=0
\end{aligned}$$
and we see that since the elements of K are divergence-free according to Proposition 5.1, the image of $L_{g_{b}}+\Pi_{\mathbf{K}}$ is included in $C_{\tau+2}^{0, \alpha} \cap \operatorname{div}_{g_{b}}^{*}\left(C_{c}^{\infty}(T N)\right)^{\perp}$.

Conversely, let $v \in C_{\tau+2}^{0, \alpha} \cap \operatorname{div}_{g_{b}}^{*}\left(C_{c}^{\infty}(T N)\right)^{\perp}$ and let us show that there exists $h_{0} \in C_{\tau}^{2, \alpha} \cap$ ker $\operatorname{div}_{g_{b}}$ such that $v=L_{g_{b}} h_{0}+\Pi_{\mathbf{K}} h_{0}$.

Thanks to the Fredholm properties of $L_{g_{b}}$, see Proposition 5.1, one has $\left(L_{g_{b}}+\Pi_{\mathbf{K}}\right)\left(C_{\tau}^{2, \alpha}\right)=$ $C_{\tau+2}^{0, \alpha}$. In particular, there exists $h \in C_{\tau}^{2, \alpha}$ such that $v=L_{g_{b}} h+\Pi_{\mathbf{K}} h$.

Now, Proposition B. 6 ensures that we have a unique decomposition $h=h_{0}+\operatorname{div}_{g_{b}}^{*} V$ for a vector field $V \in C_{\tau-1}^{3, \alpha}$ and a symmetric 2-tensor $h_{0} \in C_{\tau}^{2, \alpha} \cap \operatorname{ker}_{\operatorname{div}_{g_{b}}}$. Let us prove that $\operatorname{div}_{g_{b}}^{*} V=0$. This will prove the expected result.

Since $v \in \operatorname{div}_{g_{b}}^{*}\left(C_{c}^{\infty}(T N)\right)^{\perp}$ and by density,
$$\left\langle L_{g_{b}} h+\Pi_{\mathbf{K}} h, \operatorname{div}_{g_{b}}^{*} V\right\rangle_{L^{2}}=0 .$$

Notice that $\left\langle\Pi_{\mathbf{K}} h, \operatorname{div}_{g_{b}}^{*} V\right\rangle_{L^{2}}=0$ independently since $\Pi_{\mathbf{K}} h \in \mathbf{K}$ is divergence-free.
On the other hand, by symmetry of $L_{g_{b}}$,
$$\begin{aligned}
0 & =\left\langle L_{g_{b}} h, \operatorname{div}_{g_{b}}^{*} V\right\rangle_{L^{2}} \\
& =\left\langle h, L_{g_{b}} \operatorname{div}_{g_{b}}^{*} V\right\rangle_{L^{2}} \\
& =\left\langle h, \operatorname{div}_{g_{b}}^{*} B_{g_{b}}\left(\operatorname{div}_{g_{b}}^{*} V\right)\right\rangle_{L^{2}} \\
& =\left\langle h_{0}, \operatorname{div}_{g_{b}}^{*} B_{g_{b}}\left(\operatorname{div}_{g_{b}}^{*} V\right)\right\rangle_{L^{2}}+\left\langle\operatorname{div}_{g_{b}}^{*} V, \operatorname{div}_{g_{b}}^{*} B_{g_{b}}\left(\operatorname{div}_{g_{b}}^{*} V\right)\right\rangle_{L^{2}} \\
& =\left\langle\operatorname{div}_{g_{b}}^{*} V, \operatorname{div}_{g_{b}}^{*} B_{g_{b}}\left(\operatorname{div}_{g_{b}}^{*} V\right)\right\rangle_{L^{2}} .
\end{aligned}$$
Here, we have used integration by parts and the fact that $h_{0}$ is divergence-free in the last line. A similar computation to [(3.22), Lemma 3.18] tells us that $B_{g_{b}}\left(\operatorname{div}_{g_{b}}^{*} V\right)=0=\nabla^{g_{b}} \operatorname{div}_{g_{b}} V$. This in turn implies by Bochner formula for vector fields that $\Delta_{g_{b}} V=0$ since $g_{b}$ is Ricci-flat. The use of the maximum principle then shows that $V=0$. This fact ends the proof of the lemma. \(\square\)

We now check conditions [(1), (7.1), (2)] from Proposition 7.1.
Proposition 7.10 (Energy estimates). Let $\left(N^{n}, g_{b}\right)$ be an ALE Ricci-flat metric, asymptotic to $\mathbb{R}^{n} / \Gamma$, for some finite subgroup $\Gamma$ of $S O(n)$ acting freely on $\mathbb{S}^{n-1}$ and let $\tau \in\left(\frac{n-2}{2}, n-2\right)$. Then there exists a neighborhood $B_{C_{\tau}^{2, \alpha}}\left(g_{b}, \varepsilon\right)$ of $g_{b}$ such that the following energy estimate holds true:
$$\left\|\nabla \lambda_{\mathrm{ALE}}\left(g_{2}\right)-\nabla \lambda_{\mathrm{ALE}}\left(g_{1}\right)\right\|_{L_{\frac{n}{2}+1}^{2}} \leq C\left(n, g_{b}, \varepsilon\right)\left\|g_{2}-g_{1}\right\|_{H_{\frac{n}{2}-1}^{2}},$$
for any metric $g_{2}, g_{1}$ in $B_{C_{\tau}^{2, \alpha}}\left(g_{b}, \varepsilon\right)$. Moreover, the differential of the map $g \in B_{C_{\tau}^{2, \alpha}}\left(g_{b}, \varepsilon\right) \rightarrow$ $\nabla \lambda_{\mathrm{ALE}}(g) \in B_{C_{\tau}^{0, \alpha}}(0, \varepsilon)$ satisfies:
$$\left\|D_{g_{2}} \nabla \lambda_{\mathrm{ALE}}-D_{g_{1}} \nabla \lambda_{\mathrm{ALE}}(h)\right\|_{L_{\frac{n}{2}+1}^{2}} \leq C\left(n, g_{b}, \varepsilon\right)\left\|g_{2}-g_{1}\right\|_{C_{\tau}^{2, \alpha}}\|h\|_{H_{\frac{n}{2}-1}^{2}},$$
for any metric $g_{2}, g_{1}$ in $B_{C_{\tau}^{2, \alpha}}\left(g_{b}, \varepsilon\right)$ and $h \in H_{\frac{n}{2}-1}^{2}$.
Proof. Let us fix a neighborhood $B_{C_{\tau}^{2, \alpha}}\left(g_{b}, \varepsilon\right)$ such that the properties on the potential function $f_{g}$ established in Proposition 2.2 hold true.

Strictly speaking, the symbol $\nabla \lambda_{\text {ALE }}(g)$ means the gradient of $\lambda_{\text {ALE }}$ at $g$ with respect to the Hilbert space $L^{2}\left(d \mu_{g_{b}}\right)$. Thanks to Proposition 3.4, $\nabla \lambda_{\text {ALE }}(g)$ can be computed in coordinates from the $L^{2}\left(e^{-f_{g}} d \mu_{g}\right)$-gradient of $\lambda_{\text {ALE }}$ as follows. Indeed, consider an orthonormal frame with respect to $g_{b}$ at a point such that $g_{i j}=\left(1+\lambda_{i}\right) \delta_{i j}$ and observe that:
$$\nabla \lambda_{\mathrm{ALE}}(g)_{i j}=-e^{-f_{g}} \frac{d \mu_{g}}{d \mu_{g_{b}}}\left(1+\lambda_{i}\right)^{-1}\left(1+\lambda_{j}\right)^{-1}\left(\operatorname{Ric}(g)+\nabla^{g, 2} f_{g}\right)_{i j},$$
which can be schematically written as
$$\nabla \lambda_{\mathrm{ALE}}(g)=-e^{-f_{g}} \frac{d \mu_{g}}{d \mu_{g_{b}}} g^{-1} * g^{-1} * g_{b} * g_{b} *\left(\operatorname{Ric}(g)+\nabla^{g, 2} f_{g}\right)$$
The estimate (7.23) then implies that for two metrics $g_{i}, i=1,2$ in a $C_{\tau}^{2, \alpha}$-neighborhood of $g_{b}$,
$$\begin{aligned}
\left|\nabla \lambda_{\mathrm{ALE}}\left(g_{2}\right)-\nabla \lambda_{\mathrm{ALE}}\left(g_{1}\right)\right|_{g_{b}} \leq & C\left|\operatorname{Ric}\left(g_{2}\right)+\nabla^{g_{2}, 2} f_{g_{2}}-\operatorname{Ric}\left(g_{1}\right)-\nabla^{g_{1}, 2} f_{g_{1}}\right|_{g_{b}} \\
& +C\left(\left|g_{2}-g_{1}\right|_{g_{b}}+\left|f_{g_{2}}-f_{g_{1}}\right|\right) \rho_{g_{b}}^{-2},
\end{aligned}$$
where $C=C\left(n, g_{b}, \varepsilon, \tau\right)$ are positive constants. Here we have used the weakened assumption on the decay of the Ricci curvatures $\operatorname{Ric}\left(g_{i}\right)=O\left(\rho_{g_{b}}^{-2-\tau}\right)=O\left(\rho_{g_{b}}^{-2}\right)$ together with the decay of the Hessians $\nabla^{g_{i}, 2} f_{g_{i}}=O\left(\rho_{g_{b}}^{-2}\right)$ from Proposition 2.2. In particular, Hardy's inequality from Theorem 1.7 and Proposition 4.1 show that:
$$\begin{aligned}
\left\|\nabla \lambda_{\mathrm{ALE}}\left(g_{2}\right)-\nabla \lambda_{\mathrm{ALE}}\left(g_{1}\right)\right\|_{L_{\frac{n}{2}+1}^{2}} \leq & C\left\|\operatorname{Ric}\left(g_{2}\right)+\nabla^{g_{2}, 2} f_{g_{2}}-\operatorname{Ric}\left(g_{1}\right)-\nabla^{g_{1}, 2} f_{g_{1}}\right\|_{L_{\frac{n}{2}+1}^{2}} \\
& +C\left(\left\|g_{2}-g_{1}\right\|_{H_{\frac{n}{2}-1}^{2}}+\left\|\nabla^{g_{b}}\left(f_{g_{2}}-f_{g_{1}}\right)\right\|_{L_{\frac{n}{2}}^{2}}\right) \\
\leq & C\left\|\operatorname{Ric}\left(g_{2}\right)+\nabla^{g_{2}, 2} f_{g_{2}}-\operatorname{Ric}\left(g_{1}\right)-\nabla^{g_{1}, 2} f_{g_{1}}\right\|_{L_{\frac{n}{2}+1}^{2}} \\
& +C\left\|g_{2}-g_{1}\right\|_{H_{\frac{n}{2}-1}^{2}} .
\end{aligned}$$

We first do the proof of the energy estimates (7.21) in case one of the two metrics is $g_{b}$, which implies in particular that $\nabla \lambda_{\text {ALE }}\left(g_{b}\right)=0$. Let us write $h:=g-g_{b}$ where $g \in B_{C_{\tau}^{2, \alpha}}\left(g_{b}, \varepsilon\right)$. By Lemmata C. 1 and C.2, linearizing the Ricci curvature of $g$ at $g_{b}$ gives schematically:
$$\begin{aligned}
-2 \operatorname{Ric}(g) & =-2 \operatorname{Ric}_{g_{b}}+L_{g_{b}} h-\mathscr{L}_{B_{g_{b}}(h)}\left(g_{b}\right)+Q\left(h, \nabla^{g_{b}} h, \nabla^{g_{b}, 2} h\right) \\
& =L_{g_{b}} h-\mathscr{L}_{B_{g_{b}}}(h)\left(g_{b}\right)+Q\left(h, \nabla^{g_{b}} h, \nabla^{g_{b}, 2} h\right),
\end{aligned}$$
where $Q\left(h, \nabla^{g_{b}} h, \nabla^{g_{b}, 2} h\right)$ satisfies pointwise
$$\left|Q\left(h, \nabla^{g_{b}} h, \nabla^{g_{b}, 2} h\right)\right|_{g_{b}} \leq C\left(n, g_{b}, \varepsilon\right)\left(\left|\operatorname{Rm}\left(g_{b}\right)\right|_{g_{b}}|h|_{g_{b}}^{2}+\left|\nabla^{g_{b}} h\right|_{g_{b}}^{2}+|h|_{g_{b}}\left|\nabla^{g_{b}, 2} h\right|_{g_{b}}\right) .$$
Therefore, by using the fact that $g=g_{b}+h \in B_{C_{\tau}^{2, \alpha}}\left(g_{b}, \varepsilon\right)$,
$$\|\operatorname{Ric}(g)\|_{L_{\frac{n}{2}+1}^{2}} \leq C\left(n, g_{b}, \varepsilon\right)\|h\|_{H_{\frac{n}{2}-1}^{2}},$$
where we suppressed the dependence of the norm on $S^{2} T^{*} N$.

Now, let us estimate $\left\|\nabla^{g, 2} f_{g}\right\|_{L^{2}}$. According to the Bochner formula applied to the smooth metric measure space $\left(N, g, \nabla^{g} f_{g}\right)$ :
$$\begin{aligned}
\left(\Delta_{g}-\left\langle\nabla^{g} f_{g}, \nabla^{g} \cdot\right\rangle_{g}\right)\left|\nabla^{g} f_{g}\right|_{g}^{2} & =2\left|\nabla^{g, 2} f_{g}\right|_{g}^{2}+2\left(\operatorname{Ric}(g)+\nabla^{g, 2} f_{g}\right)\left(\nabla^{g} f_{g}, \nabla^{g} f_{g}\right) \\
& +2\left\langle\nabla^{g}\left(\Delta_{g} f_{g}-\left\langle\nabla^{g} f_{g}, \nabla^{g} f_{g}\right\rangle_{g}\right), \nabla^{g} f_{g}\right\rangle_{g} .
\end{aligned}$$
Once (7.28) is multiplied by $\rho_{g_{b}}^{2}$, an integration by parts, legitimated by the decay of $f_{g}$ established in Proposition 2.2, gives:
$$\begin{aligned}
& \left\|\nabla^{g, 2} f_{g}\right\|_{L^{2}\left(\rho_{g_{b}}^{2} e^{-f_{g}} d \mu_{g}\right)}^{2}=\left\|\Delta_{g, f_{g}} f_{g}\right\|_{L^{2}\left(\rho_{g_{b}}^{2} e^{-f_{g}} d \mu_{g}\right)}^{2}-\int_{N}\left(\operatorname{Ric}(g)+\nabla^{g, 2} f_{g}\right)\left(\nabla^{g} f_{g}, \nabla^{g} f_{g}\right) \rho_{g_{b}}^{2} e^{-f_{g}} d \mu_{g} \\
& \quad+2 \int_{N} \Delta_{g, f_{g}} f_{g} \rho_{g_{b}}\left\langle\nabla^{g} \rho_{g_{b}}, \nabla^{g} f_{g}\right\rangle_{g} e^{-f_{g}} d \mu_{g}-\int_{N} \nabla^{g, 2} f_{g}\left(\nabla^{g} f_{g}, \nabla^{g}\left(\rho_{g_{b}}^{2} e^{-f_{g}}\right)\right) d \mu_{g} \\
& \quad \leq c\left\|\left.\nabla^{g} f_{g}\right|_{g} ^{2}+\mathrm{R}_{g}\right\|_{L^{2}\left(\rho_{g_{b}}^{2} e^{-f_{g}} d \mu_{g}\right)}^{2}+\frac{1}{2}\left\|\nabla^{g, 2} f_{g}\right\|_{L^{2}\left(\rho_{g_{b}}^{2} e^{-f_{g}} d \mu_{g}\right)}^{2}+c\left\|\nabla^{g} f_{g}\right\|_{L^{2}\left(e^{-f_{g}} d \mu_{g}\right)}^{2} \\
& \quad+c\left(\left\|\left|\nabla^{g} f_{g}\right|_{g}^{2}\right\|_{L^{2}\left(\rho_{g_{b}}^{2} e^{-f_{g}} d \mu_{g}\right)}^{2}+\|\operatorname{Ric}(g)\|_{L^{2}\left(\rho_{g_{b}}^{2} e^{-f_{g}} d \mu_{g}\right)}^{2}\right) \\
& \quad \leq \frac{1}{2}\left\|\nabla^{g, 2} f_{g}\right\|_{L^{2}\left(\rho_{g_{b}}^{2} e^{-f_{g}} d \mu_{g}\right)}^{2} \\
& \quad+c\left(\left\|\left.\nabla^{g} f_{g}\right|_{g} ^{2}\right\|_{L^{2}\left(\rho_{g_{b}}^{2} e^{-f_{g}} d \mu_{g}\right)}^{2}+\left\|\nabla^{g} f_{g}\right\|_{L^{2}\left(e^{-f_{g}} d \mu_{g}\right)}^{2}+\|\operatorname{Ric}(g)\|_{L^{2}\left(\rho_{g_{b}}^{2} e^{-f_{g}} d \mu_{g}\right)}^{2}\right),
\end{aligned}$$
where we use (2.1) together with Young's inequality in the third line and where $c=c(n)$ denotes a positive constant that may vary from line to line. By Proposition 2.2, $\rho_{g_{b}}\left|\nabla^{g} f_{g}\right|_{g} \leq$ $C\left(n, \varepsilon, g_{b}\right)$ pointwise. Consequently, we get:
$$\left\|\nabla^{g, 2} f_{g}\right\|_{L^{2}\left(\rho_{g_{b}}^{2} e^{-f_{g}} d \mu_{g}\right)}^{2} \leq C\left(n, \varepsilon, g_{b}\right)\left(\left\|\nabla^{g} f_{g}\right\|_{L^{2}\left(e^{-f_{g}} d \mu_{g}\right)}^{2}+\|\operatorname{Ric}(g)\|_{L^{2}\left(\rho_{g_{b}}^{2} e^{-f_{g}} d \mu_{g}\right)}^{2}\right),$$
which in turn implies:
$$\left\|\nabla^{g, 2} f_{g}\right\|_{L^{2}\left(\rho_{g_{b}}^{2} e^{-f_{g}} d \mu_{g}\right)}^{2} \leq C\left(n, \varepsilon, g_{b}\right)\left(\left\|\nabla^{g} f_{g}\right\|_{L^{2}\left(e^{-f_{g}} d \mu_{g}\right)}^{2}+\|h\|_{H_{\frac{n}{2}-1}^{2}}^{2}\right),$$
thanks to (7.27). Indeed, by Proposition 1.12,
$$\left|w_{g}-1\right|=\left|w_{g}-w_{g_{b}}\right| \leq \frac{1}{2}, \quad g \in B_{C_{\tau}^{2, \alpha}}\left(g_{b}, \varepsilon\right),$$
if $\varepsilon$ is chosen small enough, so that the metrics $w_{g} \cdot g$ and $g$ are uniformly bi-Lipschitz on $N$.
Finally, it remains to estimate $\left\|\nabla^{g} f_{g}\right\|_{L^{2}\left(e^{-f_{g}} d \mu_{g}\right)}$ or equivalently $\left\|\nabla^{g} f_{g}\right\|_{L^{2}}$ from above. Concatenating (7.30) and [(4.1), Proposition 4.1 ] ends the proof of (7.21) in case $g_{1}=g_{b}$ once (7.25) is invoked.

Let us treat the general case, i.e. let $g_{1}$ and $g_{2}$ be two metrics in $B_{C_{\tau}^{2, \alpha}}\left(g_{b}, \varepsilon\right)$, let $h:=g_{2}-g_{1}$ and $g_{t}:=g_{1}+(t-1) h$ for $t \in[1,2]$, and let us estimate the difference of $\nabla \lambda_{\mathrm{ALE}}\left(g_{2}\right)$ and $\nabla \lambda_{\text {ALE }}\left(g_{1}\right)$ with the help of Lemmata C. 1 and C. 2 as follows:
$$\begin{aligned}
& -2 \operatorname{Ric}\left(g_{2}\right)-\mathscr{L}_{\nabla^{g_{2}} f_{g_{2}}}\left(g_{2}\right)+2 \operatorname{Ric}\left(g_{1}\right)+\mathscr{L}^{g_{1}} f_{g_{1}}\left(g_{1}\right) \\
= & L_{g_{1}} h-\mathscr{L}_{B_{g_{1}}(h)}\left(g_{2}\right)+\int_{1}^{2} \frac{\partial}{\partial t} \mathscr{L}^{g_{t}} f_{g_{t}}\left(g_{t}\right) d t+Q\left(h, \nabla^{g_{1}} h, \nabla^{g_{1}, 2} h\right) .
\end{aligned}$$

Now, observe that:
$$\int_{1}^{2} \frac{\partial}{\partial t} \mathscr{L}_{\nabla^{g_{t}} f_{g_{t}}}\left(g_{t}\right) d t=\int_{1}^{2}-\mathscr{L}_{h\left(\nabla^{g_{t}} f_{g_{t}}\right)}\left(g_{t}\right)+\mathscr{L}_{\nabla^{g_{t}} f_{g_{t}}}(h)+\mathscr{L}_{\nabla^{g_{t}}\left(\delta_{g_{t}} f(h)\right)}\left(g_{t}\right) d t .$$
On the one hand, one has
$$\begin{aligned}
\int_{1}^{2}\left|\mathscr{L}_{\nabla^{g_{t} f_{g_{t}}}}(h)\right|_{g_{1}} d t & \lesssim \int_{1}^{2}\left|\nabla^{g_{t}} h\right|_{g_{1}}\left|\nabla^{g_{t}} f_{g_{t}}\right|_{g_{1}}+|h|_{g_{1}}\left|\nabla^{g_{t}, 2} f_{g_{t}}\right|_{g_{1}} d t \\
& \lesssim \rho_{g_{b}}^{-1}\left|\nabla^{g_{1}} h\right|_{g_{1}}\|h\|_{C_{\tau}^{2, \alpha}}+\rho_{g_{b}}^{-2}|h|_{g_{1}}\|h\|_{C_{\tau}^{2, \alpha}} .
\end{aligned}$$
Here, the sign $\lesssim$ means less than or equal up to a positive constant uniform in $t \in[1,2]$ which might depend on $n, g_{b}, \varepsilon$. On the other hand, one has similarly,
$$\begin{aligned}
\left|\int_{1}^{2} \mathscr{L}_{h\left(\nabla^{g_{t}} f_{g_{t}}\right)}\left(g_{t}\right) d t\right|_{g_{1}} & \lesssim \int_{1}^{2}\left|\nabla^{g_{t}}\left(h\left(\nabla^{g_{t}} f_{g_{t}}\right)\right)\right|_{g_{1}} d t \\
& \leq \rho_{g_{b}}^{-1}\left|\nabla^{g_{1}} h\right|_{g_{1}}\|h\|_{C_{\tau}^{2, \alpha}}+\rho_{g_{b}}^{-2}|h|_{g_{1}}\|h\|_{C_{\tau}^{2, \alpha}} .
\end{aligned}$$
Then by (7.32) together with (7.33), (7.34) and (7.35), one has pointwise:
$$\begin{aligned}
\mid \operatorname{Ric}\left(g_{2}\right)+\nabla^{g_{2}, 2} f_{g_{2}}- & \operatorname{Ric}\left(g_{1}\right)-\left.\nabla^{g_{1}, 2} f_{g_{1}}\right|_{g_{1}} \\
& \lesssim\left|L_{g_{1}} h\right|_{g_{1}}+\left|\mathscr{L}_{B_{g_{1}}(h)}\left(g_{1}\right)\right|_{g_{1}}+\int_{1}^{2}\left|\mathscr{L}_{\nabla^{g_{t}}\left(\delta_{g_{t}} f(h)\right)}\left(g_{t}\right)\right|_{g_{1}} d t \\
& +\left|\operatorname{Rm}\left(g_{1}\right)\right|_{g_{1}}|h|_{g_{1}}^{2}+\left|\nabla^{g_{1}} h\right|_{g_{1}}^{2}+|h|_{g_{1}}\left|\nabla^{g_{1}, 2} h\right|_{g_{1}} \\
& +\rho_{g_{b}}^{-1}\left|\nabla^{g_{1}} h\right|_{g_{1}}\|h\|_{C_{\tau}^{2, \alpha}}+\rho_{g_{b}}^{-2}|h|_{g_{1}}\|h\|_{C_{\tau}^{2, \alpha}} \\
& \lesssim\left|L_{g_{1}} h\right|_{g_{1}}+\left|\mathscr{L}_{B_{g_{1}}(h)}\left(g_{1}\right)\right|_{g_{1}}+\int_{1}^{2}\left|\mathscr{L}_{\nabla^{g_{t}}\left(\delta_{g_{t}} f(h)\right)}\left(g_{t}\right)\right|_{g_{1}} d t \\
& +\rho_{g_{b}}^{-1}\left|\nabla^{g_{1}} h\right|_{g_{1}}+\rho_{g_{b}}^{-2}|h|_{g_{1}},
\end{aligned}$$
where we have used the fact that $g_{i} \in B_{C_{\tau}^{2, \alpha}}\left(g_{b}, \varepsilon\right), i=1,2$ in the last line.
Let us notice that by definition of the space $H_{\frac{n}{2}-1}^{2}$ and that of the linear Bianchi gauge given in (C.6),
$$\begin{aligned}
\left\|L_{g_{1}} h\right\|_{L_{\frac{n}{2}+1}^{2}} & \lesssim\left\|\operatorname{Rm}\left(g_{1}\right) * h\right\|_{L_{\frac{n}{2}+1}^{2}}+\left\|\nabla^{g_{1}} h\right\|_{L^{2}}+\left\|\nabla^{g_{1}, 2} h\right\|_{L_{\frac{n}{2}+1}^{2}} \\
& \lesssim\|h\|_{H_{\frac{n}{2}-1}^{2}}, \\
\left\|\mathscr{L}_{B_{g_{1}}(h)}\left(g_{1}\right)\right\|_{L_{\frac{n}{2}+1}^{2}} & \lesssim\left\|\nabla^{g_{1}}\left(\operatorname{div}_{g_{1}} h-\frac{\nabla^{g_{1}} \operatorname{tr}_{g_{1}} h}{2}\right)\right\|_{L_{\frac{n}{2}+1}^{2}} \\
& \lesssim\left\|\nabla^{g_{1}, 2} h\right\|_{L_{\frac{n}{2}+1}^{2}} \lesssim\|h\|_{H_{\frac{n}{2}-1}^{2}},
\end{aligned}$$
which implies that:
$$\begin{aligned}
\| \operatorname{Ric}\left(g_{2}\right)+\nabla^{g_{2}, 2} f_{g_{2}}- & \operatorname{Ric}\left(g_{1}\right)-\nabla^{g_{1}, 2} f_{g_{1}} \|_{L_{\frac{n}{2}+1}^{2}} \\
& \lesssim\|h\|_{H_{\frac{n}{2}-1}^{2}}+\left\|\int_{1}^{2} \mathscr{L}_{\nabla^{g_{t}}\left(\delta_{g_{t}} f(h)\right)}\left(g_{t}\right) d t\right\|_{L_{\frac{n}{2}+1}^{2}} \\
& \lesssim\|h\|_{H_{\frac{n}{2}-1}^{2}}+\int_{1}^{2}\left\|\mathscr{L}_{\nabla^{g_{t}}\left(\delta_{g_{t}} f(h)\right)}\left(g_{t}\right)\right\|_{L^{2}\left(\rho_{g_{b}}^{2} d \mu_{g_{t}}\right)} d t
\end{aligned}$$
Here, we have used Cauchy-Schwarz inequality together with the fact that the metrics $g_{t}$, $t \in[1,2]$ are uniformly equivalent in the last line.

According to (7.25) and (7.36), it remains to control $\left\|\mathscr{L}^{\nabla^{g_{t}}}\left(\delta_{g_{t}} f(h)\right)\left(g_{t}\right)\right\|_{L^{2}\left(e^{-f_{g_{t}}} d \mu_{g_{t}}\right)}$ from above uniformly in $t \in[1,2]$. By using the Bochner formula for the smooth metric measure space $\left(N^{n}, g_{t}, \nabla^{g_{t}} f_{g_{t}}\right)$ endowed with the measure $\mu_{t}:=e^{-f_{g_{t}}} d \mu_{g_{t}}$ :
$$\begin{aligned}
\Delta_{g_{t}, f_{g_{t}}}\left|\nabla^{g_{t}}\left(\delta_{g_{t}} f(h)\right)\right|_{g_{t}}^{2} & :=\left(\Delta_{g_{t}}-\left\langle\nabla^{g_{t}} f_{g_{t}}, \nabla^{g_{t}} \cdot\right\rangle_{g_{t}}\right)\left|\nabla^{g_{t}}\left(\delta_{g_{t}} f(h)\right)\right|_{g_{t}}^{2} \\
& =2\left|\nabla^{g_{t}, 2} \delta_{g_{t}} f(h)\right|_{g_{t}}^{2}+2\left\langle\nabla^{g_{t}} \Delta_{g_{t}, f_{g_{t}}}\left(\delta_{g_{t}} f(h)\right), \nabla^{g_{t}}\left(\delta_{g_{t}} f(h)\right)\right\rangle_{g_{t}} \\
& +2\left(\operatorname{Ric}\left(g_{t}\right)+\nabla^{g_{t}, 2} f_{g_{t}}\right)\left(\nabla^{g_{t}}\left(\delta_{g_{t}} f(h)\right), \nabla^{g_{t}}\left(\delta_{g_{t}} f(h)\right)\right) .
\end{aligned}$$
Therefore we proceed in the same way as we did in (7.29) to get:
$$\left\|\nabla^{g_{t}, 2}\left(\delta_{g_{t}} f(h)\right)\right\|_{L^{2}\left(\rho_{g_{b}}^{2} d \mu_{t}\right)} \lesssim\left\|\Delta_{g_{t}, f_{g_{t}}}\left(\delta_{g_{t}} f(h)\right)\right\|_{L^{2}\left(\rho_{g_{b}}^{2} d \mu_{t}\right)}+\left\|\nabla^{g_{t}}\left(\delta_{g_{t}} f(h)\right)\right\|_{L^{2}\left(d \mu_{t}\right)} .$$
In order to estimate the righthand side of the previous inequality in terms of $\|h\|_{H_{\frac{n}{2}-1}^{2}}$ only, we invoke [(4.2), (4.3), Proposition 4.1 together with the triangular inequality.

Coming back to (7.37), this implies that:
$$\begin{aligned}
\left.\left\|\nabla^{g_{t}, 2}\left(\delta_{g_{t}} f(h)\right)\right\|_{L^{2}\left(\rho_{g_{b}}^{2}\right.}^{2} d \mu_{g_{t}}\right) & \lesssim\left\|\Delta_{g_{t}, f_{g_{t}}}\left(\delta_{g_{t}} f(h)\right)\right\|_{L^{2}\left(\rho_{g_{b}}^{2} d \mu_{g_{t}}\right)}+\left\|\nabla^{g_{t}} h\right\|_{L^{2}} \\
& \lesssim\left\|\nabla^{g_{1}} h\right\|_{L^{2}}+\left\|\nabla^{g_{1}, 2} h\right\|_{L_{\frac{n}{2}+1}^{2}} \lesssim\|h\|_{H_{\frac{n}{2}-1}^{2}} .
\end{aligned}$$
Here we used the fact that $\left|\nabla^{g_{t}} h\right|_{g_{t}} \lesssim\left|\nabla^{g_{1}} h\right|_{g_{1}}+\left|\nabla^{g_{1}}\left(g_{t}-g_{1}\right)\right|_{g_{1}}|h|_{g_{1}}$ to get the second inequality since again, $g_{i} \in B_{C_{\tau}^{2, \alpha}}\left(g_{b}, \varepsilon\right), i=1,2$. This ends the proof of estimate (7.21).

The proof of (7.22) is along the same lines as those of the proof of (7.21). Therefore, we only sketch its main steps. According to Proposition 3.7, the differential of the $L^{2}\left(e^{-f_{g}} d \mu_{g}\right)$ - gradient of $\lambda_{\text {ALE }}$ denoted by $\nabla^{L^{2}\left(e^{-f_{g}} d \mu_{g}\right)} \lambda_{\text {ALE }}$ at a metric $g \in B_{C_{\tau}^{2, \alpha}}\left(g_{b}, \varepsilon\right)$ along a variation $h \in H_{\frac{n}{2}-1}^{2}$ is:
$$\begin{aligned}
2 D_{g}\left(\nabla^{L^{2}\left(e^{-f_{g}} d \mu_{g}\right)} \lambda_{\mathrm{ALE}}\right)(h)= & \Delta_{f_{g}} h+2 \operatorname{Rm}(g)(h)-\mathscr{L}_{B_{f_{g}}(h)}(g) \\
& +h \circ \operatorname{Ric}_{f_{g}}(g)+\operatorname{Ric}_{f_{g}}(g) \circ h-2\left(\frac{\operatorname{tr}_{g} h}{2}-\delta_{g} f(h)\right) \operatorname{Ric}_{f_{g}}(g) .
\end{aligned}$$
As explained in (7.23) at the beginning of the proof of (7.21), dealing either with the $L^{2}\left(e^{-f_{g}} d \mu_{g}\right)$-gradient or the $L^{2}\left(d \mu_{g_{b}}\right)$-gradient of $\lambda_{\text {ALE }}$ lead to the same expected estimate. Linearizing (7.39) applied to $g_{2} \in B_{C_{\tau}^{2, \alpha}}\left(g_{b}, \varepsilon\right)$ at a metric $g_{1} \in B_{C_{\tau}^{2, \alpha}}\left(g_{b}, \varepsilon\right)$ leads to (7.22): indeed, the only difficulty consists in estimating the terms involving $\delta_{g} f(h)$ or equivalently, the
volume variation $\frac{\operatorname{tr}_{g} h}{2}-\delta_{g} f(h)$. This is done with the help of Proposition 3.10 by linearizing (3.11) applied to $g_{2}$ at $g_{1}$ together with the use of Proposition 4.2. \(\square\)

We are in a good position to prove the main result of this section:
Theorem 7.11 (A Łojasiewicz inequality for ALE metrics). Let $\left(N^{n}, g_{b}\right), n \geqslant 4$, be a Ricci-flat ALE metric. Let $\tau \in\left(\frac{n-2}{2}, n-2\right)$ and $\alpha \in(0,1)$. Then the functional $\lambda_{\text {ALE }}$ satisfies the following $L_{\frac{n}{2}+1}^{2}$-Lojasiewicz inequality: there exists $\varepsilon>0$, a constant $C>0$ and $\theta \in(0,1)$ such that for all $g \in B_{C_{\tau}^{2, \alpha}}\left(g_{b}, \varepsilon\right)$ :
$$\left|\lambda_{\mathrm{ALE}}(g)\right|^{2-\theta} \leq C\left\|\operatorname{Ric}(g)+\nabla^{g, 2} f_{g}\right\|_{L_{\frac{n}{2}+1}^{2}}^{2} .$$
Proof. It suffices to prove that the functional $G:=\lambda_{\text {ALE }}$ and its derivatives satisfy the assumptions of Proposition 7.1.

Let us first note that $\lambda_{\text {ALE }}$ is analytic by Proposition 3.4.
Now, the energy estimates (7.1) hold true thanks to [(7.21), Proposition 7.10. Moreover, according to [(2.3), Proposition 2.8] and Proposition 3.4, the gradient of $\lambda_{\text {ALE }}$ in $L^{2}\left(e^{-f_{g}} d \mu_{g}\right)$ is $-\left(\operatorname{Ric}(g)+\nabla^{g, 2} f_{g}\right)$ for $g \in B_{C_{\tau}^{2, \alpha}}\left(g_{b}, \varepsilon\right)$. Condition [2), Proposition 7.1] is ensured by [(7.22), Proposition 7.10].

Next, observe that by Proposition 3.12, the inequality (7.40) is invariant by diffeomorphisms of $N$ in the connected component of the identity such that their generating vector field lies in a neighborhood of $0_{T N}$ in $C_{\tau-1}^{3, \alpha}(T N)$. For this reason, we invoke Proposition B. 2 to restrict our space of metrics to the space $B_{C_{\tau}^{2, \alpha}}\left(g_{b}, \varepsilon\right) \cap E$ where $E:=\operatorname{ker}_{C_{\tau}^{2, \alpha}}\left(\operatorname{div}_{g_{b}}\right)$ and we restrict the image to $C_{\tau+2}^{0, \alpha} \cap F$ with $F:=\operatorname{div}_{g_{b}}^{*}\left(C_{c}^{\infty}(T N)\right)^{\perp}$ as in Lemma 7.9. This space of metrics is the space of divergence-free metrics with respect to $g_{b}$. It is crucial to gauge the diffeomorphism invariance of $\lambda_{\text {ALE }}$ away to expect the Fredholmness of its Hessian.

We will denote $\lambda_{\text {ALE }}^{E}$ the restriction of $\lambda_{\text {ALE }}$ to $E$ which is also analytic.
Since $\left\|\nabla \lambda_{\text {ALE }}^{E}\right\|_{L_{\frac{n}{2}+1}^{2}} \leq\left\|\nabla \lambda_{\text {ALE }}\right\|_{L_{\frac{n}{2}+1}^{2}}$, the inequalities go in the right direction, and it is enough to prove the corresponding Lojasiewicz inequality for $\lambda_{\text {ALE }}^{E}$.

Notice that the linearization of $\nabla \lambda_{\text {ALE }}^{E}$ at $0 \in S^{2} T^{*} N$ is half the Lichnerowicz operator $\frac{1}{2} L_{g_{b}}$ by Proposition 2.7. Proposition 5.1 ensures that $L_{g_{b}}$ is symmetric and is a bounded operator from $C_{\tau}^{2, \alpha}\left(S^{2} T^{*} N\right)$ to $C_{\tau+2}^{0, \alpha}\left(S^{2} T^{*} N\right)$. It is moreover bounded from $H_{\frac{n}{2}-1}^{2}\left(S^{2} T^{*} N\right)$ to $L_{\frac{n}{2}+1}^{2}\left(S^{2} T^{*} N\right)$. The Fredholmness of $L_{g_{b}}$ follows from Proposition 5.1. Conditions (3b) and (3e) are met thanks to Proposition 5.1. This ends the proof of Theorem 7.11. \(\square\)

Let us finally prove that we obtain the optimal exponent in the integrable situation.
Let $g_{b}$ be an integrable Ricci-flat ALE metric. In this situation, the idea is to replace the kernel $\operatorname{ker}_{L^{2}} L_{g_{b}}$ by the actual zero-set of $\lambda_{\text {ALE }}$ among $C_{\tau}^{2, \alpha}$ divergence-free perturbations of $g_{b}$ which is an analytic manifold whose tangent space at $g_{b}$ is $\operatorname{ker}_{L^{2}} L_{g_{b}}$.
Theorem 7.12. Let $\left(N^{n}, g_{b}\right), n \geq 4$, be a Ricci-flat ALE metric whose infinitesimal Ricci-flat deformations are integrable. Let $\tau \in\left(\frac{n-2}{2}, n-2\right)$ and $\alpha \in(0,1)$.

Then there exists $\epsilon>0$ and a constant $C>0$ such that for all $g \in B_{C_{\tau}^{2, \alpha}}\left(g_{b}, \varepsilon\right)$, the following $L_{\frac{n}{2}+1}^{2}$-Lojasiewicz inequality holds:
$$\left|\lambda_{\mathrm{ALE}}(g)\right| \leq C\left\|\operatorname{Ric}(g)+\nabla^{g, 2} f_{g}\right\|_{L_{\frac{n}{2}+1}^{2}}^{2} .$$

In particular, if $n \geq 5$ and $\tau \in\left(\frac{n}{2}, n-2\right)$ then for any $0<\delta<\frac{2 \tau-(n-2)}{2 \tau-(n-4)}$, there exists $C>0$ such that for all $g \in B_{C_{\tau}^{2}, \alpha}\left(g_{b}, \epsilon\right)$, we have the following $L^{2}$-Lojasiewicz inequality:
$$\left|\lambda_{\mathrm{ALE}}(g)\right|^{2-\theta} \leq C\left\|\nabla \lambda_{\mathrm{ALE}}(g)\right\|_{L^{2}}^{2}, \quad \theta:=2-\frac{1}{\delta} .$$
Proof. Denote $W_{g_{b}}:=\left\{\bar{g}_{v}\right.$, for small $\left.v \in \operatorname{ker}_{L^{2}} L_{g_{b}}\right\}$, where the $\bar{g}_{v}$ are the metrics of Definition 6.1. The functional $\lambda_{\text {ALE }}$ and its gradient vanish on $W_{g_{b}}$ since the metrics $\bar{g}_{v}$ are Ricci-flat, and the Lojasiewicz inequality trivially follows on this space.

Let $g$ be $C_{\tau}^{2, \alpha}$-close enough to $g_{b}$. Then, by Proposition 6.2 there exists a unique $\bar{g}_{v} \in W_{g_{b}}$ and a diffeomorphism $\phi: N \rightarrow N$ in the connected component of the identity such that its infinitesimal generator belongs to $C_{\tau-1}^{3, \alpha}(T N)$ and such that
\begin{itemize}
\item[-] $\phi^{*} g-\bar{g}_{v} \perp_{L^{2}\left(\bar{g}_{v}\right)} \operatorname{ker}_{L^{2}\left(\bar{g}_{v}\right)} L_{\bar{g}_{v}}$, and
\item[-] $\operatorname{div}_{\bar{g}_{v}} \phi^{*} g=0$.
\end{itemize}
Therefore, up to changing the reference Ricci-flat metric by a metric in $W_{g_{b}}$, since $\lambda_{\text {ALE }}$ and the $L^{2}$-norm of its gradient are invariant by the pull-back by $\phi$ thanks to Proposition 3.12, the situation is reduced to proving a Lojasiewicz inequality on the orthogonal of the kernel, which is exactly the statement of Lemma 7.8. \(\square\)

\section*{8. Deformation of Ricci-flat ALE metrics, scalar curvature and mass}

Let us now mention some applications of the functional $\lambda_{A L E}$ that we introduced and its properties.

\subsection*{8.1. Local positive mass theorems.}

Let us mention some direct applications of the functional $\lambda_{\text {ALE }}$ and its properties for Ricciflat ALE metrics.

Corollary 8.1. Let $\left(N^{n}, g_{b}\right)$ be a Ricci-flat ALE metric which is either integrable and stable or a local maximizer of $\lambda_{A L E}$ with respect to the $C_{\tau}^{2, \alpha}$-topology. Then any deformation of $g_{b}$ small enough in $C_{\tau}^{2, \alpha}$ which has nonnegative and integrable scalar curvature in $C_{\tau^{\prime}}^{0}$, for some $\tau^{\prime}>n$, satisfies
$$m_{\mathrm{ADM}}(g) \geq 0,$$
with equality on Ricci-flat metrics only.
Proof. Consider $\left(N^{n}, g_{b}\right)$ a stable Ricci-flat ALE. By Proposition 6.6, it is a local maximum for $\lambda_{\text {ALE }}$ in the $C_{\tau}^{2, \alpha}$-topology and therefore, for any metric $g$ sufficiently $C_{\tau}^{2, \alpha}$-close to $g_{b}$, we have $\lambda_{\text {ALE }}^{0}(g) \leq 0$ with equality only if the metric is Ricci-flat. Since $\mathrm{R}_{g} \geq 0$, if $\mathrm{R}_{g} \in L^{1}$ we have $\lambda_{\text {ALE }}^{0}(g) \geq 0$. This implies that the mass is nonnegative :
$$0 \geq \lambda_{\mathrm{ALE}}(g)=\lambda_{\mathrm{ALE}}^{0}(g)-m_{\mathrm{ADM}}(g) \geq-m_{\mathrm{ADM}}(g) .$$
Moreover, if we have equality, we necessarily have $\lambda_{\text {ALE }}(g)=0, \lambda_{\text {ALE }}^{0}(g)=0$ and $m_{\text {ADM }}(g)=$ 0 and since the only maximizers of $\lambda_{\text {ALE }}$ are Ricci-flat, $g$ has to be Ricci-flat. \(\square\)

Remark 8.2. Corollary 8.1 is not a consequence of a previously known positive mass theorem. Actually, the positive mass theorem is known to be false in the ALE context [LeB88].

Finally, notice as in [HHS14] that there are counter-examples to the rigidity part of the positive mass theorem among self-similar solutions to the Ricci flow. Indeed, Feldman, Ilmanen and Knopf [FIK03] have constructed complete expanding gradient Kähler-Ricci solitons on the total space of the tautological line bundles $L^{-k}, k>n$ over $\mathbb{C} \mathbb{P}^{n-1}$. These solutions on $L^{-k}$ are $U(n)$-invariant and asymptotic to the cone $C\left(\mathbb{S}^{2 n-1} / \mathbb{Z}_{k}\right)$ endowed with the Euclidean metric $\frac{1}{2} i \partial \bar{\partial}|\cdot|^{2}$, where $\mathbb{Z}_{k}$ acts on $\mathbb{C}^{n}$ diagonally. The curvature tensor of these solitons decay exponentially fast to 0 at infinity, in particular these metrics are ALE and their mass vanish. On the other hand, the scalar curvature of these metrics is positive everywhere.
Remark 8.3. We can define and control $\lambda_{\text {ALE }}^{0}$ on the example of Feldman-Ilmanen-Knopf, denoted by $g_{\text {FIK }}$. Since for any $s>0$, we have $\lambda_{\text {ALE }}^{0}(s g)=s^{\frac{n}{2}-1} \lambda_{\text {ALE }}^{0}(g)$ by Lemma 1.15, and therefore since their example is an expanding soliton, we can prove that the Ricci flow starting at $g_{\text {FIK }}$ satisfies $\lambda_{\text {ALE }}^{0}\left(g_{\text {FIK }}(t)\right)=(1+c t)^{\frac{n}{2}-1} \lambda_{\text {ALE }}^{0}\left(g_{\text {FIK }}\right)>0$ for some $c>0$. This is in contrast with the compact situation where a Ricci-flow starting at a metric with positive $\lambda$-functional necessarily develops a finite-time singularity.

\subsection*{8.2. Global properties on spin manifolds.}

On spin 4-manifolds, the stability of Ricci-flat ALE metrics as maximizers of $\lambda_{A L E}$ is ensured globally.
Proposition 8.4. Let $\left(N^{4}, g\right)$ be an ALE metric of order $\tau>1=\frac{4-2}{2}$ on a spin manifold asymptotic to $\mathbb{R}^{4} / \Gamma$ for $\Gamma \subset \operatorname{SU}(2)$. Assume the scalar curvature $\mathrm{R}_{g}$ is integrable and nonnegative. Then, we have
$$\lambda_{\mathrm{ALE}}(g) \leq 0,$$
with equality if and only if $\left(N^{4}, g\right)$ is a hyperkähler (Ricci-flat) ALE metric.
Proof. First of all, Lemma 1.15 ensures the finiteness of $\lambda_{\text {ALE }}(g)$ under such assumptions on the scalar curvature. Witten's formula [Wit81] for the mass on spin asymptotically Euclidean manifolds which was extended by Nakajima [Nak90] to spin ALE metrics with group in $S U(2)$, states that there exists $\psi$, a Dirac spinor asymptotic to a constant spinor with unit-norm for which
$$m_{\mathrm{ADM}}(g)=\int_{N}\left(4\left|\nabla^{g} \psi\right|_{g}^{2}+\mathrm{R}_{g}|\psi|_{g}^{2}\right) d \mu_{g}$$
Using $w=|\psi|_{g}$ as a test function and Kato's inequality $\left|\nabla^{g} \psi\right|_{g} \geq\left.\left.\left|\nabla^{g}\right| \psi\right|_{g}\right|_{g}$, we find a lower bound
$$m_{\mathrm{ADM}}(g) \geq \lambda_{\mathrm{ALE}}^{0}(g)$$
similarly to [Has11].
Now, according to [CGH00, (3.9)], Dirac spinors satisfy a pointwise improved Kato inequality, and we have $\sqrt{1-\frac{1}{4}}\left|\nabla^{g} \psi\right|_{g} \geqslant\left.\left.\left|\nabla^{g}\right| \psi\right|_{g}\right|_{g}$. The equality $m_{\text {ADM }}(g)=\lambda_{\text {ALE }}^{0}(g)$ therefore implies that the spinor is parallel. Then one conclude that the ALE metric $g$ under consideration is hyperkähler: see [Nak90, Proof of Theorem 3.3] for a proof of this fact. \(\square\)

Remark 8.5. We therefore recover that Ricci-flat ALE metrics on spin manifolds are stable (they are actually hyperkähler by [Nak90]). Recall that it is a folklore conjecture (see [BKN89, Section 1, 3)] for instance) that all 4-dimensional simply connected ALE Ricci-flat metrics are hyperkähler. In light of the results of this paper, it is tempting to study the stability of 4-dimensional Ricci-flat ALE metrics as a first step towards the previous conjecture.

\section*{Appendix A. Real analytic maps between Banach spaces}

Let us recall some basic definitions and theorems about real analytic maps between Banach spaces and real analytic submanifolds.

Let $a_{k}: V^{k} \rightarrow W, k \in \mathbb{N}$ be a symmetric $k$-linear form on $V$ taking values in $W$. The power series in $x$ denoted $x \in V \mapsto \sum_{k} a_{k} x^{k} \in W$ from the Banach space $V$ with values in the Banach space $W$ is defined as the sum of the $a_{k}(x, \ldots, x)$. We will say that it is converging if the real sum $\sum_{k}\left\|a_{k}(x, \ldots, x)\right\|_{W}$ converges.
Definition A. 1 (Real analytic map). Let $V$ and $W$ be Banach spaces, and $U$ an open subset of $V$. A map $f: V \rightarrow W$ is real analytic if for each point $x \in U, f$ is equal to a power series converging in a neighborhood of $x$.

This definition is adapted to the techniques of analysis, and in particular, thanks to [Whi65, Implicit Function Theorem, p. 1081], the implicit function theorem holds for this regularity.
Lemma A. 2 ([Whi65, Implicit Function Theorem, p. 1081]). Let $X, Y$ and $Z$ be Banach spaces, and $A$ an open subset of $X \times Y$. Assume that a real analytic map $f: A \rightarrow Z$ satisfies for $\left(x_{0}, y_{0}\right) \in A$,
\begin{itemize}
\item[(1)] $f\left(x_{0}, y_{0}\right)=0$,
\item[(2)] $d_{\left(x_{0}, y_{0}\right)} f(0,):. Y \mapsto Z$ is a topological isomorphism.
\end{itemize}
Then,
\begin{itemize}
\item[(1)] there exists $N\left(x_{0}\right)$, an open neighborhood of $x_{0}$ in $X$ and a unique continuous map $g: N\left(x_{0}\right) \rightarrow Y$ such that $g\left(x_{0}\right)=y_{0},(x, g(x)) \in A$ for $x \in N\left(x_{0}\right)$, and
$$f(x, g(x))=0,$$
\item[(2)] $g$ is real analytic,
\item[(3)] $d_{x} g=-\left(d_{(x, g(x))} f(0, .)\right)^{-1} \circ\left(d_{(x, g(x))} f(., 0)\right)$.
\end{itemize}

It will be crucial for us to note that usual operations on tensors are real analytic between Hölder spaces whose regularity is higher than the number of derivatives involved. This can be proved by adapting the proof of [Koi83, Lemma 13.7] which deals with $H^{s}$-regularity for $s>0$ large enough to the Hölder context thanks to the theory developped in [Pal68]. This also holds between weighted Hölder spaces as long as the weight makes the multiplication of two functions continuous.

Lemma A.3. The operations of derivation, multiplication, contraction and integration are analytic between Hölder or between weighted Hölder spaces in which the multiplication is continuous. That is, denoting $C_{\tau}^{k, \alpha}$ one of the spaces of the present article, as long as there exists $C>0$ such that for any two functions $f, g \in C^{k, \alpha}$, we have
$$\|f g\|_{C_{\tau}^{k, \alpha}} \leq C\|f\|_{C_{\tau}^{k, \alpha}}\|g\|_{C_{\tau}^{k, \alpha}} .$$
One can check that with the spaces of Definition 1.3, this is satisfied as long as $\tau>0$. By construction, the derivation is also continuous.

\section*{Appendix B. Divergence-free gauging of asymptotically conical spaces}

As usual in geometrically covariant problems, one needs to fix a gauge transverse to the action of the diffeomorphism group to use elliptic theory in order to study the equation $\operatorname{Ric}(g)=0$. In this particular situation, a natural gauge is the divergence-free gauge because of the simplification of the expression of the second variation of the $\lambda_{\text {ALE }}^{0}$ functional,
see Remark 2.8. We will prove with the help of the inverse function theorem that in a suitable neighborhood of an asymptotically conical Ricci-flat metric, it is possible to construct divergence-free gauges. That is, given $\left(N^{n}, g_{b}\right)$ a fixed Ricci-flat asymptotically conical (AC) metric, for any metric $g$ close enough to $g_{b}$, there exists a diffeomorphism $\phi: N \rightarrow N$ such that
$$\operatorname{div}_{g_{b}} \phi^{*} g=0 .$$

We will actually work in the larger class of asymptotically conical metrics in this appendix as most of the analysis is exactly the same.
Definition B. 1 (Asymptotically conical manifolds). We will call a Riemannian manifold $\left(N^{n}, g\right)$ asymptotically conical (AC) of order $\tau>0$ if the following holds : there exists a compact set $K \subset N$, a radius $R>0,\left(S, g_{S}\right)$ a closed Riemannian manifold and a smooth diffeomorphism $\Phi: S \times[R,+\infty) \mapsto N \backslash K$ such that, denoting $g_{C(S)}:=d r^{2}+r^{2} g_{S}$, we have, for all $k \in \mathbb{N}$,
$$\rho^{k}\left|\nabla_{g_{C(S)}}^{k}\left(\Phi^{*} g-g_{C(S)}\right)\right|_{e}=O\left(\rho^{-\tau}\right),$$
on $S \times[R,+\infty)$, where $\rho=\max \left\{1, d_{C(S)}(., 0)\right\}$.
The main result of this section is the following.
Proposition B.2. Let $\left(N^{n}, g_{b}\right)$ be a non-flat Ricci-flat manifold asymptotic to a smooth Ricci-flat cone $\left(C\left(S^{n-1}\right), g_{S}\right)$.

Then, for all $k \in \mathbb{N}^{*}, \alpha \in(0,1)$ and for all $1<\beta \leq n-1$, there exists $\epsilon>0$ such that for any metric $g \in B_{C_{\beta}^{k, \alpha}}\left(g_{b}, \varepsilon\right)$ such that
$$\left\|g-g_{b}\right\|_{C_{\beta}^{k, \alpha}} \leq \epsilon,$$
there exists a vector field $X \in C_{\beta-1}^{k+1, \alpha}(T N)$ satisfying,
$$\operatorname{div}_{g_{b}}\left(\left(\exp _{X}^{g_{b}}\right)^{*} g\right)=0,$$
where $\exp _{X}$ is the diffeomorphism $\exp _{X}^{g_{b}}: x \in N \mapsto \exp _{x}^{g_{b}}(X(x))$. Moreover, there exists $C=C\left(g_{b}, k, \alpha, \beta\right)>0$ such that we have
$$\left\|\left(\exp _{X}^{g_{b}}\right)^{*} g-g\right\|_{C_{\beta}^{k, \alpha}} \leq C\|X\|_{C_{\beta-1}^{k+1, \alpha}} \leq C^{2}\left\|\operatorname{div}_{g_{b}} g\right\|_{C_{\beta+1}^{k-1, \alpha}},$$
and we can choose $X$ depending analytically on $g$.
If $\left(N^{n}, g_{b}\right)$ is $A L E$, that is if $\left(C\left(S^{n-1}\right), g_{S}\right)=\left(\mathbb{R}^{n} / \Gamma, g_{e}\right)$ for $\Gamma \subset S O(n)$ acting freely on $\mathbb{S}^{n-1}$, then, the result holds for $1<\beta<n$. Moreover, the above vector field $X$ is unique and depends analytically on $g$.

Remark B.3. The result holds on Euclidean space $\mathbb{R}^{n}$ for $1<\beta<n-1$.
Remark B.4. A completely analogous proof would give the same result for the Bianchi gauge. However, we cannot do the same to cancel out $\partial_{i} h_{i j}-\partial_{j} h_{i i}=\operatorname{div}_{g_{b}}(g)-\nabla^{g_{b}} \operatorname{tr}_{g_{b}}(g)$ thanks to the action of a diffeomorphism since the linearized equation is $d^{*} d$ which is not elliptic. This is consistent with the fact that the mass and the integrability of the curvature are invariant by diffeomorphisms.

Remark B.5. The assumption $\beta>1$ is not linked to any Fredholm property of the operator we will look at. It is however important to ensure for instance that the product of two functions
$$(u, v) \in C_{\beta-1}^{2, \alpha} \times C_{\beta-1}^{2, \alpha} \mapsto u . v \in C_{\beta-1}^{2, \alpha},$$
is continuous. This fact is necessary to prove that our operators are analytic.