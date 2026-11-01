---
retention_scope: session
part: 2
total_parts: 4
---

[Part 2/4 of: A relative energy for ALE Ricci-atmetrics]

Let us now consider the following expression, for $g_{b}+h \in \mathcal{M}^{2, \alpha}\left(g_{b}, \varepsilon\right)$,
$$\int_{N}\left(1+v_{g_{b}+h}\right) \mathrm{R}_{g_{b}+h} d \mu_{g_{b}+h}-m_{\mathrm{ADM}}\left(g_{b}+h\right) .$$
Use (3.3) together with the fact that
$$\begin{aligned}
& \int_{N} \operatorname{div}_{g_{b}}\left(\operatorname{div}_{g_{b}} h-\nabla^{g_{b}} \operatorname{tr}_{g_{b}} h\right) d \mu_{g_{b}}-m_{\mathrm{ADM}}\left(g_{b}+h\right)= \\
& \lim _{R \rightarrow+\infty}\left(\int_{\left\{\rho_{g_{b}} \leq R\right\}} \operatorname{div}_{g_{b}}\left(\operatorname{div}_{g_{b}} h-\nabla^{g_{b}} \operatorname{tr}_{g_{b}} h\right) d \mu_{g_{b}}-\int_{\left\{\rho_{g_{b}}=R\right\}}\left\langle\operatorname{div}_{g_{b}} h-\nabla^{g_{b}} \operatorname{tr}_{g_{b}} h, \mathbf{n}_{g_{b}}\right\rangle_{g_{b}} d \sigma_{g_{b}}\right) \\
& =0,
\end{aligned}$$
noticed in (1.4), to obtain
$$\begin{aligned}
\lambda_{\mathrm{ALE}}\left(g_{b}+h\right)= & \int_{N} v_{g_{b}+h} \mathrm{R}_{g_{b}+h} d \mu_{g_{b}+h}+\int_{N} Q_{g_{b}}(h) d \mu_{g_{b}+h} \\
& +\left(\int_{N} \operatorname{div}_{g_{b}}\left(\operatorname{div}_{g_{b}} h-\nabla^{g_{b}} \operatorname{tr}_{g_{b}} h\right)-m_{\mathrm{ADM}}\left(g_{b}+h\right)\right) \\
= & \int_{N} v_{g_{b}+h} \mathrm{R}_{g_{b}+h} d \mu_{g_{b}+h}+\int_{N} Q_{g_{b}}(h) d \mu_{g_{b}+h} .
\end{aligned}$$
This last expression (3.6) is well-defined and analytic on a $C_{\tau}^{2, \alpha}$-neighborhood of $g_{b}$. A similar argument leads to the proof of (3.1) by using the first expression of $\lambda_{\text {ALE }}^{0}(g)$ given in [(2.3), Proposition 2.2, $\lambda_{\text {ALE }}^{0}(g)=\int_{N}\left(\left|\nabla^{g} f_{g}\right|_{g}^{2}+\mathrm{R}_{g}\right) e^{-f_{g}} d \mu_{g}$ instead.

Moreover, for any metric $g$ in this $C_{\tau}^{2, \alpha}$-neighborhood of $g_{b}$ and from the computations of Proposition 2.3, the $L^{2}\left(e^{-f_{g}} d \mu_{g}\right)$-gradient of $\lambda_{\text {ALE }}$ at $g$ is $-\left(\operatorname{Ric}(g)+\nabla^{g, 2} f_{g}\right)$. Since $h \mapsto$ $m_{\mathrm{ADM}}\left(g_{b}+h\right)$ is linear, the Hessian of $\lambda_{\mathrm{ALE}}$ at $g_{b}$ for divergence-free deformations is $\frac{1}{2} L_{g_{b}}$.

Finally, $\lambda_{\text {ALE }}$ is independent of $\left(\tau^{\prime}, \alpha^{\prime}\right) \in\left(\frac{n-2}{2}, \tau\right] \times(0, \alpha]$ since the potential function $f_{g}$ is. Indeed, let $\frac{n-2}{2}<\tau^{\prime} \leq \tau<n-2$ and $0<\alpha^{\prime} \leq \alpha<1$ and let us show that the map $g \rightarrow f_{g}$ is constant as $g$ varies in $B_{C_{\tau^{\prime}}^{2, \alpha^{\prime}}}\left(g_{b}, \varepsilon\right) \cap B_{C_{\tau}^{2, \alpha}}\left(g_{b}, \varepsilon\right)$. Recall from Proposition 1.12 that $w_{g}:=e^{-\frac{f_{g}}{2}}$ satisfies $-4 \Delta_{g} w_{g}+\mathrm{R}_{g} w_{g}=0$ and $w_{g}-1 \in C_{\tau}^{2, \alpha}$ by definition. Let $w:=w_{g}$ (respectively $w^{\prime}:=w_{g}$ ) if $g \in B_{C_{\tau}^{2, \alpha}}\left(g_{b}, \varepsilon\right)$ (respectively if $g \in B_{C_{\tau^{\prime}}^{2, \alpha^{\prime}}}\left(g_{b}, \varepsilon\right)$ ). Then the difference $w-w^{\prime} \in C_{\tau^{\prime}}^{2, \alpha^{\prime}}$ lies in the kernel of $-4 \Delta_{g}+\mathrm{R}_{g}$. Claim 1 of the proof of Proposition 1.12 leads to $w=w^{\prime}$. \(\square\)

The next proposition computes the second variation of $\lambda_{\text {ALE }}$ at any metric $C_{\tau}^{2, \alpha}$-close to a given ALE Ricci flat metric. This is used in the proof of Theorem 7.11 in order to check condition [(2), Proposition 7.1].

Proposition 3.7. Let $\left(N^{n}, g_{b}\right)$ be an $A L E$ Ricci-flat metric asymptotic to $\mathbb{R}^{n} / \Gamma$, for some finite subgroup $\Gamma$ of $S O(n)$ acting freely on $\mathbb{S}^{n-1}$. Let $\tau \in\left(\frac{n-2}{2}, n-2\right)$ and $\alpha \in(0,1)$. Then
there exists $\varepsilon>0$ such that for any $g \in B_{C_{\tau}^{2, \alpha}}\left(g_{b}, \varepsilon\right)$ and any $h \in C_{\tau}^{2, \alpha}$,
$$\begin{aligned}
& \delta_{g}^{2} \lambda_{\mathrm{ALE}}(h, h)= \\
& \quad \frac{1}{2} \int_{N}\left\langle\Delta_{f_{g}} h+2 \operatorname{Rm}(g)(h)-\mathscr{L}_{B_{f g}}(h)(g), h\right\rangle_{g} e^{-f_{g}} d \mu_{g} \\
& \quad+\frac{1}{2} \int_{N}\left\langle h \circ \operatorname{Ric}_{f_{g}}(g)+\operatorname{Ric}_{f_{g}}(g) \circ h-2\left(\frac{\operatorname{tr}_{g} h}{2}-\delta_{g} f(h)\right) \operatorname{Ric}_{f_{g}}(g), h\right\rangle_{g} e^{-f_{g}} d \mu_{g} .
\end{aligned}$$
Here, $\operatorname{Ric}_{f_{g}}(g)$ denotes the Bakry-Émery tensor $\operatorname{Ric}(g)+\nabla^{g, 2} f_{g}$ associated to the smooth metric measure space $\left(N^{n}, g, \nabla^{g} f_{g}\right)$ and $B_{f_{g}}(h)$ denotes the weighted linear Bianchi gauge defined by
$$B_{f_{g}}(h):=\operatorname{div}_{f_{g}} h-\nabla^{g}\left(\frac{\operatorname{tr}_{g} h}{2}-\delta_{g} f(h)\right) .$$

Remark 3.8. In (3.7), notice that the function $\frac{\operatorname{tr}_{g} h}{2}-\delta_{g} f(h)$ is nothing but the infinitesimal variation of the weighted volume $e^{-f_{g}} d \mu_{g}$ and the weighted linear Bianchi gauge $B_{f_{g}}(h)$ differs from the linear Bianchi gauge defined in [C.6, Lemma C.2] by $-h\left(\nabla^{g} f_{g}\right)+\nabla^{g} \delta_{g} f(h)$. This vector field is in turn the variation of the vector field $\nabla^{g} f_{g}$.

Remark 3.9. Proposition 3.7 recovers the second variation of $\lambda_{\mathrm{ALE}}$ at $g=g_{b}$ along divergencefree variations.

Proof. We consider $\varepsilon>0$ so small that $f_{g}$ is well-defined by Proposition 2.2. Now, as the $L^{2}\left(e^{-f_{g}} d \mu_{g}\right)$-gradient of $\lambda_{\text {ALE }}$ is - $\operatorname{Ric}(g)-\nabla^{g, 2} f_{g}=:-\operatorname{Ric}_{f_{g}}(g)$ by Proposition 3.4, we deduce the following formula with the help of Lemma C. 2 and [(C.8), Lemma C.3]:
$$\begin{aligned}
2 \delta_{g}\left(-\operatorname{Ric}_{f_{g}}(g)\right)(h)= & \left(L_{g} h-\mathscr{L}_{B_{g}(h)}(g)\right)-\mathscr{L}_{\nabla^{g}\left(\delta_{g} f(h)\right)}(g)-\mathscr{L}_{\nabla^{g} f_{g}}(h)+\mathscr{L}_{h\left(\nabla^{g} f_{g}\right)}(g) \\
= & \Delta_{g} h+2 \operatorname{Rm}(g)(h)-\operatorname{Ric}(g) \circ h-h \circ \operatorname{Ric}(g) \\
& -\nabla_{\nabla^{g} f}^{g} h-\nabla^{g, 2} f_{g} \circ h-h \circ \nabla^{g, 2} f_{g}-\mathscr{L}_{B_{f_{g}}(h)}(g) \\
= & \Delta_{f_{g}} h+2 \operatorname{Rm}(g)(h)-\operatorname{Ric}_{f_{g}}(g) \circ h-h \circ \operatorname{Ric}_{f_{g}}(g)-\mathscr{L}_{B_{f_{g}}}(h)(g) .
\end{aligned}$$
Here we have used the general fact that $\mathscr{L}_{\nabla^{g} f} T=\nabla_{X}^{g} T+T \circ \nabla^{g, 2} f+\nabla^{g, 2} f \circ T$ for any symmetric $C_{\text {loc }}^{1} 2$-tensor and any $C_{\text {loc }}^{1}$ function $f$.

Next, we observe that the volume variation is
$$\delta_{g}\left(e^{-f_{g}} d \mu_{g}\right)(h)=\left(\frac{\operatorname{tr}_{g} h}{2}-\delta_{g} f(h)\right) e^{-f_{g}} d \mu_{g} .$$
Finally, we compute the variation with respect to the norm on symmetric 2-tensors induced by the metric $g$ as follows:
$$\begin{aligned}
\delta_{g}\left(\langle h, T\rangle_{g}\right)(h) & =-g^{i m} h_{m n} g^{n k} g^{j l} h_{i j} T_{k l}-g^{i k} g^{j m} h_{m n} g^{n l} h_{i j} T_{k l} \\
& =-\langle h \circ T+T \circ h, h\rangle_{g},
\end{aligned}$$
for any symmetric 2-tensor $T$. Then (3.7) follows by considering the linear combination $\frac{1}{2}(3.8)+(3.9)$ to which we add (3.10) applied to $T:=-\operatorname{Ric}_{f_{g}}(g)$. \(\square\)

We end this section by establishing the weighted elliptic equation satisfied by the volume variation at a metric $C_{\tau}^{2, \alpha}$-close to a given ALE Ricci flat metric. Again, this is used in the proof of Theorem 7.11 in order to check conditions [(1), (2), Proposition 7.1].

Proposition 3.10. Let $\left(N^{n}, g_{b}\right)$ be an $A L E$ Ricci-flat metric asymptotic to $\mathbb{R}^{n} / \Gamma$, for some finite subgroup $\Gamma$ of $S O(n)$ acting freely on $\mathbb{S}^{n-1}$. Let $\tau \in\left(\frac{n-2}{2}, n-2\right)$ and $\alpha \in(0,1)$. Then there exists $\varepsilon>0$ such that for any $g \in B_{C_{\tau}^{2, \alpha}}\left(g_{b}, \varepsilon\right)$ and any $h \in C_{\tau}^{2, \alpha}$,
$$\Delta_{f_{g}}\left(\frac{\operatorname{tr}_{g} h}{2}-\delta_{g} f(h)\right)=\frac{1}{2}\left(\operatorname{div}_{f_{g}}\left(\operatorname{div}_{f_{g}} h\right)-\left\langle h, \operatorname{Ric}_{f_{g}}(g)\right\rangle_{g}\right) .$$
Proof. We consider $\varepsilon>0$ so small that $f_{g}$ is well-defined by Proposition 2.2. In particular, the potential function $f_{g}$ satisfies the Euler-Lagrange equation (2.1) that we differentiate along a variation $h \in C_{\tau}^{2, \alpha}$ as follows:
$$\begin{aligned}
2 \delta_{g}\left(\Delta_{g} f_{g}\right)(h) & =2 \Delta_{g} \delta_{g} f(h)-2\left\langle B_{g}(h), \nabla^{g} f_{g}\right\rangle_{g}-2\left\langle h, \nabla^{g, 2} f_{g}\right\rangle_{g}, \\
\delta_{g}\left(\left|\nabla^{g} f_{g}\right|_{g}^{2}\right)(h) & =-h\left(\nabla^{g} f_{g}, \nabla^{g} f_{g}\right)+2\left\langle\nabla^{g} f_{g}, \nabla^{g}\left(\delta_{g} f(h)\right)\right\rangle_{g}, \\
\delta_{g} \mathrm{R}(h) & =\operatorname{div}_{g} \operatorname{div}_{g} h-\Delta_{g} \operatorname{tr}_{g} h-\langle h, \operatorname{Ric}(g)\rangle_{g} .
\end{aligned}$$
Here, we have used [(C.8), Lemma C. 3 ] in the first line and the last line is simply [(C.7), Lemma C.2]. By considering a suitable linear combination of the first variations described in (3.12) and using (2.1) leads to:
$$\begin{aligned}
0= & \delta_{g}\left(2 \Delta_{g} f_{g}-\left|\nabla^{g} f_{g}\right|_{g}^{2}+\mathrm{R}_{g}\right)(h) \\
= & 2 \Delta_{f_{g}}\left(\delta_{g} f(h)-\frac{\operatorname{tr}_{g} h}{2}\right)-\left\langle h, \operatorname{Ric}_{f_{g}}(g)\right\rangle_{g} \\
& -2\left\langle\operatorname{div}_{g} h, \nabla^{g} f_{g}\right\rangle_{g}-\left\langle h, \nabla^{g, 2} f_{g}\right\rangle_{g}+h\left(\nabla^{g} f_{g}, \nabla^{g} f_{g}\right)+\operatorname{div}_{g} \operatorname{div}_{g} h .
\end{aligned}$$
This ends the proof of the desired equation satisfied by $\delta_{g} f(h)-\frac{\operatorname{tr}_{g} h}{2}$ once we observe that:
$$\operatorname{div}_{f_{g}}\left(\operatorname{div}_{f_{g}} h\right)=-2\left\langle\operatorname{div}_{g} h, \nabla^{g} f_{g}\right\rangle_{g}-\left\langle h, \nabla^{g, 2} f_{g}\right\rangle_{g}+h\left(\nabla^{g} f_{g}, \nabla^{g} f_{g}\right)+\operatorname{div}_{g} \operatorname{div}_{g} h .$$ \(\square\)

\subsection*{3.2. Further properties of $\lambda_{\text {ALE }}$.}

We can approximate $C^{2, \alpha}$-perturbations by metrics which are Ricci flat outside a compact subset: this is the content of the following lemma that we state without proof.

Lemma 3.11. Let $\left(N^{n}, g_{b}\right)$ be an $A L E$ Ricci-flat metric asymptotic to $\mathbb{R}^{n} / \Gamma$, for some finite subgroup $\Gamma$ of $S O(n)$ acting freely on $\mathbb{S}^{n-1}$. Let $\tau \in\left(\frac{n-2}{2}, n-2\right)$ and $\alpha \in(0,1)$. Let $g$ be a metric in $B_{C_{\tau}^{2, \alpha}}\left(g_{b}, \varepsilon\right)$ for $\varepsilon$ sufficiently small. Then, for a sequence of cut-off functions $\chi_{s}$ for $s>1$ vanishing in smaller and smaller neighborhoods of infinity, we have for any $\alpha^{\prime} \in(0, \alpha)$ and $\tau^{\prime}<\tau$,
$$\begin{aligned}
& \chi_{s} g+\left(1-\chi_{s}\right) g_{b} \xrightarrow[s \rightarrow+\infty]{C_{\tau^{\prime}}^{2, \alpha^{\prime}}} g, \\
& \lambda_{\mathrm{ALE}}^{0}\left(\chi_{s} g+\left(1-\chi_{s}\right) g_{b}\right)-m_{\mathrm{ADM}}\left(\chi_{s} g+\left(1-\chi_{s}\right) g_{b}\right) \xrightarrow[s \rightarrow+\infty]{ } \lambda_{\mathrm{ALE}}(g) .
\end{aligned}$$

The following proposition sums up the scaling properties and the diffeomorphism invariance of the functional $\lambda_{\text {ALE }}$ : it echoes Proposition 1.14 and Lemma 1.15 established for $\lambda_{\text {ALE }}^{0}$.

Proposition 3.12. Let $\left(N^{n}, g_{b}\right)$ be an $A L E$ Ricci-flat metric asymptotic to $\mathbb{R}^{n} / \Gamma$, for some finite subgroup $\Gamma$ of $S O(n)$ acting freely on $\mathbb{S}^{n-1}$. Let $\tau \in\left(\frac{n-2}{2}, n-2\right)$ and $\alpha \in(0,1)$. Let $g$ be a metric in $B_{C_{\tau}^{2, \alpha}}\left(g_{b}, \varepsilon\right)$ and consider $\phi$ a diffeomorphism close to the identity in the $C_{\tau-1}^{3, \alpha}(T N)$ topology. Then, we have $\lambda_{\text {ALE }}\left(\phi^{*} g\right)=\lambda_{\text {ALE }}(g)$.

Moreover, if $s>0$,
$$\lambda_{\mathrm{ALE}}(s g)=s^{\frac{n-2}{2}} \lambda_{\mathrm{ALE}}(g) .$$
Proof. Let us prove the result assuming that $\mathrm{R}_{g}=0$ in a neighborhood of infinity: the general case is obtained by approximation thanks to Lemma 3.11. Under this assumption, we know that $\lambda_{\text {ALE }}^{0}$ is bounded and has the expected behavior by scaling and action of diffeomorphism thanks to Proposition 1.14 and Lemma 1.15.

The mass behaves the same way by rescaling. Indeed, if $g$ is ALE asymptotic to $g_{e}$ at infinity, then $s g$ is ALE asymptotic to $s g_{e}$ at infinity, and we therefore have
$$m_{\mathrm{ADM}}(s g)=s^{\frac{n}{2}-1} m_{\mathrm{ADM}}(g),$$
by studying the scaling of the operators involved.
The invariance of $m_{\mathrm{ADM}}$ by $C_{\tau-1}^{3, \alpha}$-diffeomorphisms was proved in [Bar86]. \(\square\)

We end this section with the proof of the monotonicity of the functional $\lambda_{\text {ALE }}$ along the Ricci flow in case it stays in a neighborhood of a Ricci-flat metric.

Proposition 3.13. Let $\left(N^{n}, g_{b}\right)$ be an ALE Ricci-flat metric asymptotic to $\mathbb{R}^{n} / \Gamma$, for some finite subgroup $\Gamma$ of $S O(n)$ acting freely on $\mathbb{S}^{n-1}$. Let $\tau \in\left(\frac{n-2}{2}, n-2\right)$ and $\alpha \in(0,1)$ and let $(g(t))_{t \in[0, T]}$ be a solution to the Ricci flow on $N$ starting from $g(0) \in B_{C_{\tau}^{2}, \alpha}\left(g_{b}, \varepsilon\right)$.

Then, $t \in[0, T] \rightarrow \lambda_{\mathrm{ALE}}(g(t)) \in \mathbb{R}$ is non-decreasing along the Ricci flow as long as $g(t) \in B_{C_{\tau}^{2, \alpha}}\left(g_{b}, \varepsilon\right)$ for every $t \in[0, T]$ and,
$$\frac{d}{d t} \lambda_{\mathrm{ALE}}(g(t))=2\left\|\operatorname{Ric}(g(t))+\nabla^{g(t), 2} f_{g(t)}\right\|_{L^{2}\left(e^{-f_{g(t)}}\right)}^{2} .$$
Moreover, $\lambda_{\text {ALE }}(g(\cdot))$ is constant in time on Ricci-flat metrics only.
Remark 3.14. Notice that Proposition 3.13 is not a direct consequence of Proposition 3.4 since in general, the curve $t \in[0, T] \rightarrow g(t) \in B_{C_{\tau}^{2, \alpha}}\left(g_{b}, \varepsilon\right)$ induced by a solution to the Ricci flow is only $C^{0}$ continuous a priori when interpreted with values into the space $C_{\tau}^{2, \alpha}$.

Remark 3.15. To check that a solution to the Ricci flow stays in a neighborhood $B_{C_{\tau}^{2}, \alpha}\left(g_{b}, \varepsilon\right)$ of $g_{b}$ is a delicate problem. In a forthcoming paper, we will investigate this question in case $\left(N^{n}, g_{b}\right)$ is stable.

Proof. Let $R \geq R_{0}>0$ where $R_{0}$ is sufficiently large so that the level sets $\left\{\rho_{g_{b}}=R\right\}$ are closed smooth hypersurfaces. Then if $(g(t))_{t \in[0, T]}$ is a Ricci flow in $B_{C_{\tau}^{2, \alpha}}\left(g_{b}, \varepsilon\right)$, thanks to the proof of Proposition 2.3 by taking into account that $h(t):=-2 \operatorname{Ric}(g(t))$ and $\varphi(t):=$
$$\begin{aligned}
& \delta_{g(t)} f(-2 \operatorname{Ric}(g(t))) \\
& \quad \int_{\left\{\rho_{g_{b}} \leq R\right\}}\left(\left|\nabla^{g(t)} f_{g(t)}\right|_{g(t)}^{2}+\mathrm{R}_{g(t)}\right) e^{-f_{g(t)}} d \mu_{g(t)} \\
& \quad-\left.\int_{\left\{\rho_{g_{b}}=R\right\}}\left\langle\operatorname{div}_{g_{b}}\left(g(t)-g_{b}\right)-\nabla^{g_{b}} \operatorname{tr}_{g_{b}}\left(g(t)-g_{b}\right), \mathbf{n}_{g_{b}}\right\rangle_{g_{b}} d \sigma_{g_{b}}\right|_{t=t_{1}} ^{t_{2}}= \\
& \quad 2 \int_{t_{1}}^{t_{2}} \int_{\left\{\rho_{g_{b}} \leq R\right\}}\left|\operatorname{Ric}(g(t))+\nabla^{g(t), 2} f_{g(t)}\right|_{g(t)}^{2} e^{-f_{g(t)}} d \mu_{g(t)} d t \\
& \quad+\int_{t_{1}}^{t_{2}} \int_{\left\{\rho_{g_{b}}=R\right\}}\left\langle\nabla^{g(t)} \mathrm{R}_{g(t)}+2 \operatorname{Ric}(g(t))\left(\nabla^{g(t)} f_{g(t)}\right), \mathbf{n}_{g(t)}\right\rangle_{g(t)} e^{-f_{g(t)}} d \sigma_{g(t)} d t \\
& \quad+\int_{t_{1}}^{t_{2}} \int_{\left\{\rho_{g_{b}}=R\right\}} 2\left(\mathrm{R}_{g(t)}+\delta_{g(t)} f(-2 \operatorname{Ric}(g(t)))\right)\left\langle\nabla^{g(t)} f_{g(t)}, \mathbf{n}_{g(t)}\right\rangle_{g(t)} e^{-f_{g(t)}} d \sigma_{g(t)} d t \\
& \quad+2 \int_{t_{1}}^{t_{2}} \int_{\left\{\rho_{g_{b}}=R\right\}}\left\langle\operatorname{div}_{g_{b}}\left(\operatorname{Ric}(g(t))-\nabla^{g_{b}} \operatorname{tr}_{g_{b}}(\operatorname{Ric}(g(t))), \mathbf{n}_{g_{b}}\right\rangle_{g_{b}} d \sigma_{g_{b}} d t\right.
\end{aligned}$$
All we need to check is that the boundary integrals go to 0 as $R$ tends to $+\infty$ uniformly in time. First, observe that by properties of the map $g \rightarrow f_{g}$ summarized in Proposition 2.2.
$$\begin{aligned}
& \left|\int_{t_{1}}^{t_{2}} \int_{\left\{\rho_{g_{b}}=R\right\}}\left\langle 2 \operatorname{Ric}(g(t))\left(\nabla^{g(t)} f_{g(t)}\right), \mathbf{n}_{g(t)}\right\rangle_{g(t)} e^{-f_{g(t)}} d \sigma_{g(t)} d t\right| \leq C R^{n-2 \tau-4}, \\
& \left|\int_{t_{1}}^{t_{2}} \int_{\left\{\rho_{g_{b}}=R\right\}} 2\left(\mathrm{R}_{g(t)}+\delta_{g(t)} f(-2 \operatorname{Ric}(g(t)))\right)\left\langle\nabla^{g(t)} f_{g(t)}, \mathbf{n}_{g(t)}\right\rangle_{g(t)} e^{-f_{g(t)}} d \sigma_{g(t)} d t\right| \leq C R^{n-2 \tau-2},
\end{aligned}$$
for some positive constant $C=C\left(n, g_{b}, \varepsilon\right)$. Since $\tau>\frac{n-2}{2}$, the righthand sides of (3.15) decay to 0 as $R$ tends to $+\infty$. Now, the remaining boundary integrals in (3.14) would cancel each other if the last integral was expressed in terms of the evolving metric $g(t)$ thanks to the Bianchi identity. To conclude, it is sufficient to notice that:
$$\left|\mathbf{n}_{g(t)}-\mathbf{n}_{g_{b}}\right|_{g_{b}}+\left|e^{-f_{g(t)}} \frac{d_{\sigma_{g(t)}}}{d_{\sigma_{g_{b}}}}-1\right| \leq C \rho^{-\tau},$$
for some positive constant $C=C\left(n, g_{b}, \varepsilon\right)$. Indeed, this implies that:
$$\begin{aligned}
& \left\lvert\, \int_{t_{1}}^{t_{2}} \int_{\left\{\rho_{g_{b}}=R\right\}}\left(\left\langle\nabla^{g(t)} \mathrm{R}_{g(t)}, \mathbf{n}_{g(t)}\right\rangle_{g(t)} e^{-f_{g(t)}} \frac{d \sigma_{g(t)}}{d \sigma_{g_{b}}}\right.\right. \\
& \quad+2\left\langle\operatorname{div}_{g_{b}}\left(\operatorname{Ric}(g(t))-\nabla^{g_{b}} \operatorname{tr}_{g_{b}}(\operatorname{Ric}(g(t))), \mathbf{n}_{g_{b}}\right\rangle_{g_{b}}\right) d \sigma_{g_{b}} d t \mid \leq C R^{n-2-2 \tau} .
\end{aligned}$$
Here we have used that $\nabla^{g(t)} \operatorname{Ric}(g(t))=O\left(\rho_{g_{b}}^{-\tau-2}\right)$ for $t>0$ by Shi's estimates [Shi89].
By letting $R$ tend to $+\infty$ in (3.14) gives the expected result:
$$\lambda_{\mathrm{ALE}}\left(g\left(t_{2}\right)\right)-\lambda_{\mathrm{ALE}}\left(g\left(t_{1}\right)\right)=2 \int_{t_{1}}^{t_{2}} \int_{N}\left|\operatorname{Ric}(g(t))+\nabla^{g(t), 2} f_{g(t)}\right|_{g(t)}^{2} e^{-f_{g(t)}} d \mu_{g(t)} d t$$ \(\square\)

Remark 3.16. Under our assumptions, the mass $m_{\mathrm{ADM}}$, when it is defined, is constant along the Ricci flow by [DM07] (see also [Li18]), the variations of the functional $\lambda_{\text {ALE }}$ therefore only come from those of $\lambda_{\mathrm{ALE}}^{0}$.

\subsection*{3.3. Local properties of stable ALE Ricci flat metric.}

Propositions 2.7 and 3.4 justify the following notion of stability for an ALE Ricci-flat metric.
Definition 3.17. An ALE Ricci-flat metric $\left(N^{n}, g_{b}\right)$ asymptotic to $\mathbb{R}^{n} / \Gamma$, for some finite subgroup $\Gamma$ of $S O(n)$ acting freely on $\mathbb{S}^{n-1}$ is said to be linearly stable if the second variation of $\lambda_{\text {ALE }}$ at $g_{b}$ along a divergence-free variation $h \in C_{\tau}^{2, \alpha}\left(S^{2} T^{*} N\right), \tau \in\left(\frac{n-2}{2}, n-2\right), \alpha \in(0,1)$, is nonpositive, i.e. if $L_{g_{b}}$ is a nonpositive operator in the $L^{2}$ sense when restricted to divergencefree variations in $C_{\tau}^{2, \alpha}\left(S^{2} T^{*} N\right)$.

Definition 3.17 is relevant with respect to the functional $\lambda_{\text {ALE }}$ but it has the apparent disadvantage that it depends on a choice of parameters $(\tau, \alpha) \in\left(\frac{n-2}{2}, n-2\right) \times(0,1)$ a priori. The following lemma shows that Definition 3.17 is actually independent of this choice of parameters.

Lemma 3.18. Let $\left(N^{n}, g_{b}\right), n \geq 4$, be an ALE Ricci-flat metric. Then the following assertions are equivalent:
\begin{itemize}
\item[(1)] $\left(N^{n}, g_{b}\right)$ is linearly stable in the sense of Definition 3.17.
\item[(2)] $\left\langle-L_{g_{b}} h, h\right\rangle_{L^{2}} \geq 0$ for all $h \in C_{c}^{\infty}\left(S^{2} T^{*} N\right)$.
\item[(3)] $\left\langle-L_{g_{b}} h, h\right\rangle_{L^{2}} \geq 0$ for all $h \in H_{\frac{n}{2}-1}^{2}\left(S^{2} T^{*} N\right)$.
\end{itemize}
Proof. We proceed by proving the implications (1) ⇒ (2) $\Rightarrow(3) \Rightarrow(1)$.
Notice first that we have the following inclusions
$$C_{c}^{\infty}\left(S^{2} T^{*} N\right) \subset C_{\tau}^{2, \alpha}\left(S^{2} T^{*} N\right) \subset H_{\frac{n}{2}-1}^{2}\left(S^{2} T^{*} N\right),$$
for any $\tau>\frac{n}{2}-1$ and $\alpha \in(0,1)$ according to Remark 1.5. Moreover, $C_{c}^{\infty}\left(S^{2} T^{*} N\right)$ is dense in $H_{\frac{n}{2}-1}^{2}\left(S^{2} T^{*} N\right)$. In particular, the implications (2) ⇒ (3) ⇒ (1) are straightforward.

We claim that if (1) holds true then
$$\left\langle-L_{g_{b}} h, h\right\rangle_{L^{2}} \geq 0, \quad \text { for all } h \in C_{\tau}^{2, \alpha}\left(S^{2} T^{*} N\right) .$$
Taken (3.16) for granted, it is immediate to conclude the proof of the implication (1) ⇒ (2). Therefore, all is left to prove is (3.16) under Condition (1). By Proposition B.6, if $h$ is a symmetric 2-tensor in $C_{\tau}^{2, \alpha}, \beta:=\tau \in\left(\frac{n-2}{2}, n-2\right) \subset(1, n-1)$ then there exist a symmetric 2-tensor $h^{\prime}$ in $C_{\tau}^{2, \alpha}$ and a vector field $X \in C_{\tau-1}^{3, \alpha}$ such that $h=h^{\prime}+\mathscr{L}_{X}\left(g_{b}\right)$. Now, observe by bilinearity that:
$$\begin{aligned}
\left\langle-L_{g_{b}} h, h\right\rangle_{L^{2}}= & \left\langle-L_{g_{b}} h^{\prime}, h^{\prime}\right\rangle_{L^{2}}+\left\langle-L_{g_{b}} h^{\prime}, \mathscr{L}_{X}\left(g_{b}\right)\right\rangle_{L^{2}} \\
& +\left\langle-L_{g_{b}} \mathscr{L}_{X}\left(g_{b}\right), h^{\prime}\right\rangle_{L^{2}}+\left\langle-L_{g_{b}} \mathscr{L}_{X}\left(g_{b}\right), \mathscr{L}_{X}\left(g_{b}\right)\right\rangle_{L^{2}} .
\end{aligned}$$
On the one hand, an integration by parts shows that:
$$\left\langle L_{g_{b}} h^{\prime}, \mathscr{L}_{X}\left(g_{b}\right)\right\rangle_{L^{2}}=\left\langle h^{\prime}, L_{g_{b}} \mathscr{L}_{X}\left(g_{b}\right)\right\rangle_{L^{2}} .$$

Here we have used the fact that $2 \tau+1>n-1$ to handle the boundary term in the integration by parts.

On the other hand, by using the flow $\left(\phi_{t}^{X}\right)_{t \in \mathbb{R}}$ generated by the vector field $X$, one observes that the one-parameter family $\left(\left(\phi_{t}^{X}\right)^{*} g_{b}\right)_{t \in \mathbb{R}}$ is a curve of Ricci-flat metrics. In particular, by differentiating the Ricci-flat equation at $t=0$ with the help of Lemma C.2.
$$L_{g_{b}} \mathscr{L}_{X}\left(g_{b}\right)=\mathscr{L}_{B^{X}}\left(g_{b}\right), \quad B^{X}:=B_{g_{b}}\left(\mathscr{L}_{X}\left(g_{b}\right)\right) .$$

Plugging (3.19) in (3.18) leads to:
$$\begin{aligned}
\left\langle L_{g_{b}} h^{\prime}, \mathscr{L}_{X}\left(g_{b}\right)\right\rangle_{L^{2}} & =\left\langle h^{\prime}, \mathscr{L}_{B^{X}}\left(g_{b}\right)\right\rangle_{L^{2}} \\
& =-2\left\langle\operatorname{div}_{g_{b}} h^{\prime}, B^{X}\right\rangle_{L^{2}}=0,
\end{aligned}$$
since by definition, $h^{\prime}$ is divergence-free. Here again, the integration by parts is legitimated by the fact that $B^{X}=O\left(\rho_{g_{b}}^{-\tau-1}\right)$.

Going back to (3.17), the vanishing (3.20) shows that it is sufficient to prove that
$$\left\langle-L_{g_{b}} \mathscr{L}_{X}\left(g_{b}\right), \mathscr{L}_{X}\left(g_{b}\right)\right\rangle_{L^{2}} \geq 0,$$
since Condition (1) is assumed to hold. Because of (3.19), it is equivalent to check the following:
$$\begin{aligned}
-\left\langle\mathscr{L}_{X}\left(g_{b}\right), \mathscr{L}_{B^{X}}\left(g_{b}\right)\right\rangle_{L^{2}} & =2\left\langle\operatorname{div}_{g_{b}} \mathscr{L}_{X}\left(g_{b}\right), B^{X}\right\rangle_{L^{2}} \\
& =2\left\|B^{X}\right\|_{L^{2}}^{2}+\left\langle\nabla^{g_{b}} \operatorname{tr}_{g_{b}} \mathscr{L}_{X}\left(g_{b}\right), B^{X}\right\rangle_{L^{2}} \\
& =2\left\|B^{X}\right\|_{L^{2}}^{2}-\left\langle\operatorname{tr}_{g_{b}} \mathscr{L}_{X}\left(g_{b}\right), \operatorname{div}_{g_{b}} B^{X}\right\rangle_{L^{2}} \\
& =2\left\|B^{X}\right\|_{L^{2}}^{2}+\frac{1}{2}\left\langle\operatorname{tr}_{g_{b}} \mathscr{L}_{X}\left(g_{b}\right),-\Delta_{g_{b}} \mathscr{L}_{X}\left(g_{b}\right)\right\rangle_{L^{2}} \\
& =2\left\|B^{X}\right\|_{L^{2}}^{2}+\frac{1}{2}\left\|\nabla^{g_{b}} \operatorname{tr}_{g_{b}} \mathscr{L}_{X}\left(g_{b}\right)\right\|_{L^{2}}^{2} \geq 0 .
\end{aligned}$$
Here, we have integrated by parts in the first, third and last lines. The second line uses the definition of $B^{X}$ given in (3.19) only. Taking into account the Ricci-flatness of $g_{b}$, the penultimate line is obtained by considering the trace of (3.19) with respect to the metric $g_{b}$. This concludes the proof of (3.21). \(\square\)

We end this section with the following strong positivity property shared by the Lichnerowicz operator associated to a stable ALE Ricci-flat metric $\left(N^{n}, g_{b}\right)$ : this result established in [DK20, Theorem 3.9] has been proved to be useful for the dynamical stability of integrable Ricci-flat ALE metrics. The proof of this result is essentially due to Devyver [Dev14] in a more general setting.

Theorem 3.19. Let $\left(N^{n}, g_{b}\right)$ be a linearly stable $A L E$ Ricci-flat metric. Then there exists some positive constant $\varepsilon\left(g_{b}\right) \in[0,1)$ such that
$$\left(1-\varepsilon\left(g_{b}\right)\right)\left\langle-\Delta_{g_{b}} h, h\right\rangle_{g_{b}} \leq\left\langle-L_{g_{b}} h, h\right\rangle_{g_{b}},$$
for all $h \in H_{\frac{n}{2}-1}^{2}$ which is $L^{2}\left(g_{b}\right)$-orthogonal to $\operatorname{ker}_{L^{2}\left(g_{b}\right)} L_{g_{b}}$.

\section*{4. Energy estimates on the potential function}

If $\left(N^{n}, g_{b}\right)$ is an ALE Ricci-flat metric, we establish energy estimates on the gradient and the (weighted) laplacian of the potential function $f_{g}$ associated to a metric $g \in B_{C_{\tau}^{2, \alpha}}\left(g_{b}, \varepsilon\right)$ in terms of the norm $\left\|g-g_{b}\right\|_{H_{\frac{n}{2}-1}^{2}}$. These estimates will be crucially used in the proof of Proposition 7.10.

Proposition 4.1. Let $\left(N^{n}, g_{b}\right)$ be an $A L E$ Ricci-flat metric asymptotic to $\mathbb{R}^{n} / \Gamma$, for some finite subgroup $\Gamma$ of $S O(n)$ acting freely on $\mathbb{S}^{n-1}$. Let $\tau \in\left(\frac{n-2}{2}, n-2\right)$ and $\alpha \in(0,1)$. Then there exists a neighborhood $B_{C_{\tau}^{2, \alpha}}\left(g_{b}, \varepsilon\right)$ of $g_{b}$ such that the following energy estimates on the potential function $v_{g}:=e^{-f_{g}}-1$ and its first variation hold true:
$$\left\|\nabla^{g} v_{g}\right\|_{L^{2}} \leq C\left(n, g_{b}, \varepsilon\right)\left\|\nabla^{g_{b}}\left(g-g_{b}\right)\right\|_{L^{2}},$$
and, if $g_{1}$ and $g_{2}$ are metrics in $B_{C_{\tau}^{2, \alpha}}\left(g_{b}, \varepsilon\right)$,
$$\left\|\nabla^{g_{t}}\left(\delta_{g_{t}} f(h)-\frac{\operatorname{tr}_{g_{t}} h}{2}\right)\right\|_{L^{2}} \leq C\left(n, g_{b}, \varepsilon\right)\left\|\nabla^{g_{t}} h\right\|_{L^{2}},$$
where $g_{t}:=g_{1}+(t-1) h:=g_{1}+(t-1)\left(g_{2}-g_{1}\right)$ for $t \in[1,2]$.
Moreover,
$$\left\|\Delta_{g_{t}, f_{g_{t}}}\left(\delta_{g_{t}} f(h)-\frac{\operatorname{tr}_{g_{t}} h}{2}\right)\right\|_{L_{\frac{n}{2}+1}^{2}} \leq C\left(n, g_{b}, \varepsilon\right)\left(\left\|\nabla^{g_{t}} h\right\|_{L^{2}}+\left\|\nabla^{g_{t}, 2} h\right\|_{L_{\frac{n}{2}+1}^{2}}\right), \quad t \in[1,2] .$$
Proof. Let us remark first that if $v_{g}:=w_{g}-1=e^{-f_{g}}-1$ then:
$$\begin{aligned}
\Delta_{g}\left(w_{g}-1\right)^{2} & =\Delta_{g} v_{g}^{2}=2\left|\nabla^{g} v_{g}\right|^{2}+2 \Delta_{g} v_{g} \cdot v_{g} \\
& =2\left|\nabla^{g} v_{g}\right|^{2}+\frac{1}{2} \mathrm{R}_{g} w_{g} \cdot v_{g} \\
& =2\left|\nabla^{g} v_{g}\right|^{2}+\frac{1}{2} \mathrm{R}_{g} v_{g}^{2}+\frac{1}{2} \mathrm{R}_{g} v_{g} .
\end{aligned}$$
Integrating by parts the previous identity gives:
$$2\left\|\nabla^{g} v_{g}\right\|_{L^{2}}^{2} \leq \int_{N}\left|\mathrm{R}_{g}\right| v_{g}^{2} d \mu_{g}-\frac{1}{2} \int_{N} \mathrm{R}_{g} v_{g} d \mu_{g} .$$
Notice that the last term on the righthand side is kept unchanged for the following reason: if $n=4, v_{g}$ or equivalently, $f_{g}$, is not in $L^{2}$ so one needs to proceed in a more subtle way than just using Young's inequality. By tracing Lemma C. 1 together with [(C.7), Lemma C.2], recall that pointwise:
$$\left|-\mathrm{R}_{g}+\operatorname{div}_{g_{b}}\left(\operatorname{div}_{g_{b}} h\right)-\Delta_{g_{b}} \operatorname{tr}_{g_{b}} h\right| \leq C\left(n, g_{b}, \varepsilon\right)\left(\left|\nabla^{g_{b}} h\right|_{g_{b}}^{2}+|h|_{g_{b}}\left|\nabla^{g_{b},{ }^{2}} h\right|_{g_{b}}\right) .$$

In particular, by integrating by parts, if $\gamma>0$,
$$\begin{aligned}
\left|\int_{N} \mathrm{R}_{g} v_{g} d \mu_{g}\right| & \leq C\left(\int_{N}\left|\nabla^{g_{b}} h\right|_{g_{b}}\left|\nabla^{g_{b}} v_{g}\right| g_{b} d \mu_{g}\right)+C \int_{N}\left(\left|\nabla^{g_{b}} h\right|_{g_{b}}^{2}+|h|_{g_{b}}\left|\nabla^{g_{b}, 2} h\right|_{g_{b}}\right)\left|v_{g}\right| d \mu_{g} \\
& \leq \gamma\left\|\nabla^{g_{b}} v_{g}\right\|_{L^{2}}^{2}+C\left(\gamma^{-1}\left\|\nabla^{g_{b}} h\right\|_{L^{2}}^{2}+\left\|\rho_{g_{b}}^{-1} h\right\|_{L^{2}}\left\|\rho_{g_{b}} \cdot v_{g} \cdot\left|\nabla^{g_{b}, 2} h\right|\right\|_{L^{2}}\right) \\
& \leq \gamma\left\|\nabla^{g_{b}} v_{g}\right\|_{L^{2}}^{2}+C\left(\gamma^{-1}\left\|\nabla^{g_{b}} h\right\|_{L^{2}}^{2}+\left\|\rho_{g_{b}}^{-1} h\right\|_{L^{2}}\left\|\rho_{g_{b}}^{-1} \cdot v_{g}\right\|_{L^{2}}\left\|\rho_{g_{b}}^{2} \nabla^{g_{b}, 2} h\right\|_{C^{0}}\right) \\
& \leq \gamma\left(\left\|\rho_{g_{b}}^{-1} \cdot v_{g}\right\|_{L^{2}}^{2}+\left\|\nabla^{g_{b}} v_{g}\right\|_{L^{2}}^{2}\right)+C \gamma^{-1}\left(\left\|\nabla^{g_{b}} h\right\|_{L^{2}}^{2}+\left\|\rho_{g_{b}}^{-1} h\right\|_{L^{2}}^{2}\right),
\end{aligned}$$
where $C=C\left(n, g_{b}, \varepsilon\right)$ is a positive constant that may vary from line to line, and where we used the inequality $2\left\|\rho_{g_{b}}^{-1} h\right\|_{L^{2}}\left\|\rho_{g_{b}}^{-1} \cdot v_{g}\right\|_{L^{2}} \leq \gamma\left\|\rho_{g_{b}}^{-1} \cdot v_{g}\right\|_{L^{2}}^{2}+\gamma^{-1}\left\|\rho_{g_{b}}^{-1} h\right\|_{L^{2}}^{2}$. Here we have used Cauchy-Schwarz inequality together with the fact that $\nabla^{g_{b}, 2} h$ decays at least quadratically since $\|h\|_{C_{0}^{2}}$ is finite. To sum it up, (4.4) and (4.5) give by Hardy's inequality for any $\gamma>0$ :
$$\left\|\nabla^{g} v_{g}\right\|_{L^{2}}^{2} \leq \int_{N}\left|\mathrm{R}_{g}\right| v_{g}^{2} d \mu_{g}+C \gamma\left\|\nabla^{g} v_{g}\right\|_{L^{2}}^{2}+C \gamma^{-1}\left\|\nabla^{g_{b}} h\right\|_{L^{2}}^{2} .$$
By choosing $\gamma$ small enough together with the fact that $\sup _{N} \rho_{g_{b}}^{2}\left|\mathrm{R}_{g}\right|$ can be made arbitrarily small by shrinking $B_{C_{\tau}^{2, \alpha}}\left(g_{b}, \varepsilon\right)$ if necessary, Hardy's inequality yields:
$$\left\|\nabla^{g} v_{g}\right\|_{L^{2}}^{2} \leq \frac{1}{2}\left\|\nabla^{g} v_{g}\right\|_{L^{2}}^{2}+C\left(n, g_{b}, \varepsilon, \gamma\right)\left\|\nabla^{g_{b}} h\right\|_{L^{2}}^{2},$$
i.e. one gets (4.1) as expected.
Now, let us turn to the proof of (4.2).
We invoke the variation of equation (2.1) satisfied by the potential function $f_{g}$ established in [(3.11), Proposition 3.10].

Consequently, $\delta_{g_{t}} f(h)$ satisfies for $t \in[1,2]$ :
$$\Delta_{f_{g_{t}}}\left(\frac{\operatorname{tr}_{g_{t}} h}{2}-\delta_{g_{t}} f(h)\right)=\frac{1}{2}\left(\operatorname{div}_{g_{t}}\left(\operatorname{div}_{f_{g_{t}}} h\right)-\left\langle h, \operatorname{Ric}_{g_{g_{t}}}\left(g_{t}\right)\right\rangle_{g_{t}}\right) .$$
Now, thanks to Proposition 2.2 and the fact that $g \in B_{C_{\tau}^{2, \alpha}}\left(g_{b}, \varepsilon\right)$,
$$\rho_{g_{b}}\left|\nabla^{g_{t}} f_{g_{t}}\right|_{g_{t}}+\rho_{g_{b}}^{2}\left(\left|\operatorname{Ric}\left(g_{t}\right)\right|_{g_{t}}+\left|\nabla^{g_{t}, 2} f_{g_{t}}\right|_{g_{t}}\right) \leq C\left(n, g_{b}, \varepsilon\right) .$$

Once we multiply the previous elliptic equation (4.7) by $\delta_{g_{t}} f(h)-\frac{\operatorname{tr}_{g_{t}} h}{2}$, let us integrate by parts as follows:
$$\begin{aligned}
\left\|\nabla^{g_{t}}\left(\delta_{g_{t}} f(h)-\frac{\operatorname{tr}_{g_{t}} h}{2}\right)\right\|_{L^{2}\left(e^{-f_{g_{t}}} d \mu_{g_{t}}\right)}^{2}= & -\frac{1}{2} \int_{N}\left\langle\nabla^{g_{t}}\left(\delta_{g_{t}} f(h)-\frac{\operatorname{tr}_{g_{t}} h}{2}\right), \operatorname{div}_{g_{t}} h\right\rangle_{g_{t}} e^{-f_{g_{t}}} d \mu_{g_{t}} \\
& -\frac{1}{2} \int_{N}\left(\delta_{g_{t}} f(h)-\frac{\operatorname{tr}_{g_{t}} h}{2}\right)\left\langle h, \operatorname{Ric}_{f_{g_{t}}}\left(g_{t}\right)\right\rangle_{g_{t}} e^{-f_{g_{t}}} d \mu_{g_{t}} \\
= & : I_{1}+I_{2} .
\end{aligned}$$

The first integrals $I_{1}$ on the righthand side of the previous computation can be handled as follows:
$$\begin{aligned}
\left|I_{1}\right| \leq & \frac{1}{4}\left\|\nabla^{g_{t}}\left(\delta_{g_{t}} f(h)-\frac{\operatorname{tr}_{g_{t}} h}{2}\right)\right\|_{L^{2}\left(e^{-f_{g_{t}}} d \mu_{g_{t}}\right)}^{2}+C\left\|\operatorname{div}_{g_{t}} h\right\|_{L^{2}\left(d \mu_{g_{t}}\right)}^{2} \\
\leq & \frac{1}{4}\left\|\nabla^{g_{t}}\left(\delta_{g_{t}} f(h)-\frac{\operatorname{tr}_{g_{t}} h}{2}\right)\right\|_{L^{2}\left(e^{-f_{g_{t}}} d \mu_{g_{t}}\right)}^{2} \\
& +C\left(n, g_{b}, \varepsilon\right)\left(\left\|\nabla^{g_{t}} h\right\|_{L^{2}\left(d \mu_{g_{t}}\right)}^{2}+\left\|\rho_{g_{b}}^{-1}|h|_{g_{b}}\right\|_{L^{2}\left(d \mu_{g_{t}}\right)}^{2}\right) \\
\leq & \frac{1}{4}\left\|\nabla^{g_{t}}\left(\delta_{g_{t}} f(h)-\frac{\operatorname{tr}_{g_{t}} h}{2}\right)\right\|_{L^{2}\left(e^{-f_{g_{t}}} d \mu_{g_{t}}\right)}^{2}+C\left(n, g_{b}, \varepsilon\right)\left\|\nabla^{g_{t}} h\right\|_{L^{2}\left(d \mu_{g_{t}}\right)}^{2},
\end{aligned}$$
where we have used Young's inequality in the first line. The second inequality follows from (4.8) and the third inequality uses Hardy's inequality from Theorem 1.7 together with the fact that $g_{t}$ (and therefore $f_{g_{t}}$ by Proposition 2.2) is arbitrary close to 0 in the $C_{\tau}^{2, \alpha}$-topology.

The integral $I_{2}$ can be estimated from above in a similar way for any $t \in[1,2]$ and $\gamma \in(0,1)$ :
$$\begin{aligned}
\left|I_{2}\right| & \leq C\left(n, g_{b}, \varepsilon\right) \int_{N} \rho_{g_{b}}^{-2}\left|\delta_{g_{t}} f(h)-\frac{\operatorname{tr}_{g_{t}} h}{2}\right||h|_{g_{t}} d \mu_{g_{t}} \\
& \leq \gamma \int_{N} \rho_{g_{b}}^{-2}\left|\delta_{g_{t}} f(h)-\frac{\operatorname{tr}_{g_{t}} h}{2}\right|^{2} d \mu_{g_{t}}+C\left(\gamma, n, g_{b}, \varepsilon\right) \int_{N} \rho_{g_{b}}^{-2}|h|_{g_{t}}^{2} d \mu_{g_{t}} \\
& \leq \frac{1}{4}\left\|\nabla^{g_{t}}\left(\delta_{g_{t}} f(h)-\frac{\operatorname{tr}_{g_{t}} h}{2}\right)\right\|_{L^{2}\left(e^{-f_{g_{t}}} d \mu_{g_{t}}\right)}^{2}+C\left(\gamma, n, g_{b}, \varepsilon\right)\left\|\nabla^{g_{t}} h\right\|_{L^{2}\left(d \mu_{g_{t}}\right)},
\end{aligned}$$
if $\gamma=\gamma\left(n, g_{b}, \varepsilon\right)$ is chosen sufficiently small. Here, we have used Hardy's inequality in the last inequality.

Putting (4.9), (4.10) and (4.11) altogether lead to the expected estimate (4.2).
By considering the $L_{\frac{n}{2}+1}^{2}$ norm of (4.7), (4.3) follows by using Hardy's inequality and (4.8). \(\square\)

We conclude this section by stating a quantitative version of Proposition 4.1 whose proof is very similar and is therefore omitted:

Proposition 4.2. Let $\left(N^{n}, g_{b}\right)$ be an $A L E$ Ricci-flat metric asymptotic to $\mathbb{R}^{n} / \Gamma$, for some finite subgroup $\Gamma$ of $S O(n)$ acting freely on $\mathbb{S}^{n-1}$. Let $\tau \in\left(\frac{n-2}{2}, n-2\right)$ and $\alpha \in(0,1)$. Then there exists a neighborhood $B_{C_{\tau}^{2, \alpha}}\left(g_{b}, \varepsilon\right)$ of $g_{b}$ such that if $g_{1}$ and $g_{2}$ are metrics in $B_{C_{\tau}^{2, \alpha}}\left(g_{b}, \varepsilon\right)$ and $h \in C_{\tau}^{2, \alpha}$,
$$\begin{aligned}
\left\|\nabla^{g_{1}}\left(\delta_{g_{2}} f(h)-\delta_{g_{1}} f(h)\right)\right\|_{L^{2}} & \leq C\left(n, g_{b}, \varepsilon\right)\left\|g_{2}-g_{1}\right\|_{C_{\tau}^{2, \alpha}}\|h\|_{H_{\frac{n}{2}-1}^{2}}, \\
\left\|\Delta_{g_{1}, f_{g_{1}}}\left(\delta_{g_{2}} f(h)-\delta_{g_{1}} f(h)\right)\right\|_{L_{\frac{n}{2}+1}^{2}} & \leq C\left(n, g_{b}, \varepsilon\right)\left\|g_{2}-g_{1}\right\|_{C_{\tau}^{2, \alpha}}\|h\|_{H_{\frac{n}{2}-1}^{2}}
\end{aligned} .$$

\section*{5. Fredholm properties of the Lichnerowicz operator in weighted spaces}

Another motivation for our weighted Hölder spaces is that they ensure that the Lichnerowicz operator which controls the second variations of $\lambda_{\text {ALE }}$ has adequate Fredholm properties. Indeed, the Lichnerowicz operator $L_{g_{b}}: H^{2}\left(S^{2} T^{*} N\right) \rightarrow L^{2}\left(S^{2} T^{*} N\right)$ is symmetric and bounded, but is not Fredholm and does not have satisfying analytical properties. This becomes the case when considering weighted spaces.

Proposition 5.1 (Fredholm properties of the Lichnerowicz operator). Let $\left(N^{n}, g_{b}\right)$ be an ALE Ricci-flat metric, asymptotic to $\mathbb{R}^{n} / \Gamma$, for some finite subgroup $\Gamma \neq\{\operatorname{Id}\}$ of $S O(n)$ acting freely on $\mathbb{S}^{n-1}$. If $\beta \in(0, n-2) \cup(n-2, n)$, then
$$L_{g_{b}}: C_{\beta}^{2, \alpha}\left(S^{2} T^{*} N\right) \rightarrow C_{\beta+2}^{0, \alpha}\left(S^{2} T^{*} N\right)$$
is Fredholm for every $\alpha \in(0,1)$, and
$$L_{g_{b}}: H_{\beta}^{2}\left(S^{2} T^{*} N\right) \rightarrow L_{\beta+2}^{2}\left(S^{2} T^{*} N\right)$$
is Fredholm.
Moreover, if a 2 -tensor $h \in C_{\beta}^{2, \alpha}\left(S^{2} T^{*} N\right)$ is in the kernel of $L_{g_{b}}$, then $h \in C_{n}^{\infty}\left(S^{2} T^{*} N\right)$ and is divergence-free.

In dimension $n \geq 3$, the operator $L_{g_{b}}: H_{\frac{n}{2}-1}^{2}\left(S^{2} T^{*} N\right) \rightarrow L_{\frac{n}{2}+1}^{2}\left(S^{2} T^{*} N\right)$ is Fredholm and both its kernel and $L^{2}$-cokernel equal $\operatorname{ker}_{L^{2}} L_{g_{b}}$. As a consequence, there exists $C>0$ such that for any $h \perp_{L^{2}} \operatorname{ker}_{L^{2}} L_{g_{b}}$, we have the following control:
$$\left\|\nabla^{g_{b}, 2} h\right\|_{L_{\frac{n}{2}+1}^{2}} \leq\|h\|_{H_{\frac{n}{2}-1}^{2}} \leq C\left\|L_{g_{b}} h\right\|_{L_{\frac{n}{2}+1}^{2}} .$$

Remark 5.2. The statement holds for $\mathbb{R}^{n}$ if we additionally assume $\beta<n-1$.
Proof. The fact that the two operators are Fredholm is a consequence of the theory of elliptic operators between weighted Hölder spaces. Indeed, the elements of the kernel of the operator $-\nabla^{*} \nabla$ on a flat nontrivial quotient of $\mathbb{R}^{n}$ are sums of homogeneous 2-tensors of order $k$ or $-n+2-k$ for $k \in \mathbb{N} \backslash\{1\}$ where 1 is not in the set of possible values because there are no nonvanishing linear functions on $\mathbb{R}^{n}$ invariant by the group action induced by $\Gamma$.

Let us now consider a 2-tensor $h \in C_{\beta}^{2, \alpha}\left(S^{2} T^{*} N\right)$ which satisfies $L_{g_{b}} h=0$, then, since $\operatorname{div}_{g_{b}} L_{g_{b}}=\frac{1}{2}\left(\nabla^{g_{b}}\right)^{*} \nabla^{g_{b}} \operatorname{div}_{g_{b}}$, by the maximum principle, we have $\operatorname{div}_{g_{b}} h=0$. At infinity, we have $h=H^{n-2}+O\left(\rho_{g_{b}}^{-n+2-\epsilon}\right)$ for a harmonic homogeneous 2-tensor $H^{n-2} \sim \rho_{g_{b}}^{-n+2}$. Now, such a divergence-free 2-tensor $H^{n-2}$ must vanish by [Ozu19, Lemma 4.1]. We therefore have $h=O\left(\rho_{g_{b}}^{-n+2-\epsilon}\right)$, and since the next decay rate in the kernel of $-\nabla^{*} \nabla$ is $\rho_{g_{b}}^{-n}$, we have $h \in C_{n}^{\infty}\left(S^{2} T^{*} N\right)$.

For the weighted Sobolev spaces, the operator
$$L_{g_{b}}: H_{\frac{n}{2}-1}^{2}\left(S^{2} T^{*} N\right) \rightarrow L_{\frac{n}{2}+1}^{2}\left(S^{2} T^{*} N\right)$$
whose kernel is the kernel of $L_{g_{b}}$ on $H_{\frac{n}{2}-1}^{2}\left(S^{2} T^{*} N\right)$ is reduced to the $L^{2}$-kernel of $L_{g_{b}}$ because there is no exceptional value between $\frac{n}{2}-1$ and $n-2$. Its cokernel is the kernel of $L_{g_{b}}$ on $L_{\frac{n}{2}-1}^{2}\left(S^{2} T^{*} N\right) \approx\left(L_{\frac{n}{2}+1}^{2}\left(S^{2} T^{*} N\right)\right)^{*}$ (see Note 5.3 below) which is also equal to $\operatorname{ker}_{L^{2}} L_{g_{b}}$. This operator is in particular of index 0 . By Banach bounded inverse theorem, this implies that there exists $C>0$ depending on $g_{b}$ such that for any $h \perp \operatorname{ker}_{L^{2}} L_{g_{b}}$, we have
$$\left\|\nabla^{g_{b}, 2} h\right\|_{L_{\frac{n}{2}+1}^{2}} \leq\|h\|_{H_{\frac{n}{2}-1}^{2}} \leq C\left\|L_{g_{b}} h\right\|_{L_{\frac{n}{2}+1}^{2}} .$$
Note that the $L^{2}$-product is well-defined between elements of $L_{\frac{n}{2}-1}^{2}\left(S^{2} T^{*} N\right)$ and elements of $\operatorname{ker}_{L^{2}} L_{g_{b}} \subset C_{n}^{0}\left(S^{2} T^{*} N\right) \subset L_{\frac{n}{2}+1}^{2}\left(S^{2} T^{*} N\right)$. \(\square\)

Note 5.3. For any $s \in \mathbb{R}$, the dual of $L_{\frac{n}{2}+s}^{2}$ classically identifies with $L_{\frac{n}{2}-s}^{2}$ because by definition, this is the set of tensors for which the $L^{2}$-product is defined for any 2-tensor in $L_{\frac{n}{2}+s}^{2}$. We therefore define the $L^{2}$-cokernel of a symmetric operator $H_{\frac{n}{2}+s-2}^{2} \mapsto L_{\frac{n}{2}+s}^{2}$ as its kernel on the dual of its image: $L_{\frac{n}{2}-s}^{2}$. This is the $L^{2}$-orthogonal of its image.

We keep this definition on subsets of $L_{\frac{n}{2}+s}^{2}$, for instance, consider a smooth elliptic operator $L$ asymptotic to the Euclidean Laplacian at infinity between $C_{\frac{n}{2}+s-2}^{2, \alpha}$ and $C_{\frac{n}{2}+s}^{0, \alpha} \subset L_{\frac{n}{2}+s-\epsilon}^{2}$ for all $\epsilon>0$. Assume moreover that $\frac{n}{2}+s$ is not a critical exponent of the Laplacian. Then, the $L^{2}$-cokernel of $L$ is the kernel of $L$ on $C_{\frac{n}{2}-s}^{0, \alpha}$. Indeed, by the above discussion, we first identify it with the kernel on $L_{\frac{n}{2}-s+\epsilon}^{2}$ which by elliptic regularity is the kernel on $H_{\frac{n}{2}-s+\epsilon}^{k}$ for all $k$. For $k$ large enough, this embeds in $C_{\frac{n}{2}-s+\epsilon}^{0, \alpha}$, and finally, by choosing $\epsilon$ small enough so that there is no critical exponent of the Laplacian in $\left[\frac{n}{2}-s, \frac{n}{2}-s+\epsilon\right]$, this is also the kernel of $L$ on $C_{\frac{n}{2}-s}^{0, \alpha}$.

\section*{6. Properties of $\lambda_{\text {ALE }}$ in the integrable case}

Now that we have proved that the functional is well-defined and well-behaved in relevant function spaces, we start by investigating the stable integrable case (which corresponds to all known examples) first where a Lojasiewicz inequality can be proved "by hand".
6.1. Integrability of Ricci-flat ALE metrics. We say that a Ricci-flat ALE metric $\left(N^{n}, g_{b}\right)$ is integrable if the moduli space of Ricci-flat ALE metric on $N$ with the same cone at infinity is a smooth manifold around $g_{b}$.

Definition 6.1 (Integrable Ricci-flat ALE metric). A Ricci-flat ALE metric ( $N^{n}, g_{b}$ ) is integrable if for all $v \in \operatorname{ker}_{L^{2}} L_{g_{b}}$ small enough, there exists a (unique) Ricci-flat ALE metric $\bar{g}_{v}$ satisfying $\bar{g}_{v}-\left(g_{b}+v\right) \perp \operatorname{ker}_{L^{2}} L_{g_{b}}$, and such that $\operatorname{div}_{g_{b}} \bar{g}_{v}=0$ and $\left\|\bar{g}_{v}-g_{b}\right\|_{C_{n}^{2, \alpha}} \leq 2\|v\|_{C_{n}^{2, \alpha}}$.

We will need the following description of the neighborhood of an integrable Ricci-flat ALE metric to restrict ourselves to deformations which are transverse to the Ricci-flat deformations.

Proposition 6.2. Let $n \geqslant 4$ and $\left(N^{n}, g_{b}\right)$ be an integrable ALE Ricci-flat metric, asymptotic to $\mathbb{R}^{n} / \Gamma$, for some finite subgroup $\Gamma$ of $S O(n)$ acting freely on $\mathbb{S}^{n-1}$. Let $\tau \in(1, n)$ and $\alpha \in(0,1)$. Then there exist $C>0$ and $\varepsilon>0$ such that for any metric $g$ satisfying $\| g-$ $g_{b} \|_{C_{\tau}^{2, \alpha}\left(g_{b}\right)} \leq \epsilon$, there exists a Ricci-flat ALE metric $g_{b}^{\prime}$ such that
\begin{itemize}
\item[-] $\left\|g_{b}-g_{b}^{\prime}\right\|_{C_{n}^{2, \alpha}\left(g_{b}\right)} \leq C\left\|g-g_{b}\right\|_{C_{\tau}^{2, \alpha}\left(g_{b}\right)}$,
\item[-] $g-g_{b}^{\prime} \perp_{L^{2}\left(g_{b}^{\prime}\right)} \operatorname{ker}_{L^{2}\left(g_{b}^{\prime}\right)} L_{g_{b}^{\prime}}$, and
\item[-] $\operatorname{div}_{g_{b}^{\prime}} g=0$.
\end{itemize}
Proof. According to [Ozu19, Corollary 5.16] and Definition 6.1, the integrability assumption rewrites in the following way. For any $v \in \operatorname{ker}_{L^{2}\left(g_{b}\right)} L_{g_{b}}$, there exists a unique Ricci-flat ALE metric $\bar{g}_{v}$ satisfying
\begin{itemize}
\item[(1)] $\operatorname{div}_{g_{b}} \bar{g}_{v}=0$,
\item[(2)] $\bar{g}_{v}-\left(g_{b}+v\right) \perp \operatorname{ker}_{L^{2}} L_{g_{b}}$,
\item[(3)] $\operatorname{Ric}\left(\bar{g}_{v}\right)=0$.
\end{itemize}
Moreover, since these metrics are obtained from the implicit function theorem, Lemma A.2, applied to $(v, g) \mapsto \operatorname{Ric}(g)+\frac{1}{2} \mathcal{L}_{\operatorname{div}_{g_{b}} \bar{g}_{v}} g$ seen as an operator from $\left(\operatorname{ker}_{L^{2}} L_{g_{b}}\right) \times C_{\tau}^{2, \alpha}$ to $C_{\tau+2}^{0, \alpha}$
for $\tau \in\left(\frac{n-2}{2}, n-2\right)$, they consequently vary analytically in $v$. Similarly, the elements of $\operatorname{ker}_{L^{2}\left(\bar{g}_{v}\right)} L_{\bar{g}_{v}}$ vary analytically in $v$ as solutions $h \in L^{2}\left(g_{b}\right)$ of the parametrized equation $(v, h) \mapsto L_{\bar{g}_{v}} h=0$.

According to Proposition B. 2 which is proved by implicit function theorem, for any $\alpha \in$ $(0,1)$, there exists $\varepsilon>0$ for which for any metric $g \in B_{C_{\tau}^{2, \alpha}}\left(g_{b}, \varepsilon\right)$ and any $v \in \operatorname{ker}_{L^{2}} L_{g_{b}}$, there exists a unique vector field $X(g, v) \in C_{\tau-1}^{2+1, \alpha}(T N)$ depending analytically on $g$ and $v$ for which
$$\operatorname{div}_{\left(\exp _{X(g, v)}\right) * \bar{g}_{v}} g=0,$$
where $\exp _{X} g: x \mapsto \exp _{x}^{g}(X(x))$. Define $\phi_{g, v}:=\left(\exp _{X(g, v)}\right)^{-1}$. We will naturally look for a 2-tensor $v$ such that $g-\phi_{g, v}^{*} \bar{g}_{v} \perp \operatorname{ker}_{L^{2}\left(\phi_{g, v}^{*} \bar{g}_{v}\right)} L_{\phi_{g, v}^{*} \bar{g}_{v}}$, where the $L^{2}$-scalar product is defined with respect to $\phi_{g, v}^{*} \bar{g}_{v}$ and such that the elements of $\operatorname{ker}_{L^{2}\left(\phi_{g, v}^{*} \bar{g}_{v}\right)} L_{\phi_{g, v}^{*} \bar{g}_{v}}$ vary analytically in $v$.

Let us therefore consider the analytic map
$$F:(g, v) \mapsto \pi^{\phi_{g, v}^{*} \bar{g}_{v}}\left(\phi_{g, v}^{*} \bar{g}_{v}-g\right),$$
where $\pi^{\phi_{g, v}^{*} \bar{g}_{v}}$ is the $L^{2}\left(\phi_{g, v}^{*} \bar{g}_{v}\right)$-orthogonal projection on $\operatorname{ker}_{L^{2}\left(\phi_{g, v}^{*} \bar{g}_{v}\right)} L_{\phi_{g, v}^{*} \bar{g}_{v}}$. Note that this projection is smooth on $C_{\tau}^{2, \alpha}$ for $\tau>0$ since the elements of $\operatorname{ker}_{L^{2}\left(\phi_{g, v}^{*} \bar{g}_{v}\right)} L_{\phi_{g, v}^{*} g_{\bar{v}}}$ decay like $\rho_{g_{b}}^{-n}$ at infinity.

We consider $F$ on a neighborhood of $\left(g_{b}, 0\right)$ in $C_{\tau}^{2, \alpha} \times \operatorname{ker}_{L^{2}\left(g_{b}\right)} L_{g_{b}}$ with values in $\operatorname{ker}_{L^{2}\left(\phi_{g, v}^{*} \bar{g}_{v}\right)} L_{\phi_{g, v}^{*} \bar{g}_{v}}$. Here the map $F$ is analytic. We can apply the implicit function theorem as stated in Lemma A. 2 to the map $F$. Indeed, $F\left(g_{b}, 0\right)=0$ and $d_{\left(g_{b}, 0\right)} F(0, v)=v$ is an isomorphism, and the spaces $C_{\tau}^{2, \alpha} \times \operatorname{ker}_{L^{2}\left(g_{b}\right)} L_{g_{b}}$ and $\operatorname{ker}_{L^{2}\left(\phi_{g, v}^{*} \bar{g}_{v}\right)} L_{\phi_{g, v}^{*} \bar{g}_{v}}$ are Banach spaces. We then conclude that there exists an analytic map (unique as a continuous map) $V$ such that for all metrics $g$ in a $C_{\tau}^{2, \alpha}$-neighborhood of $g_{b}$, we have
$$F(g, V(g))=0 .$$
Now, for any $g$ satisfying $\left\|g-g_{b}\right\|_{C_{\tau}^{2, \alpha}\left(g_{b}\right)} \leq \epsilon$ for $\epsilon>0$ small enough, we consider $g_{b}^{\prime}=$ $\phi_{g, V(g)}^{*} \bar{g}_{V(g)}$ which satisfies the desired properties. \(\square\)

Remark 6.3. The integrability of the Ricci-flat ALE metric ( $N^{n}, g_{b}$ ) is crucial to obtain the above statement.

Next, we prove that if a Ricci-flat ALE metric is stable and integrable then it is a local maximum of $\lambda_{\text {ALE }}$ : this result echoes [Theorem $A$, [Has12]]. Before stating and proving this result, we make a pause to discuss the relevant notion of stability we need here:

Definition 6.4 (Locally stable integrable Ricci-flat ALE metrics). An integrable Ricci-flat ALE metric $\left(N^{n}, g_{b}\right)$ is locally stable if for any metric $g$ satisfying $\left\|g-g_{b}\right\|_{C_{\tau}^{2, \alpha}\left(g_{b}\right)} \leq \epsilon$ for $\epsilon>0$ small enough, there exists a linearly stable Ricci-flat ALE metric $g_{b}^{\prime}$ satisfying the conclusions of Proposition 6.2 .

Let us show that being linearly stable and integrable implies being locally stable.
Proposition 6.5. Let $\left(N^{n}, g_{b}\right)$ be an integrable and linearly stable ALE Ricci-flat metric. Then it is locally stable in the sense of Definition 6.4.

Proof. Denote $\bar{g}_{0}:=g_{b}$ and for $v \in \operatorname{ker}_{L^{2}\left(\bar{g}_{0}\right)} L_{\bar{g}_{0}}$ small enough, let $\bar{g}_{v}$ be a Ricci-flat ALE metric satisfying $\bar{g}_{v}-\left(\bar{g}_{0}+v\right) \perp \operatorname{ker}_{L^{2}} L_{\bar{g}_{0}}$ and $\operatorname{div}_{\bar{g}_{0}} \bar{g}_{v}=0$ since $\bar{g}_{0}$ is assumed to be integrable. The
map $v \in C_{\tau}^{2, \alpha} \rightarrow \bar{g}_{v} \in C_{\tau}^{2, \alpha}$ is analytic: as already seen in the proof of Proposition 6.2, this implies that there exists a basis of each $\operatorname{ker}_{L^{2}\left(\bar{g}_{v}\right)} L_{\bar{g}_{v}}$ which depends analytically on $v$. Therefore, the $L^{2}\left(\bar{g}_{v}\right)$-projection on $\operatorname{ker}_{L^{2}\left(\bar{g}_{v}\right)} L_{\bar{g}_{v}}$ denoted by $\pi_{v}: H_{\frac{n}{2}-1}^{1}\left(\bar{g}_{0}\right) \rightarrow H_{\frac{n}{2}-1}^{1}\left(\bar{g}_{0}\right)$ depends analytically on $v$ since $\operatorname{ker}_{L^{2}\left(\bar{g}_{v}\right)} L_{\bar{g}_{v}} \subset C_{n}^{\infty}$ by Theorem 5.1.

As $\bar{g}_{0}$ is assumed to be linearly stable, thanks to Lemma 3.18, there exists $c>0$ such that if $h_{0} \perp \operatorname{ker}_{L^{2}\left(\bar{g}_{0}\right)} L_{\bar{g}_{0}}$ and $h_{0} \in H_{\frac{n}{2}-1}^{1}$, then one has
$$\left\langle-L_{\bar{g}_{0}} h_{0}, h_{0}\right\rangle_{L^{2}} \geq c\left\|\nabla^{\bar{g}_{0}} h_{0}\right\|_{L^{2}}^{2},$$
by Theorem 3.19.
Now, if $h \perp \operatorname{ker}_{L^{2}\left(\bar{g}_{v}\right)} L_{\bar{g}_{v}}$ and $h \in C_{c}^{\infty}\left(S^{2} T^{*} N\right)$, we decompose it as $h=h_{0}+h^{\prime}$ where $h_{0} \perp \operatorname{ker}_{L^{2}\left(\bar{g}_{0}\right)} L_{\bar{g}_{0}}$ and $h^{\prime} \in \operatorname{ker}_{L^{2}\left(\bar{g}_{0}\right)} L_{\bar{g}_{0}}$.

Let us first show that $h^{\prime}$ is small when $v$ is. We have $0=\pi_{v} h$ and $h^{\prime}=\pi_{0} h$, and since $v \mapsto \pi_{v}$ is analytic, there exists $C>0$ such that for $v$ small enough, one has $\left\|h^{\prime}\right\|_{H_{\frac{n}{2}-1}^{1}\left(\bar{g}_{0}\right)} \leq$ $\|v\|_{C_{\tau}^{2, \alpha}}\|h\|_{H_{\frac{n}{2}-1}^{1}\left(\bar{g}_{0}\right)}$.

Using the fact that $h^{\prime} \in \operatorname{ker}_{L^{2}\left(\bar{g}_{0}\right)} L_{\bar{g}_{0}}$, one gets immediately that
$$\begin{aligned}
\left\langle-L_{\bar{g}_{0}} h, h\right\rangle_{L^{2}\left(\bar{g}_{0}\right)} & =\left\langle-L_{\bar{g}_{0}} h_{0}, h_{0}\right\rangle_{L^{2}\left(\bar{g}_{0}\right)} \\
& \geq c\left\|\nabla^{\bar{g}_{0}} h_{0}\right\|_{L^{2}\left(\bar{g}_{0}\right)}^{2},
\end{aligned}$$
where we used the inequality (6.1).
In particular, if $\|v\|_{C_{\tau}^{2, \alpha}}$ is chosen small enough, then we have $\left\|\nabla^{\bar{g}_{0}} h_{0}\right\|_{L^{2}\left(\bar{g}_{0}\right)} \geq\left\|\nabla^{\bar{g}_{0}} h\right\|_{L^{2}\left(\bar{g}_{0}\right)}-$ $\left\|\nabla^{\bar{g}_{0}} h^{\prime}\right\|_{L^{2}\left(\bar{g}_{0}\right)} \geq \frac{1}{\sqrt{2}}\left\|\nabla^{\bar{g}_{0}} h\right\|_{L^{2}\left(\bar{g}_{0}\right)}$ and $\left\|\nabla^{\bar{g}_{0}} h\right\|_{L^{2}\left(g_{0}\right)}^{2} \geqslant \frac{1}{2}\left\|\nabla^{\bar{g}_{v}} h\right\|_{L^{2}\left(\bar{g}_{v}\right)}^{2}$ since $\left\|\bar{g}_{v}-\bar{g}_{0}\right\|_{C_{n}^{2, \alpha}} \leq$ $2\|v\|_{C_{n}^{2, \alpha}}$ by Definition 6.1. Therefore,
$$\left\langle-L_{\bar{g}_{0}} h, h\right\rangle_{L^{2}\left(\bar{g}_{0}\right)} \geq c\left\|\nabla^{\bar{g}_{0}} h\right\|_{L^{2}\left(\bar{g}_{0}\right)}^{2} \geqslant \frac{c}{4}\left\|\nabla^{\bar{g}_{v}} h\right\|_{L^{2}\left(\bar{g}_{v}\right)}^{2},$$
where $c$ is a positive constant independent of $v$ and $h$ that may vary from line to line. On the other hand, by linearizing $L_{\bar{g}_{0}}$ with respect to $L_{\bar{g}_{v}}$, we have
$$\begin{aligned}
\left|\left\langle\left(L_{\bar{g}_{0}}-L_{\bar{g}_{v}}\right) h, h\right\rangle_{L^{2}\left(\bar{g}_{v}\right)}\right| \leq & \left|\left\langle\left(\Delta_{\bar{g}_{0}}-\Delta_{\bar{g}_{v}}\right) h, h\right\rangle_{L^{2}\left(\bar{g}_{v}\right)}\right|+2\left|\left\langle\left(\operatorname{Rm}\left(\bar{g}_{0}\right)-\operatorname{Rm}\left(\bar{g}_{v}\right)\right) * h, h\right\rangle_{L^{2}\left(\bar{g}_{v}\right)}\right| \\
\leq & \sum_{i=0}^{2}\left\langle\nabla^{\bar{g}_{v}, i}\left(\bar{g}_{0}-\bar{g}_{v}\right) * \nabla^{\bar{g}_{v}, 2-i} h, h\right\rangle_{L^{2}\left(\bar{g}_{v}\right)} \\
\leq & C\left\|\bar{g}_{v}-\bar{g}_{0}\right\|_{C_{n}^{2, \alpha}} \sum_{i=1}^{2}\left\|\rho_{\bar{g}_{0}}^{-i} \nabla^{\bar{g}_{0}, 2-i} h * h\right\|_{L^{1}\left(\bar{g}_{0}\right)} \\
& +\left\langle\nabla^{\bar{g}_{v}}\left(\bar{g}_{0}-\bar{g}_{v}\right) * \nabla^{\bar{g}_{v}} h, h\right\rangle_{L^{2}\left(\bar{g}_{v}\right)}+\left\langle\left(\bar{g}_{0}-\bar{g}_{v}\right) * \nabla^{\bar{g}_{v}} h * \nabla^{\bar{g}_{v}} h\right\rangle_{L^{2}\left(\bar{g}_{v}\right)} \\
\leq & C\|v\|_{C_{n}^{2, \alpha}}\left\|\nabla^{\bar{g}_{v}} h\right\|_{L^{2}\left(\bar{g}_{v}\right)}^{2},
\end{aligned}$$
for some positive constant $C$ independent of $v$ and $h$. Here we have used the density of $C_{c}^{\infty}$ in $H_{\frac{n}{2}-1}^{1}$, integration by parts in the third inequality and Hardy's inequality (Theorem 1.7) in the last line.

Combining (6.2) and (6.3), one gets for $v$ small enough, and for some constant $c>0$ independent on $v$ and $h$ :
$$\left\langle-L_{\bar{g}_{v}} h, h\right\rangle_{L^{2}\left(\bar{g}_{v}\right)} \geq c\left\|\nabla^{\bar{g}_{v}} h\right\|_{L^{2}\left(\bar{g}_{v}\right)}^{2},$$
for any $h \perp \operatorname{ker}_{L^{2}\left(\bar{g}_{v}\right)} L_{\bar{g}_{v}}$. This shows that $\bar{g}_{v}$ is also linearly stable. \(\square\)

Notice that all known examples of 4-dimensional Ricci flat ALE metrics are hyperkähler which implies that they are integrable. Furthermore, each infinitesimal deformation lying in the kernel of the corresponding Lichnerowicz operator is the first jet of a curve of hyperkähler metrics. Since a hyperkähler metric is linearly stable, an ALE hyperkähler metric is integrable and locally stable in the sense of Definition 6.4: see [Bes07, Section 11, Chapter 12] for more details.

Proposition 6.6. Let $\left(N^{n}, g_{b}\right), n \geq 4$, be an $A L E$ Ricci-flat metric asymptotic to $\mathbb{R}^{n} / \Gamma$, for some finite subgroup $\Gamma$ of $S O(n)$ acting freely on $\mathbb{S}^{n-1}$. Let $\tau \in\left(\frac{n-2}{2}, n-2\right)$ and let $\alpha \in(0,1)$. If $\left(N^{n}, g_{b}\right)$ is assumed to be integrable and linearly stable then it is a local maximum for the energy $\lambda_{\text {ALE }}$ with respect to the topology defined by $C_{\tau}^{2, \alpha}\left(S^{2} T^{*} N\right)$.

Proof. Consider the following Taylor expansion of the functional $\lambda_{\text {ALE }}$ at $g_{b}$ of order 3:
$$\lambda_{\mathrm{ALE}}\left(g_{b}+h\right)=\lambda_{\mathrm{ALE}}\left(g_{b}\right)+\delta_{g_{b}} \lambda_{\mathrm{ALE}}(h)+\delta_{g_{b}}^{2} \lambda_{\mathrm{ALE}}(h, h)+\int_{0}^{1} \frac{(1-t)^{2}}{2} \delta_{g_{b}+t h}^{3} \lambda_{\mathrm{ALE}}(h, h, h) d t .$$
Now, by definition of $\lambda_{\text {ALE }}, \lambda_{\text {ALE }}\left(g_{b}\right)=0$ and by (2.8), one has $\delta_{g_{b}} \lambda_{\text {ALE }}(h)=0$ as well by Proposition 3.4. Finally, by Proposition 2.7, $\delta_{g_{b}}^{2} \lambda_{\mathrm{ALE}}(h, h)=\frac{1}{2}\left\langle L_{g_{b}} h, h\right\rangle_{L^{2}}$ if $\operatorname{div}_{g_{b}} h=0$. Since $\left(N^{n}, g_{b}\right)$ is integrable and linearly stable, it is integrable and locally stable by Proposition 6.5 and thanks to Theorem 3.19 and Proposition 6.2, it suffices to estimate the integral on the righthand side of (6.5) in such a way that it can be absorbed by $\left\|\nabla^{g_{b}} h\right\|_{L^{2}}^{2}$. More precisely, we claim the following:

Claim 2.
$$\left|\delta_{g_{b}+t h}^{3} \lambda_{\mathrm{ALE}}(h, h, h)\right| \leq C\|h\|_{C_{\tau}^{2, \alpha}}\left\|\nabla^{g_{b}} h\right\|_{L^{2}}^{2}, \quad \operatorname{div}_{g_{b}} h=0,$$
for some positive constant $C=C\left(n, g_{b}, \varepsilon\right)$ uniform in $t \in[0,1]$.
Proof of Claim 2. Recall from (2.8) that:
$$\delta_{g_{b}+t h}^{3} \lambda_{\mathrm{ALE}}(h, h, h)=-\frac{d^{2}}{d t^{2}} \int_{N}\left\langle\operatorname{Ric}\left(g_{b}+t h\right)+\nabla^{g_{b}+t h, 2} f_{g_{b}+t h}, h\right\rangle_{g_{b}+t h} e^{-f_{g_{b}+t h}} d \mu_{g_{b}+t h}$$
Denote the curve of metrics $\left(g_{b}+t h\right)_{t \in[0,1]}$ by $\left(g_{t}\right)_{t \in[0,1]}$ : the family $\left(g_{t}\right)_{t \in[0,1]}$ is uniformly equivalent in $t \in[0,1]$ since $g_{t}$ lies in an arbitrarily small neighborhood of $g_{b}$ in the $C_{\tau}^{2, \alpha}$ topology. Moreover, Proposition 2.2 ensures that $\left\|f_{g_{t}}\right\|_{C_{\tau}^{2, \alpha}} \leq \varepsilon\left(\left\|g_{t}-g_{b}\right\|_{C_{\tau}^{2, \alpha}}\right)$, where $\varepsilon(\cdot)$ is a positive function on $[0,+\infty)$ that tends to 0 as its argument goes to 0. Notice by [(C.2), Lemma C. 1 applied to $g_{1}:=g_{b}$ and $g_{2}:=g_{b}+h$, that the Bianchi gauge satisfies:
$$\begin{aligned}
B & =\operatorname{div}_{g_{1}}\left(g_{t}-g_{1}\right)-\frac{1}{2} \nabla^{g_{1}} \operatorname{tr}_{g_{1}}\left(g_{t}-g_{1}\right)+g_{t}^{-1} *\left(g_{t}-g_{1}\right) * \nabla^{g_{1}} g_{t} \\
& =-\frac{t}{2} \nabla^{g_{b}} \operatorname{tr}_{g_{b}} h+t^{2} g_{t}^{-1} * h * \nabla^{g_{b}} h,
\end{aligned}$$
since $\operatorname{div}_{g_{b}} h=0$. Finally, since $\nabla^{g_{t}} T=\nabla^{g_{b}} T+g_{t}^{-1} * \nabla^{g_{b}}\left(g_{t}-g_{b}\right) * T$ for any tensor $T$, one gets
$$\begin{aligned}
\mathscr{L}_{B}\left(g_{t}\right) & =-t \nabla^{g_{b}, 2} \operatorname{tr}_{g_{b}} h+t^{2} \nabla^{g_{b}}\left(g_{t}^{-1} * h * \nabla^{g_{b}} h\right) \\
& +t g_{t}^{-1} * \nabla^{g_{b}} h *\left(-\frac{t}{2} \nabla^{g_{b}} \operatorname{tr}_{g_{b}} h+t^{2} g_{t}^{-1} * h * \nabla^{g_{b}} h\right) .
\end{aligned}$$

Moreover, it can be shown with the help of Lemmata C. 1 and C. 2 that:
$$\left|-2 \operatorname{Ric}\left(g_{t}\right)-t L_{g_{b}} h-t \nabla^{g_{b}, 2} \operatorname{tr}_{g_{b}} h\right| \lesssim\left|\operatorname{Rm}\left(g_{b}\right)\right|_{g_{b}}|h|_{g_{b}}^{2}+\left|\nabla^{g_{b}} h\right|_{g_{b}}^{2}+|h|_{g_{b}}\left|\nabla^{g_{b}, 2} h\right|_{g_{b}},$$
and similarly,
$$\left|-2 \partial_{t} \operatorname{Ric}\left(g_{t}\right)-L_{g_{b}} h-\nabla^{g_{b}, 2} \operatorname{tr}_{g_{b}} h\right| \lesssim\left|\operatorname{Rm}\left(g_{b}\right)\right|_{g_{b}}|h|_{g_{b}}^{2}+\left|\nabla^{g_{b}} h\right|_{g_{b}}^{2}+|h|_{g_{b}}\left|\nabla^{g_{b}, 2} h\right|_{g_{b}},$$
where the symbol $\lesssim$ denotes less than or equal to up to a positive multiplicative constant uniform in $t \in[0,1]$ which might depend on $n, g_{b}, \varepsilon$.

By [(C.4), Lemma C.1],
$$\begin{aligned}
\left|\int_{N}\left\langle\frac{\partial^{2}}{\partial t^{2}} \operatorname{Ric}\left(g_{t}\right), h\right\rangle_{g_{t}} e^{-f_{g_{t}}} d \mu_{g_{t}}\right| & \lesssim \int_{N}|h|_{g_{b}}^{2}\left|\nabla^{g_{b}, 2} h\right|_{g_{b}}+\left|\operatorname{Rm}\left(g_{b}\right)\right||h|_{g_{b}}^{3}+\left|\nabla^{g_{b}} h\right|_{g_{b}}^{2}|h|_{g_{b}} d \mu_{g_{b}} \\
& \lesssim\left(\left\|\nabla^{g_{b}, 2} h\right\|_{C_{2}^{0}}+\|h\|_{C_{0}^{0}}\right)\left\|\rho_{g_{b}}^{-1} h\right\|_{L^{2}}^{2}+\|h\|_{C_{0}^{0}}\left\|\nabla^{g_{b}} h\right\|_{L^{2}}^{2} \\
& \lesssim\|h\|_{C_{\tau}^{2}}\left\|\nabla^{g_{b}} h\right\|_{L^{2}}^{2},
\end{aligned}$$
where we have used Hardy's inequality that holds on $\left(N^{n}, g_{b}\right)$ thanks to Theorem 1.7. A similar estimate holds for mixed derivatives with respect to the parameter $t \in[0,1]$ that involve the terms $\operatorname{Ric}\left(g_{t}\right)$, the scalar product on symmetric 2-tensors induced by $g_{t}$ and the Riemannian volume $d \mu_{g_{t}}$.

We use Proposition 2.2 that ensures that
$$\left\|\delta_{g_{t}}^{k} f(h, \ldots, h)\right\|_{C_{\tau}^{2, \alpha}} \leq C\left(\left\|g_{t}-g_{b}\right\|_{C_{\tau}^{2, \alpha}}\right)\|h\|_{C_{\tau}^{2, \alpha}}^{k}, \quad k \geq 0,$$
to handle the derivatives falling on $e^{-f_{g_{t}}}$.
For instance, let us handle the term involving $\left\langle\partial_{t} \operatorname{Ric}\left(g_{t}\right), h\right\rangle_{g_{t}} \delta_{g_{t}} f(h)$ as follows:
$$\begin{aligned}
\left|\int_{N}\left\langle\partial_{t} \operatorname{Ric}\left(g_{t}\right), h\right\rangle_{g_{t}} \delta_{g_{t}} f(h) e^{-f_{g_{t}}} d \mu_{g_{t}}\right| \lesssim & \left|\int_{N}\left\langle L_{g_{b}} h+\nabla^{g_{b}, 2} \operatorname{tr}_{g_{b}} h, h\right\rangle_{g_{b}} \delta_{g_{t}} f(h) e^{-f_{g_{t}}} d \mu_{g_{b}}\right| \\
& +\|h\|_{C_{\tau}^{2, \alpha}} \int_{N}\left|\operatorname{Rm}\left(g_{b}\right)\right|{ }_{g_{b}}|h|_{g_{b}}^{2}+\left|\nabla^{g_{b}} h\right|_{g_{b}}^{2} d \mu_{g_{b}} \\
& +\|h\|_{C_{\tau}^{2, \alpha}} \int_{N}|h|_{g_{b}}^{2}\left|\nabla^{g_{b}, 2} h\right|_{g_{b}} d \mu_{g_{b}} \\
\lesssim & \left|\int_{N}\left\langle\Delta_{g_{b}} h+\nabla^{g_{b}, 2} \operatorname{tr}_{g_{b}} h, h\right\rangle_{g_{b}} \delta_{g_{t}} f(h) e^{-f_{g_{t}}} d \mu_{g_{b}}\right| \\
& +\|h\|_{C_{\tau}^{2, \alpha}}\left\|\nabla^{g_{b}} h\right\|_{L^{2}}^{2} .
\end{aligned}$$
Here we have used Hardy's inequality in the first line to get rid of the zeroth order term appearing in the Lichnerowicz operator, in the first term of the second line by using that the curvature $\operatorname{Rm}\left(g_{b}\right)$ decays at least quadratically and in the third line invoking the quadratic decay of $\nabla^{g_{b}, 2} h$. Finally, the weighted Riemannian measure $e^{-f_{g_{t}}} d \mu_{g_{t}}$ on the righthand side of the first line has been turned into $d \mu_{g_{b}}$ since they are uniformly equivalent as measures by (6.10) and the fact that $g_{b}+h$ and $g_{b}$ are uniformly equivalent as metrics. Notice that we have only made use of $h \in C_{0}^{2}$ here.

It remains to estimate the terms involving the second covariant derivatives of $h$ : by integration by parts,
$$\begin{aligned}
\left|\int_{N}\left\langle\Delta_{g_{b}} h, h\right\rangle_{g_{b}} \delta_{g_{t}} f(h) e^{-f_{g_{t}}} d \mu_{g_{b}}\right| \lesssim & \int_{N}\left|\nabla^{g_{b}} h\right|_{g_{b}}^{2}\left|\delta_{g_{t}} f(h)\right|+\left|\nabla^{g_{b}} h\right|_{g_{b}}|h|_{g_{b}}\left|\nabla^{g_{b}} \delta_{g_{t}} f(h)\right|_{g_{b}} d \mu_{g_{b}} \\
& +\int_{N}\left|\nabla^{g_{b}} h\right|_{g_{b}}|h|_{g_{b}}\left|\delta_{g_{t}} f(h) \| \nabla^{g_{b}} f_{g_{t}}\right| g_{b} d \mu_{g_{b}} \\
\lesssim & \|h\|_{C_{\tau}^{2, \alpha}}\left\|\nabla^{g_{b}} h\right\|_{L^{2}}^{2}+\|h\|_{C_{\tau}^{2, \alpha}}\left\|\nabla^{g_{b}} h\right\|_{L^{2}}\left\|\rho_{g_{b}}^{-1} h\right\|_{L^{2}} \\
\lesssim & \|h\|_{C_{\tau}^{2, \alpha}}\left\|\nabla^{g_{b}} h\right\|_{L^{2}}^{2} .
\end{aligned}$$
Here, we have made constant use of (6.10). In particular, we have used the fact that $\nabla^{g_{b}} f_{g_{t}}$ and $\nabla^{g_{b}} \delta_{g_{t}} f(h)$ decay at least linearly together with Cauchy-Schwarz inequality in the second line and Hardy's inequality (Theorem 1.7) in the third line. The integral involving the Hessian of $\operatorname{tr}_{g_{b}} h$ can be handled similarly.

We are left with estimating integrals involving (the $t$-derivatives of) $\nabla^{g_{t},{ }^{2}} f_{g_{t}}$. Let us notice first that any term which contains a $t$-derivative that falls either on the scalar product on symmetric 2-tensors induced by $g_{t}$ or on the volume element $d \mu_{g_{t}}$ can be estimated as previously by using Hardy's inequality (Theorem 1.7) in a quite straightforward way. Consequently, only the integrals that contain $t$-derivatives of $\nabla^{g_{t}, 2} f_{g_{t}}$ and $e^{-f_{g_{t}}}$ will be estimated.

We start with terms involving derivatives of $e^{-f_{g_{t}}}$ only. By integration by parts,
$$\begin{aligned}
\mid \int_{N}\left\langle\nabla^{g_{t}, 2} f_{g_{t}}, h\right\rangle_{g_{t}} \delta_{g_{t}}^{2} f(h, h) & e^{-f_{g_{t}}} d \mu_{g_{t}} \mid \\
\lesssim & \int_{N}\left(|h|_{g_{t}}\left|\nabla^{g_{t}} f_{g_{t}}\right|_{g_{t}}^{2}+\left|\operatorname{div}_{g_{t}} h\right|_{g_{t}}\left|\nabla^{g_{t}} f_{g_{t}}\right| g_{t}\right)\left|\delta_{g_{t}}^{2} f(h, h)\right| d \mu_{g_{t}} \\
& +\int_{N}|h|_{g_{t}}\left|\nabla^{g_{t}} f_{g_{t}}\right| g_{t}\left|\nabla^{g_{t}} \delta_{g_{t}}^{2} f(h, h)\right|_{g_{t}} d \mu_{g_{t}} \\
\lesssim & \|h\|_{C_{\tau}^{2, \alpha}}^{2}\left(\left\|\rho_{g_{b}}^{-1} h\right\|_{L^{2}}\left\|\nabla^{g_{t}} f_{g_{t}}\right\|_{L^{2}}+\left\|\nabla^{g_{t}} h\right\|_{L^{2}}\left\|\nabla^{g_{t}} f_{g_{t}}\right\|_{L^{2}}\right) \\
\lesssim & \|h\|_{C_{\tau}^{2, \alpha}}\left\|\nabla^{g_{t}} h\right\|_{L^{2}}\left\|\nabla^{g_{t}} f_{g_{t}}\right\|_{L^{2}},
\end{aligned}$$
where we have used the linear decay of $\nabla^{g_{t}} f_{g_{t}}$ together with the fact that $\|h\|_{C_{\tau}^{2, \alpha}} \lesssim 1$. Now, from [(4.1), Proposition 4.1],
$$\left|\int_{N}\left\langle\nabla^{g_{t}, 2} f_{g_{t}}, h\right\rangle_{g_{t}} \delta_{g_{t}}^{2} f(h, h) e^{-f_{g_{t}}} d \mu_{g_{t}}\right| \lesssim\|h\|_{C_{\tau}^{2, \alpha}}\left\|\nabla^{g_{t}} h\right\|_{L^{2}}^{2},$$
as desired. With the help of (C.8) from Lemma C.3, we proceed to estimate terms involving $t$-derivatives of $\nabla^{g_{t}} f_{g_{t}}$ : by integrating by parts,
$$\begin{aligned}
\left|\int_{N}\left\langle\frac{\partial}{\partial t} \nabla^{g_{t}, 2} f_{t}, h\right\rangle_{g_{t}} \delta_{g_{t}} f(h) e^{-f_{g_{t}}} d \mu_{g_{t}}\right| \lesssim & \left|\int_{N}\left\langle\nabla^{g_{t}, 2} \delta_{g_{t}} f(h), h\right\rangle_{g_{t}} \delta_{g_{t}} f(h) e^{-f_{g_{t}}} d \mu_{g_{t}}\right| \\
& +\left|\int_{N}\left\langle\mathcal{L}_{\nabla^{g_{t}} f_{g_{t}}}(h), h\right\rangle_{g_{t}} \delta_{g_{t}} f(h) e^{-f_{g_{t}}} d \mu_{g_{t}}\right| \\
& +\left|\int_{N}\left\langle\mathcal{L}_{h\left(\nabla^{g_{t}} f_{g_{t}}\right)}\left(g_{t}\right), h\right\rangle_{g_{t}} \delta_{g_{t}} f(h) e^{-f_{g_{t}}} d \mu_{g_{t}}\right| .
\end{aligned}$$

Let us estimate the first integral on the righthand side of the previous inequalities (6.11):
$$\begin{aligned}
\mid \int_{N}\left\langle\nabla^{g_{t}, 2} \delta_{g_{t}} f(h), h\right\rangle_{g_{t}} \delta_{g_{t}} f(h) & e^{-f_{g_{t}}} d \mu_{g_{t}} \mid \\
\lesssim & \int_{N}\left|\nabla^{g_{t}} \delta_{g_{t}} f(h)\right|_{g_{t}}\left|\operatorname{div}_{g_{t}} h\right|_{g_{t}}\left|\delta_{g_{t}} f(h)\right| d \mu_{g_{t}} \\
& +\int_{N}\left|\nabla^{g_{t}} \delta_{g_{t}} f(h)\right|_{g_{t}}|h|_{g_{t}}\left(\left|\nabla^{g_{t}} f_{g_{t}}\right|_{g_{t}}+\left|\nabla^{g_{t}} \delta_{g_{t}} f(h)\right|_{g_{t}}\right) d \mu_{g_{t}} .
\end{aligned}$$
Now, since $\operatorname{div}_{g_{b}} h=0$, one has $\left|\operatorname{div}_{g_{t}} h\right|_{g_{t}} \lesssim|h|_{g_{b}}\left|\nabla^{g_{b}} h\right|_{g_{b}}$. Using that $\left|\nabla^{g_{t}} \delta_{g_{t}} f(h)\right|_{g_{t}}$ decays at least linearly together with (6.10) applied to $k=1$,
$$\begin{aligned}
\int_{N}\left|\nabla^{g_{t}} \delta_{g_{t}} f(h)\right|_{g_{t}}\left|\operatorname{div}_{g_{t}} h\right|_{g_{t}}\left|\delta_{g_{t}} f(h)\right| d \mu_{g_{t}} & \lesssim\|h\|_{C_{\tau}^{2, \alpha}}\left\|\nabla^{g_{b}} h\right\|_{L^{2}}^{2}+\left\|\rho_{g_{b}}^{-1} h\right\|_{L^{2}}\left\|\nabla^{g_{b}} h\right\|_{L^{2}} \\
& \lesssim\|h\|_{C_{\tau}^{2, \alpha}}\left\|\nabla^{g_{b}} h\right\|_{L^{2}}^{2}
\end{aligned}$$
by Young's inequality and Hardy's inequality (Theorem 1.7). Thanks to [(4.2), Proposition 4.1,
$$\int_{N}\left|\nabla^{g_{t}} \delta_{g_{t}} f(h)\right|_{g_{t}}^{2}|h|_{g_{t}} d \mu_{g_{t}} \lesssim\|h\|_{C^{0}}\left\|\nabla^{g_{t}} \delta_{g_{t}} f(h)\right\|_{L^{2}}^{2} \lesssim\|h\|_{C^{0}}\left\|\nabla^{g_{b}} h\right\|_{L^{2}}^{2} .$$
The other integrals involved on the righthand sides of (6.12) and (6.11) can be treated in a similar way. The same is true for terms involving the second $t$-derivatives of $\nabla^{g_{t}, 2} f_{g_{t}}$ by using (C.9) from Lemma C.3. \(\square\)

This concludes the proof of Proposition 6.6. \(\square\)

\subsection*{6.2. A first way to prove a Łojasiewicz inequality.}

In order to prove a Lojasiewicz inequality in the stable integrable case, a natural strategy consists in proving it at an infinitesimal level and then it is sufficient to control the nonlinear terms, see [Has12] for example in the case of a closed manifold. Here, we succintly mention how one can implement this strategy in a non-compact situation. This will be proven in general in the next section.

We start by proving an infinitesimal version of Łojasiewicz inequality.
Proposition 6.7. Let $\left(N^{n}, g_{b}\right), n \geq 4$, be a linearly stable ALE Ricci-flat metric asymptotic to $\mathbb{R}^{n} / \Gamma$, for some finite subgroup $\Gamma$ of $S O(n)$ acting freely on $\mathbb{S}^{n-1}$. Let $\tau \in\left(\frac{n-2}{2}, n-2\right)$. Then the following Łojasiewicz inequality holds true for any sufficiently small symmetric 2-tensor $h \in C_{\tau}^{2}\left(S^{2} T^{*} N\right)$ :
$$\left\langle-L_{g_{b}} h, h\right\rangle_{L^{2}} \leq C\left\|L_{g_{b}} h\right\|_{L_{\frac{n}{2}+1}^{2}}^{2},$$
for some positive constant $C=C\left(n, \tau, g_{b}\right)$.