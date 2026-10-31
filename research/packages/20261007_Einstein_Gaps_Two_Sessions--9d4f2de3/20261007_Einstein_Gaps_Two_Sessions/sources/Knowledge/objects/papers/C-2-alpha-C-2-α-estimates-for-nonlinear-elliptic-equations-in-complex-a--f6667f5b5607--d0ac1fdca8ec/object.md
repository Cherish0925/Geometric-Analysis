# $$C^{2,\alpha }$$ C 2 , α estimates for nonlinear elliptic equations in complex and almost complex geometry

- Category: papers
- Identity: doi:10.1007/s00526-014-0791-0
- Content status: fulltext_ok

---

---
source_file: 1402_0554.pdf
converter: mathpix
format: mmd
---

\title{
$C^{2, \alpha}$ ESTIMATES FOR NONLINEAR ELLIPTIC EQUATIONS IN COMPLEX AND ALMOST COMPLEX GEOMETRY
}

\author{
VALENTINO TOSATTI, YU WANG, BEN WEINKOVE, AND XIAOKUI YANG
}

\begin{abstract}
We describe how to use the perturbation theory of Caffarelli to prove Evans-Krylov type $C^{2, \alpha}$ estimates for solutions of non-linear elliptic equations in complex geometry, assuming a bound on the Laplacian of the solution. Our results can be used to replace the various Evans-Krylov type arguments in the complex geometry literature with a sharper and more unified approach. In addition, our methods extend to almost-complex manifolds, and we use this to obtain a new local estimate for an equation of Donaldson.
\end{abstract}

\section*{1. Introduction}

The Evans-Krylov theorem [22, 38] for nonlinear elliptic equations
$$F\left(D^{2} u\right)=f$$
with $F$ concave, has long been used in the study of PDEs to show that bounds on $u$ and $D^{2} u$ imply $C^{2, \alpha}$ bounds on $u$ for some $\alpha>0$. This theory applies whenever $f$ is suitably bounded and the bounds on $u$ imply uniform ellipticity. This scenario appears in the study of many PDEs, including the real Monge-Ampère equation, the $\sigma_{k}$-equations and their differentialgeometric counterparts.

At the same time, nonlinear concave operators occur frequently in the study of complex geometry. Complex-differential techniques often yield the estimates
$$\|u\|_{L^{\infty}} \leqslant K, \quad \Delta u \leqslant K,$$
and one would like to conclude that $u$ is bounded in $C^{2, \alpha}$. In the examples, as we will see, the bound on the Laplacian of $u$ typically gives bounds for the complex Hessian of $u$, but not on the real Hessian of $u$.

Up until recently there have been two approaches to the $C^{2, \alpha}$ estimate in complex geometry. The first is to carefully reprove the Evans-Krylov estimates in the complex setting by differentiating the equation twice in complex coordinates and using concavity together with a Harnack inequality. The second approach is to establish estimates on the real Hessian $D^{2} u$, using bounds that one typically has on the complex Hessian, and then apply

\footnotetext{
Research supported in part by NSF grants DMS-1236969, DMS-1308988 and DMS-1332196. The first named-author is supported in part by a Sloan Research Fellowship.
}
the real Evans-Krylov theory referred to above. Both approaches require considerable work to carry out, and are also suboptimal, in the sense that the $C^{2, \alpha}$ estimates depend on two derivatives of $f$.

Recently the second-named author showed that [65], for the complex Monge-Ampère equation,
$$\operatorname{det}\left(\frac{\partial^{2} u}{\partial z^{i} \partial \bar{z}^{j}}\right)=e^{\psi},$$
one can instead directly apply the theory of Caffarelli [3] to obtain local $C^{2, \alpha}$ estimates depending only on the constant $K$ of (1.1) and a Hölder estimate of $\psi$. This settled a regularity issue in complex geometry related to [12] (see also [19]).

In this paper, we generalize the method of [65] to a number of nonlinear equations which naturally occur in complex (and almost complex) geometry. We show that for these equations, under the assumptions (1.1), the $C^{2, \alpha}$ estimates follow from the general nonlinear PDE theory developed by Caffarelli. This can replace the menagerie of arguments in the literature by a single unified theorem. Moreover, we hope that our results can be used as a convenient "black box" in the future study of elliptic equations in complex geometry.

We should stress that the contributions of this paper are not to the general theory of real nonlinear elliptic PDE. Rather our aim is to demonstrate how the existing PDE theory (some of which may be unfamiliar to complex geometers) can be used to simplify and improve the $C^{2, \alpha}$ estimate for many examples of elliptic equations appearing in complex geometry.

We now describe the various equations in complex geometry for which our results can be applied. Let $(M, J, \omega)$ be a compact Hermitian manifold. Suppose that the real-valued function $u \in C^{2}(M)$ satisfies
$$\|u\|_{L^{\infty}(M)} \leqslant K, \text { and } \Delta u \leqslant K,$$
where
$$\Delta u=\frac{n \omega^{n-1} \wedge \sqrt{-1} \partial \bar{\partial} u}{\omega^{n}}$$
is the complex Laplacian associated to $\omega$. Note that in all of the cases described below, the $L^{\infty}$ bound on $u$ could be replaced by a normalization condition, say $\int_{M} u=0$, once the Laplacian bound is given.

Assume that $\psi \in C^{\alpha_{0}}(M)$ and $\chi$ is a real $(1,1)$ form with coefficients in $C^{\beta}(M)$. We allow the possibility that $\chi$ and $\psi$ depend on $u$, and indeed this is important for our applications. We consider $u$ satisfying one of the following equations.

The complex Monge-Ampère equation:
$$\begin{aligned}
(\chi+\sqrt{-1} \partial \bar{\partial} u)^{n} & =e^{\psi} \omega^{n} \\
\chi+\sqrt{-1} \partial \bar{\partial} u & >0 .
\end{aligned}$$

The complex Hessian equations: for a fixed $k=2, \ldots, n-1$,
$$\begin{aligned}
& (\chi+\sqrt{-1} \partial \bar{\partial} u)^{k} \wedge \omega^{n-k}=e^{\psi} \omega^{n}, \\
& (\chi+\sqrt{-1} \partial \bar{\partial} u)^{j} \wedge \omega^{n-j}>0, \quad \text { for } j=1, \ldots, k .
\end{aligned}$$
The complex $\sigma_{n} / \sigma_{k}$ equations: for a fixed $k=2, \ldots, n-1$,
$$\begin{aligned}
(\chi+\sqrt{-1} \partial \bar{\partial} u)^{k} \wedge \omega^{n-k} & =e^{\psi}(\chi+\sqrt{-1} \partial \bar{\partial} u)^{n} \\
\chi+\sqrt{-1} \partial \bar{\partial} u & >0 .
\end{aligned}$$
The Monge-Ampère equation for $(n-1)$-plurisubharmonic equations:
$$\begin{gathered}
\left(\chi+\frac{1}{n-1}((\Delta u) \omega-\sqrt{-1} \partial \bar{\partial} u)\right)^{n}=e^{\psi} \omega^{n} \\
\chi+\frac{1}{n-1}((\Delta u) \omega-\sqrt{-1} \partial \bar{\partial} u)>0 .
\end{gathered}$$
The $(n-1)$-plurisubharmonic version of the complex Hessian and $\sigma_{n} / \sigma_{k}$ equations:
$$\begin{aligned}
& \text { replace } \sqrt{-1} \partial \bar{\partial} u \text { by } \frac{1}{n-1}((\Delta u) \omega-\sqrt{-1} \partial \bar{\partial} u) \\
& \text { and suppose } u \text { satisfies one of (1.4) or (1.5). }
\end{aligned}$$
Almost complex versions of all of the above. Replace ( $M, J, \omega$ ) Hermitian by $(M, J, \omega)$ almost Hermitian, $\chi$ by a real $(1,1)$ form w.r.t. $J$ and $\sqrt{-1} \partial \bar{\partial} u$ by $\frac{1}{2}(d J d u)^{(1,1)}$ and suppose that
$$\begin{gathered}
\text { with these replacements, } \\
u \text { satisfies one of (1.3), }(1.4),(1.5),(1.6) \text { or (1.7). }
\end{gathered}$$

Our main result is:
Theorem 1.1. Assume that $u \in C^{2}(M)$ satisfies (1.2) on $(M, J, \omega)$ and any one of (1.3), (1.4), (1.5), (1.6), (1.7) or (1.8). Then
$$\|u\|_{C^{2, \alpha}(M)} \leqslant C,$$
where $\alpha, C$ depend only on $n, \beta,(M, J, \omega), K,\|\psi\|_{C^{\alpha_{0}}}$ and $\|\chi\|_{C^{\beta}}$.
A first remark is that although we have stated the results for compact $M$, this is only for convenience. All our estimates and results are purely local.

We now discuss each of the equations (1.3), (1.4), (1.5), (1.6), (1.7) and (1.8) in turn, describing briefly some of the existing results in the literature.

We begin with the complex Monge-Ampère equation (1.3) when $\chi$ is a fixed Kähler metric (i.e. $\chi>0$ and $d \chi=0$ ). Global existence of solutions was proved in the seminal work of Yau [71], in which he used Calabi's third order estimate [7] to establish the $C^{2, \alpha}$ estimate. This estimate depends on three derivatives of $\psi$. A direct proof depending on two derivatives of $\psi$, using the Evans-Krylov approach, was given by Siu [50] (cf. Trudinger [63]). A $C^{2, \alpha}$ estimate depending only on the Hölder bound for $\psi$, but also on a bound for the real Hessian of $u$ was given by Dinew-Zhang-Zhang [19]. As discussed above, the second-named author [65] established the result of

Theorem 1.1 in the case of the complex Monge-Ampère equation (under slightly weaker hypotheses for $u$ ).

In the general setting of a fixed Hermitian metric $\chi$, the existence of solutions to the complex Monge-Ampère equation (1.3) was established by Cherrier [13] for $n=2$ (and in higher dimensions with additional hypotheses) and by the first and third-named authors in general [56]. Cherrier [13] established a $C^{2, \alpha}$ bound via a Calabi-type third order estimate. Guan-Li [30] proved a $C^{2, \alpha}$ estimate by first establishing a bound on the real Hessian of $u$ using a maximum principle argument and then applying the usual Evans-Krylov theory. In [55], a direct Evans-Krylov argument was given, following a similar approach to that given in the notes of Siu [50]. All of these existing estimates depend on at least two derivatives of $\psi$. Theorem 1.1 can replace and improve these results.

The complex Hessian equations (1.4) with $\chi=\omega$ Kähler were solved by Dinew-Kołodziej [18], who made use of estimates of Hou [34] and Hou-Ma-Wu [35]. For related works see [1, 17, 36, 39, 44, 45]. A $C^{2, \alpha}$ estimate in this case was proved by Jbilou [36] by bounding the real Hessian and then applying the real Evans-Krylov theory (see also [34], [37]).

The $\sigma_{n} / \sigma_{k}$ equations for $k=n-1$ and $\chi$ a fixed Kähler metric was introduced by Donaldson [20] in the context of global complex geometry. When $n=2$, Chen [10] observed that the equation reduces to the complex Monge-Ampère equation (1.3). Necessary and sufficient conditions for existence of solutions for $k=n-1$ were given by Song-Weinkove [51] using a parabolic method (see [11, 68, 69]). For general $k$, the analogous result was proved by Fang-Lai-Ma [23], again using a parabolic equation. The elliptic equation, for $\chi$ a Hermitian metric, was solved by Sun [53] (see also the work of Guan-Sun [31] and Li [40]). In particular, Sun established the elliptic Evans-Krylov $C^{2, \alpha}$ estimate [53], again depending on two derivatives of $\psi$.

The Monge-Ampère equation for $(n-1)$-plurisubharmonic functions (1.6) has appeared in the literature in various forms, corresponding to different choices of $\chi$ and $\omega$. Harvey-Lawson introduced this equation and the notion of $(n-1)$-plurisubharmonic functions in $\mathbb{C}^{n}$ [32]. In the case of compact manifolds, the simplest case is when $\chi$ is a fixed Hermitian metric and $\omega$ is Kähler. This was introduced and investigated by Fu-Wang-Wu [25, 26], motivated by some questions related to mathematical physics (see [41, 27], for example). The equation (1.6) in this setting was solved by the first and third-named authors [60], and then more recently extended to the case of $\omega$ Hermitian [61].

Another important setup for equation (1.6) is the case
$$\chi=\chi_{0}+* E,$$
where $\chi_{0}$ is a Hermitian metric, $*$ is the Hermitian Hodge star operator of $\omega$, and
$$E=\frac{1}{(n-1)!} \operatorname{Re}\left(\sqrt{-1} \partial u \wedge \bar{\partial}\left(\omega^{n-2}\right)\right) .$$

Note that Theorem 1.2 still applies, because by the bounds (1.2) we conclude that $\|\nabla u\|_{C^{\beta}(M)} \leqslant C$, for a uniform constant $C$, and hence $\chi$ has a uniform $C^{\beta}$ bound. The equation (1.6) with this choice of $\chi$ was introduced by Popovici [48], motivated by some questions in algebraic geometry, and was also studied by the first and third-named authors [61] as an approach towards a conjecture of Gauduchon [28]. The general question of existence of solutions remains open.

There is yet another natural choice of $\chi$ in (1.6):
$$\chi=\chi_{0}+2 * E+u \sqrt{-1} \partial \bar{\partial}\left(\omega^{n-2}\right),$$
where $\chi_{0}$ is a Hermitian metric, and $* E$ is the same as above. In this case,
$$\chi+\frac{1}{n-1}((\Delta u) \omega-\sqrt{-1} \partial \bar{\partial} u)=*\left(\omega_{0}^{n-1}+\sqrt{-1} \partial \bar{\partial}\left(u \omega^{n-2}\right)\right),$$
where $\omega_{0}$ is Hermitian and $\omega_{0}^{n-1}+\sqrt{-1} \partial \bar{\partial}\left(u \omega^{n-2}\right)$ is a positive $(n-1, n-1)$ form. This choice of $\chi$ gives an equation introduced by Fu-Wang-Wu [25]. It is not known in general whether it can be solved (except when $\omega$ is Kähler [60].)

The $C^{2, \alpha}$ estimates for (1.6) in the above settings (again, depending on two derivatives of $\psi$ ) were established in [25, 60, 61] by adapting the usual Evans-Krylov approach. Theorem 1.1 replaces and sharpens these arguments.

As far as we know, the equations (1.7) have yet to be studied, at least in these explicit forms on compact manifolds. However, we have included these equations since they appear to be natural PDEs which easily fit into our setting.

The Dirichlet problem for the almost complex Monge-Ampère equation (1.8) has been solved in various settings by Harvey-Lawson [33] and Pliś [47]. A related, but different, equation in the almost complex case was investigated by Delanoë [16]. Donaldson's Calabi-Yau equation for almost Kähler forms [21], which is not ostensibly of the form (1.8), does in fact fit into this setting. Evans-Krylov results were proved for this equation in [70] and [62]. In Section 5 below, we describe Donaldson's equation and how our results can be used to prove a new local Evans-Krylov estimate (Theorem 5.1).

We next describe the local PDE theorem which we use to prove Theorem 1.1. This PDE theorem is a consequence of results of Caffarelli [3] and ideas adapted from the work of the second-named author [65] (see also [49]). We have packaged the theorem in a way to make it easy to apply to our examples.

Let $B_{1}$ be the unit ball in $\mathbb{R}^{2 n}$. Write $\operatorname{Sym}(2 n)$ for the space of symmetric $2 n \times 2 n$ matrices with real entries. We consider equations of the form
$$F\left(S(x)+T\left(D^{2} u(x), x\right), x\right)=f(x), \quad \text { for } f \in C^{\alpha_{0}}, x \in B_{1},$$
where
$$\begin{aligned}
& F: \operatorname{Sym}(2 n) \times B_{1} \rightarrow \mathbb{R}, \\
& S: B_{1} \rightarrow \operatorname{Sym}(2 n), \\
& T: \operatorname{Sym}(2 n) \times B_{1} \rightarrow \operatorname{Sym}(2 n) .
\end{aligned}$$
For any $A \in \operatorname{Sym}(2 n)$ will denote by $\|A\|$ its operator norm, i.e. the maximum of the absolute value of the eigenvalues of $A$. We impose the following structure conditions on $F, S$ and $T$. We assume that there exists a compact convex set $\mathcal{E} \subset \operatorname{Sym}(2 n)$, positive constants $\lambda, \Lambda, K$ and $\beta \in(0,1)$ such that the following hold.

H1: $F$ is of class $C^{1}$ in $U \times B_{1}$ where $U$ is a neighborhood of $\mathcal{E}$ and
\begin{itemize}
\item[(1)] $F$ is uniformly elliptic in $\mathcal{E}$ :
$$\lambda|\xi|^{2} \leqslant \sum_{i, j} F_{i j}(A, x) \xi^{i} \xi^{j} \leqslant \Lambda|\xi|^{2},$$
for all $A \in \mathcal{E}, \xi \in \mathbb{R}^{2 n}, x \in B_{1}$, where $F_{i j}(A, x)=\frac{\partial F}{\partial A_{i j}}(A, x)$.
\item[(2)] $F$ is concave in $\mathcal{E}$ :
$$F\left(\frac{A+B}{2}, x\right) \geqslant \frac{1}{2} F(A, x)+\frac{1}{2} F(B, x), \quad \text { for all } A, B \in \mathcal{E}, x \in B_{1} .$$
\item[(3)] $F$ has the following uniform Hölder bound in $x$ :
$$|F(N, x)-F(N, y)| \leqslant K|x-y|^{\beta}, \quad \text { for all } N \in \mathcal{E}, x, y \in B_{1},$$
and $|F(N, 0)| \leqslant K$, for all $N \in \mathcal{E}$.
\end{itemize}

H2: The map $T: \operatorname{Sym}(2 n) \times B_{1} \rightarrow \operatorname{Sym}(2 n)$ satisfies the following conditions:
\begin{itemize}
\item[(1)] For all $x, y \in B_{1}$ and all $N \in \operatorname{Sym}(2 n)$,
$$\frac{\|T(N, x)-T(N, y)\|}{\|N\|+1} \leqslant K|x-y|^{\beta} .$$
\item[(2)] For each fixed $x \in B_{1}$, the map $N \mapsto T(N, x)$ is linear on $\operatorname{Sym}(2 n)$.
\item[(3)] For all $P \geqslant 0$ and $x \in B_{1}$,
$$T(P, x) \geqslant 0, \text { and } K^{-1}\|P\| \leqslant\|T(P, x)\| \leqslant K\|P\| .$$
\end{itemize}

H3: $S: B_{1} \rightarrow \operatorname{Sym}(2 n)$ has a uniform $C^{\beta}$ bound:
$$\|S(x)-S(y)\| \leqslant K|x-y|^{\beta}, \quad \text { for all } x, y \in B_{1}$$
and $\|S(0)\| \leqslant K$.
The result is:
Theorem 1.2. With the assumptions above, suppose that $u \in C^{2}\left(B_{1}\right)$ solves (1.9) and satisfies
$$S(x)+T\left(D^{2} u(x), x\right) \in \mathcal{E}, \quad \text { for all } x \in B_{1} .$$

Then $u \in C^{2, \alpha}\left(B_{1 / 2}\right)$ and
$$\|u\|_{C^{2, \alpha}\left(B_{1 / 2}\right)} \leqslant C,$$
where $\alpha, C$ depend only on $\alpha_{0}, K, n, \Lambda, \lambda, \beta,\|f\|_{C^{\alpha_{0}}}$ and $\|u\|_{L^{\infty}\left(B_{1}\right)}$.
The above interior estimate can immediately be applied to each local chart for equations on a compact manifold to obtain a global estimate.

Remark 1.3. We also expect a parabolic version of the above theorem to hold (cf. [66]). This would be useful in providing a unified approach to parabolic Hölder estimates for parabolic flows in complex geometry, including the Kähler-Ricci flow, the Chern-Ricci flow, the J-flow and their generalizations (see [8, 9, 46, 14, 29, 59, 11, 68, 23] for example).

The outline of the paper is as follows. In Section 2 we describe how to apply Theorem 1.2 to obtain Theorem 1.1. In Section 3 we briefly describe the relevant Evans-Krylov-Caffarelli theory that we need, and then in Section 4 we use it to establish Theorem 1.2. Finally in Section 5 we describe an application of our results to an equation of Donaldson.

\section*{2. Equations on complex and almost complex manifolds}

In this section, we give the proof of Theorem 1.1. First, pick a chart in $M$ which is identified with the unit ball $B_{1}$ in $\mathbb{C}^{n}$ with local coordinates $\left(z^{1}, \ldots, z^{n}\right)$. In these coordinates we write
$$\omega=\sqrt{-1} \sum_{i, j} g_{i j} d z^{i} \wedge d \bar{z}^{j},$$
where $\left(g_{i \bar{j}}(x)\right)$ is a positive definite $n \times n$ Hermitian matrix at each point $x \in B_{1}$. Similarly, we write
$$\chi=\sqrt{-1} \sum_{i, j} h_{i \bar{j}} d z^{i} \wedge d \bar{z}^{j},$$
for $\left(h_{i \bar{j}}(x)\right)$ an $n \times n$ Hermitian matrix (not necessarily positive definite). Furthermore we have $\sqrt{-1} \partial \bar{\partial} u=\sqrt{-1} \sum_{i, j} u_{i \bar{j}} d z^{i} \wedge d \bar{z}^{j}$, where $u_{i \bar{j}}=\frac{\partial^{2} u}{\partial z^{i} \partial \bar{z}^{j}}$ is the complex Hessian of $u$.

We also have real coordinates $x^{1}, \ldots, x^{2 n}$ on $B_{1}$ defined by
$$z^{i}=x^{i}+\sqrt{-1} x^{n+i}, \quad \text { for } i=1, \ldots, n .$$
The standard complex structure on $\mathbb{C}^{n}$ corresponds to an endomorphism $J$ of the real tangent space to $B_{1}$. The endomorphism $J$ sends $\partial / \partial x^{i}$ to $\partial / \partial x^{n+i}$ and $\partial / \partial x^{n+i}$ to $-\partial / \partial x^{i}$. As a matrix,
$$J=\left(\begin{array}{cc}
0 & -I_{n} \\
I_{n} & 0
\end{array}\right),$$
for $I_{n}$ the $n \times n$ identity matrix.

In the standard way, we can identify Hermitian $n \times n$ matrices with the subset of $\operatorname{Sym}(2 n)$ given by $J$-invariant matrices. Namely, for $H$ a Hermitian matrix, we write $H=A+\sqrt{-1} B$ with $A, B$ real $n \times n$ matrices, and define
$$\iota(H)=\left(\begin{array}{cc}
A & B \\
-B & A
\end{array}\right) \in \operatorname{Sym}(2 n) .$$
Note that if $H_{1}, H_{2}$ are two Hermitian matrices then
$$H_{1} \leqslant H_{2} \quad \Longleftrightarrow \quad \iota\left(H_{1}\right) \leqslant \iota\left(H_{2}\right) .$$
Moreover, observe that
$$\iota\left(2 u_{i \bar{j}}(x)\right)=\mathrm{p}\left(D^{2} u(x)\right),$$
for
$$\mathrm{p}(N):=\frac{1}{2}\left(N+J^{T} N J\right),$$
the projection onto the $J$-invariant part. The image of $\iota$ is equal to the image of p.

The complex Monge-Ampère equation (1.3). Define $S(x)=\iota\left(2 h_{i \bar{j}}(x)\right)$ and $T(N, x)=\mathrm{p}(N)$. Notice that $T\left(D^{2} u(x), x\right)=\iota\left(2 u_{i \bar{j}}(x)\right)$.

Next observe that the assumption $\Delta u \leqslant K$ implies that the positive $(1,1)$ form $\chi+\sqrt{-1} \partial \bar{\partial} u$ is bounded from above. Moreover, the equation (1.3) together with the arithmetic-geometric means inequality gives a lower bound for $\chi+\sqrt{-1} \partial \bar{\partial} u$ away from zero. Hence there is a uniform $C_{0}$ such that on $B_{1}$,
$$C_{0}^{-1}\left(\delta_{i \bar{j}}\right) \leqslant 2\left(h_{i \bar{j}}+u_{i \bar{j}}\right) \leqslant C_{0}\left(\delta_{i \bar{j}}\right),$$
where $\left(\delta_{i \bar{j}}\right)$ is the $n \times n$ identity matrix, considered as a Hermitian matrix. Hence from (2.1) we have, for $x \in B_{1}$,
$$C_{0}^{-1} I_{2 n} \leqslant S(x)+T\left(D^{2} u(x), x\right) \leqslant C_{0} I_{2 n} .$$

We take the convex set $\mathcal{E}$ to be the set of matrices $N \in \operatorname{Sym}(2 n)$ with
$$C_{0}^{-1} I_{2 n} \leqslant N \leqslant C_{0} I_{2 n},$$
and note that this set is compact. It is then immediate that
$$S(x)+T\left(D^{2} u(x), x\right) \in \mathcal{E}, \quad \text { for all } x \in B_{1} .$$

We define $F(N, x)=\operatorname{det}(N)^{\frac{1}{2 n}}$ (independent of $x$ ) for all $N$ in a small neighborhood of $\mathcal{E}$, extend $F$ arbitrarily to all of $\operatorname{Sym}(2 n) \times B_{1}$, and let $f=2 e^{\psi / n} \operatorname{det}\left(g_{i \bar{j}}\right)^{1 / n} \in C^{\alpha_{0}}$. Note that for a Hermitian matrix $H$,
$$\operatorname{det}(\iota(H))=(\operatorname{det} H)^{2} .$$

Then since $u$ solves (1.3), we have that
$$\begin{aligned}
F\left(S(x)+T\left(D^{2} u(x), x\right), x\right) & =\operatorname{det}\left(\iota\left(2\left(h_{i \bar{j}}+u_{i \bar{j}}\right)\right)\right)^{1 / 2 n} \\
& =\operatorname{det}\left(2\left(h_{i \bar{j}}+u_{i \bar{j}}\right)\right)^{1 / n} \\
& =2 e^{\psi / n} \operatorname{det}\left(g_{i \bar{j}}\right)^{1 / n}=f .
\end{aligned}$$

It remains to check the conditions H1-H3. For H1.(1), note that $F_{i j}(N, x)=$ $\frac{1}{2 n}(\operatorname{det} N)^{1 / 2 n}\left(N^{-1}\right)_{i j}$ for $N \in \mathcal{E}$ and by definition of $\mathcal{E}$ it follows immediately that we have uniform ellipticity with $\lambda$ and $\Lambda$ depending only on $n$ and $C_{0}$. Concavity of $F$ in $\mathcal{E}$ is well-known (see e.g. [5]), giving H1.(2). H1.(3) is trivially satisfied.

For H2.(3), observe that if $P \in \operatorname{Sym}(2 n)$ is nonnegative then for all vectors $v \in \mathbb{R}^{2 n}$
$$\langle T(P, x) v, v\rangle=\langle\mathrm{p}(P) v, v\rangle=\frac{1}{2}(\langle P v, v\rangle+\langle P J v, J v\rangle) \geqslant 0,$$
and hence $T(P, x) \geqslant 0$. Next,
$$\frac{1}{2}\|P\| \leqslant\|T(P, x)\|=\frac{1}{2} \sup _{\|v\|=1}(\langle P v, v\rangle+\langle P J v, J v\rangle) \leqslant\|P\| .$$

The other conditions follow easily. We can then apply Theorem 1.2 and obtain $\|u\|_{C^{2, \alpha}(M)} \leqslant C$, as required.

The complex Hessian equations (1.4). Recall that if $\lambda=\left(\lambda_{1}, \ldots, \lambda_{n}\right) \in \mathbb{R}^{n}$, we define $\sigma_{k}(\lambda)$ to be the $k^{\text {th }}$ elementary symmetric polynomial
$$\sigma_{k}(\lambda)=\sum_{i_{1}<\cdots<i_{k}} \lambda_{i_{1}} \cdots \lambda_{i_{k}} .$$
We can rewrite the equations (1.4) in terms of $\sigma_{k}$ as follows. Write $T^{1,0} M$ for the $(1,0)$ part of the complexified tangent space of $M$ (that is, the span of $\frac{\partial}{\partial z^{1}}, \ldots, \frac{\partial}{\partial z^{n}}$ over $\mathbb{C}$ ). Then we have an endomorphism
$$A: T^{1,0} M \rightarrow T^{1,0} M$$
given by the matrix $A^{k}{ }_{i}=g^{k \bar{j}}\left(h_{i \bar{j}}+u_{i \bar{j}}\right)$. Namely, given $X=X^{i} \frac{\partial}{\partial z^{i}}$ we define $A(X)=A^{k}{ }_{i} X^{i} \frac{\partial}{\partial z^{k}}$. The matrix ( $A^{k}{ }_{i}$ ) is Hermitian with respect to the inner product on $T^{1,0} M$ given by $\left(g_{i \bar{j}}\right)$. That is, for $X, Y \in T^{1,0} M$, we have
$$\langle A X, Y\rangle_{g}=g_{i \bar{j}} A^{i}{ }_{k} X^{k} \overline{Y^{j}}=\left(h_{i \bar{j}}+u_{i \bar{j}}\right) X^{i} \overline{Y^{j}}=g_{i \bar{j}} X^{i} \overline{A^{j}{ }_{\ell} Y^{\ell}}=\langle X, A Y\rangle_{g} .$$
Now let $\lambda_{1} \geqslant \ldots \geqslant \lambda_{n}$ be the eigenvalues of ( $A^{k}{ }_{i}$ ), some of which could be negative. Then the equation (1.4) can be written as
$$\begin{aligned}
\left(\sigma_{k}(\lambda)\right)^{1 / k} & =\binom{n}{k}^{1 / k} e^{\psi / k} \\
\sigma_{j}(\lambda) & >0, \quad \text { for } j=1, \ldots, k,
\end{aligned}$$
for $\lambda=\left(\lambda_{1}, \ldots, \lambda_{n}\right)$. Indeed, this is easy to see after picking coordinates for which $\left(g_{i \bar{j}}\right)$ is the identity, and $\left(h_{i \bar{j}}+u_{i \bar{j}}\right)$ is diagonal.

To cast (2.6) in the form (1.9), we take a chart in $M$ which is identified with the unit ball $B_{1}$ in $\mathbb{C}^{n}$ with local coordinates $\left(z^{1}, \ldots, z^{n}\right)$. We let $S(x)=\iota\left(2 h_{i \bar{j}}(x)\right)$ and $T(N, x)=\mathrm{p}(N)$, so that $T\left(D^{2} u(x), x\right)=\iota\left(2 u_{i \bar{j}}(x)\right)$.

Next observe that the assumption $\Delta u \leqslant K$ implies that the eigenvalues $\lambda_{j}$ of ( $A^{k}{ }_{i}$ ) satisfy $\sigma_{1}(\lambda)=\lambda_{1}+\cdots+\lambda_{n} \leqslant K^{\prime}$. We have
$$\frac{\partial \sigma_{k}(\lambda)}{\partial \lambda_{i}}=\sigma_{k-1}(\lambda \mid i),$$
where $\sigma_{p}(\lambda \mid i)$ is the $p^{\text {th }}$ elementary symmetric function of the $n$-tuple $\left(\lambda_{1}, \ldots, \lambda_{n}\right)$ where we set $\lambda_{i}=0$. We will need the following algebraic lemma, which can be easily extracted from the literature (cf. [64]).

Lemma 2.1. Let $\lambda=\left(\lambda_{1}, \ldots, \lambda_{n}\right)$ be an $n$-tuple of real numbers which satisfy
$$\begin{gathered}
\sigma_{j}(\lambda)>0, \quad \text { for } j=1, \ldots, k, \\
\left(\sigma_{k}(\lambda)\right)^{1 / k} \geqslant A^{-1}>0, \\
\sigma_{1}(\lambda) \leqslant A,
\end{gathered}$$
for some $2 \leqslant k \leqslant n$, and a constant $A>0$. Then there exists a constant $K_{0}>0$, which depends only on $A, n, k$, such that
$$\begin{gathered}
\left(\sigma_{j}(\lambda)\right)^{1 / j} \geqslant K_{0}^{-1}>0, \quad \text { for } j=1, \ldots, k, \\
K_{0}^{-1} \leqslant \sigma_{j-1}(\lambda \mid i) \leqslant K_{0}, \quad \text { for } i=1, \ldots, n, \text { and } j=2, \ldots, k, \\
-K_{0} \leqslant \lambda_{j} \leqslant K_{0}, \quad \text { for } j=1, \ldots, n .
\end{gathered}$$
Proof. Inequality (2.10) just follows from (2.7), (2.8) and the Maclaurin inequality
$$\sigma_{j}(\lambda)^{\frac{1}{j}} \geqslant C_{n, j, k} \sigma_{k}(\lambda)^{\frac{1}{k}} \geqslant C_{n, j, k} A^{-1} .$$
Next we show (2.11). Assumption (2.7) implies that we have for $2 \leqslant j \leqslant k$,
$$\sigma_{j-1}(\lambda \mid i) \geqslant \sigma_{j-1}(\lambda \mid 1)>0,$$
see e.g. [64, Proposition 2.1 (2)]. It is also easy to check ([64, Proposition 2.1 (1)]) that for $2 \leqslant j \leqslant k$,
$$\sum_{i=1}^{n} \sigma_{j-1}(\lambda \mid i)=(n-j+1) \sigma_{j-1}(\lambda),$$
hence
$$\sigma_{j-1}(\lambda \mid i) \leqslant(n-j+1) \sigma_{j-1}(\lambda) \leqslant C_{n, j} \sigma_{1}(\lambda)^{j-1} \leqslant C_{n, j} A^{j-1},$$
using the Maclaurin inequality and (2.9). Using (2.8) we also have
$$\prod_{i=1}^{n} \sigma_{j-1}(\lambda \mid i) \geqslant C_{n, j} \sigma_{j}(\lambda)^{\frac{n(j-1)}{j}} \geqslant C_{n, j, k} \sigma_{k}(\lambda)^{\frac{n(j-1)}{k}} \geqslant C_{n, j, k} A^{-n(j-1)},$$
where the first inequality is [64, Proposition 2.1 (4)]. Combining (2.13) and (2.14), we get (2.11).

Finally, we prove (2.12). Since $k \geqslant 2$, inequalities (2.11) hold with $j=2$,
$$K_{0}^{-1} \leqslant \sigma_{1}(\lambda \mid i) \leqslant K_{0} .$$
But we clearly have
$$\lambda_{i}=\sigma_{1}(\lambda)-\sigma_{1}(\lambda \mid i),$$
and the bound (2.12) follows. \(\square\)

Thanks to (2.6), the eigenvalues $\lambda_{j}$ of $\left(A^{k}{ }_{i}\right)$ satisfy the hypotheses of Lemma 2.1, for some uniform constant $A$ (on the whole of $B_{1}$ ). Let $K_{0}$ be the constant that we obtain from Lemma 2.1.

Given a matrix $N \in \operatorname{Sym}(2 n)$, then $\iota^{-1}(p(N))$ is an $n \times n$ Hermitian matrix. Denote by $A(N)^{k}{ }_{i}=g^{k \bar{j}}(0)\left(\iota^{-1}(p(N))\right)_{i \bar{j}}$, which is Hermitian with respect to the inner product $g_{i \bar{j}}(0)$, with eigenvalues $\lambda(0)=\left(\lambda_{1}(0), \ldots, \lambda_{n}(0)\right)$. Let $\mathcal{E}$ be the convex set of matrices $N \in \operatorname{Sym}(2 n)$ with
$$\begin{aligned}
-2 K_{0} \leqslant \lambda_{i}(0) & \leqslant 2 K_{0}, \text { for } 1 \leqslant i \leqslant n \\
\left(\sigma_{j}(\lambda(0))^{1 / j}\right. & \geqslant\left(2 K_{0}\right)^{-1}, \text { for } 1 \leqslant j \leqslant k .
\end{aligned}$$
The set $\mathcal{E}$ is compact, and the concavity of $\sigma_{j}^{1 / j}$ (see [5], for example) implies that $\mathcal{E}$ is convex.

Now write $\lambda(x)=\left(\lambda_{1}(x), \ldots, \lambda_{n}(x)\right)$ for the eigenvalues of $A(N, x)^{k}{ }_{i}=$ $g^{k \bar{j}}(x)\left(\iota^{-1}(p(N))\right)_{i \bar{j}}$. For $N$ in a sufficiently small neighborhood of $\mathcal{E}$ we define
$$F(N, x)=\left(\sigma_{k}(\lambda(x))\right)^{1 / k},$$
and extend $F$ arbitrarily to $\operatorname{Sym}(2 n) \times B_{1}$. Since $g_{i \bar{j}}(x)$ is a continuously-varying Hermitian matrix, for all $N \in \mathcal{E}$ we have that $\lambda(x)$ satisfies
$$\begin{aligned}
-4 K_{0} \leqslant \lambda_{i}(x) & \leqslant 4 K_{0}, \text { for } 1 \leqslant i \leqslant n \\
\left(\sigma_{j}(\lambda(x))^{1 / j}\right. & \geqslant\left(4 K_{0}\right)^{-1}, \text { for } 1 \leqslant j \leqslant k .
\end{aligned}$$
as long as $x$ is sufficiently close to 0 . If necessary, we replace the ball $B_{1}$ with a smaller ball $B_{r}$ (for some uniform $0<r<1$ ) to ensure that this holds. Of course, by a simple covering argument this does not affect the conclusion.

From what we have shown above, if $u$ solves (1.4) on $M$ then the eigenvalue $\lambda(x)$ corresponding to the matrix $N=S(x)+T\left(D^{2} u(x), x\right)$ satisfies (2.16) with $4 K_{0}$ replaced by $K_{0}$. Again using the continuity of $g_{i \bar{j}}(x)$, it follows from the definition of $\mathcal{E}$ that, after possibly shrinking $r$, we have
$$S(x)+T\left(D^{2} u(x), x\right) \in \mathcal{E},$$
for all $x \in B_{r}$.
By the concavity of $\sigma_{k}^{1 / k}$, we see that for each fixed $x, F(N, x)$ is concave in $\mathcal{E}$. Moreover, thanks to Lemma 2.1, (2.16) implies bounds of the form
$$\left(K_{0}^{\prime}\right)^{-1} \leqslant \sigma_{k-1}(\lambda \mid i) \leqslant K_{0}^{\prime}, \quad 1 \leqslant i \leqslant n,$$
so we see that for $N \in \mathcal{E}, F(N, x)$ is uniformly elliptic. Since $g_{i \bar{j}}(x)$ is a smoothly-varying Hermitian matrix, it is easy to see that, since $\mathcal{E}$ is compact,
$$|F(N, x)-F(N, y)| \leqslant K|x-y|^{\beta},$$
for all $N \in \mathcal{E}$ and all $x, y \in B_{1}$, giving H1.(3).
We can then apply Theorem 1.2 and obtain $\|u\|_{C^{2, \alpha}(M)} \leqslant C$, as required.
The complex $\sigma_{n} / \sigma_{k}$ equations (1.5). The argument for the equations (1.5) is similar, and slightly simpler, than the argument given above for the complex Hessian equations. Indeed, using the same notation as there, we may write (1.5) in terms of the eigenvalues $\lambda=\left(\lambda_{1}, \ldots, \lambda_{n}\right)$ as
$$\left(\frac{\sigma_{n}}{\sigma_{k}}\right)^{1 /(n-k)}=e^{-\psi /(n-k)}\binom{n}{k}^{-1 /(n-k)}, \quad \lambda_{1} \geqslant \cdots \geqslant \lambda_{n}>0 .$$
From the assumption $\Delta u \leqslant K$ we have $\sigma_{1}(\lambda) \leqslant K^{\prime}$ and hence all the eigenvalues $\lambda_{i}$ are bounded from above by $K^{\prime}$. Moreover, the equation (2.17) implies lower bounds for $\lambda_{i}$ away from zero. Indeed, from (2.17) we have an upper bound for
$$\frac{\sum_{i_{1}<\cdots<i_{k}} \lambda_{i_{1}} \cdots \lambda_{i_{k}}}{\lambda_{1} \lambda_{2} \cdots \lambda_{n}},$$
and since each term in the sum is positive we obtain in particular,
$$\frac{1}{\lambda_{k+1} \lambda_{k+2} \cdots \lambda_{n}} \leqslant C .$$
Hence for each $i=1, \ldots, n$,
$$\lambda_{i} \geqslant \lambda_{n} \geqslant \frac{1}{C \lambda_{k+1} \cdots \lambda_{n-1}} \geqslant c>0,$$
for a uniform $c>0$, since $\lambda_{k+1}, \cdots, \lambda_{n-1}$ are all uniformly bounded from above.

Now define $\mathcal{E}$ to be the compact convex set of matrices $N \in \operatorname{Sym}(2 n)$ whose eigenvalues $\lambda_{i}(0)$ (with respect to $g(0)$ ) satisfy
$$K_{0}^{-1} \leqslant \lambda_{i}(0) \leqslant K_{0},$$
for a sufficiently large $K_{0}$. The operator
$$F(N, x)=\left(\frac{\sigma_{n}(\lambda(x))}{\sigma_{k}(\lambda(x))}\right)^{1 /(n-k)}$$
is concave (see e.g. [52]) and uniformly elliptic on $\mathcal{E}$ (after possibly shrinking the neighborhood), and hence we can apply Theorem 1.2 in the same way as for the complex Hessian equations above.

Remark 2.2. In fact, by a similar argument, Theorem 1.1 applies to the more general complex $\sigma_{\ell} / \sigma_{k}$ equations
$$\begin{aligned}
& (\chi+\sqrt{-1} \partial \bar{\partial} u)^{k} \wedge \omega^{n-k}=e^{\psi}(\chi+\sqrt{-1} \partial \bar{\partial} u)^{\ell} \wedge \omega^{n-\ell} \\
& (\chi+\sqrt{-1} \partial \bar{\partial} u)^{j} \wedge \omega^{n-j}>0, \quad \text { for } j=1, \ldots, \ell,
\end{aligned}$$
where $1<k<\ell \leqslant n$.

The Monge-Ampère equation for $(n-1)$-psh functions (1.6). First note that the assumption $\Delta u \leqslant K$ implies that the positive definite $(1,1)$ form
$$\chi+\frac{1}{n-1}((\Delta u) \omega-\sqrt{-1} \partial \bar{\partial} u)>0$$
has bounded trace with respect to $g$. The equation (1.6) then implies that this positive definite $(1,1)$ form is uniformly bounded from above, and below away from zero.

We define $S(x)=\iota\left(2 h_{\bar{i} \bar{j}}(x)\right)$. We let $g(x)=\iota\left(2 g_{i \bar{j}}(x)\right)$ be the Riemannian metric associated to $\left(g_{i \bar{j}}\right)$ and we define
$$T(N, x)=\frac{1}{n-1}\left(\frac{1}{2} \operatorname{tr}\left(g(x)^{-1} \mathrm{p}(N)\right) g(x)-\mathrm{p}(N)\right) .$$
As with the complex Monge-Ampère equation above, define $F$ by $F(N, x)=$ $\operatorname{det}(N)^{\frac{1}{2 n}}$ (independent of $x$ ) for $N$ in a neighborhood of $\mathcal{E}$, extend $F$ arbitrarily to $\operatorname{Sym}(2 n) \times B_{1}$, and observe that equation (1.6) is equivalent to
$$F\left(S(x)+T\left(D^{2} u(x), x\right), x\right)=2 e^{\psi / n} \operatorname{det}\left(g_{i \bar{j}}\right)^{1 / n}=: f .$$

Take the convex set $\mathcal{E}$ to be the set of matrices $N \in \operatorname{Sym}(2 n)$ with
$$K_{0}^{-1} I_{2 n} \leqslant N \leqslant K_{0} I_{2 n},$$
for a sufficiently large constant $K_{0}$.
We check that the hypotheses of Theorem 1.2 are satisfied. Clearly H1, H3 and H2.(2) hold. For H2.(1) we have
$$\begin{aligned}
& \|T(N, x)-T(N, y)\| \\
& \leqslant \frac{1}{(n-1)}\left(\frac{1}{2} \operatorname{tr}\left(\left(g^{-1}(x)-g^{-1}(y)\right) \mathrm{p}(N)\right) g(x)-\frac{1}{2} \operatorname{tr}\left(g^{-1}(y) \mathrm{p}(N)\right)(g(y)-g(x))\right) \\
& \leqslant K|x-y|^{\beta}\|N\| .
\end{aligned}$$
Lastly, we check H2.(3). If $P \geqslant 0$, then $\frac{1}{2} \operatorname{tr}\left(g(x)^{-1} \mathrm{p}(P)\right) g(x)-\mathrm{p}(P) \geqslant 0$, because at any $x$ we can choose a basis such that $g(x)=I$ while $\mathrm{p}(P)$ is diagonal with eigenvalues $\lambda_{1}, \lambda_{1}, \ldots, \lambda_{n}, \lambda_{n} \geqslant 0$, and then the eigenvalues of $\frac{1}{2} \operatorname{tr}\left(g(x)^{-1} \mathrm{p}(P)\right) g(x)-\mathrm{p}(P)$ are $\sum_{i \neq j} \lambda_{i} \geqslant 0$. From this we also see that
$$\frac{1}{n-1}\|\mathrm{p}(P)\| \leqslant \frac{1}{n-1}\left\|\frac{1}{2} \operatorname{tr}\left(g(x)^{-1} \mathrm{p}(P)\right) g(x)-\mathrm{p}(P)\right\| \leqslant\|\mathrm{p}(P)\| .$$

But $P \geqslant 0$ implies from (2.5) that $\|\mathrm{p}(P)\| \leqslant\|P\| \leqslant 2\|\mathrm{p}(P)\|$, which gives H2.(3).

We can then apply Theorem 1.2 and obtain $\|u\|_{C^{2, \alpha}(M)} \leqslant C$.
The $(n-1)$-plurisubharmonic version of the complex Hessian and $\sigma_{n} / \sigma_{k}$ equations (1.7). This case follows easily by combining the arguments for the previous three examples, choosing $S(x), T(N, x)$ as in the discussion of (1.6), and $F(N, x), \mathcal{E}$ as in the discussions of (1.4) and (1.5) respectively.

The almost complex case (1.8). Here we assume more generally that $(M, J)$ is an almost-complex manifold. Then one can define $(d J d u)^{(1,1)}$, which takes the place of $\sqrt{-1} \partial \bar{\partial} u$. The convention we use for the action of $J$ on 1-forms is $J \alpha(X):=-\alpha(J X)$, for any 1-form $\alpha$ and vector $X$. With this convention, we have $(d J d u)^{(1,1)}=2 \sqrt{-1} \partial \bar{\partial} u$ when $J$ is integrable. For notational convenience, in the following we will work with $(d J d u)^{(1,1)}$ instead of $\frac{1}{2}(d J d u)^{(1,1)}$, which will not affect any of the results. We first deal with the case of the Monge-Ampère equation (1.3) in this setting.

In this case, we define the Laplacian of $u$ to be
$$\Delta u=\frac{n \omega^{n-1} \wedge(d J d u)}{\omega^{n}}=\frac{n \omega^{n-1} \wedge(d J d u)^{(1,1)}}{\omega^{n}},$$
which differs from the usual Riemannian Laplacian by a first order term.
We fix a point $p \in M$ and choose a real coordinate system $x^{1}, \ldots, x^{2 n}$ centered at $p$. Writing $J=\left(J^{k}{ }_{\ell}\right)$ we see that
$$d J d u=\left(-J_{\ell}^{k} \partial_{k} \partial_{i} u-\left(\partial_{i} J_{\ell}^{k}\right) \partial_{k} u\right) d x^{i} \wedge d x^{\ell}$$
Its $(1,1)$ part is given by
$$\begin{aligned}
(d J d u)^{(1,1)}= & \frac{1}{2}\left(-J_{\ell}^{k} \partial_{k} \partial_{i} u-J_{i}^{a} J^{b} J^{k}{ }_{b} \partial_{k} \partial_{a} u\right. \\
& \left.-\left(\partial_{i} J_{\ell}^{k}\right) \partial_{k} u-J_{i}^{a} J_{\ell}^{b}\left(\partial_{a} J_{b}^{k}\right) \partial_{k} u\right) d x^{i} \wedge d x^{\ell} .
\end{aligned}$$
For later use, we note that
$$(d J d u)^{(2,0)+(0,2)}=\frac{1}{2}\left(-\left(\partial_{i} J_{\ell}^{k}\right) \partial_{k} u+J_{i}^{a} J_{\ell}^{b}\left(\partial_{a} J_{b}^{k}\right) \partial_{k} u\right) d x^{i} \wedge d x^{\ell} .$$
Associated to $(d J d u)^{(1,1)}$ is a symmetric bilinear form $H(u)$ defined by $H(u)(X, Y)=(d J d u)^{(1,1)}(X, J Y)$. Compute
$$(H(u))_{i j}:=\frac{1}{2}\left(\partial_{i} \partial_{j} u+J_{i}^{k} J^{\ell}{ }_{j} \partial_{k} \partial_{\ell} u\right)+E_{i j},$$
where
$$E_{i j}=\frac{1}{4}\left(-J_{j}^{\ell}\left(\partial_{i} J_{\ell}^{k}\right)-J_{i}^{\ell}\left(\partial_{j} J_{\ell}^{k}\right)+J_{j}^{\ell}\left(\partial_{\ell} J_{i}^{k}\right)+J_{i}^{\ell}\left(\partial_{\ell} J_{j}^{k}\right)\right) \partial_{k} u .$$
Or, in other words,
$$H(u)(x)=\mathrm{p}\left(D^{2} u(x), x\right)+E,$$
where the "error" $E$ depends linearly on $D u$ (cf. [33, Proposition 4.2]). Here we denote by
$$\mathrm{p}(N, x)=\frac{1}{2}\left(N+J^{T}(x) N J(x)\right) .$$
We set $T(N, x)=\mathrm{p}(N, x)$. Observe that $T$ satisfies the properties H2.(1) and H2.(2). Moreover, we may pick coordinates $x^{1}, \ldots, x^{2 n}$ so that at the origin,
$$J(0)=\left(\begin{array}{cc}
0 & -I_{n} \\
I_{n} & 0
\end{array}\right),$$
the standard complex structure. By shrinking the neighborhood if necessary, $J(x)$ is only a small perturbation of $J(0)$ and so $T(N, x)$ also satisfies the property H2.(3) by the same argument as above.

We define $S$ and $F$ in the obvious way, and thus we have essentially the same setup as in the complex Monge-Ampère equation (1.3) with the exception of the extra term $E$. However, this term is linear in $D u$. The uniform bounds that we assume on $u$ and $\Delta u$ imply a $C^{1, \beta}$ bound for $u$ for any $0<\beta<1$. Hence the $E$ term is bounded in $C^{\beta}$ and can then be absorbed in the term $\chi$.

The arguments for the other equations (1.4), (1.5), (1.6) and (1.7) in the almost complex case follow similarly.

\section*{3. Evans-Krylov Theory on Euclidean Space}

In this section, we recall Evans-Krylov theory on Euclidean space and its perturbation version due to Caffarelli. Again in this section $B_{1}$ will denote the unit ball in $\mathbb{R}^{2 n}$.

First, recall the following version of Evans-Krylov theorem (see [4, Theorem 6.6] and also [6, 22, 38]).

Theorem 3.1. Assume that $F: \operatorname{Sym}(2 n) \rightarrow \mathbb{R}$ is a concave function and uniformly elliptic, i.e.,
$$\lambda\|P\| \leqslant F(N+P)-F(N) \leqslant \Lambda\|P\|, \quad \forall N, P \in \operatorname{Sym}(2 n), P \geqslant 0 .$$
If $F(0)=0$ and a continuous function $u: B_{1} \rightarrow \mathbb{R}$ satisfies
$$F\left(D^{2} u\right)=0, \quad \text { in the viscosity sense. }$$
Then $u \in C^{2, \beta}\left(B_{1 / 2}\right)$ and
$$\|u\|_{C^{2, \beta}\left(B_{1 / 2}\right)} \leqslant C\|u\|_{L^{\infty}\left(B_{1}\right)}$$
where $\beta \in(0,1)$ and $C$ only depend on $n, \lambda, \Lambda$.
For our application, we need a more general version of the above theorem. We first introduce the following definition.

Definition 3.2. Let $\mathscr{F}_{2 n}(\lambda, \Lambda, K, \gamma)$ be a family of functions $\Phi: \operatorname{Sym}(2 n) \times$ $B_{1} \rightarrow \mathbb{R}$ depending on positive constants $\lambda, \Lambda, K$ and $\gamma \in(0,1)$. An element $\Phi \in \mathscr{F}_{2 n}(\lambda, \Lambda, K, \gamma)$ satisfies the following conditions:
\begin{itemize}
\item[-] Fiberwise concavity. For each fixed $x \in B_{1}$,
\item[] $\Phi\left(\frac{A+B}{2}, x\right) \geqslant \frac{1}{2} \Phi(A, x)+\frac{1}{2} \Phi(B, x), \quad$ for all $A, B \in \operatorname{Sym}(2 n)$.
\item[-] Uniform Ellipticity. For all $x \in B_{1}$ and all $N, P \in \operatorname{Sym}(2 n)$ with $P \geqslant 0$ we have
$$\lambda\|P\| \leqslant \Phi(N+P, x)-\Phi(N, x) \leqslant \Lambda\|P\| .$$
\item[-] Hölder bound in $x$. For all $x, y \in B_{1}$ and all $N \in \operatorname{Sym}(2 n)$,
$$\frac{|\Phi(N, x)-\Phi(N, y)|}{\|N\|+1} \leqslant K|x-y|^{\gamma} .$$
\end{itemize}

Remark 3.3. If $\Phi \in \mathscr{F}_{2 n}(\lambda, \Lambda, K, \gamma)$ and the equation $\Phi\left(D^{2} u(x), x\right)=0$ is a linear equation, then the linear equation takes the form
$$\sum_{i, j} a_{i j}(x) u_{i j}(x)=0$$
with $\left\|a_{i j}(x)\right\|_{C^{\gamma}} \leqslant K$ and the eigenvalues of $\left(a_{i j}(x)\right)$ lie between $\lambda$ and $\Lambda / 2 n$.
Now, we state the Evans-Krylov theorem for $\Phi \in \mathscr{F}_{2 n}(\lambda, \Lambda, K, \gamma)$.
Theorem 3.4. Assume that $\Phi \in \mathscr{F}_{2 n}(\lambda, \Lambda, K, \gamma)$ and $f \in C^{\alpha_{0}}\left(B_{1}\right)$. If $u \in C^{2}\left(B_{1}\right)$ satisfies
$$\Phi\left(D^{2} u(x), x\right)=f(x) \quad \text { in } B_{1}$$
then $u \in C^{2, \alpha}\left(B_{1 / 2}\right)$ and
$$\|u\|_{C^{2, \alpha}\left(B_{1 / 2}\right)} \leqslant C$$
where $C, \alpha$ depend only on $\alpha_{0}, K, \gamma, n, \lambda, \Lambda,\|f\|_{C^{\alpha_{0}}\left(B_{1}\right)},\|u\|_{L^{\infty}\left(B_{1}\right)}$ and $\Phi(0,0)$.
Indeed this theorem is a direct consequence of a theorem of Caffarelli [3, Theorem 3]. This result is also used in the second-named author's paper [65, Corollary 2.3], in the case when $\Phi$ does not depend on $x$. Furthermore, Theorem 3.4 remains true if $u \in C^{0}\left(B_{1}\right)$ is just a viscosity solution, and the proof is the same.

For the reader's convenience, we recall the statement of Caffarelli's theorem, following the exposition in [4, Theorem 8.1]. Suppose that we have a viscosity solution of the equation
$$G\left(D^{2} u(x), x\right)=f(x), \text { for } x \in B_{1},$$
where $u \in C^{0}\left(B_{1}\right), G: \operatorname{Sym}(2 n) \times B_{1} \rightarrow \mathbb{R}$ is continuous in $x, f$ is continuous, $G(0,0)=f(0)=0$, and $G$ satisfies the uniform ellipticity condition
$$\lambda\|P\| \leqslant G(N+P, x)-G(N, x) \leqslant \Lambda\|P\|, \quad \text { for } x \in B_{1},$$
for some positive constants $\lambda, \Lambda$, and for all $N, P \in \operatorname{Sym}(2 n)$ with $P \geqslant 0$. Let
$$\tilde{\beta}(x)=\sup _{N \in \operatorname{Sym}(2 n)} \frac{|G(N, x)-G(N, 0)|}{\|N\|+1} .$$

Furthermore assume that the following hypotheses hold:
Hypothesis 1. There are constants $0<\bar{\alpha}<1$ and $C_{e}>0$ such that for any symmetric matrix $N$ with $G(N, 0)=0$ and any $w_{0} \in C^{0}\left(\partial B_{1}\right)$, there exists a function $w \in C^{2}\left(B_{1}\right) \cap C^{0}\left(\overline{B_{1}}\right) \cap C^{2, \bar{\alpha}}\left(B_{1 / 2}\right)$ which solves
$$G\left(D^{2} w(x)+N, 0\right)=0$$
in $B_{1}$ and $w=w_{0}$ on $\partial B_{1}$, and
$$\|w\|_{C^{2, \bar{\alpha}}\left(B_{1 / 2}\right)} \leqslant C_{e}\|w\|_{L^{\infty}\left(B_{1}\right)} .$$

Hypothesis 2. There exist $0<\alpha<\bar{\alpha}, 0<r_{0} \leqslant 1, C_{1}>0$ and $C_{2}>0$, such that
$$\begin{aligned}
& \left(\frac{1}{r^{2 n}} \int_{B_{r}} \tilde{\beta}^{2 n}\right)^{1 / 2 n} \leqslant C_{1} r^{\alpha} r_{0}^{-\alpha}, \\
& \left(\frac{1}{r^{2 n}} \int_{B_{r}}|f|^{2 n}\right)^{1 / 2 n} \leqslant C_{2} r^{\alpha} r_{0}^{-\alpha},
\end{aligned}$$
for all $0<r \leqslant r_{0}$.
Then Theorem 8.1 of [4] asserts:
Theorem 3.5. Let $u$ solve (3.1) with the assumptions described above, including Hypothesis 1 and Hypothesis 2. Then $u$ is $C^{2, \alpha}$ at the origin. More precisely, there exists a constant $C>1$ which depends only on $n, \lambda, \Lambda, C_{e}$, $\bar{\alpha}, \alpha, C_{1}, C_{2}$ and a polynomial function $P$ of degree 2 such that
$$\begin{gathered}
\|u-P\|_{L^{\infty}\left(B_{r}\right)} \leqslant C_{3} r^{2+\alpha} r_{0}^{-(2+\alpha)}, \quad \text { for all } r \leqslant C^{-1} r_{0}, \\
r_{0}|D P(0)|+r_{0}^{2}\left\|D^{2} P\right\| \leqslant C_{3}, \\
C_{3} \leqslant C\left(\|u\|_{L^{\infty}\left(B_{r_{0}}\right)}+r_{0}^{2}\left(C_{2}+1\right)\right) .
\end{gathered}$$

We now use Theorems 3.1 and 3.5 to prove Theorem 3.4
Proof of Theorem 3.4. We follow the exposition in [65, Corollary 2.3]. Define
$$G(N, x)=\Phi\left(N+t_{0} I_{2 n}, x\right)-f(0),$$
where $t_{0} \in \mathbb{R}$ is chosen so that $\Phi\left(t_{0} I_{2 n}, 0\right)=f(0)$. Such a $t_{0}$ exists because of the ellipticity of $\Phi(N, 0)$, which also implies that
$$\left|t_{0}\right| \leqslant \lambda^{-1}|\Phi(0,0)-f(0)| .$$
We also define $g(x)=f(x)-f(0)$ and $v(x)=u(x)-\frac{t_{0}}{2}|x|^{2}$. Then we have that
$$G\left(D^{2} v(x), x\right)=g(x),$$
and $G(0,0)=g(0)=0$. Thanks to (3.5), it is enough to bound the $C^{2, \alpha}$ norm of $v$.

It is clear that $G$ satisfies the ellipticity condition (3.2) and is continuous in $x$. To verify Hypothesis 1, it is enough to observe that since $G$ is uniformly elliptic, the Dirichlet problem for a viscosity solution of the equation (3.3)
can be solved using Perron's method, and the Evans-Krylov Theorem 3.1 shows that $u$ is $C^{2, \bar{\alpha}}$ with the estimate (3.4), with $C_{e}$ and $\bar{\alpha}$ depending only on $n, \lambda, \Lambda$.

Furthermore, we have
$$\tilde{\beta}(x)=\sup _{N \in \operatorname{Sym}(2 n)} \frac{\left|\Phi\left(N+t_{0} I_{n}, x\right)-\Phi\left(N+t_{0} I_{n}, 0\right)\right|}{\|N\|+1} \leqslant C|x|^{\gamma},$$
where $C$ depends on $K, n, \lambda, \Phi(0,0)$ and $f(0)$. It follows that Hypothesis 2 is satisfied for any $r_{0} \leqslant 1$ and any $\alpha<\min \left(\gamma, \alpha_{0}, \bar{\alpha}\right)$, with $C_{1}, C_{2}$ depending only on $K, n, \lambda, \Phi(0,0), f(0)$ and $\|f\|_{C^{\alpha_{0}}\left(B_{1}\right)}$.

We can thus apply Theorem 3.5 and conclude that $v$ (and hence $u$ ) is $C^{2, \alpha}$ at 0 with the bounds given there. By translation of the coordinates, we see that $u$ is $C^{2, \alpha}$ at every $x \in B_{1 / 2}$ with these bounds. But a standard covering argument (see e.g. [4, Remark 3, p.74]) implies that $u \in C^{2, \alpha}\left(B_{1 / 2}\right)$ with $\|u\|_{C^{2, \alpha}\left(B_{1 / 2}\right)} \leqslant C$ for a constant $C$ depending only on the stated quantities. \(\square\)

\section*{4. Proof of Theorem 1.2}

In this section, we present the proof of Theorem 1.2.
Proof of Theorem 1.2. Under the assumptions of Theorem 1.2, we shall construct a map $\Phi: \operatorname{Sym}(2 n) \times B_{1} \rightarrow \mathbb{R}$ in $\mathscr{F}_{2 n}\left(K^{-1} \lambda, 2 K n \Lambda, 5 \Lambda K n, \beta\right)$ such that
$$F\left(S(x)+T\left(D^{2} u(x), x\right), x\right)=\Phi\left(D^{2} u(x), x\right) \quad \text { for all } x \in B_{1},$$
and then apply Theorem 3.4.
First of all, recall that since $\langle A, B\rangle=\operatorname{tr}(A B)$ defines an inner product on the space of symmetric matrices, every linear map $\operatorname{Sym}(2 n) \rightarrow \mathbb{R}$ can be written as $X \mapsto \operatorname{tr}(A X)$ for some symmetric matrix $A \in \operatorname{Sym}(2 n)$. In this way, we identify the derivative $D G$ of any map $G: \operatorname{Sym}(2 n) \rightarrow \mathbb{R}$ at a given point with an element of $\operatorname{Sym}(2 n)$.

Let also $\mathcal{H}$ be subset of $\operatorname{Sym}(2 n)$ given by symmetric matrices with all eigenvalues in the interval $[\lambda, \Lambda]$. By assumption H1.(1), for any $x \in B_{1}$ and $A \in \mathcal{E}$, the derivative $D F=\left(F_{i j}\right)$ of $F(\cdot, x)$ at $A$ lies in $\mathcal{H}$.

Following [65], we define $\bar{F}: \operatorname{Sym}(2 n) \times B_{1} \rightarrow \mathbb{R}$ as follows
$$\begin{aligned}
& \bar{F}(N, x):=\inf \{L(N) \mid L: \operatorname{Sym}(2 n) \rightarrow \mathbb{R} \text { affine linear, } D L \in \mathcal{H}, \\
&L(A) \geqslant F(A, x), \forall A \in \mathcal{E}\} .
\end{aligned}$$
Note that $\bar{F}(N, x)>-\infty$ for all $N \in \operatorname{Sym}(2 n), x \in B_{1}$. We have the following lemma (cf. [65, Section 3]).

Lemma 4.1. $\bar{F}$ satisfies the following properties.
\begin{itemize}
\item[(i)] $\bar{F}(\cdot, x)$ is concave on $\operatorname{Sym}(2 n)$ for all $x \in B_{1}$, and $\bar{F}=F$ on $\mathcal{E} \times B_{1}$.
\item[(ii)] $\bar{F}(\cdot, x)$ is Lipschitz on Sym (2n) with Lipschitz constant $2 n \Lambda$, for all $x \in B_{1}$.
\end{itemize}
\begin{itemize}
\item[(iii)] For all $N, P \in \operatorname{Sym}(2 n)$ with $P \geqslant 0$ and for all $x \in B_{1}$, we have
$$\lambda\|P\| \leqslant \bar{F}(N+P, x)-\bar{F}(N, x) \leqslant 2 n \Lambda\|P\| .$$
\item[(iv)] For all $N \in \operatorname{Sym}(2 n)$ and all $x, y \in B_{1}$ we have
$$|\bar{F}(N, x)-\bar{F}(N, y)| \leqslant K|x-y|^{\beta} .$$
\end{itemize}
Proof. Part (i) is immediate. Indeed, $\bar{F}(\cdot, x)$ is concave on $\operatorname{Sym}(2 n)$ since it is an infimum of affine linear functions. From H1, $F(\cdot, x)$ is concave on $\mathcal{E}$ and its derivative $D F$ at a point $A \in \mathcal{E}$ lies in $\mathcal{H}$, it follows that $\bar{F}=F$ on $\mathcal{E} \times B_{1}$.

Every affine linear map $L: \operatorname{Sym}(2 n) \rightarrow \mathbb{R}$ can be written as
$$L(X)=\operatorname{tr}(A X)+c$$
for $A=D L \in \operatorname{Sym}(2 n)$ and some constant $c \in \mathbb{R}$. Now for any $N, X \in$ $\operatorname{Sym}(2 n)$ we will show that
$$|\bar{F}(N+X, x)-\bar{F}(N, x)| \leqslant 2 n \Lambda\|X\| \text {, }$$
which will establish (ii). From the definition of $\bar{F}$ it follows easily that there exist affine linear maps $L_{1}, L_{2}: \operatorname{Sym}(2 n) \rightarrow \mathbb{R}$ with $A_{1}=D L_{1}, A_{2}=D L_{2} \in$ $\mathcal{H}, L_{1}, L_{2} \geqslant F(\cdot, x)$ on $\mathcal{E}$ and
$$\bar{F}(N+X, x)=L_{1}(N+X), \quad \bar{F}(N, x)=L_{2}(N) .$$
Hence
$$\begin{aligned}
\bar{F}(N+X, x)-\bar{F}(N, x) & =L_{1}(N+X)-L_{2}(N) \\
& \leqslant L_{2}(N+X)-L_{2}(N) \\
& =\operatorname{tr}\left(A_{2} X\right) \leqslant 2 n \Lambda\|X\|,
\end{aligned}$$
where the first inequality uses the fact that $L_{1}(N+X)$ is an infimum of $L(N+X)$ over all affine linear functions $L$ with $\left.L\right|_{\mathcal{E}} \geqslant\left. F(\cdot, x)\right|_{\mathcal{E}}$. Similarly,
$$\begin{aligned}
\bar{F}(N+X, x)-\bar{F}(N, x) & =L_{1}(N+X)-L_{2}(N) \\
& \geqslant L_{1}(N+X)-L_{1}(N) \\
& =\operatorname{tr}\left(A_{1} X\right) \geqslant-2 n \Lambda\|X\| .
\end{aligned}$$

For (iii), all that remains is to prove the lower bound of $\bar{F}(N+P, x)-$ $\bar{F}(N, x)$ for $P \geqslant 0$. Write $\mu_{i} \geqslant 0$ for the eigenvalues of $P$. Then if $\bar{F}(N+$ $P, x)=L_{1}(N+P)$ and $\bar{F}(N, x)=L_{2}(N)$, we have, using the notation and argument as above,
$$\bar{F}(N+P, x)-\bar{F}(N, x) \geqslant \operatorname{tr}\left(A_{1} P\right) \geqslant \lambda\left(\mu_{1}+\cdots+\mu_{2 n}\right) \geqslant \lambda\|P\| .$$
For (iv), given $N \in \operatorname{Sym}(2 n)$ there exist affine linear maps $L_{1}, L_{2}: \operatorname{Sym}(2 n) \rightarrow$ $\mathbb{R}$ with $D L_{1}, D L_{2} \in \mathcal{H}, L_{1} \geqslant F(\cdot, x)$ and $L_{2} \geqslant F(\cdot, y)$ on $\mathcal{E}$ and
$$\bar{F}(N, x)=L_{1}(N), \quad \bar{F}(N, y)=L_{2}(N) .$$
For any given $A \in \mathcal{E}$ we have
$$L_{2}(A) \geqslant F(A, y) \geqslant F(A, x)-K|x-y|^{\beta},$$
using hypothesis H1.(3). Therefore $\tilde{L}_{2}:=L_{2}+K|x-y|^{\beta}$ is another affine linear map with $D \tilde{L}_{2} \in \mathcal{H}$ and $\tilde{L}_{2} \geqslant F(\cdot, x)$ on $\mathcal{E}$. By definition of $\bar{F}$, we have
$$L_{1}(N) \leqslant \tilde{L}_{2}(N)=L_{2}(N)+K|x-y|^{\beta},$$
i.e. $L_{1}(N)-L_{2}(N) \leqslant K|x-y|^{\beta}$. Similarly we obtain $L_{2}(N)-L_{1}(N) \leqslant$ $K|x-y|^{\beta}$, and so
$$|\bar{F}(N, x)-\bar{F}(N, y)|=\left|L_{1}(N)-L_{2}(N)\right| \leqslant K|x-y|^{\beta} .$$
This completes the proof. \(\square\)

Now, define $\Phi: \operatorname{Sym}(2 n) \times B_{1} \rightarrow \mathbb{R}$ by
$$\Phi(N, x):=\bar{F}(S(x)+T(N, x), x),$$
noting that $\Phi(0,0)=\bar{F}(S(0), 0)$ is bounded by H1 and H3.
Lemma 4.2. $\Phi$ lies in $\mathscr{F}_{2 n}\left(K^{-1} \lambda, 2 K n \Lambda, 5 \Lambda K n, \beta\right)$.
Given the lemma, we can complete the proof of Theorem 1.2. Indeed, by the assumption (1.10), we know
$$S(x)+T\left(D^{2} u(x), x\right) \in \mathcal{E}, \quad \forall x \in B_{1} .$$
It follows then from Lemma 4.1 (i) that for $x \in B_{1}$
$$\Phi\left(D^{2} u(x), x\right)=F\left(S(x)+T\left(D^{2} u(x), x\right), x\right)=f(x) .$$
and applying Theorem 3.4 completes the proof. \(\square\)

Proof of Lemma 4.2. First, we check fiberwise concavity of $\Phi$. Fix $x \in B_{1}$. Then for any $A, B \in \operatorname{Sym}(2 n)$ we have
$$\begin{aligned}
\Phi\left(\frac{A+B}{2}, x\right) & =\bar{F}\left(S(x)+T\left(\frac{A+B}{2}, x\right), x\right) \\
& =\bar{F}\left(\frac{S(x)+T(A, x)}{2}+\frac{S(x)+T(B, x)}{2}, x\right) \\
& \geqslant \frac{1}{2} \bar{F}(S(x)+T(A, x), x)+\frac{1}{2} \bar{F}(S(x)+T(B, x), x) \\
& =\frac{1}{2} \Phi(A, x)+\frac{1}{2} \Phi(B, x) .
\end{aligned}$$
Here, we have used linearity of $T$ and concavity of $\bar{F}$.
For uniform ellipticity of $\Phi$, we compute for $x \in B_{1}$ and any $N, P \in$ $\operatorname{Sym}(2 n)$ with $P \geqslant 0$,
$$\begin{aligned}
& \Phi(N+P, x)-\Phi(N, x) \\
= & \bar{F}(S(x)+T(N+P, x), x)-\bar{F}(S(x)+T(N, x), x) \\
= & \bar{F}(S(x)+T(N, x)+T(P, x), x)-\bar{F}(S(x)+T(N, x), x) .
\end{aligned}$$
From the ellipticity of $\bar{F}$ we have
$$\lambda\|T(P, x)\| \leqslant \Phi(N+P, x)-\Phi(N, x) \leqslant 2 n \Lambda\|T(P, x)\|$$
and hence from H2.(3),
$$K^{-1} \lambda\|P\| \leqslant \Phi(N+P, x)-\Phi(N, x) \leqslant 2 K n \Lambda\|P\|,$$
giving the required ellipticity of $\Phi$.
Finally, we need to check that $\Phi$ has a Hölder bound in $x$. Using Lemma 4.1 (ii) and (iv) we have
$$\begin{aligned}
& \frac{|\Phi(N, x)-\Phi(N, y)|}{\|N\|+1} \\
= & \frac{1}{\|N\|+1}|\bar{F}(S(x)+T(N, x), x)-\bar{F}(S(y)+T(N, y), y)| \\
\leqslant & \frac{1}{\|N\|+1}(|\bar{F}(S(x)+T(N, x), x)-\bar{F}(S(x)+T(N, x), y)| \\
& +|\bar{F}(S(x)+T(N, x), y)-\bar{F}(S(y)+T(N, y), y)|) \\
\leqslant & K|x-y|^{\beta}+\frac{2 n \Lambda}{\|N\|+1}\|S(x)+T(N, x)-S(y)-T(N, y)\| \\
\leqslant & K|x-y|^{\beta}+\frac{2 n \Lambda\|S(x)-S(y)\|}{\|N\|+1}+\frac{2 n \Lambda\|T(N, x)-T(N, y)\|}{\|N\|+1} \\
\leqslant & K|x-y|^{\beta}+2 K n \Lambda|x-y|^{\beta}+2 K n \Lambda|x-y|^{\beta} \leqslant 5 K n \Lambda|x-y|^{\beta},
\end{aligned}$$
as required. \(\square\)

\section*{5. Donaldson's equation}

In this final section, we give an application of Theorem 1.1 to an equation of Donaldson.

We begin by recalling some basic definitions. A symplectic form $\omega$ on a manifold $M$ tames an almost complex structure $J$ if at each point of $M$, $\omega(X, J X)>0$ for all nonzero vectors $X$. We can define a Riemannian metric by $g_{\omega}(X, Y)=\frac{1}{2}(\omega(X, J Y)+\omega(Y, J X))$. If, in addition, $\omega(J X, J Y)=$ $\omega(X, Y)$ for all $X, Y$ then we say that $\omega$ is compatible with $J$.

We now describe a conjecture of Donaldson. Let $M$ be a compact $2 n$ dimensional (real) manifold with an almost complex structure $J$ and a symplectic form $\Omega$ taming $J$. Let $\sigma$ be a smooth (positive) volume form on $M$. Suppose $\tilde{\omega}$ is a symplectic form on $M$ compatible with $J$, satisfying $[\tilde{\omega}]=[\Omega] \in H^{2}(M, \mathbb{R})$ and solving the Calabi-Yau equation
$$\tilde{\omega}^{n}=\sigma .$$
Donaldson conjectured that, for $n=2$, there are $C^{\infty}$ a priori bounds on $\tilde{\omega}$ depending only on $\Omega, J$ and $\sigma$. If this result were true, it would have important applications to symplectic topology [21, 42, 43, 54]. Some partial results towards this conjecture were given in [70, 62]. In particular, the conjecture holds, for any $n$, if the curvature of the canonical connection of $\left(g_{\Omega}, J\right)$ satisfies a certain positivity condition [62]. The conjecture was
solved in several special cases, such as the Kodaira-Thurston manifold [58] and more general $T^{2}$-bundles over $T^{2}$ [2, 24] assuming $T^{2}$ symmetry. The interested reader can consult the survey [57].

The result we prove is as follows:
Theorem 5.1. Let $\tilde{\omega} \in[\Omega]$ solve (5.1) on $\left(M^{2 n}, J, \Omega\right)$ with the notation as above. Fix $\alpha_{0} \in(0,1)$. Suppose that on a geodesic $g_{\Omega}$-ball $B_{R}$ of radius $R>0$ in $M$ we have
$$\operatorname{tr}_{g_{\Omega}} \tilde{g} \leqslant C_{0},$$
where $\tilde{g}:=g_{\tilde{\omega}}$ is the metric associated to $\tilde{\omega}$. Then there exist $\alpha \in(0,1)$ and $C>0$ depending only on $M, \Omega, J, R, \alpha_{0}$ and $\|\sigma\|_{C^{\alpha_{0}}\left(B_{R}, g_{\Omega}\right)}$ such that
$$\|\tilde{g}\|_{C^{\alpha}\left(B_{R / 2}, g_{\Omega}\right)} \leqslant C .$$

In fact, one can easily derive from this higher order estimates
$$\|\tilde{g}\|_{C^{k}\left(B_{R / 4}, g_{\Omega}\right)} \leqslant C_{k},$$
for all $k \geqslant 1$, exactly as in [62], Section 5], of course depending on higher derivatives of $\sigma$. In the case when $\Omega$ is compatible with $J$ (not just taming), such a local estimate on the $C^{\alpha}$ norm of $\tilde{g}$ was proved by the thirdnamed author [70] depending on two derivatives of $\sigma$, by adapting the Evans-Krylov method. A global Calabi-type estimate on $\tilde{g}$ was proved by Tosatti-Weinkove-Yau [62], depending on three derivatives of $\sigma$. Note that we state Theorem 5.1 as a local rather than global result, because we anticipate that such local arguments may be useful in any future progress on the full conjecture of Donaldson (cf. [57]).

We now give the proof.
Proof of Theorem 5.1. By shrinking $R$ if necessary, we may assume without loss of generality that $B_{R}$ is contained in a single coordinate patch for $M$, and that it is contractible. Write $\Delta$ for the following Laplace operator associated to $g_{\Omega}$,
$$\Delta u=\frac{n\left(\Omega^{(1,1)}\right)^{n-1} \wedge(d J d u)}{\left(\Omega^{(1,1)}\right)^{n}}=\operatorname{tr}_{\Omega^{(1,1)}}(d J d u),$$
which in [62] is called the canonical Laplacian of $g_{\Omega}$ (up to a factor of 2). Note that
$$\operatorname{tr}_{\Omega^{(1,1)}}(\Omega)=\operatorname{tr}_{\Omega^{(1,1)}}\left(\Omega^{(1,1)}\right)=n,$$
and
$$\operatorname{tr}_{\Omega^{(1,1)}}(\tilde{\omega})=\frac{1}{2} \operatorname{tr}_{g_{\Omega}} \tilde{g} .$$
We let $u$ solve the Dirichlet problem
$$\Delta u=\frac{1}{2} \operatorname{tr}_{g_{\Omega}} \tilde{g}-n \quad \text { on } B_{R},\left.\quad u\right|_{\partial B_{R}}=0 .$$

From the assumption (5.2) and the equation (5.1), the metric $\tilde{g}$ is uniformly equivalent to $g_{\Omega}$. By standard linear elliptic theory, $u$ is uniformly bounded in $W^{2, p}\left(B_{R}\right)$ for any given $p>1$. From now on, we fix a value of $p>n$.

Since $\tilde{\omega}-\Omega-d J d u$ is exact, there is a 1-form $a_{0}$ on $B_{R}$ with $d a_{0}=$ $\tilde{\omega}-\Omega-d J d u$. We solve the Neumann problem
$$\Delta_{d} v=-d^{*} a_{0} \quad \text { on } B_{R},\left.\quad * d v\right|_{\partial B_{R}}=-\left.* a_{0}\right|_{\partial B_{R}},$$
where $*$ is the Riemannian Hodge star operator of $g_{\Omega}, d^{*}$ is the adjoint of $d$ with respect to $g_{\Omega}$, and $\Delta_{d}=d^{*} d$ is the Hodge Laplacian on functions. As usual given a differential form $\alpha$ on $\overline{B_{R}}$, we write $\left.\alpha\right|_{\partial B_{R}}$ for the pullback of $\alpha$ under the inclusion of $\partial B_{R}$ into $\overline{B_{R}}$. Then (5.3) is indeed a Neumann problem, because
$$\left.* d v\right|_{\partial B_{R}}=\partial_{\nu} v d S,\left.\quad * a_{0}\right|_{\partial B_{R}}=i_{\nu} a_{0} d S,$$
where $\nu$ is the $g_{\Omega}$-unit outward normal vector to $\partial B_{R}, i_{\nu}$ is the interior product with $\nu$, and $d S$ is volume form on $\partial B_{R}$ induced by $g_{\Omega}$.

We conclude that $a:=a_{0}+d v$ satisfies
$$\tilde{\omega}=\Omega+d J d u+d a, \quad d^{*} a=0,\left.\quad * a\right|_{\partial B_{R}}=0 .$$
We can then apply for example [67, Theorem D (b)] to get
$$\|a\|_{W^{1, p}\left(B_{R}\right)} \leqslant C\|d a\|_{L^{p}\left(B_{R}\right)} \leqslant C,$$
for a uniform constant $C$, thanks to assumption (5.2) and the $W^{2, p}\left(B_{R}\right)$ bound for $u$.

Now observe that on $B_{R}, a$ solves the elliptic system (cf. [62, equation (5.4)])
$$d a \wedge\left(\Omega^{(1,1)}\right)^{n-1}=0, \quad d^{*} a=0, \quad(d a)^{(2,0)+(0,2)}=-(\Omega+d J d u)^{(2,0)+(0,2)} .$$
Equation (2.20) shows that $(d J d u)^{(2,0)+(0,2)}$ does not contain any second derivatives of $u$, and in fact it depends linearly on the gradient of $u$. Since $u$ is bounded in $W^{2, p}$ it follows that $(d J d u)^{(2,0)+(0,2)}$ is bounded in $W^{1, p}$ and hence in $C^{\alpha}$ for some $\alpha \in(0,1)$. By the standard interior elliptic estimates and the fact that $a$ is already bounded in $W^{1, p}$, we obtain $C^{1, \alpha}$ bounds for $a$ in a slightly smaller ball. Hence $d a$ is bounded in $C^{\alpha}$ in that ball.

Since $\tilde{\omega}=\Omega+d a+d J d u$, we can now write equation (5.1) locally as
$$\left(\chi+(d J d u)^{(1,1)}\right)^{n}=\sigma,$$
for $\chi=\Omega+d a+(d J d u)^{(2,0)+(0,2)}$ a form of type $(1,1)$ which is bounded in $C^{\alpha}$. The theorem then follows immediately from the (local version of) Theorem 1.1 for the almost complex version of (1.3). \(\square\)

\section*{References}
\begin{itemize}
\item[] [1] Błocki, Z., Weak solutions to the complex Hessian equation, Ann. Inst. Fourier (Grenoble) 55 (2005), no. 5, 1735-1756.
\item[] [2] Buzano, E., Fino, A. and Vezzoni, L., The Calabi-Yau equation for $T^{2}$-bundles over $T^{2}$ : the non-Lagrangian case, Rend. Semin. Mat. Univ. Politec. Torino 69 (2011), no. 3, 281-298.
\end{itemize}
\begin{itemize}
\item[] [3] Caffarelli, L.A., Interior a priori estimates for solutions of fully nonlinear equations, Ann. of Math. (2) 130 (1989), no. 1, 189-213.
\item[] [4] Caffarelli, L.A. and Cabré, X., Fully nonlinear elliptic equations, American Mathematical Society, 1995.
\item[] [5] Caffarelli, L.A., Nirenberg, L. and Spruck, J., The Dirichlet problem for nonlinear second-order elliptic equations. III. Functions of the eigenvalues of the Hessian, Acta Math. 155 (1985), no. 3-4, 261-301.
\item[] [6] Caffarelli, L.A. and Silvestre, L., On the Evans-Krylov theorem, Proc. Amer. Math. Soc. 138 (2010), no. 1, 263-265.
\item[] [7] Calabi, E., Improper affine hyperspheres of convex type and a generalization of a theorem by K. Jörgens, Michigan Math. J. 5 (1958), 105-126.
\item[] [8] Cao, H.-D., Deformation of Kähler metrics to Kähler-Einstein metrics on compact Kähler manifolds, Invent. Math. 81 (1985), no. 2, 359-372.
\item[] [9] Chau, A., Convergence of the Kähler-Ricci flow on noncompact Kähler manifolds, J. Differential Geom. 66 (2004), no. 2, 211-232.
\item[] [10] Chen, X.X., On the lower bound of the Mabuchi energy and its application, Internat. Math. Res. Notices 2000, no. 12, 607-623.
\item[] [11] Chen, X.X., A new parabolic flow in Kähler manifolds, Comm. Anal. Geom. 12 (2004), no. 4, 837-852.
\item[] [12] Chen, X.X. and Tian, G., Geometry of Kähler metrics and foliations by holomorphic discs, Publ. Math. Inst. Hautes Études Sci. 107 (2008), 1-107.
\item[] [13] Cherrier, P., Équations de Monge-Ampère sur les variétés hermitiennes compactes, Bull. Sci. Math. (2) 111 (1987), no. 4, 343-385.
\item[] [14] Chow, B., Lu, P. and Ni, L., Hamilton's Ricci flow, Graduate Studies in Mathematics, 77. American Mathematical Society, Providence, RI; Science Press, New York, 2006.
\item[] [15] Crandall, M.G., Ishii, H. and Lions, P.-L., User's guide to viscosity solutions of second order partial differential equations, Bull. Amer. Math. Soc. (N.S.) 27 (1992), no. 1, 1-67.
\item[] [16] Delanoë, P., Sur l'analogue presque-complexe de l'équation de Calabi-Yau, Osaka J. Math. 33 (1996), no. 4, 829-846.
\item[] [17] Dinew, S. and Kołodziej, S., A priori estimates for the complex Hessian equations, Anal. PDE 7 (2014), no. 1, 227-244.
\item[] [18] Dinew, S. and Kołodziej, S., Liouville and Calabi-Yau type theorems for complex Hessian equations, preprint, arXiv:1203.3995.
\item[] [19] Dinew, S., Zhang, X. and Zhang, X., The $C^{2, \alpha}$ estimate of complex Monge-Ampère equation, Indiana Univ. Math. J. 60 (2011), no. 5, 1713-1722.
\item[] [20] Donaldson, S.K., Moment maps and diffeomorphisms. Sir Michael Atiyah: a great mathematician of the twentieth century, Asian J. Math. 3 (1999), no. 1, 1-15.
\item[] [21] Donaldson, S.K., Two-forms on four-manifolds and elliptic equations, in Inspired by S.S. Chern, World Scientific, 2006.
\item[] [22] Evans, L.C., Classical solutions of fully nonlinear, convex, second order elliptic equations, Comm. Pure Appl. Math 25 (1982), 333-363.
\item[] [23] Fang, H., Lai, M. and Ma, X.-N., On a class of fully nonlinear flows in Kähler geometry, J. Reine Angew. Math. 653 (2011), 189-220.
\item[] [24] Fino, A., Li, Y., Salamon, S. and Vezzoni, L., The Calabi-Yau equation on 4-manifolds over 2-tori, Trans. Amer. Math. Soc. 365 (2013), no. 3, 1551-1575.
\item[] [25] Fu, J., Wang, Z. and Wu, D., Form-type Calabi-Yau equations, Math. Res. Lett. 17 (2010), no. 5, 887-903.
\item[] [26] Fu, J., Wang, Z. and Wu, D., Form-type Calabi-Yau equations on Kähler manifolds of nonnegative orthogonal bisectional curvature, preprint, arXiv:1010.2022.
\item[] [27] Fu, J. and Yau, S.-T., The theory of superstring with flux on non-Kähler manifolds and the complex Monge-Ampère equation, J. Differential Geom. 78 (2008), no. 3, 369-428.
\end{itemize}
[28] Gauduchon, P., La 1-forme de torsion d'une variété hermitienne compacte, Math. Ann. 267 (1984), 495-518.
[29] Gill, M., Convergence of the parabolic complex Monge-Ampère equation on compact Hermitian manifolds, Comm. Anal. Geom. 19 (2011), no. 2, 277-303.
[30] Guan, B. and Li, Q., Complex Monge-Ampère equations and totally real submanifolds, Adv. Math. 225 (2010), no. 3, 1185-1223.
[31] Guan, B. and Sun, W., On a class of fully nonlinear elliptic equations on Hermitian manifolds, to appear in Calc. Var. Partial Differential Equations.
[32] Harvey, F. R. and Lawson, H. B., Dirichlet duality and the nonlinear Dirichlet problem on Riemannian manifolds, J. Differential Geom. 88 (2011), no. 3, 395-482.
[33] Harvey, F.R. and Lawson, H.B., Potential theory on almost complex manifolds, preprint, arXiv:1107.2584.
[34] Hou, Z., Complex Hessian equation on Kähler manifold, Int. Math. Res. Not. IMRN 2009 (2009), no. 16, 3098-3111.
[35] Hou, Z., Ma, X.-N. and Wu, D., A second order estimate for complex Hessian equations on a compact Kähler manifold, Math. Res. Lett. 17 (2010), no. 3, 547-561.
[36] Jbilou, A., Complex Hessian equations on some compact Kähler manifolds, Int. J. Math. Math. Sci. 2012, Art. ID 350183, 48 pp.
[37] Kokarev, V.N., Mixed volume forms and a complex equation of Monge-Ampère type on Kähler manifolds of positive curvature, Izv. Math. 74 (2010), no. 3, 501-514.
[38] Krylov, N.V., Boundedly nonhomogeneous elliptic and parabolic equations, Izvestia Akad. Nauk. SSSR 46 (1982), 487-523; English translation in Math. USSR Izv. 20 (1983), no. 3, 459-492.
[39] Li, S.-Y., On the Dirichlet problems for symmetric function equations of the eigenvalues of the complex Hessian, Asian J. Math. 8 (2004), no. 1, 87-106.
[40] Li, Y., A priori estimates for Donaldson's equation over compact Hermitian manifolds, Calc. Var. Partial Differential Equations 50 (2014), no. 3-4, 867-882.
[41] Li, J. and Yau, S.-T., The existence of supersymmetric string theory with torsion, J. Differential Geom. 70 (2005), no. 1, 143-181.
[42] Li, T.-J. and Zhang, W., Comparing tamed and compatible symplectic cones and cohomological properties of almost complex manifolds, Comm. Anal. Geom. 17 (2009), no. 4, 651-683.
[43] Li, T.-J. and Zhang, W., Almost Kähler forms on rational 4-manifolds, preprint, arXiv:1210.2377
[44] Lu, H.C., Viscosity solutions to complex Hessian equations, J. Funct. Anal. 264 (2013), no. 6, 1355-1379.
[45] Nguyen, N.C., Hölder continuous solutions to complex Hessian equations, preprint, arXiv:1301.0710.
[46] Phong, D.H., Sesum, N. and Sturm, J., Multiplier ideal sheaves and the Kähler-Ricci flow, Comm. Anal. Geom. 15 (2007), no. 3, 613-632.
[47] Pliś, S., The Monge-Ampère equation on almost complex manifolds, Math. Z. 276 (2014), no. 3-4, 969-983.
[48] Popovici, D., Aeppli Cohomology Classes Associated with Gauduchon Metrics on Compact Complex Manifolds, preprint, arXiv:1310.3685.
[49] Savin, O., Small perturbation solutions for elliptic equations, Comm. Partial Differential Equations 32 (2007), no. 4-6, 557-578.
[50] Siu, Y.-T., Lectures on Hermitian-Einstein metrics for stable bundles and Kähler-Einstein metrics, DMV Seminar, 8. Birkhäuser Verlag, Basel, 1987.
[51] Song, J. and Weinkove, B., On the convergence and singularities of the $J$-flow with applications to the Mabuchi energy, Comm. Pure Appl. Math. 61 (2008), no. 2, 210-229.
\begin{itemize}
\item[] [52] Spruck, J., Geometric aspects of the theory of fully nonlinear elliptic equations, in Global theory of minimal surfaces, 283-309, Clay Math. Proc., 2, Amer. Math. Soc., Providence, RI, 2005.
\item[] [53] Sun, W., On a class of fully nonlinear elliptic equations on closed Hermitian manifolds, preprint, arXiv:1310.0362
\item[] [54] Taubes, C.H., Tamed to compatible: symplectic forms via moduli space integration, J. Symplectic Geom. 9 (2011), no. 2, 161-250.
\item[] [55] Tosatti, V. and Weinkove, B., Estimates for the complex Monge-Ampère equation on Hermitian and balanced manifolds, Asian J. Math. 14 (2010), no.1, 19-40.
\item[] [56] Tosatti, V. and Weinkove, B., The complex Monge-Ampère equation on compact Hermitian manifolds., J. Amer. Math. Soc. 23 (2010), no. 4, 1187-1195.
\item[] [57] Tosatti, V. and Weinkove, B., The Calabi-Yau equation, symplectic forms and almost complex structures, in Geometry and Analysis, Vol. I, 475-493, Advanced Lectures in Math. 17, International Press, 2010.
\item[] [58] Tosatti, V. and Weinkove, B., The Calabi-Yau equation on the Kodaira-Thurston manifold, J. Inst. Math. Jussieu 10 (2011), no.2, 437-447.
\item[] [59] Tosatti, V. and Weinkove, B., On the evolution of a Hermitian metric by its Chern-Ricci form, to appear in J. Differential Geom.
\item[] [60] Tosatti, V. and Weinkove, B., The Monge-Ampère equation for $(n-1)$ -plurisubharmonic functions on a compact Kähler manifold, preprint, arXiv:1305.7511.
\item[] [61] Tosatti, V. and Weinkove, B., Hermitian metrics, $(n-1, n-1)$ forms and Monge-Ampère equations, preprint, arXiv:1310.6326.
\item[] [62] Tosatti, V., Weinkove, B. and Yau, S.-T., Taming symplectic forms and the Calabi-Yau equation, Proc. Lond. Math. Soc. (3) 97 (2008), no. 2, 401-424.
\item[] [63] Trudinger, N.S., Fully nonlinear, uniformly elliptic equations under natural structure conditions, Trans. Amer. Math. Soc. 278 (1983), no. 2, 751-769.
\item[] [64] Wang, X.-J., A class of fully nonlinear elliptic equations and related functionals, Indiana Univ. Math. J. 43 (1994), no. 1, 25-54.
\item[] [65] Wang, Y., On the $C^{2, \alpha}$-regularity of the complex Monge-Ampère equation, Math. Res. Lett. 19 (2012), no. 4, 939-946.
\item[] [66] Wang, Y., Small perturbation solutions for parabolic equations, Indiana Univ. Math. J. 62 (2013), no. 2, 671-697.
\item[] [67] Wehrheim, K., Uhlenbeck compactness, EMS Series of Lectures in Mathematics, European Mathematical Society (EMS), Zürich, 2004.
\item[] [68] Weinkove, B., Convergence of the $J$-flow on Kähler surfaces, Comm. Anal. Geom. 12 (2004), no. 4, 949-965.
\item[] [69] Weinkove, B., On the $J$-flow in higher dimensions and the lower boundedness of the Mabuchi energy, J. Differential Geom. 73 (2006), no. 2, 351-358.
\item[] [70] Weinkove, B., The Calabi-Yau equation on almost-Kähler four-manifolds, J. Differential Geom. 76 (2007), no. 2, 317-349.
\item[] [71] Yau, S.-T., On the Ricci curvature of a compact Kähler manifold and the complex Monge-Ampère equation, I, Comm. Pure Appl. Math. 31 (1978), no.3, 339-411.
\end{itemize}

Department of Mathematics, Northwestern University, 2033 Sheridan Road, Evanston, IL 60208
