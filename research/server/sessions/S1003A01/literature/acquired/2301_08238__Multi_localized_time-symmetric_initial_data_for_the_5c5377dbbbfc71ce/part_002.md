---
retention_scope: session
part: 2
total_parts: 3
---

[Part 2/3 of: [2301.08238] Multi–localized time-symmetric initial data for the Einstein vacuum equations]

We now apply the argument in the proof of Theorem 1.3, but instead of using a Schwarzchild as the interior metric for the Brill-Lindquist exterior, we use the metrics $u_{\theta}^{4} g_{\theta}$ considered here. As such, the computations from the proof of Theorem 1.1 are slightly modified as follows.

Let $m_{i}=m$ for all $i \in \mathbb{Z}_{+}$. There is a sequence $\mathfrak{p}$ as in Section 3 and a $0<\xi<\frac{1}{2}$, such that for any $\theta \in J_{\xi}^{\prime}:=[1-\xi, 1+\xi]$, the metric
$$\widetilde{g}_{i j}(x)=(1-\psi(x))\left(u_{\theta}^{4}(x) g_{\theta}\right)_{i j}(x)+\psi(x)\left(g_{B L}^{\mathfrak{m}, \mathfrak{p}}\right)_{i j}(x) .$$
is sufficiently near $g_{S}^{m}$ to apply Proposition 2.1 with $\gamma=\widetilde{g}$ to solve for $h(\tilde{g})$, satisfying the conditions therein.

We write
$$\widetilde{g}=(1-\psi) g_{\theta}+\psi g_{S}^{m}+\widehat{h}=: \widehat{g}+\widehat{h},$$
so that $\widehat{h}:=(1-\psi)\left(u_{\theta}^{4}-1\right) g_{\theta}+\psi\left(g_{B L}^{\mathfrak{m}, \mathfrak{p}}-g_{S}^{m}\right)$ and $\widehat{g}=(1-\psi) g_{\theta}+\psi g_{S}^{m}$, which is $(1-\psi) g_{S}^{m / \theta}+\psi g_{S}^{m}$ on the set $\bar{\Omega}=\{x: 1 \leq|x| \leq 2\}$. Now, $R(\widetilde{g}+h(\widetilde{g}))$ vanishes precisely when
$$\int_{\Omega} f^{m} R(\widetilde{g}+h(\widetilde{g})) d \mu_{g_{S}^{m}}=0$$

We note that
$$\begin{aligned}
R(\widetilde{g}+h(\widetilde{g}))= & R(\widehat{g})+L_{\widehat{g}}(\widehat{h}+h(\widetilde{g}))+\mathcal{Q}_{\widehat{g}}(\widehat{h}+h(\widetilde{g})) \\
= & R(\widehat{g})+L_{g_{S}^{m}}(\widehat{h}+h(\widetilde{g})) \\
& +\left(L_{\widehat{g}}-L_{g_{S}^{m}}\right)(\widehat{h}+h(\widetilde{g}))+\mathcal{Q}_{\widehat{g}}(\widehat{h}+h(\widetilde{g}))
\end{aligned}$$

The integral of the term $f^{m} L_{g_{S}^{m}}(h(\widetilde{g}))$ vanishes because $f^{m}$ is in the kernel of $L_{g_{S}^{m}}^{*}$, and $h(\widetilde{g})$ and its derivatives vanish along the boundary.

We can estimate as we did earlier in the proof of Theorem 1.1 and we emphasize the constants in the estimates below are independent of $\theta \in J_{\xi}^{\prime}$ : for some $C>0$,
$$\begin{aligned}
\left|\int_{\Omega} f^{m} L_{g_{S}^{m}}(\widehat{h}) d \mu_{g_{S}^{m}}\right| & \leq C\|\widehat{h}\|_{C^{2}(\Omega)} \\
\left|\mathcal{Q}_{\widehat{g}}(\widehat{h}+h(\widetilde{g}))\right| & \leq C\left(\|\widehat{h}\|_{C^{2}(\Omega)}^{2}+\|h(\widetilde{g})\|_{C^{2}(\Omega)}^{2}\right) \\
\mid\left(L_{\widehat{g}}-L_{\left.g_{S}^{m}\right)}(\widehat{h}+h(\widetilde{g})) \mid\right. & \leq C\left\|g_{S}^{m / \theta}-g_{S}^{m}\right\|_{C^{2}(\Omega)} \cdot\left(\|\widehat{h}\|_{C^{2}(\Omega)}+\|h(\widetilde{g})\|_{C^{2}(\Omega)}\right) \\
\|h(\widetilde{g})\|_{C^{2, \alpha}(\Omega)} & \leq C_{0}\|R(\widetilde{g})\|_{C^{0, \alpha}(\Omega)} \leq C\left(|m-m / \theta|+\|\widehat{h}\|_{C^{2, \alpha}(\Omega)}\right)
\end{aligned}$$

Just as we did in (2.1), we can readily compute
$$\int_{\Omega} f^{m} R(\widehat{g}) d \mu_{g_{S}^{m}}=16 \pi(m-m / \theta)=16 \pi \theta^{-1} m(\theta-1) .$$

Thus we conclude that there is a constant $C>0$ such that
$$\left|\int_{\Omega} f^{m} R(\widetilde{g}+h(\widetilde{g})) d \mu_{g_{S}^{m}}-16 \pi(m-m / \theta)\right| \leq C\left((m-m / \theta)^{2}+\|\widehat{h}\|_{C^{2, \alpha}(\Omega)}\right) .$$
Given $\xi$, we can choose $\mathfrak{p}$ and $\varepsilon$ so that $\|\widehat{h}\|_{C^{2, \alpha}(\Omega)} \leq C\left(\theta^{2} \varepsilon+\xi^{2}\right) \leq C^{\prime} \xi^{2}$. By Proposition 2.1
$$\theta \mapsto \mathcal{J}(\theta):=\int_{\Omega} f^{m} R(\tilde{g}+h(\tilde{g})) d \mu_{g_{S}^{m}}$$
is continuous for $\theta \in J_{\xi}^{\prime}$. For $\xi$ sufficiently small, we then have by the above estimates that $\mathcal{J}(1-\xi) \cdot \mathcal{J}(1+\xi)<0$. Thus by continuity, for some $\theta \in J_{\xi}^{\prime}$, $\mathcal{J}(\theta)=0$, as desired. \(\square\)

Remark 5.1. Employing the above approach in the proof of Theorem 1.3 would only retain the $C^{0}$ estimate on $g_{i j}-\delta_{i j}$.

\section*{6. On the total mass}

For suitably asymptotically flat exterior ends, the ADM mass is given by the following formula:
$$\begin{aligned}
16 \pi m_{\mathrm{ADM}}(g) & =\lim _{r \rightarrow \infty} \int_{\{|x|=r\}} \sum_{i, j=1}^{3}\left(g_{i j, i}-g_{i i, j}\right) \frac{x^{j}}{|x|} d A \\
& =\lim _{r \rightarrow \infty} \int_{\{|x|=r\}} g^{a b}\left(g_{a j, b}-g_{a b, j}\right) \frac{x^{j}}{|x|} d A \\
& =\lim _{r \rightarrow \infty} \int_{\{|x|=r\}} g^{a b}\left(g_{a j, b}-g_{a b, j}\right) \nu_{g} d \sigma_{g},
\end{aligned}$$
where $\nu_{g}$ the outward-pointing hypersurface normal with respect to $g$. The ADM mass is finite when $R(g)$ is integrable on the asymptotically flat end. More precisely, the above defines the ADM energy, one component of the ADM energy-momentum vector, but our time-symmetric setting, the linear momentum vanishes.

We prove the following proposition on the limit of the flux integrals for the data we construct. Given a sequence $\mathfrak{c}=\left(c_{k}\right)_{k \in \mathbb{Z}_{+}}$in $\mathbb{R}^{3}$, we let $B_{k}=\left\{x:\left|x-c_{k}\right|<2\right\}$, and for $r>0$, we then let $B_{k}^{r}=\left\{x:\left|x-c_{k}\right|<r / 10\right\}$, and let $B(r)=\{x:|x|<r\}$. We observe that for $\lambda \geq 1$ and $\mathfrak{c}=\lambda \mathfrak{p}$, where $\mathfrak{p}$ is as defined recursively in Section 3 and for any $r>0$, the sets $\left\{k: B_{k} \cap \partial B(r) \neq \varnothing\right\}$ and $\left\{k: B_{k}^{r} \cap \partial B(r) \neq \varnothing\right\}$ have at most one element in them, and $\left|c_{k}-c_{j}\right| \geq \frac{1}{2}\left|c_{j}\right|$ for all $j<k$.

Proposition 6.1. Consider a metric $g$ constructed according to Theorem 1.3, with mass sequence $\mathfrak{m}$ with $\|\mathfrak{m}\|_{\ell^{\infty}} \leq \varepsilon_{0}$ and corresponding center sequence $\mathfrak{c}=\lambda \mathfrak{p}$, with $\widehat{\delta}_{k}$ as in (3.4) chosen so that $\left(\widehat{\delta}_{k}\right)_{k \in \mathbb{Z}_{+}} \in \ell^{1}$, and with a constant $C>0$ such that for $x \in B_{k}$ and $0 \leq|I| \leq 2,\left|\partial_{x}^{I}\left(g_{i j}(x)-\delta_{i j}\right)\right| \leq C m_{k}$.

In case $\mathfrak{m} \notin \ell^{1}$ and $\#\left\{k: B_{k} \cap \partial B(r) \neq \varnothing\right\}$ is uniformly bounded for $r>0$, then the limit in (6.1) is infinite. As such, we conclude that since $R(g)=0, g$ is not suitably asymptotically flat.

In case $\mathfrak{m} \in \ell^{1}$, then the limit in (6.1) is finite. In this case we have the following:
\begin{itemize}
\item[-] if $\sum_{k \in \mathbb{Z}_{+}} \widehat{\delta}_{k}$ is suitably small, then the limit in (6.1) is strictly positive.
\item[-] if $\#\left\{k: B_{k}^{r} \cap \partial B(r) \neq \varnothing\right\}$ is uniformly bounded for $r>0$, and if for all $j<k,\left|c_{k}-c_{j}\right| \geq \frac{2}{7}\left|c_{j}\right|$, then the limit in (6.1) equals $16 \pi\|\mathfrak{m}\|_{\ell^{1}}$.
\end{itemize}

Proof. Let $\nu$ denote the outward-pointing Euclidean unit normal for a closed hypersurface; for example $\nu=\frac{x-c_{k}}{\left|x-c_{k}\right|}$ for the boundary $\partial B_{k}$.

The metric $g$ is exactly Brill-Lindquist outside of $\bigcup_{k \in \mathbb{Z}_{+}} B_{k}$, where we write $g_{i j}(x)=f(x) \delta_{i j}$, so that $f=\left(1+\sum_{k \in \mathbb{Z}_{+}} f_{k}\right)^{4}$, with $f_{k}(x):=\frac{m_{k}}{2\left|x-c_{k}\right|}$, and for which we readily compute (letting ∇ be the Euclidean gradient)
$$\sum_{a, b, j=1}^{3} g^{a b}\left(g_{a j, b}-g_{a b, j}\right) \frac{x^{j}}{|x|}=\sum_{j=1}^{3}-2 \frac{f_{, j}}{f} \frac{x^{j}}{|x|}=-2(\nabla \log f) \cdot \frac{x}{|x|} .$$

Let $\mathcal{J}(r)=\left\{k: B_{k} \cap B(r) \neq \varnothing\right\}=\mathcal{J}_{1}(r) \cup \mathcal{J}_{2}(r)$, where $\mathcal{J}_{1}(r)=\left\{k: B_{k} \subset B(r)\right\}$ and $\mathcal{J}_{2}(r)=\left\{k: B_{k} \cap \partial B(r) \neq \varnothing\right\}$. Let $\mathcal{B}(r)=\bigcup_{k \in \mathcal{J}(r)} B_{k}$. By the divergence
theorem, then,
$$\begin{aligned}
\frac{1}{16 \pi} & \int_{\{|x|=r\}} \sum_{a, b, j=1}^{3} g^{a b}\left(g_{a j, b}-g_{a b, j}\right) \frac{x^{j}}{|x|} d A \\
= & -\sum_{k \in \mathcal{J}_{1}(r)} \frac{1}{8 \pi} \int_{\partial B_{k}}(\nabla \log f) \cdot \nu d A-\frac{1}{8 \pi} \int_{B(r) \backslash \mathcal{B}(r)} \Delta \log f d x \\
& +\frac{1}{16 \pi} \sum_{k \in \mathcal{J}_{2}(r)} \int_{B(r) \cap B_{k}} \sum_{a, b, j=1}^{3} \partial_{j}\left(g^{a b}\left(g_{a j, b}-g_{a b, j}\right)\right) d x
\end{aligned}$$
Since $\Delta \log f=-\frac{|\nabla f|^{2}}{f^{2}}$, the contribution of the second integral is nonnegative.
We now calculate
$$-\frac{1}{8 \pi} \int_{\partial B_{k}} \nabla \log \left(\left(1+f_{k}\right)^{4}\right) \cdot \nu d A=\frac{m_{k}}{1+m_{k} / 4} \geq \min \left(\frac{m_{k}}{2}, 2\right) .$$

Recall that $f\left(1+f_{k}\right)^{-4}=\left(1+\Theta_{k}\right)^{4}$, where $\Theta_{k}=\sum_{\ell \neq k} \Theta_{\ell k}$ was defined in (3.2). By (3.3)-(3.4), for $\widehat{\delta}_{k}$ small and $1 \leq\left|x-c_{k}\right| \leq 2$,
$$\left|\nabla \log f-\nabla \log \left(\left(1+f_{k}\right)^{4}\right)\right|=4\left|\nabla \log \left(1+\Theta_{k}(x)\right)\right| \leq C^{\prime} \frac{\widehat{\delta}_{k}}{1-C \widehat{\delta}_{k}} \leq C^{\prime \prime} \widehat{\delta}_{k} .$$

Let us first consider the case $\|\mathfrak{m}\|_{\ell^{1}}=\infty$. Since $\mathfrak{m} \in \ell^{\infty}$, the last integral in (6.3) is uniformly bounded, since $\# \mathcal{J}_{2}(r)$ is bounded uniformly for all $r>0$. As $\sum_{\ell} \widehat{\delta}_{\ell}<\infty$, we conclude by (6.3)-(6.5) that
$$\lim _{r \rightarrow \infty} \frac{1}{16 \pi} \int_{\{|x|=r\}} \sum_{a, b, j=1}^{3} g^{a b}\left(g_{a j, b}-g_{a b, j}\right) \frac{x^{j}}{|x|} d A=\infty .$$

As we have shown, it follows from condition (3.4) that $\sum_{\ell} \frac{m_{\ell}}{1+\left|p_{\ell}\right|}$ converges, whence the series $\sum_{k \in \mathbb{Z}_{+}} f_{k}$ converges, uniformly on compacts of $\mathbb{R}^{3} \backslash \mathfrak{c}$, and likewise for the derivative series. As $\nabla f_{k}=-\frac{m_{k} / 2}{\left|x-c_{k}\right|^{2}} \frac{x-c_{k}}{\left|x-c_{k}\right|}$, we have
$$|\nabla \log f|=\frac{|\nabla f|}{f}=\frac{4}{f^{1 / 4}}\left|\sum_{k \in \mathbb{Z}_{+}} \frac{m_{k} / 2}{\left|x-c_{k}\right|^{2}} \frac{x-c_{k}}{\left|x-c_{k}\right|}\right| \leq 2 \sum_{k \in \mathbb{Z}_{+}} \frac{m_{k}}{\left|x-c_{k}\right|^{2}} .$$
For $\mathfrak{m} \in \ell^{1},|\nabla \log f| \in L^{2}\left(\mathbb{R}^{3} \backslash \bigcup_{k \in \mathbb{Z}_{+}} B_{k}\right)$, and so $\Delta \log f \in L^{1}\left(\mathbb{R}^{3} \backslash \bigcup_{k \in \mathbb{Z}_{+}} B_{k}\right)$ (cf. Remark 6.2).

We turn to the case $\mathfrak{m} \in \ell^{1}$, for which we see, recalling $\left|\partial_{x}^{I}\left(g_{i j}(x)-\delta_{i j}\right)\right| \leq C m_{k}$ on $B_{k}$, the last integral in (6.3) tends to 0 in the limit. If in addition $\left(\widehat{\delta}_{k}\right)_{k \in \mathbb{Z}_{+}} \in \ell^{1}$, we conclude from (6.3)-(6.5) that $\lim _{r \rightarrow \infty} \int_{\{|x|=r\}} g^{a b}\left(g_{a j, b}-g_{a b, j}\right) \frac{x^{j}}{|x|} d A$ is finite, and in fact if $\sum_{k \in \mathbb{Z}_{+}} \widehat{\delta}_{k}$ is suitably small, the limit is seen to be strictly positive.

Finally, we let $\mathcal{\partial}_{3}(r)=\left\{k: B_{k}^{r} \cap \partial B(r) \neq \varnothing\right\}$. We consider $r \geq 20$ so that $B_{k}^{r} \supset B_{k}$. By assumption, if $j \neq k$ and $\min \left\{\left|c_{j}\right|,\left|c_{k}\right|\right\} \geq \frac{7 r}{10}$, then $\left|c_{k}-c_{j}\right| \geq \frac{r}{5}$. As such, if $k \in \mathcal{J}_{3}(r)$ and if $j \neq k$, then $B_{j}^{r} \cap B_{k}^{r}=\varnothing$. Let $\Sigma_{r}$ be the boundary of
$B(r) \backslash \bigcup_{k \in \mathcal{J}_{3}(r)} B_{k}^{r}$. Then we have
$$\begin{aligned}
& \frac{1}{16 \pi} \int_{\{|x|=r\}} \sum_{a, b, j=1}^{3} g^{a b}\left(g_{a j, b}-g_{a b, j}\right) \frac{x^{j}}{|x|} d A \\
& =-\frac{1}{8 \pi} \int_{\Sigma_{r}}(\nabla \log f) \cdot \nu d A-\frac{1}{8 \pi} \int_{\bigcup_{k \in \mathcal{J}_{3}(r)}\left(B(r) \cap\left(B_{k}^{r} \backslash B_{k}\right)\right)} \Delta \log f d x \\
& \quad+\frac{1}{16 \pi} \sum_{k \in \mathcal{J}_{3}(r)} \int_{B(r) \cap B_{k}} \sum_{a, b, j=1}^{3} \partial_{j}\left(g^{a b}\left(g_{a j, b}-g_{a b, j}\right)\right) d x .
\end{aligned}$$
Since $\Delta \log f=-\frac{|\nabla f|^{2}}{f^{2}} \in L^{1}\left(\mathbb{R}^{3} \backslash \bigcup_{k \in \mathbb{Z}_{+}} B_{k}\right)$ as shown above, we see the second integral tends to 0 in the limit. As above, the final integral above tends to 0 in the limit, since $\mathfrak{m} \in \ell^{1}$ and $\left|\partial_{x}^{I}\left(g_{i j}(x)-\delta_{i j}\right)\right| \leq C m_{k}$ on $B_{k}$.

As for the first term, we have $\nabla \log f=\frac{4}{f^{1 / 4}} \sum_{k \in \mathbb{Z}_{+}} \nabla f_{k}$. For any $\delta>0$, there is an $N$ such that $\sum_{\ell \geq N+1} m_{\ell}<\delta$, and then for $r \geq R$ sufficiently large, $\sum_{\ell \leq N} f_{\ell}<\delta$ on $\Sigma_{r}$. Thus given $\varepsilon>0$, there is an $R$ such that for all $r \geq R,\left|f^{-1 / 4}-1\right| \leq \varepsilon$ on $\Sigma_{r}$. Since $\varepsilon$ is arbitrary, it follows that
$$\lim _{r \rightarrow \infty}-\frac{1}{8 \pi} \int_{\Sigma_{r}} \frac{4}{f^{1 / 4}} \nabla f_{k} \cdot \nu d A=m_{k}$$
On the other hand, by the bound on $\# \mathcal{J}_{3}(r)$, there is a constant $C>0$ so that the area of $\Sigma_{r}$ is at most $C r^{2}$. As such, $\int_{\Sigma_{r}}\left|x-c_{k}\right|^{-2} d A$ is uniformly bounded for $k \in \mathbb{Z}_{+}$and $r \geq 20$, and using $\mathfrak{m} \in \ell^{1}$ together with (6.6, we can conclude the limit in (6.7) is $\|\mathfrak{m}\|_{\ell^{1}}$ as desired. \(\square\)

Remark 6.2. It is interesting to note that having $\mathfrak{m} \in \ell^{2}$ is the most natural condition in order to ensure $\Delta \log f=-f^{-2}|\nabla f|^{2} \in L^{1}\left(R^{3} \backslash \bigcup_{k \in \mathbb{Z}_{+}} B_{k}\right)$ in our setting, as the localization makes the contributions of the $\left|\nabla f_{k}\right|$ almost $L^{2}$-orthogonal. Indeed, setting $\mathcal{R}=\mathbb{R}^{3} \backslash \bigcup_{k \in \mathbb{Z}_{+}} B_{k}$, we have that each function $\left|\nabla f_{k}\right|=\frac{m_{k}}{\left|x-c_{k}\right|^{2}}$ is in $L^{2}(\mathcal{R})$. Moreover, we have that (where $A \lesssim B$ when $A \leq C B$ for some constant $C$ )
$$\int_{\left\{\left|x-c_{k}\right| \geq 2\right\} \cap\left\{\left|x-c_{j}\right| \geq 2\right\}} \frac{1}{\left|x-c_{k}\right|^{2}\left|x-c_{j}\right|^{2}} d x \lesssim \frac{1}{1+\left|c_{k}-c_{j}\right|} \lesssim 2^{-|j-k|} .$$
This means that for $j \neq k,\left|\nabla f_{k}\right|$ and $\left|\nabla f_{j}\right|$ are almost $L^{2}$-orthogonal. Thus, we have that
$$\|\nabla \log f\|_{L^{2}(\mathcal{R})}^{2} \lesssim \int_{\mathcal{R}} \sum_{j \geq 1} \sum_{k \geq 1}\left|\nabla f_{j}\right|\left|\nabla f_{k}\right| d x \lesssim \sum_{j \geq 1} \sum_{k \geq 1} m_{j} m_{k} 2^{-|j-k|} \leq 3\|\mathfrak{m}\|_{\ell^{2}}^{2}$$
since
$$\begin{aligned}
\sum_{j \geq 1} \sum_{k \geq 1} m_{j} m_{k} 2^{-|j-k|} & =\|\mathfrak{m}\|_{\ell^{2}}+\sum_{k \geq 1} \sum_{j>k} 2 m_{j} m_{k} 2^{-j+k} \\
& \leq\|\mathfrak{m}\|_{\ell^{2}}+\sum_{j=2}^{\infty} m_{j}^{2} \sum_{k=1}^{j-1} 2^{-j+k}+\sum_{k \geq 1} m_{k}^{2} \sum_{j>k} 2^{-j+k} \leq 3\|\mathfrak{m}\|_{\ell^{2}} .
\end{aligned}$$

We remark that the above estimate uses that the points $c_{k}$ move away from each other geometrically. If the points move away more slowly, the orthogonality will be weaker, and the argument may require that $\mathfrak{m} \in \ell^{p}$ for some $p<2$ in order to compensate for this.
6.1. On the Hamiltonian. Since the data we construct may fail to be asymptotically flat, one might question what the mass integrals even mean in this context. For an interpretation, we consider the evolution of our initial data into a spacetime, expressed in lapse-shift form on a spacetime open set $\mathcal{S}$ as
$$\bar{g}=-N^{2} d t^{2}+g_{i j}\left(d x^{i}+X^{i} d t\right) \otimes\left(d x^{j}+X^{j} d t\right) .$$
The Einstein-Hilbert action is then $\int_{\mathcal{S}} R(\bar{g}) d \mu_{\bar{g}}$. Recasting this in Hamilonian form leads one, after what is by now a classical computation, to the Hamiltonian (up to a multiple of by a constant to get dimensions of energy, which we take to be $\frac{1}{16 \pi}$ )
$$\int_{\mathbb{R}^{3}}\left(-N\left(R(g)-|K|_{g}^{2}+\left(\operatorname{tr}_{g} K\right)^{2}\right)+2 X \cdot \operatorname{div}_{g}\left(K-\left(\operatorname{tr}_{g} K\right)\right) d \mu_{g}\right.$$
where our convention is that as a linear operator on each $T_{p} \mathbb{R}^{3}, K$ corresponds to the shape operator $-\nabla_{\bar{g}} n$, with $n$ the future-pointing unit normal. As such, a simple computation shows the evolution for $g$ is $\frac{\partial g_{i j}}{\partial t}=-2 N K_{i j}+X_{i ; j}+X_{j ; i}$. For this to yield the same form of the equations of motion in both the setting of a closed initial slice and the setting here, we have to analyze the contribution of certain boundary terms in the analysis of the linearization of the Hamiltonian, namely those coming from the linearization $L_{g}$ of the scalar curvature operator, and from the divergence of the variation of the momentum tensor $K-\operatorname{tr}_{g} K$. For simplicity we work in Fermi coordinates so that $N=1$ and $X=0$, in which case the term to analyze for boundary contributions ("at infinity" here) is just $\int_{\mathbb{R}^{3}}-L_{g} h d \mu_{g}$, where we consider $h$ such that $h$ and $\partial h$ tending to zero as $r$ grows without bound. Should there be any contribution from infinity, we can just modify the Hamiltonian by subtracting off the appropriate term. As such, the term to add comes from an analysis of $\int_{\mathbb{R}^{3}} L_{g} h d \mu_{g}$.

Let $g$ be one of the metrics constructed in Theorem 1.3, with $\mid \partial_{x}^{I}\left(g_{i j}(x)-\delta_{i j} \mid \leq\right.$ $C m_{k}$ on each $B_{k}$, and with $\# \mathcal{J}_{2}(r)$ uniformly bounded for $r>0$, where again $\mathcal{J}_{2}(r)=\left\{k: B_{k} \cap \partial B(r) \neq \varnothing\right\}$, and $\mathcal{B}_{2}(r)=\bigcup_{k \in \mathcal{J}_{2}(r)} B_{k}$. As $L_{g} h=-\Delta_{g}\left(\operatorname{tr}_{g} h\right)+$ $\operatorname{div}_{g} \operatorname{div}_{g} h-h \cdot \operatorname{Ric}(g)$, upon integrating over a large coordinate ball, we get the boundary term
$$\int_{\{|x|=r\}}\left(-g^{i k} h_{i k ; j}+g^{i k} h_{i j ; k}\right) \cdot \nu_{g}^{j} d \sigma_{g} .$$
Since $h$ and $\partial h$ decay to 0, then since $\mathfrak{m} \in \ell^{\infty}$ and $\# \mathcal{J}_{2}(r)$ is bounded, we see
$$\lim _{r \rightarrow \infty} \int_{\{|x|=r\} \cap \mathcal{B}_{2}(r)}\left(-g^{i k} h_{i k ; j}+g^{i k} h_{i j ; k}\right) \cdot \nu_{g}^{j} d \sigma_{g}=0 .$$

Now on $\Sigma_{r}^{\prime}:=\{|x|=r\} \backslash \mathcal{B}_{2}(r)$, the metric is given by $g_{i j}=f \delta_{i j}$ as above, and so $d \sigma_{g}=f d A$ and the unit normal is $\nu_{g}=\nu / \sqrt{f}$, so that the integral becomes
$$\begin{aligned}
\int_{\Sigma_{r}^{\prime}} \sum_{i, j}( & -f^{-1}\left(h_{i i, j}-\sum_{k}\left(\Gamma_{j i}^{k} h_{k i}+\Gamma_{i j}^{k} h_{i k}\right)\right) \frac{x^{j}}{|x|} \sqrt{f} d A \\
& +\int_{\Sigma_{r}^{\prime}} \sum_{i, j}\left(f^{-1}\left(h_{i j, i}-\sum_{k}\left(\Gamma_{i i}^{k} h_{k j}+\Gamma_{i j}^{k} h_{i k}\right)\right) \frac{x^{j}}{|x|} \sqrt{f} d A\right. \\
= & \int_{\Sigma_{r}^{\prime}} \sum_{i, j}\left(h_{i j, i}-h_{i i, j}\right) f^{-1 / 2} \frac{x^{j}}{|x|} d A \\
& +\int_{\Sigma_{r}^{\prime}} \sum_{i, j, k}\left(-\Gamma_{i i}^{k} h_{k j}+\Gamma_{i j}^{k} h_{i k}\right) f^{-1 / 2} \frac{x^{j}}{|x|} d A
\end{aligned}$$
where $\Gamma_{i j}^{k}=\frac{1}{2} f^{-1}\left(\delta_{i k} f_{, j}+\delta_{j k} f_{, i}-\delta_{i j} f_{, k}\right)$, so that $\Gamma_{i i}^{k}=\frac{1}{2} f^{-1}\left(2 \delta_{i k} f_{, i}-f_{, k}\right)$.
In order to estimate the second integral, we estimate $\int_{\Sigma_{r}^{\prime}} f^{-1}|\nabla f| d A$. With (6.6) in mind, we claim for $\mathfrak{m} \in \ell^{1}$, and with suitable decay on $h$, the second integral above limits to 0. Indeed, for $k \in \mathcal{J}_{2}(r)$, let $\gamma=\left|c_{k}\right| / r$, so $1-2 r^{-1}<\gamma<1+2 r^{-1}$. Then, we note that
$$\left|x-c_{k}\right|^{2}=|x|^{2}+\left|c_{k}\right|^{2}-2|x|\left|c_{k}\right| \cos \phi,$$
where $\phi$ is the angle between $x$ and $c_{k}$. Working in spherical coordinates, one then readily computes the integral
$$\int_{\{|x|=r\} \backslash B_{k}}\left|x-c_{k}\right|^{-2} d A=2 \pi \int_{\phi_{1}}^{\pi} \frac{\sin \phi}{1+\gamma^{2}-2 \gamma \cos \phi} d \phi=2 \pi \gamma^{-1} \log ((1+\gamma) r / 2),$$
where $\cos \phi_{1}=\frac{1+\gamma^{2}-4 r^{-2}}{2 \gamma}$. If $k \notin \mathcal{J}_{2}(r)$, then with $\gamma=\left|c_{k}\right| / r$ (so that $\gamma>1+2 r^{-1}$ or $\gamma<1-2 r^{-1}$ ), and assuming $c_{k} \neq 0$ (else the integral below evaluates to $4 \pi$ ), we have
$$\begin{aligned}
\int_{\{|x|=r\}}\left|x-c_{k}\right|^{-2} d A & =2 \pi \int_{0}^{\pi} \frac{\sin \phi}{1+\gamma^{2}-2 \gamma \cos \phi} d \phi \\
& =\left.\pi \gamma^{-1} \log \left(1+\gamma^{2}-2 \gamma \cos \phi\right)\right|_{0} ^{\pi} \\
& =2 \pi \gamma^{-1} \log \left(\frac{1+\gamma}{|1-\gamma|}\right) \leq 4 \pi \log (r+1),
\end{aligned}$$
for $r \geq 4$.
For example, then, using (6.6), the bound on $\# \mathcal{J}_{2}(r)$ and $\mathfrak{m} \in \ell^{1}$, and if we assume $\lim _{|x| \rightarrow \infty}\left|h_{i j}(x)\right| \log |x|=0$, for all $i$ and $j$, we conclude as desired.

We can recast the condition $\lim _{|x| \rightarrow \infty}\left|h_{i j}(x)\right| \log |x|=0$ in an equivalent and manifestly translation-invariant form $\sup _{p \in \mathbb{R}^{3}} \lim _{|x| \rightarrow \infty}\left|h_{i j}(x)\right| \log |x-p|=0$. Another translation-invariant condition that one might naturally impose would be $h \in W^{1, p}\left(\mathbb{R}^{3}\right)$, for some $1 \leq p<\infty$. Indeed, this condition allows us to show that
the final integral in (6.9) tends to 0 as $|x| \rightarrow \infty$. For any $h \in W^{1, p}\left(\mathbb{R}^{3}\right)$, given $\varepsilon>0$, for sufficiently large $R$
$$\int_{\{|x| \geq R\}}\left(\left|h_{i j}(x)\right|^{p}+\left|\partial h_{i j}(x)\right|^{p}\right) d x \leq \varepsilon .$$
Assuming for the moment that $h$ is smooth, then for any $r_{2}>r_{1} \geq 1$, with $\omega \in \mathbb{S}^{2}$, the unit sphere with round unit metric $\stackrel{\circ}{g}$, we have (applying Hölder's inequality)
$$\begin{aligned}
& \left.\left|\int_{\left\{|x|=r_{2}\right\}}\right| h_{i j}(x)\right|^{p} d A-\int_{\left\{|x|=r_{1}\right\}}\left|h_{i j}(x)\right|^{p} d A\left|=\left|\int_{\mathbb{S}^{2}} \int_{r_{1}}^{r_{2}} \frac{\partial}{\partial r}\left(\left|h_{i j}(r \omega)\right|^{p} r^{2}\right) d r d \sigma_{g}\right|\right. \\
& \leq \int_{\left\{r_{1} \leq|x| \leq r_{2}\right\}} p\left|h_{i j}(x)\right|^{p-1}\left|\partial_{r} h_{i j}(x)\right| d x+\int_{\left\{r_{1} \leq|x| \leq r_{2}\right\}} 2|x|^{-1}\left|h_{i j}(x)\right|^{p} d x \\
& \leq p\left(\int_{\left\{r_{1} \leq|x| \leq r_{2}\right\}}\left|h_{i j}(x)\right|^{p} d x\right)^{(p-1) / p}\left(\int_{\left\{r_{1} \leq|x| \leq r_{2}\right\}}\left|\partial_{r} h_{i j}(x)\right|^{p} d x\right)^{1 / p} \\
& \quad+2 \int_{\left\{r_{1} \leq|x| \leq r_{2}\right\}}\left|h_{i j}(x)\right|^{p} d x .
\end{aligned}$$
By density of smooth functions in $W^{1, p}\left(\mathbb{R}^{3}\right)$, the above estimate holds for almost every $r \geq 1$, and actually applying the Sobolev trace theorem, it can be construed to hold for all $r$. Thus we conclude $\lim _{r \rightarrow \infty} \int_{\{|x|=r\}}\left|h_{i j}(x)\right|^{p} d A$ exists, from which we further conclude this limit must vanish.

Now, given some $k \in \mathcal{J}_{2}(r)$, and with $\gamma$ defined as above, we can once again work in spherical coordinates, giving us that (where again $\cos \phi_{1}=\frac{1+\gamma^{2}-4 r^{-2}}{2 \gamma}$ )
$$\int_{\{|x|=r\} \backslash B_{k}}\left|x-c_{k}\right|^{-2 q} d A=2 \pi \int_{\phi_{1}}^{\pi} \frac{\sin \phi}{r^{2(q-1)}\left(1+\gamma^{2}-2 \gamma \cos \phi\right)^{q}} d \phi \leq C_{q}$$
for $q>1$; we also note that $\left\|\left|x-c_{k}\right|^{-2}\right\|_{L^{\infty}\left(\Sigma_{r}^{\prime}\right)} \leq 1 / 4$. By taking $q$ such that $\frac{1}{p}+\frac{1}{q}=1$ and using Holder's inequality, the last integral in (6.9) is bounded above by
$$C_{p}^{\prime}\|h\|_{L^{p}(\{|x|=r\})} \rightarrow 0$$
where $C_{p}^{\prime}$ is some constant depending on $p$, as desired. We note that replacing the pointwise decay assumptions on $h$ and $\partial h$ with $h \in W^{2, p}\left(\mathbb{R}^{n}\right)$, for some $1 \leq p<\infty$, we could similarly handle the limit in (6.8).

The same analysis shows that the linearization of
$$\lim _{r \rightarrow \infty} \int_{\{|x|=r\}} g^{a b}\left(g_{a j, b}-g_{a b, j}\right) \nu_{g} d \sigma_{g}$$
about a metric of the type we have constructed gives the desired limiting term.
Using $\mathfrak{m} \in \ell^{1}$, we see $f$ on $\Sigma_{r}^{\prime}$ tends to 1 as $r$ grows without bound. Thus the limiting term we must add is thus seen to be
$$\frac{1}{16 \pi} \lim _{r \rightarrow \infty} \int_{\{|x|=r\}} g^{a b}\left(g_{a j, b}-g_{a b, j}\right) \frac{x^{j}}{|x|} d A=\frac{1}{16 \pi} \lim _{r \rightarrow \infty} \int_{\{|x|=r\}}\left(g_{i j, i}-g_{i i, j}\right) \frac{x^{j}}{|x|} d A .$$

As such, under the conditions in Proposition 6.1 the mass of the metric can be identified with $\|\mathfrak{m}\|_{\ell^{1}}$, as shown above.

The total mass (energy) of a spacetime is typically associated to isolated systems and computed on a spacelike hypersurface which is suitably asymptotically flat (or hyperboloidal). We have argued that for the metrics constructed in Theorem 1.3, which tend to fail to be asymptotically flat, one can interpret the "sum of masses" $\|\mathfrak{m}\|_{\ell^{1}}$ as a suitable notion of mass. While the computations presented in this section are tailored to the specific metrics we have constructed in Theorem 1.3, they do suggest that there may be an interesting class of metrics extending beyond the asymptotically flat regime which still admits a useful notion of mass-energy.

\section*{Appendix A. On the proof of Proposition 2.1}

Recall $\Omega=\left\{x \in \mathbb{R}^{3}: 1<|x|<2\right\}$ and the definition of the rotationally symmetric bump function $\zeta$ above, and we let $\dot{g}$ be the Euclidean metric with $\stackrel{\circ}{g}_{i j}=\delta_{i j}$ in the coordinates $x$.

We will prove the following extension of Proposition 2.1 To facilitate the statement, we extend some notation: let $k_{0}=4$, and for $m>0$, let $k_{m}=1$. We now consider $g_{S}^{m}$ for $m \geq 0$, where we note $g_{S}^{0}=\stackrel{\circ}{g}$ is the Euclidean metric. For $m>0, f^{m}(x)=\frac{1-\frac{m}{2|x|}}{1+\frac{m}{2|x|}}$ spans the one-dimensional kernel of $L_{g_{S}^{m}}^{*}$, whereas $\operatorname{ker}\left(L_{\bar{g}}^{*}\right)=\operatorname{span}\left\{1, x^{2}, x^{2}, x^{3}\right\}$. So we let $f^{0}=\left\langle 1, x^{1}, x^{2}, x^{3}\right\rangle$, in order that we can express a general element of $\operatorname{ker}\left(L_{\tilde{g}}^{*}\right)$ as $b f^{m}$, with $b \in \mathbb{R}^{k_{m}}$ : in case $m=0, b f^{0}$ is the dot product.

Remark A.1. While we only require $m \geq 0$ for our applications, for $m<0$, note that $\left(g_{S}^{m}\right)_{i j}(x)=\left(1+\frac{m}{2|x|}\right)^{4} \delta_{i j}$ is a scalar-flat metric on the region $|x|>-m / 2$, and the kernel of $L_{g_{S}^{m}}^{*}=\operatorname{span}\left\{f^{m}\right\}$ has dimension $k_{m}=1$. The results in this section are formulated on $\Omega$, and apply equally well to the case $m>-2$.

Proposition A.2. Let $\Omega^{\prime}$ be open and compactly contained in $\Omega$. There is a constant $C_{0}>0$ such that for smooth metrics $\gamma$ sufficiently near $g_{S}^{m}$ in $C^{4, \alpha}(\bar{\Omega})$ and with scalar curvature $R(\gamma)$ supported in $\overline{\Omega^{\prime}}$, there exists a constant $b(\gamma) \in \mathbb{R}^{k_{m}}$ along with a smooth symmetric tensor $h=h(\gamma)$ (which extends smoothly by 0 outside $\Omega$ ), so that $\gamma+h(\gamma)$ is a metric with $R(\gamma+h(\gamma))=b(\gamma) \zeta f^{m}$. Moreover, $h(\gamma)$, and $b(\gamma)$ depend continuously on $\gamma$, with estimates $\|h(\gamma)\|_{C^{2, \alpha}} \leq C_{0}\|R(\gamma)\|_{C^{0, \alpha}}$, and $\left\|\left(h\left(\gamma_{1}\right), b\left(\gamma_{1}\right)\right)-\left(h\left(\gamma_{2}\right), b\left(\gamma_{2}\right)\right)\right\|_{C^{2, \alpha} \times \mathbb{R}^{k_{m}}} \leq C_{0}\left\|\gamma_{1}-\gamma_{2}\right\|_{C^{4, \alpha}}$. Furthermore for each $k \in \mathbb{Z}_{+}$there is a $C_{k}>0$ such that $\|h(\gamma)\|_{C^{k+2, \alpha}} \leq C_{k}\|R(\gamma)\|_{C^{k, \alpha}}$.

In case $\gamma$ is parity-symmetric, $h(\gamma)$ is parity-symmetric as well.
We briefly recall the strategy for proving this result, which is then carried out in the rest of the Appendix. Our goal is to solve for a metric with vanishing scalar curvature modulo the kernel of the adjoint of the linearized scalar curvature operator around a given metric. This will be done by iteration, repeatedly solving the equation linearized around a fixed metric (see Section A.6). In order to do this, we must effectively solve the linearized equation. This is carried out in Section A. 5 using Hilbert space methods. However, we want to solve the linearized equation in such a way that this procedure does not change the metric in the exterior of $\Omega$. Having nontrivial compact solutions of this kind is not possible for elliptic equations in general, but in this case, we can construct such solutions by leveraging the underdetermined nature of the equations. From a technical viewpoint, there is
an elliptic estimate which does not contain boundary terms (see Section A.1), and this estimate allows us to work in spaces which have weights that vanish, dual to spaces with weights that blow up, at all orders as we approach the boundary of $\Omega$ (see Sections A. 2 through A.4). Working in these spaces naturally localizes the gluing to $\Omega$, as desired.
A.1. Basic injectivity estimates. We prove two basic injectivity estimates for $L_{g}^{*}$ for metrics $g$ near $g_{S}^{m}$, on suitable spaces transverse to $\operatorname{ker}\left(L_{g_{S}^{m}}^{*}\right)$ on $\Omega$. For $\varepsilon \in[0,1)$, we let $\Omega_{\varepsilon}=\left\{x \in \mathbb{R}^{3}: 1+\varepsilon<|x|<2-\varepsilon\right\}$.

Lemma A.3. Suppose $S \subset L^{2}\left(\Omega, g_{S}^{m}\right)$ is a subspace so that $L^{2}\left(\Omega, g_{S}^{m}\right)=S \oplus$ $\operatorname{ker}\left(L_{g_{S}^{m}}^{*}\right)$. There is a $C^{2}(\bar{\Omega})$-neighborhood $\mathcal{U}$ of $g_{S}^{m}$ and a $C>0$ so that for all $g \in \mathcal{U}$ and for all $u \in H^{2}(\Omega, g) \cap S$,
$$\|u\|_{H^{2}(\Omega, g)} \leq C\left\|L_{g}^{*} u\right\|_{L^{2}(\Omega, g)} .$$
Proof. Since $\operatorname{tr}_{g}\left(L_{g}^{*} u\right)=-(n-1) \Delta_{g} u-u R(g)$, we see immediately that there is a $C>0$ and a $C^{2}(\bar{\Omega})$-neighborhood $\mathcal{U}_{0}$ of $g_{S}^{m}$ so that for all $g \in \mathcal{U}_{0}$, for all $u \in H^{2}(\Omega, g)$, and for all $\varepsilon \in[0,1)$,
$$\left\|\operatorname{Hess}_{g} u\right\|_{L^{2}\left(\Omega_{\varepsilon}, g\right)} \leq C\left(\left\|L_{g}^{*} u\right\|_{L^{2}\left(\Omega_{\varepsilon}, g\right)}+\|u\|_{L^{2}\left(\Omega_{\varepsilon}, g\right)}\right) .$$
We can choose such a $C \geq 1$, and hence
$$\|u\|_{H^{2}\left(\Omega_{\varepsilon}, g\right)} \leq C\left(\left\|L_{g}^{*} u\right\|_{L^{2}\left(\Omega_{\varepsilon}, g\right)}+\|u\|_{H^{1}\left(\Omega_{\varepsilon}, g\right)}\right) .$$

If (A.1) fails, there is a sequence $g_{i} \in \mathcal{U}_{0}, g_{i} \rightarrow g_{S}^{m}$ in $C^{2}(\bar{\Omega})$, and a sequence $u_{i} \in$ $H^{2}\left(\Omega, g_{i}\right) \cap S$ such that $\left\|u_{i}\right\|_{H^{2}\left(\Omega, g_{i}\right)}=1$ but $\left\|L_{g_{i}}^{*} u_{i}\right\|_{L^{2}\left(\Omega, g_{i}\right)} \rightarrow 0$. Thus there are $0<\beta_{1}<1<\beta_{2}$ such that $\beta_{1} \leq\left\|u_{i}\right\|_{H^{2}\left(\Omega, g_{S}^{m}\right)} \leq \beta_{2}$; moreover, $\left\|L_{g_{S}^{m}}^{*} u_{i}\right\|_{L^{2}\left(\Omega, g_{S}^{m}\right)} \rightarrow$ 0 . By the Rellich Lemma and (A.2) on $\Omega$ with $g=g_{S}^{m}$, applied to differences $u_{i}-u_{j}$, we have that $u_{i}$ converges to some $u \in H^{2}\left(\Omega, g_{S}^{m}\right)$, with $\|u\|_{H^{2}\left(\Omega, g_{S}^{m}\right)} \geq \beta$, and $L_{g_{S}^{m}}^{*} u=0$. Moreover, $u \in S$ as well, since $S$ is closed. Thus we have a contradiction. \(\square\)

Remark A.4. If $\widetilde{m}$ is sufficiently close to $m$, then $g_{S}^{\widetilde{m}} \in \mathcal{U}$ We remark that for $u \in$ $L^{2}(\Omega, g), u \in H^{2}(\Omega, g)$ if and only if $L_{g}^{*} u \in L^{2}(\Omega, g)$. Furthermore, $f \in H^{2}(\Omega, g)$ if and only if $f \in H^{2}\left(\Omega, g_{S}^{m}\right)$, and moreover one gets an equivalent estimate if one changes the metric used for the $H^{2}$ and $L^{2}$ norms.

Remark A.5. For $c \in \mathbb{R}^{3}$, let $\varphi_{c}(x)=x-c$, and $c+\Omega=\{x: 1<|x-c|<2\}$, so that $\varphi_{c}:(c+\Omega) \rightarrow \Omega$. Let $g_{S}^{m, c}=\varphi_{c}^{*}\left(g_{S}^{m}\right)$, i.e. $\left(g_{S}^{m, c}\right)_{i j}(x)=\left(1+\frac{m}{2|x-c|}\right)^{4} \delta_{i j}$. Then for $m>0$, the kernel of $L_{g_{S}^{m, c}}^{*}$ is spanned by $f^{m, c}$, where $f^{m, c}(x)=f^{m} \circ \varphi_{c}(x)=$ $f^{m}(x-c)$, and similarly for $m=0$. Furthermore, let $S_{c}$ and $\mathcal{U}_{c}$ be the pullbacks of $S$ and $\mathcal{U}$ under $\varphi_{c}$; note $g_{S}^{m, c} \in \mathcal{U}_{c}$ and $L^{2}\left(c+\Omega, g_{S}^{m, c}\right)=S_{c} \oplus \operatorname{span}\left(f^{m, c}\right)$. Then (A.1) holds for all $g \in \mathcal{U}_{c}$ and $u \in H^{2}(c+\Omega, g) \cap S_{c}$.

Given $\mathfrak{m}=\left(m_{k}\right)_{k \in \mathbb{Z}_{+}}$with $m_{k}>0$ and suitably chosen $\mathfrak{c}$, if we now let $\widetilde{\mathcal{U}}^{k}$ be the corresponding neighborhoods for $m=\widetilde{m}_{k}$ on $\Omega$, the calculations in Section 3 show that if for each $k, \widetilde{m}_{k}$ is close enough to $m_{k}, g_{B L}^{\mathfrak{m}, \mathfrak{c}} \in \bigcap_{k \in \mathbb{Z}_{+}} \widetilde{\mathcal{U}}_{c_{k}}^{k}$. For the case of finitely many points, it suffices that $\widetilde{\mathfrak{m}}$ is close to $\mathfrak{m}$ and $\left|c_{k}-c_{\ell}\right| \geq 5$ for $k \neq \ell$.

Lemma A.6. Let $\gamma$ be a metric in $C^{0}(\bar{\Omega})$. Let $S_{\gamma}$ be the $L^{2}(\Omega, \gamma)$-orthogonal complement of $\left(\zeta \operatorname{ker}\left(L_{g_{S}^{m}}^{*}\right)\right)$. There is a $C^{2}(\bar{\Omega})$-neighborhood $\mathcal{U}$ of $g_{S}^{m}$ and a $C>0$ so that for all $\varepsilon \in\left[0, \frac{1}{8}\right]$, for all $g \in \mathcal{U}$ and for all $u \in H^{2}(\Omega, g) \cap S_{\gamma}$, we have
$$\|u\|_{H^{2}\left(\Omega_{\varepsilon}, g\right)} \leq C\left\|L_{g}^{*} u\right\|_{L^{2}\left(\Omega_{\varepsilon}, g\right)} .$$
Proof. We first recall (cf. [24, Ch. 7]) that there is a constant $D>0$ and for each $\varepsilon \in\left[0, \frac{1}{8}\right]$ an extension operator $E_{\varepsilon}: H^{2}\left(\Omega_{\varepsilon}, \stackrel{\circ}{g}\right) \rightarrow H^{2}(\Omega, \stackrel{\circ}{g})$ such that for all $u \in H^{2}\left(\Omega_{\varepsilon}, \stackrel{\circ}{g}\right)$,
$$\left\|E_{\varepsilon}(u)\right\|_{H^{2}(\Omega, \stackrel{\circ}{g})} \leq D\|u\|_{H^{2}\left(\Omega_{\varepsilon}, \stackrel{\circ}{g}\right)} .$$
We conclude that we can choose $D>0$ and a neighborhood $\mathcal{U}_{0}$ of $g_{S}^{m}$ so that the extension operator satisfies the estimate (A.4) with $\stackrel{\circ}{g}$ replaced by $g \in \mathcal{U}_{0}$.

The preceding lemma handles the case $\varepsilon=0$, So if the claim fails, there is a sequence $g_{i} \rightarrow g_{S}^{m}$ in $C^{2}(\bar{\Omega})$ and $\varepsilon_{i} \in\left(0, \frac{1}{8}\right]$ as well as $u_{i} \in H^{2}\left(\Omega, g_{i}\right) \cap S_{\gamma}$ such that
$$\left\|u_{i}\right\|_{H^{2}\left(\Omega_{\varepsilon_{i}}, g_{i}\right)}>i\left\|L_{g_{i}}^{*} u_{i}\right\|_{L^{2}\left(\Omega_{\varepsilon_{i}}, g_{i}\right)} .$$
Let $u_{\varepsilon_{i}}=E_{\varepsilon_{i}}\left(\left(u_{i}\right) \upharpoonright_{\Omega_{\varepsilon_{i}}}\right)$. We can rescale to arrange $1=\left\|u_{\varepsilon_{i}}\right\|_{H^{2}\left(\Omega, g_{i}\right)}$, and so it follows that $\left\|L_{g_{i}}^{*} u_{i}\right\|_{L^{2}\left(\Omega_{\varepsilon_{i}}, g_{i}\right)} \rightarrow 0$. There are constants $0<\beta_{1}<\beta_{2}$ with $\beta 1 \leq\left\|u_{\varepsilon_{i}}\right\|_{H^{2}\left(\Omega, g_{S}^{m}\right)} \leq \beta_{2}$. In particular, then, $\left\|u_{i}\right\|_{H^{2}\left(\Omega_{\varepsilon_{i}}, g_{S}^{m}\right)} \leq \beta_{2}$, and it follows that $\left\|L_{g_{S}^{m}}^{*} u_{i}\right\|_{L^{2}\left(\Omega_{\varepsilon_{i}}, g_{S}^{m}\right)} \rightarrow 0$.

On the other hand by the estimate (A.4) of the extension operator along with (A.2), we have
$$\left\|u_{\varepsilon_{i}}\right\|_{H^{2}\left(\Omega, g_{S}^{m}\right)} \leq D\left\|u_{i}\right\|_{H^{2}\left(\Omega_{\varepsilon_{i}}, g_{S}^{m}\right)} \leq D C\left(\left\|L_{g_{S}^{m}}^{*} u_{i}\right\|_{L^{2}\left(\Omega_{\varepsilon_{i}}, g_{S}^{m}\right)}+\left\|u_{i}\right\|_{H^{1}\left(\Omega_{\varepsilon_{i}}, g_{S}^{m}\right)}\right) .$$
By applying Banach-Alaoglu, and Rellich's Lemma, we conclude $u_{\varepsilon_{i}}$ converges $H^{2}\left(\Omega, g_{S}^{m}\right)$-weakly to some $u \in H^{2}\left(\Omega, g_{S}^{m}\right)$, and strongly to $u$ in $H^{1}\left(\Omega, g_{S}^{m}\right)$. By the preceding estimate, $u_{\varepsilon_{i}}$ converges to $u$ strongly in $H^{2}\left(\Omega, g_{S}^{m}\right)$, and so we conclude $\|u\|_{H^{2}\left(\Omega, g_{S}^{m}\right)} \geq \beta>0$. Furthermore, $L_{g_{S}^{m}}^{*} u=0$, so $u \in \operatorname{span}\left\{f^{m}\right\}$.

Now, by assumption, for all $i$, and for all $f \in \operatorname{ker}\left(L_{g_{S}^{m}}^{*}\right), \int_{\Omega} u_{i} \zeta f d \mu_{\gamma}=0$. Thus since $\zeta$ vanishes outside $\Omega_{\varepsilon_{i}}$, we conclude $u_{\varepsilon_{i}} \in S_{\gamma}$. Since $S_{\gamma}$ is closed in $L^{2}(\Omega, \gamma)$, we have by the $L^{2}$-convergence that $u \in S_{\gamma}$. Since we also have $u \in \operatorname{ker}\left(L_{g_{S}^{m}}^{*}\right)$, we conclude $u=0$, which is a contradiction. \(\square\)
A.2. Weighted Function Spaces. We will use several weighted function spaces in the analysis, which we recall here.

We first define a weight function $\rho$ on $\Omega$. Let $\dot{\rho}(t)=e^{-\frac{1}{t}}$ for $0<t \leq \frac{1}{16}$, and $\stackrel{\circ}{\rho}(t)=1$ for $t \geq \frac{1}{8}$, with $\stackrel{\circ}{\rho}$ a smooth nondecreasing function supported on $t \geq 0$. For $x \in \Omega$, let $d(x)$ be the Euclidean distance to the boundary $\partial \Omega$, i.e. $d(x)=\min (|x|-1,2-|x|)$. For $x \in \Omega$, let $\rho(x)=\stackrel{\circ}{\rho}(d(x))$. Note that if $\stackrel{\circ}{\nabla}$ is the Euclidean connection, then for $d(x)<\frac{1}{16}, \stackrel{\circ}{\nabla} \rho(x)=(d(x))^{-2} \rho(x) \stackrel{\circ}{\nabla} d(x)$. By induction, we have that for $k \in \mathbb{Z}_{+}$, there is $C$ so that on $\Omega,\left|\nabla^{k} \rho\right| \leq C d^{-2 k} \rho$.

We will let $0<\phi<d \leq 1$ be a smooth function on $\Omega$, which near the boundary $\partial \Omega$ (say for $d(x)<\frac{1}{8}$ ) satisfies $\phi(x)=(d(x))^{2}$. Note that for all $x \in \Omega$, the Euclidean ball $\overline{B_{\phi(x)}(x)} \subset \Omega$. We note then that for each $k \in \mathbb{Z}_{+}$, there is a $C$ so that $\left|\phi^{k} \rho^{-1} \nabla^{k} \rho\right| \leq C$. Moreover, there is a $C>1$ so that for all $x \in \Omega$ and
$y \in B_{\phi(x)}(x), C^{-1} \leq \frac{\phi(x)}{\phi(y)} \leq C$ and $C^{-1} \leq \frac{\rho(x)}{\rho(y)} \leq C$, since for $y \in B_{\phi(x)}(x)$, it follows that $d(x)-\phi(x) \leq d(y) \leq d(x)+\phi(x)$.

Given $k \in \mathbb{Z}_{+}$and a metric $g$ on $\bar{\Omega}$, we define the weighted Sobolev space $H_{\rho}^{k}(\Omega, g)$ to be the space of functions (or sections of a tensor bundle) $u$ so that $\left|\nabla_{g}^{j} u\right|_{g} \in L^{2}\left(\Omega, \rho d \mu_{g}\right)$ for all $0 \leq j \leq k$, with $\|u\|_{H_{\rho}^{k}(\Omega, g)}^{2}=\sum_{j \leq k} \int_{\Omega}\left|\nabla_{g}^{j} u\right|_{g}^{2} \rho d \mu_{g}$. We extend this to $k=0$, and let $L_{\rho}^{2}(\Omega, g)=H_{\rho}^{0}(\Omega, g) . H_{\rho}^{k}(\Omega, g)$ has a natural Hilbert space structure. For economy of notation we will sometimes suppress the metric: $H_{\rho}^{k}(\Omega):=H_{\rho}^{k}(\Omega, g)$. We assume $g$ is smooth, or at least $C^{k}(\bar{\Omega})$, to define $\nabla_{g}^{j} u$ for a tensor field, with $j \leq k$. We can interpret $\nabla_{g}^{j} u$ weakly, and we note that by [20, Lemma 2.1], $C^{\infty}(\bar{\Omega})$ is dense in $H_{\rho}^{k}(\Omega)$. We also note that we get an equivalent norm if we use the background Euclidean metric $\stackrel{\circ}{g}$.

For $r, s \in \mathbb{R}$, let $\varphi=\phi^{r} \rho^{s}$. For $\alpha \in(0,1]$ and $k$ a nonnegative integer, define the weighted Hölder space $C_{\phi, \varphi}^{k, \alpha}(\Omega)$ as the space of all $u \in C_{\text {loc }}^{k, \alpha}(\Omega)$ for which
$$\|u\|_{C_{\phi, \varphi}^{k, \alpha}(\Omega)}:=\sup _{x \in \Omega}\left(\sum_{j=0}^{k} \varphi(x) \phi^{j}(x)\left\|\stackrel{\circ}{\nabla}^{j} u\right\|_{C^{0}\left(B_{\phi(x)}(x)\right)}+\varphi(x) \phi^{k+\alpha}(x)\left[\stackrel{\circ}{\nabla}^{k} u\right]_{0, \alpha ; B_{\phi(x)}(x)}\right)$$
is finite. $C_{\phi, \varphi}^{k, \alpha}(\Omega)$ is a Banach space. We would obtain an equivalent norm by using the connection $\nabla_{g}$ in place of the Euclidean connection, as in [13, Appendix A].

We will also make use of the following spaces: $\mathcal{B}_{0}(\Omega)=C_{\phi, \phi^{4+\frac{3}{2}} \rho^{-\frac{1}{2}}}^{0, \alpha}(\Omega) \cap L_{\rho^{-1}}^{2}(\Omega)$, $\mathcal{B}_{2}(\Omega)=C_{\phi, \phi^{2+\frac{3}{2}} \rho^{-\frac{1}{2}}}^{2, \alpha}(\Omega) \cap L_{\rho^{-1}}^{2}(\Omega)$, while $\mathcal{B}_{4}(\Omega)=C_{\phi, \phi^{\frac{3}{2}} \rho^{\frac{1}{2}}}^{4, \alpha}(\Omega) \cap H_{\rho}^{2}(\Omega)$. The norms on these spaces are defined by summing the relevant weighted Sobolev and Hölder norms, e.g. $\|u\|_{\mathcal{B}_{0}(\Omega)}:=\|u\|_{C_{\phi, \phi^{4+\frac{3}{2}} \rho^{-\frac{1}{2}}}^{0, \alpha}(\Omega)}+\|u\|_{L_{\rho-1}^{2}(\Omega)}$. As remarked above, changing the metric gives an equivalent norm, so we often suppress the metric.
A.3. The Basic Weighted Injectivity Estimate. We obtain a basic weighted coercivity estimate for $L_{g}^{*}$ for $g$ near $g_{S}^{m}$, in a suitable space transverse to $\operatorname{ker}\left(L_{g_{S}^{m}}^{*}\right)$ on $\Omega=\left\{x \in \mathbb{R}^{3}: 1<|x|<2\right\}$.

Proposition A.7. Let $\gamma$ be a metric in $C^{0}(\bar{\Omega})$. Let $S_{\gamma}$ be the $L^{2}(\Omega, \gamma)$-orthogonal complement of $\left(\zeta \operatorname{ker}\left(L_{g_{S}^{m}}^{*}\right)\right)$. There is a $C^{2}(\bar{\Omega})$-neighborhood $\mathcal{U}$ of $g_{S}^{m}$ and a $C>0$ so that for all $g \in \mathcal{U}$ and for all $u \in H_{\rho}^{2}(\Omega, g) \cap S_{\gamma}$, we have the following:
$$\|u\|_{H_{\rho}^{2}(\Omega, g)} \leq C\left\|L_{g}^{*} u\right\|_{L_{\rho}^{2}(\Omega, g)} .$$
Proof. Let $\dot{\varepsilon}=\frac{1}{8}$ and let $g \in \mathcal{U}$, where $\mathcal{U}$ is as in Lemma A.6. If suffices by density to establish the estimate for $u \in H^{2}(\Omega, g) \cap S_{\gamma}$. Using the monotonicity of $\dot{\rho}$, we have by (A.3) that
$$\int_{0}^{\varepsilon^{\mathrm{e}}} \stackrel{\circ}{\rho}^{\prime}(\varepsilon)\|u\|_{H^{2}\left(\Omega_{\varepsilon}, g\right)}^{2} d \varepsilon \leq C^{2} \int_{0}^{\varepsilon^{\mathrm{e}}} \stackrel{\circ}{\rho}^{\prime}(\varepsilon)\left\|L_{g}^{*} u\right\|_{L^{2}\left(\Omega_{\varepsilon}, g\right)}^{2} d \varepsilon .$$

Applying the co-area formula $\int_{\Omega \backslash \Omega_{\dot{\varepsilon}}} f d \mu_{g}=\int_{0}^{\varepsilon} \int_{\{x: d(x)=\varepsilon\}} f\left|\nabla_{g} d\right|_{g}^{-1} d \sigma_{g} d \varepsilon$ and integrating by parts, we have
$$\begin{aligned}
& \stackrel{\circ}{\rho}(\stackrel{\circ}{\varepsilon})\|u\|_{H^{2}\left(\Omega_{\bar{\varepsilon}}, g\right)}^{2}+\int_{0}^{\stackrel{\varepsilon}{e}} \stackrel{\circ}{\rho}(\varepsilon) \int_{\{x: d(x)=\varepsilon\}} \sum_{j \leq 2}\left|\nabla_{g}^{j} u\right|_{g}^{2}\left|\nabla_{g} d\right|_{g}^{-1} d \sigma_{g} d \varepsilon \\
& \quad \leq C^{2}\left(\stackrel{\circ}{\rho}(\stackrel{\circ}{\varepsilon})\left\|L_{g}^{*} u\right\|_{L^{2}\left(\Omega_{\bar{\varepsilon}}, g\right)}^{2}+\int_{0}^{\stackrel{\varepsilon}{\varepsilon}} \stackrel{\circ}{\rho}(\varepsilon) \int_{\{x: d(x)=\varepsilon\}}\left|L_{g}^{*} u\right|_{g}^{2}\left|\nabla_{g} d\right|_{g}^{-1} d \sigma_{g} d \varepsilon\right),
\end{aligned}$$
i.e.
$$\begin{aligned}
\stackrel{\circ}{\rho}(\stackrel{\circ}{\varepsilon})\|u\|_{H^{2}\left(\Omega_{\tilde{\varepsilon}}, g\right)}^{2} & +\|u\|_{H_{\rho}^{2}\left(\Omega \backslash \Omega_{\dot{\varepsilon}}, g\right)}^{2}=\stackrel{\circ}{\rho}(\stackrel{\circ}{\varepsilon})\|u\|_{H^{2}\left(\Omega_{\tilde{\varepsilon}}, g\right)}^{2}+\int_{\Omega \backslash \Omega_{\hat{\varepsilon}}} \sum_{j \leq 2}\left|\nabla_{g}^{j} u\right|_{g}^{2} \rho d \mu_{g} \\
\leq & C^{2}\left(\stackrel{\circ}{\rho}(\stackrel{\circ}{\varepsilon})\left\|L_{g}^{*} u\right\|_{L^{2}\left(\Omega_{\tilde{\varepsilon}}, g\right)}^{2}+\int_{\Omega \backslash \Omega_{\hat{\varepsilon}}}\left|L_{g}^{*} u\right|_{g}^{2} \rho d \mu_{g}\right) \leq C^{2}\left\|L_{g}^{*} u\right\|_{L_{\rho}^{2}(\Omega, g)}^{2} .
\end{aligned}$$
Since $0<\stackrel{\circ}{\rho} \leq 1,\|u\|_{H_{\rho}^{2}\left(\Omega_{\tilde{\varepsilon}}, g\right)}^{2} \leq\|u\|_{H^{2}\left(\Omega_{\tilde{\varepsilon}}, g\right)}^{2}$, and we can conclude
$$\|u\|_{H_{\rho}^{2}(\Omega, g)}^{2} \leq C^{2}(\AA(\AA))^{-1}\left\|L_{g}^{*} u\right\|_{L_{\rho}^{2}(\Omega, g)}^{2} .$$ \(\square\)

Remark A.8. As remarked earlier, one could take a background metric such as $\stackrel{\circ}{g}$ to define the norms and obtain an analogous estimate.
A.4. Weighted Schauder estimates. We record here a basic elliptic estimate in the weighted Hölder spaces. The proof of the relevant estimate is a fairly straightforward scaling argument using the interior Schauder estimates, and can be found in [18, Appendix A], following [13, Appendix B], where more general operators are treated, cf. [19, Appendix C]. We suppose $\phi$ and $\varphi$ are defined as above.

Proposition A.9. Suppose $P=\Delta^{2}+\sum_{|\beta| \leq 3} b_{\beta} \partial^{\beta}$ on $\Omega$, with $b_{\beta} \in C_{\phi, \phi^{4-|\beta|}}^{k, \alpha}(\Omega)$. Then for $k$ a nonnegative integer and $0<\alpha<1$, there is a constant $C$ so that for all $u \in C_{\phi, \varphi}^{k+4, \alpha}(\Omega)$,
$$\|u\|_{C_{\phi, \varphi}^{k+4, \alpha}(\Omega)} \leq C\left(\|P u\|_{C_{\phi, \phi^{4} \varphi}^{k, \alpha}(\Omega)}+\|u\|_{L_{\phi^{-} \zeta_{\varphi^{2}}}^{2}(\Omega)}\right) .$$
Moreover, if $u \in L_{\phi^{-3} \varphi^{2}}^{2}(\Omega)$ and $P u \in C_{\phi, \phi^{4} \varphi}^{k, \alpha}(\Omega)$, then $u \in C_{\phi, \varphi}^{k+4, \alpha}(\Omega)$ and the above estimate holds.

Of interest to us here, the operator $P=\frac{1}{2} \rho^{-1} L_{g} \rho L_{g}^{*}$ is of the above form, for $g \in C^{k+4, \alpha}(\bar{\Omega})$.
A.5. The linearized equation. We let $\zeta$ be as above, and let $S_{g}$ be the $L^{2}(\Omega, g)$ -orthogonal complement of $\left(\zeta \operatorname{ker}\left(L_{g_{S}^{m}}^{*}\right)\right)$, and let $\Pi_{g}$ be the corresponding orthogonal projection onto $S_{g}$; let $\stackrel{\mathrm{o}}{S}=S_{g_{S}^{m}}$ and $\stackrel{\circ}{\Pi}=\Pi_{g_{S}^{m}}$. We will establish local deformations for the nonlinear operator $g \mapsto \stackrel{ }{\Pi} \circ R(g)$ for $g$ near $g_{S}^{m}$. The linearization of this operator is $\stackrel{\circ}{\Pi} \circ L_{g}$, for which we want to establish surjectivity in appropriate spaces. This will follow from the analogous result for the related operator $\Pi_{g} \circ L_{g}$.

Let $\psi^{\perp}=\psi^{\perp_{g}}=\psi-\Pi_{g}(\psi) \in\left(\zeta \operatorname{ker}\left(L_{g_{S}^{m}}^{*}\right)\right)$. Since $\zeta$ is supported in the set where $\rho=1$, we have that since $\Pi_{g}(\psi)$ and $\psi^{\perp}$ are orthogonal in $L^{2}(\Omega, g)$, they are also orthogonal in $L_{\rho^{-1}}^{2}(\Omega, g)$, hence $\|\psi\|_{L_{\rho^{-1}}^{2}(\Omega, g)}^{2}=\left\|\Pi_{g}(\psi)\right\|_{L_{\rho^{-1}}^{2}(\Omega, g)}^{2}+\left\|\psi^{\perp}\right\|_{L_{\rho^{-1}}^{2}(\Omega, g)}^{2}$. We also note that there is a constant $C>0$ so that for all metrics $g$ near $g_{S}^{m}$, and all $\psi \in \mathcal{B}_{0}(\Omega)$ (using the fact that $\psi^{\perp}$ lies in a finite-dimensional space),
$$\begin{aligned}
\left\|\Pi_{g}(\psi)\right\|_{\mathcal{B}_{0}(\Omega, g)} & \leq\|\psi\|_{\mathcal{B}_{0}(\Omega, g)}+\left\|\psi^{\perp}\right\|_{\mathcal{B}_{0}(\Omega, g)} \leq\|\psi\|_{\mathcal{B}_{0}(\Omega, g)}+C\left\|\psi^{\perp}\right\|_{L_{\rho^{-1}}^{2}(\Omega, g)} \\
& \leq\|\psi\|_{\mathcal{B}_{0}(\Omega, g)}+C\|\psi\|_{L_{\rho^{-1}}^{2}(\Omega, g)} \leq(1+C)\|\psi\|_{\mathcal{B}_{0}(\Omega, g)} .
\end{aligned}$$

We also note that applying $\Pi_{g}$ to $\psi-\stackrel{\circ}{\Pi}(\psi)$ we conclude
$$\left\|\Pi_{g}(\psi)\right\|_{L_{\rho^{-1}(\Omega, g)}^{2}}=\left\|\Pi_{g}(\stackrel{\circ}{\Pi}(\psi))\right\|_{L_{\rho^{-1}(\Omega, g)}^{2}} \leq\|\stackrel{\circ}{\Pi}(\psi)\|_{L_{\rho^{-1}(\Omega, g)}^{2}} \leq C\|\stackrel{\circ}{\Pi}(\psi)\|_{\left.L_{\rho^{-1}\left(\Omega, g_{S}^{2}\right.} m_{0}\right)}$$
where $C$ is uniform for $g$ near $g_{S}^{m}$.
Now, if $u \in C_{c}^{\infty}(\Omega)$, then in the $L^{2}(\Omega, g)$-orthogonal decomposition $u=u_{0}+u_{1}$ where $u_{0} \in\left(\zeta \operatorname{ker}\left(L_{g_{S}^{m}}^{*}\right)\right)$ and $u_{1} \in S_{g}$, we have $u_{1} \in C_{c}^{\infty}(\Omega)$ as well. To say that $\Pi_{g}\left(L_{g} \rho L_{g}^{*}(f)\right)=\Pi_{g}(\psi)$ weakly i.e. $L_{g} \rho L_{g}^{*}(f)-\psi \in\left(\zeta \operatorname{ker}\left(L_{g_{S}^{m}}^{*}\right)\right)$ weakly, can then be interpreted as $\int_{\Omega}\left(\rho L_{g}^{*}(u) \cdot{ }_{g} L_{g}^{*}(f)-\psi u\right) d \mu_{g}=0$ for all $u \in C_{c}^{\infty}(\Omega) \cap S_{g}$.

Proposition A.10. There is a $C^{4, \alpha}(\bar{\Omega})$-neighborhood $\mathcal{U}$ of $g_{S}^{m}$ along with a constant $C_{1}>0$ so that for all $g \in \mathcal{U}$ and for $\psi \in L_{\rho^{-1}}^{2}(\Omega)$, there is a unique $f \in H_{\rho}^{2}(\Omega, g) \cap S_{g}$ that weakly solves
$$\Pi_{g}\left(L_{g} \rho L_{g}^{*}(f)\right)=\Pi_{g}(\psi),$$
along with the estimate
$$\|f\|_{H_{\rho}^{2}(\Omega, g)} \leq C_{1}\left\|\Pi_{g}(\psi)\right\|_{L_{\rho^{-1}}^{2}(\Omega, g)} .$$
For such $f$ we have $\stackrel{\circ}{\Pi}\left(L_{g} \rho L_{g}^{*}(f)\right)=\stackrel{\circ}{\Pi}(\psi)$, with $\|f\|_{H_{\rho}^{2}(\Omega, g)} \leq C_{1}\|\stackrel{\circ}{\Pi}(\psi)\|_{L_{\rho^{-} 1}^{2}(\Omega, g)}$.
Proof. Given $\psi \in L_{\rho^{-1}}^{2}(\Omega, g)$, let $\mathcal{G}(u)$ be defined for $u \in H_{\rho}^{2}(\Omega, g) \cap S_{g}$ by
$$\mathcal{G}(u)=\int_{\Omega}\left(\frac{1}{2} \rho\left|L_{g}^{*}(u)\right|_{g}^{2}-\Pi_{g}(\psi) u\right) d \mu_{g}=\int_{\Omega}\left(\frac{1}{2} \rho\left|L_{g}^{*}(u)\right|_{g}^{2}-\psi u\right) d \mu_{g} .$$
By (A.5), we have
$$\int_{\Omega}\left(\frac{1}{2}\left|L_{g}^{*}(u)\right|_{g}^{2}-\Pi_{g}(\psi) u\right) d \mu_{g} \geq C\|u\|_{H_{\rho}^{2}(\Omega, g)}^{2}-\left\|\Pi_{g}(\psi)\right\|_{L_{\rho^{-1}}^{2}(\Omega, g)} \cdot\|u\|_{L_{\rho}^{2}(\Omega, g)} .$$
Since $\zeta$ has compact support, $S_{g}$ is closed in $H_{\rho}^{2}(\Omega, g) \cap S_{g}$. A standard argument using Banach-Alaoglu and Riesz Representation for Hilbert spaces as in [15, p. 150-152] provides a minimizer $f \in H_{\rho}^{2}(\Omega, g) \cap S_{g}$. Such a minimizer is unique by the strict convexity: if $u_{1} \neq u_{2}$ are two elements in $H_{\rho}^{2}(\Omega, g) \cap S_{g}$, then for $0<s<1$, $\mathcal{G}\left(s u_{1}+(1-s) u_{2}\right)>s \mathcal{G}\left(u_{1}\right)+(1-s) \mathcal{G}\left(u_{2}\right)$, an easy estimate using the arithmetic-geometric mean inequality, and the injectivity of $L_{g}^{*}$ on $H_{\rho}^{2}(\Omega, g) \cap S_{g}$. Moreover since for the minimizer $\mathcal{G}(f) \leq 0$, the desired estimate holds.

We now consider the Euler-Lagrange equations. For $u \in S_{g} \cap C_{c}^{\infty}(\Omega)$,
$$\begin{aligned}
0 & =\left.\frac{d}{d t}\right|_{t=0} \mathcal{G}(f+t u)=\int_{\Omega}\left(\rho L_{g}^{*}(u) \cdot{ }_{g} L_{g}^{*}(f)-\Pi_{g}(\psi) u\right) d \mu_{g} \\
& =\int_{\Omega}\left(\rho L_{g}^{*}(u) \cdot{ }_{g} L_{g}^{*}(f)-\psi u\right) d \mu_{g} .
\end{aligned}$$ \(\square\)

Remark A.11. Let $T$ be the parity map $T(x)=-x$. If $g$ and $\psi$ are parity-symmetric (i.e. $T^{*} g=g$ and $\psi=\psi \circ T$ on $\Omega$ ), then the minimizer $f$ inherits the symmetry, since the minimizer is unique and $\mathcal{G}(f)=\mathcal{G}(f \circ T)$ in this case.

Since the principal part of $L_{g} L_{g}^{*}$ is $2 \Delta_{g}^{2}$, elliptic regularity immediately gives us that $f$ in the preceding is in $H_{\text {loc }}^{4}(\Omega)$, and for smooth $g$, if $\psi$ is smooth, then $f$ is smooth in $\Omega$ too. For suitable $\psi$ we want to show that $\rho L_{g}^{*} f$ extends smoothly by zero over the boundary of $\Omega$. For that we have the following proposition. We suppress the metric notation in the norms, or for definiteness, we could just use the connection $\stackrel{\circ}{\nabla}$ for $\stackrel{\circ}{g}$ and the measure $d \mu_{g}$ in defining the norms (similarly for any fixed (sufficiently) smooth metric).

Proposition A.12. There is a $C^{4, \alpha}(\bar{\Omega})$-neighborhood $\mathcal{U}$ of $g_{S}^{m}$ along with a constant $C_{2}>0$ so that for all $g \in \mathcal{U}$ and for $\psi \in \mathcal{B}_{0}(\Omega)$, if $f \in H_{\rho}^{2}(\Omega) \cap S_{g}$ weakly solves
$$\stackrel{\circ}{\Pi}\left(L_{g} \rho L_{g}^{*}(f)\right)=\stackrel{\circ}{\Pi}(\psi),$$
then $f \in \mathcal{B}_{4}(\Omega)$ and
$$\|f\|_{\mathcal{B}_{4}(\Omega)} \leq C_{2}\|\stackrel{\circ}{\Pi}(\psi)\|_{\mathcal{B}_{0}(\Omega)} .$$
Moreover if we let $h=\rho L_{g}^{*} f$, then
$$\|h\|_{\mathcal{B}_{2}(\Omega)} \leq C_{2}\|\stackrel{\circ}{\Pi}(\psi)\|_{\mathcal{B}_{0}(\Omega)} .$$
Proof. Let $P=\rho^{-1} L_{g} \rho L_{g}^{*}$. Since $\rho=1$ on the support of $\zeta, u^{\perp}=\rho^{-1}(\rho u)^{\perp}$. Then we see $P(f)=\rho^{-1}\left(\stackrel{\circ}{\Pi}(\rho P(f))+(\rho P(f))^{\perp}\right)=\rho^{-1} \stackrel{\circ}{\Pi}(\psi)+(P(f))^{\perp}$. We apply (A.6) to obtain (we omit the domain $\Omega$ in the notation for the norms)
$$\begin{aligned}
\|f\|_{C_{\phi, \phi^{\frac{3}{2} \rho^{\frac{1}{2}}}}^{4, \alpha}} & \leq C\left(\|P(f)\|_{C_{\phi, \phi^{4+\frac{3}{2} \rho^{\frac{1}{2}}}}^{0, \alpha}}+\|f\|_{L_{\rho}^{2}}\right) \\
& \leq C\left(\left\|\rho^{-1} \stackrel{\circ}{\Pi}(\psi)\right\|_{C_{\phi, \phi^{4+\frac{3}{2} \rho^{\frac{1}{2}}}}^{0, \alpha}}+\left\|P(f)^{\perp}\right\|_{C_{\phi, \phi^{4+\frac{3}{2} \rho^{\frac{1}{2}}}}^{0, \alpha}}+\|f\|_{L_{\rho}^{2}}\right) .
\end{aligned}$$
The last term on the right can be estimated by the preceding proposition, and for the first term we have $\left\|\rho^{-1} \stackrel{\circ}{\Pi}(\psi)\right\|_{C_{\phi, \phi^{4+\frac{3}{2} \rho^{\frac{1}{2}}}}^{0, \alpha}} \leq C\|\stackrel{\circ}{\Pi}(\psi)\|_{C_{\phi, \phi^{4+\frac{3}{2} \rho^{-} \frac{1}{2}}}^{0, \alpha}}$. Thus we only need to estimate $\left\|P(f)^{\perp}\right\|_{C_{\phi, \phi}^{0, \alpha}}$. Since $P(f)^{\perp}$ lies in a finite-dimensional space, there is a $C>0$ so that for all $f,\left\|P(f)^{\perp}\right\|_{C_{\phi, \phi^{4+\frac{3}{2} \rho}}^{0, \alpha}} \leq C\left\|P(f)^{\perp}\right\|_{L^{2}(\operatorname{spt}(\zeta))}$. On the
other hand, by interpolation, for any $\epsilon>0$, there is $C(\epsilon)$ so that
$$\begin{aligned}
\left\|P(f)^{\perp}\right\|_{L^{2}(\operatorname{spt}(\zeta))} & \leq\|f\|_{C^{4}(\operatorname{spt}(\zeta))} \leq \epsilon\|f\|_{C^{4, \alpha}(\operatorname{spt}(\zeta))}+C(\epsilon)\|f\|_{L^{2}(\operatorname{spt}(\zeta))} \\
& \leq C\left(\epsilon\|f\|_{C_{\phi, \phi^{\frac{3}{2} \rho^{\frac{1}{2}}}}^{4, \alpha}}+C(\epsilon)\|f\|_{L_{\rho}^{2}}\right) .
\end{aligned}$$

As for $h=\rho L_{g}^{*}(f),\|h\|_{L_{\rho^{-}}^{2}} \leq C\|f\|_{L_{\rho}^{2}}$, while for some $C_{0}$
$$\|h\|_{C_{\phi, \phi^{2+\frac{3}{2}} \rho^{-\frac{1}{2}}}^{2, \alpha}}=\left\|\rho L_{\gamma}^{*}(f)\right\|_{C_{\phi, \phi^{2+\frac{3}{2} \rho^{-\frac{1}{2}}}}^{2, \alpha}} \leq C_{0}\|f\|_{C_{\phi, \phi^{\frac{3}{2}} \rho^{\frac{1}{2}}}^{4, \alpha}} .$$ \(\square\)
A.6. Solving the nonlinear problem by iteration. We continue the proof of Proposition A.2. Given $\gamma$ close to $g_{S}^{m}$ we want to solve for suitable $h(\gamma)$ with $\stackrel{\circ}{\Pi}(R(\gamma+h(\gamma)))=0$. In fact we find $h(\gamma)$ in the form $h(\gamma)=\rho L_{\gamma}^{*}(f)$, for suitable $f$. We do this iteratively, following the same framework as our previous works [15, 20, 18, 19], cf. [13].

Let $\mathcal{L}_{\gamma}=L_{\gamma} \rho L_{\gamma}^{*}$. We recursively define $f_{j}, h_{j}$ and $\gamma_{j}$ as follows. Let $\gamma_{0}=\gamma$. Let $f_{0}$ solve $\stackrel{\circ}{\Pi}\left(\mathcal{L}_{\gamma}\left(f_{0}\right)\right)=-\stackrel{\circ}{\Pi}(R(\gamma))$. Let $h_{0}=\rho L_{\gamma}^{*}\left(f_{0}\right)$. For $\gamma$ close enough to $g_{S}^{m}$, $R(\gamma)$ is sufficiently small so that $\gamma_{1}=\gamma_{0}+h_{0}$ is a small perturbation of $\gamma$, and hence is a metric close to $g_{S}^{m}$. We next solve $\stackrel{\circ}{\Pi}\left(\mathcal{L}_{\gamma}\left(f_{1}\right)\right)=-\stackrel{\circ}{\Pi}\left(R\left(\gamma_{1}\right)\right)$; we then let $h_{1}=\rho L_{\gamma}^{*}\left(f_{1}\right)$, and $\gamma_{2}=\gamma_{1}+h_{1}$. We then justify $h_{1}$ is small, and $\gamma_{2}$ is a metric. We remark that we linearize at a fixed metric, to control some estimates required to close the argument; to illustrate, the operator $L_{\gamma_{1}}$ involves derivatives of the tensor $h_{0}$ we generated, whereas we have fixed estimates on $L_{\gamma}$. As such, though, the convergence to a limit may be slower than that of Newton's method, since the improvement is sub-quadratic after the first iteration.

Lemma A.13. Suppose $0<\delta<1$. There is a constant $C$ and a $C^{4, \alpha}(\bar{\Omega})$ - neighborhood $\mathcal{U}$ of $g_{S}^{m}$ so that the recursion outlined above produces infinite sequences $f_{j}$ and $h_{j}=\rho L_{\gamma}^{*}\left(f_{j}\right)$ and $\gamma_{j}$ with $\gamma_{0}=\gamma$, and $\gamma_{j+1}=\gamma_{0}+\sum_{k=0}^{j} h_{k}$ where each $\gamma_{j}$ is a metric, with the following estimates:
$$\begin{aligned}
\left\|f_{j}\right\|_{\mathcal{B}_{4}(\Omega)} & \leq C\|\stackrel{\circ}{\Pi}(R(\gamma))\|_{\mathcal{B}_{0}(\Omega)}^{(1+j) \delta} \\
\left\|h_{j}\right\|_{\mathcal{B}_{2}(\Omega)} & \leq C\|\stackrel{\circ}{\Pi}(R(\gamma))\|_{\mathcal{B}_{0}(\Omega)}^{(1+j) \delta} \\
\left\|\stackrel{\circ}{\Pi}\left(R\left(\gamma_{j}\right)\right)\right\|_{\mathcal{B}_{0}(\Omega)} & \leq\|\stackrel{\circ}{\Pi}(R(\gamma))\|_{\mathcal{B}_{0}(\Omega)}^{(1+j) \delta} .
\end{aligned}$$

Proof. The proof follows along the same lines as proofs of the analogous results in earlier works, in particular [18, Lemma 3.5], cf. [19, Sec. 6.3], so we just indicate the ideas. The required estimate (A.12) for $f_{0}$ is given by (A.10), and likewise for $h_{0}$ we have (A.11). The required estimate (A.14) for $\stackrel{\circ}{\Pi}\left(R\left(\gamma_{1}\right)\right)$ follows fairly readily from estimating the quadratic Taylor remainder for the scalar curvature functional $R\left(\gamma_{1}\right)=R(\gamma)+L_{\gamma}\left(h_{0}\right)+\mathcal{Q}_{\gamma}\left(h_{0}\right)$ (cf. [18, Sec. 3.5]). Note that for $j=1$ we could allow $\delta=1$, but in the end we use $\delta<1$, as we get slower convergence due to using the linearization at $\gamma=\gamma_{0}$ only, as we illustrate now.

Feeding the estimate (A.14) for $\stackrel{\circ}{\Pi}\left(R\left(\gamma_{1}\right)\right)$ into (A.10) gives the required estimate (A.12) of $f_{1}$, and then the required estimate (A.13) of $h_{1}$ follows likewise. As for the estimate (A.14) for $j=2$ and $j=3$, we write
$$\begin{aligned}
\stackrel{\circ}{\Pi}\left(R\left(\gamma_{2}\right)\right) & =\stackrel{\Pi}{\Pi}\left(R\left(\gamma_{1}\right)+L_{\gamma}\left(h_{1}\right)+\left(L_{\gamma_{1}}-L_{\gamma}\right)\left(h_{1}\right)+\mathcal{Q}_{\gamma_{1}}\left(h_{1}\right)\right) \\
& =\stackrel{\circ}{\Pi}\left(\left(L_{\gamma_{1}}-L_{\gamma}\right)\left(h_{1}\right)+\mathcal{Q}_{\gamma_{1}}\left(h_{1}\right)\right) \\
\stackrel{\circ}{\Pi}\left(R\left(\gamma_{3}\right)\right) & =\stackrel{\circ}{\Pi}\left(R\left(\gamma_{2}\right)+L_{\gamma}\left(h_{2}\right)+\left(L_{\gamma_{2}}-L_{\gamma_{1}}\right)\left(h_{2}\right)+\left[\left(L_{\gamma_{1}}-L_{\gamma}\right)\left(h_{2}\right)+\mathcal{Q}_{\gamma_{2}}\left(h_{2}\right)\right)\right. \\
& =\stackrel{\circ}{\Pi}\left(\left(L_{\gamma_{1}}-L_{\gamma}\right)\left(h_{1}\right)+\mathcal{Q}_{\gamma_{1}}\left(h_{1}\right)\right) .
\end{aligned}$$
As $\gamma_{1}-\gamma=h_{0}$, and $\gamma_{2}-\gamma_{1}=h_{1},\left\|\stackrel{\circ}{\Pi}\left(R\left(\gamma_{2}\right)\right)\right\|_{\mathcal{B}_{0}(\Omega)}$ and $\left\|\stackrel{\circ}{\Pi}\left(R\left(\gamma_{3}\right)\right)\right\|_{\mathcal{B}_{0}(\Omega)}$ above are of quadratic order in $\left(h_{0}, h_{1}, h_{2}\right)$. We also note that since we control $h_{j}$ in $C^{2, \alpha}(\bar{\Omega})$, there is a uniform estimate of $\left\|\mathcal{Q}_{\gamma_{j}}\left(h_{j}\right)\right\|_{\mathcal{B}_{0}(\Omega)}$. From here it should be clear how to proceed, and we refer to [18, Lemma 3.5], cf. [19, Sec. 6.3], for more details. \(\square\)

It follows from this lemma that the iteration converges and yields a solution $h=h(\gamma)=\rho L_{\gamma}^{*} f$ as desired. Moreover we can conclude that the extension of $h$ by zero across $\partial \Omega$ is in $C^{2, \alpha}\left(\mathbb{R}^{3}\right)$, and using Remark A. 11 at each stage of the iteration, we have that if $\gamma$ is parity symmetric, so is $h(\gamma)$. It remains to show that $h$ is smooth, and that $h(\gamma)$ depends continuously on $\gamma$.

The operator $\left.u \mapsto P(u):=\rho^{-1} R\left(\gamma+\rho L_{\gamma}^{*}(u)\right)-R(\gamma)\right)$ is a quasilinear fourth-order elliptic operator provided $\rho L_{\gamma}^{*}(u)$ is sufficiently small, in which case the fourthorder part of the operator is close to that of $\rho^{-1} L_{\gamma} \rho L_{\gamma}^{*}$ (i.e. $2 \Delta_{\gamma}^{2}$ ). So in case $\gamma$ is smooth, $h=h(\gamma)$ is smooth in $\Omega$. To see that it extends smoothly by zero over the boundary $\partial \Omega$, we consider the equation $R(\gamma+h(\gamma))-R(\gamma)=b(\gamma) \zeta f^{m}-R(\gamma)$; as the right-hand side is supported outside a collar neighborhood of the boundary, we can apply Proposition A. 9 for any nonnegative integer $k$, from which we can conclude smoothness, and the required higher-order estimates.

Remark A.14. The support of $h(\gamma)$ is contained in $\bar{\Omega}$. We could of course have arranged the support to lie strictly inside $\Omega$ by running the construction on $\Omega_{\varepsilon}$ in place of $\Omega$, for some small $\varepsilon>0$.
A.7. Continuous dependence. Finally we prove continuous dependence of $h(\gamma)$ and hence $b(\gamma)$ on $\gamma$.

Proof. Suppose we have $\gamma_{1}$ and $\gamma_{2}$ near $g_{S}^{m}$, with associated $h_{1}=h\left(\gamma_{1}\right)=\rho L_{\gamma_{1}}^{*}\left(f_{1}\right)$ and $h_{2}=h\left(\gamma_{2}\right)=\rho L_{\gamma_{2}}^{*}\left(f_{2}\right)$, so that $\stackrel{\circ}{\Pi}\left(R\left(\gamma_{i}+h_{i}\right)\right)=0$. Then writing
$$L_{\gamma_{1}}\left(h_{2}-h_{1}\right)=L_{\gamma_{2}}\left(h_{2}\right)-L_{\gamma_{1}}\left(h_{1}\right)+\left(L_{\gamma_{1}}-L_{\gamma_{2}}\right)\left(h_{2}\right)$$
and applying a Taylor expansion $R\left(\gamma_{i}+h_{i}\right)=R\left(\gamma_{i}\right)+L_{\gamma_{i}}\left(h_{i}\right)+\mathcal{Q}_{\gamma_{i}}\left(h_{i}\right)$, we see
$$\begin{aligned}
L_{\gamma_{1}}\left(h_{2}-h_{1}\right)= & R\left(\gamma_{2}+h_{2}\right)-R\left(\gamma_{1}+h_{1}\right)+R\left(\gamma_{1}\right)-R\left(\gamma_{2}\right)+\mathcal{Q}_{\gamma_{1}}\left(h_{1}\right)-\mathcal{Q}_{\gamma_{2}}\left(h_{2}\right) \\
& +\left(L_{\gamma_{1}}-L_{\gamma_{2}}\right)\left(h_{2}\right) \\
= & \left(b\left(\gamma_{2}\right)-b\left(\gamma_{1}\right)\right) \zeta f^{m}+R\left(\gamma_{1}\right)-R\left(\gamma_{2}\right)+\mathcal{Q}_{\gamma_{1}}\left(h_{1}\right)-\mathcal{Q}_{\gamma_{2}}\left(h_{2}\right) \\
& +\left(L_{\gamma_{1}}-L_{\gamma_{2}}\right)\left(h_{2}\right) .
\end{aligned}$$

Based on the form of the Taylor remainder, there is a constant $C>0$ so that
$$\begin{aligned}
& \left\|\mathcal{Q}_{\gamma_{1}}\left(h_{1}\right)-\mathcal{Q}_{\gamma_{2}}\left(h_{2}\right)\right\|_{\mathcal{B}_{0}(\Omega)} \\
& \text { A.15) } \leq C\left\|\left(h_{1}, h_{2}\right)\right\|_{\mathcal{B}_{2}(\Omega)}\left(\left\|\gamma_{1}-\gamma_{2}\right\|_{C^{2, \alpha}(\Omega)}\left\|\left(h_{1}, h_{2}\right)\right\|_{\mathcal{B}_{2}(\Omega)}+\left\|h_{1}-h_{2}\right\|_{\mathcal{B}_{2}(\Omega)}\right) .
\end{aligned}$$

We will want to express everything in terms of $f_{1}$ and $f_{2}$. Note that
$$\begin{aligned}
L_{\gamma_{1}}\left[\rho L_{\gamma_{1}}^{*}\left(f_{2}-f_{1}\right)\right]= & L_{\gamma_{1}}\left(h_{2}-h_{1}\right)+L_{\gamma_{1}}\left(\rho\left(L_{\gamma_{1}}^{*}-L_{\gamma_{2}}^{*}\right)\left(f_{2}\right)\right) \\
= & \left(b\left(\gamma_{2}\right)-b\left(\gamma_{1}\right)\right) \zeta f^{m}+R\left(\gamma_{1}\right)-R\left(\gamma_{2}\right)+\mathcal{Q}_{\gamma_{1}}\left(h_{1}\right)-\mathcal{Q}_{\gamma_{2}}\left(h_{2}\right) \\
& \quad+\left(L_{\gamma_{1}}-L_{\gamma_{2}}\right)\left(h_{2}\right)+L_{\gamma_{1}}\left[\rho\left(L_{\gamma_{1}}^{*}-L_{\gamma_{2}}^{*}\right)\left(f_{2}\right)\right] \\
=: & \left(b\left(\gamma_{2}\right)-b\left(\gamma_{1}\right)\right) \zeta f^{m}+\mathcal{E}_{1}+L_{\gamma_{1}}\left[\rho\left(L_{\gamma_{1}}^{*}-L_{\gamma_{2}}^{*}\right)\left(f_{2}\right)\right] \\
=: & \left(b\left(\gamma_{2}\right)-b\left(\gamma_{1}\right)\right) \zeta f^{m}+\mathcal{E}_{1}+\mathcal{E}_{2}=:\left(b\left(\gamma_{2}\right)-b\left(\gamma_{1}\right)\right) \zeta f^{m}+\mathcal{E} .
\end{aligned}$$
We estimate each of these terms. By (A.15), and the fact that $R\left(\gamma_{1}\right)-R\left(\gamma_{2}\right)$ is supported in $\overline{\Omega^{\prime}}$, away from $\partial \Omega$, we see for some $C>0$,
$$\begin{aligned}
17) \quad\left\|\mathcal{E}_{1}\right\|_{\mathcal{B}_{0}(\Omega)} & \leq C\left(\left\|\gamma_{1}-\gamma_{2}\right\|_{C^{2, \alpha}\left(\Omega_{0}\right)}+\left\|h_{1}-h_{2}\right\|_{\mathcal{B}_{2}(\Omega)}\left\|\left(h_{1}, h_{2}\right)\right\|_{\mathcal{B}_{2}(\Omega)}\right) \\
\left\|\mathcal{E}_{2}\right\|_{C^{0, \alpha}} & \\
18) & \leq C\left\|\gamma_{1}-\gamma_{2}\right\|_{C^{4, \alpha}(\Omega)}\left\|f_{2}\right\|_{C^{4, \alpha} \rho^{\frac{3}{2}}-\frac{{ }^{3}}{2}}(\Omega) \\
& \leq C\left\|\gamma_{1}-\gamma_{2}\right\|_{C^{4, \alpha}(\Omega)}\left\|f_{2}\right\|_{\mathcal{B}_{4}(\Omega)} .
\end{aligned}$$
Later on we will also want to estimate $\int_{\Omega}\left(f_{2}-f_{1}\right) \mathcal{E} d \mu_{\gamma_{1}}$, for which we note that, using the density of $C_{c}^{\infty}(\Omega)$ in $H_{\rho}^{2}(\Omega)$,
$$\begin{aligned}
\left|\int_{\Omega}\left(f_{2}-f_{1}\right) \mathcal{E}_{1} d \mu_{\gamma_{1}}\right| & \leq\left\|f_{2}-f_{1}\right\|_{L_{\rho}^{2}\left(\Omega, \gamma_{1}\right)}\left\|\mathcal{E}_{1}\right\|_{L_{\rho^{-1}}^{2}\left(\Omega, \gamma_{1}\right)} \\
& \leq C\left\|f_{2}-f_{1}\right\|_{L_{\rho}^{2}\left(\Omega, \gamma_{1}\right)}\left\|\mathcal{E}_{1}\right\|_{\mathcal{B}_{0}(\Omega)} \\
\left|\int_{\Omega}\left(f_{2}-f_{1}\right) \mathcal{E}_{2} d \mu_{\gamma_{1}}\right| & =\left|\int_{\Omega} \rho L_{\gamma_{1}}^{*}\left(f_{2}-f_{1}\right) \cdot \gamma_{1}\left[\left(L_{\gamma_{1}}^{*}-L_{\gamma_{2}}^{*}\right)\left(f_{2}\right)\right] d \mu_{\gamma_{1}}\right| \\
& \leq C\left\|\gamma_{1}-\gamma_{2}\right\|_{C^{2}(\Omega)}\left\|f_{2}\right\|_{H_{\rho}^{2}\left(\Omega, \gamma_{1}\right)}\left\|f_{2}-f_{1}\right\|_{H_{\rho}^{2}\left(\Omega, \gamma_{1}\right)} .
\end{aligned}$$

We next estimate $\left(b\left(\gamma_{2}\right)-b\left(\gamma_{1}\right)\right) \zeta f^{m}=R\left(\gamma_{2}+h_{2}\right)-R\left(\gamma_{1}+h_{1}\right)$. For simplicity of exposition, consider the case $m>0$. Applying the Taylor expansion we have
$$\begin{aligned}
\left(b\left(\gamma_{2}\right)-b\left(\gamma_{1}\right)\right) \int_{\Omega} \zeta\left(f^{m}\right)^{2} d \mu_{\gamma_{1}}= & \int_{\Omega}\left(R\left(\gamma_{2}\right)-R\left(\gamma_{1}\right)\right) f^{m} d \mu_{\gamma_{1}}+\int_{\Omega} L_{\gamma_{2}}\left(h_{2}\right) f^{m} d \mu_{\gamma_{2}} \\
& +\int_{\Omega} L_{\gamma_{2}}\left(h_{2}\right) f^{m}\left[d \mu_{\gamma_{1}}-d \mu_{\gamma_{2}}\right]-\int_{\Omega} L_{\gamma_{1}}\left(h_{1}\right) f^{m} d \mu_{\gamma_{1}} \\
& +\int_{\Omega}\left[\mathcal{Q}_{\gamma_{2}}\left(h_{2}\right)-\mathcal{Q}_{\gamma_{1}}\left(h_{1}\right)\right] f^{m} d \mu_{\gamma_{1}} .
\end{aligned}$$
Therefore by (A.15)
$$\begin{aligned}
\left|b\left(\gamma_{2}\right)-b\left(\gamma_{1}\right)\right| \leq C & \left(\left\|\gamma_{1}-\gamma_{2}\right\|_{C^{2, \alpha}(\Omega)}+\left\|h_{1}-h_{2}\right\|_{\mathcal{B}_{2}(\Omega)}\left\|\left(h_{1}, h_{2}\right)\right\|_{\mathcal{B}_{2}(\Omega)}\right) \\
& +\left|\int_{\Omega} L_{\gamma_{2}}\left(h_{2}\right) f^{m} d \mu_{\gamma_{2}}-\int_{\Omega} L_{\gamma_{1}}\left(h_{1}\right) f^{m} d \mu_{\gamma_{1}}\right|
\end{aligned}$$