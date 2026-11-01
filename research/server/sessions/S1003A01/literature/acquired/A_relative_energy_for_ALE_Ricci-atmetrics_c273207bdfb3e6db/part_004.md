---
retention_scope: session
part: 4
total_parts: 4
---

[Part 4/4 of: A relative energy for ALE Ricci-atmetrics]

We state the following linear version of Proposition B. 2 whose proof is along the same lines of that of Proposition B.2:

Proposition B.6. Let $\left(N^{n}, g_{b}\right)$ be a non-flat Ricci-flat manifold asymptotic to a smooth Ricciflat cone $\left(C\left(S^{n-1}\right), g_{S}\right)$. Let $\beta \in(1, n-1)$ and $\alpha \in(0,1)$. Then the following decomposition holds true:
$$C_{\beta}^{2, \alpha}\left(S^{2} T^{*} N\right)=\left.\operatorname{ker}_{C_{\beta}^{2, \alpha}} \operatorname{div}_{g_{b}} \oplus \operatorname{imdiv}_{g_{b}}^{*}\right|_{C_{\beta-1}^{3, \alpha}} .$$
Equivalently, for any symmetric 2-tensor $h$ in $C_{\beta}^{2, \alpha}$, there exist a unique divergence-free symmetric 2-tensor $h^{\prime}$ in $C_{\beta}^{2, \alpha}$ and a unique vector field $X$ on $N$ in $C_{\beta-1}^{3, \alpha}$ such that $h=h^{\prime}+\mathscr{L}_{X}(g)$. Moreover this decomposition is $L^{2}$-orthogonal if $\beta>\frac{n}{2}$.
B.1. Invertibility of the linearization. Our approach based on the implicit function theorem starts with the study of
$$\operatorname{div}_{g_{b}} \mathscr{L}_{X}\left(g_{b}\right)=-\operatorname{div}_{g_{b}} h,$$
where $X$ is a vector field, and $h$ is a symmetric 2-tensor. Notice that equation (B.3) is the linearization of equation (B.1). The operator □ , defined as
$$\square_{g_{b}}(X):=\operatorname{div}_{g_{b}} \mathscr{L}_{X}\left(g_{b}\right)=\nabla^{g_{b}}\left(\operatorname{div}_{g_{b}} X\right)+\Delta_{g_{b}} X,$$
is elliptic and self-adjoint.
Let us discuss about the kernel of □ on a Ricci-flat cone.
Let $n \geq 4$, and $\left(C(S), g_{C(S)}\right):=\left(\mathbb{R}_{+} \times S, d r^{2}+r^{2} g_{S}\right)$ be an $n$-dimensional Ricci-flat cone with smooth link $\left(S, g_{S}\right)$, satisfying $\operatorname{Ric}\left(g_{S}\right)=(n-2) g_{S}$. Let us follow [CT94, Section 2], and [AV12, Section 4.1] and consider the operator as acting on 1-forms rather than on vector fields on $C(S)$. By harmonic decomposition, any such vector field can be decomposed as an infinite sum of terms of the following types :
\begin{itemize}
\item[(1)] $p(r) \psi$, where the 1-form $\psi$ satisfies $d_{S}^{*} \psi=0$, and $d_{S}^{*} d_{S} \psi=\mu \psi$,
\item[(2)] $r^{-1} l(r) \phi d r+u(r) r d_{S} \phi$, where the function $\phi$ satisfies $d_{S}^{*} \phi=0$, et $d_{S}^{*} d_{S} \phi=\lambda \phi$.
\end{itemize}
Moreover, the operator □ preserves these two types of 1-forms.
For $\lambda$ and $\mu$ eigenvalues of $d_{S}^{*} d_{S}+d_{S} d_{S}^{*}$ on functions and 1-forms respectively, we set
$$a_{\mu}^{ \pm}:=\frac{4-n}{2} \pm \sqrt{\frac{(4-n)^{2}}{4}+\mu},$$
and
$$b_{\lambda}^{ \pm}:=\frac{2-n}{2} \pm \sqrt{\frac{(2-n)^{2}}{4}+\lambda} .$$

Remark B.7. In dimension $n=4$, we get
$$a_{\mu}^{ \pm}:= \pm \sqrt{\mu},$$
and
$$b_{\lambda}^{ \pm}:=-1 \pm \sqrt{1+\lambda} .$$

Every 1-form in the kernel of □ on $C(S)$ is a sum of the following types of homogeneous 1-forms :
\begin{itemize}
\item[(1)] $r^{a_{\mu}^{ \pm}} \psi$,
\end{itemize}
\begin{itemize}
\item[(2)]
$$\begin{aligned}
& \bullet r_{\lambda}^{ \pm} d_{S} \phi+b_{\lambda}^{ \pm} r_{\lambda}^{ \pm}-1 \phi d r \text {, } \\
& \text { - } 2 r^{b_{\lambda}^{ \pm}+2} d_{S} \phi+b_{\lambda}^{\mp} r_{\lambda}^{ \pm}+1 \phi d r \text {. }
\end{aligned}$$
\end{itemize}
We call exceptional values for □ the possible homogeneity rates, that is $a_{\mu}^{ \pm}-1, b_{\lambda}^{ \pm}-1$ or $b_{\lambda}^{ \pm}+1$ corresponding to eigenvalues of the Hodge Laplacian on functions or 1-forms. We will need to estimate these exceptional values to use analysis in weighted Hölder spaces.

Remark B.8. For $\left(S, g_{S}\right)=\left(\mathbb{S}^{n-1}, g_{\mathbb{S}^{n-1}}\right)$, we have the following values for the first exceptional values associated to the $j$-th eigenvalues of the Hodge Laplacian on functions and 1-forms respectively $\lambda_{j}\left(g_{\mathbb{S}^{n-1}}\right)$ and $\mu_{j}\left(g_{\mathbb{S}^{n-1}}\right)$.
\begin{itemize}
\item[(1)] $a_{\mu_{j}\left(g_{\mathbb{S}^{n-1}}\right)}^{+}-1=j, j \in \mathbb{N}^{*}$,
\item[(2)] $a_{\mu_{j}\left(g_{\mathbb{S}^{n-1}}\right)}^{-}-1=-(n-2)-j, j \in \mathbb{N}^{*}$,
\item[(3)] $b_{\lambda_{j}\left(g_{\mathbb{S}^{n-1}}\right)}^{+}+1=1+j, j \in \mathbb{N}$,
\item[(4)] $b_{\lambda_{j}\left(g_{\mathbb{S}^{n-1}}\right)}^{-}+1=-(n-3)-j, j \in \mathbb{N}$,
\item[(5)] $b_{\lambda_{j}\left(g_{\mathbb{S}^{n-1}}\right)}^{+}-1=-1+j, j \in \mathbb{N}$,
\item[(6)] $b_{\lambda_{j}\left(g_{\mathbb{S}^{n-1}}\right)}^{-}-1=-(n-1)-j, j \in \mathbb{N}$.
\end{itemize}

More generally, let us discuss the eigenvalues of Einstein manifolds with positive scalar curvature.

For Einstein manifolds with positive scalar curvature, the celebrated Lichnerowicz-Obata theorem provides a lower bound for the first eigenvalue of the Hodge Laplacian on functions and 1-forms as well as a rigidity statement. See [GM75] for an exposition as well as a similar result for $p$-forms. The result is a consequence of Bochner formulas (and Weitzenbock formulas for $p$-forms).

Lemma B. 9 (Lower bounds on the first eigenvalues). If a Riemannian manifold $\left(M^{n}, g\right)$ satisfies the lower bound $\operatorname{Ric}(g) \geq(n-1) g$, then, $\lambda_{1}(g)$ and $\mu_{1}(g)$, which are respectively the first eigenvalue of the Hodge laplacian on functions, and on 1-forms satisfy
$$\lambda_{1}(g) \geq \lambda_{1}\left(g_{\mathbb{S}^{n}}\right),$$
with equality if and only if $(M, g)=\left(\mathbb{S}^{n}, g_{\mathbb{S}^{n}}\right)$, and
$$\mu_{1}(g) \geq \mu_{1}\left(g_{\mathbb{S}^{n}}\right),$$
with equality if and only if $(M, g)=\left(\mathbb{S}^{n}, g_{\mathbb{S}^{n}}\right)$.
We therefore get an a priori bound on the eigenvalues of Einstein manifolds with positive scalar curvature which translates directly to a control for the exceptional values of our operator
□ .

Proposition B.10. Let $\left(S^{n-1}, g_{S}\right)$ satisfy $\operatorname{Ric}\left(g_{S}\right)=(n-2) g_{S}$ but $\left(S^{n-1}, g_{S}\right) \neq\left(\mathbb{S}^{n-1}, g_{\mathbb{S}^{n-1}}\right)$, then there is no exceptional value in $[-(n-2), 0]$.

Moreover, if the following inequality holds
$$\lambda_{1}\left(g_{S}\right) \geq \lambda_{2}\left(g_{\mathbb{S}^{n-1}}\right),$$
where $\lambda_{i}$ is the $i$-th eigenvalue (without multiplicity) of the Hodge Laplacian on functions. Then, on the Ricci-flat cone $\left(C(S), g_{C(S)}\right)$ with link $\left(S, g_{S}\right)$, there is no exceptional value for
the operator □ in $(-(n-1), 1)$. This is in particular the case for cones over nontrivial quotients of the sphere in all dimensions.

Remark B.11. For $\left(\mathbb{S}^{n-1}, g_{\mathbb{S}^{n-1}}\right)$, there is no exceptional values in $(-(n-2), 0)$.
Proof. By the description of the kernel of □ on $C(S)$ at the beginning of Section B.1, we know that the exceptional values are of one of the forms $a_{\mu}^{ \pm}-1, b_{\lambda}^{ \pm}-1, b_{\lambda}^{ \pm}+1$. For the sphere, the exceptional values corresponding to the lowest eigenvalues are detailed in Remark B.8. Assuming that $\lambda_{1}\left(g_{S}\right) \geq \lambda_{2}\left(g_{\mathbb{S}^{n-1}}\right)$, we see from the expressions (B.5) and (B.6) that the only possible exceptional values in $(-(n-1), 1)$ are $b_{\lambda_{0}\left(g_{S}\right)}^{+}-1=-1$ and $b_{\lambda_{0}\left(g_{S}\right)}^{-}+1=-(n-3)$, but as noted in [Ozu19, Lemma 3.2], coming back to the expressions of the associated 1-forms, we find that they vanish.

If we do not have the bound $\lambda_{1}\left(g_{S}\right) \geq \lambda_{2}\left(g_{\mathbb{S}^{n-1}}\right)$, we still have the estimates of Lemma B. 9 which plugged in the expressions (B.5) and (B.6) imply that there are exceptional values in $(0,1]$ and $[-(n-1),-(n-2))$, but none in [ $-(n-2), 0$ ]

In dimension 3, all Einstein manifolds with positive scalar curvature are of the form $\mathbb{S}^{3} / \Gamma$, where $\Gamma$ is a finite subgroup of $S O(4)$ acting freely on the sphere. If $\Gamma \neq\{e\}$, then the eigenfunctions and 1-forms of $\mathbb{S}^{3} / \Gamma$ are the projection of the eigenfunctions and 1-forms of $\mathbb{S}^{3}$ which are $\Gamma$-invariant. It turns out that the first eigenvalue on functions and 1-forms of $\mathbb{S}^{3}$ are respectively associated to restrictions of non-zero linear functions and constant vector fields on $\mathbb{R}^{4}$, but since none of these are $\Gamma$-invariant if $\Gamma \neq\{e\}$. This implies the bound $\lambda_{1}\left(g_{S}\right) \geq \lambda_{2}\left(g_{\mathbb{S}^{n-1}}\right)$.

The same argument works for $\mathbb{S}^{n-1} / \Gamma$ for $\Gamma \subset S O(n)$, a finite subgroup acting freely on the sphere. In this case, the first exceptional value below 1 is $-(n-1)$. \(\square\)

We can now conclude that our operator is invertible in suitable Hölder spaces.
Proposition B.12. Let $k \in \mathbb{N}^{*}, \alpha \in(0,1)$, and $\left(N^{n}, g_{b}\right)$ be a Ricci-flat manifold asymptotic to a non-flat Ricci-flat cone $\left(C(S), g_{C(S)}\right)$. Then, for all $1<\beta \leq n-1$, the operator □ : $C_{\beta-1}^{k+2, \alpha}(T N) \rightarrow C_{\beta+1}^{k, \alpha}(T N)$ is surjective.

It is moreover bijective for $1<\beta<n$ if we assume that the link satisfies
$$\lambda_{1}\left(g_{S}\right) \geq \lambda_{2}\left(g_{\mathbb{S}^{n-1}}\right) .$$

Remark B.13. For $\mathbb{R}^{n}$, the results holds for $1<\beta<n-1$.
Proof. Consider the operator $\square: C_{\beta-1}^{k+2, \alpha}(T N) \rightarrow C_{\beta+1}^{k, \alpha}(T N)$. By the theory of weighted Hölder spaces, for $\beta$ nonexceptional, the cokernel of the self-adjoint operator $\square: C_{\beta-1}^{k+2, \alpha}(T N) \rightarrow$ $C_{\beta+1}^{k, \alpha}(T N)$ is the kernel of □ on $C_{n-1-\beta}^{k, \alpha}(T N)$ (see Note 5.3). Let $Y \in C_{n-1-\beta}^{k, \alpha}(T N)$, and assume that $\square Y=0$. We can consider the following integration by parts
$$\begin{aligned}
0 & =\int_{N}\langle\square Y, Y\rangle_{g_{b}} d \mu_{g_{b}} \\
& =\int_{N}\left|\mathscr{L}_{Y} g_{b}\right|_{g_{b}}^{2} d \mu_{g_{b}}+\lim _{R \rightarrow \infty} \int_{\left\{\rho_{g_{b}}=R\right\}}\left(\mathscr{L}_{Y} g_{b}\right)(\nu, Y) d \sigma_{g_{b}},
\end{aligned}$$
where $\nu$ is the outward unit normal to the hypersurface $\left\{\rho_{g_{b}}=R\right\}$ and where $d \sigma_{g_{b}}$ is the $(n-1)$-dimensional Hausdorff measure on $\left\{\rho_{g_{b}}=R\right\}$ induced by $d \mu_{g_{b}}$. Since we assumed
that $Y \in C_{n-1-\beta}^{k, \alpha}(T N)$, we have $\left|\mathscr{L}_{Y} g_{b}\right|_{g_{b}}=O\left(\rho^{-n+\beta}\right)$ and $|Y|_{g_{b}}=O\left(\rho^{-n+1+\beta}\right)$ therefore, the boundary term vanishes for $-n+2 \beta<0$, that is $\beta<\frac{n}{2}$. This implies that for $\beta<\frac{n}{2}$, we actually have $\mathscr{L}_{Y} g_{b}=0$ and $Y$ is a Killing vector field. By the formula $\square=\frac{1}{2}\left(\nabla^{*} \nabla-\operatorname{Ric}\left(g_{b}\right)\right)$, we have $\nabla^{*} \nabla Y=0$, since $\operatorname{Ric}\left(g_{b}\right)=0$ and by integrating by parts again, we have
$$0=\int_{N}\left\langle\nabla^{*} \nabla Y, Y\right\rangle_{g_{b}} d \mu_{g_{b}}=\int_{N}\left|\nabla^{g_{b}} Y\right|_{g_{b}}^{2} d \mu_{g_{b}}$$
since the boundary terms vanish because of our decay assumption.
Consequently, $\nabla^{g_{b}} Y=0$, hence $Y=0$ because of the decay at infinity. The operator $\square: C_{\beta-1}^{k+2, \alpha} \rightarrow C_{\beta+1}^{k, \alpha}$ is therefore surjective for $0<\beta<\frac{n}{2}$, and since the kernel and cokernel are constant between exceptional values, that is for $\beta-1 \in(0, n-2]$ (and even $\beta-1 \in(-1, n-1)$ if $\lambda_{1}\left(g_{S}\right) \geq \lambda_{2}\left(g_{\mathbb{S}^{n-1}}\right)$ ), the operator is surjective for $0<\beta \leq n-1$ (and $0<\beta<n$ if $\left.\lambda_{1}\left(g_{S}\right) \geq \lambda_{2}\left(g_{\mathbb{S}^{n-1}}\right)\right)$.

Let us now prove that it is moreover injective under the assumption $\lambda_{1}\left(g_{S}\right) \geq \lambda_{2}\left(g_{\mathbb{S}^{n-1}}\right)$. Consider $X \in C_{\beta-1}^{k+2, \alpha}(T N)$ satisfying $\square X=0$. Since there is no exceptional value between $-(n-1)$ and 1 by Proposition B.10, $X$ actually lies in $C_{n-1}^{k+2, \alpha}(T N)$ and,
$$0=\int_{N}\langle\square X, X\rangle_{g_{b}} d \mu_{g_{b}}=\int_{N}\left|\mathscr{L}_{X} g_{b}\right|_{g_{b}}^{2} d \mu_{g_{b}}+\lim _{R \rightarrow \infty} \int_{\left\{\rho_{g_{b}}=R\right\}}\left(\mathscr{L}_{X} g_{b}\right)(\nu, X) d \sigma_{g_{b}}$$
where $\nu$ is the outward unit normal to the hypersurface $\left\{\rho_{g_{b}}=R\right\}$. Since we assumed that $X \in C_{n-1}^{k, \alpha}(T N)$, we have $\left|\mathscr{L}_{X} g_{b}\right|_{g_{b}}=O\left(\rho_{g_{b}}^{-n}\right)$ and $|X|_{g_{b}}=O\left(\rho_{g_{b}}^{-(n-1)}\right)$. Therefore, the boundary term vanishes, and by the same argument as above, $X=0$. \(\square\)
B.2. A divergence-free gauge. We can now apply the implicit function theorem to solve our gauging problem.

Proof of Proposition B.2. Let $\left(N^{n}, g_{b}\right)$ be a Ricci-flat manifold asymptotic to a smooth Ricciflat cone $\left(C\left(S^{n-1}\right), g_{S}\right)$, and denote by $\mathcal{S}_{b}$ a complement of the kernel of □ in $C_{\beta-1}^{k+2, \alpha}(T N)$ $\left(\mathcal{S}_{b}=C_{\beta-1}^{k+2, \alpha}(T N)\right.$ if we have the bound $\left.\lambda_{1}\left(g_{S}\right) \geq \lambda_{2}\left(g_{\mathbb{S}^{n-1}}\right)\right)$.

Let us define $\Phi: \mathcal{U}_{\beta}^{k+1, \alpha}\left(g_{b}, \varepsilon\right) \times C_{\beta-1}^{k+2, \alpha}(T N) \cap \mathcal{S}_{b} \rightarrow C_{\beta+1}^{k, \alpha}(T N)$ for a metric $g$ and vector field $X$,
$$\Phi(g, X):=\operatorname{div}_{\left(\exp _{X}^{g_{b}}\right)_{*} g_{b}} g .$$
The conclusion of our proposition is that for any $g$, there exists $X(g)$ such that $\Phi(g, X(g))=0$ and $g \mapsto X(g)$ is analytic. Indeed, for any diffeomorphism $\phi: N \rightarrow N, \phi_{*}\left(\operatorname{div}_{g} \phi^{*} g\right)=$ $\operatorname{div}_{\phi_{*} g} g$.

We want to apply the implicit function theorem, Lemma A. 2 to $\Phi$. Let us first note that by Lemma A.3, which is a local result, $\Phi$ is analytic for $k$ larger than or equal to 1 . We have $\Phi\left(g_{b}, 0\right)=0$, and $d_{\left(g_{b}, 0\right)} \Phi(0, \cdot)=\square$ is an isomorphism by Proposition B. 12 (once restricted to the orthogonal of its kernel). The Proposition follows by the implicit function Theorem, Lemma A.2. \(\square\)

\section*{Appendix C. First and second variations of geometric quantities}

In this appendix, we collect first and second derivatives of various geometric quantities. We start with a qualitative formula for the linearization of the Ricci curvature with respect to a background metric:

Lemma C.1. Let $\left(N^{n}, g_{1}\right)$ be a Riemannian manifold. Let $g_{2}$ be a second Riemannian metric on $N$ uniformly equivalent to $g_{1}$, i.e. $C^{-1} \leq g_{2} \leq C g_{1}$ for some positive constant $C$. Then, if $h:=g_{2}-g_{1}$ and if $g_{t}:=g_{1}+(t-1) h, t \in[1,2]$,
$$-2 \operatorname{Ric}\left(g_{t}\right)=-2 \operatorname{Ric}\left(g_{1}\right)+g_{t}^{-1} * \nabla^{g_{1}, 2} g_{t}+g_{t}^{-1} * h * \operatorname{Rm}\left(g_{1}\right)+g_{t}^{-1} * g_{t}^{-1} * \nabla^{g_{1}} g_{t} * \nabla^{g_{1}} g_{t}-\mathscr{L}_{B}\left(g_{t}\right),$$
where $B$ is a vector field on $N$ defined as follows:
$$\begin{aligned}
B=B\left(g_{t}, \nabla^{g_{1}}, g_{t}\right) & :=\frac{1}{2} g_{t}^{k l}\left(\nabla_{k}^{g_{1}}\left(g_{t}\right)_{i l}+\nabla_{l}^{g_{1}}\left(g_{t}\right)_{i k}-\nabla^{g_{1}}\left(g_{t}\right)_{k l}\right) \\
& =\operatorname{div}_{g_{1}}\left(g_{t}-g_{1}\right)-\frac{1}{2} \nabla^{g_{1}} \operatorname{tr}_{g_{1}}\left(g_{t}-g_{1}\right)+g_{t}^{-1} *\left(g_{t}-g_{1}\right) * \nabla^{g_{1}} g_{t}
\end{aligned}$$
Moreover,
$$\begin{aligned}
&\left|\frac{\partial}{\partial t} \operatorname{Ric}\left(g_{t}\right)\right|_{g_{1}} \lesssim\left(1+|h|_{g_{1}}\right)\left|\nabla^{g_{1}, 2} h\right|_{g_{1}}+\left|\operatorname{Rm}\left(g_{1}\right)\right|_{g_{1}}|h|_{g_{1}}+\left(1+|h|_{g_{1}}\right)\left|\nabla^{g_{1}} h\right|_{g_{1}}^{2}, \\
&\left|\frac{\partial^{2}}{\partial t^{2}} \operatorname{Ric}\left(g_{t}\right)\right|_{g_{1}} \lesssim|h|_{g_{1}}\left|\nabla^{g_{1}, 2} h\right|_{g_{1}}+\left|\operatorname{Rm}\left(g_{1}\right)\right|_{g_{1}}|h|_{g_{1}}^{2}+|h|_{g_{1}}\left|\nabla^{g_{1}} h\right|_{g_{1}}^{2},
\end{aligned}$$
where the sign $\lesssim$ means less than or equal up to a positive constant that is uniform in $t \in[1,2]$.
Proof. For a proof of (C.1) and (C.2), see for instance [Lemma 2.1, Chapter 2, [Shi89]]. To get (C.3) and (C.4) respectively, it suffices to differentiate (C.1) and (C.2) once and twice respectively. \(\square\)

Now, we recall the variations of the Ricci and scalar curvatures:
Lemma C.2. Let $\left(N^{n}, g\right)$ be a Riemannian manifold. Let $h$ be a smooth symmetric 2-tensor on $N$. Then,
$$\begin{aligned}
\delta_{g}(-2 \operatorname{Ric})(h) & =\Delta_{g} h+2 \operatorname{Rm}(g)(h)-\operatorname{Ric}(g) \circ h-h \circ \operatorname{Ric}(g)-\mathscr{L}_{B_{g}(h)} \\
& =L_{g} h-\mathscr{L}_{B_{g}(h),}
\end{aligned}$$
where $L_{g}$ denotes the Lichnerowicz operator as defined in introduced in Definition 2.6 and where $B_{g}(h)$ denotes the linearized Bianchi gauge defined by:
$$B_{g}(h):=\operatorname{div}_{g} h-\frac{1}{2} \nabla^{g} \operatorname{tr}_{g} h .$$
In particular, the first variation of the scalar curvature along a variation $h \in S^{2} T^{*} N$ is:
$$\delta_{g} \mathrm{R}(h)=\operatorname{div}_{g} \operatorname{div}_{g} h-\Delta_{g} \operatorname{tr}_{g} h-\langle h, \operatorname{Ric}(g)\rangle_{g} .$$

A proof of this lemma can be found for instance in [CLN06, Chapter 2].
We recall the following qualitative estimates whose proofs are essentially based on the definition of the Hessian of a function on a Riemannian manifold:

Lemma C.3. Let $\left(N^{n}, g_{1}\right)$ be a Riemannian manifold. Let $g_{2}$ be a second Riemannian metric on $N$ uniformly equivalent to $g_{1}$, i.e. $C^{-1} \leq g_{2} \leq C g_{1}$ for some positive constant $C$. Denote $g_{t}:=g_{1}+(t-1) g_{2}, t \in[1,2]$ and assume there exists a one-parameter family $\left(f_{g_{t}}\right)_{t \in[1,2]}$ of smooth functions on $N$ that varies smoothly in $t$. Then,
$$\frac{\partial}{\partial t} \nabla^{g_{t}, 2} f_{g_{t}}=\nabla^{g_{t}, 2}\left(\delta_{g_{t}} f(h)\right)+\frac{1}{2} \mathscr{L}_{\nabla^{g_{t}} f_{g_{t}}}(h)-\frac{1}{2} \mathscr{L}_{h\left(\nabla^{g_{t}} f_{g_{t}}\right)}\left(g_{t}\right),$$
and,
$$\begin{aligned}
\frac{\partial^{2}}{\partial t^{2}} \nabla^{g_{t}, 2} f_{g_{t}} & =\nabla^{g_{t}, 2}\left(\delta_{g_{t}}^{2} f(h, h)\right)+g_{t}^{-1} * \nabla^{g_{t}} h * \nabla^{g_{t}}\left(\delta_{g_{t}} f(h)\right) \\
& +g_{t}^{-1} * g_{t}^{-1} * \nabla^{g_{t}} h * \nabla^{g_{t}} h * \nabla^{g_{t}} f_{g_{t}}+g_{t}^{-1} * g_{t}^{-1} * h * \nabla^{g_{t}} h * \nabla^{g_{t}} f_{g_{g_{t}}} .
\end{aligned}$$

\section*{References}
[And90] Michael T. Anderson. Convergence and rigidity of manifolds under ricci curvature bounds. Inventiones mathematicae, 102(1):429-445, Dec 1990.
[App18] Alexander Appleton. Scalar curvature rigidity and Ricci DeTurck flow on perturbations of Euclidean space. Calc. Var. Partial Differential Equations, 57(5):Art. 132, 23, 2018.
[App19] Alexander Appleton. Eguchi-hanson singularities in u(2)-invariant ricci flow. 2019.
[AV12] Antonio G. Ache and Jeff A. Viaclovsky. Obstruction-flat asymptotically locally Euclidean metrics. Geom. Funct. Anal., 22(4):832-877, 2012.
[Bar86] Robert Bartnik. The mass of an asymptotically flat manifold. Comm. Pure Appl. Math., 39(5):661-693, 1986.
[BD20] Reto Buzano and Gianmichele Di Matteo. A Local Singularity Analysis for the Ricci Flow and its Applications to Ricci Flows with Bounded Scalar Curvature. arXiv e-prints, page arXiv:2006.16227, June 2020.
[Bes07] A.L. Besse. Einstein Manifolds. Classics in Mathematics. Springer Berlin Heidelberg, 2007.
[BKN89] Shigetoshi Bando, Atsushi Kasue, and Hiraku Nakajima. On a construction of coordinates at infinity on manifolds with fast curvature decay and maximal volume growth. Invent. Math., 97(2):313-349, 1989.
[BZ17] Richard H. Bamler and Qi S. Zhang. Heat kernel and curvature bounds in Ricci flows with bounded scalar curvature. Adv. Math., 319:396-450, 2017.
[CGH00] David M. J. Calderbank, Paul Gauduchon, and Marc Herzlich. Refined Kato inequalities and conformal weights in Riemannian geometry. J. Funct. Anal., 173(1):214-255, 2000.
[CLN06] Bennett Chow, Peng Lu, and Lei Ni. Hamilton's Ricci flow, volume 77 of Graduate Studies in Mathematics. American Mathematical Society, Providence, RI, 2006.
[CM14] Tobias Holck Colding and William P. Minicozzi, II. On uniqueness of tangent cones for Einstein manifolds. Invent. Math., 196(3):515-588, 2014.
[CM15] Tobias Holck Colding and William P. Minicozzi, II. Uniqueness of blowups and łojasiewicz inequalities. Ann. of Math. (2), 182(1):221-285, 2015.
[CT94] Jeff Cheeger and Gang Tian. On the cone structure at infinity of Ricci flat manifolds with Euclidean volume growth and quadratic curvature decay. Invent. Math., 118(3):493-571, 1994.
[CY75] S. Y. Cheng and S. T. Yau. Differential equations on Riemannian manifolds and their geometric applications. Comm. Pure Appl. Math., 28(3):333-354, 1975.
[Dev14] Baptiste Devyver. A Gaussian estimate for the heat kernel on differential forms and application to the Riesz transform. Math. Ann., 358(1-2):25-68, 2014.
[DK20] A. Deruelle and K. Kroencke. Stability of ALE Ricci-flat manifolds under Ricci flow. Journal of Geometric Analysis, pages 1-42, 2020.
[DM07] Xianzhe Dai and Li Ma. Mass under the Ricci flow. Comm. Math. Phys., 274(1):65-80, 2007.
[FIK03] Mikhail Feldman, Tom Ilmanen, and Dan Knopf. Rotationally symmetric shrinking and expanding gradient Kähler-Ricci solitons. J. Differential Geom., 65(2):169-209, 2003.
[GM75] S. Gallot and D. Meyer. Opérateur de courbure et laplacien des formes différentielles d'une variété riemannienne. J. Math. Pures Appl. (9), 54(3):259-284, 1975.
[Has11] Robert Haslhofer. A renormalized Perelman-functional and a lower bound for the ADM-mass. J. Geom. Phys., 61(11):2162-2167, 2011.
[Has12] Robert Haslhofer. Perelman's lambda-functional and the stability of Ricci-flat metrics. Calc. Var. Partial Differential Equations, 45(3-4):481-504, 2012.
[HHS14] Stuart Hall, Robert Haslhofer, and Michael Siepmann. The stability inequality for Ricci-flat cones. J. Geom. Anal., 24(1):472-494, 2014.
[HJ11] Alain Haraux and Mohamed Ali Jendoubi. The łojasiewicz gradient inequality in the infinite-dimensional Hilbert space framework. J. Funct. Anal., 260(9):2826-2842, 2011.
[HM14] Robert Haslhofer and Reto Müller. Dynamical stability and instability of Ricci-flat metrics. Math. Ann., 360(1-2):547-553, 2014.
[Joy00] Dominic D. Joyce. Compact manifolds with special holonomy. Oxford Mathematical Monographs. Oxford University Press, Oxford, 2000.
[Koi83] N. Koiso. Einstein metrics and complex structures. Invent. Math., 73(1):71-106, 1983.
[Kro89] P. B. Kronheimer. The construction of ALE spaces as hyper-Kähler quotients. J. Differential Geom., 29(3):665-683, 1989.
[Krö15] Klaus Kröncke. Stability and instability of Ricci solitons. Calc. Var. Partial Differential Equations, 53(1-2):265-287, 2015.
[LeB88] Claude LeBrun. Counter-examples to the generalized positive action conjecture. Comm. Math. Phys., 118(4):591-596, 1988.
[Li18] Yu Li. Ricci flow on asymptotically Euclidean manifolds. Geom. Topol., 22(3):1837-1891, 2018.
[Ło65] Stanisław Lojasiewicz. Ensembles semi-analytiques. I.H.E.S. Lecture notes, 1965.
[LP87] John M. Lee and Thomas H. Parker. The Yamabe problem. Bull. Amer. Math. Soc. (N.S.), 17(1):37-91, 1987.
[Min09] Vincent Minerbe. Weighted Sobolev inequalities and Ricci flat manifolds. Geom. Funct. Anal., 18(5):1696-1749, 2009.
[Nak90] Hiraku Nakajima. Self-duality of ALE Ricci-flat 4-manifolds and positive mass theorem. In Recent topics in differential and analytic geometry, volume 18 of Adv. Stud. Pure Math., pages 385-396. Academic Press, Boston, MA, 1990.
[Ozu19] Tristan Ozuch. Noncollapsed degeneration of einstein 4-manifolds ii, 2019.
[Pal68] Richard S. Palais. Foundations of global non-linear analysis. W. A. Benjamin, Inc., New York-Amsterdam, 1968.
[Per02] G. Perelman. The entropy formula for the Ricci flow and its geometric applications. ArXiv Mathematics e-prints, November 2002.
[Shi89] Wan-Xiong Shi. Deforming the metric on complete Riemannian manifolds. J. Differential Geom., 30(1):223-301, 1989.
[Sim83] Leon Simon. Asymptotics for a class of nonlinear evolution equations, with applications to geometric problems. Ann. of Math. (2), 118(3):525-571, 1983.
[SSS11] Oliver C. Schnürer, Felix Schulze, and Miles Simon. Stability of hyperbolic space under Ricci flow. Comm. Anal. Geom., 19(5):1023-1047, 2011.
[Whi65] E. F. Whittlesey. Analytic functions in Banach spaces. Proc. Amer. Math. Soc., 16:1077-1083, 1965.
[Wit81] Edward Witten. A new proof of the positive energy theorem. Comm. Math. Phys., 80(3):381-402, 1981.

Institut de mathématiques de Jussieu, 4, place Jussieu, Boite Courrier 247-75252 Paris
E-mail address: alix.deruelle@imj-prg.fr
École Normale Supérieure, PSL Université, 45 rue d'Ulm - 75005 Paris
E-mail address: Tristan.Ozuch-Meersseman@ens.fr