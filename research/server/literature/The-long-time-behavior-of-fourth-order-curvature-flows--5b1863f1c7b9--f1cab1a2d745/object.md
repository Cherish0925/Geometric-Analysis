# The long time behavior of fourth-order curvature flows

- Category: papers
- Identity: arxiv:1103.4136
- Content status: fulltext_ok

---

---
source_file: 1103_4136.pdf
converter: mathpix
format: mmd
---

\section*{THE LONG TIME BEHAVIOR OF FOURTH ORDER CURVATURE FLOWS}

\begin{abstract}
We show precompactness results for solutions to parabolic fourth order geometric evolution equations. As part of the proof we obtain smoothing estimates for these flows in the presence of a curvature bound, an improvement on prior results which also require a Sobolev constant bound. As consequences of these results we show that for any solution with a finite time singularity, the $L^{\infty}$ norm of the curvature must go to infinity. Furthermore, we characterize the behavior at infinity of solutions with bounded curvature.
\end{abstract}

\section*{1. Introduction}

We say that a one-parameter family of metrics $\left(M^{n}, g(t)\right)$ is a solution to fourth-order curvature flow (FOCF) if $g(t)$ and the associated Riemannian curvatures $\operatorname{Rm}(t)$ satisfy
$$\begin{aligned}
\frac{\partial}{\partial t} g & =\nabla^{2} \mathrm{Rm} * g+\mathrm{Rm}^{* 2}, \\
\frac{\partial}{\partial t} \mathrm{Rm} & =-\Delta^{2} \mathrm{Rm}+\nabla^{2} \mathrm{Rm} * \mathrm{Rm}+\nabla \mathrm{Rm}^{* 2}+\mathrm{Rm}^{* 3} .
\end{aligned}$$
Here the notation $A * B$ refers to some metric contraction of the tensor product $A \otimes B$. Solutions to this system arise naturally as gradient flows of quadratic curvature functionals on Riemannian manifolds. Before discussing the results of this paper let us give some natural instances of FOCF. In particular, with the convention that $|\mathrm{Rm}|^{2}=g^{i p} g^{j q} g^{k r} g^{l s} R_{i j k l} R_{p q r s}$, let
$$\mathcal{F}(g):=\frac{1}{2} \int_{M}|\operatorname{Rm}|_{g}^{2} d V_{g} .$$
A basic calculation ([2] Proposition 4.70) shows that
$$\operatorname{grad} \mathcal{F}=\delta d \mathrm{Rc}-\check{R}+\frac{1}{4}|\operatorname{Rm}|^{2} g .$$
where $d$ is the exterior derivative acting on the Ricci tensor treated as a one-form with values in the tangent bundle, and $\delta$ is the adjoint of $d$. Moreover,
$$\check{R}_{i j}=R_{i p q r} R_{j}^{p q r} .$$
Suppose ( $M^{n}, g(t)$ ) is a solution to the negative gradient flow for $\mathcal{F}$, i.e.
$$\frac{\partial}{\partial t} g=-\operatorname{grad} \mathcal{F} .$$
It follows from [14] that $g(t)$ is a solution to FOCF.

\footnotetext{
Date: April 6, 2018.
The author was partly supported by a grant from the National Science Foundation.
}

Next, fix a Kähler manifold $\left(M^{2 n}, J, g\right)$. One may consider the $L^{2}$ norm of the scalar curvature restricted to the given Kähler class $[\omega]$. Expressing a general metric in the Kähler class as $\omega_{\phi}:=\omega+\sqrt{-1} \partial \bar{\partial} \phi$, we have
$$\mathcal{C}(\phi):=\int_{M} s_{\phi}^{2} d V_{\phi} .$$
The gradient of this functional is
$$\operatorname{grad} \mathcal{C}=\sqrt{-1} \partial \bar{\partial} s .$$
The associated gradient flow reduces to an equation for the Kähler potential, called the Calabi flow:
$$\frac{\partial}{\partial t} \phi=s-\frac{\int_{M} s d V}{\int_{M} d V} .$$
As is shown in [5] the associated one-parameter family of metrics $g_{\phi_{t}}$ is a solution to FOCF.

Recently Bour [3] studied the gradient flow of more general quadratic curvature functionals in dimension 4, obtaining a characterization of the sphere which improves the main result of [16]. These equations are not quite of the form (1.1), as the leading order term in the curvature evolution is slightly different, though still parabolic. However, since the key input to the strategy of the proof is the fact that one has local smoothing estimates in Sobolev spaces, the results in this paper should carry over to these flows mutatis mutandis.

Finally we point out that a family of higher order geometric evolutions was recently introduced in [1] with an aim toward prescribing the ambient obstruction tensor of Fefferman-Graham. In dimension four this flow corresponds to a certain conformally modified gradient flow for the $L^{2}$ norm of the Weyl curvature tensor, and thus is perhaps appropriately called Bach flow. This flow is also of the form (1.1).

At this point many analytic results have been established for these examples of FOCF. Below we will recall some results pertaining to solutions to (1.3), as they are indicative generally of the types of results which are available for these flows. In [14] we established the general short-time existence and a long-time existence obstruction for solutions to (1.3). Specifically we have

Theorem 1.1. ([14] Theorem 6.2) Let ( $M^{n}, g_{0}$ ) be a compact Riemannian manifold. The solution to (1.3) with initial condition $g_{0}$ exists on a maximal time interval $[0, T)$. Furthermore, if $T<\infty$ then either
$$\limsup _{t \rightarrow T}|\operatorname{Rm}|_{g(t)}=\infty$$
or
$$\limsup _{t \rightarrow T} C_{S}(g(t))=\infty$$
where $C_{S}(g(t))$ denotes the $L^{2}$ Sobolev constant of the time-dependent metrics.
The proof exploits $L^{2}$ derivative estimates satisfied by solutions of (1.3) in the presence of a curvature bound, then uses the Sobolev inequality to produce pointwise bounds from these estimates. Long-time existence criteria for the Calabi flow can be found in [4], [5]. Next we recall a compactness theorem for solutions to (1.3).

Theorem 1.2. ([14] Theorem 7.1) Let $\left(\left\{M_{i}, g_{i}(t), p_{i}\right\}\right)$ be a sequence of pointed solutions to (1.3) on compact manifolds $M_{i}$, where $t \in(\alpha, \omega),-\infty \leq \alpha<\omega \leq \infty$. Suppose there exists $C, K<\infty$ such that
$$\begin{aligned}
& \sup _{M_{i} \times(\alpha, \omega)}\left|\operatorname{Rm}\left(g_{i}\right)\right|_{g_{i}} \leq K, \\
& \lim _{t \searrow \alpha}\|\operatorname{Rm}\|_{L^{2}\left(g_{i}(t)\right)} \leq C,
\end{aligned}$$
and $\delta>0$ such that
$$\inf _{M_{i} \times(\alpha, \omega)} \operatorname{inj}_{g_{i}} \geq \delta .$$
Then there exists a subsequence which converges to a complete pointed solution to (1.3) $\left(M_{\infty}, g_{\infty}(t), p_{\infty}\right)$ with the same bounds on curvature and injectivity radius.

A similar result for the Calabi flow is implicit in [4]. This theorem is analogous to Hamilton's compactness result for Ricci flow ([10] Theorem 1.2). A weakness of using this result to understand blowup limits of solutions to (1.3) is of course the injectivity radius assumption. Observe that in fact we are assuming a uniform lower bound at all points of the manifold. This is because this implies a uniform upper bound on the Sobolev constants of the time evolving manifolds, which the proof requires since it relies on $L^{2}$ bounds to obtaining the higher order estimates. One does not have a noncollapsing estimate at the scale of curvature for solutions to (1.3) akin to Perelman's estimate for solutions to Ricci flow ([13]) therefore at present Theorem 1.2 cannot be applied to understand general blowup limits of solutions to FOCF.

Our first new theorem is a generalization of Theorem 1.2 to sequences of solutions of FOCF with uniform $C^{k}$ bounds on curvature but no injectivity radius estimate. This theorem appears in section 3, and both the statement and proof are analogous to a weak compactness theorem proved for solutions to Ricci flow by Glickenstein [9]. In fact Glickenstein's theorem does not use the precise structure of Ricci flow, except to exploit the derivative estimates which automatically hold in the presence of a curvature bound. For our statement we have assumed the necessary bounds and so his proof is easy to adapt to this setting. For solutions to FOCF, direct smoothing techniques only yield bounds for curvature in $H_{k}^{2}$, and require a Sobolev constant estimate to convert to pointwise bounds, something we are specifically trying to avoid. However, in an interesting twist, we are able to exploit this compactness theorem to prove $C^{k}$ smoothing estimates without a Sobolev constant bound. Specifically, we have:

Theorem 1.3. Fix $m, n \geq 0$. There exists a constant $C=C(m, n)$ so that if $\left(M^{n}, g(t)\right)$ is a complete solution to FOCF on $[0, T]$ satisfying
$$\sup _{M \times[0, T]}|\operatorname{Rm}| \leq K,$$
then for all $t \in(0, T]$,
$$\sup _{M}\left|\nabla^{m} \mathrm{Rm}\right|_{g(t)} \leq C\left(K+\frac{1}{t^{\frac{1}{2}}}\right)^{1+\frac{m}{2}} .$$

Remark 1.4. In a recent paper on the Calabi flow on toric varieties, [11], a bound for the first derivative of curvature is required in the presence of a curvature bound. Theorem
1.3 provides this estimate. From there the obstruction to long time existence is given by a certain bound on the derivative of scalar curvature.

We can now turn around and exploit Theorem 1.3 and the weak compactness theorem of section 3 to obtain a stronger compactness result as a corollary.
Corollary 1.5. Let $\left\{\left(M_{i}^{n}, g_{i}(t), p_{i}\right)\right\}$ be a sequence of complete pointed solutions of FOCF, where $t \in(\alpha, \omega),-\infty \leq \alpha<\omega \leq \infty$. Suppose there exists $K<\infty$ such that
$$\sup _{M_{i} \times(\alpha, \omega)}\left|\operatorname{Rm}\left(g_{i}\right)\right|_{g_{i}} \leq K .$$
Then there exists a subsequence $\left\{\left(M_{i_{j}}, g_{i_{j}}(t), p_{i_{j}}\right)\right\}$ and a one parameter family of complete pointed metric spaces $(X, d(t), x)$ such that for each $t \in(\alpha, \omega),\left\{\left(M_{i_{j}}, d_{i_{j}}, p_{i_{j}}\right)\right\}$ converges to $(X, d(t), x)$ in the sense of $C^{\infty}$ local submersions. The local lifted metrics $h_{y}(t)$ are solutions to FOCF. Furthermore, if there exists a constant $\delta>0$ so that
$$\operatorname{inj}_{g_{i}(0)}\left(p_{i}\right) \geq \delta$$
then the limit space $(X, d(t), x)$ is a smooth $n$-dimensional Riemannian manifold, and the limiting metric is the $C^{\infty}$ limit of the metrics $g_{i}(t)$.

Going yet further, one can actually obtain convergence in the category of Riemannian groupoids. Compactness of solutions to Ricci flow on Riemannian groupoids satisfying a uniform curvature bound was established by Lott [12]. Again, this is less a statement about Ricci flow as it is a statement about one parameter families of metrics satisfying certain bounds on curvature and its derivatives. Therefore our smoothing estimates can be employed to carry his argument over to fourth order curvature flows. The relevant background and definitions will be given in section 6.
Theorem 1.6. Let $\left\{\left(M_{i}^{n}, g_{i}(t), p_{i}\right)\right\}$ be a sequence of complete pointed solutions of FOCF, where $t \in(\alpha, \omega),-\infty \leq \alpha<\omega \leq \infty$. Suppose there exists $K<\infty$ such that
$$\sup _{M_{i} \times(\alpha, \omega)}\left|\operatorname{Rm}\left(g_{i}\right)\right|_{g_{i}} \leq K .$$
Then there exists a subsequence $\left\{\left(M_{i_{j}}, g_{i_{j}}(t), p_{i_{j}}\right)\right\}$ such that $g_{i_{j}}(t)$ converges smoothly to a solution to $\operatorname{FOCF} g_{\infty}(t)$ on an $n$-dimensional étale groupoid $\left(G_{\infty}, p_{\infty}\right)$ defined on $(\alpha, \omega)$.
Remark 1.7. One could phrase everything we do here in the language of groupoids, but in the interests of clarity we have mainly focused on the notion of convergence of local submersions, which is probably more familiar to most.
Remark 1.8. For instances of FOCF which are gradient flows of positive quadratic scaleinvariant functionals, blowup limits of noncollapsed finite time singularities are automatically critical for the given functional. An interesting question prompted by this theorem is whether, for such gradient flows, the limits given by Theorem 1.6 are still critical points.

As another corollary to Theorem 1.3, we are able to give an improvement of Theorem 1.1,

Corollary 1.9. Let $\left(M^{n}, g\right)$ be a compact Riemannian manifold. The solution to (1.3) with initial condition $g$ exists on a maximal time interval $[0, T)$. Furthermore, if $T<\infty$ then
$$\limsup _{t \rightarrow T}|\operatorname{Rm}|_{g(t)}=\infty .$$

Remark 1.10. Theorem 1.1 allowed for the possibility that the solution could collapse with bounded curvature in finite time. This would be a very unfortunate outcome, leaving little hope to understand the singularity with blowup arguments. Corollary 1.9 ensures curvature blowup at a finite singular time.

Remark 1.11. Comparing Corollary 1.9 with Theorem 1.1 you might think we have shown that the Sobolev constant is always bounded, which is not the case. What we show is actually $C^{0}$ control over the metric in the presence of a curvature bound, a nontrivial statement for solutions to FOCF.

Remark 1.12. An important open problem is to show a noncollapsing estimate on the scale of curvature akin to Perelman's estimate for Ricci flow. Such a general estimate for solutions to FOCF which are gradient flows of $L^{2}$ curvature energies would in particular imply their long time existence on surfaces and three-manifolds using a blowup argument and Corollary 1.9.

Remark 1.13. We point out here that the methods of this paper should adapt to higherorder (even higher than fourth) geometric flows on manifolds, and other situations where the maximum principle is not available. A common feature of these equations is the presence of Sobolev space smoothing estimates, which require Sobolev constant hypotheses to convert into pointwise bounds to yield long time existence obstructions. The procedure employed in this paper allows you to remove some of these hypotheses. Here is the overall outline of the strategy:
\begin{itemize}
\item[-] Prove a precompactness result assuming $C^{k}$ bounds on curvature.
\item[-] By applying the $L^{2}$ smoothing estimates on the covering metric, use the compactness result and a blowup argument to show parabolic $C^{k}$ derivative estimates in the presence of a curvature bound.
\item[-] Turn these pointwise derivative estimates around the obtain a superior compactness result only assuming a curvature bound.
\item[-] Derive long time existence in the presence of a curvature bound using the pointwise smoothing estimates.
\end{itemize}

Remark 1.14. An interesting open problem is to localize the estimates of Theorem 1.3. Here again the fact that a curvature bound does not imply $C^{0}$ control of the metric makes things particularly difficult. This problem of course does not arise for Ricci flow, and in fact, the blowup argument of Theorem 1.3 can be applied locally to solutions of Ricci flow to get an estimate with particularly clean dependencies on time, curvature, and distance to the boundary.

Our final theorem concerns nonsingular solutions to the $L^{2}$ gradient flow. We first need to introduce the volume normalized version of (1.3). It follows from (1.2) that if $\left(M^{n}, g(t)\right)$ is a solution to (1.3) then
$$\frac{\partial}{\partial t} \operatorname{Vol}(g(t))=\frac{4-n}{4} \mathcal{F}(g(t)) .$$
In particular, the initial value problem
$$\begin{aligned}
\frac{\partial}{\partial t} g & =-\operatorname{grad} \mathcal{F}+\frac{n-4}{2 n} \frac{\mathcal{F}(g)}{\operatorname{Vol}(g)} \cdot g \\
g(0) & =g_{0},
\end{aligned}$$
preserves the volume of the time dependent metrics. One can check that for an initial metric $g_{0}$, the corresponding solutions to (1.3) and (1.5) differ by a rescaling in space and time. Furthermore, equation (1.5) is, once suitably normalized, the gradient flow of the functional
$$\widetilde{\mathcal{F}}(g)=\operatorname{Vol}(g)^{\frac{4-n}{n}} \mathcal{F}(g)$$

Definition 1.15. A solution $\left(M^{n}, g(t)\right)$ to (1.5) is nonsingular if it exists on $[0, \infty)$ with a uniform bound on the curvature tensor.

Theorem 1.16. Let $\left(M^{n}, g(t)\right)$ be a nonsingular solution to (1.5). Then either
\begin{itemize}
\item[-] For all $p \in M, \limsup _{t \rightarrow \infty} \operatorname{inj}_{p} g(t)=0$.
\item[-] There exists a sequence of times $t_{i} \rightarrow \infty$ such that $\left\{g\left(t_{i}\right)\right\}$ converges to a smooth metric on $M$ which is critical for $\widetilde{\mathcal{F}}$.
\item[-] There exists a sequence of points $\left(p_{i}, t_{i}\right), t_{i} \rightarrow \infty$ such that $\left\{\left(M, g\left(t_{i}\right), p_{i}\right)\right\}$ converges to a complete noncompact finite volume metric which is critical for $\mathcal{F}$.
\end{itemize}

Remark 1.17. The same theorem holds for solutions to any FOCF which is the gradient flow of a positive scale invariant functional, in particular the Calabi flow (replacing the word critical with extremal everywhere), and the flows of Bour mentioned above.

Here is an outline of the rest of the paper. In section 2 we collect a number of background results on Gromov-Hausdorff convergence from [9]. Section 3 has the proof of Theorem 3.1. In section 4 we prove local smoothing estimates for solutions to FOCF in the presence of certain pointwise bounds on curvature and the time derivative of the metric. In section 5 we give the proof of Theorem 1.3. We end in section 6 with the proofs of Corollary 1.5. 1.9, and Theorem 1.16.
Acknowledgements: The author would like to thank Aaron Naber for some helpful discussions, and an anonymous referee for a very thorough reading of a previous version of this paper.

\section*{2. Weak Convergence}

In this section we recall certain definitions of weak convergence of Riemannian manifolds. Further background on these definitions may be found in [8], [9].

Definition 2.1. A topological space $G$ is a pseudogroup if there exist pairs $(a, b) \in G \times G$ such that a product $a b \in G$ is defined satisfying
\begin{itemize}
\item[(1)] If $a b, b c,(a b) c, a(b c)$ are all defined, then $(a b) c=a(b c)$.
\item[(2)] If $a b$ is defined then for every neighborhood $W$ of $a b$ there are neighborhoods $a \in U$ and $b \in V$ such that for all $x \in U, y \in V, x y$ is defined and $x y \in W$.
\item[(3)] There is an element $e \in G$ such that for all $a \in G, a e$ is defined and $a e=a$.
\item[(4)] If for $(a, b) \in G \times G, a b$ is defined and $a b=e$, then $a$ is a left-inverse for $b$ and we write $a=b^{-1}$. If $b$ has a left inverse, then for every neighborhood $U$ of $b^{-1}$ there is a neighborhood $V$ of $b$ such that every $y \in V$ has a left inverse $y^{-1} \in U$.
\end{itemize}

The canonical example of a pseudogroup is a Lie group germ.
Definition 2.2. A pseudogroup $G$ is a Lie group germ if a neighborhood of the identity of $G$ can be given a differentiable structure such that the operations of group multiplication and inversion are differentiable maps when defined.

Definition 2.3. Fix $k \in \mathbb{R} \cup\{\infty\}$. A sequence of pointed $n$-dimensional Riemannian manifolds $\left\{\left(M_{i}^{n}, g_{i}, p_{i}\right)\right\}$ locally converges to a pointed metric space ( $X, d, x$ ) in the sense of $C^{k}$-local submersions at $x$ if there is a Riemannian metric $h$ on an open neighborhood $0 \in V \subset \mathbb{R}^{n}$, a pseudogroup $\Gamma$ of local isometries of ( $V, h$ ) such that the quotient is well-defined, an open set $U \subset X$ and maps
$$\phi_{i}:(V, 0) \rightarrow\left(M_{i}, p_{i}\right)$$
satisfying
\begin{itemize}
\item[(1)] $\left\{\left(M_{i}, d_{g_{i}}, p_{i}\right)\right\}$ converges to $(X, d, x)$ in the pointed Gromov-Hausdorff topology,
\item[(2)] the identity component of $\Gamma$ is a Lie group germ,
\item[(3)] $V / \Gamma, \bar{d}_{h} \cong(U, d)$ where $\bar{d}_{h}$ is the induced distance function on the quotient,
\item[(4)] $\left(\phi_{i}\right)_{*}$ is nonsingular on $V$ for all $i$,
\item[(5)] $h$ is the $C^{k}$ limit of $\phi_{i}^{*} g_{i}$, in the sense of uniform convergence on compact sets of the first $k$ derivatives. As $k \in \mathbb{R}$ this is meant in the usual Hölder sense.
\end{itemize}

Definition 2.4. Fix $k \in \mathbb{N} \cup\{\infty\}$. A sequence of pointed $n$-dimensional Riemannian manifolds $\left\{\left(M_{i}, g_{i}, p_{i}\right\}\right.$ converges to a pointed metric space $(X, d, x)$ in the sense of $C^{k}$ local submersions if for every $y \in X$ there are points $q_{i} \in M_{i}$ such that $\left\{\left(M_{i}, g_{i}, q_{i}\right)\right\}$ locally converges to $(X, d, y)$ in the sense of $C^{k}$ local submersions.

We now recall the compactness theorem of Glickenstein, which we will adapt in the next section to one-parameter families of metrics satisfying certain bounds on derivatives of curvature.

Theorem 2.5. [9] Theorem 3) Let $C_{k}>0$ be constants for $k \in \mathbb{N}$ and $\left\{\left(M_{i}^{n}, g_{i}(t), p_{i}\right)\right\}_{i=1}^{\infty}$, where $t \in[0, T]$, be a sequence of pointed solutions to the Ricci flow on complete manifolds such that
$$\begin{aligned}
|\mathrm{Rm}|_{g_{i}(t)} & \leq 1 \\
\left|\nabla_{i}^{k} \mathrm{Rm}\right|_{g_{i}(t)} & \leq C_{k},
\end{aligned}$$
for all $i, k \in \mathbb{N}$ and $t \in[0, T]$. Then there is a subsequence $\left\{\left(M_{i_{k}}, g_{i_{k}}(t), p_{i_{k}}\right)\right\}_{k=1}^{\infty}$ and a one parameter family of complete pointed metric spaces $(X, d(t), x)$ such that for each $t \in[0, T],\left(M_{i_{k}}, d_{g_{i_{k}}}(t), p_{i_{k}}\right)$ converges to $(X, d(t), x)$ in the sense of $C^{\infty}$-local submersions and the metrics $h_{y}(t)$ are solutions to the Ricci flow equation.

A fundamental result at the root of the proof of Theorem 2.5 and our adaptation Theorem 3.1 below is the next theorem on convergence of families of Riemannian manifolds.

Theorem 2.6. ([9] Theorem 20, Proposition 21) Let $\left.\left\{\left(M_{i}, g_{i}(t), p_{i}\right)\right)\right\}, t \in[0, T]$ be a sequence of pointed Riemannian manifolds of dimension $n$ satisfying that for every $\delta>0$ there is $\epsilon>0$ such that if $s, t \in[0, T],|s-t|<\epsilon$ then
$$(1+\delta)^{-1} g_{i}(s) \leq g_{i}(t) \leq(1+\delta) g_{i}\left(t_{0}\right)$$
for all $i>0$, and satisfying
$$\operatorname{Rc}\left(g_{i}(t)\right) \geq-A g_{i}(t) .$$
Then there is a subsequence $\left\{\left(M_{i_{k}}, g_{i_{k}}(t), p_{i_{k}}\right)\right\}$ and a 1 -parameter family of complete pointed metric spaces $\left(X_{\infty}(t), d_{\infty}(t), x_{\infty}(t)\right)$ such that for every $t \in[0, T]$ the subsequence
converges to $\left(X_{\infty}(t), d_{\infty}(t), x_{\infty}(t)\right)$ in the Gromov-Hausdorff topology. If furthermore
$$\left|\frac{\partial}{\partial t} g\right| \leq C$$
for all $t \in[0, T]$ then $\left(X_{\infty}(t), x_{\infty}(t)\right)$ is homeomorphic to $\left(X_{\infty}(0), x_{\infty}(0)\right)$ for all $t \in[0, T]$.

\section*{3. A weak compactness result}

The purpose of this section is to prove Theorem 3.1, a weak compactness theorem for one-parameter families of Riemannian metrics satisfying certain curvature bounds. As mentioned in the introduction, the proof is a direct adaptation of the main result of [9], therefore we only indicate the steps required to modify that proof and refer the reader to [9] for a more thorough discussion.

Theorem 3.1. Fix $k \in N \cup\{\infty\}, k \geq 3$. Let $\left\{\left(M_{i}, g_{i}(t), p_{i}\right)\right\}$ be a sequence of complete pointed solutions of FOCF on manifolds $M_{i}$, where $t \in(\alpha, \omega),-\infty \leq \alpha<\omega \leq \infty$. Suppose that for all $0 \leq l \leq k$ there exists a constant $C_{l}>0$ such that
$$\left|\nabla_{i}^{l} \operatorname{Rm}\left(g_{i}\right)\right|_{g_{i}} \leq C_{l} .$$
There exists a subsequence $\left\{\left(M_{i_{j}}, g_{i_{j}}(t), p_{i_{j}}\right)\right\}$ which converges to a one parameter family of complete pointed metric spaces $(X, d(t), x)$ such that for each $t \in(\alpha, \omega),\left\{\left(M_{i_{j}}, d_{i_{j}}, p_{i_{j}}\right)\right\}$ converges to $(X, d(t), x)$ in the sense of $C^{k-2-\beta}$ local submersions. The local lifted metrics $h_{y}(t)$ are solutions to FOCF.
Remark 3.2. A key point of the statement is that the local submersion structure, i.e. the local groups of isometries and quotient maps of Definition 2.3, are independent of time.

Lemma 3.3. Suppose $\left(M^{n}, g(t)\right)$ is a one parameter family of metrics and suppose
$$\sup _{M \times[0, T)}\left|\frac{\partial}{\partial t} g\right|_{g(t)} \leq A .$$
Then for all $s, t \in[0, T)$,
$$e^{-A|t-s|} g(s) \leq g(t) \leq e^{A|t-s|} g(s) .$$
Proof. This is a straightforward estimate, see for instance [6] Lemma 6.49. \(\square\)

Lemma 3.4. Suppose $\left(M^{n}, g(t)\right)$ is a one parameter family of metrics and suppose
$$\sup _{M \times[0, T)}\left|\frac{\partial}{\partial t} g\right|_{g(t)} \leq A .$$
Then for all $\rho>0$,
$$\begin{aligned}
B_{g(t)}\left(0, r_{A}(t) \rho\right) & \subset B_{g(0)}(0, \rho), \\
B_{(g(0)}\left(0, r_{A}(t) \rho\right) & \subset B_{g(t)}(0, \rho),
\end{aligned}$$
where
$$r_{A}(t)=\frac{1}{1+\left(e^{A t}-1\right)^{\frac{1}{2}}} .$$
Proof. Again this is a straightforward estimate, and one can consult [9] Proposition 19 for the argument for Ricci flow. \(\square\)

Lemma 3.5. Let $M$ be a Riemannian manifold with metric $g$. Let $K$ denote a compact subset of $M$, and $\left\{g_{i}\right\}$ a sequence of solutions to FOCF defined on open neighborhoods of $K \times[\alpha, \beta]$, where $0 \in[\alpha, \beta]$. Let $D, D_{i}$ and $|\cdot|,|\cdot|_{i}$ denote the Levi Civita connections and norms of $g$ and $g_{i}$ respectively. Fix $N \geq 0$, and suppose
\begin{itemize}
\item[(1)] There is a constant $C>0$ so that on $K$ one has
$$\frac{1}{C} g(0) \leq g_{i}(0) \leq C g(0) .$$
\item[(2)] For $j \leq N$, the covariant derivatives of $\left\{g_{i}\right\}$ with respect to $D$ are uniformly bounded at $t=0$ on $K$, i.e.
$$\left|D^{j} g_{i}\right| \leq C_{j} .$$
\item[(3)] For $j \leq N+2$, the $j$-th covariant derivative of $\left\{\mathrm{Rm}_{i}\right\}$ is bounded with respect to $\left\{g_{i}\right\}$ on $K \times[\alpha, \beta]$, i.e.
$$\left|D_{i}^{j} \operatorname{Rm}_{i}\right|_{i} \leq C_{j} .$$
\end{itemize}
Then the metrics $\left\{g_{i}\right\}$ are uniformly bounded with respect to $g$ on $K \times[\alpha, \beta]$, and moreover for $j \leq N$ the $j$-th covariant derivative of $\left\{g_{i}\right\}$ with respect to $D$ is uniformly bounded on $K \times[\alpha, \beta]$, i.e.
$$\left|D^{j} g_{i}\right| \leq \widetilde{C}_{j},$$
where these bounds all depend only on the assumed bounds and the dimension.
Proof. This is [10] Lemma 2.4, adapted to the case of FOCF, and also to the case where one is only assuming a finite number of derivatives of curvature are bounded. The proof relies on a straightforward integration in time using the derivative bounds. \(\square\)

We now proceed with the proof of Theorem 3.1, which closely follows the proof of [9] Theorem 3.

Proof. Recall that the statement assumed uniform pointwise bounds on the curvature and at least its first 3 derivatives. In particular the Ricci curvature is bounded below and $\left|\frac{\partial}{\partial t} g\right|$ is bounded. By applying Lemma 3.3 we see that the hypotheses of Theorem 2.6 are satisfied, and thus there is a one-parameter family of complete pointed metric spaces $(X, d(t), x)$ such that $\left\{\left(M_{i}, g_{i}(t), p_{i}\right)\right\}$ converges in the pointed Gromov-Hausdorff topology to $(X, d(t), x)$. It remains to understand the local submersion structure of this limit space $(X, d(t), x)$, and the proof is at this point a direct adaptation of the main result of [9], the only difference being convergence in $C^{k-2-\alpha}$, and so we refer the reader there for details. \(\square\)

\section*{4. Local Smoothing Estimates in Sobolev Spaces}

In this section we derive local estimates for the $H_{2}^{l}$ norms of curvature for a solution to (1.1). We will compute some evolution equations, but first let we introduce a helpful piece of notation. Given a tensor $A$, we we will write $P_{s}^{m}(A)$ for any universal expression of the form
$$P_{s}^{m}(A)=\sum_{i_{1}+\cdots+i_{s}=m} \nabla^{i_{1}} A * \cdots * \nabla^{i_{s}} A .$$

Lemma 4.1. Let ( $M^{n}, g(t)$ ) be a solution to FOCF. Then
$$\frac{\partial}{\partial t} \nabla^{k} \mathrm{Rm}=-\Delta^{2} \nabla^{k} \mathrm{Rm}+P_{2}^{k+2}(\mathrm{Rm})+P_{3}^{k}(\mathrm{Rm}) .$$
Proof. The proof is identical to [14] Proposition 4.3. \(\square\)

For now we fix a given solution $\left(M^{n}, g\right)$ to FOCF, and fix some further data. In particular, fix $\gamma \in C_{0}^{\infty}(M)$. Suppose that $K$ is a constant such that
$$\sup _{\operatorname{supp} \gamma \times[0, T]}\left\{|\operatorname{Rm}|+\left|\frac{\partial}{\partial t} g\right|+\left|\nabla \frac{\partial}{\partial t} g\right|\right\} \leq K .$$

Lemma 4.2. Let $\left(M^{n}, g(t)\right)$ denote a one-parameter family of Riemannian metrics on $[0, T]$. Let $\gamma \in C_{0}^{\infty}(M)$. There are constants $C_{1}$ and $C_{2}$ such that
$$\begin{aligned}
|d \gamma|_{g(t)} & \leq C_{1}\left(\left|\frac{\partial}{\partial t} g\right|, T,|d \gamma|_{g(0)}\right), \\
|\nabla \nabla \gamma|_{g(t)} & \leq C_{2}\left(\left|\frac{\partial}{\partial t} g\right|,\left|\nabla \frac{\partial}{\partial t} g\right|, T,|d \gamma|_{g(0)},\left|\nabla^{2} \gamma\right|_{g(0)}\right) .
\end{aligned}$$
Proof. This first estimate is straightforward. For the second we express the time-dependent Hessian as
$$(\nabla \nabla \gamma)_{i j}=\partial_{i} \partial_{j} \gamma-\Gamma_{i j}^{k} \partial_{k} \gamma .$$
Differentiating with respect to time yields
$$\begin{aligned}
\frac{\partial}{\partial t}|\nabla \nabla \gamma|_{g(t)}^{2} & =\nabla \frac{\partial}{\partial t} g * d \gamma * \nabla \nabla \gamma+\frac{\partial}{\partial t} g * \nabla^{2} \gamma^{* 2} \\
& \leq C\left(|d \gamma|,\left|\nabla^{2} \gamma\right|,\left|\frac{\partial}{\partial t} g\right|,\left|\nabla \frac{\partial}{\partial t} g\right|\right) .
\end{aligned}$$
The result follows. \(\square\)

In our setup the above lemma implies the estimates
$$\begin{aligned}
|d \gamma|_{g(t)} & \leq C\left(K, T,|d \gamma|_{g(0)}\right), \\
|\nabla \nabla \gamma|_{g(t)} & \leq C\left(K, T,|d \gamma|_{g(0)},\left|\nabla^{2} \gamma\right|_{g(0)}\right) .
\end{aligned}$$
We now recall an estimate from [14]. There is a typo we correct here in where line (4.7) in that paper only assumes a bound on the cutoff function for the initial metric. Also, we are applying the result to any solution to FOCF, not just solutions to (1.3), but the proof is identical.

Proposition 4.3. (14] Corollary 5.2) Let $\left(M^{n}, g(t)\right)$ be a solution to FOCF on $[0, T]$. Fix $\gamma \in C_{0}^{\infty}(M)$ and suppose $K$ and $L$ are constants such that
$$\begin{array}{r}
\sup _{\operatorname{supp} \gamma \times[0, T]}|\operatorname{Rm}| \leq K, \\
\sup _{[0, T]}(|d \gamma|+|\nabla \nabla \gamma|) \leq L .
\end{array}$$

Fix $W=\nabla^{m} \mathrm{Rm}$. Then for any $s \geq 2 m+4$, there exists a constant $C=C(m, s, L)$ such that
$$\frac{\partial}{\partial t} \int_{M}|W|^{2} \gamma^{s}+\frac{1}{2} \int_{M}\left|\nabla^{2} W\right|^{2} \gamma^{s} \leq C K^{2} \int_{M}|W|^{2} \gamma^{s}+C\left(1+K^{2}\right)\|\operatorname{Rm}\|_{L^{2}(\{\operatorname{supp} \gamma\})}^{2} .$$

Using this estimate we can prove a local smoothing estimate in Sobolev space norms which we will employ in the proof of Theorem 1.3.

Theorem 4.4. Let $\left(M^{n}, g(t)\right)$ be a solution to FOCF on $[0, T]$. Fix $r>0$ and suppose $x \in M$ satisfies
$$\sup _{[0, T] \times B_{g(T)}(x, r)}\left\{|\operatorname{Rm}|+\left|\frac{\partial}{\partial t} g\right|+\left|\nabla \frac{\partial}{\partial t} g\right|\right\} \leq K .$$
Given $m \geq 0$ there exists $C=C\left(m, \frac{1}{r}, T, K\right)$ such that
$$\left\|\nabla^{m} \operatorname{Rm}_{g(t)}\right\|_{L^{2}\left(B_{g(T)}(x, r)\right)}^{2} \leq \frac{C}{t^{m}} \sup _{[0, T]}\|\operatorname{Rm}\|_{L^{2}\left(B_{g(T)}(x, 2 r)\right)}^{2} .$$
Proof. We show the result for $m=2 n \geq 0$ even, and the result follows for $m$ odd by interpolation. Fix $m \geq 0$ even, and let $\beta_{k}$ be constants to be determined. Let $\gamma$ denote a cutoff function for the ball of radius $r$ with respect to the metric $g(T)$. This $\gamma$ satisfies
$$|d \gamma|_{g(T)}+|\nabla \nabla \gamma|_{g(T)} \leq C\left(\frac{1}{r}\right) .$$
Furthermore, by (4.3) and Lemma 4.2 we conclude that
$$\sup _{[0, T]}(|d \gamma|+|\nabla \nabla \gamma|) \leq L\left(T, K, \frac{1}{r}\right) .$$
Now let
$$\Phi:=\sum_{k=0}^{n} \beta_{k} t^{2 k}\left\|\gamma^{m+2} \nabla^{2 k} \mathrm{Rm}\right\|_{L^{2}}^{2} .$$
for constants $\beta_{k}$ to be determined, with $\beta_{n}=1$. It follows from Proposition 4.3 that
$$\begin{aligned}
\frac{d}{d t} \Phi \leq & \sum_{k=1}^{n}\left\|\gamma^{m+2} \nabla^{2 k} \operatorname{Rm}\right\|_{L^{2}}^{2}\left(C K^{2} \beta_{k} t^{2 k}-\frac{1}{2} \beta_{k-1} t^{2 k-2}+2 k \beta_{k} t^{2 k-1}\right) \\
& +C\left(m, s, L, K, T, \beta_{i}\right)\|\operatorname{Rm}\|_{L^{2}(\{\operatorname{supp} \gamma\})}^{2} .
\end{aligned}$$
It is clear that by an appropriate inductive choice of the constants $\beta_{i}$ with respect to the constants $K, L, T$ and $m$ we obtain
$$\frac{\partial}{\partial t} \Phi \leq C(m, s, L, K, T)\|\mathrm{Rm}\|_{L^{2}(\{\operatorname{supp} \gamma\})}^{2} .$$
Integrating this ODE yields the result for even $m$, and for odd $m$ the result follows using an interpolation inequality. \(\square\)

\section*{5. Proof of Theorem 1.3}

Here is a sketch of the proof of Theorem 1.3. Suppose there is no such constant $C$. Then one has a sequence of solutions $\left\{\left(M_{i}, g_{i}(t)\right\}\right.$ (note that the topology of $M_{i}$ is unknown) to FOCF with bounded curvature such that there exist points $\left(x_{i}, t_{i}\right)$ violating (1.4). Precisely by the scale-invariant nature of the claimed estimates, one can blow up at the scale of $\nabla^{m} \mathrm{Rm}$ and argue to get a well-defined local limit converging in the sense of $C^{\infty}$ submersions by the weak compactness theorem. This limit has vanishing curvature by construction. But also by construction the $m$-th covariant derivative is nonzero at the center point, a contradiction.

Proof. Fix $m, n>0$, and define the function
$$f_{m}(x, t, g):=\sum_{j=1}^{m}\left|\nabla^{j} \operatorname{Rm}\right|_{g(t)}^{\frac{2}{2+j}}(x) .$$
We will show that given a complete solution to FOCF as in the hypotheses, for all sufficiently large $m$ there is a constant $C=C(m, n)$ such that
$$f_{m}(x, t, g) \leq C\left(K+\frac{1}{t^{\frac{1}{2}}}\right) .$$
This clearly suffices to prove the theorem. It suffices for the proof here to assume $m \geq 3$. Suppose the claim was false. Take then a sequence $\left\{\left(M_{i}, g_{i}(t)\right)\right\}$ of complete solutions to FOCF satisfying the hypotheses of the theorem, together with points $\left(x_{i}, t_{i}\right)$ satisfying
$$\lim _{i \rightarrow \infty} \frac{f_{m}\left(x_{i}, t_{i}, g_{i}\right)}{K+\frac{1}{t_{i}^{\frac{1}{2}}}}=\infty,$$
Since each solution is smooth it follows that $t_{i}>0$. Without loss of generality we may choose the points $\left(x_{i}, t_{i}\right)$ such that
$$\frac{f_{m}\left(x_{i}, t_{i}, g_{i}\right)}{K+\frac{1}{t_{i}^{\frac{1}{2}}}}=\sup _{M_{i} \times(0, T]} \frac{f_{m}\left(x, t, g_{i}\right)}{K+\frac{1}{t^{\frac{1}{2}}}} .$$
Let $\lambda_{i}=f_{m}\left(x_{i}, t_{i}\right)$, and set
$$\widetilde{g}_{i}=\lambda_{i} g\left(t_{i}+\frac{t}{\lambda_{i}^{2}}\right) .$$
Let us make some observations about $\widetilde{g}_{i}$ which make clear why the estimates of the theorem take the form they do and moreover why we have made the choices above. First, observe that by construction the solution $\widetilde{g}_{i}$ exists on the time interval $\left[-t_{i} \lambda_{i}^{2}, 0\right]$. But since
$$t_{i}^{\frac{1}{2}} \lambda_{i}=\frac{f_{m}\left(x_{i}, t_{i}\right)}{\frac{1}{t_{i}^{\frac{1}{2}}}} \geq \frac{f_{m}\left(x_{i}, t_{i}\right)}{K+\frac{1}{t_{i}^{\frac{1}{2}}}},$$
and the right hand side above goes to infinity as $i \rightarrow \infty$ we conclude that the solutions $\widetilde{g}_{i}$ exist on $[-1,0]$ for all sufficiently large $i$. Next observe that
$$\frac{\lambda_{i}}{K}=\frac{f_{m}\left(x_{i}, t_{i}\right)}{K} \geq \frac{f_{m}\left(x_{i}, t_{i}\right)}{K+\frac{1}{t_{i}^{\frac{1}{2}}}}$$
and again the right hand side goes to infinity as $i \rightarrow \infty$. It follows that
$$\lim _{i \rightarrow \infty}\left|\widetilde{\operatorname{Rm}_{i}}\right| \leq \lim _{i \rightarrow \infty} \frac{K}{\lambda_{i}}=0 .$$
By construction clearly
$$\widetilde{f}_{m}\left(x_{i}, 0\right)=1 .$$
Also, we observe that for $\left(x_{i}^{\prime}, t_{i}^{\prime}\right) \in M_{i} \times[-1,0]$, using (5.2) one has
$$\begin{aligned}
\widetilde{f}_{m}\left(x_{i}^{\prime}, t_{i}^{\prime}\right) & =\frac{f_{m}\left(x_{i}^{\prime}, t_{i}+\frac{t_{i}^{\prime}}{\lambda_{i}^{2}}\right)}{\lambda_{i}} \\
& =\frac{f_{m}\left(x_{i}^{\prime}, t_{i}+\frac{t_{i}^{\prime}}{\lambda_{i}^{2}}\right)}{f_{m}\left(x_{i}, t_{i}\right)} \\
& \leq \frac{K+\left(t_{i}+\frac{t_{i}^{\prime}}{\lambda_{i}^{2}}\right)^{-\frac{1}{2}}}{K+t_{i}^{-\frac{1}{2}}} \\
& \leq 1 .
\end{aligned}$$

Thus the sequence of pointed solutions $\left\{\left(M_{i}, \widetilde{g}_{i}, x_{i}\right)\right\}$ has a uniform estimate on the first $m \geq 3$ derivatives of curvature on $M_{i} \times[-1,0]$. By Theorem 3.1 we have a oneparameter family of pointed metric spaces $(X, d(t), x)$ and a subsequence (denoted with the same index) such that $\left\{\left(M_{i}, \widetilde{g}_{i}(t), x_{i}\right)\right\}$ converges to $(X, d(t), x)$ in the sense of $C^{m-2-\alpha_{-}}$ local submersions. Actually, for our purposes here, the global convergence statement of Theorem 3.1 is not needed, only the pointwise statement that the pullbacks of $g_{i}(t)$ by the exponential map at $x_{i}$ converge on a ball in $\mathbb{R}^{n}$. In particular there is a sequence $\left\{\widetilde{h_{i}}\right\}$ of one-parameter families of local liftings of $\widetilde{g}_{i}(t)$ near $x_{i}$, defined on some ball $B(0, r) \subset \mathbb{R}^{n}$, converging to a one-parameter family $h_{\infty}(t)$, as guaranteed by Theorem 3.1. So far the convergence to $\widetilde{h}_{\infty}$ is only in the $C^{m-2-\alpha}$ topology, but we can improve this to $C^{\infty}$ convergence using Theorem 4.4. As the metrics $h_{i}$ are defined using the exponential map at $x_{i}$, and the curvature is uniformly bounded, we have that the metrics $\widetilde{h}_{i}(0)$ are uniformly $C^{0}$ equivalent to the Euclidean metric on $B(0, r)$. It follows that the Sobolev constant of $B_{\widetilde{h}_{i}(0)}(0, r)$ is uniformly bounded. Also, since $m \geq 3$, by (5.5) we have a uniform bound on $\frac{\partial}{\partial t} g$ and $\nabla \frac{\partial}{\partial t} g$ on [-1, 0] and so it follows from Theorem 4.4 that the $H_{2}^{p}$ norms of the curvature of $h_{i}(s), s \geq-\frac{1}{2}$ are uniformly bounded for all $p>0$. Using the Sobolev constant bound of $\widetilde{h}_{i}(0)$, it follows that the $C^{k}$ norms of the curvature of $\widetilde{h}_{i}(0)$ are uniformly bounded for all $k$, and thus by taking a further subsequence we conclude $C^{\infty}$ convergence to $\widetilde{h}_{\infty}(0)$. We conclude from this convergence and (5.4) that
$$f_{m}\left(0,0, \widetilde{h}_{\infty}\right)=1 .$$
However, we conclude from (5.3) that on $B(0, r)$,
$$\operatorname{Rm}_{\tilde{h}_{\infty}} \equiv 0 .$$
This is a clear contradiction and so the theorem follows. \(\square\)

\section*{6. Compactness Theorems}

We begin with the proof of Corollary 1.5.
Proof. By a diagonalization argument it suffices to find a convergent subsequence on a sequence of closed intervals whose endpoints approach $\alpha$ and $\omega$. By Theorem 1.3, the uniform curvature estimate implies a uniform bound on all derivatives of curvature for any closed interval contained inside $(\alpha, \omega)$. Theorem 3.1 then guarantees the existence of a subsequence converging in the sense of $C^{\infty}$-local submersions. Finally, if the injectivity radii at $p_{i}$ are uniformly bounded below, we claim the limit is a smooth manifold of the same dimension. At this point we have all of the estimates required in Hamilton's proof of the compactness of Ricci flow solutions under the hypotheses of bounded curvature and injectivity radius, and so the proof there carries over with trivial changes. Specifically, one can apply [10] Theorem 2.3 to our given sequence to conclude the existence of a subsequence where the Riemannian manifolds $\left\{M_{i}, g_{i}(0), p_{i}\right\}$ converge to $\left\{M_{\infty}, g_{\infty}, 0\right\}$. Next one can apply Lemma 3.5 (an easy adaptation of [10] Lemma 2.4) to conclude that there is a further subsequence which converges uniformly on compact subsets of $M \times(\alpha, \omega)$. \(\square\)

Now we give the proof of Theorem 1.6. We start with the main definition of a smooth étale groupoid. We do not give the more general definitions. One may consult [12] and the references therein for further background information.

Definition 6.1. A smooth étale groupoid is a pair of smooth manifolds $G^{(0)}, G^{(1)}$ together with
\begin{itemize}
\item[(1)] a smooth embedding
$$e: G^{(0)} \rightarrow G^{(1)},$$
\item[(2)] Source and range local diffeomorphisms $s, r: G^{(1)} \rightarrow G^{(0)}$ satisfying
$$s \circ e=r \circ e=\operatorname{Id}_{G^{(0)}} .$$
\item[(3)] A multiplication $G^{(1)} \times G^{(1)} \rightarrow G^{(1)}$ such that
\begin{itemize}
\item[(a)] $\gamma_{1} \gamma_{2}$ is defined if and only if $s\left(\gamma_{1}\right)=r\left(\gamma_{2}\right)$, in which case $s\left(\gamma_{1} \gamma_{2}\right)=s\left(\gamma_{2}\right)$ and $r\left(\gamma_{1} \gamma_{2}\right)=r\left(\gamma_{1}\right)$.
\item[(b)] $\left(\gamma_{1} \gamma_{2}\right) \gamma_{3}=\gamma_{1}\left(\gamma_{2} \gamma_{3}\right)$ whenever both sides are well defined.
\item[(c)] $\gamma s(\gamma)=r(\gamma) \gamma=\gamma$.
\end{itemize}
\end{itemize}

Since we are only concerned here with smooth étale groupoids we will simply refer to these as groupoids for the remainder of this paper. Given a groupoid, the orbit of $x$ is
$$\mathcal{O}_{x}=s\left(r^{-1}(x)\right) .$$
A pointed groupoid is a groupoid together with a marked orbit $\mathcal{O}_{x}$. Associated to a groupoid is a pseudogroup of diffeomorphisms of $G^{(0)}$. Specifically, given $\gamma \in G^{(1)}$, there exists a neighborhood $U$ of $\gamma$ in $G^{(1)}$ such that $\left\{\left(s\left(\gamma^{\prime}\right), r\left(\gamma^{\prime}\right) \mid \gamma^{\prime} \in U\right\}\right.$ is the graph of a diffeomorphism between neighborhoods of the source and range of $\gamma$. The pseudogroup $\mathcal{P}$ associated to a groupoid is generated by such local diffeomorphisms. A groupoid is Riemannian if there is a Riemannian metric $g$ on $G^{(0)}$ such that the elements of $\mathcal{P}$ act as Riemannian isometries. Finally, the dimension of a groupoid will be the dimension of the smooth manifold $G^{(0)}$.

With these preliminaries in place we can define the notion of convergence of Riemannian groupoids.

Definition 6.2. Let $\left\{\left(G_{i}, \mathcal{O}_{x_{i}}\right)\right\}$ be a sequence of pointed $n$-dimensional Riemannian groupoids, and let $\left(G_{\infty}, \mathcal{O}_{x_{\infty}}\right)$ be another pointed Riemannian groupoid. Let $J_{\infty}$ be the groupoid of 1-jets of local diffeomorphisms of $G_{\infty}^{(0)}$. We say that $\left\{\left(G_{i}, \mathcal{O}_{x_{i}}\right)\right\}$ converges to $\left(G_{\infty}, \mathcal{O}_{x_{\infty}}\right)$ in the pointed smooth topology if for all $R>0$,
\begin{itemize}
\item[(1)] There are pointed diffeomorphisms $\phi_{i, R}: B_{R}\left(\mathcal{O}_{x_{\infty}}\right) \rightarrow B_{R}\left(\mathcal{O}_{x_{i}}\right)$ defined for sufficiently large $i$ so that
$$\left.\lim _{i \rightarrow \infty} \phi_{i, R}^{*} g_{i}\right|_{B_{R}\left(\mathcal{O}_{x_{i}}\right)}=\left.g_{\infty}\right|_{B_{R}\left(\mathcal{O}_{x_{\infty}}\right)}$$
\item[(2)] After applying $\phi_{i, R}$, the images of $s_{i}^{-1}\left(\overline{B_{\frac{R}{2}}\left(\mathcal{O}_{x_{i}}\right)}\right) \cap r_{i}^{-1}\left(\overline{B_{\frac{R}{2}}\left(\mathcal{O}_{x_{i}}\right)}\right)$ in $J_{\infty}$ converge in the Gromov-Hausdorff topology to the image of $s_{\infty}^{-1}\left(\overline{B_{\frac{R}{2}}\left(\mathcal{O}_{x_{\infty}}\right)}\right) \cap r_{\infty}^{-1}\left(\overline{B_{\frac{R}{2}}\left(\mathcal{O}_{x_{\infty}}\right)}\right)$
\end{itemize}
Note that the groupoid of 1-jets of local diffeomorphisms of an étale groupoid is not itself étale, though this point will not concern us here. Also, note of course that we are identifying elements of $G_{i}^{(1)}$ first with local diffeomorphisms of $G_{i}^{(0)}$, and then considering the elements of $J_{i}$ they generate.

We can now give the proof of Theorem 1.6.
Proof. The main content is [12] Proposition 5.9:
Proposition 6.3. Let $\left\{\left(M_{i}, g_{i}, p_{i}\right)\right\}$ be a sequence of complete $n$-dimensional Riemannian manifolds. Suppose that for all $k, R \geq 0$ there is a constant $C_{k, R}$ such that for all $i$,
$$\sup _{B_{R}\left(p_{i}\right)}\left|\nabla^{k} \operatorname{Rm}\left(g_{i}\right)\right| \leq C_{k, R} .$$
Then there is a subsequence of $\left\{\left(M_{i}, g_{i}, p_{i}\right)\right\}$ which converges in the pointed smooth topology to an $n$-dimensional Riemannian groupoid $\left(G_{\infty}, \mathcal{O}_{\infty}\right)$.

With this we can apply the same strategy of Corollary 1.5 (i.e. the strategy of [10] Theorem 1.2). Given the pointwise smoothing estimates, the sequence of manifolds $\left\{\left(M_{i}, g_{i}(0), p_{i}\right)\right\}$ satisfies the hypotheses of the above proposition. Therefore a subsequence converges to some pointed Riemannian groupoid $\left(G_{\infty}, g_{\infty}(0), \mathcal{O}_{x_{\infty}}\right)$. One can repeat the argument of Lemma 3.5 ([10] Lemma 2.4) in the groupoid setting ([12] Theorem 5.12) to obtain a further subsequence which converges for all times the flow exists. The FOCF equation of course passes the limit solution. \(\square\)

\section*{7. Curvature blowup and nonsingular solutions}

We begin with the proof of Corollary 1.9
Proof. Suppose the maximal existence time of the solution is $T<\infty$ but
$$\sup _{[0, T)}|\operatorname{Rm}|<\infty .$$
By Theorem 1.3 one has
$$\sup _{[0, T)}|\operatorname{grad} \mathcal{F}|=C<\infty .$$

It follows from Lemma 3.3 that
$$e^{-C t} g(0) \leq g(t) \leq e^{C t} g(0) .$$
In particular, this $C^{0}$ equivalence of metrics clearly implies that
$$\lim _{t \rightarrow T} C_{S}(g(t))<\infty$$
By Theorem 1.1 we conclude that $T$ cannot be the maximal existence time. This contradicts the hypothesis that the curvature was bounded, therefore the corollary follows. \(\square\)

We end with the proof of Theorem 1.16.
Proof. First observe that since the functional $\widetilde{\mathcal{F}}$ is bounded below by zero and nonincreasing along a solution to (1.5) we have that
$$\int_{0}^{\infty} \int_{M}|\operatorname{grad} \widetilde{\mathcal{F}}|^{2} d V d t=\widetilde{\mathcal{F}}(g(0))-\lim _{t \rightarrow \infty} \widetilde{\mathcal{F}}(g(t))<\infty .$$
It follows that we may choose a sequence of times $t_{i} \rightarrow \infty$ such that
$$\lim _{i \rightarrow \infty}| | \operatorname{grad} \widetilde{\mathcal{F}}\left(g\left(t_{i}\right)\right)| |_{L^{2}}=0 .$$
Now let us assume without loss of generality that the first case does not occur. Then there exists $p \in M$ and $\delta>0$ such that $\operatorname{inj}_{g\left(t_{i}\right)}(p) \geq \delta>0$. It follows from Corollary 1.5 that there is a subsequence, also denoted $t_{i}$, such that $\left\{\left(M, g\left(t_{i}+t\right), p\right)\right\}$ converges to a new solution $\left(M_{\infty}, g_{\infty}(t), p_{\infty}\right)$ to (1.5). Since the convergence is $C^{\infty}$ on compact sets, it follows from (7.2) that the limiting metric $g_{\infty}(t)=g_{\infty}$ is critical for $\widetilde{\mathcal{F}}$. If $M_{\infty}$ is compact, it follows that $M_{\infty}$ is diffeomorphic to $M$ and thus the second alternative holds. If $M_{\infty}$ is noncompact the third alternative holds, and the theorem follows. \(\square\)

\section*{References}
[1] Bahuad, E. Helliwell, D. Short time existence for some higher order geometric flows, arXiv:1010.4287.
[2] Besse, A. Einstein Manifolds, Ergebnisse der Mathematik und ihrer Grenzgebiete (3), vol. 10, Springer-Verlag, Berlin, 1987.
[3] Bour, V. Fourth order geometric flows and applications, arXiv:1012.0342.
[4] Chen, X.X. He, Weiyong. On the Calabi flow Amer. J. Math. 130 (2008), no. 2, 539-570.
[5] Chen, X.X. He, Weiyong. The Calabi flow on Kähler surfaces with bounded Sobolev constant, arXiv:0710.5159.
[6] Chow, B. Knopf, D. The Ricci flow: an introduction, American Mathematical Society, 2004.
[7] Fukaya, K. Collapsing Riemannian manifolds to ones of lower dimensions, J. Differential Geom. 25 (1987), 139-156.
[8] Fukaya, K. A boundary of the set of Riemannian manifolds with bounded curvatures and diameters, J. Differential Geom. 28 (1988), 1-21.
[9] Glickenstein, D. Precompactness of solutions to the Ricci flow in the absence of injectivity radius estimates, Geom. and Top. Vol 7 (2003), 487-510.
[10] Hamilton, R. A compactness theorem for solutions of the Ricci flow, Amer. J. Math. 117 (1995), no. 3, 545-572.
[11] Huang, H. On the extension of the Calabi flow on toric varieties, Ann. Glob. Anal. and Geom., Vol. 40, No. 1, (2011), 1-19.
[12] Lott, J. On the long-time behavior of type III Ricci flow solutions, Math. Ann. 399 (2007), no. 3, 627-666.
[13] Perelman, G. The entropy formula for the Ricci flow and its geometric applications arXiv:math.DG/0211159.
[14] Streets, J. The gradient flow of $\int_{M}|\operatorname{Rm}|^{2}$, J. Geom. Anal. 18 (2008), no. 1, 249-271.
\begin{itemize}
\item[] [15] Streets, J. The gradient flow of the $L^{2}$ curvature functional with small initial energy, to appear J. Geom. Anal.
\item[] [16] Streets, J. The gradient flow of the $L^{2}$ curvature energy near the round sphere, arXiv:1003.1707
\item[] [17] Streets, J. The gradient flow of the $L^{2}$ curvature energy on surfaces, to appear, Int. Math. Res. Not.
\end{itemize}

Rowland Hall, University of California, Irvine, Irvine, CA 92617
E-mail address: jstreets@uci.edu
