---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: [1909.12957] Noncollapsed degeneration of Einstein 4-manifolds, I]

Proposition 5 For all $n \in \mathbb{N}$ and $0<r_{0}<\frac{1}{6}$, there exists $C>0$ and $0<\epsilon<\frac{r_{0}}{C}$ such that for any hypersurface $\Sigma$ diffeomorphic to $\mathbb{S}^{n-1} / \Gamma$, for $\Gamma \neq\{\mathrm{Id}\}$, of a manifold $(M, g)$ satisfying:
\begin{itemize}
\item[(1)] the normal injectivity radius of $\Sigma$ and the injectivity radius of the points of $\Sigma$ in $M$ are bounded below by $3 r_{0}$,
\item[(2)] $\left\|A^{\Sigma}-g^{\Sigma}\right\|_{C^{\alpha}\left(g^{\Sigma}\right)} \leqslant \epsilon$,
\item[(3)] on the annulus $\left\{x, d_{g}^{M}(x, \Sigma)<3 r_{0}\right\}$, we have $\|\operatorname{Rm}(g)\|_{C^{2}(g)}<\epsilon$,
\end{itemize}

Then, there exists a unique function $w$ satisfying $\|w\|_{C^{2, \alpha}\left(g^{\Sigma}\right)} \leqslant C \epsilon$ and such that we have
$$H^{\Sigma(w)} \equiv n-1,$$
where we denoted $\Sigma(w):=\left\{\gamma_{x}(w(x)), x \in \Sigma\right\}$, where $\gamma_{x}$ is the geodesic with $\gamma_{x}(0)=x$, and $\gamma_{x}^{\prime}(0)$ is the unit outwards normal to $\Sigma$. We moreover have the following control,
$$\|w\|_{C^{2, \alpha}\left(g^{\Sigma}\right)} \leqslant C\left\|H^{\Sigma}-(n-1)\right\|_{C^{\alpha}\left(g^{\Sigma}\right)} .$$

Remark 9 By adapting the arguments of Section 3, we know that a hypersurface satisfying the assumptions of Proposition 5 is arbitrarily close (up to a diffeomorphism) in the $C^{1, \alpha}$-topology to the round $\mathbb{S}^{n-1} / \Gamma$.

Remark 10 Recall that we defined our Hölder norms at the scale of the injectivity radius, see Definition 2.1. In our applications, the controls on the injectivity radius will be consequences of Lemma 2.2, and the different curvature controls will be consequences of the previous section.

In general, the construction of spheres with constant mean curvature can be tricky (see for example [Ye96, PX09]) because it is achieved by constructing a right-inverse for the operator $\Delta_{\mathbb{S}^{n-1}}+(n-1)$, where $\Delta_{\mathbb{S}^{n-1}}$ is the Laplace-Beltrami operator (with nonpositive eigenvalues) which is not invertible. In our case, our hypersurfaces are not close to $\mathbb{S}^{n-1}$, but to $\mathbb{S}^{n-1} / \Gamma$ for $\Gamma \neq\{\mathrm{Id}\}$. The crucial difference it makes is that $-(n-1)$ is not an eigenvalue anymore (see [CEV17] for the use of the same remark in the context of asymptotically conical manifolds). Indeed, the eigenfunctions with eigenvalue $-(n-1)$ are the restrictions of nonzero linear functions of $\mathbb{R}^{n}$ to the sphere which cannot be $\Gamma$-invariant.

Remark 11 Geometrically, this comes from the fact that given $\mathbb{S}^{n-1} \subset \mathbb{R}^{n}$, the translations provide constant mean curvature perturbations of the spheres. In the case of $\mathbb{S}^{n-1} / \Gamma \subset \mathbb{R}^{n} / \Gamma$, the center cannot move as it is the fixed point of the group action.

Normal geodesic coordinates. Let us first give some controls on the geometry of the hypersurfaces equidistant to a given hypersurface $\tilde{\Sigma}_{1}$.

Lemma 4.1 For all $n \in \mathbb{N}$ and $0<r_{0}<\frac{1}{6}$, there exists $C>0$ and $0<\epsilon<\frac{r_{0}}{C}$ such that if a hypersurface $\tilde{\Sigma}_{1}$ of a manifold $(M, g)$ satisfies:
\begin{itemize}
\item[-] the normal injectivity radius of $\tilde{\Sigma}_{1}$ and the injectivity radius of points of $\tilde{\Sigma}_{1}$ in $M$ are bounded below by $3 r_{0}$,
\end{itemize}
\begin{itemize}
\item[-] $H^{\tilde{\Sigma}_{1}} \equiv n-1$, and $\left\|A^{\tilde{\Sigma}_{1}}-g^{\tilde{\Sigma}_{1}}\right\|_{C^{\alpha}\left(g^{\tilde{\Sigma}_{1}}\right)}<\epsilon$,
\item[-] on the annulus $\left\{x, d_{g}^{M}(x, \Sigma)<3 r_{0}\right\}$, we have $\|\operatorname{Rm}\|_{C^{2}(g)} \leqslant \epsilon$,
\end{itemize}
then,
$$\begin{aligned}
\left\|\frac{A^{\Sigma_{s}}}{s}-\frac{g^{\Sigma_{s}}}{s^{2}}\right\|_{C^{\alpha}\left(\frac{g^{\Sigma_{s}}}{s^{2}}\right)} & \leqslant C\left(\left\|A^{\tilde{\Sigma}_{1}}-g^{\tilde{\Sigma}_{1}}\right\|_{C^{\alpha} g^{\tilde{\Sigma}_{1}}}+|s-1|\|\operatorname{Rm}\|_{C^{\alpha}(g)}+|s-1|^{2}\|\operatorname{Rm}\|_{C^{2}(g)}\right) \\
& \leqslant C\left(1+r_{0}^{2}\right) \epsilon
\end{aligned}$$
and
$$\left\|\frac{H^{\Sigma_{s}}}{s}-\frac{n-1}{s^{2}}\right\|_{C^{\alpha}\left(\frac{g^{\Sigma_{s}}}{s^{2}}\right)} \leqslant C\left(|s-1|\|\operatorname{Ric}\|_{C^{\alpha}(g)}+|s-1|^{2}\|\operatorname{Rm}\|_{C^{2}(g)}\right) \leqslant C\left(r_{0}+r_{0}^{2}\right) \epsilon .$$

Proof Given a hypersurface $\Sigma_{1}$ whose normal injectivity radius is larger than $3 r_{0}>0$, we define a vector field $N$ on the region $\left\{x, d_{g}^{M}(x, \Sigma)<3 r_{0}\right\}$ by setting $N(x)$, for $x \in \Sigma_{s}$, as the outwards normal vector of the hypersurface $\Sigma_{S}$.

Denoting, $S(X):=\nabla_{X} N$, for $X$ a vector field on $M$, we have
$$\left(\nabla_{N} S\right)(X)=-\left(S^{2}(X)+\operatorname{Rm}(X, N) N\right) .$$
Assuming $\left\|S_{\mid \Sigma_{1}}-\mathrm{Id}\right\|_{C^{\alpha}\left(g^{\Sigma_{1}}\right)}<\epsilon$ for $\epsilon>0$ small enough, we can follow $S$ along the normal geodesics, and integrating the previous Riccati equation (17), we find that there exits $C>0$ such that for $|s-1| \leqslant r_{0} \leqslant \frac{1}{6}$,
$$\left\|\frac{S_{\mid \Sigma_{s}}}{s}-\frac{\mathrm{Id}}{s^{2}}\right\|_{C^{\alpha}\left(g^{\Sigma_{s}}\right)} \leqslant\left\|S_{\mid \Sigma_{1}}-\mathrm{Id}\right\|_{C^{\alpha}\left(g^{\Sigma_{1}}\right)}+C|s-1|\left\|\operatorname{Rm}_{g}\right\|_{C^{\alpha}(g)}+C|s-1|^{2}\left\|\operatorname{Rm}_{g}\right\|_{C^{2}(g)} .$$
Denoting $\kappa_{i}(s)$ the eigenvalues of the second fundamental form of $\Sigma_{s}$, and $\left(e_{i}(s)\right)$ an associated orthonormal basis of eigenvectors, if we project (17) on $e_{i}(s)$, we get:
$$\kappa_{i}^{\prime}(s)=-\left(\kappa_{i}(s)^{2}+g\left(\operatorname{Rm}\left(N^{s}, e_{i}(s)\right) e_{i}(s), N^{s}\right)\right)$$
and finally, by summing on $i, H^{\prime}(s)=-\left(|A|^{2}(s)+\operatorname{Ric}\left(N^{s}, N^{s}\right)\right)$. With the initial condition $H(1) \equiv n-1$, we finally have the second stated estimate. \(\square\)

Let us now construct coordinates in the neighborhood of a hypersurface satisfying the assumptions of Proposition 5.

Lemma 4.2 Let $\Sigma$ be a hypersurface satisfying the assumptions of Proposition 5. Then, there exists a diffeomorphism $\Phi: A_{e}\left(1-2 r_{0}, 1+2 r_{0}\right) \rightarrow\left\{x, d(x, \Sigma)<2 r_{0}\right\}$ such that we have for $C>0$,
$$\left\|\Phi^{*} g-g_{e}\right\|_{C^{1, \alpha}\left(g_{e}\right)} \leqslant C \epsilon,$$
where $\epsilon>0$ is the constant of Proposition 5.

Proof Let us consider the diffeomorphism $F_{g}: \Sigma \times\left[-2 r_{0}, 2 r_{0}\right]$ obtained from the outwards normal geodesic of Σ.

We then use our controls on the second fundamental form and the ambient curvature and integrate the Riccati equation satisfied by the Jacobi fields generated by the infinitesimal change of starting point on the hypersurface $\Sigma$. We therefore obtain like in Lemma 4.1 the following control for $C=C\left(n, v_{0}\right)>0$, by noting $s$ the parameter of the geodesics vanishing on $\Sigma$ :
$$\left\|F_{g}^{*} g-\left(d s^{2}+s^{2} g^{\Sigma}\right)\right\|_{C^{1, \alpha}} \leqslant C \epsilon .$$
By the assumptions of Proposition 5, up to choosing $\epsilon$ arbitrarily small, the second fundamental form is arbitrarily close to being constant and the ambient curvature arbitrarily small. In particular, according to Gauss equation (14) together with Lemma A. 1 and Proposition 4, this implies that there exists $\Gamma \subset S O(4)$ such that, up to reparametrizing $\Sigma$, we have for some $C=C\left(n, v_{0}\right)>0$,
$$\left\|g^{\Sigma}-g^{\mathbb{S}^{n-1} / \Gamma}\right\|_{C^{1, \alpha}} \leqslant C \epsilon .$$
Combining this with the control (18), we get the stated result. \(\square\)

Normal perturbations of the hypersurface. Consider normal perturbations of a hypersurface $\Sigma$ of the form $\Sigma(w):=\left\{\gamma_{x}(w(x)), x \in \Sigma\right\}$. The computations of [PX09] adapted to our situation yield the following development of the mean curvature.

Lemma 4.3 For any $0<r_{0}<\frac{1}{6}$ and any smooth hypersurface $\Sigma \subset M$ whose injectivity radius and normal injectivity radius are larger than $3 r_{0}$, there exists $\epsilon>0$ such that for all $w: \Sigma \rightarrow \mathbb{R}$ such that $\|w\|_{C^{2, \alpha}\left(g^{\Sigma}\right)} \leqslant \epsilon$, the mean curvature of $\Sigma(w)$ has the development:
$$H(\Sigma(w))=H(\Sigma)-J_{\Sigma, M} w+Q_{\Sigma, M}(w),$$
where
$$J_{\Sigma, M}:=\Delta_{\Sigma}+\left|A^{\Sigma}\right|^{2}+\operatorname{Ric}^{M}(N, N)$$
is the Jacobi operator of the hypersurface, and where $Q_{\Sigma, M}$ is such that for a constant $C>0$ depending on the $C^{2}$-norm of the curvature and the $C^{1}$-norm of the second fundamental form and $r_{0}$, we have :
$$\left\|Q_{\Sigma, M}(w)-Q_{\Sigma, M}\left(w^{\prime}\right)\right\|_{C^{\alpha}\left(g^{\Sigma}\right)} \leqslant C\left\|w-w^{\prime}\right\|_{C^{2, \alpha}\left(g^{\Sigma}\right)}\left(\|w\|_{C^{2, \alpha}\left(g^{\Sigma}\right)}+\left\|w^{\prime}\right\|_{C^{2, \alpha}\left(g^{\Sigma}\right)}\right) .$$

Proof \(\square\)

Proposition 5 is then a consequence of the following Lemma applied to $\Sigma$.

Lemma 4.4 For any $r_{0}>0$, there exists $\epsilon>0$ such that if a metric $g$ on the annulus $A_{e}\left(1-r_{0}, 1+r_{0}\right) \subset \mathbb{R}^{n} / \Gamma$ for $\Gamma \subset \operatorname{SO}(n)$ with $\Gamma \neq\{\mathrm{Id}\}$ satisfies
\begin{itemize}
\item[-] $\left\|g-g_{e}\right\|_{C^{1, \alpha}\left(g_{e}\right)} \leqslant \epsilon$,
\item[-] on $S$ the unit sphere centered at zero in $S \subset \mathbb{R}^{n} / \Gamma$, we have
$$\left\|A_{g}^{S}-g_{\mid S}\right\|_{C^{\alpha}(S)} \leqslant \epsilon,$$
\item[-] on $A_{e}\left(1-r_{0}, 1+r_{0}\right)$, we have
$$\left\|\operatorname{Rm}_{g}\right\|_{C^{4}\left(g_{e}\right)} \leqslant \epsilon,$$
\end{itemize}
Then, there exists $\epsilon_{1}=\epsilon_{1}\left(r_{0}, \epsilon, n, \alpha\right)>0$ such that there exists a unique solution $w$ satisfiying $\|w\|_{C^{2, \alpha}(S)} \leqslant \epsilon_{1}$ to the equation
$$H_{g}(S(w)) \equiv n-1,$$
where $H_{g}$ is the mean curvature for $g$ and where $S(w)=\left\{\gamma_{x}(w(x)), x \in S\right\}$ for $\gamma_{x}$ the geodesic starting $x$ and outwards normal to $S$.

We moreover have the control:
$$\|w\|_{C^{2, \alpha}(S)} \leqslant C\left\|H_{g}(S)-(n-1)\right\|_{C^{\alpha}(S)} .$$

Proof This is a consequence of the following quantitative version of the inverse function theorem proven by Banach fixed point theorem.

Lemma 4.5 Let $\Phi: E \rightarrow F$, be a smooth map between Banach spaces and let $Q:=\Phi-\Phi(0)-d_{0} \Phi$.

Assume that there exist $q>0, r_{0}>0$ and $c>0$ such that
\begin{itemize}
\item[(1)] for all $x$ and $y$ in $B\left(0, r_{0}\right)$, we have the following control on the nonlinear terms
$$\|Q(x)-Q(y)\| \leqslant q(\|x\|+\|y\|)\|x-y\| .$$
\item[(2)] the linearization $d_{0} \Phi$ is an isomorphism, and more precisely, we have
$$\left\|\left(d_{0} \Phi\right)^{-1}\right\| \leq c .$$
If $r \leqslant \min \left(r_{0}, \frac{1}{2 q c}\right)$ and $\|\Phi(0)\| \leqslant \frac{r}{2 c}$, then, the equation $\Phi(x)=0$ admits a unique solution in $B(0, r)$.
\end{itemize}

We will equip $S$ with the Hölder norms given by the restriction of $g_{e}$ on $S$. Let us consider the operator $\Phi: C^{2, \alpha}(S) \rightarrow C^{0, \alpha}(S)$ defined by
$$\Phi: w \in C^{2, \alpha}(S) \mapsto H_{g}(S(w))-(n-1) \in C^{0, \alpha}(S),$$
and show that it satisfies the assumptions of Lemma 4.5, with $\Phi(0)=H_{g}(S)-(n-1)$, $d_{0} \Phi=J_{S, g}$.

Remark 12 In this proof, we will precise the metric instead of the manifold for the Jacobi operator and the nonlinear terms of the mean curvature variations.
\begin{itemize}
\item[(1)] The operator $J_{S, g}$ is invertible and has a bounded inverse for $\epsilon>0$ small enough. Indeed, $-(n-1)$ is not an eigenvalue of the Laplacian because $\Gamma \neq\{\mathrm{Id}\}$, therefore $J_{S, g_{e}}$ is invertible with a bounded inverse. Moreover, by proximity of the metrics and the control of the $C^{\alpha}(S)$-norm of the second fundamental form and the $C^{4}$-norm of the ambient curvature, there exists $C_{1}>0$ such that,
$$\left\|J_{S, g_{e}}-J_{S, g}\right\| \leqslant C_{1} \epsilon,$$
for the operator norm from $C^{2, \alpha}(S)$ to $C^{\alpha}(S)$. The operator $J_{S, g}$ is therefore invertible with a bounded inverse for $\epsilon$ small enough since this is an open condition.
\item[(2)] The nonlinear terms are controlled in a quadratic way. There exists a constant $C>0$ depending on $r_{0}, \alpha$ and $\epsilon$ :
$$\left\|Q_{S, g}(w)-Q_{S, g}\left(w^{\prime}\right)\right\|_{C^{\alpha}} \leqslant C\left\|w-w^{\prime}\right\|_{C^{2, \alpha}(S)}\left(\|w\|_{C^{2, \alpha}}+\left\|w^{\prime}\right\|_{C^{2, \alpha}(S)}\right) .$$
\item[(3)] Since the second fundamental form is almost constant, we have:
$$\left\|H_{g}(S)-(n-1)\right\|_{C^{\alpha}(S)} \leqslant \epsilon .$$
Therefore, there exists a unique solution $w$ to the equation $\Phi(w)=0$ such that $\|w\|_{C^{2, \alpha}(S)} \leqslant \epsilon_{1}:=\min \left(\frac{1}{2 C C_{1}}, 2 C_{1} \epsilon\right)$. This solution moreover satisfies for $C^{\prime}>0$,
$$\|w\|_{C^{2, \alpha}(S)} \leqslant C^{\prime}\left\|H_{g}(S)-(n-1)\right\|_{C^{\alpha}(S)} .$$ \(\square\)
\end{itemize}

Proof of Proposition 5 According to Lemma 4.2, under the assumptions of Proposition 5, then, there exists a diffeomorphism $\Phi: A_{e}\left(1-2 r_{0}, 1+2 r_{0}\right) \rightarrow\left\{x, d(x, \Sigma)<2 r_{0}\right\}$ such that we have for $C>0$,
\begin{itemize}
\item[-] the metrics are close,
$$\left\|\Phi^{*} g-g_{e}\right\|_{C^{1, \alpha}\left(g_{e}\right)} \leqslant C \epsilon,$$
\end{itemize}
\begin{itemize}
\item[-] for the unit-sphere centered at zero denoted $S \subset \mathbb{R}^{n} / \Gamma$, we have
$$\left\|A_{\Phi^{*} g}^{S}-\left(\Phi^{*} g\right)_{\mid S}\right\|_{C^{\alpha}} \leqslant \epsilon,$$
\item[-] for the curvature on $A_{e}\left(1-r_{0}, 1+r_{0}\right)$, we have
$$\left\|\operatorname{Rm}_{\Phi^{*} g}\right\|_{C^{4}} \leqslant \epsilon,$$
where $\epsilon>0$ is the constant in the assumptions of Proposition 5, for which the metric $\Phi^{*} g$ satisfies the assumptions of Lemma 4.4 with $S=\Phi^{*} \Sigma$ the unit-sphere of $\mathbb{R}^{n} / \Gamma$. Applying Lemma 4.4, we obtain the statement of Proposition 5. \(\square\)
\end{itemize}

For $\Sigma$ satisfying the assumptions of Proposition 5, let us define $\tilde{\Sigma}:=\Sigma(w)$, where $w$ is the unique solution given by the proof of Proposition 5.

\section*{5 Construction of a foliation of the neck regions by constant mean curvature hypersurfaces}

Let us now foliate our neck regions by constant mean curvature hypersurfaces.

\subsection*{5.1 Local foliation by constant mean curvature hypersurfaces}

We start by constructing our foliation locally.

Proposition 6 (Local foliation) For all $n \in \mathbb{N}$ and $0<r_{0}<\frac{1}{6}$, there exists $C>0$ and $0<\epsilon<\frac{r_{0}}{C}$ such that if a hypersurface $\tilde{\Sigma}_{1}$ diffeomorphic to $\mathbb{S}^{n-1} / \Gamma$, for $\Gamma \neq\{\mathrm{Id}\}$, of a manifold $(M, g)$ satisfies:
\begin{itemize}
\item[-] the normal injectivity radius of $\tilde{\Sigma}_{1}$ and the injectivity radius of the points $\tilde{\Sigma}_{1}$ in $M$ are bounded below by $3 r_{0}$,
\item[-] $H^{\tilde{\Sigma}_{1}} \equiv n-1$, and $\left\|A^{\tilde{\Sigma}_{1}}-g^{\tilde{\Sigma}_{1}}\right\|_{C^{\alpha}\left(g^{\tilde{\Sigma}_{1}}\right)}<\epsilon$,
\item[-] on the annulus $\left\{x, d_{g}^{M}(x, \Sigma)<3 r_{0}\right\}$, we have $\left\|\mathrm{Rm}_{g}\right\|_{C^{2}(g)} \leqslant \epsilon$.
\end{itemize}
Then, there exists a family of hypersurfaces $\tilde{\Sigma}_{s}, s \in\left[\frac{1}{1+2 r_{0}}, 1+2 r_{0}\right]$ with constant mean curvature $\frac{n-1}{s}$ foliating a region of the annulus $\tilde{A}\left(\frac{1}{1+2 r_{0}}, 1+2 r_{0}\right)$ satisfying:
$$\left\{x, d_{g}^{M}(x, \Sigma)<r_{0}\right\} \subset \tilde{A}\left(\frac{1}{1+2 r_{0}}, 1+2 r_{0}\right) \subset\left\{x, d_{g}^{M}(x, \Sigma)<3 r_{0}\right\} .$$

The construction we propose consists in perturbing normally the level sets of the distance function to the hypersurface $\tilde{\Sigma}_{1}$ in constant mean curvature hypersurfaces by Proposition 5.

Let us define the equidistant hypersurfaces $\Sigma_{s}:=\left\{\gamma_{x}(s-1), x \in \tilde{\Sigma}_{1}\right\}$ for $s>0$ small enough where $\gamma_{x}$ is the outwards normal geodesic to the hypersurface $\tilde{\Sigma}$ starting at $x$. These hypersurfaces foliate the annulus $\left\{x, d_{g}^{M}(x, \Sigma)<3 r_{0}\right\}$ by definition of the normal injectivity and their geometry is well controlled around $\tilde{\Sigma}_{1}$.

Proof of Proposition 6 Thanks to the controls (16), and (15), we can use Lemma 4.4 to perturb normally each hypersurface $\Sigma_{s}$ to a constant mean curvature hypersurface $\tilde{\Sigma}_{s}$. Hence, there exists a family of hypersurfaces $\left(\tilde{\Sigma}_{s}\right)_{s \in\left[\frac{1}{1+2 r_{0}}, 1+2 r_{0}\right]}$ with mean curvature constant equal to $\frac{n-1}{s}$ for each $s$. These hypersurfaces are defined from a unique function $w_{s}$ from $\tilde{\Sigma}_{1}$ to $\mathbb{R}$ by Proposition 5,
$$\tilde{\Sigma}_{s}=\Sigma\left(s\left(1+w_{s}\right)\right):=\left\{\gamma_{x}\left(s\left(1+w_{s}(x)\right)\right), x \in \tilde{\Sigma}_{1}\right\},$$
we moreover have the control
$$\left\|w_{s}\right\|_{C^{2, \alpha}\left(g^{\tilde{\Sigma}_{1}}\right)} \leqslant C \epsilon\left(|s-1|+|s-1|^{2}\right) .$$
Let us now show that this family actually foliates the annulus. More precisely, we will show that given $s$ and $s^{\prime} \in\left[\frac{1}{1+2 r_{0}}, 1+2 r_{0}\right]$, close enough and such that $s<s^{\prime}, \tilde{\Sigma}_{s^{\prime}}$ is a normal perturbation of $\tilde{\Sigma}_{s}$ by a strictly positive function $w_{s}^{s^{\prime}}: \tilde{\Sigma}_{s} \rightarrow \mathbb{R}$. They are indeed normal perturbation of each other because they are small (in $C^{2, \alpha}\left(g^{\tilde{\Sigma}_{1}}\right)$-norm) normal perturbations of the equidistant hypersurfaces from $\tilde{\Sigma}_{1}$.

By Lemma 4.4, for $s$ and $s^{\prime}$ close enough, the function $w_{s}^{s^{\prime}}$ satisfies $\left\|w_{s}^{s^{\prime}}\right\|_{C^{2, \alpha}\left(\left(g^{\Sigma_{s}}\right)\right)} \leqslant$ $2\left|s^{\prime}-s\right|$ and is a solution to
$$-J_{\tilde{\Sigma}_{s}, M}\left(w_{s}^{s^{\prime}}\right)=\frac{n-1}{s^{\prime}}-\frac{n-1}{s}+Q_{\tilde{\Sigma}_{s}, M}\left(w_{s}^{s^{\prime}}\right),$$
where there exists $C=C\left(\epsilon, n, \alpha, r_{0}\right)>0$ independent of $s$ such that for any functions $w$, and $w^{\prime}$, we have $\left\|Q_{\tilde{\Sigma}_{s}, M}(w)-Q_{\tilde{\Sigma}_{s}, M}\left(w^{\prime}\right)\right\|_{C^{\alpha}\left(g^{\tilde{\Sigma}_{s}}\right)} \leqslant C\left\|w-w^{\prime}\right\|_{C^{2, \alpha}}\left(\|w\|_{C^{2, \alpha}\left(g^{\tilde{\Sigma}_{s}}\right)}+\right.$ $\left.\left\|w^{\prime}\right\|_{C^{2, \alpha}\left(g^{\tilde{\Sigma}_{s}}\right)}\right)$.

We therefore get $\left\|Q_{\tilde{\Sigma}_{s}, M}\left(w_{s}^{s^{\prime}}\right)\right\|_{C^{\alpha}\left(g^{\tilde{\Sigma}_{s}}\right)} \leqslant 4 C\left|s^{\prime}-s\right|^{2}$, and since $s \tilde{\Sigma}_{s}$ is close to $\mathbb{S}^{n-1} / \Gamma$, for $\left|s^{\prime}-s\right|$ small enough, $J_{\tilde{\Sigma}_{s}, M}$ is close to $\Delta^{\mathbb{S}^{n-1} / \Gamma}+n-1$, and we have:
$$\left\|-\left(\Delta^{\mathbb{S}^{n-1} / \Gamma}+n-1\right)\left(w_{s}^{s^{\prime}}-\left(s^{\prime}-s\right)\right)\right\|_{C^{\alpha}\left(g^{\tilde{\Sigma}_{s}}\right)} \leqslant C\left(\left(s^{\prime}-s\right)^{2}+\epsilon\left(s^{\prime}-s\right)\right) .$$

Since $-\Delta^{\mathbb{S}^{n-1} / \Gamma}+n-1$ is invertible, there exists $C=C(\alpha, n)>0$ such that
$$\left\|w_{s}^{s^{\prime}}-\left(s^{\prime}-s\right)\right\|_{C^{2, \alpha}\left(g^{\tilde{\Sigma}_{s}}\right)} \leqslant C\left(\left(s^{\prime}-s\right)^{2}+\epsilon\left(s^{\prime}-s\right)\right) .$$
Finally, we have $w_{s}^{s^{\prime}}=\left(s^{\prime}-s\right)+\mathcal{O}\left(\left(s^{\prime}-s\right)^{2}+\epsilon\left(s^{\prime}-s\right)\right)$, and in particular, for $s^{\prime}-s>0$ and $\epsilon$ small enough (depending on $n$ and $\alpha$ ), we have $w_{s}^{s^{\prime}}>0$.

This implies that for all $s, s^{\prime} \in\left[\frac{1}{1+2 r_{0}}, 1+2 r_{0}\right]$, the hypersurfaces $\tilde{\Sigma}_{s}$ and $\tilde{\Sigma}_{s^{\prime}}$ are all disjoint and foliate the annulus. Indeed, we have just seen that for $s<s^{\prime}$ and $\left|s-s^{\prime}\right|$ small enough, the hypersurface $\tilde{\Sigma}_{s^{\prime}}$ is strictly included in one side of $\tilde{\Sigma}_{s}$. Recalling that for all $s, \tilde{\Sigma}_{s}=\tilde{\Sigma}_{1}\left(s\left(1+w_{s}\right)\right)$, this means that for all $x$, the function $s \mapsto\left(s\left(1+w_{s}(x)\right)\right)$ is strictly increasing, and therefore that we indeed have a foliation of the annulus. \(\square\)

Remark 13 It was not directly possible to ensure that two hypersurfaces $\tilde{\Sigma}_{s}$ and $\tilde{\Sigma}_{s^{\prime}}$ do not intersect for $s, s^{\prime} \in\left[\frac{1}{1+2 r_{0}}, 1+2 r_{0}\right]$ from our previous controls. Indeed, the control $\left\|w_{s}\right\|_{C^{2, \alpha}\left(g^{\tilde{\Sigma}_{1}}\right)} \leqslant C\left(\epsilon|s-1|+\epsilon|s-1|^{2}\right)$ is not enough to rule out $w_{s}(x)=w_{s^{\prime}}\left(x^{\prime}\right)$ when $s-1$ is much larger than $s-s^{\prime}$.

\subsection*{5.2 Global foliation of the neck regions.}

Let us come back to our applications and consider an Einstein manifold $(M, g)$ close to an Einstein orbifold $\left(M_{o}, g_{o}\right)$ in the Gromov-Hausdorff sense. According to Proposition 1, this manifold is $\epsilon$-approximated by a tree of Ricci-flat ALE orbifolds desingularizing the orbifold $\left(M_{o}, g_{o}\right)$. We have satisfactory coordinates on the regions $\mathcal{M}_{o}(\epsilon)$ and $\mathcal{N}_{k}(\epsilon)$ and want to find good coordinates in the annuli $\mathcal{A}_{k}(t, \epsilon)$. They are included in metric annuli $A\left(\rho_{1}, \rho_{2}\right)$ for $\rho_{1}:=\frac{1}{8} \epsilon^{-1} T_{k}^{\frac{1}{2}}$ and $\rho_{2}:=8 \epsilon T_{j}^{\frac{1}{2}}$ on which we have the following properties:
\begin{itemize}
\item[(1)] the curvature is controlled by [Ban90, Proposition 3]: for all $l \in \mathbb{N}$, there exists $C>0$ and $\beta_{1}, \beta_{2}>0$ depending on $g_{o}$ and the $g_{b_{j}}$ such that at distance $\rho \in\left[\frac{\rho_{1}}{2}, 2 \rho_{2}\right]$ from $p$, we have
$$\rho^{2+l}\left|\nabla^{l} \operatorname{Rm}\right| \leqslant \eta(\rho):=C \epsilon\left[\left(\frac{\rho_{1}}{\rho}\right)^{\beta_{1}}+\left(\frac{\rho}{\rho_{2}}\right)^{\beta_{2}}\right],$$
\end{itemize}

Remark 14 In [Ban90], the result is only stated for $l=0$, but the regularity of Einstein metrics, and in particular the fact that the curvature is harmonic (for the Hodge Laplacian) yields the estimate for higher derivatives by local elliptic estimates.
\begin{itemize}
\item[(2)] by Proposition 2, there exists $\delta(\epsilon)$ such that $\delta(\epsilon) \rightarrow 0$ as $\epsilon \rightarrow 0$ and for any $2 \rho_{1}<\rho<\frac{1}{4} \rho_{2}$, there exists a region $\hat{A}(\rho, 2 \rho)$ satisfiying
$$A((1+\delta) \rho,(2-\delta) \rho) \subset \hat{A}(\rho, 2 \rho) \subset A((1-\delta) \rho,(2+\delta) \rho),$$
$\Gamma$ a finite subgroup of $S O(4)$ and a diffeomorphism
$$\Phi_{\rho}: A_{e}(1,2) \subset \mathbb{R}^{4} / \Gamma \rightarrow \hat{A}(\rho, 2 \rho) \subset M,$$
for which we have,
$$\left\|\frac{\Phi_{\rho}^{*} g}{\rho^{2}}-g_{e}\right\|_{C^{l+2}\left(A_{e}(1,2)\right)} \leqslant \delta$$
\item[(3)] by Lemma 2.6, there exists a hypersurface $\Sigma_{\rho_{1}}$ whose second fundamental form satisfies $\left\|\frac{A_{g}^{\Sigma \rho_{1}}}{\rho_{1}}-\frac{g}{\rho_{1}^{2}}\right\|_{C^{l+1}\left(\frac{g}{\rho_{1}^{2}}\right)} \leqslant \delta$,
\item[(4)] by Lemma 2.2 and Lemma 2.7 there exists $r_{0}>0$ such that the injectivity radius at each point $x$ is bounded below by $r_{0} d(x, p)$, and the normal injectivity radius to $\Sigma_{\rho_{1}}$ by Lemma 2.6 is bounded below by $r_{0} \rho_{1}$.
\end{itemize}

The control (19) means that in the middle of the annulus, we have a much better control than initially expected since the classical $\epsilon$-regularity theorems [Gao90, BKN89, And89] would only give $\rho^{2}|\mathrm{Rm}| \leqslant C\|\mathrm{Rm}\|_{L^{2}\left(A\left(\rho_{1}, \rho_{2}\right)\right)}$. From the point of view of analysis, the difference is substantial as it allows one to do analysis in weighted Hölder spaces, and this will be heavily used in [Ozu19b].

Remark 15 Analogous estimates hold in any dimension $n$ by assuming some much less natural $L^{\frac{n}{2}}$-controls on the Riemann curvature.

The main difficulty in constructing good coordinates here is that the interior radius, $\rho_{1}$, is neglectible when compared to the radius at which our controls are optimal, $\bar{\rho}:=\left(\rho_{1}^{\beta_{1}} \rho_{2}^{\beta_{2}}\right)^{\frac{1}{\beta_{1}+\beta_{2}}}$ which minimizes $\eta$. Constant mean curvature hypersurfaces are convenient in this context as they can be constructed in the entire zone, and can be controlled by Proposition 3.

Proposition 7 For all $n \in \mathbb{N}$, there exists $\epsilon_{0}>0$, and $C>0$ such that for any $0<\epsilon<\epsilon_{0}$, we have the following property. Let $\mathcal{A}_{k}(t, \epsilon)$ be an intermediate annulus of an Einstein metric which is $\epsilon$-approximated by a naïve desingularization, and assume that it is included in a metric annulus $A\left(4 \rho_{1}, \frac{1}{4} \rho_{2}\right)$ with $\int_{A\left(\rho_{1}, \rho_{2}\right)}|\mathrm{Rm}|^{2} d v<\epsilon^{2}$. Then, there exists a foliation of a region $\tilde{A}\left(2 \rho_{1}, \frac{1}{2} \rho_{2}\right)$ bounded by two hypersurfaces of mean curvature respectively constant equal to $\frac{n-1}{2 \rho_{1}}$ and $\frac{n-1}{\frac{1}{2} \rho_{2}}$, with
$$\mathcal{A}_{k}(t, \epsilon) \subset A\left((2+C \epsilon) \rho_{1},\left(\frac{1}{2}-C \epsilon\right) \rho_{2}\right) \subset \tilde{A}\left(2 \rho_{1}, \frac{1}{2} \rho_{2}\right) \subset A\left((2-C \epsilon) \rho_{1},\left(\frac{1}{2}+C \epsilon\right) \rho_{2}\right),$$
by hypersurfaces denoted $\tilde{\Sigma}_{s}$ whose mean curvature equals $\frac{n-1}{s}$.

Proof Considering $\Phi_{2 \rho_{1}}$, the diffeomorphism of Proposition 2 at scale $2 \rho_{1}$, we define the hypersurface $\Sigma_{2 \rho_{1}}:=\Phi_{2 \rho_{1}, *} S \subset M$, where $S$ is the unit-sphere centered at zero of $\mathbb{R}^{4} / \Gamma$. According to Lemmata 2.6 and 2.7, and Corollary 1 , we satisfy the assumptions of Lemma 4.4. We can therefore perturb $\Sigma_{2 \rho_{1}}$ to a hypersurface $\tilde{\Sigma}_{2 \rho_{1}}$ whose mean curvature is constant equal to $\frac{n-1}{2 \rho_{1}}$.

According to Proposition 6, there exists a foliation by hypersurfaces $\tilde{\Sigma}_{s}$ whose mean curvature is constant equal to $\frac{n-1}{s}$ for all $2 \rho_{1}<s<\left(1+2 r_{0}\right) 2 \rho_{1}$. Moreover, for any $s$, there exists a constant $C=C(n, \alpha)>0$ such that if we recall the notation
$$\eta(s):=C \epsilon\left[\left(\frac{\rho_{1}}{s}\right)^{\beta_{1}}+\left(\frac{s}{\rho_{2}}\right)^{\beta_{2}}\right],$$
we have the following a priori controls on the $\tilde{\Sigma}_{s}$ thanks to Proposition 3:
\begin{itemize}
\item[-] the normal injectivity radius of $\tilde{\Sigma}_{s}$ and the injectivity radius of the points of $\tilde{\Sigma}_{s}$ in $M$ are bounded below by $3 s r_{0}$ according to Lemmata 2.2 and 2.7,
\item[-] $H^{\tilde{\Sigma}_{1}} \equiv \frac{n-1}{s}$, and $\left\|\frac{A^{\tilde{\Sigma}_{s}}}{s}-\frac{g^{\tilde{\Sigma}_{s}}}{s^{2}}\right\|_{C^{\alpha}}<C \eta(s)$,
\item[-] on the annulus $\left\{x, d_{g}^{M}\left(x, \tilde{\Sigma}_{1}\right)<3 s r_{0}\right\}$, we have $\left\|\operatorname{Rm}_{g}\right\|_{C^{4}(g)} \leqslant \frac{C \eta(s)}{s^{2}}$.
\end{itemize}
We can therefore apply Proposition 6 from the hypersurface $\tilde{\Sigma}_{2\left(1+2 r_{0}\right) \rho_{1}}$ in order to obtain a foliation by hypersurfaces with constant mean curvature equal to $\frac{n-1}{s}$ up to $s=2\left(1+2 r_{0}\right)^{2} \rho_{1}$. Once again, the a priori controls of Proposition 3 of order $C \eta(s)$ and the injectivity and normal injectivity controls of Lemmata 2.2 and 2.7 let us iterate this process in order to construct hypersurfaces $\tilde{\Sigma}_{s}$ with mean curvature constant equal to $\frac{n-1}{s}$ up to $s=2\left(1+2 r_{0}\right)^{k} \rho_{1}$ for any $k \in \mathbb{N}$ with $2\left(1+2 r_{0}\right)^{k} \rho_{1}<\frac{1}{2} \rho_{2}$ which is the stated result. \(\square\)

\section*{6 Construction of coordinates and control on the metric}

To construct a diffeomorphism, we will use the constant mean curvature hypersurface where our estimates are optimal and follow the gradient lines of the function $s:=\frac{n-1}{H\left(\Sigma_{s}\right)}$ whose level sets are the hypersurfaces $\tilde{\Sigma}_{S}$. The main result is the following Proposition:

Proposition 8 Under the same assumptions as Proposition 7, there exists $\beta_{1}>0$, $\beta_{2}>0, \Gamma \neq\{\mathrm{Id}\}$ a finite subgroup of $S O(4)$ such that for all $l \in \mathbb{N}$, there exists $C>0$, and a diffeomorphism:
$$\Phi: A_{e}\left(2 \rho_{1}, \frac{1}{2} \rho_{2}\right) \rightarrow \tilde{A}\left(2 \rho_{1}, \frac{1}{2} \rho_{2}\right),$$
such that for all $\rho \in\left[2 \rho_{1}, \frac{1}{4} \rho_{2}\right]$, denoting $\Phi_{\rho}:=\Phi \circ \phi_{\rho}: A_{e}(1,2) \rightarrow \tilde{A}\left(2 \rho_{1}, \frac{1}{2} \rho_{2}\right)$, where $\phi_{\rho}$ is the homothetic transformation of ratio $\rho$ on $\mathbb{R}^{4} / \Gamma$, we have:
$$\left\|\frac{\Phi_{\rho}^{*} g}{\rho^{2}}-g_{e}\right\|_{C^{l}\left(A_{e}(1,2)\right)} \leqslant C \epsilon\left(\left(\frac{\rho_{1}}{\rho}\right)^{\beta_{1}}+\left(\frac{\rho}{\rho_{2}}\right)^{\beta_{2}}\right) .$$

Remark 16 Our proofs again work in any dimension $n \in \mathbb{N}$ for metrics with a region close to a flat cone $\mathbb{R}^{n} / \Gamma$ (for $\Gamma \neq\{\mathrm{Id}\}$ ) where the curvature is small in $L^{\frac{n}{2}}$.

\subsection*{6.1 Coordinates based on our constant mean curvature foliation}

In the foliation constructed in Proposition 7, one particular hypersurface is better controlled than the others at its scale. It is $\tilde{\Sigma}_{\bar{\rho}}$ where $\eta(\bar{\rho})=\min _{\rho_{1}<\rho<\rho_{2}} \eta(\rho)$, which satisfies the following properties by (19) and Proposition 3:
\begin{itemize}
\item[(1)] there exists a diffeomorphism $\phi: \mathbb{S}^{n-1} / \Gamma \rightarrow \tilde{\Sigma}_{\bar{\rho}}$ such that: for all $k \in \mathbb{N}$ and $0<\alpha<1$, there exists $C=C\left(k, \alpha, n, r_{0}\right)>0$ for which,
$$\left\|\frac{\phi^{*} g^{\tilde{\Sigma}_{\bar{\rho}}}}{\bar{\rho}^{2}}-g^{\mathbb{S}^{n} / \Gamma}\right\|_{C^{k, \alpha}\left(g^{\mathbb{S}^{n} / \Gamma}\right)}<C \eta(\bar{\rho}),$$
\item[(2)] for all $k \in \mathbb{N}$ and $0<\alpha<1$, there exists $C=C(k, \alpha, n)>0$ such that
$$\left\|\frac{A^{\tilde{\Sigma}_{\bar{\rho}}}}{\bar{\rho}}-\frac{g^{\tilde{\Sigma}_{\bar{\rho}}}}{\bar{\rho}^{2}}\right\|_{C^{k, \alpha}\left(\frac{g^{\tilde{\Sigma}_{\bar{\rho}}}}{\bar{\rho}^{2}}\right)} \leqslant C \eta(\bar{\rho}) .$$
\item[(3)] for all $k \in \mathbb{N}$, there exists $C=C(k, n)>0$ such that on the annulus $\left[\frac{1}{2} \bar{\rho}, 2 \bar{\rho}\right]$ we have,
$$\bar{\rho}^{2+k}\left|\nabla^{k} \operatorname{Rm}\right|_{g} \leqslant C \eta(\bar{\rho}) .$$
We then define a diffeomorphism $\Phi:\left[\rho_{1}, \rho_{2}\right] \times \mathbb{S}^{n-1} / \Gamma \rightarrow \tilde{A}\left(\rho_{1}, \rho_{2}\right)$ in the following way: at $\bar{\rho}$,
$$\Phi(\bar{\rho}, x):=\phi(x),$$
where $\phi$ is the diffeomorphism of the above point 1 , and for all $s \in\left[\rho_{1}, \rho_{2}\right]$,
$$\partial_{s} \Phi(s, x)=u_{s}(x) N^{\tilde{\Sigma}_{s}}(\Phi(s, x))=-\frac{\nabla s}{|\nabla s|^{2}},$$
\end{itemize}
where $u_{s}$ is such that $\Phi\left(s, \mathbb{S}^{n-1} / \Gamma\right)=\tilde{\Sigma}_{s}$. This is a diffeomorphism on its image since two curves following the vector field $-\frac{\nabla s}{|\nabla s|^{2}}$, which never vanishes, cannot intersect if they are not equal.

\subsection*{6.2 Control of the metric in these coordinates}

In the coordinates given by $\Phi$, the metric has the following form,
$$\Phi^{*} g(s, x)=u_{s}(x)^{2} d s^{2}+s^{2} h_{s}(x),$$
where $h_{s}$ is a metric on $\mathbb{S}^{n-1} / \Gamma$.

Let us take the following notations for the rest of the section in which we will always work on $\mathbb{R}^{n} / \Gamma$ :
\begin{itemize}
\item[-] $\phi_{s}(x)=\Phi(s, x)$, which implies that $s^{2} h_{s}=\phi_{s}^{*} g^{\tilde{\Sigma}_{s}}$.
\item[-] $H(s)=\phi_{s}^{*} H^{\tilde{\Sigma}_{s}} \equiv \frac{n-1}{s}$,
\item[-] $A(s)=\phi_{s}^{*} A^{\tilde{\Sigma}_{s}}$,
\item[-] $N(s)=\phi_{s}^{*} N^{\tilde{\Sigma}_{s}}$
\item[-] $f_{i}(s)=d_{(s, .)} \Phi\left(0, e_{i}\right)$, where the $e_{i}$ form an orthonormal basis of $T_{x} \mathbb{S}^{n-1} / \Gamma$,
\item[-] $\nabla^{s}=\phi_{s}^{*} \nabla^{\tilde{\Sigma}_{s}}$,
\item[-] $\Delta^{s}=\phi_{s}^{*} \Delta^{\tilde{\Sigma}_{s}}$, where $\Delta^{\tilde{\Sigma}_{s}}$ is the Laplace-Beltrami operator associated to the metric $g^{\Sigma_{s}}$,
\item[-] grad ${ }^{s}$ is the gradient for the metric $s^{2} h_{s}$,
\item[-] $K(s)_{i}^{j}=g\left(\operatorname{Rm}_{g}\left(N(s), f_{i}(s)\right) f_{j}(s), N(s)\right)$.
\end{itemize}

We have the following variations for the different geometric quantities.
By [HP99, Theorem 3.2], given a variation $\partial_{s} \Phi(s, x)=u_{s} N^{\tilde{\Sigma}_{s}}$, we have the following variation formulas:
$$\begin{gathered}
\partial_{s}\left(s^{2} h_{s}\right)=2 u_{s} A(s), \\
\partial_{s} N(s)=\operatorname{grad}^{s} u_{s}, \\
\partial_{s} A(s)_{i j}=-\nabla_{i}^{s} \nabla_{j}^{s} u_{s}+\left(\sum_{k} A(s)_{i k} A(s)_{j}^{k}+K(s)_{i}^{j}\right), \\
\partial_{s} H(s)=-\left(\Delta^{s}+|A(s)|^{2}+\operatorname{Ric}(s)(N(s), N(s))\right) u_{s} .
\end{gathered}$$
Let us finally compare our Einstein metric to the flat metric in these coordinates.

Proposition 9 With the above notations, if we denote $g_{e}:=d s^{2}+s^{2} g^{\mathbb{S}^{n-1}}$, we have the following controls on $\Phi^{*} g$ : for all $l \in \mathbb{N}$, there exists $C\left(l, n, v_{0}, D_{0}\right)>0$ such that for all $s \in\left[\rho_{1}, \frac{\rho_{2}}{2}\right]$, on the annulus $[s, 2 s]$, we have
$$\|u-1\|_{C^{l}\left(g_{e}\right)} \leqslant C \eta(s),$$
and
$$\left\|h-g^{\mathbb{S}^{n-1} / \Gamma}\right\|_{C^{l}\left(g_{e}\right)} \leqslant C \eta(s),$$
and therefore, for all $s \in\left[\rho_{1}, \frac{\rho_{2}}{2}\right]$, on the annulus of radii $s$ and $2 s$,
$$\left\|\Phi^{*} g-g_{e}\right\|_{C^{l}\left(g_{e}\right)} \leqslant C \eta(s) .$$

Proof All along the proof, $C$ will denote a positive constant that may vary from line to line, but which only depends on the constants $n, v_{0}, D_{0}$ and the order of regularity $l \in \mathbb{N}, 0<\alpha<1$.

Let us start by noting that the equation (23) implies that for all $s, u_{s}$ satisfies the following equation
$$\frac{n-1}{s^{2}}=\left(\Delta^{s}+|A(s)|^{2}+\operatorname{Ric}(s)(N(s), N(s))\right) u_{s} .$$
Indeed, by following the normal perturbation $u_{S} N^{\tilde{\Sigma}_{s}}=-\frac{\nabla_{s}}{|\nabla s|^{2}}$, the variation of the mean curvature is exactly $-\frac{n-1}{s^{2}}$. In particular, for all $s$, we have
$$\left(\Delta^{s}+|A(s)|^{2}+\operatorname{Ric}(s)(N(s), N(s))\right)\left(u_{s}-1\right)=\frac{n-1}{s^{2}}-|A(s)|^{2}-\operatorname{Ric}(s)(N(s), N(s)),$$
According to Proposition 3, while $\left\|h_{s}-g^{\mathbb{S}^{n-1} / \Gamma}\right\|_{C^{1, \alpha}\left(g^{S^{n-1} / \Gamma}\right)}$ is sufficiently small, there exists $C=C(l)>0$ such that for all $s$,
$$\left\|\frac{A(s)}{s}-h_{s}\right\|_{C^{l, \alpha}\left(h_{s}\right)} \leqslant C \eta(s) .$$
Since $s^{2}|\operatorname{Ric}(s)(N(s), N(s))|<\eta(s)$, this implies that the right hand side of (25) satisfies: there exists $C=C(\alpha, n)>0$ such that for all $s$,
$$\left\|n-1-s^{2}|A(s)|^{2}-s^{2} \operatorname{Ric}(s)(N(s), N(s))\right\|_{C^{\alpha}\left(g^{\mathrm{S} n-1 / \Gamma}\right)} \leqslant C \eta(s) .$$
Likewise, for the left hand side, for any function $v: \mathbb{S}^{n-1} / \Gamma \rightarrow \mathbb{R}$ we have
$$\begin{aligned}
\| s^{2}\left(\Delta^{s}+|A(s)|^{2}+\operatorname{Ric}(s)(N(s), N(s))\right) v- & \left(\Delta^{\mathbb{S}^{n-1} / \Gamma}+n-1\right) v \|_{C^{\alpha}\left(g^{\mathbb{S}^{n-1} / \Gamma}\right)} \\
& \leqslant C \eta(s)\|v\|_{C^{2, \alpha}\left(g^{\mathrm{S} n-1 / \Gamma}\right)}
\end{aligned}$$

Since $\Delta^{\mathbb{S}^{n-1} / \Gamma}+n-1$ is invertible for $\Gamma \neq\{\mathrm{Id}\}$, we get by the inverse function theorem, Lemma 4.5, the following control: there exists $C=C(n, \alpha)>0$ such that for all $s$
$$\left\|u_{s}-1\right\|_{C^{2, \alpha}\left(g^{\mathbb{S}^{n-1} / \Gamma}\right)} \leqslant C \eta(s) .$$
Let us now show that for all $s \in\left[\rho_{1}, \rho_{2}\right],\left\|h_{s}-g^{\mathbb{S}^{n-1} / \Gamma}\right\|_{C^{1, \alpha}\left(g^{\mathrm{S} n-1} / \Gamma\right)}$ remains small. We will actually show that there exists $C=C(n, \alpha)>0$ such that $\left\|h_{s}-g^{\mathbb{S}^{n-1} / \Gamma}\right\|_{C^{1, \alpha}\left(g^{\mathbb{S}^{n-1} / \Gamma}\right)} \leqslant$ $C \eta(s)$. The expression (20) can be rewritten
$$\partial_{s}\left(h_{s}-g^{\mathbb{S}^{n-1} / \Gamma}\right)=\frac{2}{s}\left(u \frac{A^{s}}{s}-h_{s}\right),$$
but by the control (27), and Proposition 3, there exists $C=C(n, \alpha)>0$ such that we have $\left\|u \frac{A^{s}}{s}-h_{s}\right\|_{C^{1, \alpha}\left(g^{\mathrm{s} n-1} / \Gamma\right)} \leqslant C \eta(s)$. Recall that
$$\eta(s):=C \epsilon\left[\left(\frac{\rho_{1}}{s}\right)^{\beta_{1}}+\left(\frac{s}{\rho_{2}}\right)^{\beta_{2}}\right],$$
to deduce that for $\bar{\rho}<s_{0}<\rho_{2}$, we have
$$\begin{aligned}
\left\|h_{s_{0}}-g^{\mathbb{S}^{n-1} / \Gamma}\right\|_{C^{1, \alpha}\left(g^{\mathbb{S}^{n-1} / \Gamma}\right)} & \leqslant C\left(\eta(\bar{\rho})+\int_{\bar{\rho}}^{s_{0}} \frac{2}{s} \eta(s) d s\right) \\
& =C \eta(\bar{\rho})+\left(\frac{2 C \epsilon}{\rho_{2}^{\beta_{2}}} \int_{\bar{\rho}}^{s_{0}} s^{\beta_{2}-1} d s\right) \\
& =C \epsilon \frac{\bar{\rho}^{\beta_{2}}}{\rho_{2}^{\beta_{2}}}+\left(\frac{2 C \epsilon}{\rho_{2}^{\beta_{2}}}\left(s_{0}^{\beta_{2}}-\bar{\rho}^{\beta_{2}}\right)\right) \\
& \leqslant C \eta\left(s_{0}\right)
\end{aligned}$$
and similarly, for $\rho_{1}<s_{0}<\bar{\rho}$,
$$\left\|h_{s_{0}}-g^{\mathbb{S}^{n-1} / \Gamma}\right\|_{C^{1, \alpha}\left(g^{\mathbb{S}^{n-1} / \Gamma}\right)} \leqslant C \eta\left(s_{0}\right) .$$
To obtain controls on higher derivatives of $u$ and $h_{s}$, we use the other equalities of [HP99, Theorem 3.2]: according to (21), and the control (27), there exists $C=C(n, \alpha)$ such that for all $s$ we have
$$\left\|\partial_{s} N(s)\right\|_{C^{1, \alpha}\left(h_{s}\right)} \leqslant C \eta(s)$$
according to (22) and the controls (27), (26) and (28), and since the $l$-th derivatives of the curvature are bounded by $s^{-2-l} \eta(s)$, there exists $C=C(n, \alpha)>0$ such that for all $s$, we have:
$$\left\|\partial_{s}\left(\frac{A(s)}{s}\right)\right\|_{C^{\alpha}\left(h_{s}\right)} \leqslant C \eta(s) .$$

Differentiating the equality (23) with respect to $s$, and using the inequalities $\left\|\partial_{s} h_{s}\right\|_{C^{1, \alpha}\left(h_{s}\right)} \leqslant$ $C \eta(s)$, and (29), there exists $C=C(n, \alpha)>0$ such that for all $s$, we have:
$$\left\|\left(\Delta^{\mathbb{S}^{n-1} / \Gamma}+n-1\right) \partial_{s} u_{s}\right\|_{C^{\alpha}\left(h_{s}\right)} \leqslant C \eta(s) .$$
We can therefore conclude that for all $s,\left\|\partial_{s} u_{s}\right\|_{C^{2, \alpha}\left(h_{s}\right)} \leqslant C \eta(s)$.
Iterating this for higher derivatives in all directions, we obtain the stated controls. \(\square\)

\subsection*{6.3 Proximity between the Einstein metric and the naïve desingularization in weighted $C^{k}$-norm}

Now, to construct coordinates on the whole manifold $M$, we just "glue" the coordinates we have on each part together by using the local diffeomorphisms with the common asymptotic cone of each part. We obtain the following control for the metric.

Theorem 6.1 Let $D_{0}, v_{0}>0$ and $\left(M_{i}^{\mathcal{E}}, g_{i}^{\mathcal{E}}\right)$ a sequence of Einstein manifolds satisfying
\begin{itemize}
\item[-] the volume is bounded below by $v_{0}>0$,
\item[-] the diameter is bounded by $D_{0}$,
\item[-] the Ricci curvature is bounded $\mid$ Ric $\mid \leq 3$.
\end{itemize}
Then, there exists a subsequence with fixed topology $M=M_{i}^{\mathcal{E}}$ and a sequence of naïve desingularizations $\left(M, g_{t_{i}}^{D}\right)$ of an Einstein orbifold $\left(M_{o}, g_{o}\right)$ such that: for all $l \in \mathbb{N}$ and $i$ large enough, there exists $C\left(l, v_{0}, D_{0}\right)>0, \beta_{1}\left(v_{0}, D_{0}\right)>0$ and $\beta_{2}\left(v_{0}, D_{0}\right)>0$, $\epsilon_{i}>0, \epsilon_{i} \rightarrow 0$, and a diffeomorphism $\Phi_{i}: M \rightarrow M$ satisfying
\begin{itemize}
\item[(1)] on $\mathcal{M}_{o}\left(\epsilon_{i}\right)$, we have
$$\left\|\Phi_{i}^{*} g_{i}^{\mathcal{E}}-g_{o}\right\|_{C^{l}\left(g_{o}\right)} \leqslant C \epsilon_{i} .$$
\item[(2)] at the different scales $T_{i, j}$ (associated to $t_{i}$ ), on $\mathcal{N}_{j}\left(\epsilon_{i}\right)$ we have
$$\left\|\frac{\Phi_{i}^{*} g_{i}^{\mathcal{E}}}{T_{i, j}}-g_{b_{j}}\right\|_{C^{l}\left(g_{b_{j}}\right)} \leqslant C \epsilon_{i} .$$
\item[(3)] in the intermediate regions, $\mathcal{A}_{k}\left(t_{i}, \epsilon_{i}\right)$ included in a metric annulus of radii $\rho_{1}^{i, k}=$ $\frac{1}{8} T_{i, k}^{\frac{1}{2}} \epsilon_{i}^{-1}, \rho_{2}^{i, k}=8 T_{i, j}^{\frac{1}{2}} \epsilon_{i}$, for all $\rho_{1}^{i, k} \leqslant \rho \leqslant \frac{1}{2} \rho_{2}^{i, k}$, and denoting $\Phi_{i, \rho}=\Phi_{i} \circ \phi_{\rho}$, where $\phi_{\rho}$ is the homothetic transformation of ration $\rho$ on $\mathbb{R}^{4} / \Gamma_{k}$ with its flat metric $g_{e}$, we have
$$\left\|\frac{\Phi_{i, \rho}^{*} g_{i}^{\mathcal{E}}}{\rho^{2}}-g_{e}\right\|_{C^{l}\left(A_{e}(1,2)\right)} \leqslant C \epsilon_{i}\left[\left(\frac{\rho_{1}^{i, k}}{\rho}\right)^{\beta_{1}}+\left(\frac{\rho}{\rho_{2}^{i, k}}\right)^{\beta_{2}}\right] .$$
\end{itemize}

Remark 17 This is indeed much better than a $C^{\infty}$ convergence on compacts to a flat cone as we have $\left[\left(\frac{\rho_{1}^{i, k}}{\rho}\right)^{\beta_{1}}+\left(\frac{\rho}{\rho_{2}^{i, k}}\right)^{\beta_{2}}\right] \leqslant 2$, and a decay in the annulus.

\section*{A Optimal $C^{k, \alpha}$-proximity to a round sphere}

In this appendix, we are interested in metrics with pinched positive sectional curvatures and want to estimate how close to a round metric they have to be. To start with, a consequence of Cheeger-Gromov compactness is the following lemma, see [Pet98, Chapter 10] for instance.

Lemma A. 1 For all $n, 0<\alpha<1, \delta>0$ and $v_{0}>0$, there exists $\epsilon>0$ such that if $\left(M^{n}, g\right)$ satisfies
\begin{itemize}
\item[(1)] $1-\epsilon<\operatorname{Sec}(g)<1+\epsilon$,
\item[(2)] and $\operatorname{Vol}(M)>v_{0}$,
\end{itemize}
then, there exists $\Gamma$ a finite subgroup of $S O(n+1)$ (whose order is bounded by a function of $v_{0}$ ), and a diffeomorphism $\Phi: \mathbb{S}^{n} / \Gamma \rightarrow M$ for which:
$$\left\|\Phi^{*} g-g^{\mathbb{S}^{n} / \Gamma}\right\|_{C^{1, \alpha}\left(g^{\mathbb{S}^{n} / \Gamma}\right)} \leqslant \delta,$$
where $g^{\mathbb{S}^{n} / \Gamma}$ is a round metric on $\mathbb{S}^{n} / \Gamma$.
In this appendix, we will prove the following proposition.
Proposition 10 Let $\left(M, g_{0}\right)$ be a Riemannian manifold of dimension $n$ with sectional curvatures equal to 1 , and $k \in \mathbb{N}$. Then, there exists $\delta>0$ and $C>0$, such that if a metric $g$ on $M$ satisfies:
$$\left\|g-g_{0}\right\|_{C^{1, \alpha}\left(g_{0}\right)} \leqslant \delta,$$
then, there exists a diffeomorphism $\Phi: M \rightarrow M$, for which
$$\left\|\Phi^{*} g-g_{0}\right\|_{C^{k+1, \alpha}\left(g_{0}\right)} \leqslant C\|\operatorname{Ric}(g)-(n-1) g\|_{C^{k}\left(g_{0}\right)} .$$
As an immediate consequence of Lemma A. 1 and Proposition 10, we get the following statement.

Corollary 3 For all $n, 0<\alpha<1$ and $v_{0}>0$, there exists $\epsilon_{0}>0$ and $C>0$ such that for any $0<\epsilon<\epsilon_{0}$, if $\left(M^{n}, g\right)$ satisfies:
\begin{itemize}
\item[(1)] $1-\epsilon<\operatorname{Sec}(g)<1+\epsilon$,
\item[(2)] and $\operatorname{Vol}(M, g)>v_{0}$,
\end{itemize}
then, there exists $\Gamma$ a finite subgroup of $S O(n+1)$, and a diffeomorphism $\Phi: \mathbb{S}^{n} /$ $\Gamma \rightarrow M$ for which
$$\left\|\Phi^{*} g-g_{0}\right\|_{C^{1, \alpha}\left(g_{0}\right)} \leqslant C \epsilon .$$

Remark 18 The crucial part for us is that the $\epsilon$ in the final estimate is the same as in the assumption $1-\epsilon<\operatorname{Sec}(g)<1+\epsilon$.

Proof of Proposition 10 Let $\left(M^{n}, g_{0}\right)$ be a Riemannian manifold whose sectional curvatures are constant equal to 1 . For $\lambda:=\frac{(n-2)(n-1)}{2}$, define the operator
$$E_{g_{0}}(g):=\operatorname{Ric}(g)-\frac{\operatorname{R}(g)}{2} g+\lambda g+\delta_{g}^{*} \delta_{g_{0}} g .$$
Then, following [And10, Section 5], by [Ebi70] and by the Bianchi identity, there exists $\delta>0$ such that $E_{g_{0}}^{-1}(\{0\}) \cap B_{C^{1, \alpha}}(\delta)$ is exactly the set of Einstein metrics with constant $\Lambda$ which are in divergence-free gauge with respect to $g_{0}$ and have same volume.

Let $g$ be a metric on $M$ such that $\left\|g-g_{0}\right\|_{C^{k+1, \alpha}\left(g_{0}\right)} \leqslant \delta$ for $\delta>0$ a constant which we will choose small enough in the rest of the proof. According to [Ebi70], for $\delta$ small enough, there exists a diffeomorphism $\Phi: M \rightarrow M$ such that
$$\delta_{g_{0}} \Phi^{*} g=0 .$$
Hence, we have
$$\left\|E_{g_{0}}\left(\Phi^{*} g\right)\right\|_{C^{k}\left(g_{0}\right)} \leqslant\|\operatorname{Ric}(g)-(n-1) g\|_{C^{k}\left(g_{0}\right)} .$$
Now, by [Bes87, Corollary 12.72 (Bourguignon, unpublished)], the linearization of $E$ at $g_{0}$ is invertible (see again [And10, Section 5] for the adaptation to the operator $E$ ) and by the inverse function theorem Lemma 4.5 we deduce that for $\delta$ small enough, and for all $1 \leqslant p<+\infty$ and $k \in \mathbb{N}$ there exists $C>0$, such that we have
$$\left\|\Phi^{*} g-g_{0}\right\|_{W^{k+2, p}\left(g_{0}\right)} \leqslant C\left\|E_{g_{0}}\left(\Phi^{*} g\right)\right\|_{W^{k, p}\left(g_{0}\right)},$$
and finally, by (30), we have
$$\left\|\Phi^{*} g-g_{0}\right\|_{C^{k+1, \alpha}\left(g_{0}\right)} \leqslant C\|\operatorname{Ric}(g)-(n-1) g\|_{C^{k}\left(g_{0}\right)},$$
because on the sphere, for $p$ large enough, $W^{k+2, p}\left(g_{0}\right)$ embeds continuously in $C^{k+1, \alpha}\left(g_{0}\right)$, and so does $C^{k}\left(g_{0}\right)$ in $W^{k, p}\left(g_{0}\right)$. \(\square\)

\section*{References}
[And89] M.T. Anderson, Ricci Curvature Bounds and Einstein Metrics on Compact Manifolds. J. Amer. Math. Soc. 2 (1989), no. 3, 455\{490.
[And10] M.T. Anderson, A survey of Einstein metrics on 4-manifolds. Handbook of geometric analysis, No. 3, 1\{39, Adv. Lect. Math. (ALM), 14, Int. Press, Somerville, MA, 2010.
[BKN89] S. Bando ; A. Kasue ; H. Nakajima, On a construction of coordinates at infinity on manifolds with fast curvature decay and maximal volume growth. Invent. Math. 97 (1989), no. 2, 313\{349.
[Ban90] S. Bando, Bubbling out of Einstein manifolds. Tohoku Math. J. (2) 42 (1990), no. 2, 205\{216.
[Bes87] A.L. Besse, Einstein manifolds, Ergebnisse der Mathematik und ihrer Grenzgebiete (3) [Results in Mathematics and Related Areas (3)], 10. Springer-Verlag, Berlin, 1987.
[Biq13] O. Biquard, Désingularisation de métriques d'Einstein. I. Invent. Math. 192 (2013), no. 1, 197\{252.
[Biq16] O. Biquard, Désingularisation de métriques d'Einstein. II. Invent. Math. 204 (2016), no. 2, 473\{504.
[CC96] J. Cheeger ; T.H. Colding, Lower bounds on Ricci curvature and the almost rigidity of warped products. Ann. of Math. (2) 144 (1996), no. 1, 189\{237.
[CGT82] J. Cheeger ; M.Gromov ; M. Taylor, Finite propagation speed, kernel estimates for functinos of the laplace operator, and the geometry of complete Riemannian manifolds. J. Differential Geom. 17 (1982), no. 1, 15\{53.
[CN15] J. Cheeger; A. Naber, Regularity of Einstein Manifolds and the Codimension 4 Conjecture. Ann. of Math. (2) 182 (2015), no. 3, 1093\{1165.
[CEV17] O. Chodosh ; M. Eichmair ; A. Volkmann, Isoperimetric structure of asymptotically conical manifolds. J. Differ. Geom. 105 (2017), 1\{19.
[Cro80] C. Croke, Some isoperimetric inequalities and eigenvalue estimates. Ann. Sci. École Norm. Sup. (4) 13 (1980), no. 4, 419\{435.
[Col97] T.H. Colding, Ricci Curvature and Volume Convergence. Ann. of Math. (2) 145 (1997), no. 3, 477\{501.
[Ebi70] David G. Ebin, The manifold of Riemannian metrics, 1970 Global Analysis (Proc. Sympos. Pure Math., Vol. XV, Berkeley, Calif., 1968) pp. 11\{40 Amer. Math. Soc., Providence, R.I.
[Fol89] G.B. Folland, Harmonic analysis of the de Rham complex on the sphere. Reine Angew. Math. 398 (1989), 130\{143.
[Gao90] L. Gao, Einstein metrics. J. Diff. Geom. 32 (1990), 155-183.
[Gro81] M. Gromov, Structures métriques pour les variétés riemanniennes. Textes Mathématiques Paris (1981), 1-120. (rédigé par Lafontaine et Pansu). (in French)
[HP99] G. Huisken ; A. Polden, Geometric evolution equations for hypersurfaces. Calculus of variations and geometric evolution problems (Cetraro, 1996),45\{84. Lecture Notes in Math., 1713, Springer, Berlin, 1999
[Kro89] P.B. Kronheimer, The construction of ALE spaces as hyper-Kähler quotients. J. Differential Geom. Volume 29, Number 3 (1989), 665-683.
[Nak90] H. Nakajima, Self-Duality of ALE Ricci-Flat 4-Manifolds and Positive Mass Theorem. Adv. Stud. Pure Math. Recent Topics in Differential and Analytic Geometry, T. Ochiai, ed. (Tokyo: Mathematical Society of Japan, 1990), 385-396
[Ozu19b] T. Ozuch, Noncollapsed degeneration of Einstein 4-manifolds II. preprint.
[PX09] F. Pacard ; X. Xu, Constant mean curvature spheres in Riemannian manifolds. Manuscripta Mathematica. 128, 3 (2009), 275-295
[Pet98] P. Petersen, Riemannian geometry, New York Springer cop. 1998, Graduate texts in mathematics 171
[Suv11] I. Suvaina, ALE Ricci-flat Kähler metrics and deformations of quotient surface singularities. Ann. Global Anal. Geom. 41 (2012), no. 1, 109\{123.
[Ye96] R. Ye, Constant mean curvature foliation: singularity structure and curvature estimate. Pacific J. Math. Volume 174, Number 2 (1996), 569-587.

MIT, Dept. of Math., 77 Massachusetts Avenue, Cambridge, MA 02139-4307.
```
ozuch@mit.edu
https://tristanozuch.github.io/
```
