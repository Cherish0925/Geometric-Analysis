---
retention_scope: session
part: 2
total_parts: 4
---

[Part 2/4 of: Critical metrics on connected sums of Einstein four-manifolds]

If one knows that $h \in C^{4, \alpha}(Z)$, then Theorem 4.1 follows immediately from Theorems 4.2 and 4.3. The only symmetry needed for this part is the diagonal invariance for $t=-1 / 3$, which rules out the kernel element $g_{1}-g_{2}$. We will next employ the symmetries, in a crucial way, to prove smoothness.

Proposition 4.4. If $t \neq 0$, the indicial roots of $S^{t}$ are contained in $\mathbb{Z}$.
Proof. To determine the indicial roots of $S^{t}$, we need to analyze homogeneous solutions of the equation
$$\begin{aligned}
S_{0} h \equiv & \Delta_{0}^{2} h-2\left(t+\frac{5}{24}\right) \nabla_{0}^{2}\left(\Delta_{0} t r h\right)-2\left(t+\frac{5}{24}\right) \Delta_{0}\left(\delta_{0}^{2} h\right) g_{0} \\
& +2\left(t+\frac{5}{6}\right) \nabla_{0}^{2}\left(\delta_{0}^{2} h\right)+2\left(t-\frac{7}{96}\right) \Delta_{0}^{2}(t r h) g_{0}=0
\end{aligned}$$
on Euclidean space $\left(\mathbb{R}^{4} \backslash\{0\}, g_{0}\right)$. Assume by contradiction that $h$ solves (4.9) in $\mathbb{R}^{4} \backslash\{0\}$, with $h$ corresponding to an indicial root of $u+\sqrt{-1} v \in \mathbb{C} \backslash\{\mathbb{Z}\}$, and $u, v \in \mathbb{R}$. This means that $h$ has components of the form $r^{u} \cos (v r), r^{u} \sin (v r)$, or a polynomial in $\log (r)$ times one of these (we say such a solution is homogeneous of degree $u+\sqrt{-1} v$ ).

Taking the trace of (4.9) gives
$$\Delta_{0}\left[\Delta_{0}(\operatorname{tr} h)-\delta_{0}^{2} h\right]=0,$$
with $\Delta_{0}(\operatorname{tr} h)-\delta_{0}^{2} h$ homogeneous of degree $u-2+\sqrt{-1} v$. Since the indicial roots of the Laplacian are $\mathbb{Z} \backslash\{-1\}$, it follows that
$$\Delta_{0}(\operatorname{tr} h)-\delta_{0}^{2} h=0 .$$
Substituting this into (4.9) implies that
$$\Delta_{0}^{2} h+\frac{5}{4} \nabla_{0}^{2}\left(\Delta_{0} t r h\right)-\frac{9}{16} \Delta_{0}^{2}(\operatorname{tr} h) \cdot g_{0}=0 .$$
Applying the operator $\delta_{0}^{2}$ and using (4.10) we get
$$\Delta_{0}^{2}\left(\delta_{0}^{2} h\right)=0,$$
which implies $\Delta_{0} t r h=\delta_{0}^{2} h=0$, hence $\Delta_{0}^{2} h \equiv 0$. We note that the indicial roots of $\Delta_{0}$ on symmetric tensors are the same as those of the Laplacian on functions, which is $\mathbb{Z} \backslash\{-1\}$. Since $u+\sqrt{-1} v$ is not an indicial root of $\Delta_{0}^{2}$ on symmetric tensors, we have a contradiction. \(\square\)

To analyze the indicial root at 0, we first note that any constant tensor on $\mathbb{R}^{4}$ is a homogeneous degree zero solution, and the dimension of the space of these solutions is 10. We claim that the space of all homogeneous solutions of degree zero is of dimension 20. To see this, choose weight function on $\mathbb{R}^{4}$ to be given by
$$w(x)= \begin{cases}|x| & |x| \geq 1 \\ 1 & d\left(x, x_{0}\right)<1\end{cases}$$
With this weight function, for $\delta>0$ small but nonzero, consider the operator as mapping from
$$S_{g_{0}}^{t}: C_{\delta}^{4, \alpha} \rightarrow C_{\delta-4}^{0, \alpha} .$$
With obvious notation, the relative index theorem of [LM85] states that
$$\operatorname{Ind}(\delta)-\operatorname{Ind}(-\delta)=N(0),$$
where $N(0)$ is the space of all homogeneous solutions of degree zero on $\mathbb{R}^{4} \backslash\{0\}$. We note the important fact that any bounded solution globally defined on $\mathbb{R}^{4}$ must be constant, the proof is as in [AV12b, Proposition 5.4] (the key being that the flat metric is rigid). This implies that any globally defined decaying solution is trivial, so we have $\operatorname{dim} \operatorname{Ker}(-\delta)=0$. Since the adjoint weight of $\delta$ is $-\delta$, (4.13) may then be written as
$$2 \cdot \operatorname{dim} \operatorname{Ker}(\delta)=N(0) .$$
If $\delta$ is sufficiently small, it is not an indicial root, so any kernel element defined on all of $\mathbb{R}^{4}$ satisfying $h=O\left(|x|^{\delta}\right)$ as $|x| \rightarrow \infty$ is constant. Therefore $\operatorname{dim} \operatorname{Ker}(\delta)=10$, which implies that $N(0)=20$.

The only symmetric constant tensors invariant under the standard diagonal torus action are multiples of the identity matrix, or multiples of the matrix
$$\left(\begin{array}{cc}
I_{2} & 0 \\
0 & -I_{2}
\end{array}\right),$$
where $I_{2}$ is the $2 \times 2$ identity matrix. It is easy to see that this element is not invariant under the diagonal symmetry. Consequently, there are only 2 invariant degree zero solutions on $\mathbb{R}^{4} \backslash\{0\}$ : the identity matrix, and another solution with log-type growth (we will not need the explicit formula). Another application of the relative index theorem applied to the compact manifold (details are similar to above) shows that, since $c \cdot g$ extends to a global solution, the log-type solution does not extend to a global solution on $Z \backslash\left\{z_{0}\right\}$.

To finish the proof, if $h \in C_{\delta}^{4, \alpha}$ is a solution on $Z \backslash\left\{z_{0}\right\}$ for $\delta<0$ with $|\delta|$ sufficiently small which is invariant under the group action, then there is an expansion
$$h=c \cdot g+O\left(|z|^{\epsilon}\right)$$
for some constant $c \in \mathbb{R}$ and $\epsilon>0$ as $|z| \rightarrow 0$. Since the leading term is a global solution, we then have that $\tilde{h}=h-c \cdot g$ is solution on $Z \backslash\left\{z_{0}\right\}$ satisfying $\tilde{h}=O\left(|z|^{\epsilon}\right)$ as $|z| \rightarrow 0$. A standard integration-by-parts argument shows that $\tilde{h}$ extends to a weak solution on all of $Z$, and is therefore smooth by elliptic regularity. By the above, $\tilde{h} \equiv 0$. \(\square\)

\section*{5. Cokernel on an asymptotically flat manifold}

Let $(N, g)$ be the Green's function metric of a compact manifold $\left(Y, g_{Y}\right)$ with positive scalar curvature: more precisely,
$$\begin{aligned}
N & =Y \backslash\left\{y_{0}\right\}, y_{0} \in Y ; \\
g & =G^{2} g_{Y},
\end{aligned}$$
where $G$ is the Green's function of the conformal Laplacian with pole at $y_{0} \in Y$. Assume $\left(Y, g_{Y}\right)$ is Bach-flat and infinitesimally Bach-rigid, that is, $H_{0}^{1}\left(Y, g_{Y}\right)=\{0\}$.

Let $\left\{x^{i}\right\}$ denote an inverted normal coordinate system, and choose weight function $w=w(x)$ to be given by
$$w(x)= \begin{cases}|x| & |x| \geq R_{0} \\ 1 & d\left(x, x_{0}\right)<1\end{cases}$$
where $R_{0}$ is large, and $x_{0} \in N$ is a basepoint.
Theorem 5.1. Assume $\delta<0$ with $|\delta|$ small, and let $h \in C_{\delta}^{4, \alpha}$ solve the equation
$$S^{t}(h)=B^{\prime}(h)+t C^{\prime}(h)+\mathcal{K} \delta \mathcal{K} \delta(\stackrel{\circ}{h})=0,$$
where $t \neq 0$.
Then
$$h=\mathcal{K} \omega_{1}+f \cdot g_{N},$$
where $\omega_{1}$ and $f$ satisfy
$$\begin{aligned}
\square \omega_{1} & =0 \\
\Delta f & =-\frac{1}{3}\left\langle\text { Ric }, \mathcal{K} \omega_{1}\right\rangle
\end{aligned}$$
where $\square=\delta \mathcal{K}$.
Furthermore, suppose ( $N, g$ ) is either the Burns metric or the Green's function metric of the product metric on $S^{2} \times S^{2}$. If $h$ is toric invariant and diagonally
invariant and $\delta>0$, then $\omega$ and $f$ can also be chosen to be toric invariant and diagonally invariant, with
$$\begin{aligned}
\omega & =c \cdot x^{i} d x^{i}+O\left(|x|^{-1+\epsilon}\right) \\
f(x) & =c_{0}+\frac{c^{\prime}}{|x|^{2}}+O^{\prime}\left(|x|^{-4+\epsilon}\right)
\end{aligned}$$
where $c_{0}, c, c^{\prime} \in \mathbb{R}$ are constants, as $r \rightarrow \infty$, for any $\epsilon>0$.
The remainder of this section will be devoted to the proof of Theorem 5.1. Since the Bach tensor is conformally invariant it follows that $(N, g)$ is also Bach-flat. Also, since $(N, g)$ is scalar flat it is also $B^{t}$-flat, for any value of $t$. We also note that $h$ is smooth since $S^{t}$ is elliptic.

The splitting in (5.4) reflects the fact that each term in the linearization must vanish:

Proposition 5.2. Each term in (5.3) vanishes; i.e.,
$$\begin{aligned}
B^{\prime}(h) & =0 \\
C^{\prime}(h) & =0 \\
\mathcal{K} \delta \mathcal{K} \delta(\stackrel{\circ}{h}) & =0
\end{aligned}$$
Furthermore,
$$\delta(\stackrel{\circ}{h})=0 .$$
Proof. Since $(N, g)$ is $B^{t}$-flat, if we linearize the identity
$$\delta B^{t}=0$$
at $g$ we find
$$\delta\left[\left(B^{t}\right)^{\prime} h\right]+\left(\delta_{h}^{\prime}\right) B^{t}=0 \Rightarrow \delta\left[\left(B^{t}\right)^{\prime} h\right]=0 .$$
Therefore, taking the divergence of both sides of (5.3) gives
$$\square^{2} \delta(\stackrel{\circ}{h})=0 .$$

Proposition 5.3. There are no decaying elements in the kernel of □ .
Proof. To see this, we note the formula
$$\square \omega=\frac{3}{2} d \delta \omega+\delta d \omega+2 \operatorname{Ric}(\omega, \cdot) .$$
Since the Ricci tensor decays, to determine the indicial roots of □ , we need to analyze homogeneous solutions of the operator
$$\square \omega=\frac{3}{2} d \delta \omega+\delta d \omega$$
on Euclidean space $\left(\mathbb{R}^{4}, g_{0}\right)$. We claim that the indicial roots are contained in $\mathbb{Z} \backslash\{-1\}$. To prove this, assume by contradiction that $\omega$ solves $\square \omega=0$ in $\mathbb{R}^{4} \backslash\{0\}$, with $\omega$ corresponding to an indicial root of $u+\sqrt{-1} v \in \mathbb{C} \backslash\{\mathbb{Z} \backslash\{-1\}\}$, and $u, v \in \mathbb{R}$. This
means that $\omega$ has components of the form $r^{u} \cos (v r)$ or $r^{u} \sin (v r), r^{u} \log (r)$ (similarly to above, we say such a solution is homogeneous of degree $u+\sqrt{-1} v$ ). Applying $d$ to (5.12) yields that
$$d \delta d \omega=(d \delta+\delta d) d \omega=-\Delta_{H} d \omega .$$
We note that the indicial roots of $\Delta_{H}$ are exactly $\mathbb{Z} \backslash\{-1\}$ (this is easily seen since the leading term is the rough Laplacian, so the indicial roots are the same as for the Laplacian on functions). Since $d \omega$ is homogeneous of degree $u-1+\sqrt{-1} v$, which is not an indicial root of $\Delta_{H}$, we conclude that $d \omega=0$. A similiar argument shows that $\delta \omega=0$. Since both $d \omega=0$ and $\delta \omega=0$, we have that $\Delta_{H}(\omega)=0$, which is a contradiction since $u+\sqrt{-1} v$ was chosen to not be an indicial root of $\Delta_{H}$.

Consequently, by standard weighted space theory, any decaying solution of $\square \xi=0$ on an AF space must satisfy $\xi=O\left(r^{-2}\right)$ as $r \rightarrow \infty$ [Bar86]. An elementary integration by parts argument then shows that $\mathcal{K} \xi=0$. As there are no decaying conformal Killing fields on an AF space, we conclude that $\xi=0$. \(\square\)

Remark 5.4. By a separation of variables argument as in [AV12b, Section 4.1], it is straightforward to show that the indicial roots of □ are in fact exactly $\mathbb{Z} \backslash\{-1\}$, although we will not need this fact.

By this proposition and (5.10),
$$\square \delta(\stackrel{\circ}{h})=0 .$$
Applying the result once again gives (5.9):
$$\delta \stackrel{\circ}{h}=0 .$$
In particular,
$$\mathcal{K} \delta \mathcal{K} \delta(\stackrel{\circ}{h})=0$$
and consequently
$$B^{\prime}(h)+t C^{\prime}(h)=0 .$$

If we linearize the trace-free property of the Bach tensor at $g$ it follows that
$$\operatorname{tr} B^{\prime}(h)=0 .$$
Therefore, taking the trace of (5.15) gives
$$\begin{aligned}
0 & =\operatorname{tr} B^{\prime}(h)+t \operatorname{tr} C^{\prime}(h) \\
& =t \operatorname{tr} C^{\prime}(h) .
\end{aligned}$$

Lemma 5.5. If ( $X^{4}, g$ ) is either scalar-flat or Einstein, then
$$\begin{aligned}
\operatorname{tr} C^{\prime}(h) & =-6 \Delta R^{\prime}(h) \\
& =-6 \Delta\left[-\Delta(\operatorname{tr} h)+\delta^{2} h-\langle\text { Ric }, h\rangle\right],
\end{aligned}$$
where $R^{\prime}$ denotes the linearization of the scalar curvature.

Proof. Since $C=0$ for scalar-flat or Einstein metrics, we have
$$\begin{aligned}
(\operatorname{tr} C)^{\prime} & =(\operatorname{tr})^{\prime} C+\operatorname{tr}\left(C^{\prime}\right) \\
& =\operatorname{tr}\left(C^{\prime}\right) .
\end{aligned}$$
Also, $\operatorname{tr} C=-6 \Delta R$, so
$$\operatorname{tr}\left(C^{\prime}\right)=(\operatorname{tr} C)^{\prime}=-6(\Delta)^{\prime} R-6 \Delta R^{\prime},$$
and since $R$ is constant we get
$$\operatorname{tr}\left(C^{\prime}\right)=-6 \Delta R^{\prime},$$
as claimed. \(\square\)

In view of (5.16) and the preceding lemma we have
$$\Delta R^{\prime}(h)=\Delta\left[-\Delta(\operatorname{tr} h)+\delta^{2} h-\langle\text { Ric }, h\rangle\right]=0 .$$
Since
$$\left|\nabla^{2} h\right|=O\left(|x|^{\delta-2}\right), \quad\langle\text { Ric }, h\rangle=O\left(|x|^{\delta-4}\right),$$
it follows that $R^{\prime}(h)$ is a decaying harmonic function. Therefore,
$$R^{\prime}(h)=-\Delta(\operatorname{tr} h)+\delta^{2} h-\langle\text { Ric }, h\rangle=0 .$$

Recall $C$ is given by
$$C=2 \nabla^{2} R-2(\Delta R) g-2 R\left(R i c-\frac{1}{4} R g\right) .$$
Linearizing this at $g$ (which is scalar-flat) gives
$$C^{\prime}(h)=2 \nabla^{2} R^{\prime}(h)-2 \Delta R^{\prime}(h) g-2 R^{\prime}(h) \cdot R i c .$$
From (5.18), it follows that $C^{\prime}(h)=0$, which completes the proof of Proposition 5.2. \(\square\)

Write
$$h=\stackrel{\circ}{h}+f g,$$
where $f=(\operatorname{tr} h) / 4$. The conformal invariance of the Bach tensor leads to the formula
$$B^{\prime}(\phi g)=-2 \phi B$$
for any function $\phi$. Since $g$ is Bach-flat this implies
$$\begin{aligned}
0 & =B^{\prime}(\stackrel{\circ}{h}+f g) \\
& =B^{\prime}(\stackrel{\circ}{h})
\end{aligned}$$
It follows from [AV12b, Proposition 2.1] that any decaying, transverse-traceless element in the kernel of $B^{\prime}$ must decay quadratically, hence
$$|\stackrel{\circ}{h}|=O\left(|x|^{-2}\right),$$
as $|x| \rightarrow \infty$.

Conformal invariance of the Bach tensor also implies the invariance of its linearization:
$$0=B_{g}^{\prime}(\stackrel{\circ}{h})=B_{G^{2} g_{0}}^{\prime}(\stackrel{\circ}{h})=G^{-2} B_{g_{0}}^{\prime}\left(G^{-2} \stackrel{\circ}{h}\right) .$$
Denote
$$\tilde{h}=G^{-2} \stackrel{\circ}{h} .$$
Then $\tilde{h} \in C^{\infty}\left(Y \backslash\left\{y_{0}\right\}\right)$, and
$$B_{g_{0}}^{\prime} \tilde{h}=0 .$$
In addition, since $\stackrel{\circ}{h}$ decays quadratically at infinity, $\tilde{h}$ vanishes quadratically at $y_{0}$. To see this, first note that
$$\begin{aligned}
|\tilde{h}|_{g_{0}}^{2} & =\left(g_{0}\right)^{i k}\left(g_{0}\right)^{k \ell} \tilde{h}_{i j} \tilde{h}_{k \ell} \\
& =G^{4} g^{i k} g^{j \ell}\left(G^{-2} \stackrel{\circ}{h}_{i j}\right)\left(G^{-2} \stackrel{\circ}{h}_{k \ell}\right) \\
& =|\stackrel{\circ}{h}|_{g}^{2}
\end{aligned}$$
We note the relation between $r=|x|$ and $\rho=|y|$ :
$$r \sim \rho^{-1},$$
so that (5.21) and (5.25) together imply
$$|\tilde{h}|_{g_{0}}=O\left(\rho^{2}\right),$$
as $\rho \rightarrow 0$. In particular, $\tilde{h} \in C^{1, \alpha}(Y)$.
We now use the standard splitting of a trace-free symmetric tensor into the image of the conformal Killing operator and the space of transverse-traceless tensors. More precisely, we first solve
$$\square_{g_{0}} \omega_{0}=\delta_{g_{0}} \tilde{h}$$
with $\omega_{0} \in C^{2, \alpha}(Y)$. Since □ is self-adjoint with kernel given by the space of conformal Killing forms $\mathcal{C}\left(Y, g_{0}\right)$, this equation is solvable whenever the right-hand side is orthogonal to $\mathcal{C}\left(Y, g_{0}\right)$. However, if $\eta \in \mathcal{C}\left(Y, g_{0}\right)$, then
$$\int\left\langle\delta_{g_{0}} \tilde{h}, \eta\right\rangle d V_{0}=-\frac{1}{2} \int\left\langle\tilde{h}, \mathcal{K}_{g_{0}} \eta\right\rangle d V_{0}=0$$
It follows that (5.27) is always solvable, although the solution $\omega_{0}$ is only unique up to the space of conformal Killing fields. This fact will actually be crucial when we impose toric and diagonal invariance, in which case we will need to solve (5.27) equivariantly and study the space of invariant forms (see the end of this section).

Let
$$h_{0}=\tilde{h}-\mathcal{K}_{g_{0}} \omega_{0} .$$

Then $h_{0} \in C^{1, \alpha}(Y)$, and is smooth away from $y_{0}$. By (5.27), $h_{0}$ is transverse-traceless, and on $Y \backslash\left\{y_{0}\right\}$
$$\begin{aligned}
B_{g_{0}}^{\prime}\left(h_{0}\right) & =B_{g_{0}}^{\prime}\left(\tilde{h}-\mathcal{K}_{g_{0}} \omega_{0}\right) \\
& =B_{g_{0}}^{\prime}(\tilde{h}) \quad\left(\text { since } \operatorname{Im} \mathcal{K} \subset \operatorname{Ker} B^{\prime}\right) \\
& =0
\end{aligned}$$
A standard integration by parts argument shows that $h_{0}$ is a global weak solution of $B_{g_{0}}^{\prime} h_{0}=0$, and from elliptic theory it follows that $h_{0}$ is smooth on $Y$. Since $\left(Y, g_{0}\right)$ is assumed to be infinitesimally Bach-rigid, $h_{0}=0$, and we conclude that
$$\tilde{h}=\mathcal{K}_{g_{0}} \omega_{0} .$$
By conformal invariance of the conformal Killing operator,
$$\mathcal{K}_{g_{0}} \omega_{0}=G^{-2} \mathcal{K}_{g}\left[G^{2} \omega_{0}\right] .$$
Hence,
$$G^{-2} \stackrel{\circ}{h}=\tilde{h}=G^{-2} \mathcal{K}_{g}\left[G^{2} \omega_{0}\right],$$
which implies
$$\stackrel{\circ}{h}=\mathcal{K}_{g}\left[G^{2} \omega_{0}\right] .$$
Also, by (5.14), $\omega_{1}=G^{2} \omega_{0}$ satisfies
$$0=\delta \stackrel{\circ}{h}=\square \omega_{1},$$
which gives the first equation in (5.5). To prove the second equation, use the splitting $h=\stackrel{\circ}{h}+f g$ in (5.18); this gives
$$-3 \Delta f-\langle\text { Ric }, \stackrel{\circ}{h}\rangle=0$$
(note we have used the scalar-flat condition again).
Up to this point we have not used the invariance of $h$. In general, the form $\omega_{1}$ can grow quadratically on $N$; however, using invariance we can choose a solution $\omega_{0}$ of (5.27) so that the resulting form $\omega_{1}$ has linear growth on $N$, with highest order given by (5.6). To see this, we argue as follows. Since $\omega_{0} \in C^{2, \alpha}(Y)$, it admits an expansion
$$\omega_{0}=\omega^{(0)}+\omega^{(1)}+\omega^{(2)}+O\left(\rho^{2+\alpha}\right),$$
as $\rho \rightarrow 0$, where
$$\begin{aligned}
& \omega^{(0)}=\omega_{i}^{(0)} d y^{i} \\
& \omega^{(1)}=\omega_{i j}^{(1)} y^{i} d y^{j} \\
& \omega^{(2)}=\omega_{i j k}^{(2)} y^{i} y^{j} d y^{k},
\end{aligned}$$
where the $\{y\}$-coordinates are local normal coordinates near $y_{0}$ with torus action
$$\left(y_{1}, y_{2}, y_{3}, y_{4}\right) \mapsto\left(e^{\sqrt{-1} \theta_{1}}\left(y_{1}+\sqrt{-1} y_{2}\right), e^{\sqrt{-1} \theta_{2}}\left(y_{3}+\sqrt{-1} y_{4}\right)\right) .$$

Denote $\rho_{1}^{2}=y_{1}^{2}+y_{2}^{2}, \rho_{2}^{2}=y_{3}^{2}+y_{4}^{2}$, and $\rho^{2}=\rho_{1}^{2}+\rho_{2}^{2}$, and let $\theta_{1}, \theta_{2}$ denote the corresponding angular coordinates. Since the group is compact, we can average over the group to find a solution of (5.27) which is also invariant under the group action (5.38), as well as the diagonal symmetry. It is elementary to see that there is no form with constant coefficients which is invariant under the torus action (5.38). The only toric-invariant 1-forms with linear coefficients are
$$c_{1} d \rho_{1}+c_{2} \rho_{1} d \theta_{1}+c_{3} d \rho_{2}+c_{4} \rho_{2} d \theta_{2} .$$
The forms $\rho_{1} d \theta_{1}$ and $\rho_{2} d \theta_{2}$ extend to global Killing forms, so we may assume that $c_{2}=c_{4}=0$. Invariance under the diagonal symmetry implies that $c_{1}=c_{3}$, so we have that
$$\omega_{0}=c \cdot \rho d \rho+\omega^{(2)}+O\left(\rho^{2+\alpha}\right),$$
for some constant $c \in \mathbb{R}$. This implies the expansion
$$\omega_{1}=c \cdot x^{i} d x^{i}+O\left(|x|^{-\alpha}\right)$$
as $|x| \rightarrow \infty$. Averaging over the group, we may assume $\omega_{1}$ is also invariant under the group action.

To obtain the expansion for $f$, extend the function $|x|^{-2}$ to all of $N$ by a cutoff function (which we supress). It is not hard to see that $\Delta\left(|x|^{-2}\right)=O\left(|x|^{-6}\right)$ as $|x| \rightarrow \infty$, and there exists a constant $c^{\prime} \in \mathbb{R}$ so that
$$\int_{N}\left(-\frac{1}{3}\left\langle\text { Ric }, \mathcal{K} \omega_{1}\right\rangle-c^{\prime} \Delta|x|^{-2}\right) d V=0$$
Next, consider $\Delta: C_{-4+\epsilon}^{2, \alpha}(N) \rightarrow C_{-6+\epsilon}^{0, \alpha}(N)$. The adjoint weight is $2-\epsilon$, so from toric invariance, the kernel of the adjoint contains only constants. We may then solve the equation
$$\Delta \tilde{f}=-\frac{1}{3}\left\langle R i c, \mathcal{K} \omega_{1}\right\rangle-c^{\prime} \Delta\left(|x|^{-2}\right)$$
with $\tilde{f} \in C_{-4+\epsilon}^{2, \alpha}$. Equivalently,
$$\Delta\left(\tilde{f}+c^{\prime}|x|^{-2}\right)=-\frac{1}{3}\left\langle R i c, \mathcal{K} \omega_{1}\right\rangle .$$
Since there are no decaying harmonic functions, we must have
$$f=\tilde{f}+c^{\prime}|x|^{-2}$$
with $\tilde{f}=O\left(|x|^{-4+\epsilon}\right)$ as $|x| \rightarrow \infty$ for any $\epsilon>0$. Again, averaging over the group, we may assume that $f$ is invariant under the group action.

Finally, we consider the case that $\delta>0$. Using the same argument as in the proof of Theorem 4.1 involving the relative index theorem, the toric and diagonal symmetries imply that the only possible leading terms are $c \cdot g_{N}$ and a log-type solution. Since $c \cdot g_{N}$ extends to a global solution, again the relative index theorem implies that the log-type solution does not occur. Consequently, after subtracting a multiple of the metric, the solution is decaying, and (5.7) follows from the previous expansion.

\section*{6. Asymptotics of the cokernel}

Denote the (normalized) cokernel element described in Theorem 5.1 by
$$o_{1}=\kappa+f g,$$
where
$$\kappa=\mathcal{K}\left[\omega_{1}\right],$$
with
$$\left(\omega_{1}\right)_{i}=x^{i}+O(1) .$$
This section will be devoted to proving the following
Theorem 6.1. The tracefree part of $A F$-cokernel element $o_{1}$ satisfies
$$\kappa_{i j}=\frac{2}{3} W_{i k j \ell}\left(y_{0}\right) \frac{x^{k} x^{\ell}}{|x|^{4}}+O\left(|x|^{-4+\epsilon}\right)$$
as $|x| \rightarrow \infty$, for any $\epsilon>0$.
Recall in inverted normal coordinates at the point $y_{0}$, the AF metric has the expansion
$$g_{i j}=\delta_{i j}-\frac{1}{3} R_{i k j \ell}\left(y_{0}\right) \frac{x^{k} x^{\ell}}{|x|^{4}}+\frac{2 A}{|x|^{2}} \delta_{i j}+O\left(|x|^{-3}\right) .$$
In the following, we will need to have expansions for the Christoffel symbols:
Lemma 6.2. In inverted normal coordinates,
$$\begin{aligned}
\Gamma_{i j}^{k}=- & \frac{1}{3} R_{i \alpha k j}\left(y_{0}\right) \frac{x^{\alpha}}{|x|^{4}}-\frac{1}{3} R_{j \alpha k i}\left(y_{0}\right) \frac{x^{\alpha}}{|x|^{4}} \\
& +\frac{2}{3} R_{i \alpha k \beta}\left(y_{0}\right) \frac{x^{j} x^{\alpha} x^{\beta}}{|x|^{6}}+\frac{2}{3} R_{j \alpha k \beta}\left(y_{0}\right) \frac{x^{i} x^{\alpha} x^{\beta}}{|x|^{6}}-\frac{2}{3} R_{i \alpha j \beta}\left(y_{0}\right) \frac{x^{k} x^{\alpha} x^{\beta}}{|x|^{6}} \\
& -2 A \frac{x^{i} \delta_{j k}}{|x|^{4}}-2 A \frac{x^{j} \delta_{i k}}{|x|^{4}}+2 A \frac{x^{k} \delta_{i j}}{|x|^{4}}+O\left(|x|^{-4}\right) .
\end{aligned}$$
Proof. Recall
$$\Gamma_{i j}^{k}=\frac{1}{2} g^{k m}\left(\partial_{i} g_{j m}+\partial_{j} g_{i m}-\partial_{m} g_{i j}\right) .$$
By (6.5),
$$\begin{aligned}
\partial_{i} g_{j m}= & \partial_{i}\left\{-\frac{1}{3} R_{j \alpha m \beta}\left(y_{0}\right) \frac{x^{\alpha} x^{\beta}}{|x|^{4}}+\frac{2 A}{|x|^{2}} \delta_{j m}\right\}+\cdots \\
= & -\frac{1}{3} R_{j i m \beta}\left(y_{0}\right) \frac{x^{\beta}}{|x|^{4}}-\frac{1}{3} R_{j \alpha m i}\left(y_{0}\right) \frac{x^{\alpha}}{|x|^{4}}+\frac{4}{3} R_{j \alpha m \beta}\left(y_{0}\right) \frac{x^{i} x^{\alpha} x^{\beta}}{|x|^{6}} \\
& -4 A \frac{x^{i} \delta_{j m}}{|x|^{4}}+\cdots
\end{aligned}$$

Therefore, after combining terms and rearranging,
$$\begin{aligned}
\partial_{i} g_{j m}+\partial_{j} g_{i m} & -\partial_{m} g_{i j}=-\frac{2}{3} R_{j \alpha m i}\left(y_{0}\right) \frac{x^{\alpha}}{|x|^{4}}-\frac{2}{3} R_{i \alpha m j}\left(y_{0}\right) \frac{x^{\alpha}}{|x|^{4}} \\
& +\frac{4}{3} R_{j \alpha m \beta}\left(y_{0}\right) \frac{x^{i} x^{\alpha} x^{\beta}}{|x|^{6}}+\frac{4}{3} R_{i \alpha m \beta}\left(y_{0}\right) \frac{x^{j} x^{\alpha} x^{\beta}}{|x|^{6}}-\frac{4}{3} R_{j \alpha i \beta}\left(y_{0}\right) \frac{x^{m} x^{\alpha} x^{\beta}}{|x|^{6}} \\
& -4 A \frac{x^{i} \delta_{j m}}{|x|^{4}}-4 A \frac{x^{j} \delta_{i m}}{|x|^{4}}+4 A \frac{x^{m} \delta_{i j}}{|x|^{4}}+\cdots
\end{aligned}$$
It follows from (6.5) that the inverse matrix $g^{k m}$ is given by
$$g^{k m}=\delta_{k m}+\frac{1}{3} R_{k \alpha m \beta}\left(y_{0}\right) \frac{x^{\alpha} x^{\beta}}{|x|^{4}}-\frac{2 A}{|x|^{2}} \delta_{k m}+\cdots$$
Consequently,
$$\begin{aligned}
\Gamma_{i j}^{k}= & -\frac{1}{3} R_{j \alpha k i}\left(y_{0}\right) \frac{x^{\alpha}}{|x|^{4}}-\frac{1}{3} R_{i \alpha k j}\left(y_{0}\right) \frac{x^{\alpha}}{|x|^{4}} \\
& +\frac{2}{3} R_{j \alpha k \beta}\left(y_{0}\right) \frac{x^{j} x^{\alpha} x^{\beta}}{|x|^{6}}+\frac{2}{3} R_{i \alpha k \beta}\left(y_{0}\right) \frac{x^{j} x^{\alpha} x^{\beta}}{|x|^{6}}-\frac{2}{3} R_{j \alpha i \beta}\left(y_{0}\right) \frac{x^{k} x^{\alpha} x^{\beta}}{|x|^{6}} \\
& -2 A \frac{x^{i} \delta_{j k}}{|x|^{4}}-2 A \frac{x^{j} \delta_{i k}}{|x|^{4}}+2 A \frac{x^{k} \delta_{i j}}{|x|^{4}}+O\left(|x|^{-4}\right),
\end{aligned}$$
which is the same as (6.6) after rearranging and re-indexing. \(\square\)

Next, we consider the form $\omega=\omega_{j} d x^{j}$ with
$$\omega_{j}=x^{j}+b_{j k} \frac{x^{k}}{|x|^{2}}$$
where
$$b_{i j}=-\frac{1}{3} S_{i j}\left(y_{0}\right)+2 A \delta_{i j},$$
where
$$S_{i j}\left(y_{0}\right)=\frac{1}{2}\left(R_{i j}\left(y_{0}\right)-\frac{1}{6} R\left(y_{0}\right) \delta_{i j}\right)$$
is the Schouten tensor. We extend $\omega$ to be a globally defined form on all of $N$ by cutting it off at some finite distance from the basepoint. Since this cutoff will not matter in the following, we will suppress it from the following computations.

Lemma 6.3. In inverted normal coordinates,
$$\begin{aligned}
\mathcal{K}[\omega]= & 2 \frac{b_{i j}}{|x|^{2}}-2 \frac{b_{j k} x^{k} x^{i}}{|x|^{4}}-2 \frac{b_{i k} x^{k} x^{j}}{|x|^{4}}-\frac{1}{2} \frac{b_{k k}}{|x|^{4}} \delta_{i j}+\frac{b_{k \ell} x^{k} x^{\ell}}{|x|^{4}} \delta_{i j} \\
& +\frac{2}{3} R_{i k j \ell}\left(y_{0}\right) \frac{x^{k} x^{\ell}}{|x|^{4}}-\frac{1}{6} R_{k \ell}\left(y_{0}\right) \frac{x^{k} x^{\ell}}{|x|^{4}} \delta_{i j} \\
& +\frac{2 A}{|x|^{4}}\left[4 x^{i} x^{j}-|x|^{2} \delta_{i j}\right]+O\left(|x|^{-4}\right),
\end{aligned}$$
as $|x| \rightarrow \infty$.
Proof. We begin by noting
$$\nabla_{i} \omega_{j}=\partial_{i} \omega_{j}-\Gamma_{i j}^{k} \omega_{k} .$$
Using (6.9),
$$\partial_{i} \omega_{j}=\delta_{i j}+\frac{b_{j i}}{|x|^{2}}-2 \frac{b_{j k} x^{k} x^{i}}{|x|^{4}}+\cdots,$$
while
$$\begin{aligned}
\Gamma_{i j}^{k} \omega_{k}= & -\frac{1}{3} R_{i \alpha k j}\left(y_{0}\right) \frac{x^{\alpha} x^{k}}{|x|^{4}}-\frac{1}{3} R_{j \alpha k i}\left(y_{0}\right) \frac{x^{\alpha} x^{k}}{|x|^{4}} \\
& +\frac{2}{3} R_{i \alpha k \beta}\left(y_{0}\right) \frac{x^{j} x^{k} x^{\alpha} x^{\beta}}{|x|^{4}}+\frac{2}{3} R_{j \alpha k \beta}\left(y_{0}\right) \frac{x^{j} x^{k} x^{\alpha} x^{\beta}}{|x|^{4}}-\frac{2}{3} R_{i \alpha j \beta}\left(y_{0}\right) \frac{x^{\alpha} x^{\beta}}{|x|^{2}} \\
& -4 A \frac{x^{i} x^{j}}{|x|^{4}}+2 A \frac{\delta_{i j}}{|x|^{2}}+O\left(|x|^{-3}\right) .
\end{aligned}$$
By the symmetries of the curvature tensor, the third and fourth terms above obviously vanish. If we re-index in the first two terms, $k \leftrightarrow \beta$, then we can rewrite them as
$$\begin{aligned}
-\frac{1}{3} R_{i \alpha k j}\left(y_{0}\right) \frac{x^{\alpha} x^{k}}{|x|^{4}}-\frac{1}{3} R_{j \alpha k i}\left(y_{0}\right) \frac{x^{\alpha} x^{k}}{|x|^{4}} & =-\frac{1}{3} R_{i \alpha \beta j}\left(y_{0}\right) \frac{x^{\alpha} x^{\beta}}{|x|^{4}}-\frac{1}{3} R_{j \alpha \beta i}\left(y_{0}\right) \frac{x^{\alpha} x^{\beta}}{|x|^{4}} \\
& =\frac{1}{3} R_{i \alpha j \beta}\left(y_{0}\right) \frac{x^{\alpha} x^{\beta}}{|x|^{4}}+\frac{1}{3} R_{i \beta j \alpha}\left(y_{0}\right) \frac{x^{\alpha} x^{\beta}}{|x|^{4}} \\
& =\frac{2}{3} R_{i \alpha j \beta}\left(y_{0}\right) \frac{x^{\alpha} x^{\beta}}{|x|^{4}} .
\end{aligned}$$
Substituting this back into (6.14), we find that
$$\Gamma_{i j}^{k} \omega_{k}=-4 A \frac{x^{i} x^{j}}{|x|^{4}}+2 A \frac{\delta_{i j}}{|x|^{2}}+O\left(|x|^{-3}\right) .$$
Therefore,
$$\nabla_{i} \omega_{j}=\delta_{i j}+\frac{b_{j i}}{|x|^{2}}-2 \frac{b_{j k} x^{k} x^{i}}{|x|^{4}}+4 A \frac{x^{i} x^{j}}{|x|^{4}}-2 A \frac{\delta_{i j}}{|x|^{2}}+O\left(|x|^{-3}\right) .$$
The divergence of $\omega$ is
$$\begin{aligned}
\delta \omega= & g^{i j} \nabla_{i} \omega_{j} \\
= & \left\{\delta_{i j}+\frac{1}{3} R_{i \alpha j \beta}\left(y_{0}\right) \frac{x^{\alpha} x^{\beta}}{|x|^{4}}-\frac{2 A}{|x|^{2}} \delta_{i j}+\cdots\right\} \\
& \times\left\{\delta_{i j}+\frac{b_{j i}}{|x|^{2}}-2 \frac{b_{j k} x^{k} x^{i}}{|x|^{4}}-2 \frac{b_{j k} x^{k} x^{i}}{|x|^{4}}+4 A \frac{x^{i} x^{j}}{|x|^{4}}-2 A \frac{\delta_{i j}}{|x|^{2}}+\cdots\right\} \\
= & 4+\frac{b_{k k}}{|x|^{2}}-2 \frac{b_{k \ell} x^{k} x^{\ell}}{|x|^{4}}+\frac{1}{3} R_{k \ell}\left(y_{0}\right) \frac{x^{k} x^{\ell}}{|x|^{4}}-\frac{12 A}{|x|^{2}}+\cdots
\end{aligned}$$

Hence,
$$\begin{aligned}
(\delta \omega) g_{i j}= & \left\{4+\frac{b_{k k}}{|x|^{2}}-2 \frac{b_{k \ell} x^{k} x^{\ell}}{|x|^{4}}+\frac{1}{3} R_{k \ell}\left(y_{0}\right) \frac{x^{k} x^{\ell}}{|x|^{4}}-\frac{12 A}{|x|^{2}}+\cdots\right\} \\
& \times\left\{\delta_{i j}-\frac{1}{3} R_{i k j \ell}\left(y_{0}\right) \frac{x^{k} x^{\ell}}{|x|^{4}}+\frac{2 A}{|x|^{2}} \delta_{i j}+\cdots\right\} \\
= & 4 \delta_{i j}+\frac{b_{k k}}{|x|^{2}} \delta_{i j}-2 \frac{b_{k \ell} x^{k} x^{\ell}}{|x|^{4}} \delta_{i j}-\frac{4}{3} R_{i k j \ell}\left(y_{0}\right) \frac{x^{k} x^{\ell}}{|x|^{4}}+\frac{1}{3} R_{k \ell}\left(y_{0}\right) \frac{x^{k} x^{\ell}}{|x|^{4}} \delta_{i j} \\
& -\frac{4 A}{|x|^{2}} \delta_{i j}+\cdots
\end{aligned}$$

Finally, combining (6.16) and (6.18) we get
$$\begin{aligned}
\mathcal{K}[\omega]_{i j}= & \nabla_{i} \omega_{j}+\nabla_{j} \omega_{i}-\frac{1}{2}(\delta \omega) g_{i j} \\
= & 2 \frac{b_{i j}}{|x|^{2}}-2 \frac{b_{j k} x^{k} x^{i}}{|x|^{4}}-2 \frac{b_{i k} x^{k} x^{j}}{|x|^{4}}-\frac{1}{2} \frac{b_{k k}}{|x|^{4}} \delta_{i j}+\frac{b_{k \ell} x^{k} x^{\ell}}{|x|^{4}} \delta_{i j} \\
& +\frac{2}{3} R_{i k j \ell}\left(y_{0}\right) \frac{x^{k} x^{\ell}}{|x|^{4}}-\frac{1}{6} R_{k \ell}\left(y_{0}\right) \frac{x^{k} x^{\ell}}{|x|^{4}} \delta_{i j}+8 A \frac{x^{i} x^{j}}{|x|^{4}}-2 A \frac{\delta_{i j}}{|x|^{2}}+\cdots
\end{aligned}$$
which completes the proof. \(\square\)

This implies the following decay rate for $\square \omega$ :
Lemma 6.4. In inverted normal coordinates,
$$\square \omega=O\left(|x|^{-4}\right),$$
as $|x| \rightarrow \infty$.
Proof. Recall that □ is given by
$$\square \omega_{j}=(\delta \mathcal{K}[\omega])_{j}=g^{i k} \nabla_{k} \mathcal{K}[\omega]_{i j}=g^{i k} \partial_{k} \mathcal{K}[\omega]_{i j}+\mathcal{K}[\omega] * \Gamma .$$
Note that
$$(\mathcal{K}[\omega]) * \Gamma \sim|x|^{-5},$$
so it is much lower order than the derivative term. Also,
$$\begin{aligned}
g^{i k} \partial_{k} \mathcal{K}[\omega]_{i j} & =\left(\delta_{i k}+O\left(|x|^{-2}\right)\right) \partial_{k} \mathcal{K}_{i j}[\omega] \\
& =\partial_{i} \mathcal{K}[\omega]_{i j}+\text { (lower) } .
\end{aligned}$$
Consequently, we obtain
$$\begin{aligned}
(\square \omega)_{j}= & -2 \frac{b_{i j} x^{i}}{|x|^{4}}-4 \frac{b_{j k} x^{k}}{|x|^{4}}-\frac{b_{k k}}{|x|^{4}} x^{j}+4 \frac{b_{k \ell} x^{k} x^{\ell} x^{j}}{|x|^{6}} \\
& +\frac{2}{3} R_{k \ell}\left(y_{0}\right) \frac{x^{k} x^{\ell} x^{j}}{|x|^{6}}-R_{j k}\left(y_{0}\right) \frac{x^{k}}{|x|^{4}}+12 A \frac{x^{j}}{|x|^{4}}+O\left(|x|^{-4}\right)
\end{aligned}$$
as $|x| \rightarrow \infty$. Substituting (6.10) into this completes the proof. \(\square\)

Consider $\square: C_{-2+\epsilon}^{2, \alpha}(N) \rightarrow C_{-4+\epsilon}^{0, \alpha}(N)$, with $\epsilon>0$ small, and consider the equation
$$\square\left(\omega^{\prime}\right)=\square \omega$$
The cokernel of this operator has domain weight $-\epsilon$, so from Proposition 5.3, there is no cokernel. Consequently, (6.22) has a solution $\omega^{\prime} \in C_{-2+\epsilon}^{2, \alpha}$. The form $\tilde{\omega}=\omega-\omega^{\prime}$ is then a solution of $\square \tilde{\omega}=0$ with expansion
$$\tilde{\omega}_{j}=x^{j}+b_{j k} \frac{x^{k}}{|x|^{2}}+O\left(|x|^{-2+\epsilon}\right),$$
for any $\epsilon>0$. Since $\tilde{\omega}$ and $\omega_{1}$ have the same leading term, and their difference is decaying, we must have $\tilde{\omega}=\omega_{1}$, so of course $\omega_{1}$ admits the same expansion.

Proof of Theorem 6.1. Substituting (6.10) into (6.12) and using the decomposition of the curvature tensor into Weyl and Schouten parts gives
$$\begin{aligned}
\mathcal{K}[\omega]_{i j} & =2\left\{-\frac{1}{3} S_{i j}\left(y_{0}\right)+2 A \delta_{i j}\right\} \frac{1}{|x|^{2}}-2\left\{-\frac{1}{3} S_{j k}\left(y_{0}\right)+2 A \delta_{j k}\right\} \frac{x^{i} x^{k}}{|x|^{4}} \\
& -2\left\{-\frac{1}{3} S_{i k}\left(y_{0}\right)+2 A \delta_{i k}\right\} \frac{x^{j} x^{k}}{|x|^{4}}-\frac{1}{2}\left\{-\frac{1}{18} R\left(y_{0}\right)+8 A\right\} \frac{\delta_{i j}}{|x|^{2}} \\
& +\left\{-\frac{1}{3} S_{k \ell}\left(y_{0}\right)+2 A \delta_{k \ell}\right\} \frac{x^{k} x^{\ell}}{|x|^{4}} \delta_{i j}+\frac{2}{3}\left\{W_{i k j \ell}\left(y_{0}\right)+\left(\delta_{i j} S_{k \ell}\left(y_{0}\right)-\delta_{i \ell} S_{j k}\left(y_{0}\right)\right.\right. \\
& \left.\left.-\delta_{j k} S_{i \ell}\left(y_{0}\right)+\delta_{k \ell} S_{i j}\left(y_{0}\right)\right)\right\} \frac{x^{k} x^{\ell}}{|x|^{4}}+8 A \frac{x^{i} x^{j}}{|x|^{4}}-\frac{1}{6} R_{k \ell}\left(y_{0}\right) \frac{x^{k} x^{\ell}}{|x|^{4}} \delta_{i j}-2 A \frac{\delta_{i j}}{|x|^{2}}+\cdots \\
& =\frac{2}{3} W_{i k j \ell}\left(y_{0}\right) \frac{x^{k} x^{\ell}}{|x|^{4}}+\cdots
\end{aligned}$$ \(\square\)

\section*{7. Some auxiliary linear equations}

In this section, we solve two linear equations. First, an equation on the AF metric $\left(N, g_{N}\right)$, and second, an equation on the compact manifold $\left(Z, g_{Z}\right)$. The "group action" will refer to the $U(2)$-action in the cases $g_{Z}$ is the Fubini-Study metric and $g_{N}$ is the Burns metric, and to the toric action plus diagonal symmetry in the case $g_{Z}$ is $g_{S^{2} \times S^{2}}$ and $g_{N}$ is the corresponding Green's function metric.
7.1. A linear equation on $\left(N, g_{N}\right)$. On the compact manifold $\left(Z, g_{Z}\right)$, in normal coordinates $\left\{z^{i}\right\}$ around $z_{0}$, we have the expansion
$$g_{Z}=\left(g_{Z}\right)_{i j} d z^{i} d z^{j}=\left(\delta_{i j}+H_{2}(z)_{i j}+O\left(|z|^{4}\right)_{i j}\right) d z^{i} d z^{j},$$
where
$$H_{2}(z)_{i j}=-\frac{1}{3} R_{i k j l}\left(z_{0}\right) z^{k} z^{l}$$

Again let $\left(N, g_{N}\right)$ be the conformal blow-up of the Bach-flat manifold $\left(Y, g_{Y}\right)$, as above. Consider the quadratic tensor
$$H_{2}(x)=\left(-\frac{1}{3} R_{i k j l}\left(z_{0}\right) x^{k} x^{l}\right) d x^{i} d x^{j}$$
This tensor $H_{2}(x)$ of course does not live on all of $N$, since it is only defined in the AF coordinate system. To extend $H_{2}(x)$ to all of $N$, let $0 \leq \phi \leq 1$ be a cut-off function satisfying
$$\phi(t)= \begin{cases}1 & t \leq 1 \\ 0 & t \geq 2\end{cases}$$
and consider $\left(1-\phi\left(R_{0}^{-1} x\right)\right) H_{2}(x)$, where $R_{0}$ is very large.
Proposition 7.1. Let $S$ denote the linearized operator on $N$, then
$$S\left(\left(1-\phi\left(R_{0}^{-1} x\right) H_{2}(x)\right)=O\left(|x|^{-4}\right)\right.$$
as $|x| \rightarrow \infty$
Proof. From (3.43), the linearized operator has the general form
$$\begin{aligned}
S h & =\left(g^{-2}+g * g^{-3}\right) * \nabla^{4} h+g * g^{-3} * R m * \nabla^{2} h+g * g^{-3} * \nabla R m * \nabla h \\
& +\left(g^{-2}+g * g^{-3}\right) *\left(\nabla^{2} R m+R m * R m\right) * h .
\end{aligned}$$
It is easy to see that for $|x|$ sufficiently large and any tensor $h$,
$$\begin{aligned}
\nabla^{4} h & =\partial^{4} h+\Gamma * \partial^{3} h+(\partial \Gamma+\Gamma * \Gamma) * \partial^{2} h \\
& +\left(\partial^{2} \Gamma+\Gamma * \partial \Gamma\right) * \partial h+\left(\partial^{3} \Gamma+\partial \Gamma * \partial \Gamma+\Gamma * \partial^{2} \Gamma\right) * h
\end{aligned}$$
where $\partial$ denotes coordinate partial derivatives. If $h$ grows quadratically, then since $g_{N}$ is AF of order 2, we see that
$$\nabla^{4} h=\partial^{4} h+O\left(|x|^{-4}\right) .$$
Since $\left(g_{N}\right)_{i j}=\delta_{i j}+O\left(|x|^{-2}\right)$, it follows that
$$\left(g^{-2}+g * g^{-3}\right) * \nabla^{4} h=S_{0} h+O\left(|x|^{-4}\right),$$
where $S_{0}$ is the linearized operator with respect to the flat metric. Estimating the other terms on the right-hand side of (7.6) in a similar manner, we find
$$S(h)=S_{0} h+O\left(|x|^{-4}\right)$$
as $|x| \rightarrow \infty$. Since $H_{2}$ has quadratic leading term and $S_{0}$ is a fourth-order operator, we clearly have
$$S_{0}\left(H_{2}\right)=0 .$$
Therefore,
$$S\left(H_{2}\right)=O\left(|x|^{-4}\right)$$
as $|x| \rightarrow \infty$. \(\square\)

Next, given $\epsilon>0$, consider
$$S: C_{\epsilon}^{4, \alpha}(N) \rightarrow C_{\epsilon-4}^{0, \alpha}(N) .$$
The cokernel of this mapping is the kernel of
$$S^{*}: C_{-\epsilon}^{4, \alpha}(N) \rightarrow C_{-\epsilon-4}^{0, \alpha}(N),$$
which consists of the decaying elements.
By Theorem 5.1, $\operatorname{Ker}\left(S^{*}\right)$ is 1-dimensional, and spanned by the element
$$o_{1}=\mathcal{K} \omega_{1}+f \cdot g_{N} .$$
Since $\operatorname{Ker}\left(S^{*}\right)$ is nontrivial, this means the map in (7.12) is not surjective, that is, $S\left(C_{\epsilon}^{4, \alpha}\right) \subset C_{\epsilon-4}^{0, \alpha}$ is a proper subset, and the quotient space
$$C_{\epsilon-4}^{0, \alpha} / S\left(C_{\epsilon}^{4, \alpha}\right)$$
is 1 -dimensional. A tensor $h \in C_{\epsilon-4}^{0, \alpha}$ is in the image of $C_{\epsilon}^{4, \alpha}$ under $S$ if and only if it pairs trivially with $\operatorname{Ker}\left(S^{*}\right)$ under the $L^{2}$ pairing. That is
$$h \in S\left(C_{\epsilon}^{4, \alpha}\right) \Longleftrightarrow \int_{N}\left\langle h, o_{1}\right\rangle d V=0 .$$
Since the quotient space is 1 -dimensional, we choose $k_{1}^{(0)} \in C_{\epsilon-4}^{0, \alpha}$ having compact support in $B\left(x_{0}, R_{0}\right)$ (where $x_{0}$ is a basepoint) satisfying
$$\int\left\langle o_{1}, k_{1}^{(0)}\right\rangle d V=1,$$
and we can write
$$C_{\epsilon-4}^{0, \alpha}=S\left(C_{\epsilon}^{4, \alpha}\right) \oplus \mathbb{R} \cdot k_{1}^{(0)} .$$
By averaging over the group, we may assume that $k_{1}^{(0)}$ is invariant under the group action. Therefore, we can write
$$S\left(\left(1-\phi\left(R_{0}^{-1} x\right)\right) H_{2}(x)\right)=S\left(h_{\epsilon}\right)+\lambda k_{1}^{(0)}$$
where $h_{\epsilon} \in C_{\epsilon}^{4, \alpha}$, and $\lambda \in \mathbb{R}$. Again, by averaging over the group, we may assume that $h_{\epsilon}$ is invariant under the group action. Rewriting this as
$$S\left(\left(1-\phi\left(R_{0}^{-1} x\right)\right) H_{2}-h_{\epsilon}\right)=\lambda k_{1}^{(0)}$$
we now define
$$\tilde{H}_{2} \equiv\left(1-\phi\left(R_{0}^{-1} x\right)\right) H_{2}-h_{\epsilon} .$$
Since $h_{\epsilon} \in C_{\epsilon}^{4, \alpha}$, clearly $\tilde{H}_{2}$ has leading term exactly equal to $H_{2}$ as $|x| \rightarrow \infty$. To summarize, we have solved

Proposition 7.2. On $\left(N, g_{N}\right)$, there exists a solution of
$$\begin{aligned}
& S\left(\tilde{H}_{2}\right)=\lambda k_{1}^{(0)} \\
& \tilde{H}_{2}(x)=H_{2}(x)+O^{(4)}\left(|x|^{\epsilon}\right), \text { as }|x| \rightarrow \infty,
\end{aligned}$$
where $k_{1}^{(0)}$ is a tensor with compact support on $\left(N, g_{N}\right)$ satisfying
$$\int_{N}\left\langle o_{1}, k_{1}^{(0)}\right\rangle d V=1$$
Furthermore, $\tilde{H}_{2}$ can be chosen to be invariant under the group action.
7.2. A linear equation on $\left(Z, g_{Z}\right)$. Next we return to the compact metric $\left(Z, g_{Z}\right)$. Recall on $\left(N, g_{N}\right)$, we have an AF-coordinate system satisfying
$$g_{N}=\left(g_{N}\right)_{i j} d x^{i} d x^{j}=\left(\delta_{i j}+H_{-2}(x)_{i j}+O\left(|x|^{-4+\epsilon}\right)_{i j}\right) d x^{i} d x^{j}$$
where
$$H_{-2}(x)=\left(-\frac{1}{3} R_{i k j l}\left(y_{0}\right) \frac{x^{k} x^{l}}{|x|^{4}}+2 A \frac{1}{|x|^{2}} \delta_{i j}\right) d x^{i} d x^{j}$$
is a 2-tensor with components
$$H_{-2}(x)_{i j}=-\frac{1}{3} R_{i k j l}\left(y_{0}\right) \frac{x^{k} x^{l}}{|x|^{4}}+2 A \frac{1}{|x|^{2}} \delta_{i j} .$$
Consider the inverse quadratic tensor
$$H_{-2}(z)=\left(-\frac{1}{3} R_{i k j l}\left(y_{0}\right) \frac{z^{k} z^{l}}{|z|^{4}}+2 A \frac{1}{|z|^{2}} \delta_{i j}\right) d z^{i} d z^{j}$$
Extend this tensor to all of $Z$ by $\phi\left(\left(R^{\prime}\right)^{-1} z\right) H_{-2}(z)$, where $b<R^{\prime}<i n j_{z_{0}}\left(g_{Z}\right)$ is some fixed radius.

We will need the following technical lemma both in this Section, and later in Section 10:

Lemma 7.3. Let $S_{0}$ denote the linearized operator with respect to the flat metric. Then
$$S_{0}\left(H_{-2}\right)=0,$$
where $H_{-2}$ is viewed as a tensor on $\mathbb{R}^{4} \backslash\{0\}$.
Furthermore, if $\left(B_{0}^{t}\right)^{\prime}$ denotes the linearization of the $B^{t}$-tensor at the flat metric, then
$$\left(B_{0}^{t}\right)^{\prime}\left(H_{-2}\right)=0 .$$
Proof. To prove the Lemma we use the expansion (7.24):
$$g_{N}=g_{0}+H_{-2}+O\left(|x|^{-4+\epsilon}\right)$$
where $g_{0}$ is the flat metric. Let $\theta=g_{N}-g_{0}$. Since $g_{N}$ is $B^{t}$-flat,
$$\begin{aligned}
P_{g_{0}}(\theta) & =B^{t}\left(g_{N}\right)+\mathcal{K}_{g_{N}} \delta_{0} \mathcal{K}_{0} \delta_{0} \stackrel{\circ}{\theta} \\
& =\mathcal{K}_{g_{N}} \delta_{0} \mathcal{K}_{0} \delta_{0}^{\circ} \stackrel{\circ}{\theta}
\end{aligned}$$

We can also use the expansion of $P$ at the flat metric $g_{0}$ to write
$$\begin{aligned}
P_{g_{0}}(\theta) & =P_{g_{0}}(0)+S_{0}(\theta)+Q(\theta) \\
& =B^{t}\left(g_{0}\right)+S_{0}(\theta)+Q(\theta) \\
& =S_{0}(\theta)+Q(\theta)
\end{aligned}$$
Combining (7.31) and (7.32) we find
$$S_{0} \theta=\mathcal{K}_{g_{N}} \delta_{0} \mathcal{K}_{0} \delta_{0} \stackrel{\circ}{\theta}-Q(\theta) .$$
Since
$$\theta=H_{-2}+O\left(|x|^{-4+\epsilon}\right)$$
and $S_{0}$ is fourth order,
$$S_{0} \theta=S_{0}\left(H_{-2}\right)+O\left(|x|^{-8+\epsilon}\right),$$
hence
$$S_{0}\left(H_{-2}\right)=\mathcal{K}_{g_{N}} \delta_{0} \mathcal{K}_{0} \delta_{0} \stackrel{\circ}{\theta}-Q(\theta)+O\left(|x|^{-8+\epsilon}\right) .$$
Also, using (3.27) we have
$$Q(\theta)=O\left(|x|^{-8}\right),$$
so that
$$S_{0}\left(H_{-2}\right)=\mathcal{K}_{g_{N}} \delta_{0} \mathcal{K}_{0} \delta_{0} \stackrel{\circ}{\theta}+O\left(|x|^{-8+\epsilon}\right) .$$

It remains to estimate the gauge-fixing operator acting on $\theta$. By (7.26),
$$\stackrel{\circ}{\theta}_{i j}=-\frac{1}{3} W_{i k j l}\left(y_{0}\right) \frac{x^{k} x^{l}}{|x|^{4}}+\frac{R\left(y_{0}\right)}{36}\left\{\frac{x^{i} x^{j}}{|x|^{4}}-\frac{\delta_{i j}}{|x|^{2}}\right\}+O\left(|x|^{-4}\right) .$$
Using the skew-symmetry of the Weyl tensor we find
$$\left(\delta_{0} \stackrel{\circ}{\theta}\right)_{j}=\frac{R\left(y_{0}\right)}{24} \frac{x^{j}}{|x|^{4}}+O\left(|x|^{-5}\right) .$$
We next calculate
$$\delta_{0} \mathcal{K}_{0} \delta_{0} \stackrel{\circ}{\theta}=\square \delta_{0} \stackrel{\circ}{\theta} .$$
It is easy to check that the form
$$\omega=\frac{x^{j}}{|x|^{4}} d x^{j}$$
is harmonic. Therefore, using the formula (5.12) for □ on Euclidean space,
$$\square \omega=\frac{3}{2} d \delta \omega+\delta d \omega=0$$
Consequently,
$$\delta_{0} \mathcal{K}_{0} \delta_{0} \stackrel{\circ}{\theta}=\square \delta_{0} \stackrel{\circ}{\theta}=\square\left(\frac{R\left(y_{0}\right)}{24} \omega+O\left(|x|^{-5}\right)\right)=O\left(|x|^{-7}\right) .$$

It follows that
$$\mathcal{K}_{g_{N}} \delta_{0} \mathcal{K}_{0} \delta_{0} \stackrel{\circ}{\theta}=O\left(|x|^{-8}\right),$$
which, using (7.38), implies
$$S_{0}\left(H_{-2}\right)=O\left(|x|^{-8+\epsilon}\right) .$$
However, since $H_{-2}$ is homogeneous of degree $-2, S_{0}\left(H_{-2}\right)$ must be homogeneous of degree -6. Therefore, (7.44) implies that $S_{0}\left(H_{-2}\right)$ vanishes.

A similar argument (expanding the $B^{t}$-tensor as in Proposition 3.8) gives (7.29). \(\square\)

Proposition 7.4. Let $S$ denote the linearized operator on $Z$, then
$$S\left(\phi\left(\left(R^{\prime}\right)^{-1} z\right) H_{-2}(z)\right)=O\left(|z|^{-4}\right)$$
as $|z| \rightarrow 0$.
Proof. As above, for $|z|$ sufficiently small and any tensor $h$,
$$\begin{aligned}
\nabla^{4} h & =\partial^{4} h+\Gamma * \partial^{3} h+(\partial \Gamma+\Gamma * \Gamma) * \partial^{2} h \\
& +\left(\partial^{2} \Gamma+\Gamma * \partial \Gamma\right) * \partial h+\left(\partial^{3} \Gamma+\partial \Gamma * \partial \Gamma+\Gamma * \partial^{2} \Gamma\right) * h
\end{aligned}$$
where $\partial$ denotes coordinates partial derivatives. If $h$ blows-up inverse quadratically, then since $\left\{z^{i}\right\}$ are Riemannian normal coordinates, we see that
$$\nabla^{4} h=\partial^{4} h+O\left(|z|^{-4}\right) .$$
Arguing as we did in the proof of Proposition 7.1, we find that
$$S(h)=S_{0} h+O\left(|z|^{-4}\right),$$
where $S_{0}$ is the linearized operator with respect to the flat metric. If we take $h=H_{-2}$ in (7.48), then (7.28) of Lemma 7.3 gives
$$S\left(H_{-2}\right)=O\left(|z|^{-4}\right)$$
as $|z| \rightarrow 0$, and the Proposition follows. \(\square\)

Next, for $\epsilon>0$, we have
$$S: C_{-\epsilon}^{4, \alpha}(Z) \rightarrow C_{-\epsilon-4}^{0, \alpha}(Z),$$
with adjoint mapping
$$S^{*}: C_{\epsilon}^{4, \alpha}(Z) \rightarrow C_{\epsilon-4}^{0, \alpha}(Z) .$$
By Theorem 4.1, there is no (invariant) cokernel. Thus there exists $h_{-\epsilon} \in C_{-\epsilon}^{4, \alpha}$ such that
$$S\left(\phi\left(\left(R^{\prime}\right)^{-1} z\right) H_{-2}(z)\right)=S\left(h_{\epsilon}\right),$$
or rather
$$S\left(\phi\left(\left(R^{\prime}\right)^{-1} z\right) H_{-2}(z)-h_{\epsilon}\right)=0 .$$

Averaging over the group, we may assume that $h_{\epsilon}$ is invariant under the group action. We then define
$$\tilde{H}_{-2}(z)=\phi\left(\left(R^{\prime}\right)^{-1} z\right) H_{-2}(z)-h_{\epsilon} .$$
To summarize, we have proved
Proposition 7.5. On $\left(Z, g_{Z}\right)$, there exists a solution $\tilde{H}_{-2}$ of
$$\begin{aligned}
S\left(\tilde{H}_{-2}(z)\right) & =0 \\
\tilde{H}_{-2}(z) & =H_{-2}(z)+O\left(|z|^{-\epsilon}\right), \text { as }|z| \rightarrow 0 .
\end{aligned}$$
Furthermore, $\tilde{H}_{-2}$ can be chosen to be invariant under the group action.
Remark 7.6. From now on, we will fix $\epsilon>0$ small.

\section*{8. Computation of the leading term}

In this section we compute the constant $\lambda$ which arose above in Proposition 7.2. As the title of this section indicates, we will refer to this constant as "the leading term" for reasons which will become clear later in Section 12.

Recall from Proposition 7.2 that $\lambda$ was defined via equation (7.22):
$$S\left(\tilde{H}_{2}\right)=\lambda k_{1}^{(0)} \text { on } N,$$
with
$$\tilde{H}_{2}(x)=H_{2}(x)+O^{(4)}\left(|x|^{\epsilon}\right)$$
as $|x| \rightarrow \infty$, and
$$\left(H_{2}\right)_{i j}=-\frac{1}{3} R_{i k j \ell}\left(z_{0}\right) x^{k} x^{\ell} .$$
Pairing both side of the defining equation for $\lambda$ with the cokernel element $o_{1}$ and integrating gives
$$\left.\lambda=\int_{N} S\left(\tilde{H}_{2}\right), o_{1}\right\rangle d V$$
since
$$\int\left\langle k_{1}^{(0)}, o_{1}\right\rangle d V=1$$

Proposition 8.1. The constant $\lambda$ is given by
$$\lambda=\frac{4}{9} \omega_{3}\left[W_{i k j \ell}\left(y_{0}\right) W_{i k j \ell}\left(z_{0}\right)+W_{i k j \ell}\left(y_{0}\right) W_{i \ell j k}\left(z_{0}\right)\right]+4 t \omega_{3} R\left(z_{0}\right) \operatorname{mass}\left(g_{N}\right),$$
where $\omega_{3}=\operatorname{Vol}\left(S^{3}\right)$.

We prove this formula through a series of lemmas. To begin, let
$$B=\left\{x \in N:|x|<a^{-1}\right\},$$
(where we extend $|x|$ to be defined on all of $N$ by letting it be a constant outside of the AF region of $N$ ), and use (3.15) to write
$$\begin{aligned}
& \int_{B}\left\langle S \tilde{H}_{2}, o_{1}\right\rangle= \\
& \quad \int_{B}\left\langle\Delta^{2}\left(\stackrel{\circ}{\tilde{H}}_{2}\right), o_{1}\right\rangle+\int_{B}\left\langle\mathcal{K}\left[d\left(\mathcal{D}_{2}\left(\tilde{H}_{2}\right)\right)\right], o_{1}\right\rangle+\frac{3}{2} t \int_{B}\left\langle\left[\Delta^{2}\left(\operatorname{tr} \tilde{H}_{2}\right)-\Delta\left(\delta^{2} \tilde{H}_{2}\right)\right] g, o_{1}\right\rangle,
\end{aligned}$$
where $\stackrel{\circ}{T}$ denotes the trace-free part of the symmetric two-tensor $T$.
Lemma 8.2. As $a \rightarrow 0$,
$$\begin{aligned}
\int_{B}\left\langle\Delta^{2} \stackrel{\circ}{\tilde{H}}_{2}, o_{1}\right\rangle=\int_{B} & \left\langle\tilde{H}_{2}, \Delta^{2} \kappa\right\rangle \\
& +\frac{4}{9} \omega_{3}\left[W_{i k j \ell}\left(y_{0}\right) W_{i k j \ell}\left(z_{0}\right)+W_{i k j \ell}\left(y_{0}\right) W_{i \ell j k}\left(z_{0}\right)\right]+o(1)
\end{aligned}$$
Proof. Since $\kappa$ is the trace-free part of $o_{1}$,
$$\int_{B}\left\langle\Delta^{2} \stackrel{\circ}{\tilde{H}}_{2}, o_{1}\right\rangle=\int_{B}\left\langle\Delta^{2} \stackrel{\circ}{\tilde{H}}_{2}, \kappa\right\rangle .$$
Integrating by parts,
$$\begin{aligned}
\int_{B}\left\langle\Delta^{2} \stackrel{\circ}{\tilde{H}}_{2}, \kappa\right\rangle= & \int_{B}\left\langle\stackrel{\circ}{\tilde{H}}_{2}, \Delta^{2} \kappa\right\rangle+\oint_{\partial B}\left\langle\nabla_{N}\left(\Delta \stackrel{\circ}{\tilde{H}}_{2}\right), \kappa\right\rangle-\oint_{\partial B}\left\langle\Delta \stackrel{\circ}{\tilde{H}}_{2}, \nabla_{N} \kappa\right\rangle \\
& +\oint_{\partial B}\left\langle\nabla_{N} \stackrel{\circ}{\tilde{H}}_{2}, \Delta \kappa\right\rangle-\oint_{\partial B}\left\langle\stackrel{\circ}{\tilde{H}}_{2}, \nabla_{N}(\Delta \kappa)\right\rangle,
\end{aligned}$$
where $N$ is the outward unit normal to $N$. All the boundary integrals in (8.9) are with respect to the approximate metric $g$. To estimate each boundary term we use the fact that on $\partial B$, the metric and Christoffel symbols satisfy
$$\begin{aligned}
g & =\delta+O\left(a^{2}\right), \\
\Gamma & =O\left(a^{3}\right), \\
\partial \Gamma & =O\left(a^{4}\right),
\end{aligned}$$
where $\delta$ denotes the flat metric. For a symmetric 2-tensor $T=T_{i j}$,
$$\Delta T=g^{\alpha \beta} \nabla_{\alpha} \nabla_{\beta} T,$$
and
$$\nabla_{\alpha} \nabla_{\beta} T=\partial_{\alpha} \partial_{\beta} T+\Gamma * \partial T+\partial \Gamma * T+\Gamma * \Gamma * T,$$
hence
$$\Delta T_{i j}=\Delta_{0} T_{i j}+O\left(a^{2}\right) * \partial^{2} T+O\left(a^{3}\right) * \partial T+O\left(a^{4}\right) * T,$$
where $\Delta_{0}$ denotes the flat Laplacian.
Taking $T=\stackrel{\circ}{\tilde{H}}_{2}$ and using (8.2) we first note
$$\begin{aligned}
\left(\stackrel{\circ}{\tilde{H}}_{2}\right)_{i j} & =\left(\tilde{H}_{2}\right)_{i j}-\frac{1}{4}\left[g^{\alpha \beta}\left(\tilde{H}_{2}\right)_{\alpha \beta}\right] g_{i j} \\
& =-\frac{1}{3} R_{i k j \ell}\left(z_{0}\right) x^{k} x^{\ell}+\frac{1}{12} R_{k \ell}\left(z_{0}\right) x^{k} x^{\ell} \delta_{i j}+O\left(|x|^{\epsilon}\right) .
\end{aligned}$$
Therefore,
$$\begin{aligned}
\partial_{\alpha}\left(\stackrel{\circ}{\tilde{H}}_{2}\right)_{i j} & =-\frac{1}{3} R_{i \alpha j \ell}\left(z_{0}\right) x^{\ell}-\frac{1}{3} R_{i k j \alpha}\left(z_{0}\right) x^{k}+\frac{1}{6} R_{\alpha k}\left(z_{0}\right) x^{k} \delta_{i j}+O\left(|x|^{\epsilon-1}\right), \\
\partial_{\alpha} \partial_{\beta}\left(\stackrel{\circ}{\tilde{H}_{2}}\right)_{i j} & =-\frac{1}{3} R_{i \alpha j \beta}\left(z_{0}\right)-\frac{1}{3} R_{i \beta j \alpha}\left(z_{0}\right)+\frac{1}{6} R_{\alpha \beta}\left(z_{0}\right) \delta_{i j}+O\left(|x|^{\epsilon-2}\right),
\end{aligned}$$
hence
$$\left(\Delta \stackrel{\circ}{\tilde{H}}_{2}\right)_{i j}=-\frac{2}{3}\left[R_{i j}\left(z_{0}\right)-\frac{1}{4} R\left(z_{0}\right) \delta_{i j}\right]+O\left(|x|^{\epsilon-2}\right) .$$
Assuming $\left(Z, g_{Z}\right)$ is Einstein, then
$$R_{i j}\left(z_{0}\right)-\frac{1}{4} R\left(z_{0}\right) \delta_{i j}=0 .$$
It follows that
$$\begin{aligned}
\left(\Delta \stackrel{\circ}{\tilde{H}}_{2}\right)_{i j} & =O\left(|x|^{\epsilon-2}\right), \\
\nabla_{N}\left(\Delta \stackrel{\circ}{\tilde{H}}_{2}\right)_{i j} & =O\left(|x|^{\epsilon-3}\right),
\end{aligned}$$
as $|x| \rightarrow \infty$.
By (6.4), on $\partial B$ we have
$$\begin{aligned}
|\kappa| & =O\left(a^{2}\right), \\
|\nabla \kappa| & =O\left(a^{3}\right) .
\end{aligned}$$
Using these estimates along with those of (8.17) we find
$$\begin{aligned}
\left|\oint_{\partial B}\left\langle\nabla_{N}\left(\Delta \stackrel{\circ}{\tilde{H}}_{2}\right), \kappa\right\rangle\right| & =O\left(a^{2-\epsilon}\right), \\
\left|\oint_{\partial B}\left\langle\Delta \stackrel{\circ}{\tilde{H}}_{2}, \nabla_{N} \kappa\right\rangle\right| & =O\left(a^{2-\epsilon}\right) .
\end{aligned}$$

Next, we take $T=\kappa_{i j}$. Using (6.4),
$$\begin{aligned}
\partial_{\alpha} \kappa_{i j}= & \frac{2}{3} W_{i \alpha j \ell}\left(y_{0}\right) \frac{x^{\ell}}{|x|^{4}}+\frac{2}{3} W_{i k j \alpha}\left(y_{0}\right) \frac{x^{k}}{|x|^{4}}-\frac{8}{3} W_{i k j \ell}\left(y_{0}\right) \frac{x^{k} x^{\ell} x^{\alpha}}{|x|^{6}}+O\left(a^{4}\right), \\
\partial_{\alpha} \partial_{\beta} \kappa_{i j}= & \frac{2}{3} W_{i \alpha j \beta}\left(y_{0}\right) \frac{1}{|x|^{4}}+\frac{2}{3} W_{i \beta j \alpha}\left(y_{0}\right) \frac{1}{|x|^{4}}+16 W_{i k j \ell}\left(y_{0}\right) \frac{x^{k} x^{\ell} x^{\alpha} x^{\beta}}{|x|^{8}} \\
& -\frac{8}{3} W_{i \alpha j \ell}\left(y_{0}\right) \frac{x^{\ell} x^{\beta}}{|x|^{6}}-\frac{8}{3} W_{i k j \alpha}\left(y_{0}\right) \frac{x^{k} x^{\beta}}{|x|^{6}}-\frac{8}{3} W_{i \beta j \ell}\left(y_{0}\right) \frac{x^{\ell} x^{\alpha}}{|x|^{6}} \\
& -\frac{8}{3} W_{i k j \beta}\left(y_{0}\right) \frac{x^{k} x^{\alpha}}{|x|^{6}}-\frac{8}{3} W_{i k j \ell}\left(y_{0}\right) \frac{x^{k} x^{\ell}}{|x|^{6}} \delta_{\alpha \beta}+O\left(a^{5}\right) .
\end{aligned}$$
Therefore,
$$\begin{aligned}
\Delta \kappa_{i j} & =-\frac{16}{3} W_{i k j \ell}\left(y_{0}\right) \frac{x^{k} x^{\ell}}{|x|^{6}}+O\left(a^{5}\right) \\
& =-\frac{8}{|x|^{2}} \kappa_{i j}+O\left(a^{5}\right) .
\end{aligned}$$

On $\partial B$,
$$N^{\alpha}=\frac{x^{\alpha}}{|x|}+O\left(a^{2}\right)$$
hence
$$\nabla_{N} T_{i j}=\frac{x^{\alpha}}{|x|} \partial_{\alpha} T_{i j}+O\left(a^{2}\right) * \partial T+O\left(a^{3}\right) * T .$$
From (8.14),(8.20), and (8.23) (or, by reasons of homogeneity) we conclude
$$\begin{aligned}
\nabla_{N}\left(\stackrel{\circ}{\tilde{H}}_{2}\right)_{i j} & =-\frac{2}{3} R_{i k j \ell}\left(z_{0}\right) \frac{x^{k} x^{\ell}}{|x|}+\frac{1}{6} R_{k \ell}\left(z_{0}\right) \frac{x^{k} x^{\ell}}{|x|} \delta_{i j}+O\left(a^{1-\epsilon}\right) \\
& =\frac{2}{|x|}\left(\stackrel{\circ}{\tilde{H}}_{2}\right)_{i j}+O\left(a^{1-\epsilon}\right), \\
\nabla_{N}(\Delta \kappa)_{i j} & =\frac{64}{3} W_{i k j \ell}\left(y_{0}\right) \frac{x^{k} x^{\ell}}{|x|^{7}}+O\left(a^{7}\right) \\
& =\frac{32}{|x|^{3}} \kappa_{i j}+O\left(a^{7}\right) .
\end{aligned}$$
It follows that
$$\left\langle\nabla_{N} \stackrel{\circ}{\tilde{H}}_{2}, \Delta \kappa\right\rangle-\left\langle\stackrel{\circ}{\tilde{H}}_{2}, \nabla_{N}(\Delta \kappa)\right\rangle=-48 \frac{1}{|x|^{3}}\left\langle\stackrel{\circ}{\tilde{H}}_{2}, \kappa\right\rangle+O\left(a^{4}\right),$$
hence
$$\oint_{\partial B}\left\langle\nabla_{N} \stackrel{\circ}{\tilde{H}}_{2}, \Delta \kappa\right\rangle-\left\langle\stackrel{\circ}{\tilde{H}}_{2}, \nabla_{N}(\Delta \kappa)\right\rangle=\frac{32}{3} \int_{|\xi|=1} W_{i k j \ell}\left(y_{0}\right) R_{i \alpha j \beta}\left(z_{0}\right) \xi^{k} \xi^{\ell} \xi^{\alpha} \xi^{\beta} d S+O(a) .$$

If we decompose the curvature tensor of $R_{i \alpha j \beta}\left(z_{0}\right)$ (again assuming $\left(Z, g_{Z}\right)$ is Einstein),
$$R_{i \alpha j \beta}\left(z_{0}\right)=W_{i \alpha j \beta}\left(z_{0}\right)+\frac{1}{12} R\left(z_{0}\right)\left(\delta_{i j} \delta_{\alpha \beta}-\delta_{i \beta} \delta_{j \alpha}\right) .$$
Therefore, the integrand in (8.26) can be written
$$W_{i k j \ell}\left(y_{0}\right) R_{i \alpha j \beta}\left(z_{0}\right)=W_{i k j \ell}\left(y_{0}\right) W_{i \alpha j \beta}\left(z_{0}\right)-\frac{1}{12} R\left(z_{0}\right) W_{\beta k \alpha \ell}\left(y_{0}\right) .$$
hence
$$\begin{aligned}
\int_{|\xi|=1} W_{i k j \ell}\left(y_{0}\right) R_{i \alpha j \beta}\left(z_{0}\right) \xi^{k} \xi^{\ell} \xi^{\alpha} \xi^{\beta} d S= & \int_{|\xi|=1} W_{i k j \ell}\left(y_{0}\right) W_{i \alpha j \beta}\left(z_{0}\right) \xi^{k} \xi^{\ell} \xi^{\alpha} \xi^{\beta} d S \\
& -\frac{1}{12} R\left(z_{0}\right) \int_{|\xi|=1} W_{\beta k \alpha \ell}\left(y_{0}\right) \xi^{k} \xi^{\ell} \xi^{\alpha} \xi^{\beta} d S
\end{aligned}$$
The last integral vanishes by skew-symmetry of the Weyl tensor; therefore,
$$\oint_{\partial B}\left\langle\nabla_{N} \stackrel{\circ}{\tilde{H}}_{2}, \Delta \kappa\right\rangle-\left\langle\stackrel{\circ}{\tilde{H}}_{2}, \nabla_{N}(\Delta \kappa)\right\rangle=\frac{32}{3} \int_{|\xi|=1} W_{i k j \ell}\left(y_{0}\right) W_{i \alpha j \beta}\left(z_{0}\right) \xi^{k} \xi^{\ell} \xi^{\alpha} \xi^{\beta} d S+O(a) .$$

We now use the identity (see [Bre08])
$$\int_{|\xi|=1} \xi^{k} \xi^{\ell} \xi^{\alpha} \xi^{\beta} d S=\frac{\omega_{3}}{24}\left(\delta_{k \ell} \delta_{\alpha \beta}+\delta_{k \alpha} \delta_{\beta \ell}+\delta_{k \beta} \delta_{\alpha \ell}\right)$$
Plugging this into (8.28), we obtain
$$\begin{aligned}
\oint_{\partial B}\left\langle\nabla_{N} \stackrel{\circ}{\tilde{H}}_{2}, \Delta \kappa\right\rangle-\left\langle\stackrel{\circ}{\tilde{H}}_{2}, \nabla_{N}(\Delta \kappa)\right\rangle= & \frac{4}{9} \omega_{3}\left[W_{i k j \ell}\left(y_{0}\right) W_{i k j \ell}\left(z_{0}\right)+W_{i k j \ell}\left(y_{0}\right) W_{i \ell j k}\left(z_{0}\right)\right] \\
& +O(a),
\end{aligned}$$
which proves the Lemma. \(\square\)

Lemma 8.3. As a → 0,
$$\int_{B}\left\langle\mathcal{K}\left[d\left(\mathcal{D}_{2}\left(\tilde{H}_{2}\right)\right], o_{1}\right\rangle=O\left(a^{2-\epsilon}\right) .\right.$$
Proof. Since $\mathcal{K}[\cdot]$ is trace-free, we can rewrite the integrand in (8.31) as
$$\int_{B}\left\langle\mathcal{K}\left[d\left(\mathcal{D}_{2}\left(\tilde{H}_{2}\right)\right], o_{1}\right\rangle=\int_{B}\left\langle\mathcal{K}\left[d\left(\mathcal{D}_{2}\left(\tilde{H}_{2}\right)\right], \kappa\right\rangle .\right.\right.$$

Integrating by parts and using the fact that $\kappa$ is divergence-free, we get
$$\begin{aligned}
\int_{B}\left\langle\mathcal{K}\left[d\left(\mathcal{D}_{2}\left(\tilde{H}_{2}\right)\right], \kappa\right\rangle=\right. & -2 \int_{B}\left\langle d\left(\mathcal{D}_{2}\left(\tilde{H}_{2}\right), \delta \kappa\right\rangle\right. \\
& +2 \oint_{\partial B} \kappa\left(d\left(\mathcal{D}_{2}\left(\tilde{H}_{2}\right)\right), N\right) \\
= & 2 \oint_{\partial B} \kappa\left(d\left(\mathcal{D}_{2}\left(\tilde{H}_{2}\right)\right), N\right)
\end{aligned}$$
Using (8.12) and computing as we did in the proof of Lemma 8.2, on $\partial B$ we find
$$\begin{aligned}
\delta^{2} \tilde{H}_{2} & =\frac{1}{3} R\left(z_{0}\right)+O\left(a^{2-\epsilon}\right) \\
\Delta\left(\operatorname{tr} \tilde{H}_{2}\right) & =-\frac{2}{3} R\left(z_{0}\right)+O\left(a^{2-\epsilon}\right) .
\end{aligned}$$
Therefore,
$$\begin{aligned}
\mathcal{D}_{2}\left(\tilde{H}_{2}\right) & =\left(t+\frac{5}{12}\right) R\left(z_{0}\right)+O\left(a^{2-\epsilon}\right), \\
d\left(\mathcal{D}_{2}\left(\tilde{H}_{2}\right)\right) & =O\left(a^{3-\epsilon}\right) .
\end{aligned}$$
Since $\kappa=O\left(a^{2}\right)$ on $\partial B$, we see that the boundary term in (8.32) is $O\left(a^{2-\epsilon}\right)$, which proves the Lemma. \(\square\)

Lemma 8.4. As $a \rightarrow 0$,
$$\begin{aligned}
\frac{3}{2} t \int_{B}\left\langle\left[\Delta^{2}\left(\operatorname{tr} \tilde{H}_{2}\right)-\Delta\left(\delta^{2} \tilde{H}_{2}\right)\right] g, o_{1}\right\rangle=\int_{B} & \left\langle\tilde{H}_{2}, 6 t\left[\left(\Delta^{2} f\right) g-\nabla^{2}(\Delta f)\right]\right\rangle \\
& +4 t\left(12 A-\frac{R\left(y_{0}\right)}{12}\right) \omega_{3} R\left(z_{0}\right)+o(1)
\end{aligned}$$
Proof. Since $o_{1}=\kappa+f g$ with $\kappa$ trace-free, we have
$$\begin{aligned}
\frac{3}{2} t \int_{B}\left\langle\left[\Delta^{2}\left(\operatorname{tr} \tilde{H}_{2}\right)-\Delta\left(\delta^{2} \tilde{H}_{2}\right)\right] g, o_{1}\right\rangle & =\frac{3}{2} t \int_{B}\left\langle\left[\Delta^{2}\left(\operatorname{tr} \tilde{H}_{2}\right)-\Delta\left(\delta^{2} \tilde{H}_{2}\right)\right] g, \kappa+f g\right\rangle \\
& =\frac{3}{2} t \int_{B}\left\langle\left[\Delta^{2}\left(\operatorname{tr} \tilde{H}_{2}\right)-\Delta\left(\delta^{2} \tilde{H}_{2}\right)\right] g, f g\right\rangle \\
& =6 t \int_{B}\left[\Delta^{2}\left(\operatorname{tr} \tilde{H}_{2}\right)-\Delta\left(\delta^{2} \tilde{H}_{2}\right)\right] f .
\end{aligned}$$

Integrating by parts, we find
$$\begin{aligned}
\int_{B}\left[\Delta^{2}\left(\operatorname{tr} \tilde{H}_{2}\right)\right. & \left.-\Delta\left(\delta^{2} \tilde{H}_{2}\right)\right] f=\int_{B}\left\langle\tilde{H}_{2},\left(\Delta^{2} f\right) g-\nabla^{2}(\Delta f)\right\rangle \\
& +\oint_{\partial B} f \frac{\partial}{\partial N} \Delta\left(\operatorname{tr} \tilde{H}_{2}\right)-\oint_{\partial B} \Delta\left(\operatorname{tr} \tilde{H}_{2}\right) \frac{\partial}{\partial N} f+\oint_{\partial B} \frac{\partial}{\partial N}\left(\operatorname{tr} \tilde{H}_{2}\right) \Delta f \\
& -\oint_{\partial B}\left(\operatorname{tr} \tilde{H}_{2}\right) \frac{\partial}{\partial N}(\Delta f)+\oint_{\partial B} \tilde{H}_{2}(N, \nabla(\Delta f))-\oint_{\partial B}(\Delta f)\left\langle\delta \tilde{H}_{2}, N\right\rangle \\
& +\oint_{\partial B} \frac{\partial}{\partial N} f\left(\delta^{2} \tilde{H}_{2}\right)-\oint_{\partial B} f \frac{\partial}{\partial N}\left(\delta^{2} \tilde{H}_{2}\right) \\
& =\int_{B}\left\langle\tilde{H}_{2},\left(\Delta^{2} f\right) g-\nabla^{2}(\Delta f)\right\rangle+I_{1}+\cdots+I_{8} .
\end{aligned}$$

By Theorem 5.1, on $\partial B$
$$\begin{aligned}
\Delta f & =-\frac{1}{3}\left\langle\text { Ric }, o_{1}\right\rangle=O\left(a^{6}\right), \\
\frac{\partial}{\partial N}(\Delta f) & =-\frac{1}{3}\left\langle\nabla_{N} \text { Ric, } o_{1}\right\rangle-\frac{1}{3}\left\langle\text { Ric }, \nabla_{N} o_{1}\right\rangle=O\left(a^{7}\right) .
\end{aligned}$$
Also, from the preceding lemma (see (8.33))
$$\begin{aligned}
\operatorname{tr} \tilde{H}_{2} & =-\frac{1}{3} R_{k \ell}\left(z_{0}\right) x^{k} x^{\ell}+O\left(a^{-\epsilon}\right)=O\left(a^{-2}\right), \\
\frac{\partial}{\partial N}\left(\operatorname{tr} \tilde{H}_{2}\right) & =-\frac{2}{3} R_{k \ell}\left(z_{0}\right) \frac{x^{k} x^{\ell}}{|x|}+O\left(a^{1-\epsilon}\right)=O\left(a^{-1}\right), \\
\delta^{2} \tilde{H}_{2} & =\frac{1}{3} R\left(z_{0}\right)+O\left(a^{2-\epsilon}\right)=O(1), \\
\Delta\left(\operatorname{tr} \tilde{H}_{2}\right) & =-\frac{2}{3} R\left(z_{0}\right)+O\left(a^{2-\epsilon}\right)=O(1) \\
\frac{\partial}{\partial N}\left(\delta^{2} \tilde{H}_{2}\right) & =O\left(a^{3-\epsilon}\right), \\
\frac{\partial}{\partial N}\left(\Delta\left(\operatorname{tr} \tilde{H}_{2}\right)\right) & =O\left(a^{3-\epsilon}\right) .
\end{aligned}$$

Therefore,
$$\begin{aligned}
I_{1} & =\oint_{\partial B} f \frac{\partial}{\partial N} \Delta\left(\operatorname{tr} \tilde{H}_{2}\right)=O\left(a^{2-\epsilon}\right) \\
I_{3} & =\oint_{\partial B} \frac{\partial}{\partial N}\left(\operatorname{tr} \tilde{H}_{2}\right) \Delta f=O\left(a^{2}\right), \\
I_{4} & =-\oint_{\partial B}\left(\operatorname{tr} \tilde{H}_{2}\right) \frac{\partial}{\partial N}(\Delta f)=O\left(a^{2}\right), \\
I_{5} & =\oint_{\partial B} \tilde{H}_{2}(N, \nabla(\Delta f))=O\left(a^{2}\right), \\
I_{6} & =-\oint_{\partial B}(\Delta f)\left\langle\delta \tilde{H}_{2}, N\right\rangle=O\left(a^{2}\right), \\
I_{8} & =-\oint_{\partial B} f \frac{\partial}{\partial N}\left(\delta^{2} \tilde{H}_{2}\right)=O\left(a^{2-\epsilon}\right) .
\end{aligned}$$
Therefore, it remains to calculate $I_{2}$ and $I_{7}$.
First, using (8.38) we have
$$\begin{aligned}
I_{2}+I_{7} & =\oint_{\partial B}\left[\delta^{2} \tilde{H}_{2}-\Delta\left(\operatorname{tr} \tilde{H}_{2}\right)\right] \frac{\partial}{\partial N} f \\
& =\oint_{\partial B}\left[R\left(z_{0}\right)+O\left(a^{2-\epsilon}\right)\right] \frac{\partial}{\partial N} f \\
& =R\left(z_{0}\right) \oint_{\partial B} \frac{\partial}{\partial N} f+O\left(a^{2-\epsilon}\right) \quad(\text { by (5.6) }) \\
& =R\left(z_{0}\right) \int_{B} \Delta f+O\left(a^{2-\epsilon}\right) \quad \text { (by the divergence theorem) } \\
& =-\frac{1}{3} R\left(z_{0}\right) \int_{B}\langle\text { Ric }, \kappa\rangle+O\left(a^{2-\epsilon}\right) \quad \text { (by (5.5)). }
\end{aligned}$$
Using the fact that $\kappa=\mathcal{K}\left[\omega_{1}\right]$, we can integrate by parts to obtain
$$\begin{aligned}
\int_{B}\langle\text { Ric }, \kappa\rangle & =\int_{B}\left\langle\text { Ric }, \mathcal{K}\left[\omega_{1}\right]\right\rangle \\
& =2 \int_{B} R_{i j} \nabla^{i} \omega_{1}^{j} \\
& =-2 \int_{B} \nabla^{i} R_{i j} \omega_{1}^{j}+2 \oint_{\partial B} R_{i j} N^{i} \omega_{1}^{j}
\end{aligned}$$
Using the second Bianchi identity and the fact that the scalar curvature is zero, the solid integral above vanishes and we conclude
$$I_{2}+I_{7}=-\frac{2}{3} R\left(z_{0}\right) \oint_{\partial B} \operatorname{Ric}\left(N, \omega_{1}\right)+O\left(a^{2-\epsilon}\right) .$$

By (5.6) and (8.22),
$$\operatorname{Ric}\left(N, \omega_{1}\right)=R_{i j} \frac{x^{i} x^{j}}{|x|}+O\left(|x|^{-5}\right) .$$

Proposition 8.5. As $|x| \rightarrow \infty$,
$$\begin{aligned}
R_{i j}= & -\frac{4}{3} W_{i k j \ell}\left(y_{0}\right) \frac{x^{k} x^{\ell}}{|x|^{6}}-\frac{1}{36} R\left(y_{0}\right) \frac{1}{|x|^{4}} \delta_{i j}+\frac{1}{9} R_{\left(y_{0}\right)} \frac{x^{i} x^{j}}{|x|^{6}} \\
& -\frac{16 A}{|x|^{6}} x^{i} x^{j}+\frac{4 A}{|x|^{4}} \delta_{i j}+O\left(|x|^{-5}\right)
\end{aligned}$$
Proof. This is proved in Appendix A. \(\square\)

Assuming the proposition, we see that
$$R_{i j} \frac{x^{i} x^{j}}{|x|}=\frac{1}{12} R\left(y_{0}\right) \frac{1}{|x|^{3}}-\frac{12 A}{|x|^{3}}+O\left(|x|^{-4}\right) .$$
Therefore,
$$\begin{aligned}
I_{2}+I_{7} & =-\frac{2}{3} R\left(z_{0}\right) \oint_{\partial B} \operatorname{Ric}\left(N, \omega_{1}\right)+O\left(a^{2-\epsilon}\right) \\
& =-\frac{2}{3} R\left(z_{0}\right)\left[\frac{1}{12} R\left(y_{0}\right)-12 A\right] \oint_{\partial B} \frac{1}{|x|^{3}}+O(a) \\
& =-\frac{2}{3} \omega_{3} R\left(z_{0}\right)\left[\frac{1}{12} R\left(y_{0}\right)-12 A\right]+O(a) .
\end{aligned}$$
Plugging this into (8.35) and (8.36), we arrive at (8.34). \(\square\)

Combining Lemmas 8.2, 8.3, and 8.4, and using (8.7), we have
$$\begin{aligned}
\int_{B}\left\langle S \tilde{H}_{2}, o_{1}\right\rangle= & \int_{B}\left\langle\tilde{H}_{2}, \Delta^{2} \kappa+6 t\left[\left(\Delta^{2} f\right) g-\nabla^{2}(\Delta f)\right]\right\rangle \\
& +\frac{4}{9} \omega_{3}\left[W_{i k j \ell}\left(y_{0}\right) W_{i k j \ell}\left(z_{0}\right)+W_{i k j \ell}\left(y_{0}\right) W_{i \ell j k}\left(z_{0}\right)\right] \\
& +4 t \omega_{3} R\left(z_{0}\right)\left\{12 A-\frac{1}{12} R\left(y_{0}\right)\right\}+o(1) .
\end{aligned}$$
By Proposition 2.5, the quantity is braces is exactly the mass of the AF space. Proposition 8.1 then follows from the next Lemma:

Lemma 8.6. The cokernel element $o_{1}$ satisfies
$$0=S\left(o_{1}\right)=\Delta^{2} \kappa+6 t\left[\left(\Delta^{2} f\right) g-\nabla^{2}(\Delta f)\right]+O\left(|x|^{-8}\right) .$$
Proof. By the formula in (3.15), we have
$$S o_{1}=\Delta^{2}\left[o_{1}-\frac{1}{4}\left(\operatorname{tr} o_{1}\right) g\right]+\mathcal{K}\left[d\left(\mathcal{D}_{2}\left(o_{1}\right)\right)\right]+\frac{3}{2} t\left[\Delta^{2}\left(\operatorname{tr} o_{1}\right)-\Delta\left(\delta^{2} o_{1}\right)\right] g+\cdots$$

Using the properties of $o_{1}$ in Theorem 5.1, we have
$$\begin{aligned}
o_{1}-\frac{1}{4}\left(\operatorname{tr} o_{1}\right) g & =\kappa, \\
\operatorname{tr} o_{1} & =4 f, \\
\delta^{2} o_{1} & =\Delta f, \\
\Delta\left(\operatorname{tr} o_{1}\right) & =4 \Delta f .
\end{aligned}$$
It follows that
$$\begin{aligned}
\mathcal{D}_{2}\left(o_{1}\right) & =\left(t+\frac{5}{6}\right) \delta^{2} o_{1}-\left(t+\frac{5}{24}\right) \Delta\left(\operatorname{tr} o_{1}\right) \\
& =-3 t \Delta f
\end{aligned}$$
and
$$\begin{aligned}
\mathcal{K}\left[d\left(\mathcal{D}_{2}\left(o_{1}\right)\right)\right] & =-3 t \mathcal{K}[d(\Delta f)] \\
& =-6 t \nabla^{2}(\Delta f)+\frac{3}{2} t\left(\Delta^{2} f\right) g
\end{aligned}$$
Therefore,
$$\begin{aligned}
S o_{1} & =\Delta^{2} \kappa+\mathcal{K}\left[d\left(\mathcal{D}_{2}\left(o_{1}\right)\right)\right]+\frac{9}{2} t\left(\Delta^{2} f\right) g+\cdots \\
& =\Delta^{2} \kappa-6 t \nabla^{2}(\Delta f)+\frac{3}{2} t\left(\Delta^{2} f\right) g+\frac{9}{2} t\left(\Delta^{2} f\right) g+\cdots \\
& =\Delta^{2} \kappa+6 t\left[\left(\Delta^{2} f\right) g-\nabla^{2}(\Delta f)\right]+\cdots
\end{aligned}$$
as claimed. \(\square\)

\section*{9. NaïVe approximate metric}

Let ( $Z, g_{Z}$ ) be a compact $B^{t}$-flat manifold. In our application, ( $Z, g_{Z}$ ) will be taken to be either $\mathbb{C P}^{2}$ with the Fubini-Study metric, or $S^{2} \times S^{2}$ with the product metric, with the coordinate systems described in Subsections 2.1 and 2.3.

We let $z_{0}$ denote the base point, which is $[1,0,0]$ in the case of $\mathbb{C P}^{2}$, or $(n, n)$ in the case of $S^{2} \times S^{2}$. As seen above, we have a Riemannian normal coordinate system $\left\{z^{i}\right\}, i=1 \ldots 4$, satisfying
$$g_{Z}=d z^{2}+\eta_{Z}(z),$$
where $\eta_{Z}$ has the expansion $\eta_{Z}=\left(\eta_{Z}(z)\right)_{i j} d z^{i} d z^{j}$ with
$$\left(\eta_{Z}(z)\right)_{i j}=-\frac{1}{3} R_{i k j l}\left(z_{0}\right) z^{k} z^{l}+O\left(|z|^{4}\right)$$
as $|z| \rightarrow 0$.
Furthermore, in the case of $\mathbb{C P}^{2}$ the metric is invariant under the standard linear action of $U(2)$ in the $\{z\}$-coordinates, and in the case of $S^{2} \times S^{2}$ the metric is invariant under the standard diagonal torus action, and also invariant under the diagonal symmetry, both in the $\{z\}$-coordinates.

Next, let $\left(N, g_{N}\right)$ be a $B^{t}$-flat AF space of order 2. In our application $\left(N, g_{N}\right)$ will be taken to the either the Burns metric or Green's function metric of the product metric with AF coordinate system as described in Subsections 2.2 and 2.4. The Green's function here is with respect to the basepoint which we will denote as $y_{0}$, which is [1, 0, 0] in the case of $\mathbb{C P}^{2}$, or either point $(n, n)$ of $S^{2} \times S^{2}$.

We denote the AF coordinates as $\left\{x^{i}\right\}, i=1 \ldots 4$, and write
$$g_{N}=d x^{2}+\eta_{N},$$
where the tensor $\eta_{N}$ admits the expansion
$$\left(\eta_{N}\right)_{i j}(x)=-\frac{1}{3} R_{i k j l}\left(y_{0}\right) \frac{x^{k} x^{l}}{|x|^{4}}+2 A \frac{1}{|x|^{2}} \delta_{i j}+O\left(|x|^{-4+\epsilon}\right)$$
as $|x| \rightarrow \infty$.
In the case of the Burns metric, the metric is invariant under the standard linear action of $U(2)$ in the $\{x\}$-coordinates, and in the case of the Green's function metric on $S^{2} \times S^{2}$, the metric is invariant under the standard diagonal torus action, and also invariant under the diagonal symmetry, both in the $\{x\}$-coordinates.

Let $\phi$ be the cutoff function defined in (7.4):
$$\phi(t)= \begin{cases}1 & t \leq 1 \\ 0 & t \geq 2 .\end{cases}$$