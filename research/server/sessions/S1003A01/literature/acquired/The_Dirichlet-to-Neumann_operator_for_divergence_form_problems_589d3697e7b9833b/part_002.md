---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: The Dirichlet-to-Neumann operator for divergence form problems]

Proof. Let $j=\kappa \circ \pi_{\mathrm{BD}(G)}: \operatorname{dom}(G) \rightarrow H$ and let $V(\mathfrak{b})=\{u \in \operatorname{dom}(G): \mathfrak{b}(u, v)=$ 0 for all $v \in \operatorname{ker} j\}$. Then $V(\mathfrak{b}) \cap \operatorname{ker} j=\operatorname{ker}(-D a \stackrel{\circ}{G}+m)=\{0\}$. Then the statement follows from [ACSVV] Theorem 8.11 and Proposition 5.10. \(\square\)

Even if the inclusion $\operatorname{dom}(G) \subset H_{0}$ is compact, then in general $\Lambda_{H}$ is not an m-sectorial graph. A counterexample has been given in [BE2] Example 3.7.

\section*{6 Resolvent convergence, non-coercive case}

In this section we consider resolvent convergence of a sequence of Dirichlet-to-Neumann operators without the coercivity condition on $m$. Throughout this section, we adopt the notation and assumptions as in the beginning of Section 2. Let $H$ be a Hilbert space and let $\kappa \in \mathcal{L}(\mathrm{BD}(G), H)$ be one-to-one with dense range. Set $j=\kappa \circ \pi_{\mathrm{BD}(G)}: \operatorname{dom}(G) \rightarrow H$.

We need a stronger version of convergence for the leading coefficients, which we next introduce. Let $a, a_{1}, a_{2}, \ldots \in \mathcal{L}\left(H_{1}\right)$ be coercive. We say that $\left(a_{n}\right)_{n \in \mathbb{N}}$ converges to $a$ independent of the boundary conditions if for every strictly increasing sequence $\left(n_{k}\right)_{k \in \mathbb{N}}$ in $\mathbb{N}$, all $f, f_{1}, f_{2}, \ldots \in H_{0}$ and all $u, u_{1}, u_{2}, \ldots \in \operatorname{dom}(G)$ with
$$\left[\begin{array}{l}
\lim _{k \rightarrow \infty} f_{k}=f \text { weakly in } H_{0}, \\
\lim _{k \rightarrow \infty} u_{k}=u \text { weakly in } \operatorname{dom}(G), \text { and } \\
u_{k} \in \operatorname{dom}\left(D a_{n_{k}} G\right) \text { and }-D a_{n_{k}} G u_{k}=f_{k} \text { for all } k \in \mathbb{N}
\end{array}\right.$$
it follows that $\lim _{k \rightarrow \infty} a_{n_{k}} G u_{k}=a G u$ weakly in $H_{1}$.
Note that $D$ is weakly closed and $\lim _{k \rightarrow \infty} D\left(a_{n_{k}} G u_{k}\right)=\lim _{k \rightarrow \infty}-f_{k}=-f$ weakly in $H_{0}$. So $a G u \in \operatorname{dom}(D)$ and $-D a G u=f$. In particular $u \in \operatorname{dom}(D a G)$.

Example 6.1. In this example we show that in the classical situation, convergence of the coefficients independent of the boundary conditions is equivalent to the already studied notion of $H$-convergence, see [Tar] and [MT].

Let $\Omega \subset \mathbb{R}^{d}$ be open and bounded. Further, let $H_{0}, H_{1}, G$ and $D$ be as in Example 2.3. We identify an element of $L_{\infty}\left(\Omega, \mathbb{C}^{d \times d}\right)$ with an element of $\mathcal{L}\left(H_{1}\right)$ in the natural way. Let $a, a_{1}, a_{2}, \ldots \in L_{\infty}\left(\Omega, \mathbb{R}^{d \times d}\right)$. Note that we require that the matrices are real valued, but they do not have to be symmetric. Suppose that $\operatorname{Re} a_{n} \geqslant \mu I$ for all $n \in \mathbb{N}, \operatorname{Re} a \geqslant \mu I$ and $\sup _{n}\left\|a_{n}\right\|_{\mathcal{L}\left(H_{1}\right)}<\infty$.

Recall that the sequence $\left(a_{n}\right)_{n \in \mathbb{N}}$ is called $H$-convergent to $a$, if for all $f \in H^{-1}(\Omega)$ and for all $n \in \mathbb{N}$ with $u_{n} \in H_{0}^{1}(\Omega)$ satisfying
$$\left(a_{n} \operatorname{grad} u_{n}, \operatorname{grad} v\right)_{L_{2}(\Omega)^{d}}=f(v)$$
for all $v \in H_{0}^{1}(\Omega)$, it follows that $\lim _{n \rightarrow \infty} u_{n}=u$ weakly in $H_{0}^{1}(\Omega)$ and $\lim _{n \rightarrow \infty} a_{n} \operatorname{grad} u_{n}=$ $a \operatorname{grad} u$ weakly in $L_{2}(\Omega)^{d}$, where $u \in H_{0}^{1}(\Omega)$ is such that
$$(a \operatorname{grad} u, \operatorname{grad} v)_{L_{2}(\Omega)^{d}}=f(v)$$
for all $v \in H_{0}^{1}(\Omega)$.

Suppose that the sequence $\left(a_{n}\right)_{n \in \mathbb{N}}$ is $H$-convergent to $a$. We show that $\left(a_{n}\right)_{n \in \mathbb{N}}$ converges to $a$ independent of the boundary conditions. Let $f, f_{1}, f_{2}, \ldots \in L_{2}(\Omega), u, u_{1}, u_{2}, \ldots \in$ $H^{1}(\Omega)$ and $\left(n_{k}\right)_{k \in \mathbb{N}}$ satisfy (11). Then every subsequence $\left(a_{n_{k}}\right)_{k \in \mathbb{N}}$ is $H$-convergent to $a$ by the discussion after Definition 6.4 in [Tar]. So without loss of generality we may assume that $n_{k}=k$ for all $k \in \mathbb{N}$. As $\left(u_{k}\right)_{k \in \mathbb{N}}$ converges to $u$ weakly in $H^{1}(\Omega)$ it also converges weakly in $H_{\text {loc }}^{1}(\Omega)$. The inclusion $H_{0}^{1}(\Omega) \subset L_{2}(\Omega)$ is compact since $\Omega$ is bounded. Hence also the inclusion $L_{2}(\Omega) \subset\left(H_{0}^{1}(\Omega)\right)^{\prime}=H^{-1}(\Omega)$ is compact. Therefore $\left(f_{k}\right)_{k \in \mathbb{N}}$ converges strongly to $f$ in $H^{-1}(\Omega) \subset H_{\text {loc }}^{-1}(\Omega)$. Then the criteria of Lemma 10.3 in [Tar] are fulfilled and we obtain that $\left(a_{k} G u_{k}\right)_{k \in \mathbb{N}}$ converges weakly to $a G u$ in $L_{2, \text { loc }}(\Omega)^{d}$. Since the sequence $\left(a_{k} G u_{k}\right)_{k \in \mathbb{N}}$ in $L_{2}(\Omega)^{d}$ is bounded in $L_{2}(\Omega)^{d}$, there exists a $q \in L_{2}(\Omega)^{d}$ and a subsequence of $\left(a_{k} G u_{k}\right)_{k \in \mathbb{N}}$ that weakly converges to $q$ in $L_{2}(\Omega)^{d}$. By uniqueness of limits in $L_{2, \text { loc }}(\Omega)^{d}$, we must have that $q=a G u$. So the subsequence converges to $a G u$ in $L_{2}(\Omega)^{d}$. Using the standard subsequence argument we deduce that $\left(a_{k} G u_{k}\right)_{k \in \mathbb{N}}$ converges weakly to $a G u$ in $L_{2}(\Omega)^{d}=H_{1}$.

Conversely, suppose that $\left(a_{n}\right)_{n \in \mathbb{N}}$ converges to $a$ independent of the boundary conditions. We shall prove that the sequence $\left(a_{n}\right)_{n \in \mathbb{N}}$ is $H$-convergent to $a$. Let $f \in H^{-1}(\Omega)$. For all $n \in \mathbb{N}$ let $u_{n}, u \in H_{0}^{1}(\Omega)$ satisfy
$$\left(a_{n} \operatorname{grad} u_{n}, \operatorname{grad} v\right)_{L_{2}(\Omega)^{d}}=f(v) \quad \text { and } \quad(a \operatorname{grad} u, \operatorname{grad} v)_{L_{2}(\Omega)^{d}}=f(v)$$
for all $v \in H_{0}^{1}(\Omega)$. We need to show that $\lim u_{n}=u$ weakly in $H_{0}^{1}(\Omega)$ and $\lim a_{n} \operatorname{grad} u_{n}=$ $a \operatorname{grad} u$ weakly in $L_{2}(\Omega)^{d}$. Since $L_{2}(\Omega)$ is dense in $H^{-1}(\Omega)$, there exists a sequence $\left(f_{\ell}\right)_{\ell \in \mathbb{N}}$ in $L_{2}(\Omega)$ such that $\lim _{\ell \rightarrow \infty} f_{\ell}=f$ in $H^{-1}(\Omega)$. For all $n, \ell \in \mathbb{N}$ let $u_{n}^{\ell}, u^{\ell} \in H_{0}^{1}(\Omega)$ be such that
$$\left(a_{n} \operatorname{grad} u_{n}^{\ell}, \operatorname{grad} v\right)_{L_{2}(\Omega)^{d}}=\left(f_{\ell}, v\right)_{L_{2}(\Omega)} \quad \text { and } \quad\left(a \operatorname{grad} u^{\ell}, \operatorname{grad} v\right)_{L_{2}(\Omega)^{d}}=\left(f_{\ell}, v\right)_{L_{2}(\Omega)}$$
for all $v \in H_{0}^{1}(\Omega)$.
Let $\ell \in \mathbb{N}$. We shall show that $\lim _{n \rightarrow \infty} u_{n}^{\ell}=u^{\ell}$ weakly in $H_{0}^{1}(\Omega)$ and $\lim _{n \rightarrow \infty} a_{n} \operatorname{grad} u_{n}^{\ell}=$ $a \operatorname{grad} u^{\ell}$ weakly in $L_{2}(\Omega)^{d}$. Note that the sequence $\left(u_{n}^{\ell}\right)_{n \in \mathbb{N}}$ is bounded in $H_{0}^{1}(\Omega)$. Choose $\left(n_{k}\right)_{k \in \mathbb{N}}$ to be a strictly increasing sequence of natural numbers such that $\left(u_{n_{k}}^{\ell}\right)_{k \in \mathbb{N}}$ weakly converges in $H_{0}^{1}(\Omega)$, say to $w^{\ell} \in H_{0}^{1}(\Omega)$. Since the sequence $\left(a_{n}\right)_{n \in \mathbb{N}}$ converges to $a$ independent of the boundary conditions, one deduces that $\lim _{k \rightarrow \infty} a_{n_{k}} \operatorname{grad} u_{n_{k}}^{\ell}=a \operatorname{grad} w^{\ell}$ weakly in $L_{2}(\Omega)^{d}$ and
$$\left(a \operatorname{grad} w^{\ell}, \operatorname{grad} v\right)_{L_{2}(\Omega)^{d}}=\left(f_{\ell}, v\right)_{L_{2}(\Omega)}$$
for all $v \in H_{0}^{1}(\Omega)$. Uniqueness of $u^{\ell}$ implies $w^{\ell}=u^{\ell}$. Hence $\lim _{n \rightarrow \infty} u_{n}^{\ell}=u^{\ell}$ weakly in $H_{0}^{1}(\Omega)$ by a subsubsequence argument. Since the sequence $\left(a_{n}\right)_{n \in \mathbb{N}}$ converges to $a$ independent of the boundary conditions, we obtain $\lim _{n \rightarrow \infty} a_{n} \operatorname{grad} u_{n}^{\ell}=a \operatorname{grad} u^{\ell}$ weakly in $L_{2}(\Omega)^{d}$.

By the Dirichlet-type Poincaré inequality there exists a $c_{0}>0$ such that $\|v\|_{L_{2}(\Omega)} \leqslant$ $c_{0}\|\operatorname{grad} v\|_{L_{2}(\Omega)^{d}}$ for all $v \in H_{0}^{1}(\Omega)$. If $n, \ell \in \mathbb{N}$, then
$$\begin{aligned}
\mu\left\|\operatorname{grad}\left(u_{n}^{\ell}-u_{n}\right)\right\|_{L_{2}(\Omega)^{d}}^{2} & \leqslant \operatorname{Re}\left(a_{n} \operatorname{grad}\left(u_{n}^{\ell}-u_{n}\right), \operatorname{grad}\left(u_{n}^{\ell}-u_{n}\right)\right)_{L_{2}(\Omega)^{d}} \\
& =\operatorname{Re}\left(f_{\ell}-f\right)\left(u_{n}^{\ell}-u_{n}\right)
\end{aligned}$$
$$\begin{aligned}
& \leqslant\left\|f_{\ell}-f\right\|_{H^{-1}(\Omega)}\left\|u_{n}^{\ell}-u_{n}\right\|_{H_{0}^{1}(\Omega)} \\
& \leqslant\left(1+c_{0}\right)\left\|f_{\ell}-f\right\|_{H^{-1}(\Omega)}\left\|\operatorname{grad}\left(u_{n}^{\ell}-u_{n}\right)\right\|_{L_{2}(\Omega)^{d}} .
\end{aligned}$$
Therefore
$$\left\|u_{n}^{\ell}-u_{n}\right\|_{H_{0}^{1}(\Omega)} \leqslant\left(1+c_{0}\right)\left\|\operatorname{grad}\left(u_{n}^{\ell}-u_{n}\right)\right\|_{L_{2}(\Omega)^{d}} \leqslant\left(1+c_{0}\right)^{2} \mu^{-1}\left\|f_{\ell}-f\right\|_{H^{-1}(\Omega)} .$$
Similarly $\left\|u^{\ell}-u\right\|_{H_{0}^{1}(\Omega)} \leqslant\left(1+c_{0}\right)^{2} \mu^{-1}\left\|f_{\ell}-f\right\|_{H^{-1}(\Omega)}$. If $n, \ell \in \mathbb{N}$, then
$$\left\|a_{n} \operatorname{grad} u_{n}^{\ell}-a_{n} \operatorname{grad} u_{n}\right\|_{L_{2}(\Omega)^{d}} \leqslant c\left\|u_{n}^{\ell}-u_{n}\right\|_{H_{0}^{1}(\Omega)} \leqslant c\left(1+c_{0}\right)^{2} \mu^{-1}\left\|f_{\ell}-f\right\|_{H^{-1}(\Omega)},$$
where $c=\|a\|_{\mathcal{L}\left(H_{1}\right)} \vee \sup _{k \in \mathbb{N}}\left\|a_{k}\right\|_{\mathcal{L}\left(H_{1}\right)}$. Similarly one deduces $\left\|a \operatorname{grad} u^{\ell}-a \operatorname{grad} u\right\|_{L_{2}(\Omega)^{d}} \leqslant$ $c\left(1+c_{0}\right)^{2} \mu^{-1}\left\|f_{\ell}-f\right\|_{H^{-1}(\Omega)}$. Now let $v \in H_{0}^{1}(\Omega)$. Then
$$\begin{array}{r}
\left|\left(u_{n}-u, v\right)_{H_{0}^{1}(\Omega)}\right| \leqslant\left|\left(u_{n}-u_{n}^{\ell}, v\right)_{H_{0}^{1}(\Omega)}\right|+\left|\left(u_{n}^{\ell}-u^{\ell}, v\right)_{H_{0}^{1}(\Omega)}\right|+\left|\left(u^{\ell}-u, v\right)_{H_{0}^{1}(\Omega)}\right| \\
\leqslant\left(1+c_{0}\right)^{2} \mu^{-1}\left\|f-f_{\ell}\right\|_{H^{-1}(\Omega)}\|v\|_{H_{0}^{1}(\Omega)}+\left|\left(u_{n}^{\ell}-u^{\ell}, v\right)_{H_{0}^{1}(\Omega)}\right| \\
+\left(1+c_{0}\right)^{2} \mu^{-1}\left\|f-f_{\ell}\right\|_{H^{-1}(\Omega)}\|v\|_{H_{0}^{1}(\Omega)}
\end{array}$$
for all $\ell, n \in \mathbb{N}$, which yields $\lim _{n \rightarrow \infty} u_{n}=u$ weakly in $H_{0}^{1}(\Omega)$. It follows similarly that $\lim _{n \rightarrow \infty} a_{n} \operatorname{grad} u_{n}=a \operatorname{grad} u$ weakly in $L_{2}(\Omega)^{d}$. Hence the sequence $\left(a_{n}\right)_{n \in \mathbb{N}}$ is $H$ -convergent to $a$.

The condition $\left(a_{n}\right)_{n \in \mathbb{N}}$ converges to $a$ independent of the boundary conditions, which we use in this section, is stronger than the condition used for the convergence in Theorem 4.2.

Proposition 6.2. Let $a, a_{1}, a_{2}, \ldots \in \mathcal{L}\left(H_{1}\right)$ and $\mu>0$. Suppose that $\operatorname{Re} a_{n} \geqslant \mu I$ for all $n \in \mathbb{N}$ and $\operatorname{Re} a \geqslant \mu I$. Suppose that $\left(a_{n}\right)_{n \in \mathbb{N}}$ converges to a independent of the boundary conditions. Further assume that the inclusion $\operatorname{dom}(G) \subset H_{0}$ is compact. Let $\iota: \operatorname{ran}(G) \hookrightarrow$ $H_{1}$ be the embedding map. Then $\lim _{n \rightarrow \infty}\left(\iota^{*} a_{n} \iota\right)^{-1}=\left(\iota^{*} a \iota\right)^{-1}$ in the weak operator topology on $\mathcal{L}(\operatorname{ran}(G))$.
Proof. Let $q \in \operatorname{ran} G \cap \operatorname{dom} \stackrel{\circ}{D}$. Let $n \in \mathbb{N}$. Write $r_{n}=\left(\iota^{*} a_{n} \iota\right)^{-1} q$. Then $r_{n} \in \operatorname{ran} G$ and $\left\|r_{n}\right\|_{H_{1}} \leqslant \mu^{-1}\|q\|_{H_{1}}$. There exists a $u_{n} \in \operatorname{dom} G \cap(\operatorname{ker} G)^{\perp_{H_{0}}}$ such that $G u_{n}=r_{n}$. Then the sequence $\left(u_{n}\right)_{n \in \mathbb{N}}$ is bounded in $\operatorname{dom} G$ by Lemma 4.1.(a). Passing to a subsequence if necessary, there exists a $u \in \operatorname{dom} G$ such that $\lim u_{n}=u$ weakly in $\operatorname{dom} G$. Let $n \in \mathbb{N}$. Then $q=\iota^{*} a_{n} \iota r_{n}=\iota^{*} a_{n} G u_{n}$. Since $q \in \operatorname{dom} \stackrel{\circ}{D}$ it follows from Lemma 4.4(a) that $a_{n} G u_{n} \in \operatorname{dom} \stackrel{\circ}{D}$ and $\stackrel{\circ}{D} a_{n} G u_{n}=\stackrel{\circ}{D} \iota^{*} a_{n} G u_{n}=\stackrel{\circ}{D} q$. Because $\left(a_{n}\right)_{n \in \mathbb{N}}$ converges to $a$ independent of the boundary conditions, we obtain that $\lim a_{n} G u_{n}=a G u$ weakly in $H_{1}$. Since the operator $\stackrel{\circ}{D}$ is closed, we obtain that $a G u \in \operatorname{dom} \stackrel{\circ}{D}$ and $\stackrel{\circ}{D} a G u=\stackrel{\circ}{D} q$. Using again Lemma 4.4(a) one deduces that $\iota^{*} a G u \in \operatorname{dom} \stackrel{\circ}{D}$ and $\stackrel{\circ}{D} \iota^{*} a G u=\stackrel{\circ}{D} q$. Hence $(\stackrel{\circ}{D} \iota) \iota^{*} a \iota G u=(\stackrel{\circ}{D} \iota) q$. Since $\dot{D}_{\iota}$ is injective by Lemma 4.4(c), it follows that $\iota^{*} a \iota G u=q$. So $G u=\left(\iota^{*} a \iota\right)^{-1} q$. Then
$$\lim \left(\iota^{*} a_{n} \iota\right)^{-1} q=\lim r_{n}=\lim G u_{n}=G u=\left(\iota^{*} a \iota\right)^{-1} q$$
weakly in $\operatorname{ran} G$.
Finally, since sup $\left\|\left(\iota^{*} a_{n} \iota\right)^{-1}\right\|_{\mathcal{L}(\operatorname{ran} G)}<\infty$ and $\operatorname{ran} G \cap \operatorname{dom} \stackrel{\circ}{D}$ is dense in $\operatorname{ran} G$ by Lemma 4.4(b), one concludes that $\lim \left(\iota^{*} a_{n} \iota\right)^{-1}=\left(\iota^{*} a \iota\right)^{-1}$ in the weak operator topology on $\mathcal{L}(\operatorname{ran}(G))$. \(\square\)

Remark 6.3. The above proposition is also valid if $\iota$ is replaced by the embedding of a closed subspace of $\operatorname{ran} G$ which contains $\operatorname{ran} \stackrel{\circ}{G}$. This is the motivation for the terminology $\left(a_{n}\right)_{n \in \mathbb{N}}$ converges to $a$ independent of the boundary conditions.

The main theorem of this section is as follows.
Theorem 6.4. Let $a, a_{1}, a_{2}, \ldots \in \mathcal{L}\left(H_{1}\right), m, m_{1}, m_{2}, \ldots \in \mathcal{L}\left(H_{0}\right)$ and $\mu>0$. Suppose that $\operatorname{Re} a_{n} \geqslant \mu I$ for all $n \in \mathbb{N}, \operatorname{Re} a \geqslant \mu I$ and $\sup _{n}\left\|a_{n}\right\|_{\mathcal{L}\left(H_{1}\right)}<\infty$. Suppose that $\left(a_{n}\right)_{n \in \mathbb{N}}$ converges to a independent of the boundary conditions and $\lim m_{n}=m$ in the weak operator topology on $\mathcal{L}\left(H_{0}\right)$. Assume that $\operatorname{ker}\left(m_{n}-D a_{n} \stackrel{\circ}{G}\right)=\{0\}$ for all $n \in \mathbb{N}$ and $\operatorname{ker}(m-D a \stackrel{\circ}{G})=$ $\{0\}$. Further assume that the inclusion $\operatorname{dom}(G) \subset H_{0}$ is compact.

For all $n \in \mathbb{N}$ let $\Lambda_{H}^{(n)}$ and $\Lambda_{H}$ be the Dirichlet-to-Neumann operators in $H$ associated with $-D a_{n} G+m_{n}$ and $-D a G+m$, respectively. Then one has the following.
\begin{itemize}
\item[(a)] The sequence $\left(\Lambda_{H}^{(n)}\right)_{n \in \mathbb{N}}$ of operators is uniformly sectorial.
\item[(b)] $\lim _{n \rightarrow \infty}\left(\lambda I+\Lambda_{H}^{(n)}\right)^{-1}=\left(\lambda I+\Lambda_{H}\right)^{-1}$ in the weak operator topology for all large $\lambda>0$.
\item[(c)] If $\kappa$ is compact, then
$$\lim _{n \rightarrow \infty}\left(\lambda I+\Lambda_{H}^{(n)}\right)^{-1}=\left(\lambda I+\Lambda_{H}\right)^{-1}$$
uniformly in $\mathcal{L}(H)$ for all large $\lambda>0$.
\end{itemize}

The proof requires a lot of preparation. Adopt the notation and assumptions of Theorem 6.4. For all $n \in \mathbb{N}$ define $\mathfrak{b}_{n}: \operatorname{dom}(G) \times \operatorname{dom}(G) \rightarrow \mathbb{C}$ by
$$\mathfrak{b}_{n}(u, v)=\left(a_{n} G u, G v\right)_{H_{1}}+\left(m_{n} u, v\right)_{H_{0}}$$
and define $V\left(\mathfrak{b}_{n}\right)=\left\{u \in \operatorname{dom}(G): \mathfrak{b}_{n}(u, v)=0\right.$ for all $\left.v \in \operatorname{ker} j\right\}$. Define similarly $\mathfrak{b}$ and $V(\mathfrak{b})$.

Lemma 6.5. For all $\varepsilon>0$ there exists an $\omega>0$ such that
$$\|u\|_{H_{0}}^{2} \leqslant \varepsilon\|u\|_{\operatorname{dom}(G)}^{2}+\omega\|j(u)\|_{H}^{2}$$
for all $n \in \mathbb{N}$ and $u \in V\left(\mathfrak{b}_{n}\right)$.
Proof. Let $n \in \mathbb{N}$. Since $\operatorname{ker}\left(m_{n}-D a_{n} \stackrel{\circ}{G}\right)=\{0\}$, the restriction $\left.j\right|_{V\left(\mathfrak{b}_{n}\right)}$ is injective. Because also the inclusion $\operatorname{dom}(G) \subset H_{0}$ is compact, it follows that for all $\varepsilon>0$ there exists an $\omega>0$ such that
$$\|u\|_{H_{0}}^{2} \leqslant \varepsilon\|u\|_{\operatorname{dom}(G)}^{2}+\omega\|j(u)\|_{H}^{2}$$
for all $u \in V\left(\mathfrak{b}_{n}\right)$. We next show that one can choose $\omega$ uniformly in $n$.
Suppose the lemma is false. Then without loss of generality and passing to a subsequence if necessary there exist $\varepsilon>0$ and for all $n \in \mathbb{N}$ there exists a $u_{n} \in V\left(\mathfrak{b}_{n}\right)$ such that
$$\left\|u_{n}\right\|_{H_{0}}^{2}>\varepsilon\left\|u_{n}\right\|_{\operatorname{dom}(G)}^{2}+n\left\|j\left(u_{n}\right)\right\|_{H}^{2} .$$

Without loss of generality we may assume that $\left\|u_{n}\right\|_{H_{0}}=1$ for all $n \in \mathbb{N}$. Then $\varepsilon\left\|u_{n}\right\|_{\operatorname{dom}(G)}^{2} \leqslant$ 1 for all $n \in \mathbb{N}$, so the sequence $\left(u_{n}\right)_{n \in \mathbb{N}}$ is bounded in $\operatorname{dom}(G)$. Passing to a subsequence if necessary there exists a $u \in \operatorname{dom}(G)$ such that $\lim u_{n}=u$ weakly in $\operatorname{dom}(G)$. Since the inclusion $\operatorname{dom}(G) \subset H_{0}$ is compact it follows that $u=\lim u_{n}$ in $H_{0}$. In particular $\|u\|_{H_{0}}=1$ and $u \neq 0$. Also $j(u)=\lim j\left(u_{n}\right)=0$ in $H$, so $u \in \operatorname{ker} j=\operatorname{dom}(\stackrel{\circ}{G})$.

If $n \in \mathbb{N}$, then $\left(a_{n} G u_{n}, \stackrel{\circ}{G} v\right)_{H_{1}}=-\left(m_{n} u_{n}, v\right)_{H_{0}}$ for all $v \in \operatorname{dom}(\stackrel{\circ}{G})=\operatorname{ker} j$, since $u_{n} \in V\left(\mathfrak{b}_{n}\right)$. Therefore $a_{n} G u_{n} \in \operatorname{dom}\left((\dot{G})^{*}\right)=\operatorname{dom}(D)$ and $-D a_{n} G u_{n}=-m_{n} u_{n}$. Next $\lim m_{n} u_{n}=m u$ weakly in $H_{0}$. Since $\left(a_{n}\right)_{n \in \mathbb{N}}$ converges to $a$ independent of the boundary conditions one deduces that $a G u \in \operatorname{dom}(D)$ and $-D a G u=-m u$. Then $u \in \operatorname{ker}(m-$ $D a \stackrel{\circ}{G})=\{0\}$. So $u=0$. This is a contradiction. \(\square\)

Lemma 6.6. There exist $\tilde{\mu}, \omega>0$ such that
$$\tilde{\mu}\|u\|_{\operatorname{dom}(G)}^{2} \leqslant \operatorname{Re} \mathfrak{b}_{n}(u)+\omega\|j(u)\|_{H}^{2}$$
for all $n \in \mathbb{N}$ and $u \in V\left(\mathfrak{b}_{n}\right)$.
Proof. Let $\tilde{\omega}=\mu+\sup _{n}\left\|m_{n}\right\|_{\mathcal{L}\left(H_{0}\right)}$. Then
$$\mu\|u\|_{\operatorname{dom}(G)}^{2} \leqslant \operatorname{Re}\left(a_{n} G u, G u\right)_{H_{1}}+\mu\|u\|_{H_{0}}^{2} \leqslant \operatorname{Re} \mathfrak{b}_{n}(u)+\tilde{\omega}\|u\|_{H_{0}}^{2}$$
for all $n \in \mathbb{N}$ and $u \in \operatorname{dom}(G)$.
Choose $\varepsilon=\frac{\mu}{2 \tilde{\omega}}$ and let $\omega>0$ be as in Lemma 6.5. Let $n \in \mathbb{N}$ and $u \in V\left(\mathfrak{b}_{n}\right)$. Then
$$\begin{aligned}
\mu\|u\|_{\operatorname{dom}(G)}^{2} & \leqslant \operatorname{Re} \mathfrak{b}_{n}(u)+\tilde{\omega}\|u\|_{H_{0}}^{2} \\
& \leqslant \operatorname{Re} \mathfrak{b}_{n}(u)+\tilde{\omega}\left(\frac{\mu}{2 \tilde{\omega}}\|u\|_{\operatorname{dom}(G)}^{2}+\omega\|j(u)\|_{H}^{2}\right) \\
& =\operatorname{Re} \mathfrak{b}_{n}(u)+\frac{\mu}{2}\|u\|_{\operatorname{dom}(G)}^{2}+\omega \tilde{\omega}\|j(u)\|_{H}^{2} .
\end{aligned}$$
So
$$\frac{\mu}{2}\|u\|_{\operatorname{dom}(G)}^{2} \leqslant \operatorname{Re} \mathfrak{b}_{n}(u)+\omega \tilde{\omega}\|j(u)\|_{H}^{2}$$
and the lemma follows. \(\square\)

Now we are able to prove Theorem 6.4.
Proof of Theorem 6.4. Let $\tilde{\mu}, \omega>0$ be as in Lemma 6.6.
(a). Set $c=\sup _{n \in \mathbb{N}}\left(\left\|a_{n}\right\|_{\mathcal{L}\left(H_{1}\right)}+\left\|m_{n}\right\|_{\mathcal{L}\left(H_{0}\right)}\right)$. Let $n \in \mathbb{N}$ and $\varphi \in \operatorname{dom}\left(\Lambda_{H}^{(n)}\right)$. There exists a $u \in \operatorname{dom}(G)$ such that $j(u)=\varphi$ and $\mathfrak{b}_{n}(u, v)=\left(\Lambda_{H}^{(n)} \varphi, j(v)\right)_{H}$ for all $v \in \operatorname{dom}(G)$. Then $u \in V\left(\mathfrak{b}_{n}\right)$ and $\left(\left(\Lambda_{H}^{(n)}+\omega I\right) \varphi, \varphi\right)_{H}=\mathfrak{b}_{n}(u)+\omega\|j(u)\|_{H}^{2}$, so $\operatorname{Re}\left(\left(\Lambda_{H}^{(n)}+\omega I\right) \varphi, \varphi\right)_{H} \geqslant$ $\tilde{\mu}\|u\|_{\text {dom }(G)}^{2}$. Therefore
$$\left|\operatorname{Im}\left(\left(\Lambda_{H}^{(n)}+\omega I\right) \varphi, \varphi\right)_{H}\right|=\left|\operatorname{Im} \mathfrak{b}_{n}(u)\right| \leqslant c\|u\|_{\operatorname{dom}(G)}^{2} \leqslant \frac{c}{\tilde{\mu}} \operatorname{Re}\left(\left(\Lambda_{H}^{(n)}+\omega I\right) \varphi, \varphi\right)_{H} .$$
Hence the operators $\Lambda_{H}^{(n)}$ are sectorial with vertex $-\omega$ and semi-angle $\arctan \frac{c}{\tilde{\mu}}$, uniformly in $n$.
[(b)]. In order not to repeat part of the proof in Statement (c) we first prove something more general. Let $\lambda>\omega$. Let $\psi, \psi_{1}, \psi_{2}, \ldots \in H$ and suppose that $\lim \psi_{n}=\psi$ weakly in $H$. We shall prove that $\lim \left(\lambda I+\Lambda_{H}^{(n)}\right)^{-1} \psi_{n}=\left(\lambda I+\Lambda_{H}\right)^{-1} \psi$ weakly in $H$.

Let $n \in \mathbb{N}$. Set $\varphi_{n}=\left(\lambda I+\Lambda_{H}^{(n)}\right)^{-1} \psi_{n}$. There exists a $u_{n} \in V\left(\mathfrak{b}_{n}\right)$ such that $j\left(u_{n}\right)=\varphi_{n}$ and
$$\mathfrak{b}_{n}\left(u_{n}, v\right)+\lambda\left(j\left(u_{n}\right), j(v)\right)_{H}=\left(\psi_{n}, j(v)\right)_{H}$$
for all $v \in \operatorname{dom}(G)$. Choose $v=u_{n}$. Then Lemma 6.6 gives $\tilde{\mu}\left\|u_{n}\right\|_{\operatorname{dom}(G)}^{2} \leqslant \operatorname{Re} \mathfrak{b}_{n}\left(u_{n}\right)+\lambda\left\|j\left(u_{n}\right)\right\|_{H}^{2}=\operatorname{Re}\left(\psi_{n}, j\left(u_{n}\right)\right)_{H} \leqslant\left\|\psi_{n}\right\|_{H}\|j\|_{\mathcal{L}(\operatorname{dom}(G), H)}\left\|u_{n}\right\|_{\operatorname{dom}(G)}$. So $\left\|u_{n}\right\|_{\operatorname{dom}(G)} \leqslant \tilde{\mu}^{-1}\left\|\psi_{n}\right\|_{H}\|j\|_{\mathcal{L}(\operatorname{dom}(G), H)}$. Since the sequence $\left(\psi_{n}\right)_{n \in \mathbb{N}}$ is bounded in $H$, the sequence $\left(u_{n}\right)_{n \in \mathbb{N}}$ is bounded in $\operatorname{dom}(G)$. Passing to a subsequence if necessary, there exists a $u \in \operatorname{dom}(G)$ such that $\lim u_{n}=u$ weakly in $\operatorname{dom}(G)$. Since the inclusion $\operatorname{dom}(G) \subset H_{0}$ is compact one deduces that $\lim u_{n}=u$ in $H_{0}$. Then $\lim m_{n} u_{n}=m u$ weakly in $H_{0}$. Moreover, $\lim \varphi_{n}=\lim j\left(u_{n}\right)=j(u)$ weakly in $H$. Next we show that $j(u)=\left(\lambda I+\Lambda_{H}\right)^{-1} \psi$.

Let $n \in \mathbb{N}$. If $v \in \operatorname{ker} j=\operatorname{dom}(\stackrel{\circ}{G})$, then $\mathfrak{b}_{n}\left(u_{n}, v\right)=0$, so $\left(a_{n} G u_{n}, \stackrel{\circ}{G} v\right)_{H_{1}}=-\left(m_{n} u_{n}, v\right)_{H_{0}}$. Hence $a_{n} G u_{n} \in \operatorname{dom}\left((\dot{G})^{*}\right)=\operatorname{dom}(D)$ and $-D a_{n} G u_{n}=-m_{n} u_{n}$. In particular, $u_{n} \in$ $\operatorname{dom}\left(D a_{n} G\right)$. Moreover, $\lim u_{n}=u$ weakly in $\operatorname{dom}(G)$ and $\lim m_{n} u_{n}=m u$ weakly in $H_{0}$. Since $\left(a_{n}\right)_{n \in \mathbb{N}}$ converges to $a$ independent of the boundary conditions, one deduces that $\lim a_{n} G u_{n}=a G u$ weakly in $H_{1}$.

Let $v \in \operatorname{dom}(G)$. If $n \in \mathbb{N}$, then (12) gives
$$\left(a_{n} G u_{n}, G v\right)_{H_{1}}+\left(m_{n} u_{n}, v\right)_{H_{0}}+\lambda\left(j\left(u_{n}\right), j(v)\right)_{H}=\left(\psi_{n}, j(v)\right)_{H} .$$
Taking the limit $n \rightarrow \infty$ one establishes
$$(a G u, G v)_{H_{1}}+(m u, v)_{H_{0}}+\lambda(j(u), j(v))_{H}=(\psi, j(v))_{H} .$$
So $\mathfrak{b}(u, v)+\lambda(j(u), j(v))_{H}=(\psi, j(v))_{H}$. Therefore $j(u) \in \operatorname{dom}\left(\Lambda_{H}\right)$ and $\left(\lambda I+\Lambda_{H}\right) j(u)=\psi$. With the usual subsequence argument we proved that $\lim \left(\lambda I+\Lambda_{H}^{(n)}\right)^{-1} \psi_{n}=\left(\lambda I+\Lambda_{H}\right)^{-1} \psi$ weakly in $H$. Now Statement (b) follows by choosing $\psi_{n}=\psi$ for all $n \in \mathbb{N}$.
(c). Finally suppose that $\kappa$ is compact. Then also $j$ is compact. Let $\lambda>\omega$. Suppose $\lim \left(\lambda I+\Lambda_{H}^{(n)}\right)^{-1}=\left(\lambda I+\Lambda_{H}\right)^{-1}$ in $\mathcal{L}(H)$ is false. Passing to a subsequence if necessary, there exist $\delta>0$ and $\psi_{1}, \psi_{2}, \ldots \in H$ such that
$$\left\|\left(\lambda I+\Lambda_{H}^{(n)}\right)^{-1} \psi_{n}-\left(\lambda I+\Lambda_{H}\right)^{-1} \psi_{n}\right\|_{H}>\delta\left\|\psi_{n}\right\|_{H}$$
for all $n \in \mathbb{N}$. Without loss of generality we may assume that $\left\|\psi_{n}\right\|_{H}=1$ for all $n \in \mathbb{N}$. Passing again to a subsequence if necessary, there exists a $\psi \in H$ such that $\lim \psi_{n}=\psi$ weakly in $H$. Let $u_{n} \in V\left(\mathfrak{b}_{n}\right)$ and $u \in \operatorname{dom}(G)$ be as in Part (b) for all $n \in \mathbb{N}$. Then $\lim u_{n}=u$ weakly in $\operatorname{dom}(G)$, so
$$\lim _{n \rightarrow \infty}\left(\lambda I+\Lambda_{H}^{(n)}\right)^{-1} \psi_{n}=\lim _{n \rightarrow \infty} j\left(u_{n}\right)=j(u)=\left(\lambda I+\Lambda_{H}\right)^{-1} \psi$$
in $H$ by the compactness of $j$. Similarly $\lim _{n \rightarrow \infty}\left(\lambda I+\Lambda_{H}^{(n)}\right)^{-1} \psi=\left(\lambda I+\Lambda_{H}\right)^{-1} \psi$ in $H$. So
$$\lim _{n \rightarrow \infty}\left\|\left(\lambda I+\Lambda_{H}^{(n)}\right)^{-1} \psi_{n}-\left(\lambda I+\Lambda_{H}\right)^{-1} \psi_{n}\right\|_{H}=0 .$$
This is a contradiction. \(\square\)

Note that the limit Dirichlet-to-Neumann graph $\Lambda_{H}$ is an operator in Theorem 6.4. In [AEKS] Theorem 5.11 a different condition on the $a_{n}$ is used to obtain resolvent convergence for symmetric operators/graphs, but possibly multi-valued limit graph $\Lambda_{H}$. Since we do not wish to require symmetry in Theorem 6.4 and we need that the limit graph $\Lambda_{H}$ is msectorial, we require conveniently that all graphs are single-valued. See also the discussion at the end of Section 5.

Finally we compare various conditions on the $a_{n}$ in the classical case.
Example 6.7. In this example we characterise the condition $\lim _{n \rightarrow \infty}\left(\iota^{*} a_{n} \iota\right)^{-1}=\left(\iota^{*} a \iota\right)^{-1}$ in the weak operator topology of $\mathcal{L}(\operatorname{ran}(G))$ in Theorem 4.2 for the classical case of Example 2.3 and real symmetric coefficients.

Let $\Omega \subset \mathbb{R}^{d}$ be open, bounded and connected. Assume that $H^{1}(\Omega)$ embeds compactly into $L_{2}(\Omega)$. Further, let $H_{0}, H_{1}, G$ and $D$ be as in Example 2.3. We identify an element of $L_{\infty}\left(\Omega, \mathbb{C}^{d \times d}\right)$ with an element of $\mathcal{L}\left(H_{1}\right)$ in the natural way. Let $a, a_{1}, a_{2}, \ldots \in L_{\infty}\left(\Omega, \mathbb{R}^{d \times d}\right)$. Suppose that $a_{n}=a_{n}^{*} \geqslant \mu I$ for all $n \in \mathbb{N}$ and $\sup _{n}\left\|a_{n}\right\|_{\mathcal{L}\left(H_{1}\right)}<\infty$. Moreover, assume that $a=a^{*} \geqslant \mu I$. We emphasise that the $a_{n}$ and $a$ are real valued and symmetric. Then the following three conditions are equivalent.
\begin{itemize}
\item[(a)] The sequence $\left(a_{n}\right)_{n \in \mathbb{N}}$ is $H$-convergent to $a$.
\item[(b)] The sequence $\left(a_{n}\right)_{n \in \mathbb{N}}$ converges to $a$ independent of the boundary conditions.
\item[(c)] $\lim _{n \rightarrow \infty}\left(\iota^{*} a_{n} \iota\right)^{-1}=\left(\iota^{*} a \iota\right)^{-1}$ in the weak operator topology of $\mathcal{L}(\operatorname{ran}(G))$.
\end{itemize}
We proved the implications (a) ⇒ (b) $\Rightarrow$ (c) in Example 6.1 and Proposition 6.2. So it remains to show the implcation (c) $\Rightarrow$ (a).

Suppose that $\lim _{n \rightarrow \infty}\left(\iota^{*} a_{n} \iota\right)^{-1}=\left(\iota^{*} a \iota\right)^{-1}$ in the weak operator topology of $\mathcal{L}(\operatorname{ran}(G))$. Since $a_{n} \geqslant \mu I$ for all $n \in \mathbb{N}$ and $\sup _{n}\left\|a_{n}\right\|_{\mathcal{L}\left(H_{1}\right)}<\infty$, it follows from [Tar] Theorem 6.5 that the sequence $\left(a_{n}\right)_{n \in \mathbb{N}}$ has a subsequence $\left(a_{n_{k}}\right)_{k \in \mathbb{N}}$ which is $H$-convergent. Hence there exist $b \in L_{\infty}\left(\Omega, \mathbb{R}^{d \times d}\right)$ and $\nu>0$ such that $\operatorname{Re} b \geqslant \nu I$ and the sequence $\left(a_{n_{k}}\right)_{k \in \mathbb{N}}$ is $H$ -convergent to $b$. Then $b=b^{*}$ by [Tar] Lemma 10.2. It follows from the implication (a) ⇒ (c) that $\lim _{k \rightarrow \infty}\left(\iota^{*} a_{n_{k}} \iota\right)^{-1}=\left(\iota^{*} b \iota\right)^{-1}$ in the weak operator topology of $\mathcal{L}(\operatorname{ran}(G))$. Therefore $\left(\iota^{*} a \iota\right)^{-1}=\left(\iota^{*} b \iota\right)^{-1}$ and $\left(\iota^{*} a \iota\right)=\left(\iota^{*} b \iota\right)$. So
$$(a \operatorname{grad} u, \operatorname{grad} v)_{L_{2}(\Omega)^{d}}=(b \operatorname{grad} u, \operatorname{grad} v)_{L_{2}(\Omega)^{d}}$$
for all $u, v \in H^{1}(\Omega)$. Write $c=a-b$. Then $(c \operatorname{grad} u, \operatorname{grad} v)_{L_{2}(\Omega)^{d}}=0$ for all $u, v \in H^{1}(\Omega)$. We shall show that $c=0$. Let $\tau \in C_{c}^{\infty}(\Omega)$ and $\xi \in \mathbb{R}^{d}$. For all $\lambda \geqslant 1$ define $u_{\lambda} \in C_{c}^{\infty}(\Omega)$ by $u_{\lambda}(x)=\tau(x) e^{i \lambda \xi \cdot x}$. Then
$$0=\left(c \operatorname{grad} u_{\lambda}, \operatorname{grad} u_{\lambda}\right)_{L_{2}(\Omega)^{d}}=(c(\operatorname{grad} \tau+i \lambda \tau \xi),(\operatorname{grad} \tau+i \lambda \tau \xi))_{L_{2}(\Omega)^{d}} .$$
Dividing by $\lambda^{2}$ and taking the limit $\lambda \rightarrow \infty$ gives $\int_{\Omega}|\tau(x)|^{2}\langle c(x) \xi, \xi\rangle_{\mathbb{C}^{d}} d x=0$. This implies that $\langle c(x) \xi, \xi\rangle_{\mathbb{C}^{d}}=0$ for almost all $x \in \Omega$. Since $\mathbb{R}^{d}$ is separable and $c=c^{*}$, this implies that $c=0$ almost everywhere. So $b=a$ almost everywhere. We proved that the sequence $\left(a_{n_{k}}\right)_{k \in \mathbb{N}}$ is $H$-convergent to $a$.

It follows similarly that every subsequence of $\left(a_{n}\right)_{n \in \mathbb{N}}$ has a subsubsequence which is $H$-convergent to $a$. Since the topology of $H$-convergence is metrisable by the discussion after Definition 6.4 in [Tar] one concludes that the sequence $\left(a_{n}\right)_{n \in \mathbb{N}}$ is $H$-convergent to $a$. This completes the proof of the implication (c) $\Rightarrow$ (a).

In [Wau2] Theorem 1.2 it is proved that the three equivalent conditions are also equivalent to a version of Condition (c), where grad is replaced by grad and $\iota$ by the embedding $\operatorname{ran}(\operatorname{grad}) \subset H_{1}$; see also Remark 6.3.

Remark 6.8. In the situation of Example 6.7, we deduce that convergence of $\left(a_{n}\right)_{n \in \mathbb{N}}$ in the weak* topology of $L_{\infty}\left(\Omega, \mathbb{R}^{d \times d}\right)$ neither implies nor is implied by $\lim \left(\iota^{*} a_{n} \iota\right)^{-1}=\left(\iota^{*} a \iota\right)^{-1}$ in the weak operator topology of $\mathcal{L}(\operatorname{ran}(G))$. One may also consult [Wau3, Examples 3.2 and 3.4] on this.

\section*{7 More examples}

The first example is from linearized elasticity.
Example 7.1. Let $\Omega \subset \mathbb{R}^{d}$ be open. Set
$$L_{2, \text { sym }}(\Omega)=\left\{S \in L_{2}(\Omega)^{d \times d}: S^{T}=S \text { a.e. }\right\} .$$
Choose $H_{0}=L_{2}(\Omega)^{d}$ and $H_{1}=L_{2, \text { sym }}(\Omega)$. Define $\widehat{G}: C_{c}^{\infty}(\Omega)^{d} \rightarrow L_{2, \text { sym }}(\Omega)$ by
$$(\widehat{G} u)_{k l}=\frac{1}{2}\left(\partial_{k} u_{l}+\partial_{l} u_{k}\right) .$$
Further define $\widehat{D}: C_{c}^{\infty}(\Omega)^{d \times d} \cap L_{2, \text { sym }}(\Omega) \rightarrow L_{2}(\Omega)^{d}$ by
$$(\widehat{D} q)_{k}=\sum_{l=1}^{d} \partial_{l} q_{k l} .$$
Then $\operatorname{dom}(\widehat{G})$ is dense in $H_{0}$ and $\operatorname{dom}(\widehat{D})$ is dense in $H_{1}$. Moreover, using integration by parts one deduces that (2) is valid. Then one can apply Example 2.2.

Korn's first inequality implies that $\left\|\partial_{k} u_{l}\right\|_{L_{2}(\Omega)} \leqslant \sqrt{2}\|\widehat{G} u\|_{H_{1}}$ for all $u \in C_{c}^{\infty}(\Omega)^{d}$ and $k, l \in\{1, \ldots, d\}$. So $\operatorname{dom}(\dot{G}) \subset H_{0}^{1}(\Omega)$. In particular the inclusion $\operatorname{dom}(\stackrel{\circ}{G}) \subset H_{0}$ is compact if $\Omega$ is bounded.

Under some regularity conditions on the boundary of $\Omega$, Korn's second inequality states that there exists a $c>0$ such that $\left\|\partial_{k} u_{l}\right\|_{L_{2}(\Omega)} \leqslant c\|u\|_{\operatorname{dom}(G)}$ for all $u \in \operatorname{dom}(G)$ and $k, l \in\{1, \ldots, d\}$. For example, if $\Omega$ is bounded with a Lipschitz boundary, then Korn's second inequality is valid. For an easy proof see [Nit] Section 3. If Korn's second inequality is valid, then $\operatorname{dom}(G) \subset H^{1}(\Omega)^{d}$. Consequently, if Korn's second inequality is valid and $\Omega$ has a continuous boundary, then the inclusion $H^{1}(\Omega) \subset L_{2}(\Omega)$ is compact and hence the inclusion $\operatorname{dom}(G) \subset H_{0}$ is compact. We point out that Korn's second inequality is not a necessary condition for the inclusion $\operatorname{dom}(G) \subset H_{0}$ to be compact, see [Wec] Theorem 1.

In particular, suppose $\Omega$ is bounded with a Lipschitz boundary and write $\Gamma=\partial \Omega$. Let $\sigma \in\left(-\infty, \frac{1}{2}\right]$ and set $H=H^{\sigma}(\Gamma)^{d}$. Then $\operatorname{Tr} u \in H$ for all $u \in \operatorname{dom}(G)$. Moreover, $\left.\operatorname{Tr}\right|_{\mathrm{BD}(G)}: \operatorname{BD}(G) \rightarrow H$ is injective and has dense range. So one can consider as in Section 3 a Dirichlet-to-Neumann operator in $H$. Note that $\left.\operatorname{Tr}\right|_{\mathrm{BD}(G)}$ is compact if $\sigma<\frac{1}{2}$.

The second example is from electro-magneto statics.
Example 7.2. Let $\Omega \subset \mathbb{R}^{3}$ be open. Using integration by parts one deduces that
$$(\operatorname{curl} u, v)_{L_{2}(\Omega)^{3}}=(u, \operatorname{curl} v)_{L_{2}(\Omega)^{3}}$$
for all $u, v \in C_{c}^{\infty}(\Omega)^{3}$. Therefore let $H_{0}=H_{1}=L_{2}(\Omega)^{3}$ and define $\widehat{G}=\widehat{D}: C_{c}^{\infty}(\Omega)^{3} \rightarrow$ $L_{2}(\Omega)^{3}$ by $\widehat{G} u=\widehat{D} u=i$ curl $u$. Then (2) is satisfied. Using the construction in Example 2.2 one obtains a new example.

\section*{Acknowledgements}

The authors wish to thank the referee to raise questions which improved the paper. The third named author expresses his gratitude for the wonderful atmosphere and hospitality extended to him during a two months research visit at the University of Auckland. Part of this work is supported by the Marsden Fund Council from Government funding, administered by the Royal Society of New Zealand. Part of this work is supported by the EU Marie Curie IRSES program, Project AOS, No. 318910. Part of this work was carried out with financial support of the EPSRC grant EP/L018802/2: Mathematical foundations of metamaterials: homogenisation, dissipation and operator theory.

\section*{References}
\begin{itemize}
\item[] [ACSVV] Arendt, W., Chill, R., Seifert, C., Vogt, H. and Voigt, J., Internet Seminar 18, 2015.
\item[] [AE1] Arendt, W. and Elst, A. F. M. ter, The Dirichlet-to-Neumann operator on rough domains. J. Differential Equations 251 (2011), 2100-2124.
\item[] [AE2] -, Sectorial forms and degenerate differential operators. J. Operator Theory 67 (2012), 33-72.
\item[] [AEKS] Arendt, W., Elst, A. F. M. ter, Kennedy, J. B. and Sauter, M., The Dirichlet-to-Neumann operator via hidden compactness. J. Funct. Anal. 266 (2014), 1757-1786.
\item[] [AKM] Axelsson, A., Keith, S. and M ${ }^{\mathrm{c}}$ Intosh, A., Quadratic estimates and functional calculi of perturbed Dirac operators. Invent. Math. 163 (2006), 455-497.
\item[] [BE1] Behrndt, J. and Elst, A. F. M. ter, Dirichlet-to-Neumann maps on bounded Lipschitz domains. J. Differential Equations 259 (2015), 5903-5926.
\item[] [BE2] -, The Dirichlet-to-Neumann map for Schrödinger operators with complex potentials. Discrete Contin. Dyn. Syst. Ser. S 10 (2017), 661-671.
\item[] [McL] McLean, W., Strongly elliptic systems and boundary integral equations. Cambridge University Press, 2000.
\end{itemize}
\begin{itemize}
\item[] [MT] Murat, F. and Tartar, L., H-convergence. In Cherkaev, A. and Kohn, R., eds., Topics in the mathematical modelling of composite materials, Progr. Nonlinear Differential Equations Appl. 31, 21-43. Birkhäuser, Boston, 1997.
\item[] [Nit] Nitsche, J. A., On Korn's second inequality. RAIRO Anal. Numér. 15 (1981), 237-248.
\item[] [PSTW] Picard, R., Seidler, S., Trostorff, S. and Waurick, M., On abstract div-grad systems. J. Differential Equations 260 (2016), 4888-4917.
\item[] [PTW1] Picard, R., Trostorff, S. and Waurick, M., On a class of boundary control problems. Oper. Matrices 8 (2014), 185-204.
\item[] [PTW2] \_\_\_\_, On a comprehensive class of linear control problems. IMA J. Math. Control Inform. 33 (2016), 257-291.
\item[] [Ron] Rondi, L., Continuity properties of Neumann-to-Dirichlet maps with respect to the $H$-convergence of the coefficients matrices. Inverse Problems 31 (2015), 045002.
\item[] [Tar] Tartar, L., The general theory of homogenization. A personalized introduction. Lecture Notes of the Unione Matematica Italiana 7. Springer-Verlag, Berlin, 2009.
\item[] [Tro] Trostorff, S., A characterization of boundary conditions yielding maximal monotone operators. J. Funct. Anal. 267 (2014), 2787-2822.
\item[] [TW] Trostorff, S. and Waurick, M., A note on elliptic type boundary value problems with maximal monotone relations. Math. Nachr. 287 (2014), 1545-1558.
\item[] [Wau1] Waurick, M., On the continuous dependence on the coefficients of evolutionary equations, 2016. Habilitation thesis, TU Dresden.
\item[] [Wau2] \_\_\_\_G-convergence and the weak operator topology. Proc. Appl. Math. Mech. 16 (2016), 883-884.
\item[] [Wau3] \_\_\_\_ , Nonlocal $H$-convergence. arXiv-preprint (2018) arXiv:1804.02026.
\item[] [Wec] Weck, N., Local compactness for linear elasticity in irregular domains. Math. Methods Appl. Sci. 17 (1994), 107-113.
\end{itemize}
A.F.M. ter Elst
University of Auckland
Department of Mathematics
Auckland 1142
New Zealand
terelst@math.auckland.ac.nz
G. Gordon
University of Auckland
Department of Mathematics
Auckland 1142
New Zealand
g.gordon@auckland.ac.nz

Marcus Waurick
Department of Mathematics and Statistics
University of Strathclyde
Livingstone Tower
26 Richmond Street
Glasgow G1 1XH
UK
marcus.waurick@strath.ac.uk