---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: Gluing Eguchi-Hanson metrics and a question of Page]

Here, the supremum is taken over all numbers $r \in(0,10)$, all times $t, t^{\prime} \in$ $(-\infty,-\Lambda]$ satisfying $\left|t-t^{\prime}\right| \leq\left((-t)^{-\frac{1}{4}}+r\right)^{2}$, and all points $x, x^{\prime} \in\left[-\frac{1}{2}, \frac{1}{2}\right]^{4}$ satisfying $|x|,\left|x^{\prime}\right| \in\left[\frac{1}{2} r,(-t)^{-\frac{1}{4}}+r\right]$. Moreover, the norm of $h(x, t)$ is taken with respect to the metric $\bar{g}_{(-32 \omega t)^{-\frac{1}{4}},(-t)^{-}} \frac{1}{400}$. We next define
$$\|h\|_{X_{\gamma, \sigma, \Lambda}^{l, \alpha}}:=\|h\|_{X_{\gamma, \sigma, \Lambda}^{0, \alpha}}+\|D h\|_{X_{\gamma, \sigma+1, \Lambda}^{0, \alpha}}+\left\|D^{2} h\right\|_{X_{\gamma, \sigma+2, \Lambda}^{0, \alpha}}+\left\|\frac{\partial}{\partial t} h\right\|_{X_{\gamma, \sigma+2, \Lambda}^{0, \alpha}},$$
where $D$ denotes the Riemannian connection with respect to $\bar{g}_{(-32 \omega t)^{-\frac{1}{4}},(-t)^{-\frac{1}{400}}}$.
Note that the space decay rates in the above definition are appropriately adjusted for the derivatives so that they accommodate for the scaling involved. This allows us to combine Proposition 6.2 with standard interior estimates for parabolic equations to draw the following conclusion:

Corollary 6.4. Given real numbers $\gamma>0$ and $\sigma \in(0,2)$, we can find real numbers $\Lambda>0$ and $C>0$ with the following property. Suppose that $\varepsilon(t)$ is a function which is defined on the interval $(-\infty,-\Lambda]$ and satisfies Assumption 6.1, and let $\delta(t)=(-t)^{-\frac{1}{400}}$. Let $h \in X_{\gamma, \sigma, \Lambda}^{1, \alpha}$ be a solution of the inhomogeneous heat equation $\frac{\partial}{\partial t} h(t)=\Delta_{L, \bar{g}_{\varepsilon(t), \delta(t)}} h(t)+\psi(t)$ which is defined on $M \times(-\infty,-\Lambda]$. Moreover, we assume that $h$ is invariant under the group $\mathscr{G}$ and satisfies the orthogonality conditions
$$\int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}}\left\langle h(t), \bar{o}_{1, \varepsilon(t), \delta(t)}\right\rangle_{\bar{g}_{\varepsilon(t), \delta(t)}} d \operatorname{vol}_{\bar{g}_{\varepsilon(t), \delta(t)}}=0$$
and
$$\int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}}\left\langle h(t), \bar{g}_{\varepsilon(t), \delta(t)}\right\rangle_{\bar{g}_{\varepsilon(t), \delta(t)}} d \operatorname{vol}_{\bar{g}_{\varepsilon(t), \delta(t)}}=0$$
for all $t \in(-\infty,-\Lambda]$. Then
$$\|h\|_{X_{\gamma, \sigma, \Lambda}^{1, \alpha}} \leq C\|\psi\|_{X_{\gamma, \sigma+2, \Lambda}^{0, \alpha}} .$$

The following result is the main result of this section:
Proposition 6.5. Given real numbers $\gamma>0$ and $\sigma \in(0,2)$, we can find real numbers $\Lambda>0$ and $C>0$ with the following property. Suppose that $\varepsilon(t)$ is a function which is defined on the interval $(-\infty,-\Lambda]$ and satisfies Assumption 6.1, and let $\delta(t)=(-t)^{-\frac{1}{400}}$. Let $h \in X_{\gamma, \sigma, \Lambda}^{1, \alpha}$ be a solution of the inhomogeneous heat equation
$$\frac{\partial}{\partial t} h(t)=\Delta_{L, \bar{g}_{\varepsilon(t), \delta(t)}} h(t)+\psi(t)+\lambda(t) \bar{o}_{1, \varepsilon(t), \delta(t)}+\nu(t) \bar{g}_{\varepsilon(t), \delta(t)}$$
which is defined on $M \times(-\infty,-\Lambda]$. Moreover, we assume that $h$ is invariant under the group $\mathscr{G}$ and satisfies the orthogonality conditions
$$\int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}}\left\langle h(t), \bar{o}_{1, \varepsilon(t), \delta(t)}\right\rangle_{\bar{g}_{\varepsilon(t), \delta(t)}} d \operatorname{vol}_{\bar{g}_{\varepsilon(t), \delta(t)}}=0$$
and
$$\int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}}\left\langle h(t), \bar{g}_{\varepsilon(t), \delta(t)}\right\rangle \bar{g}_{\varepsilon(t), \delta(t)} d \operatorname{vol}_{\bar{g}_{\varepsilon(t), \delta(t)}}=0$$
for all $t \in(-\infty,-\Lambda]$. Then
$$\|h\|_{X_{\gamma, \sigma, \Lambda}^{1, \alpha}} \leq C\|\psi\|_{X_{\gamma+\alpha, \sigma+2, \Lambda}^{0, \alpha}} .$$
Moreover, the function
$$E(t):=\int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}}\left\langle\psi(t)+\lambda(t) \bar{o}_{1, \varepsilon(t), \delta(t)}, \bar{o}_{1, \varepsilon(t), \delta(t)}\right\rangle_{\bar{g}_{\varepsilon(t), \delta(t)}} d \operatorname{vol}_{\bar{g}_{\varepsilon(t), \delta(t)}}$$
satisfies
$$|E(t)| \leq C(-t)^{-1-\gamma-\alpha} \delta(t)^{2-\sigma}\|\psi\|_{X_{\gamma+\alpha, \sigma+2, \Lambda}^{0, \alpha}}$$
and
$$\left|t-t^{\prime}\right|^{-\alpha}\left|E(t)-E\left(t^{\prime}\right)\right| \leq C(-t)^{-1-\gamma-\frac{\alpha}{2}} \delta(t)^{2-\sigma}\|\psi\|_{X_{\gamma+\alpha, \sigma+2, \Lambda}^{0, \alpha}}$$
for $0<\left|t-t^{\prime}\right| \leq(-t)^{-\frac{1}{2}}$. Finally, the function
$$F(t):=\int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}}\left\langle\psi(t)+\nu(t) \bar{g}_{\varepsilon(t), \delta(t)}, \bar{g}_{\varepsilon(t), \delta(t)}\right\rangle_{\bar{g}_{\varepsilon(t), \delta(t)}} d \operatorname{vol}_{\bar{g}_{\varepsilon(t), \delta(t)}}$$
satisfies
$$|F(t)| \leq C(-t)^{-2-\gamma+\frac{\sigma}{4}}\|\psi\|_{X_{\gamma+\alpha, \sigma+2, \Lambda}^{0, \alpha}}$$
and
$$\left|t-t^{\prime}\right|^{-\alpha}\left|F(t)-F\left(t^{\prime}\right)\right| \leq C(-t)^{-2-\gamma+\frac{\sigma}{4}+\frac{\alpha}{2}}\|\psi\|_{X_{\gamma+\alpha, \sigma+2, \Lambda}^{0, \alpha}}$$
for $0<\left|t-t^{\prime}\right| \leq(-t)^{-\frac{1}{2}}$.
Proof. Let us define
$$\begin{aligned}
& E_{0}(t)=\int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}}\left\langle\frac{\partial}{\partial t} h(t), \bar{o}_{1, \varepsilon(t), \delta(t)}\right\rangle \bar{g}_{\varepsilon(t), \delta(t)} d \operatorname{vol}_{\bar{g}_{\varepsilon(t), \delta(t)}}, \\
& E_{1}(t)=\int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}}\left\langle h(t), \Delta_{L, \bar{g}_{\varepsilon(t), \delta(t)}} \bar{o}_{1, \varepsilon(t), \delta(t)}\right\rangle_{\bar{g}_{\varepsilon(t), \delta(t)}} d \operatorname{vol}_{\bar{g}_{\varepsilon(t), \delta(t)}}, \\
& E_{2}(t)=\int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}}\left\langle\psi, \bar{o}_{1, \varepsilon(t), \delta(t)}\right\rangle_{\bar{g}_{\varepsilon(t), \delta(t)}} d \operatorname{vol}_{\bar{g}_{\varepsilon(t), \delta(t)}} .
\end{aligned}$$
Differentiating the identity
$$\int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}}\left\langle h(t), \bar{o}_{1, \varepsilon(t), \delta(t)}\right\rangle_{\bar{g}_{\varepsilon(t), \delta(t)}} d \operatorname{vol}_{\bar{g}_{\varepsilon(t), \delta(t)}}=0$$
with respect to $t$ gives
$$\left|E_{0}(t)\right| \leq C(-t)^{-2-\gamma+\frac{\sigma}{4}}\|h\|_{X_{\gamma, \sigma, \Lambda}^{0, \alpha}}$$
and
$$\left|t-t^{\prime}\right|^{-\alpha}\left|E_{0}(t)-E_{0}\left(t^{\prime}\right)\right| \leq C(-t)^{-2-\gamma+\frac{\sigma}{4}+\frac{\alpha}{2}}\|h\|_{X_{\gamma, \sigma, \Lambda}^{0, \alpha}}$$
for $0<\left|t-t^{\prime}\right| \leq(-t)^{-\frac{1}{2}}$. Moreover, in view of Proposition 3.5, the error term $E_{1}(t)$ satisfies
$$\left|E_{1}(t)\right| \leq C(-t)^{-1-\gamma} \delta(t)^{2-\sigma}\|h\|_{X_{\gamma, \sigma, \Lambda}^{0, \alpha}}$$
and
$$\left|t-t^{\prime}\right|^{-\alpha}\left|E_{1}(t)-E_{1}\left(t^{\prime}\right)\right| \leq C(-t)^{-1-\gamma+\frac{\alpha}{2}} \delta(t)^{2-\sigma}\|h\|_{X_{\gamma, \sigma, \Lambda}^{0, \alpha}}$$
for $0<\left|t-t^{\prime}\right| \leq(-t)^{-\frac{1}{2}}$. Finally, we have
$$\left|E_{2}(t)\right| \leq C(-t)^{-\frac{1}{2}-\gamma+\frac{\sigma}{4}-\alpha}\|\psi\|_{X_{\gamma+\alpha, \sigma+2, \Lambda}^{0, \alpha}}$$
and
$$\left|t-t^{\prime}\right|^{-\alpha}\left|E_{2}(t)-E_{2}\left(t^{\prime}\right)\right| \leq C(-t)^{-\frac{1}{2}-\gamma+\frac{\sigma}{4}-\frac{\alpha}{2}}\|\psi\|_{X_{\gamma+\alpha, \sigma+2, \Lambda}^{0, \alpha}}$$
for $0<\left|t-t^{\prime}\right| \leq(-t)^{-\frac{1}{2}}$. Using the identity
$$\lambda(t) \int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}}\left|\bar{o}_{1, \varepsilon(t), \delta(t)}\right|_{\bar{g}_{\varepsilon(t), \delta(t)}}^{2} d \operatorname{vol}_{\bar{g}_{\varepsilon(t), \delta(t)}}=E_{0}(t)-E_{1}(t)-E_{2}(t),$$
we conclude that
$$|\lambda(t)| \leq C(-t)^{-\gamma} \delta(t)^{2-\sigma}\|h\|_{X_{\gamma, \sigma, \Lambda}^{0, \alpha}}+C(-t)^{\frac{1}{2}-\gamma+\frac{\sigma}{4}-\alpha}\|\psi\|_{X_{\gamma+\alpha, \sigma+2, \Lambda}^{0, \alpha}}$$
and
$$\begin{aligned}
\left|t-t^{\prime}\right|^{-\alpha}\left|\lambda(t)-\lambda\left(t^{\prime}\right)\right| & \leq C(-t)^{-\gamma+\frac{\alpha}{2}} \delta(t)^{2-\sigma}\|h\|_{X_{\gamma, \sigma, \Lambda}^{0, \alpha}} \\
& +C(-t)^{\frac{1}{2}-\gamma+\frac{\sigma}{4}-\frac{\alpha}{2}}\|\psi\|_{X_{\gamma+\alpha, \sigma+2, \Lambda}^{0, \alpha}}
\end{aligned}$$
for $0<\left|t-t^{\prime}\right| \leq(-t)^{-\frac{1}{2}}$. From this, we deduce that
$$\left\|\lambda(\cdot) \bar{o}_{1, \varepsilon(\cdot), \delta(\cdot)}\right\|_{X_{\gamma, \sigma+2, \Lambda}^{0, \alpha}} \leq o(1)\|h\|_{X_{\gamma, \sigma, \Lambda}^{0, \alpha}}+C\|\psi\|_{X_{\gamma+\alpha, \sigma+2, \Lambda}^{0, \alpha}},$$
where $o(1)$ represents a term that goes to 0 as $\Lambda \rightarrow \infty$.
In the next step, we define
$$\begin{aligned}
& F_{0}(t)=\int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}}\left\langle\frac{\partial}{\partial t} h(t), \bar{g}_{\varepsilon(t), \delta(t)}\right\rangle_{\bar{g}_{\varepsilon(t), \delta(t)}} d \operatorname{vol}_{\bar{g}_{\varepsilon(t), \delta(t)}}, \\
& F_{1}(t)=\int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}}\left\langle\psi, \bar{g}_{\varepsilon(t), \delta(t)}\right\rangle_{\bar{g}_{\varepsilon(t), \delta(t)}} d \operatorname{vol}_{\bar{g}_{\varepsilon(t), \delta(t)}}
\end{aligned}$$
Differentiating the relation
$$\int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}}\left\langle h(t), \bar{g}_{\varepsilon(t), \delta(t)}\right\rangle \bar{g}_{\varepsilon(t), \delta(t)} d \operatorname{vol}_{\bar{g}_{\varepsilon(t), \delta(t)}}=0$$
with respect to $t$ yields
$$\left|F_{0}(t)\right| \leq C(-t)^{-2-\gamma+\frac{\sigma}{4}}\|h\|_{X_{\gamma, \sigma, \Lambda}^{0, \alpha}}$$
and
$$\left|t-t^{\prime}\right|^{-\alpha}\left|F_{0}(t)-F_{0}\left(t^{\prime}\right)\right| \leq C(-t)^{-2-\gamma+\frac{\sigma}{4}+\frac{\alpha}{2}}\|h\|_{X_{\gamma, \sigma, \Lambda}^{0, \alpha}}$$
for $0<\left|t-t^{\prime}\right| \leq(-t)^{-\frac{1}{2}}$. We next observe that
$$\left|F_{1}(t)\right| \leq C(-t)^{-\gamma-\alpha}\|\psi\|_{X_{\gamma+\alpha, \sigma+2, \Lambda}^{0, \alpha}}$$
and
$$\left|t-t^{\prime}\right|-\alpha\left|F_{1}(t)-F_{1}\left(t^{\prime}\right)\right| \leq C(-t)^{-\gamma-\frac{\alpha}{2}}\|\psi\|_{X_{\gamma+\alpha, \sigma+2, \Lambda}^{0, \alpha}}$$
for $0<\left|t-t^{\prime}\right| \leq(-t)^{-\frac{1}{2}}$. Using the identity
$$\nu(t) \int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}} 4 d \operatorname{vol}_{\bar{g}_{\varepsilon(t), \delta(t)}}=F_{0}(t)-F_{1}(t),$$
we conclude that
$$|\nu(t)| \leq C(-t)^{-2-\gamma+\frac{\sigma}{4}}\|h\|_{X_{\gamma, \sigma, \Lambda}^{0, \alpha}}+C(-t)^{-\gamma-\alpha}\|\psi\|_{X_{\gamma+\alpha, \sigma+2, \Lambda}^{0, \alpha}}$$
and
$$\left|t-t^{\prime}\right|^{-\alpha}\left|\nu(t)-\nu\left(t^{\prime}\right)\right| \leq C(-t)^{-2-\gamma+\frac{\sigma}{4}+\frac{\alpha}{2}}\|h\|_{X_{\gamma, \sigma, \Lambda}^{0, \alpha}}+C(-t)^{-\gamma-\frac{\alpha}{2}}\|\psi\|_{X_{\gamma+\alpha, \sigma+2, \Lambda}^{0, \alpha}}$$
for $0<\left|t-t^{\prime}\right| \leq(-t)^{-\frac{1}{2}}$. This gives
$$\left\|\nu(\cdot) \bar{g}_{\varepsilon(\cdot), \delta(\cdot)}\right\|_{X_{\gamma, \sigma+2, \Lambda}^{0, \alpha}} \leq o(1)\|h\|_{X_{\gamma, \sigma, \Lambda}^{0, \alpha}}+C\|\psi\|_{X_{\gamma+\alpha, \sigma+2, \Lambda}^{0, \alpha}},$$
where again $o(1)$ represents a term that converges to 0 as $\Lambda \rightarrow \infty$.
After these preparations, we can now complete the proof. Using Corollary 6.4, we obtain
$$\|h\|_{X_{\gamma, \sigma, \Lambda}^{1, \alpha}} \leq C\|\psi\|_{X_{\gamma, \sigma+2, \Lambda}^{0, \alpha}}+C\left\|\lambda(\cdot) \bar{o}_{1, \varepsilon(\cdot), \delta(\cdot)}\right\|_{X_{\gamma, \sigma+2, \Lambda}^{0, \alpha}}+C\left\|\nu(\cdot) \bar{g}_{\varepsilon(\cdot), \delta(\cdot)}\right\|_{X_{\gamma, \sigma+2, \Lambda}^{0, \alpha}},$$
hence
$$\|h\|_{X_{\gamma, \sigma, \Lambda}^{1, \alpha}} \leq o(1)\|h\|_{X_{\gamma, \sigma, \Lambda}^{0, \alpha}}+C\|\psi\|_{X_{\gamma+\alpha, \sigma+2, \Lambda}^{0, \alpha}}$$
if $\Lambda$ is sufficiently large. From this, the first statement follows. Finally, the estimates for $E(t)$ and $F(t)$ follow from the fact that $E(t)=E_{0}(t)-E_{1}(t)$ and $F(t)=F_{0}(t)$. \(\square\)

Corollary 6.6. Let $\gamma>0$ and $\sigma \in(0,2)$ be arbitrary, and let $\Lambda>0$ be chosen as in Proposition 6.5. Then, given any tensor $\psi \in X_{\gamma+\alpha, \sigma+2, \Lambda}^{0, \alpha}$, there exists a unique tensor $h \in X_{\gamma, \sigma, \Lambda}^{1, \alpha}$ and scalar functions $\lambda:(-\infty,-\Lambda] \rightarrow \mathbb{R}$ and $\nu:(-\infty,-\Lambda] \rightarrow \mathbb{R}$ such that
$$\frac{\partial}{\partial t} h(t)=\Delta_{L, \bar{g}_{\varepsilon(t), \delta(t)}} h(t)+\psi(t)+\lambda(t) \bar{o}_{1, \varepsilon(t), \delta(t)}+\nu(t) \bar{g}_{\varepsilon(t), \delta(t)} .$$
Moreover, $h$ is invariant under the group $\mathscr{G}$, and satisfies the orthogonality conditions
$$\int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}}\left\langle h(t), \bar{o}_{1, \varepsilon(t), \delta(t)}\right\rangle_{\bar{g}_{\varepsilon(t), \delta(t)}} d \operatorname{vol}_{\bar{g}_{\varepsilon(t), \delta(t)}}=0$$
and
$$\int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}}\left\langle h(t), \bar{g}_{\varepsilon(t), \delta(t)}\right\rangle \bar{g}_{\varepsilon(t), \delta(t)} d \operatorname{vol}_{\bar{g}_{\varepsilon(t), \delta(t)}}=0$$
for all $t \in(-\infty,-\Lambda]$.
Proof. The uniqueness statement follows immediately from Proposition 6.5. Hence, it remains to prove the existence statement. If $\psi$ is compactly supported, standard results on linear parabolic equations imply that there exists a compactly supported tensor $h$ and scalar functions $\lambda(\cdot)$ and $\nu(\cdot)$ with the required properties. To prove the assertion in general, we approximate $\psi$ by compactly supported tensors, and use the a priori estimate in Proposition 6.5 to pass to the limit. \(\square\)

\section*{7. Existence of a solution to the nonlinear problem}

Throughout this section, we fix positive real numbers $\alpha, \gamma, \sigma \in(0,1)$. We assume that $\alpha$ and $\sigma$ are very small, and $\gamma$ is close to 1. Specifically, we may choose $\alpha \in\left(0, \frac{1}{10000}\right), \gamma \in\left(1-\frac{1}{10000}, 1\right)$, and $\sigma \in\left(0, \frac{1}{10000}\right)$. In addition, we require that $\gamma+\alpha<1$. Furthermore, $\Lambda$ will denote a positive real number which we will choose sufficiently large depending on $\alpha, \gamma, \sigma$.

Given a metric $g$ and a symmetric (0, 2)-tensor $k$ satisfying $|k|_{g} \leq \frac{1}{2}$, we define
$$Q_{g}(k)=2 \operatorname{Ric}_{g+k}-2 \operatorname{Ric}_{g}+\Delta_{L, g} k-\mathscr{L}_{Y}(g+k),$$
where $Y=\operatorname{div}_{g} k-\frac{1}{2} \nabla \operatorname{tr}_{g} k$. Note that $Q_{g}(k)$ can be expanded as
$$Q_{g}(k)=k * \nabla^{2} k+\nabla k * \nabla k+\mathrm{Rm}_{g} * k * k+\text { higher order terms. }$$

Recall the definition of $\bar{g}_{\varepsilon, \delta}$ from Section 3. Our goal is to perturb the family of metrics $\bar{g}_{(-32 \omega t)^{-\frac{1}{4}},(-t)^{-}} \frac{1}{400}$ to an exact solution to the Ricci flow which is defined for $t \in(-\infty,-\Lambda]$. This problem comes down to finding a fixed point of a nonlinear mapping between Banach spaces. In the following, we describe this mapping in detail. Let $\mathscr{A}_{\gamma, \sigma, \Lambda}^{\alpha}$ denote the set of all triplets $(k, \eta(\cdot), \beta(\cdot))$ which satisfy the following conditions:
\begin{itemize}
\item[-] The tensor $k$ is invariant under $\mathscr{G}$ and satisfies $\|k\|_{X_{\gamma, \sigma, \Lambda}^{1, \alpha}} \leq 1$.
\item[-] The function $\eta:(-\infty,-\Lambda] \rightarrow \mathbb{R}$ satisfies $|\eta(t)| \leq(-t)^{-\frac{1}{1000}}$, and $\left|t-t^{\prime}\right|^{-\alpha}\left|\eta(t)-\eta\left(t^{\prime}\right)\right| \leq(-t)^{-\frac{1}{1000}}$ for $0<\left|t-t^{\prime}\right| \leq(-t)^{-\frac{1}{2}}$.
\item[-] The function $\beta:(-\infty,-\Lambda] \rightarrow \mathbb{R}$ satisfies $|\beta(t)| \leq(-t)^{-1}$ and $\left|t-t^{\prime}\right|^{-\alpha}\left|\beta(t)-\beta\left(t^{\prime}\right)\right| \leq(-t)^{-1}$ for $0<\left|t-t^{\prime}\right| \leq(-t)^{-\frac{1}{2}}$.
\end{itemize}
We can think of $\mathscr{A}_{\gamma, \sigma, \Lambda}^{\alpha}$ as the unit ball in a suitable Banach space. This Banach space will be denoted by $\mathscr{E}_{\gamma, \sigma, \Lambda}^{\alpha}$.

Given a triplet $(k, \eta(\cdot), \beta(\cdot)) \in \mathscr{A}_{\gamma, \sigma, \Lambda}^{\alpha}$, we consider the family of metrics $\bar{g}_{\varepsilon(t), \delta(t)}$, where
$$\varepsilon(t)=\left(-32 \omega t+\int_{t}^{-\Lambda} \eta(s) d s\right)^{-\frac{1}{4}}$$
and $\delta(t)=(-t)^{-\frac{1}{400}}$ for $t \in(-\infty,-\Lambda]$. It is straightforward to verify that the function $\varepsilon(t)$ satisfies Assumption 6.1 provided that $\Lambda$ is sufficiently
large. By Corollary 6.6, there exists a unique tensor $h \in X_{\gamma, \sigma, \Lambda}^{1, \alpha}$ and scalar functions $\lambda:(-\infty,-\Lambda] \rightarrow \mathbb{R}$ and $\nu:(-\infty,-\Lambda] \rightarrow \mathbb{R}$ such that
$$\frac{\partial}{\partial t} h(t)=\Delta_{L, \bar{g}_{\varepsilon(t), \delta(t)}} h(t)+\psi(t)+\lambda(t) \bar{o}_{1, \varepsilon(t), \delta(t)}+\nu(t) \bar{g}_{\varepsilon(t), \delta(t)},$$
where $\psi(t):=-Q_{\bar{g}_{\varepsilon(t), \delta(t)}}(k(t))+\beta(t) k(t)-\left(\frac{\partial}{\partial t} \bar{g}_{\varepsilon(t), \delta(t)}+2 \operatorname{Ric}_{\bar{g}_{\varepsilon(t), \delta(t)}}\right)$, and $h(t)$ satisfies the orthogonality conditions
$$\int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}}\left\langle h(t), \bar{o}_{1, \varepsilon(t), \delta(t)}\right\rangle_{\bar{g}_{\varepsilon(t), \delta(t)}} d \operatorname{vol}_{\bar{g}_{\varepsilon(t), \delta(t)}}=0$$
and
$$\int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}}\left\langle h(t), \bar{g}_{\varepsilon(t), \delta(t)}\right\rangle \bar{g}_{\varepsilon(t), \delta(t)} d \operatorname{vol}_{\bar{g}_{\varepsilon(t), \delta(t)}}=0$$
for all $t \in(-\infty,-\Lambda]$.
Having solved this linear PDE for $h, \lambda(\cdot), \nu(\cdot)$, we next define a function $\xi:(-\infty,-\Lambda] \rightarrow \mathbb{R}$ by
$$\xi(t)=\eta(t)-\pi^{-2} \varepsilon(t)^{-8} \lambda(t) \int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}}\left|\bar{o}_{1, \varepsilon(t), \delta(t)}\right|_{\bar{g}_{\varepsilon(t), \delta(t)}}^{2} d \operatorname{vol}_{\bar{g}_{\varepsilon(t), \delta(t)}}$$
for $t \in(-\infty,-\Lambda]$.
In the remainder of this section, we will analyze the map $\mathscr{J}$ which sends the triplet $(k, \eta(\cdot), \beta(\cdot)) \in \mathscr{A}_{\gamma, \sigma, \Lambda}^{\alpha}$ to the triplet $(h, \xi(\cdot), \nu(\cdot))$. In order to prove the existence of a fixed point, we need to show that $\mathscr{J}$ maps the unit ball $\mathscr{A}_{\gamma, \sigma, \Lambda}^{\alpha}$ into itself. By combining Corollary 4.4, Proposition 4.5, and Proposition 4.6, we obtain the following result, which relates the time derivative of $\varepsilon(t)$ to the orthogonal projection of $\psi$ to the approximate kernel. This plays the role of a balancing condition; it serves as the main motivation for the definition of $\varepsilon(t)$ above.

Proposition 7.1. Consider a triplet $(k, \eta(\cdot), \beta(\cdot)) \in \mathscr{A}_{\gamma, \sigma, \Lambda}^{\alpha}$, and let $\psi(t)$ and $h(t)$ be as in the discussion above. Then $\|\psi\|_{X_{\gamma+\alpha, \sigma+2, \Lambda}^{0, \alpha}} \leq o(1)$, where $o(1)$ represents a term that converges to 0 as $\Lambda \rightarrow \infty$. Moreover, the function
$$\begin{aligned}
G(t) & :=4 \pi^{2} \varepsilon(t)^{3} \frac{d \varepsilon}{d t}(t)-32 \pi^{2} \omega \varepsilon(t)^{8} \\
& +\int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}}\left\langle\psi(t), \bar{o}_{1, \varepsilon(t), \delta(t)}\right\rangle_{\bar{g}_{\varepsilon(t), \delta(t)}} d \operatorname{vol}_{\bar{g}_{\varepsilon(t), \delta(t)}}
\end{aligned}$$
satisfies $|G(t)| \leq C(-t)^{-2-\frac{1}{400}}$ and $\left|t-t^{\prime}\right|^{-\alpha}\left|G(t)-G\left(t^{\prime}\right)\right| \leq C(-t)^{-2-\frac{1}{400}}$ for $0<\left|t-t^{\prime}\right| \leq(-t)^{-\frac{1}{2}}$. Finally, the function
$$H(t):=\int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}}\left\langle\psi(t), \bar{g}_{\varepsilon(t), \delta(t)}\right\rangle_{\bar{g}_{\varepsilon(t), \delta(t)}} d \operatorname{vol}_{\bar{g}_{\varepsilon(t), \delta(t)}}$$
satisfies $|H(t)| \leq C(-t)^{-\frac{5}{4}}$ and $\left|t-t^{\prime}\right|^{-\alpha}\left|H(t)-H\left(t^{\prime}\right)\right| \leq C(-t)^{-\frac{5}{4}}$ for $0<\left|t-t^{\prime}\right| \leq(-t)^{-\frac{1}{2}}$.

Proof. The inequality $\|k\|_{X_{\gamma, \sigma, \Lambda}^{1, \alpha}} \leq 1$ implies $\left\|Q_{g}(k)\right\|_{X_{\gamma+\alpha, \sigma+2, \Lambda}^{0, \alpha}} \leq o(1)$ and $\|\beta k\|_{X_{\gamma+\alpha, \sigma+2, \Lambda}^{0, \alpha}} \leq o(1)$. Moreover, since $\gamma+\alpha<1$, we have
$$\left\|\frac{\partial}{\partial t} \bar{g}_{\varepsilon(t), \delta(t)}+2 \operatorname{Ric}_{\bar{g}_{\varepsilon(t), \delta(t)}}\right\|_{X_{\gamma+\alpha, \sigma+2, \Lambda}^{0, \alpha}} \leq o(1) .$$
Putting these facts together, we conclude that $\|\psi\|_{X_{\gamma+\alpha, \sigma+2, \Lambda}^{0, \alpha}} \leq o(1)$.
We next estimate the function $G(t)$. Using the inequality $\|k\|_{X_{\gamma, \sigma, \Lambda}^{1, \alpha}} \leq 1$, we obtain $\left|Q_{\bar{g}_{\varepsilon(t), \delta(t)}}(k(t))\right| \leq C(-t)^{-2 \gamma}\left((-t)^{-\frac{1}{4}}+|x|\right)^{-2-2 \sigma}$, hence
$$\begin{aligned}
& \left|\int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}}\left\langle Q_{\bar{g}_{\varepsilon(t), \delta(t)}}(k(t)), \bar{o}_{1, \varepsilon(t), \delta(t)}\right\rangle_{\bar{g}_{\varepsilon(t), \delta(t)}} d \operatorname{vol}_{\bar{g}_{\varepsilon(t), \delta(t)}}\right| \\
& \leq C \int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}}(-t)^{-1-2 \gamma}\left((-t)^{-\frac{1}{4}}+|x|\right)^{-6-2 \sigma} d \operatorname{vol}_{\bar{g}_{\varepsilon(t), \delta(t)}} \\
& \leq C(-t)^{-\frac{1}{2}-2 \gamma+\frac{\sigma}{2}}
\end{aligned}$$
Moreover, since $|k| \leq(-t)^{-\gamma}\left((-t)^{-\frac{1}{4}}+|x|\right)^{-\sigma}$ and $|\beta(t)| \leq(-t)^{-1}$, we obtain
$$\begin{aligned}
& \left|\int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}}\left\langle\beta(t) k(t), \bar{o}_{1, \varepsilon(t), \delta(t)}\right\rangle \bar{g}_{\varepsilon(t), \delta(t)} d \operatorname{vol}_{\bar{g}_{\varepsilon(t), \delta(t)}}\right| \\
& \leq C \int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}}(-t)^{-2-\gamma}\left((-t)^{-\frac{1}{4}}+|x|\right)^{-4-\sigma} d \operatorname{vol}_{\bar{g}_{\varepsilon(t), \delta(t)}} \\
& \leq C(-t)^{-2-\gamma+\frac{\sigma}{4}}
\end{aligned}$$
Finally, using Corollary 4.4 and Proposition 4.6, we obtain
$$\begin{aligned}
& \left\lvert\, 4 \pi^{2} \varepsilon(t)^{3} \frac{d \varepsilon}{d t}(t)-32 \pi^{2} \omega \varepsilon(t)^{8}\right. \\
& \left.-\int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}}\left\langle\frac{\partial}{\partial t} \bar{g}_{\varepsilon(t), \delta(t)}+2 \operatorname{Ric}_{\bar{g}_{\varepsilon(t), \delta(t)},} \bar{o}_{1, \varepsilon(t), \delta(t)}\right\rangle_{\bar{g}_{\varepsilon(t), \delta(t)}} d \operatorname{vol}_{\bar{g}_{\varepsilon(t), \delta(t)}} \right\rvert\, \\
& \leq C \varepsilon(t)^{8} \delta(t)^{2}
\end{aligned}$$
Putting these facts together, we obtain $|G(t)| \leq C(-t)^{-2-\frac{1}{400}}$, as claimed. A similar argument gives $\left|t-t^{\prime}\right|^{-\alpha}\left|G(t)-G\left(t^{\prime}\right)\right| \leq C(-t)^{-2-\frac{1}{400}}$ for $0<$ $\left|t-t^{\prime}\right| \leq(-t)^{-\frac{1}{2}}$.

It remains to estimate the function $H(t)$. Using the inequality $\|k\|_{X_{\gamma, \sigma, \Lambda}^{1, \alpha}} \leq$ 1, we obtain
$$\begin{aligned}
& \left|\int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}}\left\langle Q_{\bar{g}_{\varepsilon(t), \delta(t)}}(k(t)), \bar{g}_{\varepsilon(t), \delta(t)}\right\rangle_{\bar{g}_{\varepsilon(t), \delta(t)}} d \operatorname{vol}_{\bar{g}_{\varepsilon(t), \delta(t)}}\right| \\
& \leq C \int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}}(-t)^{-2 \gamma}\left((-t)^{-\frac{1}{4}}+|x|\right)^{-2-2 \sigma} d \operatorname{vol}_{\bar{g}_{\varepsilon(t), \delta(t)}} \\
& \leq C(-t)^{-2 \gamma}
\end{aligned}$$
and
$$\begin{aligned}
& \left|\int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}}\left\langle\beta(t) k(t), \bar{g}_{\varepsilon(t), \delta(t)}\right\rangle_{\bar{g}_{\varepsilon(t), \delta(t)}} d \operatorname{vol}_{\bar{g}_{\varepsilon(t), \delta(t)}}\right| \\
& \leq C \int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}}(-t)^{-1-\gamma}\left((-t)^{-\frac{1}{4}}+|x|\right)^{-\sigma} d \operatorname{vol}_{\bar{g}_{\varepsilon(t), \delta(t)}} \\
& \leq C(-t)^{-1-\gamma} .
\end{aligned}$$
Moreover, it follows from Proposition 4.5 and Proposition 4.6 that
$$\begin{aligned}
& \left|\int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}}\left\langle\frac{\partial}{\partial t} \bar{g}_{\varepsilon(t), \delta(t)}+2 \operatorname{Ric}_{\bar{g}_{\varepsilon(t), \delta(t)}}, \bar{g}_{\varepsilon(t), \delta(t)}\right\rangle_{\bar{g}_{\varepsilon(t), \delta(t)}} d \operatorname{vol}_{\bar{g}_{\varepsilon(t), \delta(t)}}\right| \\
& \leq C \varepsilon(t)^{8} \delta(t)^{-6} .
\end{aligned}$$
Putting these facts together, we obtain $|H(t)| \leq C(-t)^{-\frac{5}{4}}$. A similar argument gives $\left|t-t^{\prime}\right|^{-\alpha}\left|H(t)-H\left(t^{\prime}\right)\right| \leq C(-t)^{-\frac{5}{4}}$ for $0<\left|t-t^{\prime}\right| \leq(-t)^{-\frac{1}{2}}$. This completes the proof. \(\square\)

Combining Proposition 7.1 with Proposition 6.5, we can draw the following conclusion:

Corollary 7.2. Consider a triplet $(k, \eta(\cdot), \beta(\cdot)) \in \mathscr{A}_{\gamma, \sigma, \Lambda}^{\alpha}$. Then:
\begin{itemize}
\item[-] The tensor $h$ satisfies $\|h\|_{X_{\gamma, \sigma, \Lambda}^{1, \alpha}} \leq o(1)$.
\item[-] The function $\xi(\cdot)$ satisfies $|\xi(t)| \leq C(-t)^{-\frac{1}{400}}$ and $\left|t-t^{\prime}\right|^{-\alpha} \mid \xi(t)-$ $\xi\left(t^{\prime}\right) \left\lvert\, \leq C(-t)^{-\frac{1}{400}}\right.$ for $0<\left|t-t^{\prime}\right| \leq(-t)^{-\frac{1}{2}}$.
\item[-] The function $\nu(\cdot)$ satisfies $|\nu(t)| \leq C(-t)^{-\frac{5}{4}}$ and $\left|t-t^{\prime}\right|^{-\alpha} \mid \nu(t)-$ $\nu\left(t^{\prime}\right) \left\lvert\, \leq C(-t)^{-\frac{5}{4}}\right.$ for $0<\left|t-t^{\prime}\right| \leq(-t)^{-\frac{1}{2}}$.
\end{itemize}
Here, $C$ is a positive constant which does not depend on $\Lambda$, and $o(1)$ represents a quantity which converges to 0 as $\Lambda \rightarrow \infty$.

Proof. For $k$ and $h$ as in the discussion preceding Proposition 7.1 we have by Proposition 6.5 that $\|h\|_{X_{\gamma, \sigma, \Lambda}^{1, \alpha}} \leq C\|\psi\|_{X_{\gamma+\alpha, \sigma+2, \Lambda}^{0, \alpha}}$. This implies by Proposition 7.1 that $\|h\|_{X_{\gamma, \sigma, \Lambda}^{1, \alpha}} \leq o(1)$ which proves the first statement.

We next define
$$\begin{aligned}
E(t) & =\int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}}\left\langle\psi(t)+\lambda(t) \bar{o}_{1, \varepsilon(t), \delta(t)}, \bar{o}_{1, \varepsilon(t), \delta(t)}\right\rangle_{\bar{g}_{\varepsilon(t), \delta(t)}} d \operatorname{vol}_{\bar{g}_{\varepsilon(t), \delta(t)}}, \\
F(t) & =\int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}}\left\langle\psi(t)+\nu(t) \bar{g}_{\varepsilon(t), \delta(t)}, \bar{g}_{\varepsilon(t), \delta(t)}\right\rangle_{\bar{g}_{\varepsilon(t), \delta(t)}} d \operatorname{vol}_{\bar{g}_{\varepsilon(t), \delta(t)}}, \\
G(t) & =4 \pi^{2} \varepsilon(t)^{3} \frac{d \varepsilon}{d t}(t)-32 \pi^{2} \omega \varepsilon(t)^{8} \\
& +\int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}}\left\langle\psi(t), \bar{o}_{1, \varepsilon(t), \delta(t)}\right\rangle_{\bar{g}_{\varepsilon(t), \delta(t)}} d \operatorname{vol}_{\bar{g}_{\varepsilon(t), \delta(t)}}, \\
H(t) & =\int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}}\left\langle\psi(t), \bar{g}_{\varepsilon(t), \delta(t)}\right\rangle_{\bar{g}_{\varepsilon(t), \delta(t)}} d \operatorname{vol}_{\bar{g}_{\varepsilon(t), \delta(t)}} .
\end{aligned}$$
By definition of $\xi(\cdot)$, we have
$$\begin{aligned}
\xi(t) & =\eta(t)-\pi^{-2} \varepsilon(t)^{-8} \lambda(t) \int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}}\left|\bar{o}_{1, \varepsilon(t), \delta(t)}\right|_{\bar{g}_{\varepsilon(t), \delta(t)}} d \operatorname{vol}_{\bar{g}_{\varepsilon(t), \delta(t)}} \\
& =4 \varepsilon(t)^{-5} \frac{d \varepsilon}{d t}(t)-32 \omega \\
& -\pi^{-2} \varepsilon(t)^{-8} \lambda(t) \int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}}\left|\bar{o}_{1, \varepsilon(t), \delta(t)}\right| \overline{\bar{g}}_{\varepsilon(t), \delta(t)}^{2} d \operatorname{vol}_{\bar{g}_{\varepsilon(t), \delta(t)}} \\
& =\pi^{-2} \varepsilon(t)^{-8}(G(t)-E(t))
\end{aligned}$$
Using Proposition 6.5 and Proposition 7.1, we obtain $|\xi(t)| \leq C(-t)^{-\frac{1}{400}}$ and $\left|t-t^{\prime}\right|^{-\alpha}\left|\xi(t)-\xi\left(t^{\prime}\right)\right| \leq C(-t)^{-\frac{1}{400}}$ for $0<\left|t-t^{\prime}\right| \leq(-t)^{-\frac{1}{2}}$. This proves the second statement.

Finally, we have
$$\nu(t) \int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}} 4 d \operatorname{vol}_{\bar{g}_{\varepsilon(t), \delta(t)}}=F(t)-H(t) .$$
Hence, it follows from Proposition 6.5 and Proposition 7.1 that $|\nu(t)| \leq$ $C(-t)^{-\frac{5}{4}}$ and $\left|t-t^{\prime}\right|^{-\alpha}\left|\nu(t)-\nu\left(t^{\prime}\right)\right| \leq C(-t)^{-\frac{5}{4}}$ for $0<\left|t-t^{\prime}\right| \leq(-t)^{-\frac{1}{2}}$. From this, the third statement follows. \(\square\)

After these preparations, we now prove that $\mathscr{J}$ has a fixed point. In addition to the original parameters $\gamma, \alpha$, we will consider another pair of parameters $\tilde{\gamma}, \tilde{\alpha}$ such that $\tilde{\gamma}<\gamma$ and $\tilde{\alpha}<\alpha$.
Proposition 7.3. The set $\mathscr{A}_{\gamma, \sigma, \Lambda}^{\alpha}$ is a compact subset of $\mathscr{E}_{\tilde{\gamma}, \sigma, \Lambda}^{\tilde{\alpha}}$. Moreover, if $\Lambda$ is sufficiently large, then $\mathscr{J}$ maps the set $\mathscr{A}_{\gamma, \sigma, \Lambda}^{\alpha}$ into itself. Finally, the map $\mathscr{J}: \mathscr{A}_{\gamma, \sigma, \Lambda}^{\alpha} \rightarrow \mathscr{A}_{\gamma, \sigma, \Lambda}^{\alpha}$ is continuous with respect to the norm on $\mathscr{E}_{\tilde{\gamma}, \sigma, \Lambda}^{\tilde{\alpha}}$.
Proof. The first statement is standard. The second statement follows directly from Corollary 7.2. In order to prove the third statement, we argue by contradiction. Suppose that there exists a sequence of triplets $u^{(j)} \in$ $\mathscr{A}_{\gamma, \sigma, \Lambda}^{\alpha}$ and a triplet $u \in \mathscr{A}_{\gamma, \sigma, \Lambda}^{\alpha}$ such that $\limsup _{j \rightarrow \infty}\left\|u^{(j)}-u\right\|_{\mathscr{E}_{\bar{\gamma}, \sigma, \Lambda}^{\tilde{\alpha}}}=0$
and $\liminf _{j \rightarrow \infty}\left\|\mathscr{J}\left(u^{(j)}\right)-\mathscr{J}(u)\right\|_{\mathscr{E}_{\hat{\gamma}, \sigma, \Lambda}^{\tilde{\alpha}}}>0$. Note that $\mathscr{A}_{\gamma, \sigma, \Lambda}^{\alpha}$ is a compact subset of $\mathscr{E}_{\tilde{\gamma}, \sigma, \Lambda}^{\tilde{\alpha}}$ which contains the sequence $\mathscr{J}\left(u^{(j)}\right)$. Hence, after passing to a subsequence, we can find an element $v \in \mathscr{A}_{\gamma, \sigma, \Lambda}^{\alpha}$ such that $\limsup _{j \rightarrow \infty}\left\|\mathscr{J}\left(u^{(j)}\right)-v\right\|_{\mathscr{E}_{\tilde{\gamma}, \sigma, \Lambda}^{\tilde{\alpha}}}=0$. From the definition of $\mathscr{J}$, it is easy to see that $v=\mathscr{J}(u)$. This is a contradiction. \(\square\)

Corollary 7.4. The map $\mathscr{J}: \mathscr{A}_{\gamma, \sigma, \Lambda}^{\alpha} \rightarrow \mathscr{A}_{\gamma, \sigma, \Lambda}^{\alpha}$ has a fixed point.
Proof. This follows immediately from Proposition 7.3 and the Schauder fixed point theorem. \(\square\)

Proposition 7.5. Consider the map which sends a triplet ( $k, \eta(\cdot), \beta(\cdot)$ ) to the triplet $(h, \xi(\cdot), \nu(\cdot))$. Every fixed point of this map corresponds to a solution of the Ricci flow on $M$ which is defined for $t \in(-\infty,-\Lambda]$.

Proof. Let us consider a triplet $(k, \eta(\cdot), \beta(\cdot)) \in \mathscr{A}_{\gamma, \sigma, \Lambda}^{\alpha}$ with the property that $h=k, \xi(\cdot)=\eta(\cdot)$, and $\nu(\cdot)=\beta(\cdot)$. As above, we define
$$\varepsilon(t)=\left(-32 \omega t+\int_{t}^{-\Lambda} \eta(s) d s\right)^{-\frac{1}{4}}$$
and $\delta(t)=(-t)^{-\frac{1}{400}}$ for $t \in(-\infty,-\Lambda]$. The relation $\xi(\cdot)=\eta(\cdot)$ directly implies $\lambda(\cdot)=0$. Moreover, since $h=k$ and $\nu(\cdot)=\beta(\cdot)$, it follows that $k$ is a solution of the equation
$$\begin{aligned}
\frac{\partial}{\partial t} k(t) & =\Delta_{L, \bar{g}_{\varepsilon(t), \delta(t)}} k(t)-Q_{\bar{g}_{\varepsilon(t), \delta(t)}}(k(t))+\beta(t) k(t) \\
& -\left(\frac{\partial}{\partial t} \bar{g}_{\varepsilon(t), \delta(t)}+2 \operatorname{Ric}_{\bar{g}_{\varepsilon(t), \delta(t)}}\right)+\beta(t) \bar{g}_{\varepsilon(t), \delta(t)}
\end{aligned}$$
Rearranging terms gives
$$\begin{aligned}
& \frac{\partial}{\partial t}\left(\bar{g}_{\varepsilon(t), \delta(t)}+k(t)\right) \\
& =-2 \operatorname{Ric}_{\bar{g}_{\varepsilon(t), \delta(t)}}+\Delta_{L, \bar{g}_{\varepsilon(t), \delta(t)}} k(t)-Q_{\bar{g}_{\varepsilon(t), \delta(t)}}(k(t))+\beta(t)\left(\bar{g}_{\varepsilon(t), \delta(t)}+k(t)\right) \\
& =-2 \operatorname{Ric}_{\bar{g}_{\varepsilon(t), \delta(t)}}+k(t)+\mathscr{L}_{Y}\left(\bar{g}_{\varepsilon(t), \delta(t)}+k(t)\right)+\beta(t)\left(\bar{g}_{\varepsilon(t), \delta(t)}+k(t)\right),
\end{aligned}$$
where $Y=\operatorname{div}_{\bar{g}_{\varepsilon(t), \delta(t)}} k-\frac{1}{2} \nabla \operatorname{tr}_{\bar{g}_{\varepsilon(t), \delta(t)}} k$. Hence, if we put
$$g(t):=e^{\int_{t}^{-\Lambda} \beta(s) d s}\left(\bar{g}_{\varepsilon(t), \delta(t)}+k(t)\right),$$
then the metrics $g(t)$ satisfy
$$\frac{\partial}{\partial t} g(t)=-2 \operatorname{Ric}_{g(t)}+\mathscr{L}_{Y} g(t) .$$
By pulling back the metrics $g(t)$ under the flow of diffeomorphisms generated by $Y(t)$, we obtain a solution to the Ricci flow which is defined for $t \in$ $(-\infty,-\Lambda]$. \(\square\)

Proof of Theorem 1.1. By Corollary 7.4, the map $\mathscr{J}$ has a fixed point. By Proposition 7.5, this corresponds to an ancient solution of the Ricci flow. \(\square\)

\section*{References}
\begin{itemize}
\item[] [1] M. Anderson, Ricci curvature bounds and Einstein metrics on compact manifolds, J. Amer. Math. Soc. 2, 455-490 (1989)
\item[] [2] M. Anderson, Dehn filling and Einstein metrics in higher dimensions, J. Diff. Geom. 73, 219-261 (2006)
\item[] [3] R. Bamler, Construction of Einstein metrics by generalized Dehn filling, J. Eur. Math. Soc. 14, 887-909 (2012)
\item[] [4] S. Bando, A. Kasue, and H. Nakajima, On a construction of coordinates at infinity on manifolds with fast curvature decay and maximal volume growth, Invent. Math. 97, 313-349 (1989)
\item[] [5] O. Biquard, Désingularisation de métriques d'Einstein, I, Invent. Math. 192, 197-252 (2013)
\item[] [6] O. Biquard and V. Minerbe, A Kummer construction for gravitational instantons, Comm. Math. Phys. 308, 773-794 (2011)
\item[] [7] O. Biquard and Y. Rollin, Wormholes in ACH manifolds, Trans. Amer. Math. Soc. 361, 2021-2046 (2009)
\item[] [8] S. Brendle, Blow-up phenomena for the Yamabe equation, J. Amer. Math. Soc. 21, 951-979 (2008)
\item[] [9] S. Brendle, Ricci Flow and the Sphere Theorem, Graduate Studies in Mathematics, vol. 111, American Mathematical Society (2010)
\item[] [10] S. Brendle, Rotational symmetry of self-similar solutions to the Ricci flow, Invent. Math. 194, 731-764 (2013)
\item[] [11] S. Brendle, Rotational symmetry of Ricci solitons in higher dimensions, J. Diff. Geom. 97, 191-214 (2014)
\item[] [12] S. Brendle, G. Huisken, and C. Sinestrari, Ancient solutions to the Ricci flow with pinched curvature, Duke Math J. 158, 537-551 (2011)
\item[] [13] J. Cheeger, Degeneration of Einstein metrics and metrics with special holonomy, Surveys in Differential Geometry, vol. VIII, 29-73, International Press, Somerville MA (2003)
\item[] [14] P. Daskalopoulos, R. Hamilton, and N. Šešum, Classification of ancient compact solutions to the Ricci flow on surfaces, J. Diff. Geom. 91, 171-214 (2012)
\item[] [15] P. Daskalopoulos, M. del Pino, and N. Šešum, Type II ancient compact solutions to the Yamabe flow, to appear in J. Reine Angew. Math.
\item[] [16] S.K. Donaldson, Calabi-Yau metrics on Kummer surfaces as a model gluing problem, Advances in geometric analysis, 109-118, Adv. Lect. Math. 21, International Press, Somerville, MA (2012)
\item[] [17] T. Eguchi and A. Hanson, Asymptotically flat self-dual solutions to Euclidean gravity, Physics Letters B74, 249-251 (1978)
\item[] [18] G.W. Gibbons and C.N. Pope, The positive action conjecture and asymptotically euclidean metrics in quantum gravity, Comm. Math. Phys. 66, 267-290 (1979)
\item[] [19] M. Gursky and J. Viaclovsky, Critical metrics on connected sums of Einstein fourmanifolds, arXiv:1303.0827
\item[] [20] R. Hamilton, Three-manifolds with positive Ricci curvature, J. Diff. Geom. 17, 255-306 (1982)
\item[] [21] R. Hamilton, Four-manifolds with positive curvature operator, J. Diff. Geom. 24, 153-179 (1986)
\item[] [22] R. Hamilton, The formation of singularities in the Ricci flow, Surveys in Differential Geometry, vol. II, 7-136, International Press, Somerville MA (1995)
\item[] [23] D. Joyce, Compact 8-manifolds with holonomy Spin(7), Invent. Math. 123, 507-552 (1996)
\item[] [24] N. Kapouleas, Complete constant mean curvature surfaces in Euclidean three-space, Ann. of Math. 131, 239-330 (1990)
\end{itemize}
\begin{itemize}
\item[] [25] N. Kapouleas, Compact constant mean curvature surfaces in Euclidean three-space, J. Diff. Geom. 33, 683-715 (1991)
\item[] [26] N. Kapouleas, Constant mean curvature surfaces constructed by fusing Wente tori, Invent. Math. 119, 443-518 (1995)
\item[] [27] N. Kapouleas, Minimal surfaces in the round three-sphere by doubling the equatorial two-sphere, I, arXiv:1409.0226
\item[] [28] N. Kapouleas, Doubling and desingularization constructions for minimal surfaces, Surveys in Geometric Analysis and Relativity, Adv. Lect. Math. vol. 20, 281-325, International Press, Somerville MA (2011)
\item[] [29] C. LeBrun and M. Singer, A Kummer-type construction of self-dual 4-manifolds, Math. Ann. 300, 165-180 (1994)
\item[] [30] R. Mazzeo and F. Pacard, A construction of singular solutions for a semilinear elliptic equation using asymptotic analysis, J. Diff. Geom. 44, 331-370 (1996)
\item[] [31] R. Mazzeo and F. Pacard, Maskit combinations of Poincaré-Einstein metrics, Adv. Math. 204, 379-412 (2006)
\item[] [32] D.N. Page, A physical picture of the K3 gravitational instanton, Physics Letters B80, 55-57 (1978)
\item[] [33] D.N. Page, A periodic but nonstationary gravitational instanton, Physics Letters B100, 313-315 (1981)
\item[] [34] G. Perelman, The entropy formula for the Ricci flow and its geometric applications, arxiv:0211159
\item[] [35] G. Perelman, Ricci flow with surgery on three-manifolds, arxiv:0303109
\item[] [36] R. Schoen, The existence of weak solutions with prescribed singular behavior for a conformally invariant scalar equation, Comm. Pure Appl. Math. 41, 317-392 (1988)
\item[] [37] M. Struwe, A flow approach to Nirenberg's problem, Duke Math. J. 128, 19-64 (2005)
\item[] [38] R. Takahashi, An ancient solution of the Ricci flow in dimension 4 converging to the Euclidean Schwarzschild metric, Comm. Anal. Geom. 22, 289-342 (2014)
\item[] [39] C.H. Taubes, The existence of anti-self-dual conformal structures, J. Diff. Geom. 36, 163-253 (1992)
\item[] [40] C.H. Taubes, Metrics, connections, and gluing theorems, CBMS Regional Conference Series in Mathematics, vol. 89, American Mathematical Society (2011)
\item[] [41] P. Topiwala, A new proof of the existence of Kähler-Einstein metrics on K3, I, Invent. Math. 89, 425-448 (1987)
\item[] [42] P. Topiwala, A new proof of the existence of Kähler-Einstein metrics on K3, II, Invent. Math. 89, 449-454 (1987)
\end{itemize}

Department of Mathematics, Stanford University, Stanford, CA 94305
Department of Mathematics, Brown University, Providence, RI 02912