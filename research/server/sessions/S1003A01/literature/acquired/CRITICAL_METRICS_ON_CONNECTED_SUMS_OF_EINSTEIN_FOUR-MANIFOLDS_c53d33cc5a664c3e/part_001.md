---
retention_scope: session
part: 1
total_parts: 4
---

[Part 1/4 of: CRITICAL METRICS ON CONNECTED SUMS OF EINSTEIN FOUR-MANIFOLDS]

---
source_file: 1303_0827.pdf
converter: mathpix
format: mmd
---

\title{
CRITICAL METRICS ON CONNECTED SUMS OF EINSTEIN FOUR-MANIFOLDS
}

\author{
MATTHEW J. GURSKY AND JEFF A. VIACLOVSKY
}

\begin{abstract}
We develop a gluing procedure designed to obtain canonical metrics on connected sums of Einstein four-manifolds. The main application is an existence result, using two well-known Einstein manifolds as building blocks: the Fubini-Study metric on $\mathbb{C P}^{2}$ and the product metric on $S^{2} \times S^{2}$. Using these metrics in various gluing configurations, critical metrics are found on connected sums for a specific Riemannian functional, which depends on the global geometry of the factors. Furthermore, using certain quotients of $S^{2} \times S^{2}$ as one of the gluing factors, critical metrics on several non-simply-connected manifolds are also obtained.
\end{abstract}

Contents
1. Introduction ..... 1
2. The building blocks ..... 10
3. The nonlinear map ..... 17
4. Cokernel on a compact manifold ..... 26
5. Cokernel on an asymptotically flat manifold ..... 29
6. Asymptotics of the cokernel ..... 36
7. Some auxiliary linear equations ..... 40
8. Computation of the leading term ..... 46
9. Naïve approximate metric ..... 55
10. Refined approximate metric ..... 59
11. Lyapunov-Schmidt reduction ..... 68
12. Completion of proofs ..... 78
Appendix A. Proof of Proposition 8.5 ..... 85
Appendix B. Non-simply-connected examples ..... 89
References ..... 89

\section*{1. Introduction}

A Riemannian manifold $\left(M^{4}, g\right)$ in dimension four is critical for the Einstein-Hilbert functional
$$\mathcal{R}(g)=\operatorname{Vol}(g)^{-1 / 2} \int_{M} R_{g} d V_{g}$$

\footnotetext{
Date: March 4, 2013.
}
where $R_{g}$ is the scalar curvature, if and only if it satisfies
$$\operatorname{Ric}(g)=\lambda \cdot g,$$
where $\lambda$ is a constant; such Riemannian manifolds are called Einstein manifolds. Non-collapsing limits of Einstein manifolds have been studied in great depth [And89, [BKN89, Tia90]. In particular, with certain geometric conditions, the limit space is an orbifold, with asymptotically locally Euclidean (ALE) spaces bubbling off at the singular points. A natural question is whether it is possible to reverse this process: can one start with the limit space, and glue on a bubble in order to obtain an Einstein metric? A recent article of Olivier Biquard makes great strides in the Poincaré-Einstein setting [Biq11]. In this work it is shown that a $\mathbb{Z} / 2 \mathbb{Z}$-orbifold singularity $p$ of a non-degenerate Poincaré-Einstein orbifold $(M, g)$ has a Poinaré-Einstein resolution obtained by gluing on an Eguchi-Hanson metric if and only if the condition
$$\operatorname{det}\left(\mathbf{R}^{+}(p)\right)=0$$
is satisfied, where $\mathbf{R}^{+}(p): \Lambda_{+}^{2} \rightarrow \Lambda_{+}^{2}$ is the purely self-dual part of the curvature operator at $p$. The self-adjointness of this gluing problem is overcome by the freedom of changing the boundary data of the Poincaré-Einstein metric.

However, there is not much known about gluing compact manifolds together in the Einstein case. In this work, we will replace the Einstein equations with a generalization of the Einstein condition. Namely, we ask whether it is possible to glue together Einstein metrics and produce a critical point of a certain Riemannian functional generalizing the Einstein-Hilbert functional. It turns out that there is a family of such functionals; this gives an extra parameter which will allow us to overcome the self-adjointness of this problem. The particular functional will then depend on the global geometry of the gluing factors.

To describe the functionals, let $M$ be a closed manifold of dimension 4 . We will consider functionals on the space of Riemannian metrics $\mathcal{M}$ which are quadratic in the curvature. Such functionals have also been widely studied in physics under the name "fourth-order," "critical," or "quadratic" gravity; see for example [LP11, Mal11, Sch07, Ste78]. In previous work, the authors have studied rigidity and stability properties of Einstein metrics for quadratic curvature functionals [GV11]; these results will play a crucial rôle in this paper.

Using the standard decomposition of the curvature tensor $R m$ into the Weyl, Ricci and scalar curvature curvature components (denoted by $W$, Ric, and $R$, respectively), a basis for the space of quadratic curvature functionals is
$$\mathcal{W}=\int|W|^{2} d V, \quad \rho=\int|\operatorname{Ric}|^{2} d V, \quad \mathcal{S}=\int R^{2} d V$$
where we use the tensor norm. In dimension four, the Chern-Gauss-Bonnet formula
$$32 \pi^{2} \chi(M)=\int|W|^{2} d V-2 \int|\operatorname{Ric}|^{2} d V+\frac{2}{3} \int R^{2} d V$$
implies that $\rho$ can be written as a linear combination of the other two (plus a topological term). Consequently, we will be interested in the functional
$$\mathcal{B}_{t}[g]=\int|W|^{2} d V+t \int R^{2} d V$$
(with $t=\infty$ formally corresponding to $\int R^{2} d V$ ).
The Euler-Lagrange equations of $\mathcal{B}_{t}$ are given by
$$B^{t} \equiv B+t C=0,$$
where $B$ is the Bach tensor defined by
$$B_{i j} \equiv-4\left(\nabla^{k} \nabla^{l} W_{i k j l}+\frac{1}{2} R^{k l} W_{i k j l}\right)=0,$$
and $C$ is the tensor defined by
$$C_{i j}=2 \nabla_{i} \nabla_{j} R-2(\Delta R) g_{i j}-2 R R_{i j}+\frac{1}{2} R^{2} g_{i j} .$$
It follows that any Einstein metric is critical for $\mathcal{B}_{t}$ [Bes87]. We will refer to such a critical metric as a $B^{t}$-flat metric. Note that by taking a trace of (1.7), it follows that the scalar curvature of a $B^{t}$-flat metric on a compact manifold is necessarily constant. Therefore a $B^{t}$-flat metric satisfies the equation
$$B=2 t R \cdot E,$$
where $E$ denotes the traceless Ricci tensor. That is, the Bach tensor is a constant multiple of the traceless Ricci tensor.

The convergence results described above for Einstein metrics were generalized to systems of the form
$$\Delta R i c=R m * R i c$$
(of which (1.10) is a special case) in [TV05a, TV05b, TV08]. In particular, with certain geometric conditions, non-collapsing sequences of metrics satisfying an equation of the form (1.11) have orbifold limits. Again, the natural question is whether it is possible to reverse this bubbling process.

The analogous gluing problem for the anti-self-dual equations $W^{+}=0$ in dimension four has been very successful [DF89, Flo91, Tau92, KS01, AV12a]. However, gluing for the $B^{t}$-flat equations is much more difficult because, as in the Einstein case, this is a self-adjoint problem. The parameter $t$ is the key to overcoming this difficulty.

We point out that the linearization of the $B^{t}$-flat equation (1.7) is not elliptic due to diffeomorphism invariance. It will be necessary to "gauge" the equation in order to work with an elliptic operator. This is analogous to the Bianchi gauge for the Einstein equations. The details of this gauging process appear in Section 3.

The main building blocks in this paper are the Fubini-Study metric $\left(\mathbb{C P}^{2}, g_{F S}\right)$, and $\left(S^{2} \times S^{2}, g_{S^{2} \times S^{2}}\right)$, the product of 2-dimensional spheres with unit Gauss curvature. Both are Einstein, so are $B^{t}$-flat for all $t \in \mathbb{R}$. A key result used in this paper is rigidity of these metrics for certain ranges of $t$, which was proved in our previous
work [GV11]. That is, these metrics admit no non-trivial infinitesimal $B^{t}$-flat deformations for certain ranges of $t$ (other than scalings). These rigidity properties will be discussed in Section 4.
1.1. Green's function metric. Recall that the conformal Laplacian is the operator
$$L u=-6 \Delta u+R u,$$
where our convention is to use the analyst's Laplacian (which has negative eigenvalues). If $(M, g)$ is compact and has positive scalar curvature, then for any $p \in M$, there exists a unique positive solution to the equation
$$\begin{aligned}
L G & =0 \text { on } M \backslash\{p\} \\
G & =\rho^{-2}(1+o(1))
\end{aligned}$$
as $\rho \rightarrow 0$, where $\rho$ is geodesic distance to the basepoint $p$, which is called the Green's function. Denote $N=M \backslash\{p\}$ with metric $g_{N}=G^{2} g_{M}$. The metric $g_{N}$ is scalar-flat and asymptotically flat of order 2. Recall the mass of an AF space is defined by
$$\left.\operatorname{mass}\left(g_{N}\right)=\lim _{R \rightarrow \infty} \omega_{3}^{-1} \int_{S(R)} \sum_{i, j}\left(\partial_{i} g_{i j}-\partial_{j} g_{i i}\right)\left(\partial_{i}\right\lrcorner d V\right),$$
with $\omega_{3}=\operatorname{Vol}\left(S^{3}\right)$.
A crucial point is the following: if $(M, g)$ is Bach-flat, then from conformal invariance of the Bach tensor, $\left(N, g_{N}\right)$ is also Bach-flat. Also, since the Green's function is used as the conformal factor, $g_{N}$ is scalar-flat. Consequently, $g_{N}$ is $B^{t}$-flat for all $t \in \mathbb{R}$.

The Green's function metric of the Fubini-Study metric $\hat{g}_{F S}$ is also known as the Burns metric, and is completely explicit, with mass given by
$$\operatorname{mass}\left(\hat{g}_{F S}\right)=2 .$$
However, the Green's function metric $\hat{g}_{S^{2} \times S^{2}}$ of the product metric does not seem to have a known explicit description. We will denote
$$m_{1}=\operatorname{mass}\left(\hat{g}_{S^{2} \times S^{2}}\right) .$$
By the positive mass theorem of Schoen-Yau, $m_{1}>0$ [SY79, SY81]. We note that since $S^{2} \times S^{2}$ is spin, this also follows from Witten's proof of the positive mass theorem [Wit81].
1.2. The gluing procedure. Let $\left(Z, g_{Z}\right)$ and $\left(Y, g_{Y}\right)$ be Einstein manifolds, and assume that $g_{Y}$ has positive scalar curvature. Choose basepoints $z_{0} \in Z$ and $y_{0} \in Y$. Convert $\left(Y, g_{Y}\right)$ into an asymptotically flat (AF) metric $\left(N, g_{N}\right)$ using the Green's function for the conformal Laplacian based at $y_{0}$. As pointed out above, $g_{N}$ is $B^{t}$-flat for any $t$.

Let $a>0$ be small, and consider $Z \backslash B\left(z_{0}, a\right)$. Scale the compact metric to $(Z, \tilde{g}=$ $\left.a^{-4} g_{Z}\right)$. Attach this metric to the metric $\left(N \backslash B\left(a^{-1}\right), g_{N}\right)$ using cutoff functions near the boundary, to obtain a smooth metric on the connect sum $Z \# \bar{Y}$. Since both $g_{Z}$ and $g_{N}$ are $B^{t}$-flat, this metric is an "approximate" $B^{t}$-flat metric, with vanishing
$B^{t}$ tensor away from the "damage zone", where cutoff functions were used. This construction is described in detail in Section 9, and is illustrated in Figure 1.1.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/f26727bd-f2f4-4432-97d4-75d415edfc6a-05.jpg?height=686&width=1495&top_left_y=450&top_left_x=314}
\captionsetup{labelformat=empty}
\caption{Figure 1.1. The approximate metric.}
\end{figure}

This "naïve" approximate metric is too rough for our purposes - the size of the $B^{t}$ tensor is an order too large in the damage zone. A refinement of this approximate metric is found by solving linear equations on each piece to make the metrics match up to highest order. The $B^{t}$ tensor of the refined metric is now an order of magnitude smaller. This step is inspired by the recent work of Biquard in the Einstein case which was mentioned above [Biq11]. These auxiliary linear equations are solved in Section 7, and the refined approximate metric is constructed in Section 10.

Lyapunov-Schmidt reduction is then used to reduce the problem from an infinitedimensional problem to a finite-dimensional one. That is, the problem of finding a $B^{t}$-flat metric is reduced to finding a zero of the Kuranishi map, which is a mapping between finite-dimensional spaces. This reduction is carried out in Section 11.

For the general gluing problem, even if the pieces are rigid, there can be nonzero infinitesimal kernel elements due to the presence of gluing parameters. In general, there are infinitesimal kernel elements corresponding geometrically to freedom of scaling the AF space, rotating the gluing factor, and moving the base points of the gluing. The leading term of the Kuranishi map corresponding to the scaling parameter, denoted by $\lambda_{1}(a)$, is given by:

Theorem 1.1. As $a \rightarrow 0$, then for any $\epsilon>0$,
$$\lambda_{1}(a)=\left(\frac{2}{3} W\left(z_{0}\right) \circledast W\left(y_{0}\right)+4 t R\left(z_{0}\right) \operatorname{mass}\left(g_{N}\right)\right) \omega_{3} a^{4}+O\left(a^{6-\epsilon}\right),$$
where $\omega_{3}=\operatorname{Vol}\left(S^{3}\right)$, and the product of the Weyl tensors is given by
$$W\left(z_{0}\right) \circledast W\left(y_{0}\right)=\sum_{i j k l} W_{i j k l}\left(z_{0}\right)\left(W_{i j k l}\left(y_{0}\right)+W_{i l k j}\left(y_{0}\right)\right),$$
where $W_{i j k l}(\cdot)$ denotes the components of the Weyl tensor in a normal coordinate system at the corresponding point.

We note that the product $\circledast$ depends upon the coordinate systems chosen, and therefore in general depends upon a rotation parameter, and obviously on the base points of the gluing.
1.3. Simply-connected examples. In the case either of the factors are $\left(\mathbb{C} \mathbb{P}^{2}, g_{F S}\right)$ or $\left(S^{2} \times S^{2}, g_{S^{2} \times S^{2}}\right)$, Theorem 1.1 implies an existence theorem. Since these manifolds are toric, we can use the torus action plus a certain discrete symmetry, called a diagonal symmetry, to eliminate all gluing parameters except for the scaling parameter. Theorem 1.1 will then allow us to obtain critical metrics on the following manifolds "near" the indicated approximate metric:
\begin{itemize}
\item[-] (i) $\mathbb{C P}^{2} \# \overline{\mathbb{C P}}^{2}$; the Fubini-Study metric with a Burns metric attached at one fixed point. This case admits a $U(2)$-action.
\item[-] (ii) $S^{2} \times S^{2} \# \overline{\mathbb{C P}}^{2}=\mathbb{C P}^{2} \# 2 \overline{\mathbb{C P}}^{2}$; the product metric on $S^{2} \times S^{2}$ with a Burns metric attached at one fixed point. Alternatively, we can view this as the Fubini-Study metric on $\mathbb{C P}^{2}$, with a Green's function $S^{2} \times S^{2}$ metric attached at one fixed point. For this topology, we will therefore construct two different critical metrics.
\item[-] (iii) $2 \# S^{2} \times S^{2}$; the product metric on $S^{2} \times S^{2}$ with a Green's function $S^{2} \times S^{2}$ metric attached at one fixed point.
\end{itemize}

More precisely, we have
Theorem 1.2. In each of the above cases, a $B^{t}$-flat metric exists for some $t$ near the critical value of
$$t_{0}=\frac{-1}{6 R\left(z_{0}\right) \operatorname{mass}\left(g_{N}\right)} W\left(z_{0}\right) \circledast W\left(y_{0}\right) .$$
Furthermore, this metric is invariant under the indicated action(s).
The proof of the theorem appears in Section 12, and the special values of $t_{0}$ in each case are indicated in Table 1.1.

\begin{table}
\captionsetup{labelformat=empty}
\caption{Table 1.1. Simply-connected examples with one bubble}
\begin{tabular}[t]{|l|l|}
\hline Topology of connected sum & Value(s) of $t_{0}$ \\
\hline $\mathbb{C P}^{2} \# \overline{\mathbb{C P}}^{2}$ & -1/3 \\
\hline $S^{2} \times S^{2} \# \overline{\mathbb{C P}}^{2}=\mathbb{C P}^{2} \# 2 \overline{\mathbb{C P}}^{2}$ & $-1 / 3,-\left(9 m_{1}\right)^{-1}$ \\
\hline $2 \# S^{2} \times S^{2}$ & $-2\left(9 m_{1}\right)^{-1}$ \\
\hline
\end{tabular}
\end{table}

With $\mathbb{C P}^{2}$ as a compact factor, there are three fixed points of the torus action, and with $S^{2} \times S^{2}$, there are four fixed points. Employing various discrete symmetries will also allow us to obtain critical metrics on connected sums with more than two factors. Theorem 1.2 extends to the following cases:
\begin{itemize}
\item[-] (iv) $3 \# S^{2} \times S^{2}$; the product metric on $S^{2} \times S^{2}$ with Green's function $S^{2} \times S^{2}$ metrics attached at two fixed points. In this case, we will impose an additional symmetry called bilateral symmetry.
\item[-] (v) $S^{2} \times S^{2} \# 2 \overline{\mathbb{C P}}^{2}=\mathbb{C P}^{2} \# 3 \overline{\mathbb{C P}}^{2}$; the product metric on $S^{2} \times S^{2}$ with Burns metrics attached at two fixed points, with bilateral symmetry.
\item[-] (vi) $\mathbb{C P}^{2} \# 3 \overline{\mathbb{C P}}^{2}$; the Fubini-Study metric with Burns metrics attached at all fixed points, with a symmetry called trilateral symmetry.
\item[-] (vii) $\mathbb{C P}^{2} \# 3\left(S^{2} \times S^{2}\right)=4 \mathbb{C P}^{2} \# 3 \overline{\mathbb{C P}}^{2}$; the Fubini-Study metric with Green's function $S^{2} \times S^{2}$ metrics attached at all fixed points, with trilateral symmetry.
\item[-] (viii) $S^{2} \times S^{2} \# 4 \overline{\mathbb{C P}}^{2}=\mathbb{C P}^{2} \# 5 \overline{\mathbb{C P}}^{2}$; the product metric on $S^{2} \times S^{2}$ with Burns metrics attached at all fixed points, with a symmetry called quadrilateral symmetry.
\item[-] (ix) $5 \# S^{2} \times S^{2}$ viewed as the product metric on $S^{2} \times S^{2}$ with Greens function $S^{2} \times S^{2}$ metrics attached at all fixed points, with quadrilateral symmetry.
\end{itemize}

The special values of $t_{0}$ in each case are indicated in Table 1.2.

\begin{table}
\captionsetup{labelformat=empty}
\caption{Table 1.2. Simply-connected examples with several bubbles}
\begin{tabular}[t]{|l|l|l|}
\hline Topology of connected sum & Value of $t_{0}$ & Symmetry \\
\hline $3 \# S^{2} \times S^{2}$ & $-2\left(9 m_{1}\right)^{-1}$ & bilateral \\
\hline $S^{2} \times S^{2} \# 2 \overline{\mathbb{C P}}^{2}=\mathbb{C P}^{2} \# 3 \overline{\mathbb{C P}}^{2}$ & -1/3 & bilateral \\
\hline $\mathbb{C P}^{2} \# 3 \overline{\mathbb{C P}}^{2}$ & -1/3 & trilateral \\
\hline $\mathbb{C P}^{2} \# 3\left(S^{2} \times S^{2}\right)=4 \mathbb{C P}^{2} \# 3 \overline{\mathbb{C P}}^{2}$ & $-\left(9 m_{1}\right)^{-1}$ & trilateral \\
\hline $S^{2} \times S^{2} \# 4 \overline{\mathbb{C P}}^{2}=\mathbb{C P}^{2} \# 5 \overline{\mathbb{C P}}^{2}$ & -1/3 & quadrilateral \\
\hline $5 \# S^{2} \times S^{2}$ & $-2\left(9 m_{1}\right)^{-1}$ & quadrilateral \\
\hline
\end{tabular}
\end{table}

Remark 1.3. Since $S^{2} \times S^{2}$ admits an orientation-reversing diffeomorphism, there is only one possibility for a connect sum with $S^{2} \times S^{2}$, which is why $\overline{S^{2} \times S^{2}}$ does not appear in the list of examples.
1.4. Non-simply-connected examples. The product metric on $S^{2} \times S^{2}$ admits the Einstein quotient $S^{2} \times S^{2} / \mathbb{Z}_{2}$, where $\mathbb{Z}_{2}$ acts by the antipodal map on both factors, and the quotient $\mathbb{R P}^{2} \times \mathbb{R P}^{2}$. Using one of these metrics as the compact factor or the Green's function metric of one of these as one of the AF spaces, we can obtain several non-simply-connected examples. We will denote
$$m_{2}=\operatorname{mass}\left(\hat{g}_{S^{2} \times S^{2} / \mathbb{Z}^{2}}\right),$$
and
$$m_{3}=\operatorname{mass}\left(\hat{g}_{\mathbb{R P}^{2} \times \mathbb{R P}^{2}}\right) .$$
Again, by the positive mass theorem, $m_{2}>0$ and $m_{3}>0$. Theorem 1.2 holds for these examples as well, and the special values of $t_{0}$ in each non-simply-connected case with one bubble are indicated in Table 1.3. We note those without an $\mathbb{R} \mathbb{P}^{2} \times \mathbb{R P}^{2}$
factor are orientable, and those with an $\mathbb{R P}^{2} \times \mathbb{R P}^{2}$ factor are non-orientable. Also note that the first, second, fifth and sixth examples have finite fundamental groups. The others have infinite fundamental group (in particular, by the Myers Theorem these manifolds do not admit positive Einstein metrics).

\begin{table}
\captionsetup{labelformat=empty}
\caption{Table 1.3. Non-simply-connected examples with one bubble}
\begin{tabular}[t]{|l|l|}
\hline Topology of connected sum & Value(s) of $t_{0}$ \\
\hline $\left(S^{2} \times S^{2} / \mathbb{Z}_{2}\right) \# \overline{\mathbb{C P}}^{2}$ & $-1 / 3,-\left(9 m_{2}\right)^{-1}$ \\
\hline $\left(S^{2} \times S^{2} / \mathbb{Z}_{2}\right) \# S^{2} \times S^{2}$ & $-2\left(9 m_{1}\right)^{-1},-2\left(9 m_{2}\right)^{-1}$ \\
\hline $\left(S^{2} \times S^{2} / \mathbb{Z}_{2}\right) \#\left(S^{2} \times S^{2} / \mathbb{Z}_{2}\right)$ & $-2\left(9 m_{2}\right)^{-1}$ \\
\hline $\left(S^{2} \times S^{2} / \mathbb{Z}_{2}\right) \# \mathbb{R} \mathbb{P}^{2} \times \mathbb{R} \mathbb{P}^{2}$ & $-2\left(9 m_{3}\right)^{-1},-2\left(9 m_{2}\right)^{-1}$ \\
\hline $\mathbb{R P}^{2} \times \mathbb{R P}^{2} \# \overline{\mathbb{C P}}^{2}$ & $-1 / 3,-\left(9 m_{3}\right)^{-1}$ \\
\hline $\mathbb{R} \mathbb{P}^{2} \times \mathbb{R} \mathbb{P}^{2} \# S^{2} \times S^{2}$ & $-2\left(9 m_{1}\right)^{-1},-2\left(9 m_{3}\right)^{-1}$ \\
\hline $\mathbb{R P}^{2} \times \mathbb{R P}^{2} \# \mathbb{R} \mathbb{P}^{2} \times \mathbb{R} \mathbb{P}^{2}$ & $-2\left(9 m_{3}\right)^{-1}$ \\
\hline
\end{tabular}
\end{table}

As in the simply-connected case, we can take advantage of various symmetries to obtain non-simply-connected examples with more than one bubble. For the complete list, see Appendix B.
1.5. The Bach-flat case. We remark that Theorem 1.1 holds in the Bach-flat case $(t=0)$, provided one restricts to traceless tensors throughout the argument (this is necessary due to conformal invariance of the Bach tensor). This expansion cannot be directly used to produce Bach-flat metrics, since the freedom to move the parameter $t$ is crucial in the proof of Theorem 1.2. However, the main argument does imply the following non-existence result:

Theorem 1.4. Assume that both $\left(Z, g_{Z}\right)$ and $\left(Y, g_{Y}\right)$ are Bach-flat, toric, and admit a diagonal symmetry. Let $z_{0} \in Z$ and $y_{0} \in Y$ be fixed points of the respective torus actions. If
$$W\left(y_{0}\right) \circledast W\left(z_{0}\right) \neq 0,$$
then there is no equivariant Bach-flat metric in a $C^{4, \alpha}$-neighborhood of the approximate metric.

This is applicable to all of the above examples, so we may conclude that there is no Bach-flat metric near the metrics found in Theorem 1.2. In particular, these metrics are not Einstein. We remark that this non-existence theorem is true without the equivariance assumption, but a complete proof of this adds considerable technical details, so is not included.

Note that in the case of $\mathbb{C P}^{2} \# \mathbb{C P}^{2}$, it is easy to see that $W\left(y_{0}\right) \circledast W\left(z_{0}\right)=0$, since there is an orientation-reversal required when performing the connected sum. This is not surprising, since it is well-known that there is a 1-parameter family of self-dual metrics (which are Bach-flat) near the approximate metric [Poo86, LeB91, Via10].
1.6. Remarks. The proof of Theorem 1.2 shows the following dichotomy: either (i) there is a critical metric at exactly the critical $t_{0}$, in which case there would necessarily be a 1 -dimensional moduli space of solutions for this fixed $t_{0}$ (as pointed out above, this indeed happens for $\mathbb{C P}^{2} \# \mathbb{C P}^{2}$, in which case there is a 1-parameter family of selfdual metrics). The other possibility (ii) is that for each value of the gluing parameter $a$ sufficiently small, there will be a critical metric for a corresponding value of $t_{0}=t_{0}(a)$. The dependence of $t_{0}$ on $a$ will depend on the next term in the expansion of (1.18). For example, if this expansion were improved to
$$\lambda_{1}=\lambda a^{4}+\mu a^{8}+O\left(a^{12-\epsilon}\right),$$
with $\mu \neq 0$, then we would have the dependence
$$t_{0}=\frac{1}{4 R\left(z_{0}\right) \operatorname{mass}\left(g_{N}\right)}\left(-\frac{2}{3} W\left(y_{0}\right) \circledast W\left(z_{0}\right)-\frac{\mu}{\omega_{3}} a^{4}\right)+O\left(a^{8-\epsilon}\right) .$$
as $a \rightarrow 0$.
It should be possible to extend the methods in this paper to compute $\mu$. If it turns out that $\mu \neq 0$, then one may conclude that possibility (ii) definitely happens. The sign of $\mu$ would then determine if solutions are found for $t>t_{0}$ or $t<t_{0}$. If $\mu=0$, this would indicate (but not prove) that possibility (i) is what actually occurs. The methods in this paper cannot practically be used to determine that possibility (i) actually happens, since there would be an infinite sequence of obstructions to check in this eventuality.

We next make some remarks about some relations between Kähler geometry and the value $t_{0}=-1 / 3$ appearing in the above tables. Using the Hirzebruch signature theorem, we can write
$$\mathcal{B}_{-1 / 3}[g]=-48 \pi^{2} \sigma\left(M^{4}\right)+2 \int\left(\left|W^{+}\right|^{2}-\frac{1}{6} R^{2}\right) d V$$
An immediate corollary of this formula is that if $\left(M^{4}, g\right)$ is Kähler, then
$$\mathcal{B}_{-1 / 3}[g]=-48 \pi^{2} \sigma\left(M^{4}\right) .$$
In addition, a constant scalar curvature Kähler metric is necessarily critical for the value $t_{0}=-1 / 3$ [Der83]. We note that important gluing results for constant scalar curvature Kähler metrics were proved in [AP06, AP09].

For the manifolds $\mathbb{C P}^{2} \# k \overline{\mathbb{C P}}^{2}$, when $k=1,2,3$, or 5 , consider the cases when a Burns metric is used for the bubbles (the cases when $t_{0}=-1 / 3$ ). In these cases, it is known that there are extremal Kähler metrics near the näive approximate metric [APS11, Szé12]. These extremal metrics do not have constant scalar curvature, so they are not the same as the critical metrics found in Theorem 1.2. There might be some other relation between these metrics (such as conformality), but we are not aware of any such relation. These manifolds are known to admit Einstein metrics [Bes87, CLW08, LeB12].

However, on many of the other manifolds considered in this paper, there does not exist any Kähler metric (for example $2 \# S^{2} \times S^{2}$ ), and the critical metrics found in

Theorem 1.2 are the first known "canonical" metrics, to the best of the authors' knowledge.
1.7. Acknowledgements. This work was done in part at the Institute for Advanced Study in Princeton and at the Institut Henri Poincaré in Paris. Both authors have been partially supported by the NSF; the first author under NSF grant DMS-1206661 and the second author under NSF grant DMS-1105187. The second author was partially supported by the Simons Foundation as a Simons Fellow of Mathematics. Both authors thank the above institutions for their generous support.

The authors would like to thank Olivier Biquard for crucial assistance in completing this work, and to Simon Brendle, Claude LeBrun, Rafe Mazzeo, Frank Pacard, and Karen Uhlenbeck for many helpful remarks.

\section*{2. The building blocks}

In this section, we will derive metric expansions for the "building blocks" of our gluing procedure; the Fubini-Study metric and product metric on $S^{2} \times S^{2}$. We will also give metric expansions of the associated scalar-flat asymptotically flat metrics, arising from the Green's function of the conformal Laplacian.

The general gluing problem has many degrees of freedom. We will take advantage of various symmetries to reduce eventually to only one degree of freedom. So in this section, we will also describe the various group actions which will be used for an equivariant gluing.
2.1. The Fubini-Study metric. Recall that $\mathbb{C P}^{2}$ is the set of complex projective lines through the origin in $\mathbb{C}^{3}$. Equivalently, $\mathbb{C P}^{2}$ is the set of equivalence classes $\left\{\mathbb{C}^{3} \backslash\{0\}\right\} / \mathbb{C}^{*}$, where the action of $\mathbb{C}^{*}$ is defined by, for $\lambda \in \mathbb{C}^{*}$,
$$\left[u_{0}, u_{1}, u_{2}\right] \mapsto\left[\lambda u_{0}, \lambda u_{1}, \lambda u_{2}\right] .$$
Let $U_{i}=\left\{\left[u_{0}, u_{1}, u_{2}\right] \mid u_{i} \neq 0\right\}$, for $i=0,1,2$. The Fubini-Study metric is given in $U_{0}$ by [KN96]
$$\begin{aligned}
g_{F S} & =\frac{\sqrt{-1}}{2} \partial \bar{\partial}\left(1+\left|u_{1}\right|^{2}+\left|u_{2}\right|^{2}\right) \\
& =\frac{\left(1+|u|^{2}\right)\left(d u_{1} d \bar{u}_{1}+d u_{2} d \bar{u}_{2}\right)-\left(\bar{u}_{1} d u_{1}+\bar{u}_{2} d u_{2}\right)\left(u_{1} d \bar{u}_{1}+u_{2} d \bar{u}_{2}\right)}{\left(1+|u|^{2}\right)^{2}}
\end{aligned} .$$
This extends to an Einstein metric on $\mathbb{C P}^{2}$ with $\operatorname{Ric}(g)=6 g$, and $\operatorname{PU}(3)$, the projective unitary group (the unitary group $U(3)$ modulo its center), acts by isometries.

We will consider two sub-actions of this group action. The first is an action of $U(2)$ fixing the point [1, 0, 0]. Globally, this action is given by, for $A \in U(2)$,
$$\left[u_{0}, u_{1}, u_{2}\right] \mapsto\left[u_{0}, A\left(u_{1}, u_{2}\right)\right] .$$
The point [1, 0, 0] is the only fixed point of this action. In $U_{0}$, this action is given by the standard action of $U(2)$ acting on $\mathbb{C}^{2}$.

The second action is the torus action of the form
$$\left[u_{0}, u_{1}, u_{2}\right] \mapsto\left[u_{0}, e^{\sqrt{-1} \theta_{1}} u_{1}, e^{\sqrt{-1} \theta_{2}} u_{2}\right]$$
where $\theta_{1}, \theta_{2} \in[0,2 \pi]$. This action has 3 fixed points $[1,0,0],[0,1,0]$, and $[0,0,1]$. In $U_{0}$, this action is given by
$$\left(u_{1}, u_{2}\right) \mapsto\left(e^{\sqrt{-1} \theta_{1}} u_{1}, e^{\sqrt{-1} \theta_{2}} u_{2}\right) .$$
Next, let $\left\{\sigma_{1}, \sigma_{2}, \sigma_{3}\right\}$ be a left-invariant coframing on $S^{3}$ such that $\sigma_{3}$ is a connection form for the Hopf fibration $\pi: S^{3} \rightarrow S^{2}=\mathbb{C P}^{1}$ defined by
$$\pi\left(u_{1}, u_{2}\right)=\left[u_{1}: u_{2}\right],$$
and such that $\pi^{*} g_{S^{2}}=4\left(\sigma_{1}^{2}+\sigma_{2}^{2}\right)$. The Fubini-Study metric can then be written as [EGH80, page 257]
$$g_{F S}=\frac{1}{\left(1+r^{2}\right)^{2}} d r^{2}+\frac{r^{2}}{1+r^{2}}\left(\sigma_{1}^{2}+\sigma_{2}^{2}+\frac{1}{1+r^{2}} \sigma_{3}^{2}\right)$$
From this expression, the above action of $U(2)$ is seen here here as an action of SO(3) × SO(2) where the first factor acts by rotations of $S^{2}$, and the second factor acts by rotations of the fiber of the Hopf fibration. The above torus action is the restricted action where the first factor acts by a rotation of $S^{2}$ fixing the north and south pole.

From (2.6), we see that $\rho=\arctan (r)$ is the geodesic distance from the basepoint, and under this radial change of coordinates the metric is written as [LNN97]
$$g_{F S}=d \rho^{2}+\sin ^{2}(\rho)\left(\sigma_{1}^{2}+\sigma_{2}^{2}+\cos ^{2}(\rho) \sigma_{3}^{2}\right)$$
with the restriction that $0<\rho<\pi / 2$. Since the coordinate change is radial, we note the important fact that in these coordinates, the above action of $U(2)$ is still the standard linear action.

Finally, we let $\left\{z^{i}\right\}$ be Euclidean normal coordinates, based at [1, 0, 0], so that $U(2)$ acts linearly, and that the above torus action acts by
$$\left(z_{1}, z_{2}, z_{3}, z_{4}\right) \mapsto\left(e^{\sqrt{-1} \theta_{1}}\left(z_{1}+\sqrt{-1} z_{2}\right), e^{\sqrt{-1} \theta_{2}}\left(z_{3}+\sqrt{-1} z_{4}\right)\right) .$$
In this coordinate system, we have the expansion
$$g_{i j}=\delta_{i j}-\frac{1}{3} R_{i k j l}([1,0,0]) z^{k} z^{l}+O^{(4)}\left(|z|^{4}\right)_{i j}$$
as $|z| \rightarrow 0$.
Remark 2.1. We adopt the convention that for a function (or tensor) $f=f(z)$, $f=O^{(m)}\left(|z|^{\alpha}\right)$ means $\left|\partial^{k} f\right|=O\left(|z|^{\alpha-k}\right)$ for all $1 \leq k \leq m$ (as $z$ approaches an indicated limit).

This metric is invariant under the diagonal symmetry:
$$\left(z_{1}, z_{2}, z_{3}, z_{4}\right) \mapsto\left(z_{3}, z_{4}, z_{1}, z_{2}\right),$$
which is contained in $U(2)$. In the case of toric invariance, we will impose this as an extra symmetry for the equivariant gluing problem. In both cases, there will
therefore be only one fixed point, the point [1, 0, 0]. These symmetries are illustrated in Figure 2.1.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/f26727bd-f2f4-4432-97d4-75d415edfc6a-12.jpg?height=688&width=780&top_left_y=455&top_left_x=672}
\captionsetup{labelformat=empty}
\caption{Figure 2.1. Orbit space of the torus action on $\mathbb{C P}^{2}$. The vertices of the triangle are fixed points, open edge points are circle orbits, and interior points are principal orbits. The diagonal symmetry is a reflection in the dotted diagonal line passing through [1,0,0]. Invariance under reflection in all dotted diagonal lines will be called trilateral symmetry (note these reflections correspond to coordinate flips $u_{i} \leftrightarrow u_{j}$ on $\mathbb{C P}^{2}$, which are isometries of $g_{F S}$ ).}
\end{figure}
2.2. The Burns metric. We begin with a general result regarding the Green's function expansion for a toric Einstein manifold:

Proposition 2.2. Let $G$ be the Green's function for the conformal Laplacian at the point $p \in M$, where ( $M, g$ ) is an Einstein metric with positive scalar curvature. If $(M, g)$ admits a non-trivial torus action fixing the point $p$, then in a Riemannian normal coordinate system $\left\{z^{i}\right\}$, we have the following expansion: For any $\epsilon>0$,
$$G=|z|^{-2}+A+O^{(4)}\left(|z|^{2-\epsilon}\right)$$
as $|z| \rightarrow 0$, where $A$ is a constant (independent of $\epsilon$ ).
Proof. A straightforward computation, which we omit, shows that there is a formal power series solution of the form with leading terms
$$G=|z|^{-2}+A+\ldots,$$
and $A$ is a constant. Recall that the indicial roots of the Laplacian are $\mathbb{Z} \backslash\{-1\}$. Solutions corresponding to the indicial root 1 are linear, and not invariant under the torus action, so there is no linear term in the expansion. It follows from standard techniques that the formal expansion (2.12) implies the actual expansion (2.11). The
proof is identical to [LP87, Lemma 6.4] (using Riemannian normal coordinates instead of conformal normal coordinates), so the details are omitted. \(\square\)

In the case of the Fubini-Study metric, we have the following improved expansion:
Proposition 2.3. Let $G$ be the Green's function for the conformal Laplacian of the Fubini-Study metric based at [1, 0, 0], normalized so that $\operatorname{Ric}(g)=6 g$. Then in the above normal coordinate system $\left\{z^{i}\right\}$ we have the expansion
$$G=|z|^{-2}+\frac{1}{3}+O^{(4)}\left(|z|^{2}\right)$$
as $|z| \rightarrow 0$.
Proof. Since the metric is invariant under $U(2)$, from uniqueness of the Green's function, $G$ must be radial. Using that $R=24$, the equation is
$$\Delta G=4 G .$$
We let $\rho=|z|$ denote the radial distance function. For a radial function, (2.14) reduces to the ODE
$$G_{\rho \rho}+(3 \cot (\rho)-\tan (\rho)) G_{\rho}=4 G$$
on the interval $[0, \pi / 2]$. This ODE has the general solution
$$G=\frac{C_{1}}{\sin ^{2}(\rho)}+C_{2} \frac{\log (\cos (\rho))}{\sin ^{2}(\rho)}$$
for constants $C_{1}$ and $C_{2}$. The boundary condition $G=\rho^{-2}(1+o(1))$ as $\rho \rightarrow 0$ implies that $C_{1}=1$. For the other boundary condition, in order to give a smooth global solution, we require that $G_{\rho}(\pi / 2)=0$, which implies that $C_{2}=0$. The claimed expansion follows easily from
$$(\sin \rho)^{-2}=\rho^{-2}+\frac{1}{3}+\frac{1}{15} \rho^{2}+O^{(4)}\left(\rho^{4}\right)$$
as $\rho \rightarrow 0$. \(\square\)

Since $g_{F S}$ is Bach-flat (it is self-dual with respect to the complex orientation), the metric $g_{N}=G^{2} g_{F S}$ is also Bach-flat, and scalar-flat. Consequently, $g_{N}$ is $B^{t}$-flat for any $t \in \mathbb{R}$. Let $\left\{x^{i}=z^{i} /|z|^{2}\right\}$ denote inverted normal coordinates near [1, 0, 0], and let
$$\mathcal{I}(x)=\frac{x}{|x|^{2}}=z$$
denote the inversion map. With respect to these coordinates, we can write the metric $g_{N}$ in the complement of a large ball as
$$\begin{aligned}
g_{N} & =\mathcal{I}^{*}\left(G^{2} g_{F S}\right) \\
& =(G \circ \mathcal{I})^{2} \mathcal{I}^{*}\left(\left\{\delta_{i j}-\frac{1}{3} R_{i k j l}([1,0,0]) z^{k} z^{l}+O^{(4)}\left(|z|^{4}\right)_{i j}\right\} d z^{i} d z^{j}\right) \\
& =\left(|x|^{2}+A+O^{(4)}\left(|x|^{-2}\right)\right)^{2}\left\{\delta_{i j}-\frac{1}{3} R_{i k j l}([1,0,0]) \frac{x^{k} x^{l}}{|x|^{4}}+O^{(4)}\left(|x|^{-4}\right)_{i j}\right\} \\
& \cdot \frac{1}{|x|^{2}}\left(\delta_{i p}-\frac{2}{|x|^{2}} x^{i} x^{p}\right) d x^{p} \cdot \frac{1}{|x|^{2}}\left(\delta_{j q}-\frac{2}{|x|^{2}} x^{j} x^{q}\right) d x^{q}
\end{aligned}$$
so we have the expansion
$$\left(g_{N}\right)_{i j}(x)=\delta_{i j}-\frac{1}{3} R_{i k j l}([1,0,0]) \frac{x^{k} x^{l}}{|x|^{4}}+2 A \frac{1}{|x|^{2}} \delta_{i j}+O^{(4)}\left(|x|^{-4}\right)$$
as $|x| \rightarrow \infty$. Clearly, $g_{N}$ is asymptotically flat (AF) of order $\gamma=2$.
Note that this metric is also invariant under the standard linear action of $U(2)$, now acting in the $\{x\}$-coordinates.

Remark 2.4. As the title of the subsection indicates, this metric is also known as the Burns metric; it is a Kähler scalar-flat metric on the blow-up of $\mathbb{C}^{2}$ at the origin. By the coordinate change $r=\sin ^{-1}(\rho)$, and multiplying by $r^{4}$, one obtains
$$g_{N}=\frac{d r^{2}}{1-r^{-2}}+r^{2}\left[\sigma_{1}^{2}+\sigma_{2}^{2}+\left(1-r^{-2}\right) \sigma_{3}^{2}\right]$$
which is the expression of the Burns metric obtained in [LeB88]. We could instead use this coordinate system for the Burns metric in this paper. However, since there is not an analogue of this for the next example, we will remain with the above inverted Riemannian normal coordinates, in order to give a unified approach.

We note here the following, which relates the constant $A$ to the mass of the Green's function metric, and will be used later.

Proposition 2.5. Let $(M, g)$ be as in Proposition 2.2. Then the mass of the $A F$ metric $g_{N}=G^{2} g$ on $N=M \backslash\{p\}$ is given by
$$\operatorname{mass}\left(g_{N}\right)=12 A-\frac{R(p)}{12} .$$
Proof. This follows from (1.15) using inverted normal coordinates; the routine calculation is omitted. \(\square\)

For the Fubini-Study metric, since $R(p)=24$, and $A=1 / 3$, this implies that
$$\operatorname{mass}\left(g_{N}\right)=2 .$$
2.3. The product metric on $S^{2} \times S^{2}$. Next, we consider $S^{2} \times S^{2}$ with metric $g=g_{S^{2}} \times g_{S^{2}}$ the product of metrics of constant Gaussian curvature 1. The torus action we will consider is just the product of counter-clockwise $S^{1}$-rotations fixing the north and south poles. This action has 4 fixed points $(n, n),(n, s),(s, n)$, and $(s, s)$, where $n$ and $s$ are the north and south poles, respectively.

Taking normal coordinates on each factor around $(n, n) \in S^{2} \times S^{2}$, yields a normal coordinate system $\left(r_{1}, \theta_{1}, r_{2}, \theta_{2}\right)$ so that
$$g_{S^{2} \times S^{2}}=d r_{1}^{2}+\sin ^{2}\left(r_{1}\right) d \theta_{1}^{2}+d r_{2}^{2}+\sin ^{2}\left(r_{2}\right) d \theta_{2}^{2},$$
and the radial distance function is given by $\rho=\sqrt{r_{1}^{2}+r_{2}^{2}}$. Finally, we let $\left\{z^{i}\right\}$ be Euclidean normal coordinates based at $(n, n)$, so that the above torus action acts by
$$\left(z_{1}, z_{2}, z_{3}, z_{4}\right) \mapsto\left(e^{\sqrt{-1} \theta_{1}}\left(z_{1}+\sqrt{-1} z_{2}\right), e^{\sqrt{-1} \theta_{2}}\left(z_{3}+\sqrt{-1} z_{4}\right)\right) .$$
In this coordinate system, we have the expansion
$$g_{i j}=\delta_{i j}-\frac{1}{3} R_{i k j l}((n, n)) z^{k} z^{l}+O\left(|z|^{4}\right)_{i j}$$
as $|z| \rightarrow 0$.
In addition to toric invariance, this metric is also invariant under the diagonal symmetry:
$$\left(z_{1}, z_{2}, z_{3}, z_{4}\right) \mapsto\left(z_{3}, z_{4}, z_{1}, z_{2}\right) .$$
We will also impose this as an extra symmetry for the equivariant gluing problem. These symmetries, as well as some other symmetries we will use later, are illustrated in Figure 2.2.

As mentioned in the introduction, the product metric on $S^{2} \times S^{2}$ admits the Einstein quotient $S^{2} \times S^{2} / \mathbb{Z}_{2}$, where $\mathbb{Z}_{2}$ acts by the antipodal map on both factors, and the quotient $\mathbb{R P}^{2} \times \mathbb{R P}^{2}$. These quotients are also toric and the same expansion (2.26) holds for these. The diagonal symmetry also descends to a symmetry of these metrics.
2.4. Green's function of product metric. Let $G$ be the Green's function for the conformal Laplacian of the product metric at the point $(n, n)$, normalized so that $R=4$. By Proposition 2.2, in the above normal coordinate system $\left\{z^{i}\right\}$, for any $\epsilon>0$, we have the expansion
$$G=|z|^{-2}+A+O^{(4)}\left(|z|^{2-\epsilon}\right)$$
as $|z| \rightarrow 0$, where $A$ is a constant (independent of $\epsilon$ ).
Since $g_{S^{2} \times S^{2}}$ is Bach-flat (it is Einstein), the metric $g_{N}=G^{2} g_{S^{2} \times S^{2}}$ is also Bachflat, and scalar-flat. Consequently, $g_{N}$ is $B^{t}$-flat for any $t \in \mathbb{R}$. Letting $\left\{x^{i}=z^{i} /|z|^{2}\right\}$ denote inverted normal coordinates, analogous to (2.20), the metric $g_{N}$ admits the expansion
$$\left(g_{N}\right)_{i j}(x)=\delta_{i j}-\frac{1}{3} R_{i k j l}((n, n)) \frac{x^{k} x^{l}}{|x|^{4}}+2 A \frac{1}{|x|^{2}} \delta_{i j}+O^{(4)}\left(|x|^{-4+\epsilon}\right)$$
as $|x| \rightarrow \infty$, for any $\epsilon>0$. Clearly, $g_{N}$ is AF of order $\gamma=2$.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/f26727bd-f2f4-4432-97d4-75d415edfc6a-16.jpg?height=713&width=733&top_left_y=319&top_left_x=697}
\captionsetup{labelformat=empty}
\caption{Figure 2.2. Orbit space of the torus action on $S^{2} \times S^{2}$. The vertices of the square are fixed points, open edge points are circle orbits, and interior points are principal orbits. The diagonal symmetry is a reflection in the dotted diagonal line passing through $(n, n)$. The bilateral symmetry is reflection in the dotted anti-diagonal line. Reflection in the dotted vertical line is the antipodal map of the first factor, while reflection in the dotted horizontal line is the antipodal map of the second factor. Invariance under all of these reflections will be called quadrilateral symmetry.}
\end{figure}

This metric is invariant under the above diagonal torus action, now acting in the $\{x\}$-coordinates, and is also invariant under the diagonal symmetry
$$\left(x_{1}, x_{2}, x_{3}, x_{4}\right) \mapsto\left(x_{3}, x_{4}, x_{1}, x_{2}\right) .$$

Remark 2.6. Unlike the case of the Burns metric, there is no explicit description of this metric known (to the best of the authors' knowledge). Since the metric is invariant under the above torus action, from uniqueness of the Green's function, $G=G\left(r_{1}, r_{2}\right)$. Using that $R=4$, the equation is
$$\Delta G=\frac{2}{3} G .$$
Since $G=G\left(r_{1}, r_{2}\right)$, a computation shows that this reduces to the PDE
$$G_{r_{1} r_{1}}+\cot \left(r_{1}\right) G_{r_{1}}+G_{r_{2} r_{2}}+\cot \left(r_{2}\right) G_{r_{2}}=\frac{2}{3} G$$
on the square $[0, \pi] \times[0, \pi]$. Unlike the case of the Fubini-Study metric, this does not appear to admit any explicit solution.

\section*{3. The nonlinear map}

Let $(M, g)$ be a compact manifold of dimension 4, and Let $S^{2}\left(T^{*} M\right)$ denote the bundle of symmetric 2-tensors on $M$. We recall some important linear operators. For simplicity of notation, we will treat the domain and range of an operator as if it were the bundle itself, although the operator really acts on sections of the bundle. Let $\delta_{g}: S^{2}\left(T^{*} M\right) \rightarrow T^{*} M$ denote the divergence operator
$$\left(\delta_{g} h\right)_{j}=\nabla^{i} h_{i j},$$
and $\delta^{*}: T^{*} M \rightarrow S^{2}\left(T^{*} M\right)$ its $L^{2}$-adjoint. Note that
$$\delta^{*}=-\frac{1}{2} \mathcal{L}$$
where $\mathcal{L}$ is the Killing operator:
$$\left(\mathcal{L}_{g} \omega\right)_{i j}=\nabla_{i} \omega_{j}+\nabla_{j} \omega_{i} .$$
We let $\mathcal{K}_{g}$ denote the conformal Killing operator, the trace-free part of $\mathcal{L}_{g}$ :
$$\left(\mathcal{K}_{g} \omega\right)_{i j}=\nabla_{i} \omega_{j}+\nabla_{j} \omega_{i}-\frac{1}{2}\left(\delta_{g} \omega\right) g_{i j} .$$

Next, for a fixed background metric $g$, define the nonlinear map $P_{g}$
$$P_{g}^{t}: C^{4, \alpha}\left(S^{2}\left(T^{*} M\right)\right) \rightarrow C^{0, \alpha}\left(S^{2}\left(T^{*} M\right)\right)$$
by
$$P_{g}^{t}(\theta)=B^{t}(g+\theta)+\mathcal{K}_{g+\theta} \delta_{g} \mathcal{K}_{g} \delta_{g} \stackrel{\circ}{\theta},$$
where
$$\stackrel{\circ}{\theta}=\theta-\frac{1}{4} \operatorname{tr}_{g}(\theta) g .$$

Remark 3.1. The domain of $P_{g}^{t}$ is not actually the entire space; it is the subset of $C^{4, \alpha}$ so that $g+\theta$ is a Riemannian metric. The fact that the image lies in $C^{0, \alpha}$ is a consequence of $P_{g}^{t}$ being analytic as a function of $\theta$ and its derivatives up to order four.

We let $S_{g}^{t} \equiv\left(P_{g}^{t}\right)^{\prime}(0)$ denote the linearized operator at $\theta=0$.
Remark 3.2. When the base metric is clear from the context, we will often omit the subscript in the operator $P^{t}$ and its linearization $S^{t}$. To further simplify notation, we will also often omit the superscript $t$ from both of these operators, since it is clear that they depend on $t$.

Proposition 3.3. If $t \neq 0$, then $S^{t}$ is elliptic.
Proof. This is proved in [GV11, Theorem 2.7 (i)], although we provide a brief sketch since some of the formulas will be needed in subsequent sections. We also note a
difference in notation with our previous paper [GV11]. In that paper we considered the functional
$$\mathcal{F}_{\tau}=\int_{M}|\operatorname{Ric}|^{2} d V+\tau \int_{M} R^{2} d V$$
From (1.5), we obtain the relation
$$\mathcal{F}_{\tau}=16 \pi^{2} \chi(M)+\frac{1}{2} \mathcal{B}_{2\left(\tau+\frac{1}{3}\right)} .$$
Taking gradients, we obtain the relation
$$\nabla \mathcal{B}_{t}=2 \nabla \mathcal{F}_{\frac{t}{2}-\frac{1}{3}} .$$
It follows from the formula for $P$ that the linearized operator is given by
$$S^{t} h=\left(B^{\prime}+t C^{\prime}\right) h+\mathcal{K}_{g} \delta_{g} \mathcal{K}_{g} \delta_{g} \stackrel{\circ}{h},$$
where $B^{\prime}$ and $C^{\prime}$ are the linearizations of $B$ and $C$ respectively. Using (3.10), from [GV11, Equation (2.54)] the leading terms of $B^{\prime}+t C^{\prime}$ are
$$\begin{aligned}
\left(B^{\prime}+t C^{\prime}\right) h_{i j}= & \Delta^{2} h_{i j}-\Delta\left[\nabla_{i} \delta_{j} h+\nabla_{j} \delta_{i} h\right]-\left(2 t-\frac{1}{3}\right) \nabla_{i} \nabla_{j}(\Delta t r h) \\
& +\left(2 t+\frac{2}{3}\right) \nabla_{i} \nabla_{j}\left(\delta^{2} h\right)+\left(2 t-\frac{1}{3}\right)\left[\Delta^{2}(t r h)-\Delta\left(\delta^{2} h\right)\right] g_{i j}+\cdots
\end{aligned}$$
Also, a simple calculation gives
$$\begin{gathered}
\left(\mathcal{K}_{g} \delta_{g} \mathcal{K}_{g} \delta_{g} \stackrel{\circ}{h}\right)_{i j}=\Delta\left[\nabla_{i} \delta_{j} h+\nabla_{j} \delta_{i} h\right]-\frac{3}{4} \nabla_{i} \nabla_{j}(\Delta t r h)+\nabla_{i} \nabla_{j}\left(\delta^{2} h\right) \\
+\frac{3}{16} \Delta^{2}(t r h) g_{i j}-\frac{3}{4} \Delta\left(\delta^{2} h\right) g_{i j}+\cdots
\end{gathered}$$
Consequently,
$$\begin{aligned}
S h= & \Delta^{2} h-2\left(t+\frac{5}{24}\right) \nabla^{2}(\Delta t r h)-2\left(t+\frac{5}{24}\right) \Delta\left(\delta^{2} h\right) g \\
& +2\left(t+\frac{5}{6}\right) \nabla^{2}\left(\delta^{2} h\right)+2\left(t-\frac{7}{96}\right) \Delta^{2}(t r h) g+\cdots
\end{aligned}$$
It follows from (3.13) that the symbol of $S$ is
$$\begin{aligned}
\left(\sigma_{\xi} S\right) h_{i j}= & |\xi|^{4} h-2\left(t+\frac{5}{24}\right) \xi_{i} \xi_{j}|\xi|^{2}(\operatorname{tr} h)-2\left(t+\frac{5}{24}\right)|\xi|^{2} h_{k \ell} \xi_{k} \xi_{\ell} g_{i j} \\
& +2\left(t+\frac{5}{6}\right) \xi_{i} \xi_{j} h_{k \ell} \xi_{k} \xi_{\ell}+2\left(t-\frac{7}{96}\right)|\xi|^{4}(\operatorname{tr} h) g_{i j}
\end{aligned}$$
which is elliptic for $t \neq 0$, according to [GV11, Theorem 2.7 (i)]. \(\square\) \(\square\)

Remark 3.4. For purposes below, it will be useful to rewrite (3.13) as
$$S h=\Delta^{2}\left[h-\frac{1}{4}(\operatorname{tr} h) g\right]+\mathcal{K}\left[d\left(\mathcal{D}_{2}(h)\right)\right]+\frac{3}{2} t\left[\Delta^{2}(\operatorname{tr} h)-\Delta\left(\delta^{2} h\right)\right] g+\cdots$$
where $\mathcal{D}_{2}: S^{2} T^{*} M \rightarrow C^{\infty}$ is a second-order operator given by
$$\mathcal{D}_{2}(h)=\left(t+\frac{5}{6}\right) \delta^{2} h-\left(t+\frac{5}{24}\right) \Delta(t r h) .$$

The following proposition shows that the zeroes of $P$ are in fact $B^{t}$-flat metrics:
Proposition 3.5. Assume $t \neq 0$. If $P(\theta)=0$ and $\theta \in C^{4, \alpha}$ for some $0<\alpha<1$, then $B^{t}(g+\theta)=0$ and $\theta \in C^{\infty}$.

Proof. The equation is
$$B^{t}(g+\theta)+\mathcal{K}_{g+\theta} \delta_{g} \mathcal{K}_{g} \delta_{g} \stackrel{\circ}{\theta}=0 .$$
We claim that both terms on the left hand side of (3.17) vanish. The proof involves an integration by parts argument, but this presents a difficulty since $\theta \in C^{4, \alpha}$ only implies that $P_{g}(\theta)$ is $C^{\alpha}$, and not necessarily differentiable. To get around this problem we mollify $\theta$; i.e., let $\left\{\theta_{\epsilon}\right\}$ be a family of smooth tensor fields such that $\theta_{\epsilon} \rightarrow \theta$ in $C^{4, \alpha}$ as $\epsilon \rightarrow 0$, and let $\tilde{g}_{\epsilon}=g+\theta_{\epsilon}$. From (3.17) and the continuity of $P$ it follows that
$$\eta_{\epsilon}=B^{t}\left(g+\theta_{\epsilon}\right)+\mathcal{K}_{g+\theta_{\epsilon}}\left[\square_{\mathcal{K}_{g}} \beta_{g} \theta_{\epsilon}\right],$$
where $\eta_{\epsilon} \rightarrow 0$ in $C^{\alpha}$. Pair both sides of (3.18) with $\mathcal{L}_{\tilde{g_{\epsilon}}}\left[\square_{\mathcal{K}_{g}} \beta_{g} \theta_{\epsilon}\right]$ (with respect to the $L^{2}$-inner product defined by $\tilde{g}_{\epsilon}$ ), where $\mathcal{L}$ is the Killing operator defined in (3.3):
$$\begin{aligned}
\left\langle\mathcal{L}_{\tilde{g}_{\epsilon}}\left[\square \mathcal{K}_{g} \beta_{g} \theta_{\epsilon}\right], \eta_{\epsilon}\right\rangle_{L^{2}} & =\left\langle\mathcal{L}_{\tilde{g}_{\epsilon}}\left[\square_{\mathcal{K}_{g}} \beta_{g} \theta_{\epsilon}\right], B^{t}\left(\tilde{g}_{\epsilon}\right)+\mathcal{K}_{\tilde{g}_{\epsilon}}\left[\square_{\mathcal{K}_{g}} \beta_{g} \theta_{\epsilon}\right]\right\rangle_{L^{2}} \\
& =\left\langle\mathcal{L}_{\tilde{g}_{\epsilon}}\left[\square_{\mathcal{K}_{g}} \beta_{g} \theta_{\epsilon}\right], B^{t}\left(\tilde{g}_{\epsilon}\right)\right\rangle_{L^{2}}+\left\|\mathcal{K}_{\tilde{g}_{\epsilon}}\left[\square_{\mathcal{K}_{g}} \beta_{g} \theta_{\epsilon}\right]\right\|_{L^{2}}^{2} .
\end{aligned}$$
Integrating by parts in the first term on the right-hand side, we get
$$\left\langle\mathcal{L}_{\tilde{g}_{\epsilon}}\left[\square_{\mathcal{K}_{g}} \beta_{g} \theta_{\epsilon}\right], B^{t}\left(\tilde{g}_{\epsilon}\right)\right\rangle_{L^{2}}=-2\left\langle\square_{\mathcal{K}_{g}} \beta_{g} \theta_{\epsilon}, \delta_{\tilde{g}_{\epsilon}}\left(B^{t}\left(\tilde{g}_{\epsilon}\right)\right)\right\rangle_{L^{2}}=0,$$
since $\mathcal{L}^{*}=-2 \delta$ and the gradient of a Riemannian functional is always divergence-free (see [Bes87], Proposition 4.11). Therefore,
$$\left\langle\mathcal{L}_{\tilde{g}_{\epsilon}}\left[\square_{\mathcal{K}_{g}} \beta_{g} \theta_{\epsilon}\right], \eta_{\epsilon}\right\rangle_{L^{2}}=\frac{1}{2}\left\|\mathcal{K}_{\tilde{g}_{\epsilon}}\left[\square_{\mathcal{K}_{g}} \beta_{g} \theta_{\epsilon}\right]\right\|_{L^{2}}^{2} .$$
Letting $\epsilon \rightarrow 0$, the left-hand side converges to zero, while the right-hand side converges to $\mathcal{K}_{\tilde{g}}\left[\square_{\mathcal{K}_{g}} \beta_{g} \theta\right]$, which consequently vanishes. We conclude that
$$B^{t}(\tilde{g})=0$$
as claimed.
Next, taking a trace of (3.19), yields
$$-6 t \Delta R_{\tilde{g}}=0,$$
which implies that the scalar curvature of $\tilde{g}$ is constant. The equation (3.19) then implies that $\Delta_{\tilde{g}}$ Ric $_{\tilde{g}} \in C^{2, \alpha}$ (more precisely, around any point $p \in M$, there exists a coordinate system $\left\{x^{i}\right\}$ such that the components are in $C^{2, \alpha}$ ), which implies that Ric $_{\tilde{g}} \in C^{4, \alpha}$. Since $\tilde{g} \in C^{4, \alpha}$, there exists a harmonic coordinate system $\left\{y^{i}\right\}$ around $p$ such that the equation
$$\frac{1}{2} \tilde{g}^{i j} \partial_{i j}^{2} \tilde{g}_{k l}+Q_{k l}(\partial \tilde{g}, \tilde{g})=-\operatorname{Ric}{ }_{k l}(\tilde{g})$$
holds, where $Q(\partial \tilde{g}, \tilde{g})$ is an expression that is quadratic in $\partial \tilde{g}$, polynomial in $\tilde{g}$ and has $\sqrt{|\tilde{g}|}$ in its denominator [Pet06]. From this we conclude that $\tilde{g}_{i j} \in C^{5, \alpha}$. A bootstrap argument shows that $\tilde{g}_{i j} \in C^{\ell, \alpha}$ for any $\ell>0$. \(\square\)

Later, we will view the nonlinear map in (3.6) as a mapping from
$$P_{g}: C_{\delta}^{4, \alpha} \rightarrow C_{\delta-4}^{0, \alpha},$$
where the spaces are certain weighted Hölder spaces with weight function $w>0$. Of course, since $w>0$ and $M$ is compact, these norms are equivalent to the usual Hölder norms. However, in the gluing construction, the weight function will become large, and these norms will then not be uniformly equivalent to the usual norms.

Next, we define the weighted norms we will use. For $\delta \in \mathbb{R}$, and a positive weight function $w>0$,
$$\|h\|_{C_{\delta}^{0}} \equiv\left\|w^{-\delta} h\right\|_{C^{0}}=\sup _{x \in M}\left|w^{-\delta}(x) h(x)\right| .$$
For $0<\alpha<1$, define the semi-norm
$$|h|_{C_{\delta}^{0, \alpha}} \equiv \sup _{x \in M}\left(w^{-\delta+\alpha}(x) \sup _{0<4 d(x, y) \leq w(x)} \frac{|h(x)-h(y)|}{d(x, y)^{\alpha}}\right) .$$
Finally, define the norm
$$\|h\|_{C_{\delta}^{k, \alpha}} \equiv \sum_{i=0}^{k}\left\|\nabla^{i} h\right\|_{C_{\delta-i}^{0}}+\left|\nabla^{k} h\right|_{C_{\delta}^{0, \alpha}} .$$

Remark 3.6. For the remainder of the paper, we fix $\alpha \in \mathbb{R}$ satisyfing $0<\alpha<1$.
3.1. Estimate on the nonlinear terms. The following proposition regarding the nonlinear structure of the operator $P_{g}$ is crucial and will be used througout the paper.

Proposition 3.7. Write
$$P_{g}(h)=P_{g}(0)+S_{g} h+Q_{g}(h),$$
where $S_{g}$ is the linearization of $P$. Then we have the following:
(i) If $h \in C^{4, \alpha}$ with $\|h\|_{C^{0}}<s_{0}$ small, then there exists a constant $C_{1}=C_{1}\left(s_{0}\right)$ so that $Q_{g}$ satisfies
$$\begin{aligned}
\left|Q_{g}(h)\right| \leq C_{1} & \left\{\left(\left|\nabla^{2} R m_{g}\right|+\left|R m_{g}\right|^{2}\right)|h|^{2}+\left|\nabla R m_{g}\right||h|\left|\nabla^{2} h\right|+\left|\nabla R m_{g}\right||h||\nabla h|\right. \\
& +\left|R m_{g}\right||h|\left|\nabla^{2} h\right|+\left|R m_{g}\right||h||\nabla h|^{2}+|h|\left|\nabla^{4} h\right| \\
& \left.+|\nabla h|\left|\nabla^{3} h\right|+\left|\nabla^{2} h\right|^{2}+|\nabla h|^{2}\left|\nabla^{2} h\right|+|\nabla h|^{4}\right\} .
\end{aligned}$$
$$\begin{aligned}
& w \geq 1, \\
& \delta<0 .
\end{aligned}$$

In addition, assume there is a constant $C_{0}>0$ such that
$$\begin{aligned}
w^{2}\left|R m_{g}\right| & \leq C_{0}, \\
w^{3}\left|\nabla_{g} R m_{g}\right| & \leq C_{0}, \\
w^{4}\left|\nabla_{g}^{2} R m_{g}\right| & \leq C_{0} .
\end{aligned}$$
Then, for $h_{i} \in C_{\delta}^{4, \alpha}$ with $\left\|h_{i}\right\|_{C_{\delta}^{4, \alpha}}<s_{0}$ small, there exists a constant $C_{2}=C_{2}\left(s_{0}\right)$ so that $Q_{g}$ satisfies the following estimate:
$$\left\|Q_{g}\left(h_{1}\right)-Q_{g}\left(h_{2}\right)\right\|_{C_{\delta-4}^{0, \alpha}} \leq C_{2}\left(\left\|h_{1}\right\|_{C_{\delta}^{4, \alpha}}+\left\|h_{2}\right\|_{C_{\delta}^{4, \alpha}}\right) \cdot\left\|h_{1}-h_{2}\right\|_{C_{\delta}^{4, \alpha}} .$$
Proof. Since the proof involves a rather lengthy calculation we begin with a brief overview. The tensor $B+t C$ can be schematically expressed as
$$B_{g}+t C_{g}=g * g^{-1} * g^{-1} * \nabla_{g}^{2} R m_{g}+g * g^{-1} * g^{-1} * R m_{g} * R m_{g},$$
where $R m_{g}$ denotes the curvature tensor of $g, g^{-1} * \cdots * g^{-1} * A * B$ denotes any linear combination of terms involving contractions of the tensor product $A \otimes B$, and $g^{-1} * \cdots * g^{-1} * \nabla_{g}^{k} * A$ denotes linear combinations of contractions of the $k$-th iterated covariant derivative of $A$. Since the mapping $P$ is defined by
$$P_{g}(h)=B_{g+h}+t C_{g+h}+\mathcal{K}_{g+h} \square_{g} \beta_{g} h,$$
the first step in proving the estimates is to analyze the curvature term
$$\begin{aligned}
B_{g+h}+t C_{g+h}= & (g+h) *(g+h)^{-1} *(g+h)^{-1} * \nabla_{g+h}^{2} R m_{g+h} \\
& +(g+h) *(g+h)^{-1} *(g+h)^{-1} * R m_{g+h} * R m_{g+h} .
\end{aligned}$$
The starting point is the formula
$$\Gamma(g+h)_{i j}^{k}=\Gamma(g)_{i j}^{k}+\frac{1}{2}(g+h)^{k m}\left\{\nabla_{j} h_{i m}+\nabla_{i} h_{j m}-\nabla_{m} h_{i j}\right\},$$
where $\Gamma(\cdot)$ denotes the Christoffel symbols of a metric. In the following, any covariant derivative without a subscript will mean with respect to the fixed metric $g$. Using this formula and the notation introduced above, we can express the covariant derivative with respect to the metric $g+h$ as
$$\nabla_{g+h} T=\nabla_{g} T+(g+h)^{-1} * \nabla_{g} h * T,$$
where $T$ is any tensor field. Also, by the standard formula for the (1,3)-curvature tensor in terms of the Christoffel symbols we have
$$R m_{g+h}=R m_{g}+(g+h)^{-1} * \nabla^{2} h+(g+h)^{-2} * \nabla h * \nabla h .$$

Taking the covariant derivative $\nabla_{g+h}$ of $R m_{g+h}$ and repeatedly using (3.35), we obtain
$$\begin{aligned}
\nabla_{g+h} R m_{g+h} & =\nabla R m_{g}+(g+h)^{-1} * R m_{g} * \nabla h+(g+h)^{-1} * \nabla^{3} h \\
& +(g+h)^{-2} *\left(\nabla^{2} h * \nabla h\right)+(g+h)^{-3} *(\nabla h * \nabla h * \nabla h) .
\end{aligned}$$

Differentiating again, repeating the above procedure and collecting terms we have
$$\begin{aligned}
\nabla_{g+h}^{2} R m_{g+h}= & \nabla^{2} R m_{g}+(g+h)^{-1} * \nabla R m_{g} * \nabla h+(g+h)^{-1} * R m_{g} * \nabla^{2} h \\
& +(g+h)^{-2} * R m_{g} * \nabla h * \nabla h+(g+h)^{-1} * \nabla_{g}^{4} h \\
& +(g+h)^{-2} * \nabla^{3} h * \nabla h+(g+h)^{-2} * \nabla^{2} h * \nabla^{2} h \\
& +(g+h)^{-3} * \nabla^{2} h * \nabla h * \nabla h+(g+h)^{-4} * \nabla h * \nabla h * \nabla h * \nabla h .
\end{aligned}$$
Therefore,
$$\begin{aligned}
& (g+h) *(g+h)^{-2} * \nabla_{g+h}^{2} R m_{g+h}= \\
& \quad(g+h) *\left\{(g+h)^{-2} * \nabla^{2} R m_{g}+(g+h)^{-3} * \nabla R m_{g} * \nabla h\right. \\
& \quad+(g+h)^{-3} * R m_{g} * \nabla^{2} h+(g+h)^{-4} * R m_{g} * \nabla h * \nabla h \\
& \quad+(g+h)^{-3} * \nabla^{4} h+(g+h)^{-4} * \nabla^{3} h * \nabla h \\
& \quad+(g+h)^{-4} * \nabla^{2} h * \nabla^{2} h+(g+h)^{-5} * \nabla^{2} h * \nabla h * \nabla h+ \\
& \left.\quad+(g+h)^{-6} * \nabla h * \nabla h * \nabla h * \nabla h\right\} .
\end{aligned}$$
Using (3.36), we have a similar expression for the second term in (3.33):
$$\begin{aligned}
& (g+h) *(g+h)^{-2} * R m_{g+h} * R m_{g+h} \\
& =(g+h) *\left\{(g+h)^{-2} * R m_{g} * R m_{g}+(g+h)^{-3} * R m_{g} * \nabla^{2} h\right. \\
& +(g+h)^{-4} * R m_{g} * \nabla h * \nabla h+(g+h)^{-4} * \nabla^{2} h * \nabla^{2} h \\
& \left.+(g+h)^{-5} * \nabla^{2} h * \nabla h * \nabla h+(g+h)^{-6} * \nabla h * \nabla h * \nabla h * \nabla h\right\} .
\end{aligned}$$
Combining (3.39) and (3.40) gives
$$\begin{aligned}
& (g+h) *\left\{(g+h)^{-2} * \nabla_{g+h}^{2} R m_{g+h}+(g+h)^{-2} * R m_{g+h} * R m_{g+h}\right\} \\
& =(g+h) *\left\{(g+h)^{-2} * \nabla^{2} R m_{g}+(g+h)^{-2} * R m_{g} * R m_{g}\right. \\
& +(g+h)^{-3} * \nabla R m_{g} * \nabla h+(g+h)^{-3} * R m_{g} * \nabla^{2} h \\
& +(g+h)^{-4} * R m_{g} * \nabla h * \nabla h+(g+h)^{-3} * \nabla^{4} h \\
& +(g+h)^{-4} * \nabla^{3} h * \nabla h+(g+h)^{-4} * \nabla^{2} h * \nabla^{2} h \\
& \left.+(g+h)^{-5} * \nabla^{2} h * \nabla h * \nabla h+(g+h)^{-6} * \nabla h * \nabla h * \nabla h * \nabla h\right\} .
\end{aligned}$$
Returning to the formula (3.32), the gauge-fixing term can be written
$$\begin{aligned}
& \mathcal{K}_{g+h} \square_{g} \beta_{g} h=(g+h)^{-1} *(g+h) * \nabla_{g+h}\left(\square_{g} \beta_{g} h\right) \\
& \quad=(g+h)^{-1} *(g+h) *\left(\nabla_{g}+(g+h)^{-1} * \nabla h\right) *\left(\square_{g} \beta_{g} h\right) \\
& \quad=(g+h)^{-1} *(g+h) * g^{-3} * g * \nabla^{4} h \\
& \quad+(g+h)^{-2} *(g+h) * g^{-3} * g * \nabla h * \nabla^{3} h
\end{aligned}$$

Combining (3.41) and (3.42) we finally have
$$\begin{aligned}
P_{g}(h)=(g+h) & *\left\{(g+h)^{-2} * \nabla^{2} R m_{g}+(g+h)^{-2} * R m_{g} * R m_{g}\right. \\
+ & (g+h)^{-3} * \nabla R m_{g} * \nabla h+(g+h)^{-3} * R m_{g} * \nabla^{2} h \\
+ & (g+h)^{-4} * R m_{g} * \nabla h * \nabla h+(g+h)^{-3} * \nabla^{4} h \\
+ & (g+h)^{-1} * g^{-3} * g * \nabla^{4} h+(g+h)^{-4} * \nabla^{3} h * \nabla h \\
+ & (g+h)^{-2} * g^{-3} * g * \nabla^{3} h * \nabla h+(g+h)^{-4} * \nabla^{2} h * \nabla^{2} h \\
+ & \left.(g+h)^{-5} * \nabla^{2} h * \nabla h * \nabla h+(g+h)^{-6} * \nabla h * \nabla h * \nabla h * \nabla h\right\} .
\end{aligned}$$

Since we are trying to estimate the remainder terms in the Taylor expansion of $P(h)$, we want to write the above expression in terms of its linearization; i.e.,
$$\begin{aligned}
P_{g}(h) & =P_{g}(0)+S h+\cdots \\
& =B_{g}+t C_{g}+S h+\cdots
\end{aligned}$$
To do this, we use the identity (which holds for $h$ small)
$$(g+h)^{-1}-g^{-1}=g^{-2} * h+\sum_{k \geq 2} g^{-k-1} * h^{k}$$
which follows from the usual geometric series formula. Therefore,
$$\left(g+h_{1}\right)^{-1}-\left(g+h_{2}\right)^{-1}=g^{-2} *\left(h_{1}-h_{2}\right)+\sum_{k \geq 2} g^{-k-1} *\left(h_{1}^{k}-h_{2}^{k}\right) .$$
Each term in the sum in (3.45) can be written
$$g^{-k-1} * h_{1}^{k}-g^{-k-1} * h_{2}^{k}=g^{-k-1} *\left(h_{1}-h_{2}\right) * \sum_{i+j=k-1} h_{1}^{i} * h_{2}^{j}$$
Therefore, for $h$ small we can write
$$(g+h)^{-1}-g^{-1}=g^{-2} * h+r_{1}(h),$$
where $r_{1}$ satisfies
$$\left|r_{1}\left(h_{1}\right)-r_{1}\left(h_{2}\right)\right| \leq C(g)\left(\left|h_{1}\right|+\left|h_{2}\right|\right)\left|h_{1}-h_{2}\right|$$
for $h_{1}, h_{2}$ small. In general we can write
$$(g+h)^{-k}-g^{-k}=g^{-k-1} * h+r_{k}(h),$$
where the remainder satisfies
$$\left|r_{k}\left(h_{1}\right)-r_{k}\left(h_{2}\right)\right| \leq C_{k}(g)\left(\left|h_{1}\right|+\left|h_{2}\right|\right)\left|h_{1}-h_{2}\right|,$$
with a similar estimate for the Hölder norm.
We note that, using the restrictions on the weight function assumed in (3.28), the assumption that $\left\|h_{i}\right\|_{C_{\delta}^{4, \alpha}}$ is small implies that the $C^{0}$-norm of $h_{i}$ is also small, so we are free to employ (3.50) in the following.

Next, we substitute (3.49) into each term of (3.43) involving a power of $(g+h)^{-1}$, then collect all terms which are zeroth order in $h$ (which combine to give $P_{g}(0)$ ), those which are linear in $h$ (which combine to give $S h$ ), and those which are higher order in $h$. For example, consider the term
$$\begin{aligned}
(g+h) *(g+h)^{-3} * \nabla^{4} h & =(g+h) *\left(g^{-3}+g^{-4} * h+r_{3}(h)\right) * \nabla^{4} h \\
& =g * g^{-3} * \nabla^{4} h+g * g^{-4} * h * \nabla^{4} h+g * r_{3}(h) * \nabla^{4} h \\
& +g^{-3} * h * \nabla^{4} h+g^{-4} * h * h * \nabla^{4} h+r_{3}(h) * h * \nabla^{4} h .
\end{aligned}$$

Next, apply (3.49) to each term in (3.43) in a similar fashion, and write the resulting expression as
$$P_{g}(h)=P_{g}(0)+S h+Q(h),$$
where $Q$ is
$$\begin{aligned}
Q(h) & =(g+h) *\left\{r_{2}(h) * \nabla^{2} R m_{g}+r_{2}(h) * R m_{g} * R m_{g}+g^{-4} * R m_{g} * h * \nabla^{2} h\right. \\
& +g^{-4} * \nabla R m_{g} * h * \nabla h+r_{3}(h) * \nabla R m_{g} * \nabla h+g^{-4} * R m_{g} * h * \nabla^{2} h \\
& +r_{3}(h) * R m_{g} * \nabla^{2} h+g^{-5} * R m_{g} * h * \nabla h * \nabla h \\
& +r_{4}(h) * R m_{g} * \nabla h * \nabla h+g^{-4} * h * \nabla^{4} h+g^{-5} * g * h * \nabla^{4} h \\
& +g^{-3} * g * r_{1}(h) * \nabla^{4} h+r_{3}(h) * \nabla^{4} h \\
& +g^{-4} * \nabla^{3} h * \nabla h+g^{-5} * h * \nabla h * \nabla^{3} h+r_{4}(h) * \nabla h * \nabla^{3} h \\
& +g^{-5} * g * \nabla^{3} h * \nabla h+g^{-6} * g * h * \nabla h * \nabla^{3} h+g^{-3} * g * r_{2}(h) * \nabla h * \nabla^{3} h \\
& +g^{-4} * \nabla^{2} h * \nabla^{2} h+g^{-5} * h * \nabla^{2} h * \nabla^{2} h+r_{4}(h) * \nabla^{2} h * \nabla^{2} h \\
& +g^{-3} * \nabla h * \nabla h * \nabla^{2} h+g^{-6} * h * \nabla h * \nabla h * \nabla^{2} h \\
& +r_{5}(h) * \nabla h * \nabla h * \nabla^{2} h+g^{-6} * \nabla h * \nabla h * \nabla h * \nabla h \\
& \left.+g^{-7} * h * \nabla h * \nabla h * \nabla h * \nabla h+r_{6}(h) * \nabla h * \nabla h * \nabla h * \nabla h\right\} .
\end{aligned}$$
The estimate (3.27) follows from considering each term in (3.52), inequality (3.50), and the smallness of $h$.

We can then prove (3.30) by a fairly straightforward-but, due to the number of terms, very lengthy-process. We will provide the details for estimating some representative terms; the rest can be handled similarly.

For example, consider the term
$$T(h)=g * g^{-4} * h * \nabla^{4} h .$$
Then
$$\begin{aligned}
T\left(h_{1}\right)-T\left(h_{2}\right) & =g * g^{-4} * h_{1} * \nabla^{4} h_{1}-g * g^{-4} * h_{2} * \nabla^{4} h_{2} \\
& =g * g^{-4} *\left(h_{1}-h_{2}\right) * \nabla^{4} h_{1}+g * g^{-4} * h_{2} * \nabla^{4}\left(h_{1}-h_{2}\right)
\end{aligned}$$

If $w$ denotes the weight, then this implies
$$\begin{aligned}
\left|T\left(h_{1}\right)-T\left(h_{2}\right)\right| w^{4-\delta} & \leq\left|h_{1}-h_{2}\right|\left|\nabla^{4} h_{1}\right| w^{4-\delta}+\left|h_{2}\right|\left|\nabla^{4}\left(h_{1}-h_{2}\right)\right| w^{4-\delta} \\
& =\left\{\left|h_{1}-h_{2}\right| w^{-\delta}\right\}\left\{\left|\nabla^{4} h_{1}\right| w^{4-\delta}\right\} w^{\delta} \\
& \quad+\left\{\left|h_{2}\right| w^{-\delta}\right\}\left\{\left|\nabla^{4}\left(h_{1}-h_{2}\right)\right| w^{4-\delta}\right\} w^{\delta} .
\end{aligned}$$
Since $w \geq 1$ and $\delta<0$, taking the supremum gives
$$\begin{aligned}
\left\|T\left(h_{1}\right)-T\left(h_{2}\right)\right\|_{C_{\delta-4}^{0}} & \leq\left\{\left\|h_{1}-h_{2}\right\|_{C_{\delta}^{0}}\left\|h_{1}\right\|_{C_{\delta-4}^{4}}+\left\|h_{2}\right\|_{C_{\delta}^{0}}\left\|h_{1}-h_{2}\right\|_{C_{\delta-4}^{4}}\right\} \\
& \leq C\left(\left\|h_{1}\right\|_{C_{\delta}^{4}}+\left\|h_{2}\right\|_{C_{\delta}^{4}}\right) \cdot\left\|h_{1}-h_{2}\right\|_{C_{\delta}^{4}}
\end{aligned}$$

Next, consider the term
$$\rho(h)=g * g^{-4} * R m_{g} * h * \nabla^{2} h .$$
Taking differences as we did above yields
$$\left|\rho\left(h_{1}\right)-\rho\left(h_{2}\right)\right| \leq\left|R m_{g} \| h_{1}-h_{2}\right|\left|\nabla^{2} h_{1}\right|+\left|R m_{g}\right|\left|h_{2}\right|\left|\nabla^{2}\left(h_{1}-h_{2}\right)\right| .$$
Multiplying by the appropriate power of the weight,
$$\begin{aligned}
\left|\rho\left(h_{1}\right)-\rho\left(h_{2}\right)\right| w^{4-\delta} \leq\left\{w^{2} \mid\right. & \left.R m_{g} \mid\right\}\left\{\left|h_{1}-h_{2}\right| w^{-\delta}\right\}\left\{\left|\nabla^{2} h_{1}\right| w^{2-\delta}\right\} w^{\delta} \\
& +\left\{w^{2}\left|R m_{g}\right|\right\}\left\{\left|h_{2}\right| w^{-\delta}\right\}\left\{\left|\nabla^{2}\left(h_{1}-h_{2}\right)\right| w^{2-\delta}\right\} w^{\delta}
\end{aligned}$$
Using (3.29), we arrive at an estimate similar to (3.54).
Finally, let us consider a term in $Q h$ which has a higher order of homogeneity,
$$K(h)=g * r_{6}(h) * \nabla h * \nabla h * \nabla h * \nabla h .$$
Then
$$\begin{aligned}
& K\left(h_{1}\right)-K\left(h_{2}\right)=g *\left[r_{6}\left(h_{1}\right)-r_{6}\left(h_{2}\right)\right] * \nabla h_{1} * \nabla h_{1} * \nabla h_{1} * \nabla h_{1} \\
& +g * r_{6}\left(h_{2}\right)\left\{\nabla\left(h_{1}-h_{2}\right) * \nabla h_{1} * \nabla h_{1} * \nabla h_{1}+\nabla h_{2} * \nabla\left(h_{1}-h_{2}\right) * \nabla h_{1} * \nabla h_{1}\right. \\
& \left.+\nabla h_{2} * \nabla h_{2} * \nabla\left(h_{1}-h_{2}\right) * \nabla h_{1}+\nabla h_{2} * \nabla h_{2} * \nabla h_{2} * \nabla\left(h_{1}-h_{2}\right)\right\}
\end{aligned}$$
Multiplying by the weight,
$$\begin{aligned}
\left|K\left(h_{1}\right)-K\left(h_{2}\right)\right| & w^{4-\delta} \leq C\left\{\left|h_{1}-h_{2}\right| w^{-\delta}\right\}\left\{\left|\nabla h_{1}\right| w^{1-\delta}\right\}^{4} w^{4 \delta} \\
& +C\left|\nabla\left(h_{1}-h_{2}\right)\right| w^{1-\delta}\left[\left\{\left|\nabla h_{1}\right| w^{1-\delta}\right\}^{3}+\left\{\left|\nabla h_{2}\right| w^{1-\delta}\right\}\left\{\left|\nabla h_{1}\right| w^{1-\delta}\right\}^{2}\right. \\
& \left.+\left\{\left|\nabla h_{1}\right| w^{1-\delta}\right\}\left\{\left|\nabla h_{2}\right| w^{1-\delta}\right\}^{2}+\left\{\left|\nabla h_{1}\right| w^{1-\delta}\right\}^{3}\right] w^{3 \delta}
\end{aligned}$$
which gives an estimate as in (3.54).
Similar arguments (estimating difference quotients) give the Holder estimate in (3.30). \(\square\)

Since the operator $P_{g}$ differs from $B^{t}$ only by the gauge term, a similar estimate holds for $B^{t}$, see the following Proposition. This fact will be used in several places below (e.g., Proposition 10.3).

Proposition 3.8. Let $\left(B_{g}^{t}\right)^{\prime}$ denote the linearization of the $B^{t}$ tensor:
$$\left(B_{g}^{t}\right)^{\prime} h=\left.\frac{d}{d s} B^{t}(g+s h)\right|_{s=0} .$$
If we write
$$B^{t}(g+h)=B^{t}(g)+\left(B_{g}^{t}\right)^{\prime} h+\mathcal{Q}_{g}(h),$$
then under the same assumptions as in (i) of Proposition 3.7, the remainder $\mathcal{Q}$ satisfies the estimate (3.27).

\section*{4. Cokernel on a compact manifold}

On a compact manifold $\left(Z, g_{Z}\right)$, with basepoint $z_{0}$, we define the weight function to be a smooth function satisfying
$$w(z)= \begin{cases}d\left(z, z_{0}\right) & d\left(z, z_{0}\right)<1 / 2 \\ 1 & d\left(z, z_{0}\right) \geq 1\end{cases}$$
and $1 / 2 \leq w(z) \leq 1$ when $1 / 2 \leq d\left(z, z_{0}\right) \leq 1$.
Theorem 4.1. Let $\left(Z, g_{Z}\right)$ be either $\mathbb{C P}^{2}$ with the Fubini-Study metric $g_{F S}$, or $S^{2} \times S^{2}$ with the product metric $g_{S^{2}} \times g_{S^{2}}$. Assume that
$$t<0,$$
and let $h \in C_{\delta}^{4, \alpha}$ solve the equation
$$S^{t}(h)=0$$
for $\delta<0$ with $|\delta|$ small. If $h$ is toric-invariant and diagonally invariant, then $h=c \cdot g_{Z}$ for some constant $c \in \mathbb{R}$. Consequently, if $h$ satisfies
$$h=O\left(|z|^{\delta}\right)$$
as $|z| \rightarrow 0$, for $\delta>0$, then $h \equiv 0$.
Proof. For $t \neq 0$, we define $H_{t}^{1}$ to be the kernel of the linearization of $P_{g}$ :
$$H_{t}^{1}=H_{t}^{1}(M, g)=\left\{h \in \bar{S}_{0}^{2}\left(T^{*} M\right) \mid S_{g}^{t} h=0\right\},$$
where
$$\bar{S}_{0}^{2}\left(T^{*} M\right)=\left\{h \in C^{4, \alpha}\left(S^{2}\left(T^{*} M\right)\right): \int\left(t r_{g} h\right) d V_{g}=0\right\} .$$
For $t=0$ (the Bach tensor), we restrict to traceless tensors:
$$H_{0}^{1}=H_{0}^{1}(M, g)=\left\{h \in C^{4, \alpha}\left(S_{0}^{2}\left(T^{*} M\right)\right) \mid S_{g}^{0} h=0\right\} .$$
If $H_{t}^{1}(M, g)=\{0\}$, we say that $(M, g)$ is infinitesimally $B^{t}$-rigid. We next quote two crucial rigidity theorems from [GV11] with the following caveat: as pointed out in
the proof of Proposition 3.3, a different parametrization $\tau$ was used in [GV11]. The relation between $\tau$ and $t$ is given by
$$\tau=\frac{t}{2}-\frac{1}{3} .$$
The following is then a direct consequence of [GV11, Theorem 7.8]:
Theorem 4.2 ([GV11]). On $\left(\mathbb{C P}^{2}, g_{F S}\right), H_{t}^{1}=0$ provided that $t<1$.
The following is a direct consequence of [GV11, Theorem 7.13]:
Theorem 4.3 ([GV11]). On $\left(S^{2} \times S^{2}, g_{S^{2} \times S^{2}}\right)$, $H_{t}^{1}=0$ provided that $t<2 / 3$ and $t \neq-1 / 3$. If $t=-1 / 3$, then $H_{t}^{1}$ is one-dimensional and spanned by the element $g_{1}-g_{2}$.