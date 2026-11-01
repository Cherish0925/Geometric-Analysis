---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: Desingularizations of Conformally Kähler, Einstein Orbifolds]

By [43], then, after possibly passing to a subsequence, there then exist scales $t_{i}$, naïve desingularizations $g_{t_{i}}^{D}$, and parameters $v_{i} \in \mathfrak{O}\left(g_{b}\right) \times \mathfrak{O}\left(g_{\infty}\right)$ such that
\begin{itemize}
\item[-] $\left\|g_{i}-g_{t_{i}, v_{i}}^{A}\right\|_{C_{\beta, *}^{2, \alpha}\left(g_{t_{i}}^{D}\right)} \rightarrow 0$, and
\item[-] $g_{i}-g_{t_{i}, v_{i}}^{A} \perp_{g_{t j}^{D}} \tilde{\mathfrak{O}}\left(g_{t_{i}, v_{i}}^{A}\right)$.
\end{itemize}
Then [43, Proposition 5.11] tells us that
$$\left\|g_{i}-g_{t_{i}, v_{i}}^{A}\right\|_{C_{\beta, *}^{2, \alpha}\left(g_{t_{i}}^{D}\right)} \leqslant C\left\|\mathscr{F}_{g_{t_{i}}^{D}}\left(g_{t_{i}, v_{i}}^{A}\right)+\tilde{\mathfrak{D}}_{t_{i}, v_{i}}^{A}\right\|_{\varrho_{D}^{-2} C_{\beta}^{\alpha}\left(g_{t_{i}}^{D}\right)}^{A}=o\left(t_{i}\right)$$
as $i \rightarrow \infty$, by virtue of (23). This then allows us to obtain the following curvature-control: for some $C>0$, independent of $i$,
$$\left\|\mathrm{W}^{+}\left(g_{t_{i}, v_{i}}^{A}\right)-\mathrm{W}^{+}\left(g_{i}\right)\right\|_{C^{0}\left(g_{i}\right)} \leqslant C t_{i}^{-1}\left\|\mathrm{~W}^{+}\left(g_{t_{i}, v_{i}}^{A}\right)-\mathrm{W}^{+}\left(g_{i}\right)\right\|_{\varrho_{D}^{-2} C_{\beta}^{\alpha}\left(g_{t_{i}}^{D}\right)} \rightarrow 0$$
as $i \rightarrow \infty$, since, by definition of the norms: $\|\cdot\|_{C^{0}\left(g_{i}\right)} \leqslant C t_{i}^{-1}\|\cdot\|_{\varrho_{D}^{-2} C_{\beta}^{\alpha}\left(g_{t_{i}}^{D}\right)}$ because $\varrho_{D}^{2}>t_{i}$. However, because $\operatorname{det}\left(W^{+}\right)\left(g_{\infty}\right)>0$ everywhere,Corollary 8.4 implies that $\operatorname{det} \mathrm{W}^{+}\left(g_{t_{i}, v_{i}}^{A}\right)>0$ for $i \gg 0$. By (24), the open property
$\operatorname{det} \mathrm{W}^{+}>0$ is therefore inherited by the genuine Einstein metrics $g_{i}$ for sufficiently large $i$. We have thus shown that the Einstein metrics $g_{i}$ satisfy Wu's criterion (1), so it follows [34, 46] that the $g_{i}$ must be conformally Kähler when $i \gg 0$. However, such Einstein metrics on smooth 4-manifolds are actually all Kähler-Einstein, aside [31, Theorem A] from two stronglyrigid exceptions for which, up to isometries and rescalings, there is only one conformally-Kähler Einstein manifold on the given 4-manifold; but this rigid scenario is then precluded by our assumption that the limit has an orbifold singularity. We have thus shown that Theorems A and B do in fact hold in the test-case where $X$ has exactly one singularity, and no trees of singularities occur. \(\square\)

\section*{9 Without Trees of Singularities}

We now allow multiple singularities, but exclude the formation of trees of singularities. For example, as explained in Corollary 9.2 below, this applies to desingularizations of a Kähler-Einstein orbifolds with $c_{1}^{2}=4$. In general terms, this case is very similar to the situation discussed in §8, and can best be understood using the framework of [43, Section 5.2] through the use of partial Einstein-modulo-obstructions desingularizations. Roughly speaking, the idea is to desingularize the singularities one-by-one, from the smallest scale to the largest one. A priori, one can only partially desingularize by Einstein-modulo-obstruction metrics. Starting by the smallest scale is crucial as it ensures negligible perturbations of the orbifold at its remaining singular points.

Let us once again take $\left(M, g_{i}\right)$ to be an admissible sequence of Einstein metrics that converges to a conformally Kähler, Einstein orbifold $\left(X, g_{\infty}\right)$ in the Gromov-Hausdorff sense. We now allow $X$ to possibly have multiple singularities, but we still suppose trees of singularities do not occur. As in the previous Section 8, by [42, 43], then, up to taking a subsequence, for $i$ large enough, there exists a naïve desingularization $g_{t_{i}}^{D}$ and parameters $v_{i} \in \tilde{\mathfrak{D}}\left(g_{t_{i}}^{D}\right)$ such that: $\left\|g_{i}-g_{t_{i}}^{D}\right\|_{C_{\beta, *}^{2, \alpha}\left(g_{t_{i}}^{D}\right)} \rightarrow 0$. As in [43, Section 5.2], we will produce a better approximate metrics $g_{t_{i}, v_{i}}^{A}$ by using partial Einstein-moduloobstructions desingularizations as stepping stones.

\section*{Iterative partial naïve desingularizations}

After passing to a subsequence, we may assume that we can order the $n$ singular points of $X$ as $p_{1}, \ldots, p_{n}$ so that
$$0<t_{1, i} \leqslant t_{2, i} \leqslant \ldots \leqslant t_{n, i},$$
where $t_{k, i}$ is the scale of the gluing at $p_{k}$ in the construction of $g_{t_{i}}^{A}$ in Definition 10.

Definition 11 (Partial naïve desingularizations). For $k \in\{1, \ldots, n\}$, the $k^{\text {th }}$ partial desingularization of $\left(X, g_{\infty}\right)$, which we will denote by $\left(Y_{k}, g_{t}^{D_{k}}\right)$, is obtained by the naïve gluing of $g_{b_{1}}, \ldots, g_{b_{k}}$ to $\left(X, g_{\infty}\right)$ at the corresponding points $p_{1}, \ldots, p_{k}$ at the scales $t_{1}, \ldots, t_{k}$.

By iteration on $k$, we can then define approximate-Einstein-modulo-obstructions metrics $g_{t, v}^{A_{k}}$ and actual Einstein-modulo-obstructions metrics $\hat{g}_{t, v}^{k}$ on $Y_{k}$ as follows:

For $k=0, \quad$ we define $g_{t, v}^{D_{0}}=g_{t, v}^{A_{0}}=\hat{g}_{t, v}^{0}=\bar{g}_{v_{o}}$ and $\tilde{\mathfrak{O}}\left(g_{t, v}^{A_{0}}\right):=\mathfrak{O}\left(g_{\infty}\right)$.
Now let $0 \leqslant k \leqslant n-1$. The idea is to replace $\bar{g}_{v_{o}}$ by $\hat{g}_{t, v}^{k}$ and $\mathfrak{O}\left(g_{\infty}\right)$ by $\tilde{\mathfrak{D}}\left(g_{t, v}^{A_{k}}\right)$ and to perform the constructions as in Section 8.

We start with some $\hat{g}_{t, v}^{k}$ that in a neighborhood of $p_{k+1}$ satisfies
$$r\left(\hat{g}_{t, v}^{k}\right)-3 \hat{g}_{t, v}^{k}=w_{0}^{k}+w_{2}^{k}+\mathrm{O}\left(\varrho_{o}^{3}\right) \in \mathfrak{O}\left(g_{\infty}\right),$$
and has an expansion
$$\hat{g}_{t, v}^{k}=\boldsymbol{\delta}+\mathfrak{H}_{2}(k)+\mathfrak{H}_{3}(k)+\mathfrak{H}_{4}(k)+\mathrm{O}\left(\varrho^{5}\right),$$
exactly like (12). We can therefore define the approximate Einstein-moduloobstructions $g_{t, v}^{A_{k+1}}$ as in Section 8 as the desingularization of $\hat{g}_{t, v}^{k}$ at $p_{k+1}$ by $\bar{g}_{v_{b}}$ at scale $t_{k+1}$ replacing the $\mathfrak{H}_{i}$ by the present $\mathfrak{H}_{i}(k)$. Indeed, all of the steps of the construction are local and do not see the global properties of $g_{\infty}$, except the construction of $h^{4}$ in (21) with $\mho\left(g_{\infty}\right)$ by $\tilde{\mho}\left(g_{t, v}^{A_{k}}\right)$, which follows from the application of [43, Proposition 4.9] to $P_{g_{t, v}^{D_{k}}}\left(\Upsilon\left(\mathfrak{H}^{4}+\mathfrak{H}_{2}^{4}+\mathfrak{H}_{3}^{4}\right)\right)$, where $\Upsilon$ is a controlled cut-off function supported in a neighborhood of $p_{k+1}$.

We also extend the definition of $\tilde{\mathfrak{D}}\left(g_{t, v}^{A_{k+1}}\right)$ as in Definition 10: as the set of $\tilde{\mathbf{w}}+\tilde{\mathfrak{o}}$ for $(\mathbf{w}, \mathfrak{o}) \in \tilde{\mathfrak{D}}\left(g_{t, v}^{A_{k}}\right) \times \mathfrak{O}\left(\bar{g}_{v_{b}}\right)$, defined exactly as in Section 8 replacing $\bar{g}_{v_{o}}$ by $g_{t, v}^{A_{k}}$ and $\mathfrak{O}\left(g_{\infty}\right)$ by $\tilde{\mathfrak{O}}\left(g_{t, v}^{A_{k}}\right)$.

Now, by [43, Theorem 4.10], there exists a unique Einstein-modulo-obstructions metric $\hat{g}_{t, v}^{k+1}$ satisfying: for $(t, v)$ small enough,
\begin{itemize}
\item[-] $\left\|\hat{g}_{t, v}^{k+1}-g_{t, v}^{A_{k+1}}\right\|_{C_{\beta, *}^{2, \alpha}\left(g_{t}^{D_{k}}\right)} \rightarrow 0$ as $(t, v) \rightarrow 0$,
\item[-] $\hat{g}_{t, v}^{k+1}-g_{t, v}^{A_{k+1}} \perp_{g_{t, v}^{D_{k}}} \tilde{\mathfrak{D}}\left(g_{t, v}^{A_{k+1}}\right)$, and
\item[-] $\mathscr{F}_{g_{t}{ }^{D_{k+1}}}\left(\hat{g}_{t, v}^{k+1}\right) \in \tilde{\mathfrak{O}}\left(g_{t, v}^{A_{k+1}}\right)$.
\end{itemize}

\section*{Controlling the approximate desingularizations}

As in the proof of [43, (96), Proposition 5.13], the proof of Proposition 8.1, which is local in nature, extends to the case of partial desingularizations.

Proposition 9.1. Let $k \in\{1, \ldots, n\}$. We have the following controls:
\begin{itemize}
\item[(i)] $\left\|\mathscr{F}_{g_{t}{ }^{D_{k}}}\left(g_{t, v}^{A_{k}}\right)-\mho_{t, v}^{A_{k}}\right\|_{\varrho_{D}^{-2} C_{\beta}^{\alpha}\left(g_{t}^{D_{k}}\right)}=o\left(t_{k}\right)$, as $t_{k} \rightarrow 0$,
\item[(ii)] $\left\|\hat{g}_{t, v}^{k}-g_{t, v}^{A_{k}}\right\|_{C_{\beta, *}^{2, \alpha}\left(g_{t}^{D_{k}}\right)}=o\left(t_{k}\right)$, as $t_{k} \rightarrow 0$, and
\item[(iii)] at every point, the eigenvalues of the self-dual Weyl curvature of $\hat{g}_{t, v}^{k}$ are arbitrarily close to those of $g_{\infty}$ at some corresponding point of $X$.
\end{itemize}

Proof. We will prove this by induction on $k$. When $k=0$, one has $g_{t, v}^{D_{0}}=$ $g_{t, v}^{A_{0}}=\hat{g}_{t, v}^{0}=\bar{g}_{v_{o}}$ and the result is clear. Proceeding by induction, let us now assume that the Proposition holds for $0 \leqslant k \leqslant n-1$.

To prove (i), notice that the control of
$$\left\|\mathscr{F}_{g_{t}{ }^{D_{k+1}}}\left(g_{t, v}^{A_{k+1}}\right)-\mho_{t, v}^{A_{k+1}}\right\|_{\varrho_{D}^{-2} C_{\beta}^{2, \alpha}\left(g_{t}^{D_{k+1}}\right)}$$
is exactly as in the proof of (23), as the argument is local, and therefore also applies to partial desingularizations; cf. [43, Proposition 5.13].

To prove (ii), notice that, as in Section 8, we once again have
$$\left\|\hat{g}_{t, v}^{k+1}-g_{t, v}^{A_{k+1}}\right\|_{C_{\beta, *}^{2, \alpha}\left(g_{t, v}^{D_{k+1}}\right)} \leqslant C\left\|\mathscr{F}_{g_{t}^{D_{k+1}}}\left(g_{t, v}^{A_{k+1}}\right)-\mho_{t, v}^{A_{k+1}}\right\|_{\varrho_{D}^{-2} C_{\beta}^{\alpha}\left(g_{t, v}^{D_{k+1}}\right)}$$
for some $C>0$, where the right-hand side is $o\left(t_{k+1}\right)$ as $t_{k+1} \rightarrow 0$. Indeed, this follows from (i) and [43, (88), Proposition 5.11], the proof of which does not require the existence of an Einstein desingularization, but instead holds for any Einstein-modulo-obstructions metric.

Finally, to prove (iii), notice that the proof of Corollary 8.4 also works in our present setting, both at and away from the orbifold singularities. By the property for $k$, the metric $\hat{g}_{t, v}^{k}$, which plays the role of $\bar{g}_{v_{o}}$ in Section 8, has self-dual Weyl curvature with eigenvalues arbitrarily close to those of $\left(X, g_{\infty}\right)$ at some corresponding. An extension of the proof of Corollary 8.4, which is local in nature, then shows that the eigenvalues of $W^{+}\left(g_{t, v}^{A_{k+1}}\right)$ are arbitrarily close to those of $W^{+}\left(g_{\infty}\right)$ at an appropriate point. We then conclude, in exact analogy to (24), that
$$\begin{aligned}
\| \mathrm{W}^{+}\left(g_{t, v}^{A_{k+1}}\right) & -\mathrm{W}^{+}\left(\hat{g}_{t, v}^{k+1}\right) \|_{C^{0}\left(g_{t}^{D k+1}\right)} \\
& \leqslant C t^{-1}\left\|\mathrm{~W}^{+}\left(g_{t, v}^{A_{k+1}}\right)-\mathrm{W}^{+}\left(\hat{g}_{t, v}^{k+1}\right)\right\|_{\varrho_{D}^{-2} C_{\beta}^{\alpha}\left(g_{t}^{D k+1}\right)}
\end{aligned}$$
where the right-hand side tends to zero as $(t, v) \rightarrow 0$. \(\square\)

\section*{Conclusion of the proof}

Bringing these ideas together, let us now assume
\begin{itemize}
\item[-] that $X^{4}$ is an orbifold with $n$ isolated singularities $p_{1}, \ldots, p_{n}$;
\item[-] that $\left(X^{4}, g_{\infty}\right)$ is Hermitian and Einstein, with $\lambda>0$;
\item[-] that there is an admissible sequence $\left(M, g_{i}\right)$ with
$$d_{G H}\left(\left(M, g_{i}\right),\left(X, g_{\infty}\right)\right) \rightarrow 0 ; \quad \text { and }$$
\item[-] that no trees of singularities arise in this limiting process.
\end{itemize}

By [43], then, up to taking a subsequence, for $i$ large enough, there exist $t_{i}>0$, along with naïve desingularizations $g_{t_{i}}^{D}$ and parameters
$$v_{i} \in \mathfrak{O}\left(g_{b_{1}}\right) \times \ldots \times \mathfrak{O}\left(g_{b_{n}}\right) \times \mathfrak{O}\left(g_{\infty}\right)$$
for which
\begin{itemize}
\item[-] $\left\|g_{i}-g_{t_{i}, v_{i}}^{A_{n}}\right\|_{C_{\beta, *}^{2, \alpha}\left(g_{t_{i}}^{D}\right)} \rightarrow 0$, and
\item[-] $g_{i}-g_{t_{i}, v_{i}}^{A_{n}} \perp_{g_{t_{i}}^{D}} \tilde{\mathfrak{O}}\left(g_{t_{i}, v_{i}}^{A_{n}}\right)$.
\end{itemize}

Since our assumptions in particular imply that $M$ has the expected topology, and all of the Ricci-flat ALE spaces arising from curvature concentration are Kähler, our assumption that no trees of singularities arise then implies [43, §7.1] that, after passing to a subsequence and up to a diffeomorphism, $g_{i}=\hat{g}_{t_{i}, v_{i}}^{n}$ for one of the above $\hat{g}_{t_{i}, v_{i}}^{n}$. In particular, $g_{i}$ is an Einstein metric satisfying Wu's criterion $\operatorname{det} \mathrm{W}^{+}\left(g_{i}\right)>0$, and it therefore follows [34, 46] that, for $i$ large enough, the $g_{i}$ are necessarily conformally Kähler. However, as previously noted, such metrics on a smooth 4-manifold $M$ are actually Kähler-Einstein unless [31] there is, up to isometries and rescalings, only one conformally-Kähler Einstein manifold on $M$. Theorems A and B thus now follow in the case where no trees of singularities arise. \(\square\)

Combining this with Proposition 4.3 now yields the following application:
Corollary 9.2. Let $\left(X^{4}, g_{\infty}\right)$ be a Kähler-Einstein orbifold with at least one singular point. If $c_{1}^{2}(X) \geq 4$, and if ( $X, g_{\infty}$ ) is the Gromov-Hausdorff limit of an admissible sequence $\left(M, g_{i}\right)$ of smooth $\lambda>0$ Einstein 4-manifolds, then $c_{1}^{2}(X)=4$, and $M \approx \mathbb{C P}_{2} \# 5 \overline{\mathbb{C P}}_{2}$.

Proof. When $c_{1}^{2}(X) \geq 4$ and $\left(X, g_{\infty}\right)$ is Kähler-Einstein, Proposition 4.3 tells us that each singularity of $X$ is modeled on $\mathbb{C}^{2} / \mathbb{Z}_{2}$, and this in particular excludes the formation of bubble-trees. The above argument therefore shows that the Einstein 4-manifolds $\left(M, g_{i}\right)$ must be Hermitian for all sufficiently large $i$. However, classification [31] tells us that, up to isometry and rescalings, there is at most one $\lambda>0$ Hermitian, Einstein metric on the underlying smooth 4-manifold $M$ of a complex surface with $c_{1}^{2} \geq 5$. When $c_{1}^{2}(X) \geq 4$, singularities can therefore only form in the limit when $c_{1}^{2}(M)=c_{1}^{2}(X)=4$ and $M$ is diffeomorphic to $\mathbb{C P}_{2} \# 5 \overline{\mathbb{C P}}_{2}$. \(\square\)

\section*{10 The General Case}

Finally, we deal with trees of singularities by further refining our notion of approximate Einstein-modulo-obstructions metric. In fact, our proof of Proposition 2.2 already depended on the reason why it is possible to handle trees of Ricci-flat Kähler ALE metrics: when glued together in the expected
manner, they can always be approximated by a single Ricci-flat Kähler ALE metric [43]. The essence of what we will now do amounts to a controlled, quantitative implementation of this observation. While there are more elementary ways of carrying this out for the Gibbons-Hawking gravitational instantons, our proof will be geared to handle the general case.

\section*{Asymptotics of the building blocks}

We will now consider:
\begin{itemize}
\item[-] $\left(N_{1}, \bar{g}_{v_{b_{1}}}\right)$ a Ricci-flat ALE orbifold with a singularity at $p_{1}$, and
\item[-] $\left(N_{2}, \bar{g}_{v_{b_{2}}}\right)$ glued at scale $t_{2}$ at a remaining singular point $p_{1}$ of $\left(N_{1}, \bar{g}_{v_{b_{1}}}\right)$.
\end{itemize}

We have the following expansions of the different metrics: for any $l \leqslant 4$,
\begin{itemize}
\item[-] at its singular point $p_{1}: \bar{g}_{v_{b_{1}}}=\boldsymbol{\delta}+\mathfrak{H}_{2}+\mathfrak{H}_{3}+\mathfrak{H}_{4}+\ldots+\mathfrak{H}_{l}+\mathrm{O}\left(\rho_{b_{1}}^{l+1}\right)$
\item[-] at its infinity: $\bar{g}_{v_{b_{2}}}=\boldsymbol{\delta}+\mathfrak{H}^{4}+\ldots+\mathfrak{H}^{l}+\mathrm{O}\left(\rho_{b_{2}}^{l+1}\right)$.
\end{itemize}
In particular, developing the equations $\mathscr{F}_{\boldsymbol{\delta}}\left(g_{b_{1}}\right)=0$ and $\mathscr{F}_{\boldsymbol{\delta}}\left(g_{b_{2}}\right)=0$ according to powers of $r_{b_{1}}$ and $r_{b_{2}}$ the above tensors satisfy equalities:
\begin{itemize}
\item[-] $P_{\boldsymbol{\delta}} \mathfrak{H}_{i}+Q_{\boldsymbol{\delta}}^{[i],+}\left(\mathfrak{H}_{2}, \mathfrak{H}_{3}, \ldots, \mathfrak{H}_{i-1}\right)=0$, and
\item[-] $P_{\boldsymbol{\delta}} \mathfrak{H}^{j}+Q_{\boldsymbol{\delta}}^{[j],-}\left(\mathfrak{H}^{4}, \mathfrak{H}^{5}, \ldots, \mathfrak{H}^{j-1}\right)=0$,
\end{itemize}
where $Q_{\delta}^{[j], \pm}$ are specific finite sums of multilinear operations on the tensors and their two first derivatives. The key point is that $Q_{\delta}^{[i],+}\left(\mathfrak{H}_{2}, \mathfrak{H}_{3}, \ldots, \mathfrak{H}_{i-1}\right)=$ $\mathrm{O}\left(\varrho^{i-2}\right)$, and $Q_{\boldsymbol{\delta}}^{[j],-}\left(\mathfrak{H}^{4}, \mathfrak{H}^{5}, \ldots, \mathfrak{H}^{j-1}\right)=\mathrm{O}\left(\varrho^{-j-2}\right)$.

\section*{Approximations of Ricci-flat Kähler metrics}

When $v_{b}=\left(v_{b_{1}}, t_{2}, v_{b_{2}}\right)$ is sufficiently small, we will use $g_{v_{b}}^{B}$ to denote the naïve gluing $\bar{g}_{v_{1}} \#_{p_{1}, t_{2}} \bar{g}_{v_{b_{2}}}$ and let $\varrho_{b}$ be the associated extension of $\varrho_{D}$ of Definition 7. By [43, Section 6.2], there is a unique Ricci-flat Kähler ALE metric $\bar{g}_{v_{b}}$ that, for some $\epsilon>0$, satisfies
\begin{itemize}
\item[1.] $\mathscr{F}_{g_{v_{b}}^{B}}\left(\bar{g}_{v_{b}}\right)=0$,
\item[2.] $\left\|\bar{g}_{v_{b}}-g_{v_{b}}^{B}\right\|_{C_{\beta, * *}^{2, \alpha}} \leqslant \epsilon$, and
\end{itemize}
3. $\bar{g}_{v_{b}}-g_{v_{b}}^{B} \perp_{L^{2}\left(g_{b}\right)} \tilde{\mathfrak{D}}\left(g_{v_{b}}^{B}\right)$,
where $C_{\beta, * *}^{2, \alpha}\left(g_{v_{b}}^{B}\right)$ is defined in Definition 16 below. We emphasize that this construction reaches all nearby Ricci-flat ALE metrics.

The results of [43, Section 6.2] tell us that any Einstein-modulo-obstructions perturbation of a tree of Ricci-flat Kähler ALE metrics is in fact a Ricci-flat Kähler ALE metric. For any $l \in \mathbb{N}$, this metric can then be approximated by a naïve gluing:
$$g_{v_{b}}^{B,[l]}:=\left(\bar{g}_{v_{b_{1}}}+\sum_{j=4}^{l} t_{2}^{\frac{j}{2}} h^{j}\right) \#_{p_{1}, t_{2}}\left(\bar{g}_{v_{b_{2}}}+\sum_{i=2}^{l} t_{2}^{\frac{i}{2}} h_{i}\right),$$
where for $i, j \leqslant 4$, one defines the $h_{i}$ and $h^{j}$ as in (18), (19), (21) where all of the obstructions $\mho_{i}$ and $\mathbf{w}^{4}$ vanish. Following (22), we now solve iteratively for $i, j \geqslant 4$ by applying the following two steps:
1. first, solve the system
$$\begin{aligned}
& P_{\bar{g}_{v_{b_{1}}}} h^{j}=-Q_{\bar{g}_{v_{b_{1}}}}^{[j],-}\left(h^{4}, \ldots, h^{j-1}\right) \\
& \quad h^{j}=\sum_{i \leqslant j-1} \mathfrak{H}_{i}^{j}+\mathfrak{H}_{j}^{j}+\mathrm{O}\left(\varrho^{-1-\epsilon}\right), \quad \forall \epsilon>0 \\
& \int_{\Sigma}\left\langle h^{j}, \mho_{v_{b_{1}}}\right\rangle_{\bar{g}_{v_{b_{1}}}} d a_{\left(\bar{g}_{v_{b_{1}} \mid \Sigma}\right)}=0 \quad \forall \mho_{v_{b_{1}}} \in \mathfrak{O}\left(\bar{g}_{v_{b_{1}}}\right)
\end{aligned}$$
where $Q_{\bar{g}_{v_{1}}}^{[j],-}$ involves the nonlinear terms in $h^{l}$ for $l \leqslant j-1$ appearing when solving $\mathscr{F}_{\bar{g}_{b_{1}}}(g)=0$, and where the $\mathfrak{H}_{i}^{j}$ for $i \leqslant j-1$ are determined by the previously defined $h_{i}$. In order to solve this equation, notice that for $\tilde{\Upsilon}$ a cut-off function supported in a neighborhood of $p_{1}$
$$P_{\bar{g}_{v_{b_{1}}}}\left(\tilde{\Upsilon} \sum_{i \leqslant j-1} \mathfrak{H}_{i}^{j}\right)-Q_{\bar{g}_{v_{b_{1}}}^{[j],-}}\left(h^{4}, \ldots, h^{j-1}\right)=\mathrm{O}\left(r_{b_{1}}^{-2-\epsilon}\right), \quad \forall \epsilon>0,$$
hence, by [40, Lemma 4.42], one can find $h^{\prime}$ such that
$$P_{\bar{g}_{v_{b_{1}}}}\left(h^{\prime}+\tilde{\Upsilon} \sum_{i \leqslant j-1} \mathfrak{H}_{i}^{j}\right)-Q_{\bar{g}_{v_{b_{1}}}^{[j],-}}\left(h^{4}, \ldots, h^{j-1}\right) \in \mathfrak{O}\left(\bar{g}_{v_{b_{1}}}\right) .$$

Since the gluing is unobstructed by [43, Section 6.2], one then shows iteratively that the element of $\mathfrak{O}\left(\bar{g}_{v_{b_{1}}}\right)$ vanishes, and $h^{\prime}=\mathfrak{H}_{j}^{j}+\mathrm{O}\left(\varrho^{-1-\epsilon}\right)$ for $\mathfrak{H}_{j}^{j}=\mathrm{O}\left(\varrho^{-\epsilon}\right)$ for all $\epsilon>0$, and in fact, for any $L \geqslant 2$ and $\epsilon>0$, there is a neighborhood of infinity where
$$h^{\prime}=\mathfrak{H}_{j}^{j}+\sum_{l=j+1}^{L} \mathfrak{H}_{l}^{j}+\mathrm{O}\left(\varrho_{o}^{L-j-\epsilon}\right),$$
2. then, one similarly solves the equation
$$\begin{aligned}
& P_{\bar{g}_{v_{b}}} h_{j}=-Q \bar{g}_{v_{b_{2}}}^{[j],+}\left(h_{2}, \ldots, h_{j-1}\right) \\
& \quad h_{j}=\sum_{i \leqslant j} \mathfrak{H}_{j}^{i}+\mathfrak{H}_{j}^{j+1}+\mathrm{O}\left(\varrho^{-2+\epsilon}\right), \quad \forall \epsilon>0 \\
& \quad \int_{\Sigma}\left\langle h_{j}, \mho_{v_{b_{2}}}\right\rangle_{\bar{g}_{v_{b_{2}}}} d a_{\left(\bar{g}_{v_{b_{2}} \mid \Sigma}\right)}=0 \text { for all } \mho_{v_{b_{2}}} \in \mathfrak{O}\left(\bar{g}_{v_{b_{2}}}\right)
\end{aligned}$$
where $Q_{\bar{g}_{v_{2}}}^{[j],+}$ involves the nonlinear terms in $h^{l}$ for $l \leqslant j$ appearing when solving $\mathscr{F}_{\bar{g}_{v_{2}}}(g)=0$, and where the $\mathfrak{H}_{j}^{i}$ for $i \leqslant j$ are determined by the previous $h^{l}$ defined. One then obtains $\mathfrak{H}_{j}^{j+1}$ determined from the unique solution of (29) such that in a neighborhood of infinity, for all $L \geqslant 4$, and $\epsilon>0 h_{j}=\sum_{l=4}^{L} \mathfrak{H}_{j}^{l}+\mathrm{O}\left(\varrho_{b}^{j-L+\epsilon}\right)$.

The point is that there are no obstructions [43, Section 6.2] which lets us estimate the metrics directly without having to approximate obstructions. Explicit computations generalizing slightly those of Proposition 23 (see also [41, Sections 2 and 3]) lead to the following result.

Proposition 10.1. For any $l \geqslant 4$ and $0<\alpha<1$ and $0<\beta<\frac{1}{4}$, there is $C>0$ independent of $v_{b}$ so that we have the control
$$\left\|\left(1+\varrho_{b}\right)^{4} \mathscr{F}_{g_{v_{b}}^{B}}\left(g_{v_{b}}^{B,[l]}\right)\right\|_{\varrho_{b}^{-2} C_{\beta}^{\alpha}\left(g_{v_{b}}^{B}\right)} \leqslant C t_{2}^{\frac{l+1-\beta}{4}}=o\left(t_{2}^{\frac{l}{4}}\right)$$
and consequently, by [40, (5.15), Lemma 5.19], we therefore have
$$\left\|\bar{g}_{v_{b}}-g_{v_{b}}^{B,[l]}\right\|_{C_{\beta, * *}^{2, \alpha}\left(g_{v_{b}}^{B}\right)} \leqslant C^{\prime} t_{2}^{\frac{l+1-\beta}{4}}=o\left(t_{2}^{\frac{l}{4}}\right)$$
for some $C^{\prime}>0$ independent of $v_{b}$,

In particular, considering $l \geqslant 9$ for $g_{b}$, we have the following controls.
Corollary 10.2. We have the following more concrete controls on $\bar{g}_{v_{b}}$ :
\begin{itemize}
\item[1.] in the region $\sqrt{t_{2}} \ll r_{b_{1}}$, or $1 \ll r_{b_{2}}$, and so in particular at infinity,
$$\bar{g}_{v_{b}}=\bar{g}_{v_{b_{1}}}+t_{2}^{2} h^{4}+o\left(t_{2}^{2} r_{b_{1}}^{-4}\right)$$
\item[2.] in the region $r_{b_{1}} \ll 1$, or $r_{b_{2}} \ll t_{2}^{-\frac{1}{2}}$
$$\bar{g}_{v_{b}}=t_{2}\left(\bar{g}_{v_{b_{1}}}+t_{2} h_{2}+t_{2}^{\frac{3}{2}} h_{3}+t_{2}^{2} h_{4}\right)+o\left(t_{2}^{2} r_{b_{2}}^{4}\right)$$
\item[3.] in the gluing region $\sqrt{t_{2}} \ll r_{b_{1}} \ll 1$ or $1 \ll r_{b_{2}} \ll t_{2}^{-\frac{1}{2}}$, we have
$$\bar{g}_{v_{b}}=\boldsymbol{\delta}+\mathfrak{H}_{2}+\mathfrak{H}_{3}+\mathfrak{H}^{4}+\mathfrak{H}_{2}^{4}+\mathfrak{H}_{3}^{4}+\mathfrak{H}_{4}^{4}+\mathfrak{H}_{4}+\mathrm{O}\left(r_{b_{1}}^{5}+r_{b_{2}}^{-5}\right) .$$
\end{itemize}

We finish this section by an estimate of the variations at infinity of a tree of singularities with respect to the size of the bubbles attached to it.
\begin{itemize}
\item[-] for $l \in\{0, \ldots, k+1\}$, Ricci-flat Kähler $g_{b_{l}}$ that can be glued as a tree of singularities according to [43, Section 4.3]
\item[-] $g^{B_{k+1}}$ (resp. $g^{B_{k}}$ ), the naïve gluing of the $g_{b_{l}}$ at scales $T_{l}=t_{0} \ldots t_{l}>0$ for small enough $t_{l}>0$ as a tree for $l \in\{0, \ldots, k+1\}$ (resp. $l \in\{0, \ldots, k\}$ ),
\item[-] $\bar{g}_{B_{k+1}}$ (resp. $\bar{g}_{B_{k}}$ ) the Ricci-flat Kähler ALE perturbation of $g^{B_{k+1}}$ (resp. $\left.g^{B_{k}}\right)$,
\end{itemize}

Proposition 10.3. For any $r_{B_{k}} \gg \sqrt{T_{k+1}}$, we have, for any $l \in \mathbf{N}$, and $C_{l}>0$ depending only on $l$,
$$\varrho_{B_{k}}^{l}\left|\nabla^{l}\left(\bar{g}_{B_{k}}-\bar{g}_{B_{k+1}}\right)\right| \leqslant C_{l} T_{k+1}^{2} r_{B_{k}}^{-4} .$$

More precisely, there is a converging expansion
$$\bar{g}_{B_{k}}-\bar{g}_{B_{k+1}}=\sum_{j \geqslant 4} \mathfrak{K}^{j},$$
with $\left|\mathfrak{K}^{j}\right| \leqslant C_{j}^{\prime} T_{k+1}^{2} \varrho^{-j}$ for $C_{j}^{\prime}>0$ independent of $T_{k+1}$ or $r_{B_{k}}$.
Sketch of proof. The result can be easily obtained for the Ricci-flat Kähler ALE metrics asymptotic to $\mathbb{R}^{4} / \Gamma$ for $\Gamma \subset \operatorname{SU}(2)$ cyclic. Indeed, they are Gibbons-Hawking's gravitational instantons which are explicitly given in coordinates [20].

For the general case, one can combine the resolution of singularities described in [27, Proposition 3.10] together with the description of the asymptotic expansion of the [27, Proposition 3.14] (see also [4, Theorem 2.1]). \(\square\)

\section*{Approximate metrics with trees of singularities}

We now explain how to deal with trees of singularities.

\section*{Setting up the iterative construction}

In this section, we consider $\left(X, g_{\infty}\right)$, a conformally Kähler Einstein orbifold with scalar curvature 12 with multiple singularities of general type. We then consider a naïve desingularization of $\left(X, g_{\infty}\right)$ at all of its singularities by trees of singularities which we will denote $g_{t, v}^{D}$.

We will order our desingularizations according to their depth, that is the size of the bubbles glued.
\begin{itemize}
\item[1.] we start with $g_{t, v}^{D_{0}}:=g_{t, v}^{A_{0}}:=\hat{g}_{t, v}^{0}:=\bar{g}_{v_{o}}$ as before, and
\item[2.] given $g_{t, v}^{D_{k}}$, and the next largest scale $T_{k+1}$ at which to glue a Ricci-flat ALE metric $\bar{g}_{v_{k+1}}$ to a remaining singular point $p_{k+1}$,
$$g_{t, v}^{D_{k+1}}:=g_{t, v}^{D_{k}} \#_{p_{k+1}, T_{k}^{2} t_{k+1}} \bar{g}_{v_{k+1}} .$$
\end{itemize}

The rest of the argument mainly consists in carefully constructing approximations $g_{t, v}^{A_{k}}$ in order to control the Einstein-modulo-obstructions metrics $\hat{g}_{t, v}^{k}$ and their curvature. We will eventually reach the total Einstein-moduloobstructions desingularization and be able to control its curvature.

Proposition 10.4. For each $k \in\{1, \ldots, n\}$, we have:
\begin{itemize}
\item[1.] at every point, the eignenvalues of the self-dual curvature $W^{+}$of $\hat{g}_{t, v}^{k}$ differ form the eigenvalues of $W^{+}\left(g_{\infty}\right)$, at a suitable point of $X$, by only an error that uniformly tends to zero as $(t, v) \rightarrow(0,0)$;
\item[2.] $\left\|\hat{g}_{t, v}^{k}-g^{A_{k}}\right\|_{C_{\beta, *}^{2, \alpha}}=o\left(T_{k}\right)$, and there is $C>0$ such that for any $l \in$ $\{0,1,2,3\}$; and
$$\left|\nabla^{l}\left(\hat{g}_{t, v}^{k}-g^{D_{k}}\right)\right| \leqslant C r_{D_{k}}^{2} .$$
\end{itemize}

\section*{The iterative step}

If we have previously defined $g_{t, v}^{D_{k}}, g_{t, v}^{A_{k}}$ and $\hat{g}_{t, v}^{k}$, and $\tilde{\mathfrak{O}}\left(g_{t, v}^{A_{k}}\right)$ in a suitable manner, we may then define $g_{t, v}^{A_{k+1}}$ so as to control $\hat{g}_{t, v}^{k+1}$.

If the next considered singular point $p_{k+1}$ is a singular point of $X$, then we define $g_{t, v}^{A_{k+1}}$ and obtain a control of $\hat{g}_{t, v}^{k+1}$ and its curvature exactly as in Section 9. Here, we will therefore consider the remaining case where the singular point $p_{k+1}$ belongs to another Ricci-flat ALE metric of the tree of singularities.

Note. In order to simplify our notation in the remainder of the argument, we will drop (when not necessary) the $(t, v)$-dependence of our tensors and in particular denote $g_{b_{i}}$ for $\bar{g}_{v_{b_{i}}}$. \(\square\)

Assume that:
\begin{itemize}
\item[-] $g^{D_{k}}$ and $\hat{g}^{k}$ defined from the previous steps, satisfy:
$$\mathscr{F}_{g^{D_{k}}}\left(\hat{g}^{k}\right)=\mathfrak{w}_{0}+\mathfrak{w}_{2}+\mathrm{O}\left(T_{k} r_{b_{k}}^{3}\right) \in \tilde{\mathfrak{O}}\left(g^{A_{k}}\right),$$
with $\left|\mathfrak{w}_{l}\right| \leqslant C_{l} T_{k} r_{b_{k}}^{l}$ for $C_{l}>0$,
\item[-] $g^{D_{k+1}}=g^{D_{k}} \#_{p_{k+1}, T_{k}^{2} t_{k+1}} g_{b_{k+1}}$ where $g_{b_{k+1}}$ is a Ricci-flat ALE metric with a remaining singular point $p_{1}$, and
\item[-] $\hat{g}^{k+1}$ the Einstein-modulo-obstructions perturbation of $g^{D_{k+1}}=g_{t, v}^{D_{k+1}}$ transversely to $\tilde{\mathfrak{D}}\left(g^{A_{k}}\right)$.
\end{itemize}
Our goal will now be to obtain curvature estimates for $\hat{g}^{k+1}$ using the construction of an approximate Einstein-modulo-obstructions metric. We will in particular show that the above properties stay true by iteration.

For this we will also use the following metrics.
\begin{itemize}
\item[-] $g^{B_{k+1}}$, the naïve gluing of the tree of singularity at which $g_{b_{k+1}}$ is glued in $g^{D_{k+1}}$,
\item[-] $g^{B_{k}}$, the naïve gluing of the tree of singularity at which $g_{b_{k+1}}$ is glued in $g^{D_{k+1}}$, but without $g_{b_{k+1}}$, and
\item[-] $\bar{g}_{B_{k+1}}$ (resp. $\bar{g}_{B_{k}}$ ) the Ricci-flat Kähler ALE perturbation of $g^{B_{k+1}}$ (resp. $g^{B_{k}}$ ).
\end{itemize}

The rest of the section consists in constructing a suitable approximate Einstein-modulo-obstructions metric $g^{A_{k+1}}$ controlling $\hat{g}^{k+1}$ in $o\left(T_{k+1}\right)$ in order to compensate the $\varrho_{D}^{-2}$ term of our function space. For this, we will
leverage the fact that both $\hat{g}^{k}$ and $\bar{g}_{B_{k}}$ satisfy exact equations in order to rule out errors in powers of $T_{k}$ alone or in powers of $t_{k+1}$ alone. The following key technical lemma follows from the expansion of Ricci curvature at a metric $g$ in the (small) direction $h$ :
$$r(g+h)=r(g)+(g+h)^{-1} * \mathcal{R}(g)+(g+h)^{-2} * \nabla^{2} h+(g+h)^{-3} * \nabla h * \nabla h,$$
where $*$ corresponds to contractions of tensors.
Lemma 10.5. Let $g$ be an Einstein metric on an open set $U \subset \mathbb{R}^{4}$ such that $\left|\nabla_{\boldsymbol{\delta}}^{l}(g-\boldsymbol{\delta})\right|_{\boldsymbol{\delta}}<\frac{1}{100}$ for $l \leqslant L$. Assume that there exist 2-tensors $h_{1}$ and $h_{2}$ small enough in $C^{L}(U, \boldsymbol{\delta})$ such that $\mathscr{F}_{g}\left(g+h_{i}\right)=w_{i}$ for $i \in\{1,2\}$.

Then, we have the following control: there exists a $C_{L}>0$, independent of $g, h_{1}$, and $h_{2}$, such that, for $l \in\{0, \ldots$,$\} ,$
$$\left|\nabla_{g}^{l}\left(\mathscr{F}_{g}\left(g+h_{1}+h_{2}\right)-w_{1}-w_{2}\right)\right|_{g} \leqslant C_{L} \sum_{l_{1}+l_{2}=l o r(l+2)}\left|\nabla_{g}^{l_{1}} h_{1}\right|\left|\nabla_{g}^{l_{2}} h_{2}\right| .$$

Remark. The assumption on $g$ always holds in suitably rescaled harmonic coordinates, whether our space is a manifold or an orbifold; cf. e.g. [24]. ◇

Near the singular point $p_{k+1}$, we have the following expansions of the relevant metrics:
$$\begin{gathered}
\bar{g}_{B_{k}}=\boldsymbol{\delta}+\mathfrak{H}_{2}+\mathfrak{H}_{3}+\mathfrak{H}_{4}+\mathrm{O}\left(r_{b_{1}}^{5}\right) \\
T_{k}^{-1} \hat{g}^{k}=\bar{g}_{B_{k}}+\mathfrak{K}_{0}+\mathfrak{K}_{2}+\mathfrak{K}_{3}+\mathfrak{K}_{4}+\mathrm{O}\left(T_{k} r_{B_{k}}^{5}\right),
\end{gathered}$$
where $\left|\mathfrak{K}_{i}\right| \leqslant T_{k} r_{B_{k}}^{i}$. In particular, by the equation satisfied by $\hat{g}_{t, v}^{k}$ and (32), the above tensors satisfy the following equalities:
\begin{itemize}
\item[-] $P_{\delta} \mathfrak{K}_{0}=0$
\item[-] $P_{\boldsymbol{\delta}} \mathfrak{K}_{2}+Q_{\boldsymbol{\delta}}\left(\mathfrak{K}_{0}, \mathfrak{H}_{2}\right)=\Lambda\left(\boldsymbol{\delta}+\mathfrak{K}_{0}\right)+\mathfrak{w}_{0}$,
\item[-] $P_{\delta} \mathfrak{K}_{3}+Q_{\delta}\left(\mathfrak{K}_{0}, \mathfrak{H}_{3}\right)=0$,
\item[-] $P_{\boldsymbol{\delta}} \mathfrak{K}_{4}+Q_{\boldsymbol{\delta}}\left(\mathfrak{K}_{0}, \mathfrak{H}_{4}\right)+Q_{\boldsymbol{\delta}}\left(\mathfrak{H}_{2}, \mathfrak{K}_{2}\right)+Q_{\boldsymbol{\delta}}\left(\mathfrak{K}_{0}, \mathfrak{H}_{2}, \mathfrak{H}_{2}\right)+Q_{\boldsymbol{\delta}}\left(\mathfrak{K}_{0}, \mathfrak{K}_{2}, \mathfrak{H}_{2}\right)+$ $Q_{\boldsymbol{\delta}}\left(\mathfrak{K}_{0}, \mathfrak{K}_{2}, \mathfrak{K}_{2}\right)=\Lambda\left(\mathfrak{H}_{2}+\mathfrak{K}_{2}\right)+\mathfrak{w}_{2}$.
\end{itemize}

Extending the results of Section 8, we define the following tensors extending the above ones: given the $h_{i}$ of (29), and $w_{0}$ and $w_{2}$ extensions of $\mathfrak{w}_{0}$ and $\mathfrak{w}_{2}$ of (32) as in Section 8,
\begin{itemize}
\item[-] $P_{\bar{g}_{v_{2}}} k_{0}=0$
\item[-] $P_{\bar{g}_{v_{2}}} k_{2}+Q_{\bar{g}_{v_{2}}}\left(k_{0}, h_{2}\right)-\Lambda\left(\bar{g}_{v_{b_{2}}}+k_{0}\right)-w_{0}=\mho_{2} \in \mathfrak{O}\left(\bar{g}_{v_{b_{2}}}\right)$,
\item[-] $P_{\bar{g}_{v_{2}}} k_{3}+Q_{\bar{g}_{v_{2}}}\left(k_{0}, h_{3}\right)=0$,
\item[-] $P_{\bar{g}_{v_{2}}} k_{4}+Q_{\bar{g}_{v_{2}}}\left(k_{0}, h_{4}\right)+Q_{\bar{g}_{v_{b_{2}}}}\left(h_{2}, h_{2}\right)+Q_{\bar{g}_{v_{b_{2}}}}\left(k_{0}, h_{2}, h_{2}\right)+Q_{\bar{g}_{v_{2}}}\left(k_{0}, k_{2}, h_{2}\right)+$ $Q_{\bar{g}_{v_{b_{2}}}}\left(k_{0}, k_{2}, k_{2}\right)-\Lambda\left(h_{2}+k_{2}\right)-w_{2}=\mho_{4} \in \mathfrak{O}\left(\bar{g}_{v_{b_{2}}}\right)$.
\end{itemize}

Define $\Upsilon_{t}$ to be a cut-off function supported on $r_{D_{k}}<2 t_{k_{0}}^{\frac{1}{4}}$ and equal to 1 on $r_{D_{k}}<t_{k_{0}}^{\frac{1}{4}}$ satisfying for some $C_{l}$ independent of $t$, or $r_{D_{k}}$,
$$\nabla_{g_{k}^{D}}^{l} \Upsilon_{t} \leqslant C_{l} r_{D_{k}}^{l} .$$
Next, define an approximate Einstein-modulo-obstructions metric as:
$g^{A_{k+1}}:=\left(\hat{g}^{k}+\Upsilon_{t}\left(\bar{g}_{B_{k+1}}-\bar{g}_{B_{k}}\right)\right) \widetilde{\#}_{p_{k+1}, T_{k}, t_{k+1}}\left(T_{k+1}^{-1} \bar{g}_{B_{k+1}}+k_{0}+t_{k+1} k_{2}+t_{k+1}^{3 / 2} k_{3}+t_{k+1}^{2} k_{4}\right)$,
where $\widetilde{\#}$ is essentially the same operation introduced in Definition 6, but with the gluing scale $t^{\frac{1}{4}}$ replaced by $T_{k}^{\frac{1}{2}} t_{k+1}^{\frac{2}{9}}$. Finally, define the obstruction space $\tilde{\mathfrak{O}}\left(g^{A_{k+1}}\right)$ as the set of $\tilde{\mathfrak{o}}+\tilde{\mathbf{w}}$ for $\mathfrak{o} \in \mathfrak{O}\left(g_{b_{k+1}}\right)$ and $\mathbf{w} \in \tilde{\mathfrak{D}}\left(g^{A_{k}}\right)$, where $\tilde{\mathfrak{O}}$ and $\tilde{\mathbf{w}}$ are defined as in Definition 9 We also extend the definition of $\tilde{\mathfrak{O}}\left(g_{t, v}^{A_{k+1}}\right)$ exactly as in Section 8 replacing $\bar{g}_{v_{o}}$ by $g_{t, v}^{A_{k}}$ and $\mathfrak{O}\left(g_{\infty}\right)$ by $\tilde{\mathfrak{O}}\left(g_{t, v}^{A_{k}}\right)$.

\section*{Approximate metrics with trees of singularities}

We now control how close we are to the actual Einstein-modulo-obstructions metric. This proves the last point of Proposition 10.4.

Proposition 10.6. We have the following control:
$$\left\|\mathscr{F}_{g^{D_{k+1}}}\left(g^{A_{k+1}}\right)-\mho^{A_{k+1}}\right\|_{\varrho_{D}^{-2} C_{\beta}^{\alpha}\left(g^{D_{k+1}}\right)} \leqslant o\left(T_{k+1}\right) .$$
Thus, by [43, Proposition 5.11], we have $\left\|\hat{g}_{t, v}^{k+1}-g^{A_{k+1}}\right\|_{C_{\beta, *}^{2, \alpha}\left(g^{D_{k+1}}\right)}=o\left(T_{k+1}\right)$. In particular, since $r_{D_{k+1}} \geqslant T_{k+1}$ there is $C>0$ such that for any $l \in$ \{0, 1, 2, 3\},
$$\left|\nabla^{l}\left(\hat{g}_{t, v}^{k+1}-g^{D_{k+1}}\right)\right|_{g^{D_{k+1}}} \leqslant C r_{D_{k+1}}^{2} .$$

Proof. There are three regions to consider, and we will control our operator on each of them.
\begin{itemize}
\item[1.] In the region where we have $g^{A_{k+1}}=\hat{g}^{k}+\Upsilon_{t}\left(\bar{g}_{B_{k+1}}-\bar{g}_{B_{k}}\right)$, thanks to the local controls of Lemma 10.5 applied to $g$ (30) and (31) we find:
$$r_{D_{k}}^{2+l}\left|\nabla_{g_{k}^{D}}^{l}\left(\mathscr{F}_{g^{D_{k}}}\left(g^{A_{k+1}}\right)-\mho^{A_{k+1}}\right)\right|_{g^{D_{k}}}=\mathrm{O}\left(T_{k+1}^{2} r_{D_{k}}^{-4} r_{D_{k}}^{2}\right) .$$
\item[2.] In the region $t_{k_{0}}^{\frac{1}{4}}<r_{D_{k}}<2 t_{k_{0}}^{\frac{1}{4}}$, thanks to (30) and the controls (33) of the cut-off function, we find:
$$r_{D_{k}}^{2+l}\left|\nabla_{g_{k}^{D}}^{l}\left(\mathscr{F}_{g^{D_{k}}}\left(g^{A_{k+1}}\right)-\mho^{A_{k+1}}\right)\right|_{g^{D_{k}}}=\mathrm{O}\left(T_{k+1}^{2} r_{D_{k}}^{-4}\right)=\mathrm{O}\left(T_{k+1}^{2} t_{k_{0}}\right)=o\left(T_{k+1}\right) .$$
\item[3.] Since $T_{k+1}^{-1} g_{t, v}^{A}=T_{k+1}^{-1} \bar{g}_{B_{k+1}}+k_{0}+t_{k+1} k_{2}+t_{k+1}^{3 / 2} k_{3}+t_{k+1}^{2} k_{4}$, using (31), we find:
$$r_{D_{k+1}}^{2+l}\left|\nabla_{g_{k+1}^{D}}^{l}\left(\mathscr{F}_{g^{D_{k+1}}}\left(g^{A_{k+1}}\right)-\mho^{A_{k+1}}\right)\right|_{g^{D_{k+1}}}=\mathrm{O}\left(T_{k} t_{k+1}^{\frac{5}{2}} r_{b_{k+1}}^{5}\right) .$$
Here, the error comes from multilinear terms involving the following tensors such that for all $l \leqslant 3$, there exists $C_{l}>0$ so that
$$r_{b_{k+1}}^{l}\left|\nabla_{b_{k+1}}^{l}\left(t_{k+1}^{\frac{i}{2}} k_{i}\right)\right|_{g_{b_{k+1}}} \leqslant T_{k} t_{k+1}^{\frac{i}{2}} r_{b_{k+1}}^{i}$$
by (31), and $r_{b_{k+1}}^{l}\left|\nabla_{g_{b_{k+1}}}^{l}\left(t_{k+1}^{-1} \bar{g}_{B_{k+1}}-g_{b_{k+1}}\right)\right|_{g_{b_{k+1}}} \leqslant t_{k+1} r_{b_{k+1}}^{2}$ by Proposition 10.1.
\item[4.] Lastly, in the cut-off region $T_{k}^{\frac{1}{2}} t_{k+1}^{\frac{2}{9}}<r_{D_{k+1}}<2 T_{k}^{\frac{1}{2}} t_{k+1}^{\frac{2}{9}}$, the difference of the metrics is in:
$$T_{k} r_{b_{k}}^{5}+T_{k} r_{b_{k+1}}^{-4} .$$
\end{itemize}

Putting all of this together, we consequently obtain the stated estimate by gluing at scale $t_{k+1}^{\frac{1}{5}} \ll r_{b_{k+1}} \ll t_{k+1}^{\frac{1}{4}}$, which is satisfied by the scale of gluing chosen in the definition of $g^{A_{k+1}}$. \(\square\)

Mimicking the proof of the third point of Proposition 9.1 now yields the following result.

Corollary 10.7. If the eigenvalues of the self-dual Weyl curvature $W^{+}$of $\hat{g}^{k}$ are, are uniformly close to those of $g_{\infty}$ at some corresponding point of $X$, then the eigenvalues of the self-dual Weyl curvature $W^{+}$of $\hat{g}^{k+1}$ also have this property, with an error that uniformly tends to zero as $(t, v) \rightarrow 0$.

\section*{Conclusion of the proof}

Let us now assume that the $\lambda>0$ Einstein orbifold ( $X, g_{\infty}$ ) is conformally Kähler, and that there is an admissible sequence $\left(M, g_{i}\right)$ with
$$d_{G H}\left(\left(M, g_{i}\right),\left(X, g_{\infty}\right)\right) \rightarrow 0 .$$
By [42], after passing to a subsequence indexed by $j$, and for sufficiently large $j$, there thus exist naïve desingularizations $g_{t_{j}}^{D}$ such that $\left\|g_{j}-g_{t_{j}}^{D}\right\|_{C_{\beta_{, *}}^{2, \alpha}\left(g_{t_{j}}^{D}\right)} \rightarrow 0$, possibly with the involvement of trees of singularities. After perhaps refining our subsequence, the associated gluing scales $T_{k, j}>0$ in the tree can then be ordered such that, for all $j$,
$$T_{1, j} \leqslant T_{2, j} \leqslant \ldots \leqslant T_{n, j} .$$
By [42, 43], each $g_{j}$ is then isometric to some such $\hat{g}_{t_{j}, v_{j}}^{n}$ for $j \gg 0$.
However, the two lowest eigenvalues of $W^{+}$are everywhere negative and equal for the conformally Kähler $\lambda>0$ Einstein orbifold metric $g_{\infty}$. By Corollary 10.7, it therefore follows, for $j \gg 0$, that the two lowest eigenvalues of the self-dual Weyl curvatures $W^{+}$of our Einstein metrics $g_{j}$ are therefore everywhere negative. Since $W^{+} \in \operatorname{End}\left(\Lambda^{+}\right)$is trace-free, this means that these $g_{j}$ must have $\operatorname{det}\left(W^{+}\right)>0$ everywhere. Thus, all but a finite number of the Einstein metrics $g_{j}$ must actually satisfy Wu's criterion (1).

It is therefore a formal consequence that all but a finite number of the original $g_{i}$ must also satisfy ( 1 ). Indeed, there would otherwise be a subsequence $\left\{g_{j^{\prime}}\right\} \subset\left\{g_{i}\right\}$ consisting of Einstein metrics that do not satisfy (1). But since the $\left\{g_{j^{\prime}}\right\}$ would still be an admissible sequence converging to $\left(X, g_{\infty}\right)$, the above argument would then demonstrate that (1) must hold for an infinite number of the $\left\{g_{j^{\prime}}\right\}$, and this is of course a contradiction. This shows that, for all $i \gg 0$, the original $\left\{g_{i}\right\}$ must actually satisfy (1), and must therefore [34, 46] be conformally Kähler.

The classification [31, Theorem A] of conformally Kähler, Einstein metrics on smooth, compact 4-manifolds therefore tells us that these $\left(M, g_{i}\right)$ must actually be Kähler-Einstein unless $M$ is either $\mathbb{C P}_{2} \# \overline{\mathbb{C P}}_{2}$ or $\mathbb{C P}_{2} \# 2 \overline{\mathbb{C P}}_{2}$, equipped with a constant multiple of the Page metric or the Chen-LeBrun-Weber metric, respectively. Since these exceptional metrics are also, up to isometry and rescaling, the only conformally Kähler, Einstein metrics on these exceptional manifolds, the ( $M, g_{i}$ ) must in fact be Kähler-Einstein for $i \gg 0$ if we assume that $\left(X, g_{\infty}\right)$ either has an orbifold singularity, or is itself Kähler-Einstein. Theorems A and B thus now follow, as promised. \(\square\)

\section*{A Function Spaces}

For a tensor $s$, a point $x, \alpha>0$ and a Riemannian manifold $(M, g)$. The Hölder seminorm is defined as
$$[f]_{C^{\alpha}(g)}(x):=\sup _{\left\{y \in T_{x} M,|y|<\operatorname{inj}_{g}(x)\right\}}\left|\frac{f(x)-f\left(\exp _{x}^{g}(y)\right)}{|y|^{\alpha}}\right|_{g} .$$

For orbifolds, we consider a norm which is bounded for tensors decaying at the singular points.

Definition 12 (Weighted Hölder norms on an orbifold). Let $\beta \in \mathbb{R}, k \in \mathbb{N}$, $0<\alpha<1$ and $\left(X, g_{\infty}\right)$ an orbifold. Then, for any tensor $s$ on $X$, we define
$$\|s\|_{C_{\beta}^{k, \alpha}\left(g_{\infty}\right)}:=\sup _{X} \varrho_{o}^{-\beta}\left(\sum_{i=0}^{k} \varrho_{o}^{i}\left|\nabla_{g_{\infty}}^{i} s\right|_{g_{\infty}}+\varrho_{o}^{k+\alpha}\left[\nabla_{g_{\infty}}^{k} s\right]_{C^{\alpha}\left(g_{\infty}\right)}\right) .$$

For ALE manifolds, we will consider a norm which is bounded for tensors decaying at infinity.

Definition 13 (Weighted Hölder norms on an ALE orbifold). Let $\beta \in \mathbb{R}$, $k \in \mathbb{N}, 0<\alpha<1$ and $\left(N, g_{b}\right)$ be an ALE manifold. Then, for any tensor $s$ on $N$, we define
$$\|s\|_{C_{\beta}^{k, \alpha}\left(g_{b}\right)}:=\sup _{N} \varrho_{b}^{\beta}\left(\sum_{i=0}^{k} \varrho_{b}^{i}\left|\nabla_{g_{b}}^{i} s\right|_{g_{b}}+\varrho_{b}^{k+\alpha}\left[\nabla_{g_{b}}^{k} s\right]_{C^{\alpha}\left(g_{b}\right)}\right) .$$

Next, using a partition of unity
$$1=\Upsilon_{X^{t}}+\sum_{j} \Upsilon_{N_{j}^{t}}$$
on $M$, where $\Upsilon_{X^{t}}$ equals 1 when $g_{t}^{D}=g_{\infty}$ and $\Upsilon_{N_{j}^{t}}$ equals 1 where $g_{t}^{D}=t_{j} g_{b_{j}}$ (see [42]), we can define a global norm.

Definition 14 (Weighted Hölder norm on a naïve desingularization). Let $\beta \in \mathbb{R}, k \in \mathbb{N}$ and $0<\alpha<1$. We define for $s \in T M^{\otimes l_{+}} \otimes T^{*} M^{\otimes l_{-}}$a tensor $\left(l_{+}, l_{-}\right) \in \mathbb{N}^{2}$, with $l:=l_{+}-l_{-}$the associated conformal weight,
$$\|s\|_{C_{\beta}^{k, \alpha}\left(g^{D}\right)}:=\left\|\Upsilon_{X^{t}} s\right\|_{C_{\beta}^{k, \alpha}\left(g_{\infty}\right)}+\sum_{j} T_{j}^{\frac{l}{2}}\left\|\Upsilon_{N_{j}^{t}} s\right\|_{C_{\beta}^{k, \alpha}\left(g_{b_{j}}\right)} .$$

\section*{Decoupling norms.}

For each singular point $p_{k}$, we consider the annuli $A_{k}\left(t, \epsilon_{0}\right):=\left(\Phi_{k}\right)_{*} A_{\boldsymbol{\delta}}\left(\epsilon_{0}^{-1} \sqrt{t_{k}}, \epsilon_{0}\right)$ and $B_{k}\left(\epsilon_{0}\right):=\left(\Phi_{k}\right)_{*} B_{\boldsymbol{\delta}}\left(0, \epsilon_{0}\right)$, as well as cut-off functions $\Upsilon_{A_{k}\left(t, \epsilon_{0}\right)}$ and $\Upsilon_{B_{k}\left(\epsilon_{0}\right)}$ respectively supported in $A_{k}\left(t, \epsilon_{0}\right)$ and $B_{k}\left(\epsilon_{0}\right)$, and equal to 1 on $A_{k}\left(t, 2 \epsilon_{0}\right)$ and $B_{k}\left(\epsilon_{0} / 2\right)$.

Definition 15 ( $C_{\beta, *}^{k, \alpha}$-norm on 2-tensors). Let $h$ be a 2-tensor on $\left(M, g^{D}\right)$, $\left(X, g_{\infty}\right)$ or $\left(N, g_{b}\right)$. We define its $C_{\beta, *}^{k, \alpha}$-norm by
$$\|h\|_{C_{\beta, *}^{k, \alpha}}:=\inf _{h_{*}, \mathfrak{H}_{k}}\left\|h_{*}\right\|_{C_{\beta}^{k, \alpha}}+\sum_{k}\left|\mathfrak{H}_{k}\right|_{\delta},$$
where the infimum is taken on the $\left(h_{*},\left(\mathfrak{H}_{k}\right)_{k}\right)$ satisfying $h=h_{*}+\sum_{k} \Upsilon_{A_{k}\left(t, \epsilon_{0}\right)} \mathfrak{H}_{k}$ for $\left(M, g^{D}\right)$ or $h=h_{*}+\sum_{k} \Upsilon_{B_{k}\left(\epsilon_{0}\right)} \mathfrak{H}_{k}$ for $\left(X, g_{\infty}\right)$ or $\left(N, g_{b}\right)$, where each $\mathfrak{H}_{k}$ is some constant and trace-free symmetric 2 -tensors on $\mathbb{R}^{4} / \Gamma_{k}$.

Finally, we also introduce a function space that is particularly well-suited to Ricci-flat ALE spaces; cf. [40, Definition 5.18].

Definition 16 ( $C_{\beta, * *}^{2, \alpha}$ norm on an ALE orbifold). Let ( $N, g_{b}$ ) be an ALE orbifold, let $h$ be a 2 -tensor on $N$, and assume that $h=\mathfrak{H}^{4}+\mathrm{O}\left(\varrho_{b}^{-4-\beta}\right)$ for $\beta>0$. For $\Upsilon$, a cut-off function supported in $N-K$. We define the $C_{\beta, * *}^{2, \alpha}$-norm of $h$ as:
$$\|h\|_{C_{\beta, * *}^{2, \alpha}}:=\sup \varrho_{b}^{4}\left|\mathfrak{H}^{4}\right|_{g_{\delta}}+\left\|\left(1+\varrho_{b}\right)^{4}\left(h-\Upsilon \mathfrak{H}^{4}\right)\right\|_{C_{\beta, \phi}^{2, \alpha}} .$$

Note that this definition actually corrects a minor error in [43] that is fortunately harmless in most contexts. For a detailed discussion of this point, see [23, Remark A.12] concerning Ricci-flat Kähler ALE metrics.

Acknowledgments. The authors would like to thank the Simons Center for Geometry and Physics for its hospitality during the completion of this article. The first author would also like to express his gratitude to the Simons Foundation and the Fondation Sciences Mathématiques de Paris for their partial financial support of this research.

\section*{References}
[1] M. T. Anderson, Ricci curvature bounds and Einstein metrics on compact manifolds, J. Amer. Math. Soc., 2 (1989), pp. 455-490.
[2] M. T. Anderson and J. Cheeger, Diffeomorphism finiteness for manifolds with Ricci curvature and $L^{n / 2}$-norm of curvature bounded, Geom. Funct. Anal., 1 (1991), pp. 231-252.
[3] V. Apostolov and P. Gauduchon, Selfdual Einstein Hermitian four-manifolds, Ann. Sc. Norm. Super. Pisa Cl. Sci. (5), 1 (2002), pp. 203-243.
[4] H. Auvray, From ALE to ALF gravitational instantons, Compos. Math., 154 (2018), pp. 1159-1221.
[5] S. Bando, Bubbling out of Einstein manifolds, Tohoku Math. J. (2), 42 (1990), pp. 205-216.
[6] -, Correction and addition: "Bubbling out of Einstein manifolds", Tohoku Math. J. (2), 42 (1990), pp. 587-588.
[7] S. Bando, A. Kasue, and H. Nakajima, On a construction of coordinates at infinity on manifolds with fast curvature decay and maximal volume growth, Invent. Math., 97 (1989), pp. 313-349.
[8] A. L. Besse, Einstein Manifolds, vol. 10 of Ergebnisse der Mathematik und ihrer Grenzgebiete (3), Springer-Verlag, Berlin, 1987.
[9] O. Biquard, Désingularisation de métriques d'Einstein. I, Invent. Math., 192 (2013), pp. 197-252.
[10] -, Désingularisation de métriques d'Einstein. II, Invent. Math., 204 (2016), pp. 473-504.
[11] C. P. Boyer, Conformal duality and compact complex surfaces, Math. Ann., 274 (1986), pp. 517-526.
[12] C. P. Boyer and K. Galicki, Sasakian geometry, Oxford Mathematical Monographs, Oxford University Press, Oxford, 2008.
[13] C. P. Boyer, K. Galicki, and J. Kollár, Einstein metrics on spheres, Ann. of Math. (2), 162 (2005), pp. 557-580.
[14] R. L. Bryant, Bochner-Kähler metrics, J. Amer. Math. Soc., 14 (2001), pp. 623-715.
[15] J. Cheeger and A. Naber, Regularity of Einstein manifolds and the codimension 4 conjecture, Ann. of Math. (2), 182 (2015), pp. 1093-1165.
[16] X. X. Chen, C. LeBrun, and B. Weber, On conformally Kähler, Einstein manifolds, J. Amer. Math. Soc., 21 (2008), pp. 1137-1168.
[17] T. C. Collins and G. Székelyhidi, Sasaki-Einstein metrics and K-stability, Geom. Topol., 23 (2019), pp. 1339-1413.
[18] A. Derdziński, Self-dual Kähler manifolds and Einstein manifolds of dimension four, Compositio Math., 49 (1983), pp. 405-433.
[19] K. Galicki and H. B. Lawson, Jr., Quaternionic reduction and quaternionic orbifolds, Math. Ann., 282 (1988), pp. 1-21.
[20] P. Griffiths and J. Harris, Principles of Algebraic Geometry, Wiley-Interscience, New York, 1978.
[21] M. Gromov, Structures métriques pour les variétés riemanniennes, CEDIC, Paris, 1981. Edited by J. Lafontaine and P. Pansu.
[22] N. J. Hitchin, Compact four-dimensional Einstein manifolds, J. Differential Geometry, 9 (1974), pp. 435-441.
[23] Y. Huang and T. Ozuch, Regularity of Einstein 5-manifolds via 4dimensional gap theorems, e-print arXiv:2512.21317 [math.DG], 2025.
[24] J. Jost, Harmonic mappings between Riemannian manifolds, vol. 4 of Proceedings of the Centre for Mathematical Analysis, Australian National University, Australian National University, Centre for Mathematical Analysis, Canberra, 1984.
[25] J. Kollár, Einstein metrics on five-dimensional Seifert bundles, J. Geom. Anal., 15 (2005), pp. 445-476.
[26] J. Kollár and N. I. Shepherd-Barron, Threefolds and deformations of surface singularities, Invent. Math., 91 (1988), pp. 299-338.
[27] P. B. Kronheimer, The construction of ALE spaces as hyper-Kähler quotients, J. Differential Geom., 29 (1989), pp. 665-683.
[28] -, A Torelli-type theorem for gravitational instantons, J. Differential Geom., 29 (1989), pp. 685-697.
[29] C. LeBrun, Einstein metrics on complex surfaces, in Geometry and Physics (Aarhus, 1995), vol. 184 of Lecture Notes in Pure and Appl. Math., Dekker, New York, 1997, pp. 167-176.
[30] -, Einstein metrics, complex surfaces, and symplectic 4-manifolds, Math. Proc. Cambridge Philos. Soc., 147 (2009), pp. 1-8.
[31] -, On Einstein, Hermitian 4-manifolds, J. Differential Geom., 90 (2012), pp. 277-302.
[32] -, Einstein metrics, harmonic forms, and symplectic four-manifolds, Ann. Global Anal. Geom., 48 (2015), pp. 75-85.
[33] -, Mass, Kähler manifolds, and symplectic geometry, Ann. Global Anal. Geom., 56 (2019), pp. 97-112.
[34] -, Einstein manifolds, self-dual Weyl curvature, and conformally Kähler geometry, Math. Res. Lett., 28 (2021), pp. 127-144.
[35] A.-K. Liu, Some new applications of general wall crossing formula, Gompf's conjecture and its applications, Math. Res. Lett., 3 (1996), pp. 569-585.
[36] H. Nakajima, Hausdorff convergence of Einstein 4-manifolds, J. Fac. Sci. Univ. Tokyo Sect. IA Math., 35 (1988), pp. 411-424.
[37] -, Self-duality of ALE Ricci-flat 4-manifolds and positive mass theorem, in Recent topics in differential and analytic geometry, vol. 18 of Adv. Stud. Pure Math., Academic Press, Boston, MA, 1990, pp. 385-396.
\begin{itemize}
\item[] [38] Y. Odaka, C. Spotti, and S. Sun, Compact moduli spaces of del Pezzo surfaces and Kähler-Einstein metrics, J. Differential Geom., 102 (2016), pp. 127-172.
\item[] [39] H. Ohta and K. Ono, Notes on symplectic 4-manifolds with $b_{2}^{+}=1$. II, Internat. J. Math., 7 (1996), pp. 755-770.
\item[] [40] T. Ozuch, Completion of the Moduli Space of Einstein 4-Manifolds, PhD thesis, École Normale Supérieure (Paris), 2020.
\item[] [41] -, Higher order obstructions to the desingularization of Einstein metrics, Camb. J. Math., 9 (2021), pp. 901-976.
\item[] [42] -, Noncollapsed degeneration of Einstein 4-manifolds, I, Geom. Topol., 26 (2022), pp. 1483-1528.
\item[] [43] -, Noncollapsed degeneration of Einstein 4-manifolds, II, Geom. Topol., 26 (2022), pp. 1529-1634.
\item[] [44] I. Şuvaina, ALE Ricci-flat Kähler metrics and deformations of quotient surface singularities, Ann. Global Anal. Geom., 41 (2012), pp. 109-123.
\item[] [45] E. P. Wright, Quotients of gravitational instantons, Ann. Global Anal. Geom., 41 (2012), pp. 91-108.
\item[] [46] P. Wu, Einstein four-manifolds with self-dual Weyl curvature of nonnegative determinant, Int. Math. Res. Not. IMRN, (2021), pp. 1043-1054.
\end{itemize}