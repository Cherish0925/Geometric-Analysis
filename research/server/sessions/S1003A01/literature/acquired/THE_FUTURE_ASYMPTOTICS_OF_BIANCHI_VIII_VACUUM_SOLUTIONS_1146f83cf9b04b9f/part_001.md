---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: THE FUTURE ASYMPTOTICS OF BIANCHI VIII VACUUM SOLUTIONS]

---
source_file: gr-qc_0103107.pdf
converter: mathpix
format: mmd
---

\title{
THE FUTURE ASYMPTOTICS OF BIANCHI VIII VACUUM SOLUTIONS
}

\author{
HANS RINGSTRÖM
}

\begin{abstract}
Bianchi VIII vacuum solutions to Einstein's equations are causally geodesically complete to the future, given an appropriate time orientation, and the objective of this article is to analyze the asymptotic behaviour of solutions in this time direction. For the Bianchi class A spacetimes, there is a formulation of the field equations that was presented in an article by Wainwright and Hsu, and we will analyze the asymptotic behaviour of solutions in these variables. We also try to give the analytic results a geometric interpretation by analyzing how a normalized version of the Riemannian metric on the spatial hypersurfaces of homogeneity evolves.
\end{abstract}

\section*{1. Introduction}

Let us begin by defining what we mean by Bianchi class A spacetimes. We do this by defining the concept class A vacuum initial data. Let us introduce some terminology. Let $G$ be a 3-dimensional Lie group, $e_{i}, i=1,2,3$ be a basis of the Lie algebra with structure constants determined by $\left[e_{i}, e_{j}\right]=\gamma_{i j}^{k} e_{k}$. If $\gamma_{i k}^{k}=0$, then the Lie algebra and Lie group are said to be of class A and
$$\gamma_{i j}^{k}=\epsilon_{i j m} n^{k m}$$
where the symmetric matrix $n^{i j}$ is given by
$$n^{i j}=\frac{1}{2} \gamma_{k l}^{(i} \epsilon^{j) k l} .$$

Definition 1. Class A vacuum initial data for Einstein's equations consist of the following. A Lie group $G$ of class A, a left invariant metric $g$ on $G$ and a left invariant symmetric covariant two-tensor $k$ on $G$ satisfying
$$R_{g}-k_{i j} k^{i j}+\left(\operatorname{tr}_{g} k\right)^{2}=0$$
and
$$\nabla_{i} \operatorname{tr}_{g} k-\nabla^{j} k_{i j}=0$$
where ∇ is the Levi-Civita connection of $g$ and $R_{g}$ is the corresponding scalar curvature, indices are raised and lowered by $g$.

Consider class A vacuum initial data. We can choose a left invariant orthonormal basis $\left\{e_{i}\right\}$ with respect to $g$ so that the corresponding matrix $n^{i j}$ defined in (2) is diagonal with diagonal elements $n_{1}, n_{2}$ and $n_{3}$. By an appropriate choice of orthonormal basis $n_{1}, n_{2}, n_{3}$ can be assumed to belong to one and only one of the types given in table 1. We assign a Bianchi type to the initial data accordingly. This division constitutes a classification of the class A Lie algebras, see Lemma 3.

\begin{table}
\captionsetup{labelformat=empty}
\caption{Table 1. Bianchi class A.}
\begin{tabular}[t]{|l|l|l|l|}
\hline Type & $n_{1}$ & $n_{2}$ & $n_{3}$ \\
\hline I & 0 & 0 & 0 \\
\hline II & + & 0 & 0 \\
\hline $\mathrm{VI}_{0}$ & 0 & + & - \\
\hline $\mathrm{VII}_{0}$ & 0 & + & + \\
\hline VIII & - & + & + \\
\hline IX & + & + & + \\
\hline
\end{tabular}
\end{table}

We can divide the initial data into three classes,
\begin{itemize}
\item[1.] Bianchi IX initial data. In this case the maximal globally hyperbolic development of the initial data is future and past causally geodesically incomplete. It expands for a certain period of time, reaches a moment of maximal expansion and then recollapses.
\item[2.] Bianchi I and $\mathrm{VII}_{0}$ initial data with $\operatorname{tr}_{g} k=0$. The corresponding developments are causally geodesically complete.
\item[3.] The remaining types of initial data. With a suitable time orientation such data evolve into a future causally geodesically complete spacetime expanding forever into the future. The development is however past causally geodesically incomplete.
\end{itemize}

In this paper we are interested in the third class of initial data.
There is a formulation of Einstein's equations due to Ellis and MacCallum [1] covering, among other things, the Bianchi class A spacetimes. In an article by Wainwright and Hsu [2], a normalized version of the corresponding variables together with a different time coordinate were introduced. The main part of this paper consists of an analysis of the asymptotic behaviour of these variables. Our main interest is in Bianchi VIII, but we also consider the other Bianchi class A spacetimes in the third class as above. The Bianchi I, II and $\mathrm{VI}_{0}$ cases are quickly handled, and are included for completeness, but it takes some time to analyze the asymptotics of Bianchi $\mathrm{VII}_{0}$. Observe that Bianchi $\mathrm{VII}_{0}$ perfect fluids have been considered in [3]. Bianchi VIII is dealt with definitively, in the sense that it is proven to what the variables of Wainwright and Hsu converge. However, in certain situations this may not necessarily be enough. For instance, it is proven that $N_{2}+N_{3}$ converge to infinity, if $N_{2}, N_{3}>0$ and $N_{1}<0$, and that $N_{2}-N_{3}$ converge to zero. It is conceivable that if one is interested in computing curvature invariants for instance, one has to consider expressions of the form $N_{2}^{2}-N_{3}^{2}$, concerning which the results contained in this paper say nothing.

Let us also mention that even though it does not require much time to sort out the asymptotics for Bianchi $\mathrm{VI}_{0}$, the results yield an interesting consequence. In fact, one gets the conclusion that Bianchi VIII is very different from Bianchi IX as far as the behaviour towards the singularity is concerned. In [4] it was proven that generic Bianchi IX solutions converge to an attractor, where by the attractor, we mean the set of vacuum type I and II points, and the generic points are obtained by subtracting a finite number of positive codimension submanifolds from the manifold of Bianchi type IX points. It was also proven that for generic Bianchi IX solutions, the convergence to the attractor is almost monotone in the following sense. Given
an $\epsilon>0$, there is a $\delta>0$ such that if $x$ constitutes Bianchi IX initial data closer to the attractor than $\delta$, then applying the flow to $x$ in the past time direction will not result in points further away from the attractor than $\epsilon$. By distance, we here mean the ordinary Euclidean distance in the Wainwright Hsu variables in $\mathbb{R}^{6}$, the relevant space in the Bianchi IX matter case. This result, together with the result that generic Bianchi IX solutions have an $\alpha$-limit point on the Kasner circle, yield the conclusion that generic solutions converge to the attractor. The almost monotone convergence constitutes the most difficult step. In Proposition 3, we prove that the corresponding statement for Bianchi VIII is not true. In fact, we prove that there is a fixed number $\eta>0$, such that for any $\epsilon>0$ we can find Bianchi VIII initial data closer to the Kasner circle than $\epsilon$ which will at one point to the past be at a distance further than $\eta$ away from the attractor. This does of course not prove that Bianchi VIII solutions may not converge to the attractor, but it does imply that the main part of the argument concerning Bianchi IX presented in [4] is of no help in proving convergence to the attractor, and that a completely different method is required, assuming one still believes that generic Bianchi VIII solutions converge to the attractor towards the singularity.
Let us try to explain the argument concerning the future asymptotics of a Bianchi VIII solution with $N_{1}<0$ and $N_{2}, N_{3}>0$. By a monotonicity argument, one can prove that $N_{1} \rightarrow 0$ and $N_{2}, N_{3} \rightarrow \infty$ as $\tau \rightarrow \infty$. This is a very important observation in that it introduces a natural concept of order of magnitude; powers of $N_{2}+N_{3}$. Writing the constraint as
$$\Sigma_{+}^{2}+\Sigma_{-}^{2}+\frac{3}{4}\left[N_{1}^{2}+\left(N_{2}-N_{3}\right)^{2}-2 N_{1}\left(N_{2}+N_{3}\right)\right]=1,$$
we conclude that all the terms involved are bounded since they are all non-negative. The derivatives of $\Sigma_{+}$and $N_{1}\left(N_{2}+N_{3}\right)$ are bounded by constants independent of the initial data, but we have
$$\tilde{x}^{\prime}=-3\left(N_{2}+N_{3}\right) \tilde{y}+\ldots, \tilde{y}^{\prime}=3\left(N_{2}+N_{3}\right) \tilde{x}+\ldots$$
where $\tilde{x}=\Sigma_{-}$and $\tilde{y}=\sqrt{3}\left(N_{2}-N_{3}\right) / 2$, and the dots represent expressions that can be bounded by constants independent of which Bianchi VIII solution we are considering. Thus, if $\left(\tilde{x}^{2}+\tilde{y}^{2}\right)^{1 / 2}$ is big in comparison with $\left(N_{2}+N_{3}\right)^{-1}, \tilde{y}$ and $\tilde{x}$ will essentially behave as sine and cosine, and the frequency of the oscillation will go to infinity as $\tau \rightarrow \infty$. The oscillations in $\tilde{x}$ and $\tilde{y}$ are not so interesting, but the evolution in $\Sigma_{+}$and $N_{1}\left(N_{2}+N_{3}\right)$ is. For that reason, it is natural to consider what happens from, say, one time at which $\Sigma_{-}=0$ to the next. Before doing so, some effort has to be put into estimating the error committed in approximating $\tilde{y}$ and $\tilde{x}$ with sine and cosine, into proving that there actually are zeros of $\Sigma_{-}$and estimating the variation of different objects during the time that elapses between the zeros. After having done that, it will be possible to express $\Sigma_{+}$and $N_{1}\left(N_{2}+N_{3}\right)$ at a zero of $\Sigma_{-}$in terms of the values of the same expressions in the previous zero. In other words, it will be possible to replace the continuous flow with a discrete map depending on only two variables. This approximation will not always be valid, but when it is not, it can be replaced by less sophisticated arguments. The discrete map is then the main tool in a sequence of technical arguments proving the desired result.

When we evolve initial data we get a Lorentz metric $\bar{g}=-d t^{2}+g(t)$ on $I \times G$ where $I$ is an open interval and $g(t)$ is a Riemannian left invariant metric on $G$. Let $\Gamma$ be a
subgroup of the group of diffeomorphisms of $G$, acting properly discontinuously on $G$. We can consider $\Gamma$ as acting on $I \times G$ by letting $\Gamma$ act only on $G$. In situations where $g(t)$ is invariant under $\Gamma$, we can take the quotient to get a solution to Einstein's equations on $I \times M$, where $M=G / \Gamma$. Assuming $M$ to be compact we can define the reduced Hamiltonian, c.f. [5],
$$H_{\text {reduced }}=-\left(\operatorname{tr}_{g} k\right)^{3} \operatorname{vol}(M, g),$$
where $k(t)$ is the second fundamental form of $\{t\} \times M$. We can consider it to be a function of $t$. This object is of interest in the context of the work by Fischer and Moncrief [5]. We prove that the reduced Hamiltonian converges to zero for all the initial data in class three, though it should be remarked that the spatial hypersurfaces should be of Yamabe type -1, see [5], for this result to be of interest. Finally, let us refer the reader to [6] and references therein for further discussion of Bianchi VIII vacuum solutions.

The equations of Wainwright and Hsu are to be found in section 2. We mention some properties and describe an important tool in the analysis of the asymptotics of solutions to these equations; the monotonicity principle. In section 3 we relate the Lorentz metric on the development with the Wainwright Hsu variables. A formula expressing the reduced Hamiltonian in terms of these variables is also given. The main part of this paper consists of an analysis of the asymptotic behaviour of solutions to the equations of Wainwright and Hsu. This analysis occupies the remaining sections except for the last. The final section contains an analysis of the asymptotic behaviour of the Riemannian metric on the spatial hypersurfaces of homogeneity.

\section*{2. The equations of Wainwright and Hsu}

We formulate the equations we will use here and state some properties. The following section contains a derivation. Einstein's vacuum equations take the following form in the formulation due to Wainwright and Hsu
$$\begin{aligned}
N_{1}^{\prime} & =\left(q-4 \Sigma_{+}\right) N_{1} \\
N_{2}^{\prime} & =\left(q+2 \Sigma_{+}+2 \sqrt{3} \Sigma_{-}\right) N_{2} \\
N_{3}^{\prime} & =\left(q+2 \Sigma_{+}-2 \sqrt{3} \Sigma_{-}\right) N_{3} \\
\Sigma_{+}^{\prime} & =-(2-q) \Sigma_{+}-3 S_{+} \\
\Sigma_{-}^{\prime} & =-(2-q) \Sigma_{-}-3 S_{-}
\end{aligned}$$
where the prime denotes derivative with respect to $\tau$ and
$$\begin{aligned}
q & =2\left(\Sigma_{+}^{2}+\Sigma_{-}^{2}\right) \\
S_{+} & =\frac{1}{2}\left[\left(N_{2}-N_{3}\right)^{2}-N_{1}\left(2 N_{1}-N_{2}-N_{3}\right)\right] \\
S_{-} & =\frac{\sqrt{3}}{2}\left(N_{3}-N_{2}\right)\left(N_{1}-N_{2}-N_{3}\right) .
\end{aligned}$$
The vacuum Hamiltonian constraint is
$$\Sigma_{+}^{2}+\Sigma_{-}^{2}+\frac{3}{4}\left[N_{1}^{2}+N_{2}^{2}+N_{3}^{2}-2\left(N_{1} N_{2}+N_{2} N_{3}+N_{1} N_{3}\right)\right]=1 .$$
The above equations have certain symmetries described in Wainwright and Hsu [2]. By permuting $N_{1}, N_{2}, N_{3}$ arbitrarily we get new solutions if we at the same time
carry out appropriate combinations of rotations by integer multiples of $2 \pi / 3$ and reflections in the $\left(\Sigma_{+}, \Sigma_{-}\right)$-plane. Changing the sign of all the $N_{i}$ at the same time does not change the equations. Classify points $\left(N_{1}, N_{2}, N_{3}, \Sigma_{+}, \Sigma_{-}\right)$according to the values of $N_{1}, N_{2}, N_{3}$ in the same way as in table 1. Since the sets $N_{i}>0, N_{i}<0$ and $N_{i}=0$ are invariant under the flow of the equation we may classify solutions to (5)-(7) accordingly. When we speak of Bianchi VIII solutions we will assume two $N_{i}>0$ and one < 0. The Kasner circle is the subset of $\Sigma_{+} \Sigma_{-} N_{1} N_{2} N_{3}$-space where $N_{i}=0$ and $\Sigma_{+}^{2}+\Sigma_{-}^{2}=1$.
We only consider solutions to (5)-(7) which are not of Bianchi IX type. By the constraint (7) we conclude that $q \leq 2$ for the entire solution. As a consequence the $N_{i}$ cannot grow faster than exponentially due to (5). The solutions we consider can thus not blow up in a finite time so that we have existence intervals of the form $(-\infty, \infty)$.

Definition 2. Let $\mathcal{K}_{1}, \mathcal{K}_{2}$ and $\mathcal{K}_{3}$ be defined as the subset of the Kasner circle on which $q-4 \Sigma_{+}<0, q+2 \Sigma_{+}+2 \sqrt{3} \Sigma_{-}<0$ and $q+2 \Sigma_{+}-2 \sqrt{3} \Sigma_{-}<0$ respectively, c.f. (5).

The set $\Sigma_{-}=0, N_{2}=N_{3}$ is invariant under the flow of (5)-(7). Applying the symmetries to this set we get new invariant sets.
The concepts $\alpha$ - and $\omega$-limit set will be useful.
Definition 3. Let $f \in C^{\infty}\left(\mathbb{R}^{n}, \mathbb{R}^{n}\right)$, and consider a solution $x$ to the equation
$$\frac{d x}{d t}=f \circ x, x(0)=x_{0},$$
with maximal existence interval $\left(t_{-}, t_{+}\right)$. We call a point $x_{*}$ an $\omega$-limit point of the solution $x$, if there is a sequence $t_{k} \rightarrow t_{+}$with $x\left(t_{k}\right) \rightarrow x_{*}$. The $\omega$-limit set of $x$ is the set of its $\omega$-limit points. The $\alpha$-limit set is defined similarly by replacing $t_{+}$ with $t_{-}$.

Lemma 1. Let $f$ and $x$ be as in Definition 3. The $\omega$-limit set of $x$ is closed and invariant under the flow of $f$. If there is a $T$ such that $x(t)$ is contained in a compact set for $t \geq T$, then the $\omega$-limit set of $x$ is connected.

Proof. See e.g. [7]. □
The following lemma will be a basic tool in the analysis of the asymptotics, we will refer to it as the monotonicity principle.

Lemma 2. Consider (8). Let $U$ be an open subset of $\mathbb{R}^{n}$ and $M$ a closed subset which is invariant under the flow of the vectorfield $f$. Assume there is a function $F \in C(U, \mathbb{R})$ such that $F(x(t))$ is strictly monotone for any solution $x(t)$ of (8), as long as $x(t) \in U \cap M$. Then no solution of (8) whose image is contained in $U \cap M$ has an $\alpha$ - or $\omega$-limit point in $U$.

Remark. Observe that one can use $M=\mathbb{R}^{n}$. We will mainly choose $M$ to be the closed invariant submanifold of $\mathbb{R}^{5}$ defined by (7). If one $N_{i}$ is zero and two are non-zero we consider the number of variables to be four etc.

Proof. Let $x$ be a solution to (8) which is contained in $U \cap M$, and which has maximal existence interval $\left(t_{-}, t_{+}\right)$. Then $F \circ x$ is strictly monotone. Suppose $p \in U$ is an
$\omega$-limit point of $x$, so that there is a sequence $t_{n} \rightarrow t_{+}$such that $x\left(t_{n}\right) \rightarrow p$. Thus $F\left(x\left(t_{n}\right)\right) \rightarrow F(p)$, but $F \circ x$ is monotone so that $F(x(t)) \rightarrow F(p)$ as $t \rightarrow t_{+}-$. Thus $F(q)=F(p)$ for all $\omega$-limit points $q$ of $x$. Since $M$ is closed $p \in M$. The solution $\bar{x}$ of (8) with initial value $p$ is contained in $M$ by the invariance property of $M$, it consists of $\omega$-limit points of $x$ so that $F(\bar{x}(t))=F(p)$ which is constant. Furthermore, on an open set containing zero it takes values in $U$ contradicting the assumptions of the lemma. The argument for the $\alpha$-limit set is similar. □

\section*{3. Relation between the variables of Wainwright and Hsu and the space time metric}

We need to relate the evolution of the variables in the formulation due to Wainwright and Hsu to the evolution of the corresponding spacetime. In order to do this we first derive the formulation first presented by Ellis and MacCallum [1]. Then we derive equations (5)-(7) as in [2]. Secondly, we turn the argument around and start with solutions to the equations of Ellis and MacCallum and then construct the spacetime metric. The second part uses the first part. We can then express the spacetime metric in terms of the variables of Wainwright and Hsu. Finally, we find expressions for the reduced Hamiltonian in terms of the Wainwright Hsu variables.
3.1. Derivation of the equations of Wainwright and Hsu. Consider first a special class of spatially homogeneous four dimensional Lorentz manifolds of the form
$$\left(I \times G,-d t^{2}+\chi_{i j}(t) \xi^{i} \otimes \xi^{j}\right)$$
where $I$ is an open interval, $G$ is a Lie group of class A, $\chi_{i j}$ is a smooth positive definite matrix and the $\xi^{i}$ are the duals of a left invariant basis on $G$.
We express the condition that a manifold of the form (9) satisfies Einstein's vacuum equations in terms of the variables of Ellis and MacCallum. As these variables are defined in terms of a suitable orthonormal basis, we begin by constructing it. Let $e_{0}=\partial_{t}$ and $e_{i}=a_{i}{ }^{j} Z_{j}, \mathrm{i}=1,2,3$, be an orthonormal basis, where $a$ is a $C^{\infty}$ matrix valued function of $t$ and the $Z_{i}$ are the duals of $\xi^{i}$. Below, Latin indices will be raised and lowered by $\delta_{i j}$.
By the following argument we can assume $<\nabla_{e_{0}} e_{i}, e_{j}>=0$. Let the matrix $A$ satisfy $e_{0}(A)+A B=0, A(0)=\mathrm{Id}$ where $B_{i j}=<\nabla_{e_{0}} e_{i}, e_{j}>$ and Id is the $3 \times 3$ identity matrix. Then $A$ is smooth and $S O(3)$ valued and if $e_{i}^{\prime}=A_{i}{ }^{j} e_{j}$ then $<\nabla_{e_{0}} e_{i}^{\prime}, e_{j}^{\prime}>=0$.
Let
$$\theta(X, Y)=<\nabla_{X} e_{0}, Y>,$$
$\theta_{\alpha \beta}=\theta\left(e_{\alpha}, e_{\beta}\right)$ and $\left[e_{\beta}, e_{\delta}\right]=\gamma_{\beta \delta}^{\alpha} e_{\alpha}$ where Greek indices run from 0 to 3. The objects $\theta_{\alpha \beta}$ and $\gamma_{\beta \delta}^{\alpha}$ will be viewed as smooth functions from $I$ to some suitable $\mathbb{R}^{k}$ and the variables will be defined in terms of them.

Observe that $\left[Z_{i}, e_{0}\right]=0$. The $e_{i}$ span the tangent space of $G$ and $\left\langle\left[e_{0}, e_{i}\right], e_{0}\right\rangle=$ 0. We get $\theta_{00}=\theta_{0 i}=0$ and $\theta_{\alpha \beta}$ symmetric. We also have $\gamma_{i j}^{0}=\gamma_{0 i}^{0}=0$ and
$\gamma_{0 j}^{i}=-\theta_{i j}$. We let $n$ be defined as in (2) and
$$\sigma_{i j}=\theta_{i j}-\frac{1}{3} \theta \delta_{i j}$$
where we by abuse of notation have written $\operatorname{tr}(\theta)$ as $\theta$.
We compute the Einstein tensor in terms of $n, \sigma$ and $\theta$. The Jacobi identities for $e_{\alpha}$ yield
$$e_{0}\left(n_{i j}\right)-2 n_{k(i} \sigma_{j)}^{k}+\frac{1}{3} \theta n_{i j}=0 .$$
The $0 i$-components of the Einstein equations are equivalent to
$$\sigma_{i}{ }^{k} n_{k j}-n_{i}{ }^{k} \sigma_{k j}=0 .$$
Letting $b_{i j}=2 n_{i}{ }^{k} n_{k j}-\operatorname{tr}(n) n_{i j}$ and $s_{i j}=b_{i j}-\frac{1}{3} \operatorname{tr}(b) \delta_{i j}$ the trace free part of the $i j$ equations are
$$e_{0}\left(\sigma_{i j}\right)+\theta \sigma_{i j}+s_{i j}=0 .$$
The fact that $R_{00}=0$ yields the Raychaudhuri equation
$$e_{0}(\theta)+\theta_{i j} \theta^{i j}=0$$
and using this together with the trace of the $i j$-equations yields a constraint
$$\sigma_{i j} \sigma^{i j}+\left(n_{i j} n^{i j}-\frac{1}{2} \operatorname{tr}(n)^{2}\right)=\frac{2}{3} \theta^{2} .$$
Equations (11)-(15) are special cases of equations given in Ellis and MacCallum [1]. At $t=0$ we may diagonalize $n$ and $\sigma$ simultaneously since they commute (12). Rotating $e_{\alpha}$ by the corresponding element of $S O(3)$ yields upon going through the definitions that the new $n$ and $\sigma$ are diagonal at $t=0$. Collect the off-diagonal terms of $n$ and $\sigma$ in one vector $v$. By (11) and (13) there is a time dependent matrix $C$ such that $\dot{v}=C v$ so that $v(t)=0 \forall t$ since $v(0)=0$. Since the rotation was time independent $\left\langle\nabla_{e_{0}} e_{i}, e_{j}\right\rangle=0$ holds in the new basis.
Introduce, as in Wainwright and Hsu [2], $\Sigma_{i j}=\sigma_{i j} / \theta, N_{i j}=n_{i j} / \theta, B_{i j}=$ $2 N_{i}{ }^{k} N_{k j}-N^{k}{ }_{k} N_{i j}$ and $S_{i j}=B_{i j}-\frac{1}{3} B^{k}{ }_{k} \delta_{i j}$ and define a new time coordinate $\tau$, independent of time orientation, by
$$\frac{d t}{d \tau}=\frac{3}{\theta} .$$
Let $\Sigma_{+}=\frac{3}{2}\left(\Sigma_{22}+\Sigma_{33}\right)$ and $\Sigma_{-}=\sqrt{3}\left(\Sigma_{22}-\Sigma_{33}\right) / 2$. If we let $N_{i}$ be the diagonal elements of $N_{i j}$, equations (11) and (13) turn into (5)-(7) The Raychaudhuri equation (14) takes the form
$$\theta^{\prime}=-(1+q) \theta .$$
3.2. Construction of the spacetime. Above we derived Einstein's equations assuming the spacetime to be of a special form. Next we construct a spacetime of the form (9) beginning with initial data as in Definition 1. The construction allows us to express the evolution of the metric in terms of the variables of Wainwright and Hsu. One step is the following lemma, which also classifies the class A Lie algebras.

Lemma 3. Table 1 constitutes a classification of the class A Lie algebras. Consider an arbitrary basis $\left\{e_{i}\right\}$ of the Lie algebra. Then by applying an orthogonal matrix to it, we can construct a basis $\left\{e_{i}^{\prime}\right\}$ such that the corresponding $n^{\prime}$ defined by (2) has diagonal elements of one of the types given in table 1.

Proof. Let $e_{i}$ be a basis for the Lie algebra and $n$ be defined as in (2). If we change the basis according to $e_{i}^{\prime}=\left(A^{-1}\right)_{i}{ }^{j} e_{j}$ then $n$ transforms to
$$n^{\prime}=(\operatorname{det} A)^{-1} A^{t} n A$$
Since $n$ is symmetric we assume from here on that the basis is such that it is diagonal. The matrix $A=\operatorname{diag}(11-1)$ changes the sign of $n$. A suitable orthogonal matrix performs even permutations of the diagonal. The number of nonzero elements on the diagonal is invariant under transformations (18) taking one diagonal matrix to another. If $A=\left(a_{i j}\right)$ and the diagonal matrix $n^{\prime}$ is constructed as in (18) we have $n_{k k}^{\prime}=(\operatorname{det} A)^{-1} \sum_{i=1}^{3} a_{i k}^{2} n_{i i}$ so that if all the diagonal elements of $n$ have the same sign the same is true for $n^{\prime}$. The statements of the lemma follow. \(\square\)

Consider class A vacuum initial data $(G, g, k)$ with notation as in Definition 1. We construct a spacetime of the form (9) whose induced metric and second fundamental form on $\{0\} \times G$ is $g$ and $k$. Let $e_{i}^{\prime}, i=1,2,3$ be a left invariant orthonormal basis. We can assume the corresponding $n^{\prime}$ to be of one of the forms given in table 1 by Lemma 3. The content of (4) is that $k_{i j}=k\left(e_{i}^{\prime}, e_{j}^{\prime}\right)$ and $n^{\prime}$ are to commute. We may thus also assume $k_{i j}$ to be diagonal without changing the earlier conditions of the construction. If we let $n(0)=n^{\prime}, \theta(0)=-\operatorname{tr}_{g} k$ and $\sigma_{i j}(0)=-k_{i j}+\theta \delta_{i j} / 3$ then (3) is the same as (15). Let $n, \sigma$ and $\theta$ satisfy (11), (13) and (14) with initial values as specified above. Since (15) is satisfied at $t=0$ it is satisfied for all times. For reasons given in connection with (15) $n$ and $\sigma$ will remain diagonal so that (12) will always hold.
Let $M=I \times G$ where $I$ is the maximal existence interval for solutions to (11)-(15) with initial data as above. We construct a basis $e_{\alpha}$ with the same properties as the basis used in deriving (11)-(15). Then we define a metric by demanding that the basis be orthonormal and show that the corresponding $\tilde{n}, \tilde{\sigma}$ and $\tilde{\theta}$ coincide with $n$, $\sigma$ and $\theta$. We will thereby have constructed a Lorentz manifold satisfying Einstein's vacuum equations with the correct initial conditions.

Let $n_{i}$ and $\sigma_{i}$ denote the diagonal elements of $n$ and $\sigma$ respectively. Let $f_{i}(0)=1$ and $\dot{f}_{i} / f_{i}=2 \sigma_{i}-\theta / 3$. Let $a_{i}=\left(\Pi_{j \neq i} f_{j}\right)^{1 / 2}$ and define $e_{i}=a_{i} e_{i}^{\prime}$. Then $\tilde{n}$ associated to $e_{i}$ equals $n$. We complete the basis by letting $e_{0}=\partial_{t}$. Define a metric $<\cdot, \cdot>$ on $M$ by demanding $e_{\alpha}$ to be orthonormal with $<e_{0}, e_{0}>=-1$ and $<e_{i}, e_{i}>=1$, $i=1,2,3$ and let ∇ be the associated Levi-Civita connection.
Compute $<\nabla_{e_{0}} e_{i}, e_{j}>=0$. If $\tilde{\theta}(X, Y)=<\nabla_{X} e_{0}, Y>$ and $\tilde{\theta}_{\mu \nu}=\tilde{\theta}\left(e_{\mu}, e_{\nu}\right)$, then $\tilde{\theta}_{00}=\tilde{\theta}_{i 0}=\tilde{\theta}_{0 i}=0$. Furthermore,
$$\frac{1}{a_{j}} e_{0}\left(a_{j}\right) \delta_{i j}=-\tilde{\theta}_{i j}$$
(no summation over $j$ ) so that $\tilde{\theta}_{i j}$ is diagonal and $\operatorname{tr} \tilde{\theta}=\theta$. Finally,
$$-\tilde{\sigma}_{i i}=-\tilde{\theta}_{i i}+\frac{1}{3} \theta=-\sigma_{i} .$$

The constructed Lorentz manifold thus satisfies Einstein's vacuum equations. By the above we have.

Lemma 4. Given initial data as in Definition 1, we get a solution to Einstein's equations
$$\bar{g}=-d t^{2}+\sum_{i=1}^{3} a_{i}^{-2}(t) \xi^{i} \otimes \xi^{i}$$
where $\xi^{i}$ are the duals of a basis of the Lie algebra of G and
$$a_{i}(t)=\exp \left(-\int_{0}^{t}\left(\sigma_{i}+\frac{1}{3} \theta\right) d s\right)$$
where $\theta, \sigma_{i}$ (and $n_{i}$ ) constitute solutions to (11)-(15) with suitable initial conditions. If $I$ is the corresponding existence interval, the metric (19) is defined on the manifold $I \times G$.

By [4] this metric is globally hyperbolic, future causally geodesically complete and $\tau \rightarrow \infty$ corresponds to the geodesically complete direction, assuming the initial data are not of type IX.
3.3. The rescaled metric. The equations (19) and (20) express the spacetime metric in terms of the Ellis-MacCallum variables. Let $g(t)$ denote the Riemannian metric induced on $\{t\} \times G$, which we will also consider to be a metric on $G$. Define a rescaled version of this metric by
$$\tilde{g}(t)=\left(a_{1} a_{2} a_{3}\right)^{2 / 3}(t) \sum_{i=1}^{3} a_{i}^{-2}(t) \xi^{i} \otimes \xi^{i} .$$
We can write it as
$$\tilde{g}(t)=\sum_{i=1}^{3} \lambda_{i}(t) \xi^{i} \otimes \xi^{i}$$
where
$$\lambda_{i}(t)=\exp \left(\int_{0}^{t} 2 \sigma_{i} d s\right)$$
Defining a new time coordinate by
$$\frac{d t}{d \tau}=\frac{3}{\theta}, \tau(0)=0$$
we get
$$\int_{0}^{t} 2 \sigma_{i} d s=\int_{0}^{\tau} 2 \sigma_{i} \frac{3}{\theta} d \tau^{\prime}=\int_{0}^{\tau} 6 \Sigma_{i} d \tau^{\prime}$$
Thus if we consider the $\lambda_{i}$ to be functions of $\tau$ we have
$$\lambda_{i}(\tau)=\exp \left(\int_{0}^{\tau} 6 \Sigma_{i} d \tau^{\prime}\right) .$$
Similarly,
$$a_{i}(\tau)=\exp \left(-\int_{0}^{\tau}\left(3 \Sigma_{i}+1\right) d s\right)$$

However, the $\Sigma_{i}$ can be expressed in terms of $\Sigma_{+}$and $\Sigma_{-}$. We have
$$\Sigma_{1}=-\frac{2}{3} \Sigma_{+}, \Sigma_{2}=\frac{1}{3} \Sigma_{+}+\frac{1}{\sqrt{3}} \Sigma_{-}, \Sigma_{3}=\frac{1}{3} \Sigma_{+}-\frac{1}{\sqrt{3}} \Sigma_{-} .$$
Thus, if we know what $\Sigma_{+}$and $\Sigma_{-}$converge to as $\tau \rightarrow \infty$, we roughly know how $\tilde{g}$ behaves asymptotically.
3.4. The reduced Hamiltonian. As mentioned in the introduction, there is in some situations a subgroup $\Gamma$ of the group of diffeomorphisms of $G$, acting properly discontinuously on $G$, such that $g(t)$ is invariant under $\Gamma$ for all $t$. In such situations, we can consider $g$ to be a metric on $M=G / \Gamma$. Observe however that the basis $e_{i}^{\prime}$ need not necessarily descend to a basis on $M$. Let us assume $M$ to be compact. We can then consider the reduced Hamiltonian
$$H(t)=-[-\theta(t)]^{3} V(t)$$
where $V(t)=\operatorname{vol}(M, g(t))$.
Lemma 5. In terms of the time coordinate $\tau$ defined by (23) we have
$$H(\tau)=\theta^{3}(0) V(0) \exp \left(-3 \int_{0}^{\tau} q d s\right)$$
Proof. Since $M$ is compact we can choose a finite partition of unity $\phi_{i} i=1, \ldots, k$ subordinated to coordinate charts. We can then write
$$V(t)=\sum_{i=1}^{k} \int_{M} \phi_{i} \sqrt{\operatorname{det} g(t)\left(\partial_{j}, \partial_{m}\right)} d x^{1} \ldots d x^{3} .$$
We compute
$$\frac{d V}{d t}=\theta V$$
so that
$$\frac{d V}{d \tau}=\theta V \frac{d t}{d \tau}=\theta V \frac{3}{\theta}=3 V .$$
Considering $H$ as a function of $\tau$, we get (27) using (17). □

\section*{4. Bianchi I}

Bianchi I solutions of (5)-(7) are of the form $\left(\sigma_{+}, \sigma_{-}, 0,0,0\right)$ where $\left(\sigma_{+}, \sigma_{-}\right)$are independent of time and satisfy $\sigma_{+}^{2}+\sigma_{-}^{2}=1$.

\section*{5. Bianchi II}

Proposition 1. A Bianchi II solution of (5)-(7) with $N_{1}>0$ and $N_{2}=N_{3}=0$ satisfies
$$\lim _{\tau \rightarrow \infty} N_{1}=0$$
and
$$\lim _{\tau \rightarrow \infty}\left(\Sigma_{+}, \Sigma_{-}\right)=\left(\sigma_{+}, \sigma_{-}\right)$$
where $\left(\sigma_{+}, \sigma_{-}\right)$belongs to $\mathcal{K}_{1}$.

Proof. Using the constraint (7) we deduce that
$$\Sigma_{+}^{\prime}=\frac{3}{2} N_{1}^{2}\left(2-\Sigma_{+}\right) .$$
We wish to apply the monotonicity principle. There are three variables. Let $U$ be defined by $N_{1}>0, M$ be defined by (7) and $F\left(\Sigma_{+}, \Sigma_{-}, N_{1}\right)=\Sigma_{+}$. Equation (28) follows, since if $N_{1}$ does not converge to zero, we can construct an $\omega$-limit point in $U$ due to the fact that the variables are contained in a compact set. Combining this with the constraint we deduce
$$\lim _{\tau \rightarrow \infty} q=2 .$$
Since $\Sigma_{+}$is monotone and bounded, it converges. Since $q \rightarrow 2$ and the $\omega$-limit set is connected, c.f. Lemma 1, (29) holds, but we do not yet know anything about the limit. Compute
$$\left(\frac{\Sigma_{-}}{2-\Sigma_{+}}\right)^{\prime}=0 .$$
We get
$$\frac{\Sigma_{-}}{2-\Sigma_{+}}=\frac{\sigma_{-}}{2-\sigma_{+}}$$
for arbitrary $\left(\Sigma_{+}, \Sigma_{-}\right)$belonging to the solution. Since $N_{1}^{\prime}=\left(q-4 \Sigma_{+}\right) N_{1}$ and $N_{1} \rightarrow 0$ we have to have $\sigma_{+} \geq \frac{1}{2}$. If $\sigma_{+}=\frac{1}{2}$ then $\sigma_{-}= \pm \frac{\sqrt{3}}{2}$. The two corresponding lines in the $\Sigma_{+} \Sigma_{-}$-plane obtained by substituting $\left(\sigma_{+}, \sigma_{-}\right)$into (30) do not intersect any points interior to the Kasner circle. Therefore $\sigma_{+}=\frac{1}{2}$ is not an allowed limit point and the proposition follows. □

\section*{6. Bianchi $\mathrm{VI}_{0}$}

Proposition 2. Consider a Bianchi $V I_{0}$ solution of (5)-(7) with $N_{1}=0, N_{2}>0$ and $N_{3}<0$. Then
$$\lim _{\tau \rightarrow \infty} N_{2}=0, \lim _{\tau \rightarrow \infty} N_{3}=0$$
and
$$\lim _{\tau \rightarrow \infty} \Sigma_{-}=0, \lim _{\tau \rightarrow \infty} \Sigma_{+}=-1 .$$
Proof. By the constraint (7) the variables belong to a compact set. Since
$$\Sigma_{+}^{\prime}=-(2-q)\left(1+\Sigma_{+}\right)$$
$\Sigma_{+}$is strictly monotone as long as $q<2$ which is true for the entire solution. The monotonicity principle yields
$$\lim _{\tau \rightarrow \infty} q=2$$
for similar reasons as in the proof of Proposition 1. By the constraint we conclude that (31) holds. Since $\Sigma_{+}$is monotone, (33) holds and the $\omega$-limit set is connected, we have
$$\lim _{\tau \rightarrow \infty}\left(\Sigma_{+}, \Sigma_{-}\right)=\left(\sigma_{+}, \sigma_{-}\right)$$
with $\sigma_{+}^{2}+\sigma_{-}^{2}=1$. Since $N_{2}$ and $N_{3}$ converge to zero and since they satisfy (5) we must have
$$\begin{aligned}
& 2\left(\sigma_{+}^{2}+\sigma_{-}^{2}\right)+2 \sigma_{+}+2 \sqrt{3} \sigma_{-} \leq 0 \\
& 2\left(\sigma_{+}^{2}+\sigma_{-}^{2}\right)+2 \sigma_{+}-2 \sqrt{3} \sigma_{-} \leq 0 .
\end{aligned}$$
Adding these inequalities we obtain $4+4 \sigma_{+} \leq 0$. Equation (32) follows. \(\square\)

Let us now record the fact that Bianchi VIII is very different from Bianchi IX in the direction towards the singularity.

Proposition 3. For every $\epsilon>0$, there exists Bianchi VIII vacuum initial data $y_{\epsilon}$ and a real number $T_{\epsilon}>0$, where $y_{\epsilon}$ is closer to the Kasner circle than $\epsilon$, such that evolving $y_{\epsilon}$ a time $T_{\epsilon}$ to the past yields a Bianchi VIII point with the property that
$$\left|N_{1} N_{2}\right|+\left|N_{2} N_{3}\right|+\left|N_{3} N_{1}\right| \geq \frac{1}{4} .$$
Remark. By distance to the Kasner circle we here mean the Euclidean distance in $\mathbb{R}^{5}$.

Proof. Let $\epsilon>0$ and $x$ be any Bianchi $\mathrm{VI}_{0}$ initial data. By Proposition 2, there is a $T_{\epsilon}>0$ such that applying the flow to $x, \Phi\left(T_{\epsilon}, x\right)$ is closer to the Kasner circle than $\epsilon / 2$, where $\Phi(\tau, x)$ represents the solution to (5)-(7) with initial data $x$ evaluated in $\tau$. However, there are Bianchi VIII points as close to $\Phi\left(T_{\epsilon}, x\right)$ as we wish. Given an $\eta>0$, we can thus, by the continuity of the flow, choose Bianchi VIII initial data $y_{\epsilon}$ with the property that $y_{\epsilon}$ is closer to the Kasner circle than $\epsilon$ and $\Phi\left(-T_{\epsilon}, y_{\epsilon}\right)$ is closer to $x$ than $\eta$. Choosing $x$ to have $\Sigma_{+}=\Sigma_{-}=0$ and $N_{2}=-N_{3}=\frac{1}{\sqrt{3}}$ and letting $\eta$ be small enough, we get the conclusion of the proposition. □

\section*{7. Bianchi $\mathrm{VII}_{0}$}

The following proposition is a consequence of (5)-(7).
Proposition 4. Consider a Bianchi VII ${ }_{0}$ solution to (5)-(7) with $N_{2}=N_{3}>0$, $N_{1}=0$ and $\Sigma_{-}=0$. Then one of the following statements holds
\begin{itemize}
\item[-] $\Sigma_{+}=1$ for the entire solution and $N_{2}=N_{3} \rightarrow \infty$ as $\tau \rightarrow \infty$.
\item[-] $\Sigma_{+}=-1$ and $N_{2}=N_{3}$ are constant for the entire solution.
\end{itemize}
Given a solution to (5)-(7), if $N_{2}(\tau)=N_{3}(\tau)$ and $\Sigma_{-}(\tau)=0$ for one $\tau$ then the two equalities hold for all $\tau$. Thus the above proposition together with the one below exhaust the possibilities for Bianchi $\mathrm{VII}_{0}$ solutions.

Proposition 5. Consider a Bianchi VII ${ }_{0}$ solution to (5)-(7) with $N_{2}, N_{3}>0$ and $N_{1}=0$ which never satisfies $N_{2}=N_{3}$ and $\Sigma_{-}=0$ simultaneously. Then
$$\lim _{\tau \rightarrow \infty} \Sigma_{+}=-1, \lim _{\tau \rightarrow \infty} \Sigma_{-}=0$$
and
$$\lim _{\tau \rightarrow \infty}\left(N_{2}-N_{3}\right)=0 .$$
Remark. In Proposition 6, we also prove that $N_{2}$ and $N_{3}$ converge to finite positive values.

Proof. Assume first that there is an $\boldsymbol{\omega}$-limit point. Then the monotonicity principle suffices. Consider
$$\Sigma_{+}^{\prime}=-(2-q)\left(\Sigma_{+}+1\right) .$$
We apply the monotonicity principle with $F\left(\Sigma_{+}, \Sigma_{-}, N_{2}, N_{3}\right)=\Sigma_{+}, M$ defined by (7) and $U$ defined by $\Sigma_{-}^{2}+\left(N_{2}-N_{3}\right)^{2}>0$ and $N_{2}+N_{3}>0 . F$ is strictly monotone on a solution in $U \cap M$ since if $\Sigma_{+}^{\prime}(\tau)=0$ then $\left[N_{2}-N_{3}\right](\tau)=0$ so that $\Sigma_{-}(\tau) \neq 0$ whence $\left[N_{2}-N_{3}\right]^{\prime}(\tau) \neq 0$, c.f. (5)-(7). If $\tau_{k} \rightarrow \infty$ yields an $\omega$-limit point, we must thus have $\left[\Sigma_{-}^{2}+\left(N_{2}-N_{3}\right)^{2}\right]\left(\tau_{k}\right) \rightarrow 0$ or $\left(N_{2}+N_{3}\right)\left(\tau_{k}\right) \rightarrow 0$ by the monotonicity principle. However
$$Z_{-1}=\frac{\frac{4}{3} \Sigma_{-}^{2}+\left(N_{2}-N_{3}\right)^{2}}{N_{2} N_{3}}=\frac{\frac{4}{3}\left(1-\Sigma_{+}^{2}\right)}{N_{2} N_{3}}$$
has non-positive derivative, and consequently $\left[\Sigma_{-}^{2}+\left(N_{2}-N_{3}\right)^{2}\right]\left(\tau_{k}\right) \rightarrow 0$ (if it does not converge to zero, $Z_{-1}\left(\tau_{k}\right) \rightarrow \infty$ ). We conclude that $\Sigma_{+}\left(\tau_{k}\right) \rightarrow-1$. By the monotonicity of $\Sigma_{+}$the proposition follows.
Assume that there is no $\omega$-limit point. If there is a sequence $\tau_{k} \rightarrow \infty$ such that $N_{2}\left(\tau_{k}\right)$ is bounded, then there is an $\omega$-limit point by the constraint (7). Similarly if there is a sequence such that $N_{3}$ is bounded. We can thus assume that $N_{2}$ and $N_{3}$ converge to $\infty$.
The variable $\Sigma_{+}$is still decreasing and bounded. We can thus assume it to converge to $\sigma_{+}$with $-1 \leq \sigma_{+}<1$. If $\sigma_{+}=-1$ we are done so assume not. We prove that this assumption leads to the consequence that $(2-q) \notin L^{1}([0, \infty))$. Combining this with (34) we conclude that $\Sigma_{+} \rightarrow-1$ contradicting our assumption.
The intuitive idea is as follows. $\Sigma_{+} \rightarrow \sigma_{+}$but $\Sigma_{-}$will oscillate between $\pm(1-$ $\left.\sigma_{+}^{2}\right)^{1 / 2}$, roughly speaking. When $\Sigma_{-}$is small we get a contribution to the integral of $2-q$. If $\Sigma_{-}$spends most of its time close to $\pm\left(1-\sigma_{+}^{2}\right)^{1 / 2}$ we would have a problem, but that turns out not to be the case.
If $N_{2}$ and $N_{3}$ converge to infinity, we will see that the solution will become oscillatory. To be more precise, let $x$ and $y$ be defined by
$$\begin{aligned}
x & =\frac{\Sigma_{-}}{\left(1-\Sigma_{+}^{2}\right)^{1 / 2}} \\
y & =\frac{\sqrt{3}}{2} \frac{N_{2}-N_{3}}{\left(1-\Sigma_{+}^{2}\right)^{1 / 2}} .
\end{aligned}$$
Since $\Sigma_{+}^{2}(\tau)<1$ for all $\tau, x$ and $y$ are smooth. Let
$$g=3\left(N_{2}+N_{3}\right)+2\left(1+\Sigma_{+}\right) x y .$$
Then $x^{\prime}=-g y$ and $y^{\prime}=g x$. By the constraint $x^{2}+y^{2}=1$ so that we can choose a $\phi_{0}$ such that $\left(x\left(\tau_{0}\right), y\left(\tau_{0}\right)\right)=\left(\cos \left(\phi_{0}\right), \sin \left(\phi_{0}\right)\right)$. Define
$$\xi(\tau)=\int_{\tau_{0}}^{\tau} g(s) d s+\phi_{0}$$
Then $x(\tau)=\cos (\xi(\tau))$ and $y(\tau)=\sin (\xi(\tau))$.
As mentioned it suffices to prove that $2-q \notin L^{1}([0, \infty))$ under the assumption that $-1<\sigma_{+}<1$. Consider
$$2-q=2\left(1-\Sigma_{+}^{2}-\left(1-\Sigma_{+}^{2}\right) \cos ^{2}(\xi)\right)=2\left(1-\Sigma_{+}^{2}\right) \sin ^{2}(\xi) \geq 2\left(1-\sigma_{+}^{2}\right) \sin ^{2}(\xi)$$
$$=c \sin ^{2}(\xi),$$
where $c>0$ by assumption. Consider a period. Assume $T$ is great enough that $1<5\left(N_{2}+N_{3}\right) / 2 \leq g \leq 7\left(N_{2}+N_{3}\right) / 2$ for $\tau \geq T$ and that $\xi\left(\tau_{2}\right)-\xi\left(\tau_{1}\right)=2 \pi$ where $T \leq \tau_{1}<\tau_{2}$. Let us estimate $\Delta \tau=\tau_{2}-\tau_{1}$. By considering (38) we conclude that $\Delta \tau$ can be chosen arbitrarily small if $T$ is great enough since $N_{2}, N_{3} \rightarrow \infty$. Using (5) we derive the consequence that for every $\epsilon>0$
$$1-\epsilon \leq \frac{\left(N_{2}+N_{3}\right)(\tau)}{\left(N_{2}+N_{3}\right)\left(\tau_{1}\right)} \leq 1+\epsilon$$
for every $\tau \in\left[\tau_{1}, \tau_{2}\right]$ if $T$ is great enough. Thus
$$\Delta \tau=\int_{\tau_{1}}^{\tau_{2}} d \tau=\int_{\xi\left(\tau_{1}\right)}^{\xi\left(\tau_{2}\right)} \frac{1}{g} d \xi \leq \int_{\xi\left(\tau_{1}\right)}^{\xi\left(\tau_{2}\right)} \frac{2}{5\left(N_{2}+N_{3}\right)} d \xi \leq \frac{8 \pi}{5\left(N_{2}+N_{3}\right)\left(\tau_{1}\right)}$$
if $T$ is great enough. But then
$$\begin{gathered}
\int_{\tau_{1}}^{\tau_{2}}(2-q) d \tau \geq \int_{\tau_{1}}^{\tau_{2}} c \sin ^{2}(\xi) d \tau=\int_{\xi\left(\tau_{1}\right)}^{\xi\left(\tau_{2}\right)} c \sin ^{2}(\xi) \frac{1}{g} d \xi \\
\geq \int_{\xi\left(\tau_{1}\right)}^{\xi\left(\tau_{2}\right)} c \sin ^{2}(\xi) \frac{2}{7\left(N_{2}+N_{3}\right)} d \xi \geq \frac{c}{7\left(N_{2}+N_{3}\right)\left(\tau_{1}\right)} \int_{\xi\left(\tau_{1}\right)}^{\xi\left(\tau_{2}\right)} \sin ^{2}(\xi) d \xi \\
=\frac{c \pi}{7\left(N_{2}+N_{3}\right)\left(\tau_{1}\right)} \geq \frac{5 c}{56} \Delta \tau=c^{\prime} \Delta \tau
\end{gathered}$$
if $T$ is great enough. Here $c^{\prime}>0$. Let $M>0$ be any number. Consider an interval $\left[\tau_{a}, \tau_{b}\right]$ where $\tau_{a}$ is great enough that the above conditions are met, $\left(\tau_{b}-\tau_{a}\right) / c^{\prime}>M$ and $\xi\left(\tau_{b}\right)-\xi\left(\tau_{a}\right)$ is an integer multiple of $2 \pi$. Then
$$\int_{\tau_{a}}^{\tau_{b}}(2-q) d \tau \geq M$$
and consequently $2-q \notin L^{1}([0, \infty))$. The proposition follows. □
It will be of interest to know that $N_{2}$ is bounded away from zero.
Lemma 6. Consider a Bianchi $V I I_{0}$ solution to (5)-(7). Then
$$N_{2} N_{3} \geq c>0$$
on $[0, \infty)$, where $c$ is a positive constant.
Proof. Assume there is a time sequence $\tau_{k} \rightarrow \infty$ such that $\left(N_{2} N_{3}\right)\left(\tau_{k}\right)$ converges to zero. Since $N_{2}-N_{3} \rightarrow 0$, we conclude that the solution evaluated at $\tau_{k}$ converges to the Kasner circle. Since the flow is continuous, and Bianchi $\mathrm{VII}_{0}$ belongs to the boundary of Bianchi IX, we can construct a sequence of Bianchi IX initial data $x_{k}$ converging to the Kasner circle, such that $\Phi\left(-\tau_{k}, x_{k}\right)$ converges to a Bianchi $\mathrm{VII}_{0}$ point with $N_{2} N_{3}>0$. This is impossible by Theorem 15.1 of [4]. □
As was noted in the proof of Proposition 5, the objects $x$ and $y$ defined in (35) and (36) can be written as
$$x(\tau)=\cos \xi(\tau), \quad y(\tau)=\sin \xi(\tau)$$
where $\xi$ is defined in (38). Since $N_{2}+N_{3}$ is bounded away from zero to the future by Lemma 6 and $1+\Sigma_{+}$converges to zero, we can assume that
$$g(\tau) \geq 2\left(N_{2}+N_{3}\right)(\tau) \geq c>0 \quad \forall \tau \geq \tau_{0}$$
for some positive constant $c$, where $g$ is defined by (37). In other words, the expressions $x$ and $y$ will carry out an infinite number of oscillations as time progresses. It is natural to average over a period of this oscillation in order to analyze the asymptotics, and we need to know how certain expressions vary over a period to be able to do this.

In the rest of this section we will implicitly assume that all Bianchi $\mathrm{VII}_{0}$ solutions satisfy $\Sigma_{-}^{2}+\left(N_{2}-N_{3}\right)^{2}>0$.

Lemma 7. Consider a Bianchi VII ${ }_{0}$ solution to (5)-(7) with $N_{2}, N_{3}>0$, and let $\tau_{0}$ be such that (39) is fulfilled. Let $\tau_{0} \leq \tau_{a}<\tau_{b}$, and assume
$$\xi\left(\tau_{b}\right)-\xi\left(\tau_{a}\right)=\pi .$$
Then there is a $T$ such that
$$\left|1-\frac{\left(1+\Sigma_{+}\right)\left(\tau_{1}\right)}{\left(1+\Sigma_{+}\right)\left(\tau_{2}\right)}\right| \leq C \frac{\left(1+\Sigma_{+}\right)\left(\tau_{b}\right)}{\left(N_{2}+N_{3}\right)\left(\tau_{\max }\right)}$$
and
$$\left|1-\frac{\left(N_{2}+N_{3}\right)\left(\tau_{1}\right)}{\left(N_{2}+N_{3}\right)\left(\tau_{2}\right)}\right| \leq C \frac{\left(1+\Sigma_{+}\right)\left(\tau_{b}\right)}{\left(N_{2}+N_{3}\right)\left(\tau_{\max }\right)}$$
if $\tau_{a} \geq T$, where $\tau_{\text {max }}$ yields the maximum value of $N_{2}+N_{3}$ in $\left[\tau_{a}, \tau_{b}\right]$ and $\tau_{1}, \tau_{2}$ are arbitrary members of $\left[\tau_{a}, \tau_{b}\right]$. The constant $C$ only depends on the constant $c$ appearing in (39).

Proof. Observe that
$$\pi=\int_{\tau_{a}}^{\tau_{b}} g(s) d s \geq c\left(\tau_{b}-\tau_{a}\right)$$
so that
$$\tau_{b}-\tau_{a} \leq \frac{\pi}{c} .$$
Consider
$$\left(N_{2}+N_{3}\right)^{\prime}=\left(q+2 \Sigma_{+}\right)\left(N_{2}+N_{3}\right)+2 \sqrt{3} \Sigma_{-}\left(N_{2}-N_{3}\right) .$$
Estimate
$$\left|q+2 \Sigma_{+}\right| \leq 2\left|\Sigma_{+}\left(1+\Sigma_{+}\right)\right|+2 \Sigma_{-}^{2} \leq 2\left(1+\Sigma_{+}\right)+2\left(1-\Sigma_{+}^{2}\right) \leq 6\left(1+\Sigma_{+}\right),$$
and
$$\left|2 \sqrt{3} \Sigma_{-}\left(N_{2}-N_{3}\right)\right| \leq 2\left[\Sigma_{-}^{2}+\frac{3}{4}\left(N_{2}-N_{3}\right)^{2}\right] \leq 2\left(1-\Sigma_{+}^{2}\right) \leq 4\left(1+\Sigma_{+}\right) .$$
Since $N_{2}+N_{3}$ is bounded below by a positive constant for $\tau \geq \tau_{0}$, we conclude that
$$\left|\left(N_{2}+N_{3}\right)^{\prime}\right| \leq C_{1}\left(1+\Sigma_{+}\right)\left(N_{2}+N_{3}\right)$$
for some positive constant $C_{1}$. Letting $\tau_{1}, \tau_{2} \in\left[\tau_{a}, \tau_{b}\right]$, we get
$$\ln \alpha=\ln \left(\frac{\left(N_{2}+N_{3}\right)\left(\tau_{1}\right)}{\left(N_{2}+N_{3}\right)\left(\tau_{2}\right)}\right) \leq C_{1} \int_{\tau_{a}}^{\tau_{b}}\left(1+\Sigma_{+}\right) d s=\beta,$$
where we have introduced the quantities $\alpha$ and $\beta$ in order to make the following arguments easier to follow. If $\alpha \geq 1$, then
$$0 \leq \alpha-1 \leq e^{\beta}-1=\sum_{k=1}^{\infty} \frac{\beta^{k}}{k!} \leq \beta e^{\beta} .$$
If $\alpha \leq 1$, then (44) also holds if we replace $\alpha$ with $1 / \alpha$, since $\tau_{1}$ and $\tau_{2}$ in (43) are arbitrary. Multiplying this inequality with $\alpha$ then yields the conclusion
$$|1-\alpha| \leq \beta e^{\beta}$$
without any conditions on $\alpha$. Since we have the bound (42) and $0 \leq 1+\Sigma_{+} \leq 2$, we conclude that $e^{\beta}$ is bounded by a constant, so that
$$\left|1-\frac{\left(N_{2}+N_{3}\right)\left(\tau_{1}\right)}{\left(N_{2}+N_{3}\right)\left(\tau_{2}\right)}\right| \leq C_{2} \int_{\tau_{a}}^{\tau_{b}}\left(1+\Sigma_{+}\right) d s$$
Observe that this inequality proves that the left hand side can be chosen to be arbitrarily small by demanding $\tau_{a}$ to be big enough. Let us estimate the integral on the right hand side. Assuming $\tau_{a}$ to be great enough that the right hand side of (45) is less than $\frac{1}{2}$, and using (39) and the fact that $\Sigma_{+}$is monotone, we conclude that
$$\begin{gathered}
\int_{\tau_{a}}^{\tau_{b}}\left(1+\Sigma_{+}\right) d s \leq\left(1+\Sigma_{+}\right)\left(\tau_{a}\right) \int_{\xi\left(\tau_{a}\right)}^{\xi\left(\tau_{b}\right)} \frac{1}{g} d \xi \leq\left(1+\Sigma_{+}\right)\left(\tau_{a}\right) \int_{\xi\left(\tau_{a}\right)}^{\xi\left(\tau_{b}\right)} \frac{1}{2\left(N_{2}+N_{3}\right)} d \xi \\
\leq \frac{3 \pi}{4} \frac{\left(1+\Sigma_{+}\right)\left(\tau_{a}\right)}{\left(N_{2}+N_{3}\right)\left(\tau_{\max }\right)}
\end{gathered}$$
where $\tau_{\text {max }}$ corresponds to the maximum value of $N_{2}+N_{3}$ in $\left[\tau_{1}, \tau_{2}\right]$. Combining this with (45) we get
$$\left|1-\frac{\left(N_{2}+N_{3}\right)\left(\tau_{1}\right)}{\left(N_{2}+N_{3}\right)\left(\tau_{2}\right)}\right| \leq C_{3} \frac{\left(1+\Sigma_{+}\right)\left(\tau_{a}\right)}{\left(N_{2}+N_{3}\right)\left(\tau_{\max }\right)} .$$
Consider now
$$\left(1+\Sigma_{+}\right)^{\prime}=-(2-q)\left(1+\Sigma_{+}\right)$$
Since
$$0 \leq 2-q \leq 4\left(1+\Sigma_{+}\right),$$
we conclude that
$$\left|1-\frac{\left(1+\Sigma_{+}\right)\left(\tau_{1}\right)}{\left(1+\Sigma_{+}\right)\left(\tau_{2}\right)}\right| \leq C_{3} \frac{\left(1+\Sigma_{+}\right)\left(\tau_{a}\right)}{\left(N_{2}+N_{3}\right)\left(\tau_{\max }\right)}$$
by an argument similar to that proving (46). By assuming $\tau_{a}$ to be big enough (48) leads to the conclusion that we, at the cost of increasing the constants, can replace $\left(1+\Sigma_{+}\right)\left(\tau_{a}\right)$ in the right hand side of (46) and (48) with the same expression evaluated in $\tau_{b}$, yielding the statement of the lemma. □

The following lemma constitutes the main observation.
Lemma 8. Consider a Bianchi VII ${ }_{0}$ solution to (5)-(7) with $N_{2}, N_{3}>0$, and let $\tau_{0}$ be such that (39) is fulfilled. Let $\tau_{0} \leq \tau_{a}<\tau_{b}$, and assume
$$\xi\left(\tau_{b}\right)-\xi\left(\tau_{a}\right)=\pi .$$

Then there is a $T$ such that
$$\left|\int_{\tau_{a}}^{\tau_{b}}\left[\Sigma_{-}^{2}-\left(1+\Sigma_{+}\right)\right] d s\right| \leq C \int_{\tau_{a}}^{\tau_{b}}\left(1+\Sigma_{+}\right)^{2} d s$$
if $\tau_{a} \geq T$, for some constant $C$ depending only on the constant $c$ appearing in (39).
Proof. Observe first that
$$\Sigma_{-}^{2}=\left(1-\Sigma_{+}^{2}\right) x^{2}=\left(1-\Sigma_{+}\right)\left(1+\Sigma_{+}\right) x^{2}=2\left(1+\Sigma_{+}\right) x^{2}-\left(1+\Sigma_{+}\right)^{2} x^{2} .$$
In consequence, the integrand of interest is
$$2\left(1+\Sigma_{+}\right) x^{2}-\left(1+\Sigma_{+}\right)=\left(1+\Sigma_{+}\right) \cos \eta$$
where $\eta(\tau)=2 \xi(\tau)$. Let $\eta_{a}=\eta\left(\tau_{a}\right)$ and $\eta_{b}=\eta\left(\tau_{b}\right)=\eta_{a}+2 \pi$ and observe that
$$\begin{aligned}
& \int_{\tau_{a}}^{\tau_{b}}\left(1+\Sigma_{+}\right) \cos \eta d \tau=\int_{\eta_{a}}^{\eta_{b}} \frac{1+\Sigma_{+}}{2 g} \cos \eta d \eta \\
= & \int_{\eta_{a}}^{\eta_{a}+\pi}\left(\frac{1+\Sigma_{+}(\eta)}{2 g(\eta)}-\frac{1+\Sigma_{+}(\eta+\pi)}{2 g(\eta+\pi)}\right) \cos \eta d \eta
\end{aligned}$$
where we in order to obtain the last equality divided the integral into one part from $\eta_{a}$ to $\eta_{a}+\pi$ and one from $\eta_{a}+\pi$ to $\eta_{a}+2 \pi$, and then made the substitution $\eta \rightarrow \eta-\pi$ in the second integral. We now wish to prove that the absolute value of the integrand in the integral from $\eta_{a}$ to $\eta_{a}+\pi$ can be bounded by
$$C_{1} \frac{\left[1+\Sigma_{+}(\eta)\right]^{2}}{2 g(\eta)}+C_{2} \frac{\left[1+\Sigma_{+}(\eta+\pi)\right]^{2}}{2 g(\eta+\pi)},$$
since this would prove the assertion. Let us first rewrite
$$\frac{1+\Sigma_{+}(\eta)}{2 g(\eta)}-\frac{1+\Sigma_{+}(\eta+\pi)}{2 g(\eta+\pi)}=\frac{1+\Sigma_{+}(\eta)}{2 g(\eta)}\left(1-\frac{g(\eta)}{g(\eta+\pi)}\right)-\frac{\Sigma_{+}(\eta+\pi)-\Sigma_{+}(\eta)}{2 g(\eta+\pi)} .$$
Using (40) and the fact that $N_{2}+N_{3}$ is bounded from below by a positive constant, we note that the second term can be estimated in the desired way; multiply (40) by $1+\Sigma_{+}\left(\tau_{2}\right)$ in order to get an estimate of $\Sigma_{+}\left(\tau_{1}\right)-\Sigma_{+}\left(\tau_{2}\right)$. If we had
$$1-\frac{\left(N_{2}+N_{3}\right)(\eta)}{\left(N_{2}+N_{3}\right)(\eta+\pi)}$$
instead of
$$1-\frac{g(\eta)}{g(\eta+\pi)}$$
in the first term, then we could estimate the first term in the desired way as well. However, using (40), (41) and the fact that $g$ and $N_{2}+N_{3}$ can be bounded from below by a positive constant, one can show that
$$\frac{\left(N_{2}+N_{3}\right)(\eta)}{\left(N_{2}+N_{3}\right)(\eta+\pi)}-\frac{g(\eta)}{g(\eta+\pi)}$$
is small enough to yield the desired bound. □
Lemma 9. Consider a Bianchi VII ${ }_{0}$ solution to (5)-(7) with $N_{2}, N_{3}>0$, and let $\tau_{0}$ be such that (39) is fulfilled. Then
$$\lim _{\tau \rightarrow \infty} \frac{\int_{\tau_{0}}^{\tau} \Sigma_{-}^{2} d s}{\int_{\tau_{0}}^{\tau}\left(1+\Sigma_{+}\right) d s}=1$$
and
$$\lim _{\tau \rightarrow \infty} \frac{\int_{\tau_{0}}^{\tau}(2-q) d s}{\int_{\tau_{0}}^{\tau} 2\left(1+\Sigma_{+}\right) d s}=1$$
Proof. Observe first that since (47) is fulfilled and $1+\Sigma_{+} \rightarrow 0$ as $\tau \rightarrow \infty, 2-q \notin$ $L^{1}\left(\left[\tau_{0}, \infty\right)\right)$. Moreover,
$$2-q \leq 2\left(1-\Sigma_{+}^{2}\right) \leq 4\left(1+\Sigma_{+}\right),$$
so that $1+\Sigma_{+} \notin L^{1}\left(\left[\tau_{0}, \infty\right)\right)$. In order to prove (50), let us prove that
$$\lim _{\tau \rightarrow \infty} \frac{\int_{\tau_{0}}^{\tau}\left[\Sigma_{-}^{2}-\left(1+\Sigma_{+}\right)\right] d s}{\int_{\tau_{0}}^{\tau}\left(1+\Sigma_{+}\right) d s}=0$$
Let $\epsilon>0$ and let $T$ be such that Lemma 8 can be applied and such that $1+\Sigma_{+}(\tau) \leq$ $\epsilon /(2 C)$ for $\tau \geq T$, where $C$ is the constant appearing in (49). Given $\tau>T$, let $\tau_{1}$ be the greatest number smaller than $\tau$ such that $\xi\left(\tau_{1}\right)-\xi(T)$ is an integer multiple of $\pi$. We have
$$\begin{aligned}
\left|\int_{\tau_{0}}^{\tau}\left[\Sigma_{-}^{2}-\left(1+\Sigma_{+}\right)\right] d s\right| \leq & \int_{\tau_{0}}^{T}\left|\Sigma_{-}^{2}-\left(1+\Sigma_{+}\right)\right| d s+\left|\int_{T}^{\tau_{1}}\left[\Sigma_{-}^{2}-\left(1+\Sigma_{+}\right)\right] d s\right| \\
& +\int_{\tau_{1}}^{\tau}\left|\Sigma_{-}^{2}-\left(1+\Sigma_{+}\right)\right| d s .
\end{aligned}$$
We should divide this expression with $\int_{\tau_{0}}^{\tau}\left(1+\Sigma_{+}\right) d s$, and then evaluate the limit as $\tau \rightarrow \infty$. After having carried out this division, the first and the third terms will yield something that can be assumed to be arbitrarily small by assuming $\tau$ to be big enough. Using (49), the middle term can be bounded by
$$\begin{aligned}
\left|\int_{T}^{\tau_{1}}\left[\Sigma_{-}^{2}-\left(1+\Sigma_{+}\right)\right] d s\right| \leq & C \int_{T}^{\tau_{1}}\left(1+\Sigma_{+}\right)^{2} d s \leq C\left[1+\Sigma_{+}(T)\right] \int_{T}^{\tau_{1}}\left(1+\Sigma_{+}\right) d s \\
& \leq \frac{\epsilon}{2} \int_{T}^{\tau_{1}}\left(1+\Sigma_{+}\right) d s
\end{aligned}$$
After having carried out the division, the corresponding contribution can consequently be assumed to be less than or equal to $\epsilon / 2$. Equation (50) follows. In order to prove (51), observe that
$$(2-q)-2\left(1+\Sigma_{+}\right)=2\left(1+\Sigma_{+}\right)-2 \Sigma_{-}^{2}-2\left(1+\Sigma_{+}\right)^{2} .$$
In consequence the proof of (51) is similar to the proof of (50). □
Lemma 10. Consider a Bianchi VII ${ }_{0}$ solution to (5)-(7) with $N_{2}, N_{3}>0$, and let $\tau_{0}$ be such that (39) is fulfilled. Then, if $p>1$,
$$1+\Sigma_{+} \in L^{p}\left(\left[\tau_{0}, \infty\right)\right) .$$
Proof. By (51) we conclude that for each $\alpha_{1}<2<\alpha_{2}$, there is a $T$ such that $\tau \geq T$ implies
$$\alpha_{1}<\frac{\int_{\tau_{0}}^{\tau}(2-q) d s}{\int_{\tau_{0}}^{\tau}\left(1+\Sigma_{+}\right) d s}<\alpha_{2}$$
Introduce the notation
$$\alpha=1+\Sigma_{+}\left(\tau_{0}\right)$$
and
$$h(\tau)=\int_{\tau_{0}}^{\tau}\left[1+\Sigma_{+}(s)\right] d s$$
By (47) we conclude that
$$\alpha \exp \left[-\alpha_{2} h(\tau)\right] \leq h^{\prime}(\tau) \leq \alpha \exp \left[-\alpha_{1} h(\tau)\right]$$
for all $\tau \geq T$. Integrating the leftmost inequality, we get
$$\frac{1}{\alpha_{2}} \ln \left[\exp \left[\alpha_{2} h(T)\right]+\alpha \alpha_{2}(\tau-T)\right] \leq h(\tau)$$
for all $\tau \geq T$. Inserting this in the rightmost inequality of (52), we conclude that
$$h^{\prime}(\tau) \leq \alpha\left[\exp \left[\alpha_{2} h(T)\right]+\alpha \alpha_{2}(\tau-T)\right]^{-\frac{\alpha_{1}}{\alpha_{2}}} .$$
Since $h^{\prime}=1+\Sigma_{+}$, and since the quotient $\alpha_{1} / \alpha_{2}$ can be chosen to be arbitrarily close to one, the lemma follows. □

Proposition 6. Consider a Bianchi VII ${ }_{0}$ solution to (5)-(7) with $N_{2}, N_{3}>0$. Then
$$\lim _{\tau \rightarrow \infty} N_{2}(\tau)=\lim _{\tau \rightarrow \infty} N_{3}(\tau)=n_{0}$$
where $0<n_{0}<\infty$.
Proof. It is enough to prove that $N_{2} N_{3}$ converges to a positive number. The reason is that this would prove that all the variables are contained in a compact set to the future, so that
$$N_{2}=\left(N_{2} N_{3}\right)^{1 / 2}+N_{2}^{1 / 2} \frac{N_{2}-N_{3}}{N_{2}^{1 / 2}+N_{3}^{1 / 2}}$$
converges, since $N_{2} N_{3}$ converges, $N_{2}^{1 / 2}+N_{3}^{1 / 2}$ is bounded from below by a positive constant, $N_{2}^{1 / 2}$ is bounded from above, and $N_{2}-N_{3} \rightarrow 0$ by Proposition 5. Since $N_{2}-N_{3} \rightarrow 0$, the limit for $N_{3}$ follows. Since
$$\left(N_{2} N_{3}\right)^{\prime}=\left(2 q+4 \Sigma_{+}\right) N_{2} N_{3},$$
the essential point is to prove that
$$\int_{\tau_{0}}^{\tau}\left(q / 2+\Sigma_{+}\right) d s$$
converges as $\tau \rightarrow \infty$. Observe now that
$$q / 2+\Sigma_{+}=\Sigma_{+}\left(1+\Sigma_{+}\right)+\Sigma_{-}^{2}=\left(1+\Sigma_{+}\right)^{2}-\left(1+\Sigma_{+}\right)+\Sigma_{-}^{2} .$$
Since $1+\Sigma_{+} \in L^{2}\left(\left[\tau_{0}, \infty\right)\right)$ by Lemma 10, we need only consider
$$\psi(\tau)=\int_{\tau_{0}}^{\tau}\left[\Sigma_{-}^{2}-\left(1+\Sigma_{+}\right)\right] d s$$
Let $T$ be big enough that (49) is applicable. If $\tau_{2} \geq \tau_{1} \geq T$ and $\tau_{3}$ is the largest number smaller than $\tau_{2}$ such that
$$\xi\left(\tau_{3}\right)-\xi\left(\tau_{1}\right)$$
is an integer multiple of $\pi$, then
$$\psi\left(\tau_{2}\right)-\psi\left(\tau_{1}\right)=\int_{\tau_{1}}^{\tau_{3}}\left[\Sigma_{-}^{2}-\left(1+\Sigma_{+}\right)\right] d s+\int_{\tau_{3}}^{\tau_{2}}\left[\Sigma_{-}^{2}-\left(1+\Sigma_{+}\right)\right] d s$$

The second integral converges to zero as $\tau_{1}$ and $\tau_{2}$ go to infinity, since the integrand goes to zero and the length of the interval is bounded (42). By (49) we conclude that
$$\left|\int_{\tau_{1}}^{\tau_{3}}\left[\Sigma_{-}^{2}-\left(1+\Sigma_{+}\right)\right] d s\right| \leq C \int_{\tau_{1}}^{\tau_{3}}\left(1+\Sigma_{+}\right)^{2} d s$$
Since $1+\Sigma_{+} \in L^{2}\left(\left[\tau_{0}, \infty\right)\right)$, this expression converges to zero as $\tau_{1}$ goes to infinity. The lemma follows. □

\section*{8. Bianchi VIII}

We assume that $N_{2}, N_{3}>0$ and $N_{1}<0$. Let us begin by giving the asymptotic behaviour of the $N_{i}$.

Lemma 11. Consider a Bianchi VIII solution to (5)-(7) with $N_{2}, N_{3}>0$ and $N_{1}<0$. Then,
$$\lim _{\tau \rightarrow \infty} N_{1}(\tau)=0, \quad \lim _{\tau \rightarrow \infty} N_{2}(\tau)=\lim _{\tau \rightarrow \infty} N_{3}(\tau)=\infty .$$
Proof. Reformulate the constraint (7) as
$$\Sigma_{+}^{2}+\Sigma_{-}^{2}+\frac{3}{4}\left[N_{1}^{2}+\left(N_{2}-N_{3}\right)^{2}-2 N_{1}\left(N_{2}+N_{3}\right)\right]=1 .$$
Observe that all terms appearing on the left hand side are non-negative so that the absolute values of, for instance, $N_{1}$ and $N_{2}-N_{3}$ are bounded by numerical constants. Assume there is a sequence $\tau_{k} \rightarrow \infty$ such that $N_{2}\left(\tau_{k}\right) \leq C<\infty$. Then the $N_{i}\left(\tau_{k}\right)$ are uniformly bounded. By the constraint $\Sigma_{+}$and $\Sigma_{-}$are contained in a compact set. Thus we can choose a convergent subsequence so that we have an $\omega$-limit point $\left(\sigma_{+}, \sigma_{-}, n_{1}, n_{2}, n_{3}\right)$. We apply the monotonicity principle with $U$ defined by $N_{i} \neq 0, i=1,2,3, M$ defined by (7) and $F\left(\Sigma_{+}, \Sigma_{-}, N_{1}, N_{2}, N_{3}\right)=$ $N_{1} N_{2} N_{3} . F$, evaluated on a solution contained in $U \cap M$, is strictly monotone since $\left(N_{1} N_{2} N_{3}\right)^{\prime}=3 q N_{1} N_{2} N_{3}$. If $q(\tau)=0$ then either $\Sigma_{-}^{\prime}(\tau) \neq 0$ or $\Sigma_{+}^{\prime}(\tau) \neq 0$ by (5)-(7). By the monotonicity principle one of the $n_{i}$ must be zero contradicting the growth of $\left|N_{1} N_{2} N_{3}\right|$. We conclude that $N_{2} \rightarrow \infty$, but then $N_{3} \rightarrow \infty$ and $N_{1} \rightarrow 0$ since $N_{1}\left(N_{2}+N_{3}\right)$ and $N_{2}-N_{3}$ are bounded by the constraint (7). □
8.1. The NUT case. Consider the special case $N_{2}=N_{3}$ and $\Sigma_{-}=0$.

Proposition 7. A Bianchi VIII solution with $N_{1}<0$, satisfying $N_{2}=N_{3}>0$ and $\Sigma_{-}=0$ has the following asymptotic behaviour
$$\lim _{\tau \rightarrow \infty} \Sigma_{+}(\tau)=\frac{1}{2}, \lim _{\tau \rightarrow \infty} N_{1}(\tau)=0, \lim _{\tau \rightarrow \infty} N_{2}(\tau)=\infty \text { and } \lim _{\tau \rightarrow \infty}\left(N_{1} N_{2}\right)(\tau)=-\frac{1}{4} .$$
Proof. The constraint implies
$$\Sigma_{+}^{\prime}=\left(1-\Sigma_{+}^{2}\right)\left(1-2 \Sigma_{+}\right)+\frac{9}{4} N_{1}^{2} .$$
Observe that we cannot have $\Sigma_{+} \rightarrow 1$ since $N_{1} N_{2}$ diverges to infinity there, c.f. (5). Also, $\Sigma_{+} \rightarrow-1$ is an impossibility since $\Sigma_{+}^{\prime}$ is always positive when $\Sigma_{+}$is close to -1. Since $N_{1} \rightarrow 0$ by Lemma 11 and $-1<\Sigma_{+}(\tau)<1 \forall \tau$ by the constraint (7) $\Sigma_{+} \rightarrow \frac{1}{2}$ follows. The last limit follows from the first and the constraint. □
8.2. Oscillatory behaviour. The behaviour of a Bianchi VIII solution as $\tau \rightarrow \infty$ is in some sense oscillatory. The quantities that oscillate are $\Sigma_{-}$and $N_{2}-N_{3}$. In order to analyze the asymptotics, we quantify this behaviour. Let
$$\tilde{x}=\Sigma_{-}, \tilde{y}=\frac{\sqrt{3}}{2}\left(N_{2}-N_{3}\right) .$$
We have
$$\tilde{x}^{\prime}=-3\left(N_{2}+N_{3}\right) \tilde{y}+\epsilon_{x}, \epsilon_{x}=-(2-q) \Sigma_{-}+3 N_{1} \tilde{y} .$$
Furthermore,
$$\tilde{y}^{\prime}=3\left(N_{2}+N_{3}\right) \tilde{x}+\epsilon_{y}, \epsilon_{y}=\left(q+2 \Sigma_{+}\right) \tilde{y} .$$
Observe that by the constraint (7) $|\tilde{x}|,|\tilde{y}|,\left|\epsilon_{x}\right|$ and $\left|\epsilon_{y}\right|$ are bounded by numerical constants whereas $N_{2}+N_{3} \rightarrow \infty$ by Lemma 11. Let $g=3\left(N_{2}+N_{3}\right)$,
$$A=\left(\begin{array}{rr}
0 & -g \\
g & 0
\end{array}\right)$$
$\tilde{\mathbf{x}}=(\tilde{x}, \tilde{y})^{t}$ and $\epsilon=\left(\epsilon_{x}, \epsilon_{y}\right)^{t}$ so that $\tilde{\mathbf{x}}^{\prime}=A \tilde{\mathbf{x}}+\epsilon$. Let
$$\xi(\tau)=\int_{\tau_{0}}^{\tau} g(s) d s+\phi_{0}$$
for some $\phi_{0}$ and $x_{1}(\tau)=\cos (\xi(\tau)), y_{1}(\tau)=\sin (\xi(\tau))$. Then, if $\mathbf{x}_{1}=\left(x_{1}, y_{1}\right)^{t}$, $\mathbf{x}_{1}^{\prime}=A \mathbf{x}_{1}$. Define
$$\Phi=\left(\begin{array}{rr}
x_{1} & y_{1} \\
-y_{1} & x_{1}
\end{array}\right) .$$
Then $\Phi^{\prime}=-A \Phi$ and $[A, \Phi]=0$. Let
$$r(\tau)=\left(\tilde{x}^{2}(\tau)+\tilde{y}^{2}(\tau)\right)^{1 / 2}$$
and
$$\mathbf{x}(\tau)=(x(\tau), y(\tau))^{t}=\left(r\left(\tau_{0}\right) \cos [\xi(\tau)], r\left(\tau_{0}\right) \sin [\xi(\tau)]\right)^{t}$$
where $\phi_{0}$ has been chosen so that $\mathbf{x}\left(\tau_{0}\right)=\tilde{\mathbf{x}}\left(\tau_{0}\right)$. Since $[\Phi(\mathbf{x}-\tilde{\mathbf{x}})]^{\prime}=-\Phi \epsilon$ and $\Phi(\tau) \in S O(2) \forall \tau$ we have
$$\|\tilde{\mathbf{x}}(\tau)-\mathbf{x}(\tau)\| \leq\left|\int_{\tau_{0}}^{\tau}\|\epsilon(s)\| d s\right|$$
By the constraint (7), we have $\|\epsilon\| \leq 9$, and thus
$$\|\tilde{\mathbf{x}}(\tau)-\mathbf{x}(\tau)\| \leq 9\left|\tau-\tau_{0}\right| .$$
The next lemma collects some technical estimates. We present them here in order not to interrupt the flow of later proofs.

Lemma 12. Consider a Bianchi VIII solution of (5)-(7) and let $C$ be a constant. Then there is a $T$ depending on $C$ and the initial values such that if $\left[\tau_{1}, \tau_{2}\right]$ is a time interval with $\tau_{1} \geq T$ and
$$\left|\tau_{2}-\tau_{1}\right| \leq \frac{C}{\left(N_{2}+N_{3}\right)\left(\tau_{3}\right)}$$
for some $\tau_{3} \in\left[\tau_{1}, \tau_{2}\right]$, then
$$\begin{aligned}
\left|\Sigma_{+}\left(t_{1}\right)-\Sigma_{+}\left(t_{2}\right)\right| & \leq \frac{C_{1}}{\left(N_{2}+N_{3}\right)\left(t_{3}\right)} \\
\left|\left[N_{1}\left(N_{2}+N_{3}\right)\right]\left(t_{1}\right)-\left[N_{1}\left(N_{2}+N_{3}\right)\right]\left(t_{2}\right)\right| & \leq \frac{C_{2}}{\left(N_{2}+N_{3}\right)\left(t_{3}\right)} \\
\left|1-\frac{\left(N_{2}+N_{3}\right)\left(t_{1}\right)}{\left(N_{2}+N_{3}\right)\left(t_{2}\right)}\right| & \leq \frac{C_{3}}{\left(N_{2}+N_{3}\right)\left(t_{3}\right)}
\end{aligned}$$
for arbitrary $t_{1}, t_{2}, t_{3} \in\left[\tau_{1}, \tau_{2}\right]$ where $C_{1}, C_{2}$ and $C_{3}$ are constants only depending on $C$.

Proof. By Lemma 11 we can assume $T$ to be great enough that $\Delta \tau=\tau_{2}-\tau_{1} \leq 1$. The inequality
$$\left|\frac{\left(N_{2}+N_{3}\right)^{\prime}}{N_{2}+N_{3}}\right| \leq 8$$
follows from (5)-(7). Thus
$$\left|\frac{\left(N_{2}+N_{3}\right)\left(t_{1}\right)}{\left(N_{2}+N_{3}\right)\left(t_{2}\right)}\right| \leq e^{8\left(\tau_{2}-\tau_{1}\right)}$$
so that if $\left(N_{2}+N_{3}\right)\left(t_{1}\right) \geq\left(N_{2}+N_{3}\right)\left(t_{2}\right)$,
$$\left|1-\frac{\left(N_{2}+N_{3}\right)\left(t_{1}\right)}{\left(N_{2}+N_{3}\right)\left(t_{2}\right)}\right| \leq\left|e^{8 \Delta \tau}-1\right| \leq 8 e^{8} \Delta \tau$$
since $\Delta \tau \leq 1$. Multiplying this inequality by $\left(N_{2}+N_{3}\right)\left(t_{2}\right) /\left(N_{2}+N_{3}\right)\left(t_{1}\right) \leq 1$ we conclude that the assumption $\left(N_{2}+N_{3}\right)\left(t_{1}\right) \geq\left(N_{2}+N_{3}\right)\left(t_{2}\right)$ is not essential. There is thus a constant $c<\infty$ such that
$$\frac{\left(N_{2}+N_{3}\right)\left(t_{1}\right)}{\left(N_{2}+N_{3}\right)\left(t_{2}\right)} \leq c$$
for any $t_{1}, t_{2} \in\left[\tau_{1}, \tau_{2}\right]$. Consequently
$$\Delta \tau \leq \frac{C}{\left(N_{2}+N_{3}\right)\left(\tau_{3}\right)} \leq \frac{c C}{\left(N_{2}+N_{3}\right)\left(t_{3}\right)} .$$
By (5)-(7) $\left|\Sigma_{+}^{\prime}\right|$ and $\left|\left[N_{1}\left(N_{2}+N_{3}\right)\right]^{\prime}\right|$ are bounded by constants independent of Bianchi VIII solution. Equations (58) and (59) follow from (62). Equation (60) follows from (61) and (62). □
Let us give the intuitive idea behind the next lemma. How the variables vary during a period is not so interesting, what is interesting is to compute the change over a period. In that way the continuous time evolution is replaced with a discrete evolution. To make the time step independent of approximation we wish to see what happens from $\tilde{x}=0$ to the next time $\tilde{x}=0$, but then we need to know that we have such zeros of $\tilde{x}$. In order to be able to prove this we assume that $r(55)$ is not too small. The assumption is not too restrictive; our ultimate goal is to prove that $r \rightarrow 0$ and that a general Bianchi VIII solution in some sense converges to a NUT solution. If $r$ is big our iteration is well defined and we will use it to prove that $r$ decreases and if $r$ is already small we do not need it.