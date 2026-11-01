---
retention_scope: session
part: 1
total_parts: 3
---

[Part 1/3 of: Fully Non-linear Elliptic Equations on Complex Manifolds]

---
source_file: 2404_12350.pdf
converter: mathpix
format: mmd
---

\title{
FULLY NON-LINEAR ELLIPTIC EQUATIONS ON COMPLEX MANIFOLDS
}

\author{
RIRONG YUAN
}

\begin{abstract}
In this paper, we study a broad class of fully nonlinear elliptic equations on Hermitian manifolds. On one hand, under the optimal structural assumptions we derive $C^{2, \alpha}$-estimate for solutions of the equations on closed Hermitian manifolds. On the other hand, we treat the Dirichlet problem. In both cases, we prove the existence theorems with unbounded condition.
\end{abstract}

\section*{1. Introduction}

Let $(M, \omega)$ be a Hermitian manifold of complex dimension $n, \omega=\sqrt{-1} g_{i \bar{j}} d z^{i} \wedge$ $d \bar{z}^{j}$, and let $\chi=\sqrt{-1} \chi_{i \bar{j}} d z^{i} \wedge d \bar{z}^{j}$ be a smooth real (1,1)-form. We consider the fully nonlinear elliptic equation
$$F(\chi+\sqrt{-1} \partial \bar{\partial} u)=\psi$$
for a given sufficiently smooth function $\psi$ on $M$. The operator has the form
$$F(\chi+\sqrt{-1} \partial \bar{\partial} u) \equiv f\left(\lambda\left[\omega^{-1}(\chi+\sqrt{-1} \partial \bar{\partial} u)\right]\right),$$
where $\lambda\left[\omega^{-1}(\chi+\sqrt{-1} \partial \bar{\partial} u)\right]=\left(\lambda_{1}, \cdots, \lambda_{n}\right)$ denotes the $n$-tuple of eigenvalues of $\chi+\sqrt{-1} \partial \bar{\partial} u$ with respect to $\omega$. Henceforth, $f$ is a smooth symmetric function defined in an open symmetric convex cone $\Gamma \subset \mathbb{R}^{n}$, with vertex at the origin and $\partial \Gamma \neq \emptyset$,
$$\Gamma_{n} \equiv\left\{\left(\lambda_{1}, \cdots, \lambda_{n}\right) \in \mathbb{R}^{n}: \text { each component } \lambda_{i}>0\right\} \subseteq \Gamma .$$
In addition, we assume that $f$ satisfies the following fundamental hypotheses:
$$\begin{gathered}
f_{i}(\lambda)=f_{\lambda_{i}}(\lambda) \equiv \frac{\partial f}{\partial \lambda_{i}}(\lambda)>0 \text { in } \Gamma, \forall 1 \leqslant i \leqslant n, \\
f \text { is a concave function in } \Gamma,
\end{gathered}$$
$$\inf _{M} \psi>\sup _{\partial \Gamma} f,$$
where
$$\sup _{\partial \Gamma} f \equiv \sup _{\lambda_{0} \in \partial \Gamma} \limsup _{\lambda \rightarrow \lambda_{0}} f(\lambda) .$$

Following [7] we call $u$ an admissible function, if at each point $z$
$$\lambda\left[\omega^{-1}(\chi+\sqrt{-1} \partial \bar{\partial} u)\right](z) \in \Gamma .$$
The condition (1.3) ensures the ellipticity of (1.1) at admissible solutions, while (1.5) prevents the equation from degeneracy. Assumption (1.4) guarantees that
$F(\tilde{\chi})$ is concave for $\tilde{\chi}$ with $\lambda\left(\omega^{-1} \tilde{\chi}\right) \in \Gamma$. The assumptions allow us to apply Evans-Krylov theorem to derive $C^{2, \alpha}$ bounds from a priori estimates up to second order.

The study of equations of this type was pioneered by Caffarelli-Nirenberg-Spruck [7]. Perhaps the most important operator of the form (1.2) is the complex Monge-Ampère operator, where we take $f=\sum_{i=1}^{n} \log \lambda_{i}, \Gamma=\Gamma_{n}$. The complex Monge-Ampère equation has played a significant role in Yau's [61] proof of Calabi's conjecture in connection with the Ricci curvature and volume form over Kähler manifolds. Over the past decades, their work has fundamental impact in the study of fully nonlinear equations of elliptic and parabolic type. More recently, Guan [25] and Székelyhidi [52] made important contributions to the notion of subsolution, which is a key ingredient for a priori estimate and solvability of fully nonlinear elliptic equations on closed manifolds.

It is an important problem to establish $C^{2, \alpha}$-estimate for general fully nonlinear elliptic equations on closed complex manifolds, since there have been increasing interests in fully nonlinear PDEs from complex geometry. The problem was studied in existing literature, among which [16, 37, 10, 49, 19, 20, 21, 55, 56, 53, 38, 13, 52], to name just a few, focusing on complex $k$-Hessian equation, $J$-flow and extensions, Form-type Calabi-Yau equation, Monge-Ampère equation for $(n-1)$-PSH functions, deformed Hermitian Yang-Mills equation, and more general equations satisfying an extra assumption that
$$\lim _{t \rightarrow+\infty} f(t \lambda)>f(\mu), \forall \lambda, \mu \in \Gamma .$$
Such a condition or certain slightly stronger assumption was commonly imposed as a key assumption in a huge amount of literature starting from the landmark work of Caffarelli-Nirenberg-Spruck [7]. It is interesting and challenging to drop such additional conditions from the viewpoint of geometry and PDEs.

When $M$ admits nonempty boundary $\partial M$, given a function $\psi$ and a smooth real (1, 1)-form $\chi$ on $\bar{M} \equiv M \cup \partial M$, it is natural to consider the Dirichlet problem
$$F(\chi+\sqrt{-1} \partial \bar{\partial} u)=\psi \text { in } \bar{M}, u=\varphi \text { on } \partial M .$$
The Dirichlet problem for complex Monge-Ampère equation in $\mathbb{C}^{n}$ was solved by Caffarelli-Kohn-Nirenberg-Spruck [6] on strictly pseudoconvex domains. In [24] Guan extended their result to arbitrary bounded smooth domains in $\mathbb{C}^{n}$, assuming existence of subsolution. Under the assumption of existence of a strict subsolution, Li [40] treated the Dirichlet problem for general equations on bounded domains in unbounded case. Nevertheless, the existence and regularity of Dirichlet problem for general fully nonlinear elliptic equations are widely open on curved complex manifolds. The primary obstruction is gradient estimate (first order estimate). To the best knowledge of the author, the direct proof of gradient estimate is rarely known, beyond the complex Monge-Ampère equation [35, 3, 27] and other fairly restrictive cases considered by [29, 62, 64, 69]. This is in contrast with Hessian equations on Riemannian manifolds; we refer to [26] for recent progress on direct proof of gradient estimate with some earlier work by [41, 59].

The subject of this paper is to consider the above-mentioned problems. In particular, we can draw some existence theorems for the equation on closed Hermitian
manifolds and the Dirichlet problem in the unbounded case
$$\lim _{t \rightarrow+\infty} f\left(\lambda_{1}, \cdots, \lambda_{n-1}, \lambda_{n}+t\right)=+\infty, \forall \lambda=\left(\lambda_{1}, \cdots, \lambda_{n}\right) \in \Gamma .$$
1.1. Equations on closed manifolds. The first object of this article is to derive $a$ priori estimate for equation (1.1) on closed Hermitian manifolds. For our purpose, we require the notion of $C$-subsolution.

Definition 1.1 ( $C$-subsolution). We say that a $C^{2}$ function $\underline{u}$ is a $C$-subsolution of (1.1), if for any $z \in M$ the following set is bounded
$$\left\{\mu \in \Gamma: f(\mu)=\psi(z), \mu \in \lambda\left[\omega^{-1}(\chi+\sqrt{-1} \partial \bar{\partial} \underline{u})\right](z)+\Gamma_{n}\right\} .$$

The notion of $\mathcal{C}$-subsolution was developed by Guan [26] and more specifically Székelyhidi [52]. Subsequently, Phong-Tô [45] proposed a parabolic version of $C$-subsolution. For $J$-equation and inverse $\sigma_{k}$ flow, the $C$-subsolution coincides with the cone conditions considered in earlier work [19, 49]. Such a notion is very important, since the $\mathcal{C}$-subsolution assumption can be viewed as an indication of a priori estimate and existence for fully nonlinear equations on closed manifolds.

Our first result may be stated as follows:
Theorem 1.2. Let $(M, \omega)$ be a closed Hermitian manifold. In addition to (1.3), (1.4) and (1.5), we assume $\psi \in C^{\infty}(M)$ and that (1.1) admits a $C$-subsolution $\underline{u} \in C^{2}(M)$. Let $u \in C^{4}(M)$ be an admissible solution to (1.1) with $\sup _{M} u=0$, then for any $\alpha \in(0,1)$ we have
$$\|u\|_{C^{2, \alpha}} \leqslant C,$$
where $C$ is a positive constant depending on the data $(M, \omega), \alpha, f, \psi, \chi$ and $\underline{u}$.
The theorem is optimal in the sense that it fails if any of conditions (1.3), (1.4) and (1.5) is removed. This settles a problem left open by Szèkelyhidi [52], wherein he derived the $C^{2, \alpha}$-estimate under the extra assumption (1.6). As we know, the additional condition (1.6) is a vital ingredient for his approach towards second order estimate and especially gradient estimate via blow-up argument.

Below we sketch the proof of Theorem 1.2. It suffices to set up the estimate for complex Hessian of the solution $u$. With this bound at hand, similar to [27] we can establish the bound on real Hessian of $u$ using maximum principle and then the usual Evans-Krylov theorem [18, 39] gives $C^{2, \alpha}$ estimate.

The $C^{0}$-estimate for (1.1) is known by the work of Székelyhidi [52], generalizing the method that Błocki [2] used in the case of complex Monge-Ampère equation. The strategy is based on Alexandroff-Bakelman-Pucci inequality, which is different from Yau's [61] Moser iteration method. The $C^{0}$-estimate for complex Monge-Ampère equation and more general complex $(k, l)$-quotient equations on closed Hermitian manifolds can also be found in [54] and [51], respectively. Recently, Guo-Phong-Tong [34] gave a PDE proof of sharp $L^{\infty}$-estimate for complex Monge-Ampère equation and some other fully nonlinear elliptic equations.

The main issue is to establish first and second order estimates. In order to set up first order estimate, we use the blow-up method that was developed by Dinew-Kołodziej [16] in the case of complex $k$-Hessian equations. The argument is based
on a Liouville type theorem and the second order estimate of the form
$$\sup _{M}|\partial \bar{\partial} u|_{\omega} \leqslant C\left(1+\sup _{M}|\nabla u|_{\omega}^{2}\right) .$$
Such a second estimate was first established by Hou-Ma-Wu [37] for complex $k$ -Hessian equations on closed Kähler manifolds. More recently, their works were extended by Székelyhidi [52] to general fully nonlinear elliptic equations satisfying (1.6). For more related work, we refer to [55, 56, 53] for Monge-Ampère equation for $(n-1)$-PSH functions, and also to [68] for complex $k$-Hessian equation.

Below, we set up second order estimate of the form (1.9) in generic case.
Theorem 1.3. Under the assumptions of Theorem 1.2, we have
$$\sup _{M}|\partial \bar{\partial} u|_{\omega} \leqslant C\left(1+\sup _{M}|\nabla u|_{\omega}^{2}\right),$$
where $C$ depends on the given data $(M, \omega), f,|\psi|_{C^{2}(M)},|\chi|_{C^{2}(M)}, \underset{M}{\operatorname{Osc}} u$ and $|\underline{u}|_{C^{2}(M)}$.
With the aid of second order estimate of the form (1.9), similar to [16,55] we can construct a function $v: \mathbb{C}^{n} \rightarrow \mathbb{R}$ as the limit of appropriate blowing up sequence. To apply Liouville type theorem, what we need is to give a proper characterization of the function $v$. To this end, for $(f, \Gamma)$ we define the cone
$$\Gamma_{\mathcal{G}}^{f}=\left\{\lambda \in \Gamma: \lim _{t \rightarrow+\infty} f(t \lambda)>-\infty\right\} .$$
In addition, $\stackrel{\circ}{\Gamma}_{\mathcal{G}}^{f}$ denotes the interior of $\Gamma_{\mathcal{G}}^{f}$. And then we may employ Lemma 3.7 to prove that $v$ is a $\stackrel{\circ}{\Gamma}_{\mathcal{G}}^{f}$-solution in the sense of [52, Definition 15]. This will contradict to Székelyhidi's Liouville type theorem [52, Theorem 20] (in analogy with Dinew-Kołodziej [16, Theorem 3.2]) and then give the desired gradient bound.

Comparing with the literature mentioned above, in the proof of Theorem 1.3 a new difficulty we face is that the positive lower bound $\sum_{i=1}^{n} f_{i} \geqslant \delta$ possibly fails when dropping (1.6). In order to overcome this, we propose Lemmas 3.1 and 3.3 below. The idea of exploiting such type lemma is from Guan [25]. With the aid of this lemma, we can make use of $(\underline{u}-u)$ in the construction of auxiliary function in order to overcome the difficulties caused by geometric quantities and equations. The newly introduced terms of the form $1+\left|\sum f_{i} \lambda_{i}\right|$ in Lemma 3.1 will greatly simplify the process of managing and solving general equations under optimal conditions. As usual, the casewise argument of Hou-Ma-Wu [37] is employed. This trick is motivated by the treatment of Chou-Wang [12] on real Hessian equation. In addition, we follow the technique of Szekélyhidi [52] to treat the troublesome third order terms arising from nontrivial torsion tensors of non-Kähler metrics.

Note that in the unbounded case, any admissible function is a $C$-subsolution to (1.1). As a consequence, we obtain the following existence result.

Theorem 1.4. Assume $\sup _{\partial \Gamma} f=-\infty$ and that $f$ satisfies (1.4) and (1.8). Suppose that $M$ carries a $C^{2}$ admissible function $\underline{u}$. Then for any $\psi \in C^{\infty}(M)$, we can find a constant $c$ and a smooth admissible function $u$ with $\sup _{M} u=0$ such that
$$f\left(\lambda\left[\omega^{-1}(\chi+\sqrt{-1} \partial \bar{\partial} u)\right]\right)=\psi+c .$$

When $f$ satisfies (1.6) and (1.3) additionally, the theorem can be found in [45]. The existence result includes among others the celebrated theorem of Yau [61] and the extension of Tosatti-Weinkove [54] to Hermitian case, with important contributions from [11, 27, 35]. Some more special cases embraced by Theorem 1.4 are the complex $k$-Hessian equations and Monge-Ampère equation for $(n-1)$-PSH functions. In addition, the above structural conditions allow the function
$$f=\frac{\sigma_{k+1}}{\sigma_{k}}+\sum_{j=1}^{k} \beta_{j} \log \sigma_{j}, \Gamma=\Gamma_{k}, \forall \beta_{j} \geqslant 0, \sum_{j=1}^{k} \beta_{j}>0,$$
where $\sigma_{k}$ is the $k$-th elementary symmetric function, and $\Gamma_{k}$ is the $k$-Gårding cone.
The Hessian equation with (1.11) was considered by [26]. Notice that the function does not satisfy (1.6). More such functions can be found in literature [26, 32].
1.2. The Dirichlet problem. The second subject of this paper is to study the Dirichlet problem. To do this, we require the notion of admissible subsolution.

Definition 1.5. We say that a $C^{2}$ function $u$ is an admissible subsolution of Dirichlet problem (1.7), if $u$ is an admissible function subject to
$$F(\chi+\sqrt{-1} \partial \bar{\partial} \underline{u}) \geqslant \psi \text { in } \bar{M}, \underline{u}=\varphi \text { on } \partial M .$$

The concept of subsolution was imposed by [24, 28, 36] as a vital tool to deal with second order boundary estimate for Dirichlet problem of Monge-Ampère equation. Also the perspective of subsolutions has a great advantage in applications to certain geometric problems that it relaxes restrictions to the shape of boundary; such as Guan's [30] proof of the Chern-Levine-Nirenberg problem and Chen's [9] work on Donaldson's conjecture (see also [31] for Sasaki geometry counterpart).

In this paper, we solve the Dirichlet problem under subsolution assumption.
Theorem 1.6. Let $(\bar{M}, \omega)$ be a compact Hermitian manifold with smooth boundary. Let $f$ satisfy the hypotheses (1.4) and (1.8). Assume the data $\varphi \in C^{\infty}(\partial M)$ and $\psi \in C^{\infty}(\bar{M})$ satisfy (1.5) and support a $C^{2,1}$-admissible subsolution. Then the Dirichlet problem (1.7) possesses a unique smooth admissible solution $u \in C^{\infty}(\bar{M})$.

We emphasize in Theorem 1.6 the importance of allowing manifolds with boundary of arbitrary geometry, assuming existence of subsolution. To achieve this, a specific problem that we have in mind is to establish boundary estimate of the form
$$\sup _{\partial M}|\partial \bar{\partial} u|_{\omega} \leqslant C\left(1+\sup _{M}|\nabla u|_{\omega}^{2}\right) .$$
The quantitative boundary estimate (1.13) for the Dirichlet problem of complex Monge-Ampère equation was first established by Chen [9] on some product manifolds and later by Phong-Sturm [44] on manifolds with holomorphically flat boundary. Subsequently, such restrictions to boundary were dropped by Boucksom [5]. More recently, the estimate (1.13) for the Dirichlet problem of complex $k$-Hessian equations was obtained by Collins-Picard [14]. However, their methods rely heavily on the specific structure of the Monge-Ampère and $k$-Hessian operators, which cannot be further adapted to treat general equations.

Below, based on Lemma 3.12 we establish the quantitative boundary estimate.
Theorem 1.7. Let $(\bar{M}, \omega)$ and $f$ be as in Theorem 1.6. Assume that $\varphi \in C^{3}(\partial M)$ and $\psi \in C^{1}(\bar{M})$ satisfy (1.5) and support a $C^{2}$-admissible subsolution $\underline{u}$. Then any admissible solution $u \in C^{3}(M) \cap C^{2}(\bar{M})$ to Dirichlet problem (1.7) satisfies
$$\sup _{\partial M}|\partial \bar{\partial} u|_{\omega} \leqslant C\left(1+\sup _{M}|\nabla u|_{\omega}^{2}\right),$$
where $C$ is a positive constant depending on $|\varphi|_{C^{3}(\bar{M})},|\nabla u|_{C^{0}(\partial M)},|\underline{u}|_{C^{2}(\bar{M})},|\psi|_{C^{1}(M)}$, $\partial M$ up to third derivatives, and other known data under control.

Remark 1.8. As shown by Lemma 3.5, the unbound and concavity of $f$ together imply (1.3). Thus we do not impose (1.3) in Theorems 1.4, 1.6 and 1.7.

In [7], the condition (1.8) is necessary for second order boundary estimate for double normal derivative; subsequently, it was further removed by Trudinger [58]. However, their boundary estimates are not in a quantitative form. In order to draw (1.13), we propose Lemma 3.12 to follow the behavior of the equation near boundary as $u_{n \bar{n}}$ grows quadratically in terms of $u_{\alpha \bar{n}}(\alpha<n)$. Together with Lemmas 7.4, 8.1 and 3.7, we may establish quantitative boundary estimate for double normal derivative. Our estimate is new even for equations in Euclidean space. In addition, the boundary estimate is fairly delicate in some case; see Theorems 9.5 and 9.6. Such delicate estimates enable us to study degenerate equation in the sense that
$$\inf _{M} \psi=\sup _{\partial \Gamma} f .$$
which will be shown in Sections 9 and 10. In this case we further assume
$$f \in C^{\infty}(\Gamma) \cap C(\bar{\Gamma}), \text { where } \bar{\Gamma}=\Gamma \cup \partial \Gamma .$$

In conclusion, in the first part of this paper we derive global second estimate and especially extend the blow-up argument to generic case. As a result, under the optimal structural conditions, we establish $C^{2, \alpha}$-estimate for general Hessian type fully nonlinear elliptic equations on closed Hermitian manifolds. Given the assumptions (1.3)-(1.5) and the smoothness condition $\psi \in C^{\infty}(M)$, our result indicates that the sole impediment to achieving $C^{2, \alpha}$ estimate on closed manifolds arises from the existence of a $C$-subsolution. In the second part we first derive the quantitative boundary estimate and then solve the Dirichlet problem, possibly with degenerate right-hand side. No matter the equations are degenerate or not, the existence results for Dirichlet problem of general fully nonlinear elliptic equations are rarely known until this work. Moreover, we construct subsolutions on products, which are of numerous interests from complex geometry and analysis.

In addition, our method applies with almost no change to real Hessian equations
$$f\left(\lambda\left[g^{-1}\left(\nabla^{2} u+A\right)\right]\right)=\psi .$$

In the previous draft [66] of this paper, the Dirichlet problem (1.7) was investigated under the extra assumption (1.6).

The paper is organized as follows. In Section 2 we present notation used in the paper. In Section 3 we prove key lemmas for a priori estimates. In Sections 4 and 5
we derive a priori estimate for equations on closed manifolds. More precisely, we first derive second order estimate in Section 4 and then prove the gradient bound by extending blow-up argument in Section 5. In Section 6 we first construct admissible functions using Morse theory and then solve the equations with type 2 cones. In Sections 7 and 8 we establish quantitative boundary estimate for Dirichlet problem. In Section 9 we study Dirichlet problem for degenerate equations. In Section 10 the subsolutions are constructed when $M$ is a product of a closed complex manifold with a compact Riemann surface with boundary. In addition, we study Dirichlet problem on such products with less regularity assumptions on boundary. In Section 11 we complete the proof of Lemma 3.12.

\section*{2. Notation}

Throughout this paper, we use the notation as follows:
\begin{itemize}
\item[-] $\overrightarrow{\mathbf{1}}=(1, \cdots, 1) \in \mathbb{R}^{n}$.
\item[-] $\delta_{\psi, f}=\inf _{M} \psi-\sup _{\partial \Gamma} f$.
\item[-] $\partial \Gamma^{\sigma}=\{\lambda \in \Gamma: f(\lambda)=\sigma\}, \Gamma^{\sigma}=\{\lambda \in \Gamma: f(\lambda)>\sigma\}, \bar{\Gamma}^{\sigma}=\Gamma^{\sigma} \cup \partial \Gamma^{\sigma}$.
\item[-] $\Gamma_{\infty}=\left\{\left(\lambda_{1}, \cdots, \lambda_{n-1}\right):\left(\lambda_{1}, \cdots, \lambda_{n-1}, R\right) \in \Gamma\right.$ for some $\left.R>0\right\}$.
\item[-] Given a $C^{2}$ function $w$, for simplicity we denote
$$\mathfrak{g}[w] \equiv \chi+\sqrt{-1} \partial \bar{\partial} w .$$
In particular, we write $\mathfrak{g}=\mathfrak{g}[u]$ and $\underline{\mathfrak{g}}=\mathfrak{g}[\underline{u}]$ for solution $u$ and subsolution $\underline{u}$, respectively. In addition, denote $\lambda=\lambda\left(\omega^{-1} \mathfrak{g}\right), \underline{\lambda}=\lambda\left(\omega^{-1} \underline{\mathfrak{g}}\right)$.
\item[-] In local coordinates $z=\left(z^{1}, \cdots, z^{n}\right), z^{i}=x^{i}+\sqrt{-1} y^{i}$
$$\mathfrak{g}=\sqrt{-1} \mathfrak{g}_{i \bar{j}} d z^{i} \wedge d \bar{z}^{j}, \underline{\mathfrak{g}}=\sqrt{-1} \underline{\mathfrak{g}}_{i \bar{j}} d z^{i} \wedge d \bar{z}^{j}$$
\item[-] In computation we use derivatives with respect to the Chern connection $\nabla$ of $\omega$, and write $\partial_{i}=\frac{\partial}{\partial z^{i}}, \bar{\partial}_{i}=\frac{\partial}{\partial \bar{z}^{i}}, \nabla_{i}=\nabla_{\frac{\partial}{\partial z^{i}}}, \nabla_{\bar{i}}=\nabla_{\frac{\partial}{\partial \bar{z}^{i}}}, \nabla_{x^{i}}=\nabla_{\frac{\partial}{\partial x^{i}}}$, $\nabla_{y^{i}}=\nabla_{\frac{\partial}{\partial y^{i}}}, \nabla_{t^{k}}=\nabla_{\frac{\partial}{\partial t^{k}}}$. Given a function $v$, we denote
$$\begin{aligned}
& v_{i}=\partial_{i} v, v_{i}=\partial_{\bar{i}} v, v_{x^{i}}=\nabla_{x^{i}} v, v_{y^{i}}=\nabla_{y^{i}} v, v_{t^{k}}=\nabla_{t^{k}} v, v_{t^{k} t^{l}}=\nabla_{t^{l}} \nabla_{t^{k}} v, \\
& v_{i \bar{j}}=\partial_{i} \bar{\partial}_{j} v, v_{i j}=\partial_{j} \partial_{i} v-\Gamma_{j i}^{k} v_{k}, v_{i \bar{j} k}=\partial_{k} v_{i \bar{j}}-\Gamma_{k i}^{l} v_{l \bar{j}}, \cdots, \text { etc },
\end{aligned}$$
where $\Gamma_{i j}^{k}$ are the Christoffel symbols defined by $\nabla_{\frac{\partial}{\partial z^{i}}} \frac{\partial}{\partial z^{j}}=\Gamma_{i j}^{k} \frac{\partial}{\partial z^{k}}$. Moreover, for $\tilde{\chi}=\sqrt{-1} \tilde{\chi}_{i \bar{j}} d z^{i} \wedge d \bar{z}^{j}$ we write
$$\tilde{\chi}_{i \bar{j} k}=\nabla_{k} \tilde{\chi}_{i \bar{j}}, \quad \tilde{\chi}_{i \bar{j} \bar{k}}=\nabla_{\bar{k}} \tilde{\chi}_{i \bar{j}}, \quad \tilde{\chi}_{i \bar{j} \bar{k} \bar{l}}=\nabla_{\bar{l}} \nabla_{k} \tilde{\chi}_{i \bar{j}} .$$
\item[-] $F^{i \bar{j}}=\frac{\partial F(\mathrm{~g})}{\partial \mathrm{g}_{i j} \bar{j}}, F^{i \bar{j}, k \bar{l}}=\frac{\partial^{2} F(\mathrm{~g})}{\partial \mathrm{g}_{i j} \partial \mathrm{~g}_{k l}}$. Moreover, $F^{i \bar{j}} \mathrm{~g}_{i \bar{j}}=\sum_{i=1}^{n} f_{i}(\lambda) \lambda_{i}, F^{i \bar{j}} g_{i \bar{j}}=$ $\sum_{i=1}^{n} f_{i}(\lambda)$. In view of [7, Lemma 6.2] (with proper order $\underline{\lambda}_{1}, \cdots, \underline{\lambda}_{n}$ ), we have
$$F^{i \bar{j}}\left(\underline{\mathfrak{g}}_{i \bar{j}}-\underline{\mathfrak{g}}_{i \bar{j}}\right) \geqslant \sum_{i=1}^{n} f_{i}(\lambda)\left(\underline{\lambda}_{i}-\lambda_{i}\right) .$$
\end{itemize}
\begin{itemize}
\item[-] $\mathcal{L}$ stands for the linearized operator of (1.1). Locally, it is given by
$$\mathcal{L} v=F^{i \bar{j}} v_{i \bar{j}} .$$
\end{itemize}

\section*{3. Key lemmas}
3.1. A lemma for subsolution. We prove a lemma in order to derive second estimate. The lemma is a refinement of [25, Theorem 2.18], [26, Lemma 1.9] and [52, Proposition 5].

Lemma 3.1. Assume (1.3) and (1.4) hold. Fix $\sigma \in\left(\sup _{\partial \Gamma} f, \sup _{\Gamma} f\right)$. Suppose that $\mu \in \mathbb{R}^{n}$ satisfies for some $\delta, R>0$ that
$$\left(\mu-2 \delta \overrightarrow{\mathbf{1}}+\Gamma_{n}\right) \cap \partial \Gamma^{\sigma} \subset B_{R}(0) .$$
Then there is a constant $\varepsilon$ depending on $\sigma, \mu, \delta, R, f$ (explicitly see (3.7)) such that if $\lambda \in \partial \Gamma^{\sigma}$, then either
$$\sum_{i=1}^{n} f_{i}(\lambda)\left(\mu_{i}-\lambda_{i}\right) \geqslant \varepsilon\left(1+\sum_{i=1}^{n} f_{i}(\lambda)+\left|\sum_{i=1}^{n} f_{i}(\lambda) \lambda_{i}\right|\right),$$
or
$$f_{i}(\lambda) \geqslant \varepsilon\left(1+\sum_{j=1}^{n} f_{j}(\lambda)+\left|\sum_{j=1}^{n} f_{j}(\lambda) \lambda_{j}\right|\right), \forall 1 \leqslant i \leqslant n .$$
Proof. Our proof is based only on the concavity assumption. Denote $\tilde{\mu}=\mu-\delta \overrightarrow{\mathbf{1}}$. By (3.1), there exists a positive constant $R_{0}$ depending only on $\tilde{\mu}$ and $R$ such that
$$f\left(\tilde{\mu}+R_{0} \overrightarrow{\mathbf{e}}_{i}\right)>\sigma, \tilde{\mu}+R_{0} \overrightarrow{\mathbf{e}}_{i} \in \Gamma, \forall 1 \leqslant i \leqslant n,$$
where $\overrightarrow{\mathbf{e}}_{i}$ is the $i$-th standard basis vector in $\mathbb{R}^{n}$.
To see this, we pick some $R_{0}>0$ such that $\tilde{\mu}_{i}+R_{0}>R, \forall 1 \leqslant i \leqslant n$. Suppose by contradiction that $\tilde{\mu}+R_{0} \overrightarrow{\mathbf{e}}_{i^{\prime}} \in \mathbb{R}^{n} \backslash \Gamma^{\sigma}$ for some $i^{\prime}$. Then we take suitable (small) constant $0<\epsilon<R_{0}$ such that $\tilde{\mu}+\left(R_{0}-\epsilon\right) \overrightarrow{\mathbf{e}}_{i^{\prime}} \in \mathbb{R}^{n} \backslash \bar{\Gamma}^{\sigma}$ and $\tilde{\mu}_{i^{\prime}}+R_{0}-\epsilon>R$. From this we know that there is some $t>0$ such that $\tilde{\mu}+\left(R_{0}-\epsilon\right) \overrightarrow{\mathbf{e}}_{i^{\prime}}+t \overrightarrow{\mathbf{1}} \in \partial \Gamma^{\sigma}$, which contradicts to (3.1).

From (3.4) we can see that there is a small constant $0<\epsilon_{1} \ll 1$ depending only on $\tilde{\mu}$ and $\delta$ such that
$$f\left(\left(1+\epsilon_{1}\right) \tilde{\mu}+R_{0} \overrightarrow{\mathbf{e}}_{i}\right)>\sigma, f\left(\left(1-\epsilon_{1}\right) \tilde{\mu}+R_{0} \overrightarrow{\mathbf{e}}_{i}\right)>\sigma, \forall 1 \leq i \leq n .$$
Fix such $\epsilon_{1}$, we take
$$\frac{1}{1+c}= \begin{cases}1-\epsilon_{1} & \text { if } \sum_{i=1}^{n} f_{i}(\lambda) \lambda_{i} \geq 0, \\ 1+\epsilon_{1} & \text { otherwise. }\end{cases}$$
Denote $\delta_{0}=\min \left\{\min _{1 \leqslant i \leqslant n}\left\{f\left(\left(1+\epsilon_{1}\right) \tilde{\mu}+R_{0} \overrightarrow{\mathbf{e}}_{i}\right)-\sigma\right\}, \min _{1 \leqslant i \leqslant n}\left\{f\left(\left(1-\epsilon_{1}\right) \tilde{\mu}+R_{0} \overrightarrow{\mathbf{e}}_{i}\right)-\sigma\right\}\right\}$.
Below we prove that the conclusion holds for
$$\varepsilon=\min \left\{\frac{\delta_{0}}{2 R_{0}}, \frac{\delta\left(1-\epsilon_{1}\right)}{2 R_{0}}, \frac{\epsilon_{1}}{2 R_{0}}, \frac{\delta_{0}}{2\left(1+\epsilon_{1}\right)}, \frac{\delta}{2}, \frac{\epsilon_{1}}{2\left(1+\epsilon_{1}\right)}\right\} .$$

Without loss of generality, assume $\lambda_{1} \leqslant \cdots \leqslant \lambda_{n}$. Then $f_{1}(\lambda) \geqslant \cdots \geqslant f_{n}(\lambda)$. If
$$f_{n}(\lambda)>\frac{\delta_{0}}{2 R_{0}}+\frac{\delta}{2 R_{0}(1+c)} \sum_{i=1}^{n} f_{i}(\lambda)+\frac{c}{2 R_{0}(1+c)} \sum_{i=1}^{n} f_{i}(\lambda) \lambda_{i},$$
then by (3.6)
$$f_{n}(\lambda)>\frac{\delta_{0}}{2 R_{0}}+\frac{\delta\left(1-\epsilon_{1}\right)}{2 R_{0}} \sum_{i=1}^{n} f_{i}(\lambda)+\frac{\epsilon_{1}}{2 R_{0}}\left|\sum_{i=1}^{n} f_{i}(\lambda) \lambda_{i}\right| .$$

From now on we assume
$$\frac{\delta_{0}}{2}+\frac{\delta}{2(1+c)} \sum_{i=1}^{n} f_{i}(\lambda)+\frac{c}{2(1+c)} \sum_{i=1}^{n} f_{i}(\lambda) \lambda_{i} \geqslant R_{0} f_{n}(\lambda) .$$
Note $\mu=\tilde{\mu}+\delta \overrightarrow{\mathbf{1}}$. By the concavity of $f$, using (3.10) below we have
$$\begin{aligned}
\frac{1}{1+c} \sum_{i=1}^{n} f_{i}(\lambda)\left(\mu_{i}-\lambda_{i}\right)= & \sum_{i=1}^{n} f_{i}(\lambda)\left(\frac{1}{1+c} \tilde{\mu}_{i}-\lambda_{i}\right)+\frac{\delta}{1+c} \sum_{i=1}^{n} f_{i}(\lambda)+\frac{c}{1+c} \sum_{i=1}^{n} f_{i}(\lambda) \lambda_{i} \\
= & \sum_{i=1}^{n-1} f_{i}(\lambda)\left(\frac{1}{1+c} \tilde{\mu}_{i}-\lambda_{i}\right)+f_{n}(\lambda)\left(\frac{1}{1+c} \tilde{\mu}_{n}+R_{0}-\lambda_{n}\right) \\
& -R_{0} f_{n}(\lambda)+\frac{\delta}{1+c} \sum_{i=1}^{n} f_{i}(\lambda)+\frac{c}{1+c} \sum_{i=1}^{n} f_{i}(\lambda) \lambda_{i} \\
\geqslant & f\left(\frac{1}{1+c} \tilde{\mu}+R_{0} \overrightarrow{\mathbf{e}}_{n}\right)-f(\lambda)+\frac{\delta}{1+c} \sum_{i=1}^{n} f_{i}(\lambda) \\
& +\frac{c}{1+c} \sum_{i=1}^{n} f_{i}(\lambda) \lambda_{i}-R_{0} f_{n}(\lambda) \\
\geqslant & \delta_{0}+\frac{\delta}{1+c} \sum_{i=1}^{n} f_{i}(\lambda)+\frac{c}{1+c} \sum_{i=1}^{n} f_{i}(\lambda) \lambda_{i}-R_{0} f_{n}(\lambda) \\
\geqslant & \frac{\delta_{0}}{2}+\frac{\delta}{2(1+c)} \sum_{i=1}^{n} f_{i}(\lambda)+\frac{c}{2(1+c)} \sum_{i=1}^{n} f_{i}(\lambda) \lambda_{i} .
\end{aligned}$$
That is
$$\begin{aligned}
\sum_{i=1}^{n} f_{i}(\lambda)\left(\mu_{i}-\lambda_{i}\right) & \geqslant \frac{\delta_{0}(1+c)}{2}+\frac{\delta}{2} \sum_{i=1}^{n} f_{i}(\lambda)+\frac{(1+c) \epsilon_{1}}{2}\left|\sum_{i=1}^{n} f_{i}(\lambda) \lambda_{i}\right| \\
& \geqslant \frac{\delta_{0}}{2\left(1+\epsilon_{1}\right)}+\frac{\delta}{2} \sum_{i=1}^{n} f_{i}(\lambda)+\frac{\epsilon_{1}}{2\left(1+\epsilon_{1}\right)}\left|\sum_{i=1}^{n} f_{i}(\lambda) \lambda_{i}\right| .
\end{aligned}$$ \(\square\)

Remark 3.2. In contrast to previous works [25, 26, 52], Lemma 3.1 stands out prominently due to its inclusion of the new terms of the form $1+\left|\sum f_{i} \lambda_{i}\right|$ in both (3.2) and (3.3). This feature enhances the scope of the results.

As a consequence, we have
Lemma 3.3. Let $(\bar{M}, \omega)$ be a compact Hermitian manifold of complex dimension $n \geqslant 2$ (possibly with boundary). Suppose that there exists a $C$-subsolution $\underline{u} \in$ $C^{2}(\bar{M})$ to the equation (1.1). Then there exists a positive constant $\varepsilon$, independent of $\left(\delta_{\psi, f}\right)^{-1}$, such that either
$$F^{i \bar{j}}\left(\underline{\mathfrak{g}}_{i \bar{j}}-\underline{\mathfrak{g}}_{i \bar{j}}\right) \geqslant \varepsilon\left(1+F^{i \bar{j}} g_{i \bar{j}}+\left|F^{i \bar{j}} \mathfrak{g}_{i \bar{j}}\right|\right)$$
or
$$F^{i \bar{j}} \geqslant \varepsilon\left(1+F^{p \bar{q}} g_{p \bar{q}}+\left|F^{p \bar{q}} \mathfrak{g}_{p \bar{q}}\right|\right) g^{i \bar{j}} .$$
Proof. Since $\underline{u}$ is a $C$-subsolution, $\left(\underline{\lambda}+\Gamma_{n}\right) \cap \partial \Gamma^{\psi(z)}$ is bounded for any $z \in \bar{M}$. Thus, one can choose $\delta$ sufficiently small such that for some $R>0$,
$$\left(\underline{\lambda}-2 \delta \overrightarrow{\mathbf{1}}+\Gamma_{n}\right) \cap \partial \Gamma^{\psi(z)} \subset B_{R}(0), \forall z \in \bar{M} .$$
Combining Lemma 3.1, (2.2) and $F^{i \bar{j}} \mathfrak{g}_{i \bar{j}}=\sum f_{i}(\lambda) \lambda_{i}$, we have either (3.8) or (3.9). From the choice of $\varepsilon$ in (3.2), we see that the constant does not depend on $\left(\delta_{\psi, f}\right)^{-1}$. \(\square\)

Remark 3.4. Note that from concavity assumption (1.4) we can infer that
$$\sum_{i=1}^{n} f_{i}(\lambda)\left(\mu_{i}-\lambda_{i}\right) \geqslant f(\mu)-f(\lambda), \forall \lambda, \mu \in \Gamma .$$
In comparison, Lemmas 3.1 and 3.3 more fully exploit the information about concavity.
3.2. Monotonicity. The following lemma asserts that, together with the unbounded condition, the concavity assumption may imply the monotonicity.

Lemma 3.5. If $f$ satisfies (1.4) and (1.8) in $\Gamma$, then (1.3) holds.
Proof. Suppose $\lambda_{1} \leqslant \cdots \leqslant \lambda_{n}$. Then $f_{1}(\lambda) \geqslant \cdots \geqslant f_{n}(\lambda)$. In view of the concavity and unbound of $f$, by setting $t \gg 1$ we know
$$f_{n}(\lambda) \geqslant \frac{f\left(\lambda_{1}, \cdots, \lambda_{n-1}, \lambda_{n}+t\right)-f(\lambda)}{t}>0 .$$ \(\square\)
3.3. Lemmas for blow-up argument. Let $\Gamma_{\mathcal{G}}^{f}$ be as in (1.10). First, we verify that

Lemma 3.6. Suppose that $f$ satisfies (1.3) and (1.4) in $\Gamma$. Then $\stackrel{\circ}{\Gamma}_{\mathcal{G}}^{f}$ is an open symmetric convex cone with vertex at origin and $\Gamma_{n} \subseteq \stackrel{\circ}{\Gamma}_{\mathcal{G}}^{f} \subseteq \Gamma$.
Proof. It suffices to consider $\Gamma_{\mathcal{G}}^{f}$. By the definition, $\Gamma_{\mathcal{G}}^{f}$ is a cone with vertex at origin and $\Gamma_{\mathcal{G}}^{f} \subseteq \Gamma$. By (1.3), $\Gamma_{n} \subseteq \Gamma_{\mathcal{G}}^{f}$. From the symmetry of $f$ and $\Gamma$, it follows that $\Gamma_{\mathcal{G}}^{f}$ is symmetric. By the concavity of $f$ and convexity of $\Gamma$, for all $\lambda, \mu \in \Gamma$,
$$f(t(s \lambda+(1-s) \mu)) \geqslant s f(t \lambda)+(1-s) f(t \mu), \forall 0 \leqslant s \leqslant 1, \forall t>0 .$$
This implies that $\Gamma_{\mathcal{G}}^{f}$ is convex. \(\square\)

The cone $\Gamma_{\mathcal{G}}^{f}$ is a key ingredient for analyzing the limiting function of blow-up sequence. We start with an observation
$$\sum_{i=1}^{n} f_{i}(\lambda) \mu_{i} \geqslant \limsup _{t \rightarrow+\infty} f(t \mu) / t, \forall \lambda, \mu \in \Gamma .$$
This inequality follows from the concavity of $f$. Now we come to our key lemma.
Lemma 3.7. Suppose that $f$ satisfies (1.4) in $\Gamma$. Then
$$f(\lambda+\mu) \geqslant f(\lambda), \forall \lambda \in \Gamma, \forall \mu \in \Gamma_{\mathcal{G}}^{f} .$$

Proof. From (3.11), for any $\lambda \in \Gamma$ and $\mu \in \Gamma_{\mathcal{G}}^{f}$, we have $\sum_{i=1}^{n} f_{i}(\lambda) \mu_{i} \geqslant 0$. Combining (3.10), we obtain (3.12). \(\square\)

Moreover, we have some criteria for the cone $\Gamma_{\mathcal{G}}^{f}$.
Lemma 3.8. Given $\mu \in \Gamma$. Suppose that $f$ satisfies (1.4) in $\Gamma$. Then the following are mutually equivalent.
\begin{itemize}
\item[(1)] $\lim _{t \rightarrow+\infty} f(t \mu)>-\infty$, i.e., $\mu \in \Gamma_{\mathcal{G}}^{f}$.
\item[(2)] $\limsup f(t \mu) / t \geqslant 0$.
\item[(3)] $\sum_{i=1}^{n \rightarrow+\infty} f_{i}(\lambda) \mu_{i} \geqslant 0, \forall \lambda \in \Gamma$.
\item[(4)] $f(\lambda+\mu) \geqslant f(\lambda), \forall \lambda \in \Gamma$.
\end{itemize}

Proof. Obviously, (3) ⇒ (1) ⇒ (2). By (3.11), (2) ⇒ (3). From (3.10), (3) ⇔ (4). \(\square\)

Remark 3.9. In Lemmas 3.7 and 3.8, the condition (1.3) is not needed.
Remark 3.10. If $f$ is a homogeneous function of degree one, i.e., $f(t \lambda)=t f(\lambda)$ $\forall \lambda \in \Gamma, t>0$, using (3.11) we then obtain a Gårding type inequality
$$\sum_{i=1}^{n} f_{i}(\lambda) \mu_{i} \geqslant f(\mu), \forall \lambda, \mu \in \Gamma .$$

Criteria for the function satisfying (1.6). According to Lemma 3.8, the assumption (1.6) is equivalent to one of the following conditions:
$$\begin{aligned}
& \text { For any } \lambda \in \Gamma, \quad \lim _{t \rightarrow+\infty} f(t \lambda)>-\infty \text {, } \\
& \text { For any } \lambda \in \Gamma, \quad \limsup _{t \rightarrow+\infty} f(t \lambda) / t \geqslant 0 \text {, } \\
& \qquad f(\lambda+\mu)>f(\lambda), \forall \lambda, \mu \in \Gamma \text {, } \\
& \qquad \sum_{i=1}^{n} f_{i}(\lambda) \mu_{i}>0, \forall \lambda, \mu \in \Gamma \text {. }
\end{aligned}$$

Lemma 3.11. In the presence of (1.3) and (1.4), the following are equivalent.
\begin{itemize}
\item[(1)] $f$ satisfies (1.6).
\end{itemize}
\begin{itemize}
\item[(2)] $f$ satisfies (3.13), i.e., $\Gamma_{\mathcal{G}}^{f}=\Gamma$.
\item[(3)] $f$ satisfies (3.14).
\item[(4)] $f$ satisfies (3.15).
\item[(5)] $f$ satisfies (3.16).
\end{itemize}
3.4. A quantitative lemma. One of key ingredients for quantitative boundary estimate for double normal derivative is how to follow the track of the eigenvalues of $\left(\mathfrak{g}_{i \bar{j}}\right)$ as $\mathfrak{g}_{n \bar{n}}$ tends to infinity. To this end, we propose the following lemma. (Since the proof is somewhat complicated and long, we will leave it to Section 11).

Lemma 3.12. Let $A$ be an $n \times n$ Hermitian matrix
$$\left(\begin{array}{ccccc}
d_{1} & & & & a_{1} \\
& d_{2} & & & a_{2} \\
& & \ddots & & \vdots \\
& & & d_{n-1} & a_{n-1} \\
\bar{a}_{1} & \bar{a}_{2} & \cdots & \bar{a}_{n-1} & \mathbf{a}
\end{array}\right)$$
with $d_{1}, \cdots, d_{n-1}, a_{1}, \cdots, a_{n-1}$ fixed, and with $\mathbf{a}$ variable. Denote the eigenvalues of $A$ by $\lambda=\left(\lambda_{1}, \cdots, \lambda_{n}\right)$. Let $\epsilon$ be a fixed positive constant. Suppose that the parameter a satisfies the quadratic growth condition
$$\mathbf{a} \geqslant \frac{2 n-3}{\epsilon} \sum_{i=1}^{n-1}\left|a_{i}\right|^{2}+(n-1) \sum_{i=1}^{n-1}\left|d_{i}\right|+\frac{(n-2) \epsilon}{2 n-3} .$$
Then the eigenvalues (possibly with a proper permutation) behave like
$$\begin{gathered}
d_{\alpha}-\epsilon<\lambda_{\alpha}<d_{\alpha}+\epsilon, \forall 1 \leqslant \alpha \leqslant n-1, \\
\mathbf{a} \leqslant \lambda_{n}<\mathbf{a}+(n-1) \epsilon .
\end{gathered}$$

Remark 3.13. This lemma can be viewed as a quantitative version of [7, Lemma 1.2].

\section*{4. Second estimate and proof of Theorem 1.3}

As above, denote $\lambda\left(\omega^{-1} \mathfrak{g}\right)=\left(\lambda_{1}, \cdots, \lambda_{n}\right)$. Assume $\lambda_{1}: M \rightarrow \mathbb{R}$ is the largest eigenvalue and $\lambda_{1} \geqslant \lambda_{2} \geqslant \cdots \geqslant \lambda_{n}$ at each point. We consider the quantity
$$Q \equiv \lambda_{1} e^{H},$$
where the test function has the form $H=\phi\left(|\nabla u|_{\omega}^{2}\right)+\varphi(u-\underline{u})$. Here
$$\phi(t)=-\frac{1}{2} \log \left(1-\frac{t}{2 K}\right), K=1+\sup _{M}\left(|\nabla u|_{\omega}^{2}+|\nabla(u-\underline{u})|_{\omega}^{2}\right)$$
is the function used in [37], and $\varphi:\left[\right.$ inf $\left._{M}(u-\underline{u}),+\infty\right) \rightarrow \mathbb{R}$ is the function with
$$\varphi(x)=\frac{C_{*}}{1+x-\inf _{M}(u-\underline{u})},$$
where $C_{*} \geqslant 1$ is a large constant to be chosen later. It is easy to verify that
$$\phi^{\prime \prime}=2 \phi^{\prime 2},(4 K)^{-1}<\phi^{\prime}<(2 K)^{-1} \text { for } t \in[0, K],$$
$$\varphi^{\prime}(x)=-\frac{C_{*}}{\left(1+x-\inf _{M}(u-\underline{u})\right)^{2}}, \varphi^{\prime \prime}(x)=\frac{2 C_{*}}{\left(1+x-\inf _{M}(u-\underline{u})\right)^{3}} .$$

Suppose $Q$ achieves its maximum at $z_{0} \in M$. It suffices to prove that at $z_{0}$
$$\lambda_{1} \leqslant C K .$$
We choose local coordinates $z=\left(z^{1}, \cdots, z^{n}\right)$ with origin at $z_{0}$, so that at the origin
$$g_{i \bar{j}}=\delta_{i j}, \mathfrak{g}_{i \bar{j}}=\delta_{i j} \lambda_{i} \text { and } F^{i \bar{j}}=\delta_{i j} f_{i} \text {. }$$
Under the local coordinates, $\left(\lambda_{1}, \cdots, \lambda_{n}\right)$ are the eigenvalues of $A=\left\{A^{i}{ }_{j}\right\}=\left\{g^{i \bar{q}} \mathfrak{g}_{j \bar{q}}\right\}$.
Since the eigenvalues need to be distinct at $z_{0}$, the quantity $Q$ may only be continuous. In order to use maximum principle, we employ the perturbation argument of [52]. Let $B$ be a diagonal matrix $B_{q}^{p}$ with real entries with $B_{1}^{1}=0, B_{n}^{n}>2 B_{2}^{2}$ and $B_{n}^{n}<B_{n-1}^{n-1}<\cdots<B_{2}^{2}<0$ being small. Define the matrix $\tilde{A}=A+B$ with the eigenvalues $\tilde{\lambda}=\left(\tilde{\lambda}_{1}, \cdots, \tilde{\lambda}_{n}\right)$. At the origin, $\tilde{\lambda}_{1}=\lambda_{1}=\mathfrak{g}_{1 \overline{1}}, \tilde{\lambda}_{i}=\lambda_{i}+B_{i}^{i}$ for $i \geqslant 2$ and the eigenvalues of $\tilde{A}$ define $C^{2}$-functions near the origin.

In what follows, the discussion will be given at the origin. Notice that $\tilde{Q}=\tilde{\lambda}_{1} e^{H}$ also achieves its maximum at the same point $z_{0}$ (we may assume $\lambda_{1}>K$ ). Then
$$\begin{gathered}
\frac{\tilde{\lambda}_{1, i}}{\lambda_{1}}+H_{i}=0, \frac{\tilde{\lambda}_{1, \bar{i}}}{\lambda_{1}}+H_{\bar{i}}=0, \\
\frac{\tilde{\lambda}_{1, \bar{i}}}{\lambda_{1}}-\frac{\left|\tilde{\lambda}_{1, i}\right|^{2}}{\lambda_{1}^{2}}+H_{\bar{i} \bar{i}} \leqslant 0 .
\end{gathered}$$

By straightforward calculations, one obtains
$$\tilde{\lambda}_{1, i}=\mathfrak{g}_{1 \overline{1} i}+\left(B_{1}^{1}\right)_{i} .$$
Moreover
$$\begin{aligned}
\tilde{\lambda}_{1, \bar{i} \bar{i}}= & \sum_{k>1} \frac{\left|\mathfrak{g}_{k \overline{1} i}\right|^{2}+\left|\mathfrak{g}_{1 \bar{k} i}\right|^{2}}{\tilde{\lambda}_{1}-\tilde{\lambda}_{k}}+2 \Re \mathrm{e} \sum_{k>1} \frac{\mathfrak{g}_{k \overline{1} i}\left(B_{k}^{1}\right)_{\bar{i}}+\mathfrak{g}_{1 \bar{k} i}\left(B_{1}^{k}\right)_{\bar{i}}}{\tilde{\lambda}_{1}-\tilde{\lambda}_{k}} \\
& +\mathfrak{g}_{1 \overline{1} \bar{i} \bar{i}}-\left(B_{1}^{1}\right)_{\overline{i i}}+\tilde{\lambda}_{1}{ }^{p q, r s}\left(B_{q}^{p}\right)_{i}\left(B_{s}^{r}\right)_{\bar{i}},
\end{aligned}$$
where $\tilde{\lambda}_{1}^{p q, r s}=\left(1-\delta_{1 p}\right) \frac{\delta_{1 q} \delta_{1 r} \delta_{p s}}{\tilde{\lambda}_{1}-\tilde{\lambda}_{p}}+\left(1-\delta_{1 r}\right) \frac{\delta_{1 s} \delta_{1 p} \delta_{r q}}{\tilde{\lambda}_{1}-\tilde{\lambda}_{r}}$, see e.g. [50].
We need to estimate $\tilde{\lambda_{1}}-\tilde{\lambda_{p}}$ near the origin for $p>1$. Since $\sum \tilde{\lambda_{i}}>\sum_{k=1}^{n} B_{k}^{k}$, and then $\left|\tilde{\lambda}_{i}\right| \leqslant(n-1) \tilde{\lambda}_{1}+\sum_{k}\left|B_{k}^{k}\right|$ for all $i$. We assume $\tilde{\lambda}_{1}$ is large such that $\tilde{\lambda}_{1} \geqslant \sum\left|B_{k}^{k}\right|$, hence $\left(\tilde{\lambda}_{1}-\tilde{\lambda}_{k}\right)^{-1} \geqslant\left(n \tilde{\lambda}_{1}\right)^{-1}$ for $k>1$. On the other hand, $\left(\tilde{\lambda}_{1}-\tilde{\lambda}_{k}\right) \leqslant 2\left(-B_{n}^{n}\right)^{-1}$ for $k>1$. Using Cauchy-Schwarz inequality, as in [52] from (4.9) we obtain
$$\tilde{\lambda}_{1, \bar{i} \bar{i}} \geqslant \mathfrak{g}_{1 \overline{1} \bar{i}}+\frac{1}{2 n \lambda_{1}} \sum_{k>1}\left(\left|\mathfrak{g}_{k \overline{1} i}\right|^{2}+\left|\mathfrak{g}_{1 \bar{k} i}\right|^{2}\right)-1,$$
when $B$ is chosen sufficiently small. Moreover, we have the elementary inequality
$$\frac{1}{n \lambda_{1}^{2}} \sum_{k>1} F^{i \bar{i}}\left|\mathfrak{g}_{1 \bar{k} i}\right|^{2}+\frac{2}{\lambda_{1}} \Re \mathfrak{e}\left(F^{i \bar{i}} \bar{T}_{1 i}^{j} \mathfrak{g}_{1 \bar{j} i}\right) \geqslant \frac{2}{\lambda_{1}} \Re \mathfrak{e}\left(F^{i \bar{i}} \bar{T}_{1 i}^{1} \mathfrak{g}_{1 \overline{1} i}\right)-C_{1} \sum F^{i \bar{i}} .$$

Differentiating the equation (1.1) twice (using covariant derivative), we have
$$F^{i \bar{i}} \mathfrak{g}_{\bar{i} \bar{l} l}=\psi_{l}, F^{i \bar{i}} \mathfrak{g}_{i \bar{i} \overline{1} \overline{1}}=\psi_{1 \overline{1}}-F^{i \bar{j}, l \bar{m}} \mathfrak{g}_{i \bar{j} 1} \mathfrak{g}_{l \bar{m} \overline{1}},$$
and so
$$F^{i \bar{i}} \mathfrak{g}_{1 \overline{1} \bar{i} \bar{i}} \geqslant-F^{i \bar{j}, l \bar{m}} \mathfrak{g}_{i \bar{j} 1} \mathfrak{g}_{l \bar{m} \overline{1}}+2 \Re \mathfrak{e}\left(F^{i \bar{i}} \bar{T}_{1 i}^{j} \mathfrak{g}_{1 \bar{j} i}\right)+\psi_{1 \overline{1}}-C_{2} \lambda_{1} \sum F^{\bar{i} \bar{i}} .$$
Here we use the following standard formula
$$\begin{gathered}
u_{i \bar{j} k}-u_{k \bar{j} i}=T_{i k}^{l} u_{l \bar{j}}, \\
u_{1 \overline{1} \bar{i} \bar{i}}-u_{i \bar{i} 1 \overline{1}}=R_{\bar{i} \overline{1} \bar{p}} u_{p \overline{1}}-R_{1 \overline{1} i \bar{p}} u_{p \bar{i}}+2 \Re \mathfrak{e}\left\{\bar{T}_{1 i}^{j} u_{i \bar{j} 1}\right\}+T_{i 1}^{p} \bar{T}_{i 1}^{q} u_{p \bar{q}},
\end{gathered}$$
where
$$T_{i j}^{k}=g^{k \bar{l}}\left(\partial_{i} g_{j \bar{l}}-\partial_{j} g_{i \bar{l}}\right), R_{i \bar{j} k \bar{l}}=-\partial_{\bar{j}} \partial_{i} g_{k \bar{l}}+g^{p \bar{q}} \partial_{i} g_{k \bar{q}} \partial_{\bar{j}} g_{p \bar{l}} .$$

From (4.10), (4.12), (4.11) and (4.8), we conclude that
$$\mathcal{L}\left(\log \tilde{\lambda}_{1}\right) \geqslant-F^{\bar{i} \bar{i}} \frac{\left|\tilde{\lambda}_{1, i}\right|^{2}}{\lambda_{1}^{2}}-\frac{F^{i \bar{j}, l \bar{m}} \mathfrak{g}_{i \bar{j} 1} \mathfrak{g}_{l \bar{m} \overline{1}}}{\lambda_{1}}+2 \Re \mathfrak{e}\left(F^{\overline{i i}} \bar{T}_{1 i}^{1} \frac{\tilde{\lambda}_{1, i}}{\lambda_{1}}\right)+\frac{\psi_{1 \overline{1}}}{\lambda_{1}}-C_{3} \sum F^{\overline{i i}} .$$

The straightforward computation gives that
$$\begin{aligned}
\mathcal{L}\left(|\nabla u|_{\omega}^{2}\right)= & F^{i \bar{i}}\left(\left|u_{k i}\right|^{2}+\left|u_{i \bar{k}}\right|^{2}\right)-2 \Re \mathfrak{e}\left\{F^{i \bar{i}} T_{i k}^{l} u_{\bar{k}} u_{\bar{l}}\right\} \\
& +2 \Re \mathfrak{e}\left\{\left(\psi_{k}-F^{i \bar{i}} \chi_{\bar{i} \bar{k}}\right) u_{\bar{k}}\right\}+F^{i \bar{i}} R_{\bar{i} \bar{k} l} u_{l} u_{\bar{k}},
\end{aligned}$$
and so
$$\begin{aligned}
\mathcal{L} H \geqslant & \frac{1}{2} \phi^{\prime} F^{\bar{i} \bar{i}}\left(\left|u_{k i}\right|^{2}+\left|u_{k i}\right|^{2}\right)+\varphi^{\prime} \mathcal{L}(u-\underline{u})+\phi^{\prime \prime} F^{\overline{i i}}\left|\left(|\nabla u|_{\omega}^{2}\right)_{i}\right|^{2} \\
& +\varphi^{\prime \prime} F^{i \bar{i}}\left|(u-\underline{u})_{i}\right|^{2}+2 \phi^{\prime} \Re e\left\{\psi_{k} u_{\bar{k}}\right\}-C_{4} \sum F^{i \bar{i}} .
\end{aligned}$$

Combining (4.13) and (4.15), we derive that
$$\begin{aligned}
0 \geqslant & \frac{1}{2} \phi^{\prime} F^{i \bar{i}}\left(\left|u_{k i}\right|^{2}+\left|u_{k \bar{i}}\right|^{2}\right)+\varphi^{\prime} \mathcal{L}(u-\underline{u})+\phi^{\prime \prime} F^{i \bar{i}}\left|\left(|\nabla u|_{\omega}^{2}\right)_{i}\right|^{2} \\
& +\varphi^{\prime \prime} F^{i \bar{i}}\left|(u-\underline{u})_{i}\right|^{2}-\frac{F^{i \bar{j}, l \bar{m}} \mathfrak{g}_{i \bar{j} 1} \mathfrak{g}_{l \bar{m} \overline{1}}}{\lambda_{1}}-F^{i \bar{i}} \frac{\left|\tilde{\lambda}_{1, i}\right|^{2}}{\lambda_{1}^{2}} \\
& +2 \Re \mathfrak{e}\left(F^{i \bar{i}} \bar{T}_{1 i}^{1} \frac{\tilde{\lambda}_{1, i}}{\lambda_{1}}\right)+2 \phi^{\prime} \Re e\left\{\psi_{k} u_{\bar{k}}\right\}+\frac{\psi_{1 \overline{1}}}{\lambda_{1}}-C_{5} \sum F^{i \bar{i}} .
\end{aligned}$$

Case I. Assume that $\delta \lambda_{1} \geqslant-\lambda_{n}\left(0<\delta \ll \frac{1}{2}\right)$. Set
$$I=\left\{i: F^{i \bar{i}}>\delta^{-1} F^{1 \overline{1}}\right\} \text { and } J=\left\{i: F^{i \bar{i}} \leqslant \delta^{-1} F^{1 \overline{1}}\right\} .$$
Clearly $1 \in J$. Moreover, the identity (4.6) implies that for any index $1 \leqslant i \leqslant n$
$$-\frac{\left|\tilde{\lambda}_{1, i}\right|^{2}}{\lambda_{1}^{2}} \geqslant-2 \varphi^{\prime 2}\left|(u-\underline{u})_{i}\right|^{2}-2 \phi^{\prime 2}\left|\left(|\nabla u|_{\omega}^{2}\right)_{i}\right|^{2} .$$

By an inequality from concavity and symmetry of $f$ (see [1] or [22]), we derive
$$-F^{i \bar{j}, l \bar{m}} \mathfrak{g}_{i \bar{j} 1} \mathfrak{g}_{l \bar{m} \overline{1}} \geqslant \sum_{i \in I} \frac{F^{i \bar{i}}-F^{1 \overline{1}}}{\lambda_{1}-\lambda_{i}}\left|\mathfrak{g}_{i \overline{1} 1}\right|^{2} \geqslant \sum_{i \in I} \frac{1-\delta}{\lambda_{1}-\lambda_{i}} F^{i \bar{i}}\left|\mathfrak{g}_{i \overline{1} 1}\right|^{2} .$$
The assumption $\delta \lambda_{1} \geqslant-\lambda_{n}$ implies $\frac{1-\delta}{\lambda_{1}-\lambda_{i}} \geqslant \frac{1-2 \delta}{\lambda_{1}}$. Therefore, we can deduce that
$$\begin{gathered}
-\frac{F^{i \bar{j}, l \bar{m}} \mathfrak{g}_{i \bar{j} 1} \mathfrak{g}_{l \bar{m}} \overline{1}}{\lambda_{1}}-F^{i \bar{i}} \frac{\left|\tilde{\lambda}_{1, i}\right|^{2}}{\lambda_{1}^{2}} \geqslant(1-2 \delta) \sum_{i \in I} F^{i \bar{i}} \frac{\left|\mathfrak{g}_{i \overline{1} 1}\right|^{2}}{\lambda_{1}^{2}}-F^{i \bar{i}} \frac{\left|\tilde{\lambda}_{1, i}\right|^{2}}{\lambda_{1}^{2}} \\
\geqslant(1-2 \delta) \sum_{i \in I} F^{i \bar{i}} \frac{\left|\mathfrak{g}_{i \overline{1} 1}\right|^{2}-\left|\tilde{\lambda}_{1, i}\right|^{2}}{\lambda_{1}^{2}} \\
-4 \delta \varphi^{\prime 2} \sum_{i \in I} F^{i \bar{i}}\left|(u-\underline{u})_{i}\right|^{2} \\
-2 \varphi^{\prime 2} \delta^{-1} F^{1 \overline{1}} K-2 \phi^{\prime 2} F^{i \bar{i}}\left|\left(|\nabla u|_{\omega}^{2}\right)_{i}\right|^{2} .
\end{gathered}$$

Write $g_{i \overline{1} 1}=\tilde{\lambda}_{1, i}+\tau_{i}$, where $\tau_{i}=\chi_{i \overline{1} 1}-\chi_{1 \overline{1} i}+T_{i 1}^{l} u_{l \overline{1}}-\left(B_{1}^{1}\right)_{i}$. A straightforward computation gives
$$\left|g_{i \overline{1} 1}\right|^{2}-\left|\tilde{\lambda}_{1, i}\right|^{2}=\left|\tau_{i}\right|^{2}+2 \operatorname{Re}\left(\tilde{\lambda}_{1, i} \bar{\tau}_{i}\right) \geqslant-C_{6}\left(\lambda_{1}^{2}+\left|\tilde{\lambda}_{1, i}\right|\right)+2 \lambda_{1} \operatorname{Re}\left(\bar{T}_{i 1}^{1} \tilde{\lambda}_{1, i}\right) .$$
For any $\epsilon>0$ and $1 \leqslant i \leqslant n$, we have by (4.6) and (4.3)
$$\frac{\left|\tilde{\lambda}_{1, i}\right|}{\lambda_{1}} \leqslant \frac{1}{2 \epsilon}+\frac{\epsilon}{2} \phi^{\prime} \sum_{k=1}^{n}\left(\left|\left(\left.u_{k i}\right|^{2}+\left|u_{\bar{k} i}\right|^{2}\right)+\left|\varphi^{\prime}(u-\underline{u})_{i}\right| .\right.\right.$$
By (4.3), $\phi^{\prime \prime}=2 \phi^{\prime 2}$. Together with (4.18), (4.19) and (4.16), we obtain
$$\begin{aligned}
0 \geqslant & \frac{1}{2} \phi^{\prime} F^{\bar{i} \bar{i}}\left(\left|u_{k i}\right|^{2}+\left|u_{k i}\right|^{2}\right)+\varphi^{\prime} \mathcal{L}(u-\underline{u})+\left(\varphi^{\prime \prime}-4 \delta \varphi^{\prime 2}\right) F^{i \bar{i}}\left|(u-\underline{u})_{i}\right|^{2} \\
& +2 \Re \mathrm{e}\left(\sum_{i \in J} F^{i \bar{i}} \bar{T}_{1 i}^{1} \frac{\tilde{\lambda}_{1, i}}{\lambda_{1}}\right)+4 \delta \Re \mathrm{e}\left(\sum_{i \in I} F^{i \bar{i}} \bar{T}_{1 i}^{1} \frac{\tilde{\lambda}_{1, i}}{\lambda_{1}}\right)-C_{6} \sum_{i \in I} F^{i \bar{i}} \frac{\left|\tilde{\lambda}_{1, i}\right|}{\lambda_{1}^{2}} \\
& -2 \varphi^{\prime 2} \delta^{-1} F^{1 \overline{1}} K+2 \phi^{\prime} \Re e\left\{\psi_{k} u_{\bar{k}}\right\}+\frac{\psi_{1 \overline{1}}}{\lambda_{1}}-C_{7} \sum F^{i \bar{i}} .
\end{aligned}$$
Note that $\left|u_{\bar{i}}\right|^{2}=\left|\mathfrak{g}_{\bar{i} \bar{i}}-\chi_{\bar{i} \bar{i}}\right|^{2} \geqslant \frac{1}{2}\left|\mathfrak{g}_{\bar{i} \bar{i}}\right|^{2}-\left|\chi_{\bar{i} \bar{i}}\right|^{2}$ and $2 \delta<1$. Combining (4.20) and (4.3),
$$\begin{aligned}
0 \geqslant & \frac{1}{32 K} F^{i \bar{i}} \mathfrak{g}_{\bar{i} \bar{i}}^{2}+\varphi^{\prime} \mathcal{L}(u-\underline{u})+\left(\frac{1}{2} \varphi^{\prime \prime}-4 \delta \varphi^{\prime 2}\right) F^{i \bar{i}}\left|(u-\underline{u})_{i}\right|^{2} \\
& -2 \delta^{-1} T\left|\varphi^{\prime}\right| F^{1 \overline{1}} \sqrt{K}-2 \delta^{-1} \varphi^{\prime 2} F^{1 \overline{1}} K-\frac{C_{9}}{\sqrt{K}}+\frac{\psi_{1 \overline{1}}}{\lambda_{1}} \\
& -\left(C_{8}+\frac{8 \delta^{2} T^{2} \varphi^{\prime 2}}{\varphi^{\prime \prime}}+C_{6} \lambda_{1}^{-1}\left|\varphi^{\prime}\right| \sqrt{K}\right) \sum F^{i \bar{i}} .
\end{aligned}$$
where $T=\sup \left|T_{j i}^{j}\right|$. Here we also use the elementary inequality
$$\frac{1}{2} \varphi^{\prime \prime} F^{i \bar{i}}\left|(u-\underline{u})_{i}\right|^{2}-4 \delta T F^{i \bar{i}}\left|\varphi^{\prime}(u-\underline{u})_{i}\right| \geqslant-\frac{8 \delta^{2} T^{2} \varphi^{\prime 2}}{\varphi^{\prime \prime}} \sum F^{i \bar{i}} .$$

Let $\varepsilon$ be the constant as in Lemma 3.3. Pick $C_{*} \gg 1$ such that
$$-\frac{\varepsilon}{2} \varphi^{\prime} \geqslant \frac{\varepsilon C_{*}}{2\left(1+\sup _{M}(u-\underline{u})-\inf _{M}(u-\underline{u})\right)^{2}}>1+C_{8}+C_{9} .$$
Fix such $C_{*}$ we then find $\delta$ sufficiently small so that $4 \delta \varphi^{\prime 2}<\frac{1}{2} \varphi^{\prime \prime}, \delta T^{2}<\frac{1}{2}$. Thus
$$\begin{aligned}
0 \geqslant & \frac{1}{32 K} F^{i \bar{i}} \mathfrak{g}_{\bar{i} \bar{i}}^{2}+\varphi^{\prime} \mathcal{L}(u-\underline{u})-\left(C_{8}+\delta T^{2}+C_{6} \lambda_{1}^{-1}\left|\varphi^{\prime}\right| \sqrt{K}\right) \sum F^{i \bar{i}} \\
& -2 \delta^{-1} \varphi^{\prime 2} F^{1 \overline{1}} K-2 \delta^{-1} T\left|\varphi^{\prime}\right| F^{1 \overline{1}} \sqrt{K}-\frac{C_{9}}{\sqrt{K}}+\frac{\psi_{1 \overline{1}}}{\lambda_{1}} .
\end{aligned}$$

Below our discussion is based on Lemma 3.3. According to Lemma 3.3, in the first case we may assume
$$\mathcal{L}(\underline{u}-u) \geqslant \varepsilon\left(1+\sum F^{\bar{i}}\right) .$$
Then by (4.25) we get
$$\lambda_{1} \leqslant C K .$$

In the second case, we have
$$f_{i} \geqslant \varepsilon\left(1+\sum_{j=1}^{n} f_{j}\right), \forall 1 \leqslant i \leqslant n .$$
Together with (4.25), (2.2) and (3.10), we thus obtain
$$\begin{aligned}
0 \geqslant & \frac{\varepsilon}{32 K}|\mathfrak{g}|^{2}\left(1+\sum F^{i \bar{i}}\right)-\left(C_{8}+\delta T^{2}+C_{6} \lambda_{1}^{-1}\left|\varphi^{\prime}\right| \sqrt{K}\right) \sum F^{i \bar{i}} \\
& +\varphi^{\prime}(\psi-F(\underline{\mathfrak{g}}))-2 \varphi^{\prime 2} \delta^{-1} F^{1 \overline{1}} K-2 T \delta^{-1}\left|\varphi^{\prime}\right| F^{1 \overline{1}} \sqrt{K}-\frac{C_{9}}{\sqrt{K}}+\frac{\psi_{1 \overline{1}}}{\lambda_{1}} .
\end{aligned}$$
Consequently, we can derive that
$$\lambda_{1} \leqslant C K .$$

Case II. We assume that $\delta \lambda_{1}<-\lambda_{n}$ with the constants $C_{*}, N$ and $\delta$ fixed as in the previous case. Then $\left|\lambda_{i}\right| \leqslant \frac{1}{\delta}\left|\lambda_{n}\right|$ for all $i$. Note that $F^{n \bar{n}} \geqslant \frac{1}{n} \sum F^{\overline{i i}},\left|u_{n \bar{n}}\right|^{2}=$ $\frac{1}{2}\left|\mathfrak{g}_{n \bar{n}}\right|^{2}-\left|\chi_{n \bar{n}}\right|^{2} \geqslant \frac{\delta^{2}}{2} \lambda_{1}^{2}-\left|\chi_{n \bar{n}}\right|^{2}$ and $-F^{i \bar{j}, l \bar{m}} \mathfrak{g}_{i \bar{j} 1} \mathfrak{g}_{l \bar{m} \overline{1}} \geq 0$. From (2.2) and (3.10) we see $\mathcal{L}(\underline{u}-u) \geq F(\underline{\mathfrak{g}})-\psi$. Combining (4.16), (4.3), (4.17) and (4.20) we obtain
$$\begin{aligned}
0 \geqslant & \frac{1}{2} \phi^{\prime} F^{\overline{i i}}\left(\left|u_{k i}\right|^{2}+\left|u_{k i}\right|^{2}\right)+\varphi^{\prime} \mathcal{L}(u-\underline{u})+2 \phi^{\prime} \Re \mathfrak{e}\left\{\psi_{k} u_{k}\right\} \\
& +\left(\varphi^{\prime \prime}-2 \varphi^{\prime 2}\right) F^{i \bar{i}}\left|(u-\underline{u})_{i}\right|^{2}+\frac{\psi_{1 \overline{1}}}{\lambda_{1}}-C_{5} \sum F^{i \bar{i}}+2 \Re \mathfrak{e}\left(F^{i \bar{i}} \bar{T}_{1 i}^{1} \frac{\tilde{\lambda}_{1}, i}{\lambda_{1}}\right) \\
\geqslant & \frac{\delta^{2}}{32 n K} \lambda_{1}^{2} \sum F^{i \bar{i}}+\varphi^{\prime}(\psi-F(\underline{\mathfrak{g}}))+\left(\varphi^{\prime \prime}-2 \varphi^{\prime 2}\right) F^{i \bar{i}}\left|(u-\underline{u})_{i}\right|^{2} \\
& -\left(C_{10}+2 T\left|\varphi^{\prime}\right| \sqrt{K}\right) \sum F^{\overline{i i}}-\frac{C_{9}}{\sqrt{K}}+\frac{\psi_{1 \overline{1}}}{\lambda_{1}} .
\end{aligned}$$

By an observation of [26], the concavity assumption implies that there exist $R_{1}$, $c_{1}>0$ depending only on $\sup _{M} \psi$ and $f$ such that
$$|\lambda| \sum_{i=1}^{n} f_{i}(\lambda) \geqslant c_{1} \text { in }\left\{\lambda \in \Gamma: \inf _{M} \psi \leqslant f(\lambda) \leqslant \sup _{M} \psi\right\} \text { when }|\lambda| \geqslant R_{1} .$$
Consequently, together with (4.29) we may conclude that $\lambda_{1} \leqslant C K$.

\section*{5. Blow-up argument and completion of proof of Theorem 1.2}

Under optimal structural conditions, we derive gradient estimate.
Theorem 5.1. In the setting of Theorem 1.2, let $u$ be an admissible solution to (1.1) with $\sup _{M} u=0$. Then there is a constant $C$ such that
$$\sup _{M}|\nabla u|_{\omega} \leqslant C .$$
Proof. Let $\left\{\psi_{j}\right\}$ be a sequence of smooth functions such that
$$\left|\psi_{j}\right|_{C^{2}(M)} \leqslant C, \sup _{\partial \Gamma} f<\inf _{M} \psi_{j}-\delta, \sup _{M} \psi_{j}+\delta<\sup _{\Gamma} f$$
uniformly hold for some $\delta, C>0$, and the corresponding equations
$$f\left(\lambda\left[\omega^{-1}\left(\chi+\sqrt{-1} \partial \bar{\partial} u_{j}\right)\right]\right)=\psi_{j}$$
admit $C$-subsolutions $\underline{u}_{j}$ with uniform bound $\left|\underline{u}_{j}\right|_{C^{2}(M)} \leqslant C, \forall j$.
Assume by contradiction that (5.1) does not hold. Then there exist $\psi_{j}$ as above such that the corresponding equations possess smooth admissible solutions $u_{j}$ satisfying
$$\sup _{M} u_{j}=0, R_{j} \equiv \sup _{M}\left|\nabla u_{j}\right|_{\omega} \rightarrow+\infty \text { as } j \rightarrow+\infty .$$
In addition, for any $j$ there exists some $x_{j} \in M$ such that
$$R_{j}=\left|\nabla u_{j}\left(x_{j}\right)\right|_{\omega} .$$
Up to passing to a subsequence, we may assume $x_{j} \rightarrow x \in M$ as $j \rightarrow+\infty$.
Using localization, without loss of generality, we may choose a coordinate chart $\left\{U,\left(z^{1}, \cdots, z^{n}\right)\right\}$ centered at $x$, identifying with the ball $B_{2}(0) \subset \mathbb{C}^{n}$ of radius 2 centered at origin such that $\omega(x)=\beta$, where $\beta=\sqrt{-1} \sum d z^{i} \wedge d \bar{z}^{i}$. We assume that $j$ is sufficiently large so that the points $z_{j}=z\left(x_{j}\right) \in B_{1}(0)$. Define the maps
$$\begin{gathered}
\Phi_{j}: \mathbb{C}^{n} \rightarrow \mathbb{C}^{n}, \Phi_{j}(z)=z_{j}+R_{j}^{-1} z, \\
\tilde{u}_{j}: B_{R_{j}}(0) \rightarrow \mathbb{R}, \tilde{u}_{j}(z)=u_{j} \circ \Phi_{j}(z)=u_{j}\left(z_{j}+R_{j}^{-1} z\right), \\
\tilde{\psi}_{j}: B_{R_{j}}(0) \rightarrow \mathbb{R}, \tilde{\psi}_{j}(z)=\psi_{j} \circ \Phi_{j}(z)=\psi_{j}\left(z_{j}+R_{j}^{-1} z\right) .
\end{gathered}$$

Denote
$$\beta_{j}=R_{j}^{2} \Phi_{j}^{*} \omega, \chi_{j}=\Phi_{j}^{*} \chi .$$
Then the equation $f\left(\lambda\left[\omega^{-1}\left(\chi+\sqrt{-1} \partial \bar{\partial} u_{j}\right)\right]\right)=\psi_{j}$ implies that
$$f\left(R_{j}^{2} \lambda\left[\beta_{j}^{-1}\left(\chi_{j}+\sqrt{-1} \partial \bar{\partial} \tilde{u}_{j}\right)\right]\right)=\tilde{\psi}_{j} .$$

On the chart near $x, \beta_{j} \rightarrow \beta$ and $\chi_{j}(z) \rightarrow 0$, in $C_{\text {loc }}^{\infty}$, as $j \rightarrow+\infty$. Then we get
$$\lambda\left[\beta_{j}^{-1}\left(\chi_{j}+\sqrt{-1} \partial \bar{\partial} \tilde{u}_{j}\right)\right]=\lambda\left(\tilde{u}_{j, p \bar{q}}\right)+O\left(R_{j}^{-2}|z|\right) .$$

From the $C^{0}$-estimate in [52], $\sup _{M}\left|u_{j}\right| \leqslant C$. By the construction
$$\sup _{B_{R_{j}}(0)}\left|\tilde{u}_{j}\right|+\sup _{B_{R_{j}}(0)}\left|\nabla \tilde{u}_{j}\right| \leqslant C^{\prime}$$
for some $C^{\prime}>0$, where here the gradient is the Euclidean gradient. Moreover,
$$\left|\nabla \tilde{u}_{j}(0)\right|=R_{j}^{-1}\left|\nabla u_{j}\right|_{\omega}\left(x_{j}\right)=1 .$$
According to Theorem 1.3, we also have that
$$\sup _{B_{R_{j}}(0)}\left|\sqrt{-1} \partial \bar{\partial} \tilde{u}_{j}\right|_{\beta} \leqslant C R_{j}^{-2} \sup _{M}\left|\partial \bar{\partial} u_{j}\right|_{\omega} \leqslant C^{\prime \prime} .$$
As the argument in [16,55], using the elliptic estimates for $\Delta$ and the Sobolev embedding that for each given $K \subset \mathbb{C}^{n}$ compact, each $0<\alpha<1$ and $p>1$, there exists a constant $C$ such that
$$\left\|\tilde{u}_{j}\right\|_{C^{1, \alpha}(K)}+\left\|\tilde{u}_{j}\right\|_{W^{2, p}(K)} \leqslant C .$$
Therefore, a subsequence of $\tilde{u}_{j}$ converges uniformly in $C_{\text {loc }}^{1, \alpha}\left(\mathbb{C}^{n}\right)$ as well as weakly in $W_{\text {loc }}^{2, p}\left(\mathbb{C}^{n}\right)$ to a function
$$v: \mathbb{C}^{n} \rightarrow \mathbb{R} .$$
By the construction we have global bounds $\sup _{\mathbb{C}^{n}}(|v|+|\nabla v|) \leqslant C$ and $|\nabla v(0)|=1$. In particular, $v$ is not constant.

The rest of proof is to show that $v$ is a $\stackrel{\circ}{\Gamma}_{\mathcal{G}}^{f}$-solution in the sense of [52, Definition 15]. Here $\Gamma_{\mathcal{G}}^{f}$ is the cone defined in (1.10). To do this, suppose first that we have a $C^{2}$-function $\phi$, such that $\phi \geqslant v$, and $\phi\left(z_{0}\right)=v\left(z_{0}\right)$ for some point $z_{0}$. We need to show that $\lambda\left[\phi_{p \bar{q}}\left(z_{0}\right)\right] \in \bar{\Gamma}_{\mathcal{G}}^{f}$. By the construction of $v$, similar to [52] for any $\epsilon>0$ we can find a $\tilde{u}_{j}$ as above, corresponding to a sufficiently large $j$, a number $c$ with $|c|<\epsilon$, and a point $z_{0}^{\prime}$ with $\left|z_{0}^{\prime}-z_{0}\right|<\epsilon$, so that
$$\phi+\epsilon\left|z-z_{0}\right|^{2}+c \geqslant \tilde{u}_{j} \text { on } B_{1}\left(z_{0}\right)$$
with equality at $z_{0}^{\prime}$. Therefore,
$$\phi_{p \bar{q}}\left(z_{0}^{\prime}\right)+\epsilon \delta_{p q} \geqslant \tilde{u}_{j, p \bar{q}}\left(z_{0}^{\prime}\right) .$$
Furthermore, note that for $j \gg 1$ (and so $R_{j}$ ) we have by (5.5) that
$$\lambda\left[\tilde{u}_{j, p \bar{q}}\left(z_{0}^{\prime}\right)\right]+\epsilon \overrightarrow{\mathbf{1}}-\lambda\left[\beta_{j}^{-1}\left(\chi_{j}+\sqrt{-1} \partial \bar{\partial} \tilde{u}_{j}\right)\left(z_{0}^{\prime}\right)\right] \in \Gamma_{n} .$$
Set $\tilde{\varepsilon}=\sup _{z \in B_{\epsilon}\left(z_{0}\right)}\left|\phi_{p \bar{q}}(z)-\phi_{p \bar{q}}\left(z_{0}\right)\right|$. Then
$$\phi_{p \bar{q}}\left(z_{0}^{\prime}\right) \leqslant \phi_{p \bar{q}}\left(z_{0}\right)+\tilde{\varepsilon} \delta_{p q} .$$

Combining (5.13), (5.11), (5.12) and (5.4), we have
$$f\left(R_{j}^{2}\left[\lambda\left[\phi_{p \bar{q}}\left(z_{0}\right)\right]+(2 \epsilon+\tilde{\varepsilon}) \overrightarrow{\mathbf{1}}\right]\right) \geqslant \tilde{\psi}_{j}\left(z_{0}^{\prime}\right) .$$

Together with the choice of $R_{j}, \phi, \tilde{\psi}_{j}, \epsilon, \tilde{\varepsilon}$, and the definition of $\Gamma_{\mathcal{G}}^{f}$, we infer that
$$\lambda\left[\phi_{p \bar{q}}\left(z_{0}\right)\right]+(2 \epsilon+\tilde{\varepsilon}) \overrightarrow{\mathbf{1}} \in \Gamma_{\mathcal{G}}^{f} .$$
Let $\epsilon \rightarrow 0$, we get $\tilde{\varepsilon} \rightarrow 0$, and also $\lambda\left[\phi_{p \bar{q}}\left(z_{0}\right)\right] \in \bar{\Gamma}_{\mathcal{G}}^{f}$. We remark that this conclusion is not that obvious, which is in contrast with the case $\Gamma_{\mathcal{G}}^{f}=\Gamma$.

Suppose now that we have a $C^{2}$-function $\phi$, such that $\phi \leqslant v$, and $\phi\left(z_{0}\right)=v\left(z_{0}\right)$ for some point $z_{0}$. It requires to show that $\lambda\left[\phi_{p \bar{q}}\left(z_{0}\right)\right] \in \mathbb{R}^{n} \backslash \stackrel{\circ}{\Gamma}_{\mathcal{G}}^{f}$. As above, for any $\epsilon$ we can find a $\tilde{u}_{j}$ corresponding to large $j$, and $c, z_{0}^{\prime}$ with $\left|z_{0}^{\prime}-z_{0}\right|<\epsilon$, so that
$$\phi-\epsilon\left|z-z_{0}\right|^{2}+c \leqslant \tilde{u}_{j} \text { on } B_{1}\left(z_{0}\right)$$
with equality at $z_{0}^{\prime}$. This implies that
$$\phi_{p \bar{q}}\left(z_{0}^{\prime}\right)-\epsilon \delta_{p q} \leqslant \tilde{u}_{j, p \bar{q}}\left(z_{0}^{\prime}\right) .$$
Suppose by contradiction that
$$\lambda\left(\phi_{p \bar{q}}\left(z_{0}^{\prime}\right)-3 \epsilon \delta_{p \bar{q}}\right) \in \stackrel{\circ}{\Gamma}_{\mathcal{G}}^{f} \text {, i.e., } \lambda\left(\phi_{p \bar{q}}\left(z_{0}^{\prime}\right)\right) \in \stackrel{\circ}{\Gamma}_{\mathcal{G}}^{f}+3 \epsilon \overrightarrow{\mathbf{1}} .$$
Then $\lambda\left[\tilde{u}_{j, p \bar{q}}\left(z_{0}^{\prime}\right)\right] \in \stackrel{\circ}{\Gamma}_{\mathcal{G}}^{f}+2 \epsilon \overrightarrow{\mathbf{1}}$. By (5.5) and the openness of $\stackrel{\circ}{\Gamma}_{\mathcal{G}}^{f}$, if $j$ is sufficiently large (so does $R_{j}$ ), we have
$$\lambda\left[\beta_{j}^{-1}\left(\chi_{j}+\sqrt{-1} \partial \bar{\partial} \tilde{u}_{j}\right)\right]\left(z_{0}^{\prime}\right) \in \stackrel{\circ}{\Gamma}_{\mathcal{G}}^{f}+\epsilon \overrightarrow{\mathbf{1}} .$$
According to Lemma 3.7, we conclude that
$$f\left(R_{j}^{2} \lambda\left[\beta_{j}^{-1}\left(\chi_{j}+\sqrt{-1} \partial \bar{\partial} \tilde{u}_{j}\right)\right]\left(z_{0}^{\prime}\right)\right) \geqslant f\left(\epsilon R_{j}^{2} \overrightarrow{\mathbf{l}}\right) .$$
It contradicts to (5.4) when $R_{j}$ is sufficiently large. Thus
$$\lambda\left[\phi_{p \bar{q}}\left(z_{0}^{\prime}\right)-3 \epsilon \delta_{p q}\right] \in \mathbb{R}^{n} \backslash \stackrel{\circ}{\Gamma}_{\mathcal{G}}^{f} .$$
Let $\epsilon \rightarrow 0$, we will have $z_{0}^{\prime} \rightarrow z_{0}$, and so $\lambda\left[\phi_{p \bar{q}}\left(z_{0}\right)\right] \in \mathbb{R}^{n} \backslash \stackrel{\circ}{\Gamma}_{\mathcal{G}}^{f}$.
Therefore, $v$ is a $\stackrel{\circ}{\Gamma}_{\mathcal{G}}^{f}$-solution. From Lemma 3.6, $\stackrel{\circ}{\Gamma}_{\mathcal{G}}^{f}$ is an open symmetric convex cone, containing the positive cone $\Gamma_{n}$ and not equal to all of $\mathbb{R}^{n}$. According to Székelyhidi's Liouville type theorem [52, Theorem 20], $v$ is a constant. This is a contradiction. \(\square\)

Remark 5.2. The definition of $\Gamma_{\mathcal{G}}^{f}$ in (1.10) is important, since it can straightforwardly utilize (5.14).

\section*{6. Fully nonlinear elliptic equations with type 2 cone}

For the equation (1.1), we say that $\chi$ is quasi-admissible, if
$$\lambda\left(\omega^{-1} \chi\right) \in \bar{\Gamma} \text { in } M$$
and
$$\lambda\left(\omega^{-1} \chi\right)\left(p_{0}\right) \in \Gamma \text { for some } p_{0} \in M \text {. }$$

Throughout this section, we assume that $(M, \omega)$ is a connected closed Hermitian manifold, and $\chi$ is a smooth quasi-admissible real (1, 1)-form.

Proposition 6.1. Suppose $\Gamma$ is of type 2 in the sense of [7], i.e., $(0, \cdots, 0,1) \in \Gamma$. Then there exists a smooth admissible function $\underline{u}$, i.e., $\lambda\left[\omega^{-1}(\chi+\sqrt{-1} \partial \bar{\partial} \underline{u})\right] \in \Gamma$ in $M$.

Proof. We use an idea of [67], using some technique from Morse theory. By (6.2) and the openness of $\Gamma$,
$$\lambda\left(\omega^{-1} \chi\right) \in \Gamma \text { in } \overline{B_{r_{0}}\left(p_{0}\right)}$$
for some positive constant $r_{0}$. We take a smooth Morse function $w$ with critical set
$$C(w)=\left\{p_{1}, \cdots, p_{m}, p_{m+1} \cdots p_{m+k}\right\}$$
among which $p_{1}, \cdots, p_{m}$ are all the critical points being in $M \backslash \overline{B_{r_{0} / 2}\left(p_{0}\right)}$. Pick $q_{1}, \cdots, q_{m} \in B_{r_{0} / 2}\left(p_{0}\right)$ but not the critical point of $w$. By the homogeneity lemma (see e.g. [43]), one can find a diffeomorphism $h: M \rightarrow M$, which is smoothly isotopic to the identity, such that
\begin{itemize}
\item[-] $h\left(p_{i}\right)=q_{i}, 1 \leqslant i \leqslant m$.
\item[-] $h\left(p_{i}\right)=p_{i}, m+1 \leqslant i \leqslant m+k$.
\end{itemize}
Then we obtain a Morse function $v=w \circ h^{-1}$ with the critical set
$$C(v)=\left\{q_{1}, \cdots, q_{m}, p_{m+1} \cdots p_{m+k}\right\} \subset \overline{B_{r_{0} / 2}\left(p_{0}\right)} .$$

Next we complete the proof. Assume $v \leqslant-1$. Take $\underline{u}=e^{t v}$, then
$$\chi+\sqrt{-1} \partial \bar{\partial} \underline{u}=\chi+t e^{t v}(\sqrt{-1} \partial \bar{\partial} v+t \sqrt{-1} \partial v \wedge \bar{\partial} v) .$$
Notice that
$$\lambda\left[\omega^{-1}(\sqrt{-1} \partial v \wedge \bar{\partial} v)\right]=|\nabla v|^{2}(0, \cdots, 0,1) .$$
From (6.4) there is a positive constant $m_{0}$ such that $|\nabla v|^{2} \geqslant m_{0}$ in $M \backslash \overline{B_{r_{0}}\left(p_{0}\right)}$. By (6.1), (6.5), (6.6) and the openness of $\Gamma$, there exists $t \gg 1$ such that
$$\lambda\left[\omega^{-1}(\chi+\sqrt{-1} \partial \bar{\partial} \underline{u})\right] \in \Gamma \text { in } M \backslash \overline{B_{r_{0}}\left(p_{0}\right)},$$
and moreover by (6.3)
$$\lambda\left[\omega^{-1}\left(\chi+t e^{t v} \sqrt{-1} \partial \bar{\partial} v\right)\right] \text { in } \overline{B_{r_{0}}\left(p_{0}\right)} .$$
In conclusion, we know $\lambda\left[\omega^{-1}(\chi+\sqrt{-1} \partial \bar{\partial} \underline{u})\right] \in \Gamma$ in $M$. \(\square\)

Theorem 6.2. In addition to (1.4), $\sup _{\partial \Gamma} f=-\infty$ and $\sup _{\Gamma} f=+\infty$, we assume $(0, \cdots, 0,1) \in \stackrel{\circ}{\Gamma}_{\mathcal{G}}^{f}$. Then for any $\psi \in C^{\infty}(M)$, there exists a constant $c$ and a smooth admissible function $u$ with $\sup _{M} u=0$ such that
$$f\left(\lambda\left[\omega^{-1}(\chi+\sqrt{-1} \partial \bar{\partial} u)\right]\right)=\psi+c .$$
Proof. By Proposition 6.1, we have a smooth admissible function $\underline{u}$. According to Lemma 3.7, (1.8) automatically holds if $(0, \cdots, 0,1) \in \stackrel{\circ}{\Gamma}_{\mathcal{G}}^{f}$ and $\sup _{\Gamma} f=+\infty$. \(\square\)

\section*{7. Quantitative boundary estimate: Set-up}

Denote $\sigma(z)$ the distance from $z$ to $\partial M$ with respect to $\omega$. Let
$$M_{\delta} \equiv\{z \in M: \sigma(z)<\delta\} .$$
Given a boundary point $z_{0} \in \partial M$. We choose local complex coordinates with origin at $z_{0}$
$$\left(z^{1}, \cdots, z^{n}\right), z^{i}=x^{i}+\sqrt{-1} y^{i}$$
in a neighborhood which we assume to be contained in $M_{\delta}$, such that at the origin $z_{0}(z=0), g_{i \bar{j}}(0)=\delta_{i j}, \frac{\partial}{\partial x^{n}}$ is the interior normal to $\partial M$. (Here and in what follows we identify the boundary point $z_{0}$ with $z=0$ ). For convenience we set
$$t^{2 \alpha-1}=x^{\alpha}, t^{2 \alpha}=y^{\alpha}, 1 \leqslant \alpha \leqslant n-1 ; t^{2 n-1}=y^{n}, t^{2 n}=x^{n} .$$
In the computation, we use the notation in (2.1). Also we denote
$$\Omega_{\delta} \equiv\{z \in M:|z|<\delta\} .$$
Throughout this section and Section 8, the Greek letters $\alpha, \beta$ run from 1 to $n-1$.
Since $u-\varphi=0$ on $\partial M$, we can derive
$$\left|u_{t^{k} t^{\prime}}\left(z_{0}\right)\right| \leqslant C \text { for } k, l<2 n,$$
where $C$ depends on $\sup _{\partial M}|\nabla(u-\varphi)|$ and geometric quantities of $\partial M$.
To show Theorem 1.7, it suffices to prove the following two propositions:
Proposition 7.1. Suppose $f$ satisfies (1.4), (1.5) and (1.8). Assume that Dirichlet problem (1.7) admits a $C^{2}$ admissible subsolution $\underline{u}$. Let $u \in C^{2}(\bar{M})$ be an admissible solution to the Dirichlet problem, then
$$g_{n \bar{n}}\left(z_{0}\right) \leqslant C\left(1+\sum_{\alpha=1}^{n-1}\left|g_{\alpha \bar{n}}\left(z_{0}\right)\right|^{2}\right), \forall z_{0} \in \partial M .$$
Here the constant $C$ depends on $\left(\delta_{\psi, f}\right)^{-1}, \sup _{M} \psi,|u|_{C^{0}(\bar{M})},|\nabla u|_{C^{0}(\partial M)},|\underline{u}|_{C^{2}(\bar{M})}, \partial M$ up to third order derivatives and other known data (but not on $\sup _{M}|\nabla u|$ ).