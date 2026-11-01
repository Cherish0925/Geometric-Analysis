---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: On asymptotic behavior of the second Chern forms on degenerating Kähler-Einstein surfaces]

Lemma 9. $\left|\sigma_{t}\right|_{h_{t}}<C$ for some constant $C$ independent of $t$.
Proof. It is sufficient to estimate $\left|\sigma_{t}\right|_{h_{t}}$ around the singularity. Recall that $\sigma$ is smooth form on $\mathcal{X}$. Hence, by definition of a smooth form on (possibly) singular analytic space, we have an embedding $i: V \hookrightarrow \mathbb{C}^{m}$ of an open neighbourhood $V \subset \mathcal{X}$ of $x_{0}$ such that $\sigma$ extends to a smooth form on $\mathbb{C}^{m}$. Furthermore, the embedding $i: V \hookrightarrow \mathbb{C}^{m}$ factors through the embedding $\iota_{\zeta}: \mathcal{Y}_{\zeta} \rightarrow \mathbb{C}^{3} \times \Delta_{d}$ i.e. there exists a regular map $\phi: V^{\prime} \rightarrow \mathbb{C}^{m}$ defined on a neighbourhood $V^{\prime}:=\iota_{\zeta}(V) \subset \mathbb{C}^{3} \times \Delta$ of the origin such that $i=\phi \circ \iota_{\zeta}$. Therefore, by considering the pullback of $\sigma$ by $\phi$, we may assume $\sigma$ is defined on $\mathbb{C}^{3} \times \Delta_{d}$. Hence we consider an embedding $Y_{\zeta(t)} \hookrightarrow \mathbb{C}^{3}$ and a smooth form $\sigma_{t}$ on $\mathbb{C}^{3}$ (parameterized by $t$ smoothly). For a point $y \in Y_{\zeta(t), r<1}$, take a $g_{\zeta(t)}$-normal coordinate $\left(V_{y},\left(y_{1}, y_{2}\right)\right)$ centered at $y$ i.e. $y=(0,0)$ and $g_{\zeta(t)}=\left(\delta_{i \bar{j}}+O\left(|y|^{2}\right)\right) d y_{i} d \bar{y}_{j}$ under this coordinate. Let
$$F=\left(f_{1}, f_{2}, f_{3}\right): V_{y} \rightarrow \mathbb{C}^{3}$$
be the restriction of $\iota_{\zeta(t)}$ on $V_{y}$. Then, for a two form $\sigma=\sigma_{i \bar{j}} d z_{i} \wedge d \bar{z}_{j}$ on $\mathbb{C}^{3}$, its norm $|\sigma|_{g_{\zeta(t)}}$ at $y$ is equal to
$$\begin{aligned}
|\sigma|_{g_{\zeta(t)}} & =\left|F^{*} \sigma\right|_{g_{\zeta(t)}} \\
& =\sum_{i, j, k, l} \sigma_{i \bar{j}} \frac{\partial f_{i}}{\partial y_{k}} \frac{\partial f_{j}}{\partial y_{l}} .
\end{aligned}$$
Therefore, as $\sigma_{i \bar{j}}$ are smooth functions on $\mathbb{C}^{3}$, it is sufficient to estimate the quantity
$$\left|\frac{\partial f_{i}}{\partial y_{k}}\right| .$$

Recall that $F=\left(f_{1}, f_{2}, f_{3}\right)$ is the restriction of $\iota$, hence we have
$$\begin{aligned}
F_{*} \frac{\partial}{\partial y_{i}} & =\sum_{k} \frac{\partial f_{k}}{\partial y_{i}} \frac{\partial}{\partial z_{k}}, \\
\sum_{k}\left|\frac{\partial f_{k}}{\partial y_{i}}\right|^{2} & =\left|\left(\iota_{\zeta(t)}\right)_{*} \frac{\partial}{\partial y_{i}}\right|_{g_{\mathbb{C}} 3}^{2} \\
& =\left|\frac{\partial}{\partial y_{i}}\right|_{\iota_{\zeta(t)}^{*} g_{\mathbb{C}^{3}}} .
\end{aligned}$$
Let $y^{\prime} \in Y_{\zeta(t) / \varepsilon^{2}}$ be the image of $y$ by the dilation $H_{(1 / \varepsilon, \zeta(t))}: Y_{\zeta(t)} \rightarrow Y_{\zeta(t) / \varepsilon^{2}}$ i.e. $y^{\prime}=H_{(1 / \varepsilon, \zeta(t))}(y)$. Then, as $H_{\left(\varepsilon, \zeta(t) / \varepsilon^{2}\right)}^{*} g_{\zeta(t)}=\varepsilon^{2} g_{\zeta(t) / \varepsilon^{2}}$, we see that
$$\begin{aligned}
\left|\left(H_{\left(\varepsilon, \zeta(t) / \varepsilon^{2}\right)}\right)_{*}(v)\right|_{g_{\zeta(t)}} & =|v|_{H_{\left(\varepsilon, \zeta(t) / \varepsilon^{2}\right)}^{*}} g_{\zeta(t)} \\
& =|v|_{\varepsilon^{2} g_{\zeta(t) / \varepsilon^{2}}}=\varepsilon,
\end{aligned}$$
for any unit vector $v \in T_{y^{\prime}} Y_{\zeta(t) / \varepsilon^{2}}$. In particular, for any unit vector $u \in T_{y} Y_{\zeta(t)}$, there exits a unit vector $v \in T_{y^{\prime}} Y_{\zeta(t) / \varepsilon^{2}}$ such that $\left(H_{\left(\varepsilon, \zeta(t) / \varepsilon^{2}\right)}\right) *(v / \varepsilon)=u$. Then, for a unit vector $v \in T_{y^{\prime}} Y_{\zeta(t) / \varepsilon^{2}}$ such that $\left(H_{(\varepsilon, \zeta(t))}\right)_{*}(v / \varepsilon)=\frac{\partial}{\partial y_{i}}$, we obtain
$$\left|\frac{\partial}{\partial y_{i}}\right|_{\iota_{\zeta(t)}^{*} g_{\mathbb{C}^{3}}}=\frac{1}{\varepsilon}|v|_{H_{\left(\varepsilon, \zeta(t) / \varepsilon^{2}\right)}^{*} \iota_{\zeta(t)}^{*} g_{\mathbb{C}^{3}}} .$$
Recall that the embedding $\iota_{\zeta}: Y_{\zeta} \rightarrow \mathbb{C}^{3}$ is equivariant i.e. $\varepsilon \cdot \circ \iota_{\zeta / \varepsilon^{2}}=\iota_{\zeta} \circ H_{\left(\varepsilon, \zeta / \varepsilon^{2}\right)}$, where $\varepsilon \cdot$ is the weighted $\mathbb{C}^{*}$-action on $\mathbb{C}^{3}$ (see proof of lemma (3)). Then,
$$\begin{aligned}
H_{\left(\varepsilon, \zeta(t) / \varepsilon^{2}\right)}^{*} \iota_{\zeta(t)}^{*} g_{\mathbb{C}^{3}} & =\iota_{\zeta(t) / \varepsilon^{2}}^{*}(\varepsilon \cdot)^{*} g_{\mathbb{C}^{3}} \\
& =\left.\left(\sum \varepsilon^{2 k_{i}} d z_{i} d \bar{z}_{i}\right)\right|_{Y_{\zeta(t) / \varepsilon^{2}}} .
\end{aligned}$$
Therefore, if we put $\left(\iota_{\zeta(t) / \varepsilon^{2}}\right)_{*}(v)=\sum v_{i} \frac{\partial}{\partial z_{i}}$, it is sufficient to show that $\sum \varepsilon^{2 k_{i}-2}\left|v_{i}\right|^{2}$ is uniformly bounded. By the equivariance of $\iota_{\zeta}$ again, if we put $\left(\iota_{\zeta}\right)_{*} \frac{\partial}{\partial y_{i}}=$ $\sum_{j}\left(y_{i}\right)_{j} \frac{\partial}{\partial z_{j}}$, the following holds:
$$\begin{aligned}
\sum_{j}\left(y_{i}\right)_{j} \frac{\partial}{\partial z_{j}} & =\frac{1}{\varepsilon}(\varepsilon \cdot)_{*}\left(\sum v_{j} \frac{\partial}{\partial z_{j}}\right) \\
& =\sum_{j} \varepsilon^{k_{j}-1} v_{j} \frac{\partial}{\partial z_{j}} .
\end{aligned}$$
Now, consider the equality
$$\sum \varepsilon^{2 k_{j}-2}\left|v_{j}\right|^{2}=\sum\left|\left(y_{i}\right)_{j}\right|^{2} .$$
The right hand side of (92) is uniformly bounded as $y$ runs $Y_{\zeta(t), r<1}$ for each (fixed) $t$. On the other hand, since $g_{\zeta(t) / \varepsilon^{2}} \rightarrow g_{\dot{\zeta}}$, there exists a constant $C>0$ independent of $t$ (possibly depends on $r=r\left(y^{\prime}\right)$ ) such that
$$C^{-1}<|v|_{g_{\dot{\zeta}}}<C$$
for any unit vector $v \in T_{y^{\prime}} Y_{\zeta(t) / \varepsilon^{2}}$ with respect to $g_{\zeta(t) / \varepsilon^{2}}$ for any sufficiently small $t$. Then,
$$\left\{v | v \in T _ { y ^ { \prime } } Y _ { \zeta ( t ) / \varepsilon ^ { 2 } } , | v | _ { g _ { \zeta ( t ) / \varepsilon ^ { 2 } } } = 1 , r ( y ^ { \prime } ) = r \} \subset \left\{v\left|v \in T_{y^{\prime}} Y_{\zeta(t) / \varepsilon^{2}}, C^{-1}<|v|_{g_{\dot{\zeta}}}<C, r\left(y^{\prime}\right)=r\right\}\right.\right.$$
for any $t$. In particular,
$$\bigcup_{t \ll 1}\left\{\left(\iota_{\zeta(t) / \varepsilon^{2}}\right)_{*}(v)\left|v \in T_{y^{\prime}} Y_{\zeta(t) / \varepsilon^{2}},|v|_{g_{\zeta(t) / \varepsilon^{2}}}=1, r\left(y^{\prime}\right)=r\right\}\right.$$
is contained in a relatively compact subset
$$\left\{\left(\iota_{\left.\zeta(t) / \varepsilon^{2}\right)_{*}(v)\left|v \in T_{y^{\prime}} Y_{\zeta(t) / \varepsilon^{2}}, C^{-1}<|v|_{g_{\dot{\zeta}}}<C, r\left(y^{\prime}\right)=r\right\}}\right.\right.$$
of $\mathbb{C}^{3}$ for each $r$ (note that $\iota_{\zeta(t) / \varepsilon^{2}}$ defines a smooth family of embedding $\left\{\iota_{\dot{\zeta}+O(\varepsilon)}\right.$ : $\left.Y_{\dot{\zeta}+O(\varepsilon)} \mathbb{C}^{3}\right\}_{0 \leq t \leq 1}$, hence an image of a relatively compact subset is a relatively compact). Then the left hand side of (92) is bounded from above uniformly with respect to $t$ (recall that $k_{i} \geq 2$ ). Then in particular, $\left|\frac{\partial f_{i}}{\partial y_{k}}\right|$ is uniformly bounded. Therefore, $\left|\sigma_{t}\right|$ is uniformly bounded as desired. \(\square\)

Lemma 10. $\int_{X_{t}} \sigma_{t} \wedge \tau=O\left(\varepsilon^{2-\beta(\delta+2)}\right)$.
Proof. By lemma 9, it is sufficient to estimate $\int_{X_{t}}|\tau|_{h_{t}} \operatorname{Vol}_{h_{t}}$. By Biquard-Rollin's a priori estimate, we have
$$\sup \left|\rho^{j-\delta} \nabla^{j}\left(g_{t}-h_{t}\right)\right|_{h_{t}}=O\left(\varepsilon^{2-\beta(\delta+2)}\right)$$
for $j=0,1,2$. More explicitly,
$$\left|\nabla^{j}\left(g_{t}-h_{t}\right)\right|_{h_{t}}=\left\{\begin{array}{cc}
O\left(\varepsilon^{2-\beta(\delta+2)}\right) & 1 \leq r \\
r^{\delta-j} O\left(\varepsilon^{2-\beta(\delta+2)}\right) & \varepsilon \leq r \leq 1 \\
O\left(\varepsilon^{(1-\beta)(2+\delta)-j}\right) & r \leq \varepsilon
\end{array} .\right.$$
Therefore, we have
$$\begin{gathered}
\left|\dot{k}_{t}\right|_{h_{t}}=\left|\left(h_{t}-g_{t}\right)\right|_{h_{t}}=\left\{\begin{array}{cc}
O\left(\varepsilon^{2-\beta(\delta+2)}\right) & 1 \leq r \\
r^{\delta} O\left(\varepsilon^{2-\beta(\delta+2)}\right) & \varepsilon \leq r \leq 1 \\
O\left(\varepsilon^{(1-\beta)(2+\delta)}\right) & r \leq \varepsilon
\end{array},\right. \\
\left|k_{t}^{-1}-h_{t}^{-1}\right|_{h_{t}}=\left\{\begin{array}{cc}
O\left(\varepsilon^{2-\beta(\delta+2)}\right) & 1 \leq r \\
r^{\delta} O\left(\varepsilon^{2-\beta(\delta+2)}\right) & \varepsilon \leq r \leq 1 \\
O\left(\varepsilon^{(1-\beta)(2+\delta)}\right) & r \leq \varepsilon
\end{array} .\right.
\end{gathered}$$
Hence we obtain the following estimate:
$$\left|N_{s}\right|_{h_{t}}=\left\{\begin{array}{cc}
O\left(\varepsilon^{2-\beta(\delta+2)}\right) & 1 \leq r \\
r^{\delta} O\left(\varepsilon^{2-\beta(\delta+2)}\right) & \varepsilon \leq r \leq 1 \\
O\left(\varepsilon^{(1-\beta)(2+\delta)}\right) & r \leq \varepsilon
\end{array} .\right.$$
For the curvature $R_{s}$, as we have
$$\left|\nabla^{j}\left(k_{s}\right)-\nabla^{j}\left(h_{t}\right)\right|_{h_{t}}=\left\{\begin{array}{cc}
O\left(\varepsilon^{2-\beta(\delta+2)}\right) & 1 \leq r \\
r^{\delta-j} O\left(\varepsilon^{2-\beta(\delta+2)}\right) & \varepsilon \leq r \leq 1 \\
O\left(\varepsilon^{(1-\beta)(2+\delta)-j}\right) & r \leq \varepsilon
\end{array},\right.$$
we have the following:
$$\left|\left(R_{s}\right)-R\left(h_{t}\right)\right|_{h_{t}}=\left\{\begin{array}{cc}
O\left(\varepsilon^{2-\beta(\delta+2)}\right) & 1 \leq r \\
r^{\delta-2} O\left(\varepsilon^{2-\beta(\delta+2)}\right) & \varepsilon \leq r \leq 1 \\
O\left(\varepsilon^{\delta-\beta(\delta+2)}\right) & r \leq \varepsilon
\end{array} .\right.$$
By lemma 2, (64), and (73), we have the following:
$$\left|R\left(h_{t}\right)-R\left(g_{0}\right)\right|_{h_{t}}=\left\{\begin{array}{cc}
O\left(t^{d}\right) & 1 \leq r \\
O\left(\varepsilon^{4} r^{-6}\right) & 4 b \leq r \leq 1 \\
O\left(r^{0}\right) & b \leq r \leq 4 b
\end{array} .\right.$$
Note that there exists a constant $C>0$ independent of $t$ such that $C h_{t} \leq g_{0} \leq$ $C^{-1} h_{t}$ (see (68) and corresponding estimates in the above lemmas) on $b \leq r$. Then, estimates with respect to $|\cdot|_{h_{t}}$ are equivalent to those with respect to $|\cdot|_{g_{0}}$. Therefore,
$$|\tau|_{h_{t}}=\left\{\begin{array}{cc}
O\left(\varepsilon^{2-\beta(\delta+2)}\right) & 1 \leq r \\
r^{2 \delta-2} O\left(\varepsilon^{4-2 \beta(\delta+2)}\right) & b \leq r \leq 1 \\
r^{\delta}\left|R\left(g_{\zeta(t)}\right)\right|_{g_{\zeta(t)}} O\left(\varepsilon^{2-\beta(\delta+2)}\right) & \varepsilon \leq r \leq b \\
\left|R\left(g_{\zeta(t)}\right)\right|_{g_{\zeta(t)}} O\left(\varepsilon^{(1-\beta)(\delta+2)}\right) & r \leq \varepsilon
\end{array} .\right.$$
As $\left|R\left(g_{\zeta / \varepsilon^{2}}\right)\right|_{g_{\zeta(t) / \varepsilon^{2}}}$ is bounded on $r \leq 1$ and has asymptotic $O\left(r^{-6}\right)$ as $r \rightarrow \infty$, $\left|R\left(g_{\zeta(t)}\right)\right|_{g_{\zeta(t)}}$ can be estimated as follows:
$$\left|R\left(g_{\zeta(t)}\right)\right|_{g_{\zeta(t)}}=\left\{\begin{array}{cc}
O\left(\varepsilon^{4} r^{-6}\right) & \varepsilon \leq r \\
O\left(\varepsilon^{-2}\right) & r \leq \varepsilon
\end{array} .\right.$$
Therefore, we have
$$|\tau|_{h_{t}}=\left\{\begin{array}{cc}
O\left(\varepsilon^{2-\beta(\delta+2)}\right) & 1 \leq r \\
r^{2 \delta-2} O\left(\varepsilon^{4-2 \beta(\delta+2)}\right) & b \leq r \leq 1 \\
r^{\delta-6} O\left(\varepsilon^{6-\beta(\delta+2)}\right) & \varepsilon \leq r \leq b \\
O\left(\varepsilon^{(1-\beta)(\delta+2)-2}\right) & r \leq \varepsilon
\end{array} .\right.$$
Finally, by integrating them, we obtain
$$\int_{X_{t}} \omega \wedge \tau=O\left(\varepsilon^{2-\beta(\delta+2)}\right),$$
which is what we needed. \(\square\)
proof of the Theorem 7 . By summing up above lemmas, we see
$$F(t)=\int_{X_{0}} f_{0} c_{2}\left(g_{0}\right)+f(0) e_{\text {orb }}\left(X_{\dot{\zeta}}\right)+O(t) .$$
In particular, $F(0)=\int_{X_{0}} f_{0} c_{2}\left(g_{0}\right)+f(0) e_{\text {orb }}\left(X_{\dot{\zeta}}\right)$. Then, it follows that $F(t)-$ $F(0)=O(t)$ from the above estimate. Then, $F$ is Hölder continuous with exponent 1 on $\Delta_{d} \cap[0,1)$, therefore, Hölder continuous with exponent at least $\frac{1}{d}$ on $\Delta \cap$ [0, 1). \(\square\)

\section*{4. Polarized K3 surface case}

In this section, we discuss a degeneration of Kähler-Einstein metrics on a non-degenerate family of polarized K3 surfaces. In particular, we extend the main theorem to a function defined on the whole disc.

For a polarized family of Calabi-Yau manifolds (note that K3 surface is the two dimensional Calabi-Yau manifold), the following convergence theorem is known [21] (see also [22]).

Theorem 8 (Theorem 1.4. [21] and its proof). Let $X_{0}$ be an $n$ dimensional Calabi-Yau variety. Assume that $X_{0}$ admits a smoothing $\mathcal{X} \rightarrow \Delta$ such that $\mathcal{X}$ admits an ample line bundle $\mathcal{L}$ and the relative canonical bundle is trivial, i.e., $K_{\mathcal{X} / \Delta} \cong \mathcal{O}_{\mathcal{X}}$. Let $\hat{g}_{t}$ denote the unique Ricci-flat Kähler metric with Kähler form $\left.\hat{\omega}_{t} \in c_{1}(\mathcal{L})\right|_{X_{t}}$ and let $\left\{\phi_{t}\right\}$ be the solution of the equation of Calabi-Yau metric
$$\left\{\begin{array}{c}
\left(\omega_{t}+d d^{c} \phi_{t}\right)^{n}=(-1)^{\frac{n^{2}}{2}} S_{t} \Omega_{t} \wedge \bar{\Omega}_{t} \\
\sup _{X_{t}} \phi_{t}=0,
\end{array}\right.$$
where $\Omega_{t}$ is a holomorphic $n$-form on $X_{t}, S_{t}$ is a constant depending only on $t$ and $\omega_{t}=\left.\frac{1}{m} \omega_{\mathrm{FS}}\right|_{X_{t}}$ is the restriction of the Fubini-Study metric under an embedding $\mathcal{L}^{m}: \mathcal{X} \rightarrow \mathbb{P}^{N} \times \Delta$. Then, $\phi_{t} \rightarrow \phi_{0}$ on any compact subset $K \subset X_{0}^{\text {reg }}$ in the $C^{\infty}$ sense.

Let $\mathcal{X} \rightarrow \Delta$ be a flat family of K3 surfaces. Assume that the fibre $X_{t}$ on $t \in \Delta$ is smooth for $t \neq 0$ and $X_{0}$ has ADE singularities. Additionally, we assume that the central fibre $X_{0}$ has exactly one singularity $x_{0}$ and the family admits the simultaneous minimal resolution $\tilde{\mathcal{X}} \rightarrow \Delta$ for simplicity. Take an ample line bundle $\mathcal{L}$ on $\mathcal{X}$ and let $\hat{g}_{t}$ be the Ricci-flat Kähler metric with Kähler form $\left.\hat{\omega}_{t} \in c_{1}(\mathcal{L})\right|_{X_{t}}$. Fix nowhere vanishing holomorphic 2-forms $\Omega_{t}$ on $X_{t}$ so that $\hat{\omega}_{t}^{2}=\Omega_{t} \wedge \bar{\Omega}_{t}$. We may take an open neighbourhood $\mathcal{U}$ of $x_{0} \in \mathcal{X}$ as in section 2.3. However, we may take $\mathcal{U}$ (sufficiently small, if necessary) with better properties.

Lemma 11. Let $(\mathcal{X}, \mathcal{L}) \rightarrow \Delta, x_{0} \in X_{0}$ and $\hat{g}_{t}$ be as above. Then there exists an open neighbourhood $\mathcal{U} \subset \mathcal{X}$ of $x_{0}$ such that
\begin{itemize}
\item[-] $\mathcal{U} \rightarrow \Delta$ is a flat deformation of the singularity $x_{0} \in X_{0}$ described by $\zeta(t)=$ $\left(0, \sqrt{2}\left[\Omega_{t}\right]\right): \Delta \rightarrow \mathfrak{h}_{\mathbb{R}} \oplus \mathfrak{h}_{\mathbb{C}}$,
\item[-] $U_{0} \subset X_{0}$ admits a $\hat{g}_{0}$-adopted uniformization $\mathbb{C}^{2} \supset B(0 ; 1) \rightarrow U_{0}$,
\item[-] the simultaneous resolution $\tilde{\mathcal{U}} \rightarrow \Delta$ induced by $\tilde{\mathcal{X}} \rightarrow \mathcal{X}$ is diffeomorphic to $U \times \Delta$ for $U=\{r<1\} \subset X$,
\item[-] $\hat{g}_{t}$ has a potential $r^{2}+\hat{\phi}_{t}$ on $U_{t} \subset X_{t}$ and $\left\{\hat{\phi}_{t}\right\}$ converges smoothly to $\hat{\phi}_{0}$ on any compact subset of $\frac{1}{2}<r<1$.
\end{itemize}
Proof. We show the fourth condition is possible, and then, take its intersection with an open neighbourhood satisfying the first three conditions. Consider an embedding
$$\mathcal{L}^{m}: \mathcal{X} \rightarrow \mathbb{P}^{N} \times \Delta$$
with suitable $m$ and $N$. Take an affine open subset
$$\mathbb{C}^{N} \times \Delta \subset \mathbb{P}^{N} \times \Delta$$
such that $x_{0} \in \mathcal{X} \cap\left(\mathbb{C}^{N} \times \Delta\right)$. Let $\mathcal{X}^{o} \subset \mathcal{X}$ be the intersection $\mathcal{X} \cap\left(\mathbb{C}^{N} \times \Delta\right)$. Then, $\mathcal{X}^{O}$ is a family of affine varieties with central fiber having a rational double point $x_{0}$ and $\mathcal{L}^{m}$ is trivial on $\mathcal{X}^{o}$. Then, by theorem 8, we may take a function $\phi_{t}$ on $X_{t}$ such that $\phi_{t} \rightarrow \phi_{0}$ smoothly on $X_{t} \cap\left\{\frac{1}{2} \leq r \leq 1\right\}$ and $\hat{\omega}_{t}=\left.\frac{1}{m} \omega_{\mathrm{FS}}\right|_{X_{t}}+d d^{c} \phi_{t}$. Therefore, we have $\hat{\omega}_{t}=d d^{c}\left(\left.\frac{1}{m} \log \left(1+\sum\left|z_{i}\right|^{2}\right)\right|_{X_{t}^{o}}+\phi_{t}\right)$ on $X_{t}^{o}:=X_{t} \cap \mathcal{X}^{o} \subset \mathbb{C}^{N}$. Then we can attain the fourth condition by taking $\hat{\phi}_{t}=\left.\frac{1}{m} \log \left(1+\sum\left|z_{i}\right|^{2}\right)\right|_{X_{t}^{o}}+\phi_{t}-r^{2} . \quad \square$

We construct an almost Ricci-flat Kähler metric on $X_{t}$ by gluing $\hat{g}_{t}$ and $g_{\zeta(t)}$. As in section 2.3 and section 3, we assume that the family is non-degenerate in the sense of Biquard-Rollin [7] in the following extended sense:

Definition 5. Let $(\mathcal{X}, \mathcal{L}) \rightarrow \Delta$ be a polarized flat family of K3 surfaces with the central fiber with an ADE singularity $x_{0} \in X_{0} \cong 0 \in \mathbb{C}^{2} / \Gamma$. Take a suitable open neighborhood $x_{0} \in \mathcal{U} \subset \mathcal{X}$ of $x_{0}$ which is isomorphic to an open subset of the family $\mathcal{Y}_{\zeta(t)}$ of Kronheimer's ALE gravitational instantons defined by a holomorphic function $\zeta: \Delta \rightarrow \mathfrak{h}_{\mathbb{C}}$. Then the family is non-degenerate at $x_{0}$ if $\zeta(t)$ satisfies the following condition:
Let $\zeta(t)=\dot{\zeta} t^{p}+O\left(t^{p+1}\right)$ be the expansion of $\zeta(t)$ at the origin so that $\dot{\zeta} \neq 0$. Then $\dot{\zeta}$ is not in the discriminant locus, i.e., $\dot{\zeta} \notin \theta^{\perp}=\left\{v \in \mathfrak{h}_{\mathbb{C}} \mid\langle v, s\rangle=0\right.$ for any $\left.s \in \theta\right\}$ for any root $\theta$.

We also need the next lemma.

Lemma 12 (Theorem 8.4.4. [14]). Let $Y$ be an ALE gravitational instanton and $\tau$ be a $d$-exact real $(1,1)$ form on $Y$ with asymptotic $\left\|\nabla^{k} \tau\right\|=O\left(r^{-4-k}\right)$. Then $\tau$ is $d d^{c}$-exact and a potential $\phi$ can be chosen with asymptotic $\left\|\nabla^{k} \phi\right\|=O\left(r^{-2-k}\right)$.

By applying the above lemma to $\tau=d d_{t}^{c}\left(r^{2}\right)-\omega_{\zeta(t)}$, we can take a potential $r^{2}+\phi_{\zeta(t)}$ of $\omega_{\zeta(t)}$ on $Y$ such that $\phi_{\zeta(t)}=O\left(r^{-2}\right)$. We define a Kähler metric $\tilde{g}_{t}$ on $X_{t}$ by
$$\tilde{g}_{t}=\left\{\begin{array}{cc}
\hat{g}_{t} & \text { on } X_{t} \backslash U \\
d d_{t}^{c}\left(r^{2}+\tilde{\phi}_{t}\right) & \text { on } U
\end{array},\right.$$
where $\tilde{\phi}_{t}$ is a function on $U$ defined by
$$\tilde{\phi}_{t}=\left(1-\chi_{\left(\varepsilon^{1 / 2}, 2 \varepsilon^{1 / 2}\right)}(r)\right) \phi_{\zeta(t)}+\chi_{\left(\varepsilon^{1 / 2}, 2 \varepsilon^{1 / 2}\right)}(r)\left(1-\chi_{(1 / 2,3 / 4)}(r)\right) \hat{\phi}_{0}+\chi_{(1 / 2,3 / 4)}(r) \hat{\phi}_{t},$$
where $\varepsilon=|t|^{p / 2}$ and $\chi$ is the bump function defined in section 2.3, see (39).
![](https://cdn.mathpix.com/cropped/5560a88a-8112-4d9d-a6b3-3db74de545fb-26.jpg?height=798&width=1212&top_left_y=427&top_left_x=461)

Gluing of metrics.
The tensor $\tilde{g}_{t}$ satisfies the following estimates (in particular, $\tilde{g}_{t}$ is actually a metric).

Lemma 13. On the domain $X_{t} \backslash U_{r \leq \frac{3}{4}}$, $\tilde{g}_{t}$ satisfies the following estimates:
$$\begin{aligned}
\tilde{\omega}_{t}^{2} & =\Omega_{t} \wedge \bar{\Omega}_{t}, \\
\left\|\operatorname{Ric}\left(\tilde{g}_{t}\right)-\operatorname{Ric}\left(\hat{g}_{0}\right)\right\|_{\hat{g}_{0}} & =O(|t|), \\
\left\|c_{2}\left(\tilde{g}_{t}\right)-c_{2}\left(\hat{g}_{0}\right)\right\|_{\hat{g}_{0}} & =O(|t|) .
\end{aligned}$$

Proof. Recall that $\tilde{g}_{t}=\hat{g}_{t}$ and $\hat{g}_{t} \rightarrow \hat{g}_{0}$ smoothly on this domain and that $\hat{g}_{0}$ is a Ricci flat metric. The assertion follows from these facts immediately. \(\square\)

Lemma 14. On the domain $U_{\frac{1}{2} \leq r \leq \frac{3}{4}}, \tilde{g}_{t}$ satisfies the following estimates:
$$\begin{aligned}
\left\|\tilde{g}_{t}-\hat{g}_{0}\right\| \hat{g}_{0} & =O(|t|), \\
\left|\log \left(\frac{\Omega_{t} \wedge \bar{\Omega}_{t}}{\tilde{\omega}_{t}^{2}}\right)\right| & =O\left(\varepsilon^{4}\right), \\
\left\|\operatorname{Ric}\left(\tilde{g}_{t}\right)-\operatorname{Ric}\left(\hat{g}_{0}\right)\right\|_{\hat{g}_{0}} & =O(|t|), \\
\left\|c_{2}\left(\tilde{g}_{t}\right)-c_{2}\left(\hat{g}_{0}\right)\right\|_{\hat{g}_{0}} & =O(|t|) .
\end{aligned}$$

Proof. By the construction of $\hat{\phi}_{t}$ and $\hat{g}_{t} \rightarrow \hat{g}_{0}$ smoothly, we have
$$\begin{aligned}
d d_{t}^{c}\left(r^{2}+\hat{\phi}_{0}\right) & =d d_{t}^{c}\left(r^{2}+\hat{\phi}_{t}\right)+d d_{t}^{c}\left(\hat{\phi}_{0}-\hat{\phi}_{t}\right) \\
& =\hat{g}_{t}+O(|t|)=\hat{g}_{0}+O(|t|),
\end{aligned}$$
$$d d_{t}^{c}\left(\chi_{\left(\frac{1}{2}, \frac{3}{4}\right)}(r)\left(\hat{\phi}_{t}-\hat{\phi}_{t}\right)\right)=O(|t|) .$$

In particular, we obtain the first assertion (115). For (116), recall that for the complex structure $I_{t}=I_{\zeta(t)}$, we have the following estimate (see lemma (1)) :
$$\begin{aligned}
I_{\zeta(t)} & =I_{0}+I_{\zeta}^{(2)} r^{-4}+O\left(r^{-6}\right) \\
& =I_{0}+O\left(\varepsilon^{4}\right),
\end{aligned}$$
where $I_{\zeta}^{(2)}$ is a homogeneous polynomial in $\zeta$ of degree 2 (recall that $\zeta(t)=t^{p} \dot{\zeta}+$ $O\left(t^{p+1}\right)$ and $\varepsilon^{2}=|t|^{p}$ ). By direct calculation, we have the following:
$$\begin{aligned}
\tilde{\omega}_{t}^{2} & =\left(\hat{g}_{t}+d d_{t}^{c}\left(\left(\hat{\phi}_{0}-\hat{\phi}_{t}\right)+\chi_{(1 / 2,3 / 4)}(r)\left(\hat{\phi}_{t}-\hat{\phi}_{0}\right)\right)^{2}\right. \\
& =\hat{\omega}_{t}^{2}+\hat{\omega}_{t} \wedge d d_{t}^{c}\left(\left(\hat{\phi}_{0}-\hat{\phi}_{t}\right)+\chi_{(1 / 2,3 / 4)}(r)\left(\hat{\phi}_{t}-\hat{\phi}_{0}\right)\right) \\
& +\left(d d_{t}^{c}\left(\left(\hat{\phi}_{0}-\hat{\phi}_{t}\right)+\chi_{(1 / 2,3 / 4)}(r)\left(\hat{\phi}_{t}-\hat{\phi}_{0}\right)\right)\right)^{2} .
\end{aligned}$$
The first term is equal to $\Omega_{t} \wedge \bar{\Omega}_{t}$. For the second and the third terms, we use the following estimates:
$$\left(\hat{\omega}_{t}-\hat{\omega}_{0}\right)\left(\hat{\omega}_{t}+\hat{\omega}_{0}\right)=\Omega_{t} \wedge \bar{\Omega}_{t}-\Omega_{0} \wedge \bar{\Omega}_{0}=O\left(\varepsilon^{4}\right) \Omega_{0} \wedge \bar{\Omega}_{t},$$
and there exists a constant $C>0$ independent of $t$ such that
$$C^{-1}\left\|d d_{t}^{c}\left(\hat{\phi}_{t}-\hat{\phi}_{0}\right)\right\|_{\hat{g}_{t}}<\left\|d d_{t}^{c}\left(\left(\chi_{(1 / 2,3 / 4)}(r)-1\right)\left(\hat{\phi}_{t}-\hat{\phi}_{0}\right)\right)\right\|_{\hat{g}_{t}}<C\left\|d d_{t}^{c}\left(\hat{\phi}_{t}-\hat{\phi}_{0}\right)\right\|_{\hat{g}_{t}},$$
$$C^{-1} \hat{g}_{0}<\hat{g}_{t}<C \hat{g}_{0} .$$
Then, we obtain the followings:
$$\hat{\omega}_{t} \wedge d d_{t}^{c}\left(\hat{\phi}_{0}-\hat{\phi}_{t}\right)=O\left(\varepsilon^{4}\right) \hat{\omega}_{t}^{2}$$
$$\left(d d_{t}^{c}\left(\hat{\phi}_{t}-\hat{\phi}_{0}\right)\right)^{2}=O\left(\varepsilon^{4}\right) \hat{\omega}_{t}^{2} .$$
Therefore, $\log \left(\frac{\Omega_{t} \wedge \bar{\Omega}_{t}}{\tilde{\omega}_{t}^{2}}\right)=O\left(\varepsilon^{4}\right)$ on this domain. The last assertion (118) can be confirmed by the similar arguments as in section 3 (namely, the proofs of lemma 5 for example). Explicitly, direct calculation yields
$$\begin{aligned}
\tilde{g}_{t}^{-1} & =\hat{g}_{0}^{-1}+O(|t|) \\
\partial_{t} \tilde{g}_{t} & =\partial_{0} \hat{g}_{0}+O(|t|) \\
\partial_{t}^{2} \tilde{g}_{t} & =\partial_{0}^{2} \hat{g}_{0}+O(|t|),
\end{aligned}$$
under the trivialization by $\left\{e_{t}^{1}, e_{t}^{2}\right\}$, where $\partial_{t}$ denotes any differential by the vector fields $\left\{e_{t}^{1}, e_{t}^{2}\right\}$ defined in Lemma 1. Then we have (117) (118). \(\square\)

Lemma 15. On the domain $U_{2 \varepsilon^{1 / 2} \leq r \leq \frac{1}{2}}, \tilde{g}_{t}$ satisfies the following estimates:
$$\begin{aligned}
\left\|\tilde{g}_{t}-\hat{g}_{0}\right\|_{\hat{g}_{0}} & =O\left(\varepsilon^{4} r^{-4}\right), \\
\log \left(\frac{\Omega_{t} \wedge \bar{\Omega}_{t}}{\tilde{\omega}_{t}^{2}}\right) & =O\left(\varepsilon^{4} r^{-4}\right), \\
\left\|\operatorname{Ric}\left(\tilde{g}_{t}\right)-\operatorname{Ric}\left(\hat{g}_{0}\right)\right\|_{\hat{g}_{0}} & =O\left(\varepsilon^{4} r^{-4}\right), \\
\left\|c_{2}\left(\tilde{g}_{t}\right)-c_{2}\left(\hat{g}_{0}\right)\right\|_{\hat{g}_{0}} & =O\left(\varepsilon^{4} r^{-4}\right) .
\end{aligned}$$

Proof. On this domain, we have the following estimate on the complex structure $I_{\zeta(t)}$ :
$$I_{\zeta(t)}=I_{0}+O\left(\varepsilon^{4} r^{-4}\right) .$$
In particular, we have
$$\begin{aligned}
\tilde{g}_{t} & =d d_{t}^{c}\left(r^{2}+\hat{\phi}_{0}\right) \\
& =d d_{0}^{c}\left(r^{2}+\hat{\phi}_{0}\right)+O\left(\varepsilon^{4} r^{-4}\right) \\
& =\hat{g}_{0}+O\left(\varepsilon^{4} r^{-4}\right) .
\end{aligned}$$
Therefore,
$$\begin{aligned}
\tilde{\omega}_{t}^{2} & =\hat{\omega}_{0}^{2}+O\left(\varepsilon^{4} r^{-4}\right) \Omega_{t} \wedge \bar{\Omega}_{t} \\
& =\left(1+O\left(\varepsilon^{4} r^{-4}\right)\right) \Omega_{t} \wedge \bar{\Omega}_{t} .
\end{aligned}$$
Again, (133) and (134) follows from a direct calculation as in the proof of Lemma 14. \(\square\)

Lemma 16. On $U_{\varepsilon^{1 / 2} \leq r \leq 2 \varepsilon^{1 / 2}}, \tilde{g}_{t}$ satisfies the following estimates:
$$\begin{aligned}
\tilde{g}_{t} & =g_{\zeta(t)}+O(\varepsilon), \\
\log \left(\frac{\Omega_{t} \wedge \bar{\Omega}_{t}}{\tilde{\omega}_{t}^{2}}\right) & =O\left(\varepsilon^{2}\right), \\
\left\|\operatorname{Ric}\left(\tilde{g}_{t}\right)-\operatorname{Ric}\left(\hat{g}_{0}\right)\right\|_{\hat{g}_{0}} & =O(\varepsilon), \\
c_{2}\left(\tilde{g}_{t}\right) & =c_{2}\left(g_{\zeta(t)}\right)+O(\varepsilon) .
\end{aligned}$$
Proof. By direct calculation, we have the following:
$$\begin{aligned}
d d_{t}^{c}\left(\chi_{\left(\varepsilon^{1 / 2}, 2 \varepsilon^{1 / 2}\right)}(r)\left(\hat{\phi}_{0}-\phi_{\zeta(t)}\right)\right) & =\frac{\chi_{\left(\varepsilon^{1 / 2}, 2 \varepsilon^{1 / 2}\right)}^{\prime}(r)\left(\hat{\phi}_{0}-\phi_{\zeta(t)}\right)}{\varepsilon^{1 / 2}} d d_{t}^{c} r \\
& +\frac{\chi_{\left(\varepsilon^{1 / 2}, 2 \varepsilon^{1 / 2}\right)}^{\prime \prime}(r)\left(\hat{\phi}_{0}-\phi_{\zeta(t)}\right)}{\varepsilon} d r \wedge d_{t}^{c} r \\
& +\frac{\chi_{\left(\varepsilon^{1 / 2}, 2 \varepsilon^{1 / 2}\right)}^{\prime}(r)}{\varepsilon^{1 / 2}}\left(d\left(\hat{\phi}_{0}-\phi_{\zeta(t)}\right) \wedge d_{t}^{c} r+d r \wedge d_{t}^{c}\left(\hat{\phi}_{0}-\phi_{\zeta(t)}\right)\right) \\
& +\chi_{\left(\varepsilon^{1 / 2}, 2 \varepsilon^{1 / 2}\right)}(r) d d_{t}^{c}\left(\hat{\phi}_{0}-\phi_{\zeta(t)}\right) .
\end{aligned}$$
As $\hat{\phi}_{0}=O\left(r^{4}\right), \phi_{\zeta(r)}=O\left(\varepsilon^{4} r^{-4}\right)$ and $r=O\left(\varepsilon^{1 / 2}\right)$, we have
$$d d_{t}^{c}\left(\chi_{\left(\varepsilon^{1 / 2}, 2 \varepsilon^{1 / 2}\right)}(r)\left(\hat{\phi}_{0}-\phi_{\zeta(t)}\right)\right)=O(\varepsilon)$$
as $|t| \rightarrow 0$. In particular, we have
$$\tilde{g}_{t}=g_{\zeta(t)}+O(\varepsilon) .$$
By direct calculation, we have the following:
$$\begin{aligned}
\tilde{\omega}_{t}^{2} & =\left(\omega_{\zeta(t)}+d d_{t}^{c}\left(\chi_{\left(\varepsilon^{1 / 2}, 2 \varepsilon^{1 / 2}\right)}(r)\left(\hat{\phi}_{0}-\phi_{\zeta(t)}\right)\right)\right)^{2} \\
& =\Omega_{t} \wedge \bar{\Omega}_{t}+2 \omega_{\zeta(t)} \wedge d d_{t}^{c}\left(\chi_{\left(\varepsilon^{1 / 2}, 2 \varepsilon^{1 / 2}\right)}(r)\left(\hat{\phi}_{0}-\phi_{\zeta(t)}\right)\right) \\
& +\left(d d_{t}^{c}\left(\chi_{\left(\varepsilon^{1 / 2}, 2 \varepsilon^{1 / 2}\right)}(r)\left(\hat{\phi}_{0}-\phi_{\zeta(t)}\right)\right)\right)^{2} .
\end{aligned}$$
For the second and the third terms, we use the following estimates:
$$\left(\omega_{\zeta(t)}-\hat{\omega}_{0}\right)\left(\omega_{\zeta(t)}+\hat{\omega}_{0}\right)=\Omega_{t} \wedge \bar{\Omega}_{t}-\Omega_{0} \wedge \bar{\Omega}_{0}=O\left(\varepsilon^{2}\right) \Omega_{0} \wedge \bar{\Omega}_{t},$$
and there exists a constant $C>0$ independent of $t$ such that
$$\begin{aligned}
& C^{-1}\left\|d d_{t}^{c}\left(\hat{\phi}_{0}-\phi_{\zeta(t)}\right)\right\|_{\hat{g}_{0}}<\left\|d d_{t}^{c}\left(\left(\chi_{\left(\varepsilon^{1 / 2}, 2 \varepsilon^{1 / 2}\right)}(r)\right)\left(\hat{\phi}_{0}-g_{\zeta(t)}\right)\right)\right\|_{\hat{g}_{0}}<C\left\|d d_{t}^{c}\left(\hat{\phi}_{0}-g_{\zeta(t)}\right)\right\|_{\hat{g}_{0}}, \\
& \begin{array}{l}
(148) \quad C^{-1} \hat{g}_{0}<g_{\zeta(t)}<C \hat{g}_{0}
\end{array} .
\end{aligned}$$
Then, we obtain the followings:
$$\begin{aligned}
\hat{\omega}_{t} \wedge d d_{t}^{c}\left(\hat{\phi}_{0}-\hat{\phi}_{t}\right) & =O\left(\varepsilon^{2}\right) \hat{\omega}_{t}^{2} \\
\left(d d_{t}^{c}\left(\hat{\phi}_{t}-\hat{\phi}_{0}\right)\right)^{2} & =O\left(\varepsilon^{2}\right) \hat{\omega}_{t}^{2} .
\end{aligned}$$
Therefore, $\log \left(\frac{\Omega_{t} \wedge \bar{\Omega}_{t}}{\tilde{\omega}_{t}^{2}}\right)=O\left(\varepsilon^{2}\right)$ on this domain. \(\square\)

For later use, we also give estimates for rescaled data.
Lemma 17. Let $\tilde{g}_{t}, \hat{g}_{t}, f_{t}$ are as above. Consider the following rescaled data:
$$\begin{aligned}
\tilde{h}_{t} & :=\frac{1}{\varepsilon^{2}} H_{\left(\zeta / \varepsilon^{2}, \varepsilon\right)}^{*} \tilde{g}_{t} \quad \text { and } \\
k_{t} & :=H_{\left(\zeta / \varepsilon^{2}, \varepsilon\right)}^{*} f_{t},
\end{aligned}$$
on the domain $Y_{t}:=Y_{\zeta / \varepsilon^{2}, r<1 / \varepsilon}$. Then, the following estimates hold:
$$\begin{gathered}
\sup _{Y_{t}}\left\|\operatorname{Rm}\left(\tilde{h}_{t}\right)\right\|_{\tilde{h}_{t}}<C, \\
\left\|k_{t}\right\|_{C^{1}\left(Y_{t}\right)}<C \varepsilon^{2},
\end{gathered}$$
for some constant $C>0$ independent of $t$.
Proof. Note that
$$k_{t}=\log \left(\frac{\frac{1}{\varepsilon^{2}} H_{\left(\zeta / \varepsilon^{2}, \varepsilon\right)}^{*} \Omega_{t} \wedge \frac{1}{\varepsilon^{2}} H_{\left(\zeta / \varepsilon^{2}, \varepsilon\right)}^{*} \bar{\Omega}_{t}}{\tilde{\varpi}_{t}^{2}}\right),$$
where $\tilde{\varpi}_{t}$ is the Kähler form of $\tilde{h}_{t}$. We take a similar strategy to the above lemmas. Namely, for the domain $\left\{r<\varepsilon^{-\frac{1}{2}}\right\}$ (corresponds to $\left\{r<\varepsilon^{\frac{1}{2}}\right\}$ in $X_{t}$ ), we have $\tilde{h}_{t}=g_{\zeta(t) / \varepsilon^{2}}$ which converges to $g_{\dot{\zeta}}$ locally uniformly in $C^{\infty}$ sense. Additionally, they are ALE gravitational instantons then by taking a compact subset $K$ of $Y$ (the underlying differentiable manifold of $Y_{\zeta} \mathrm{s}$ ), the curvatures are of $O\left(r^{-6}\right)$ outside of $K$ uniformly with respect to $t$. Then the norm of curvature is uniformly bounded in this domain. By construction of $\Omega_{t}$, we have $\tilde{\varpi}_{t}^{2}=\omega_{\zeta / \varepsilon^{2}}^{2}=\varepsilon^{-4} H_{\left(\zeta / \varepsilon^{2}, \varepsilon\right)}^{*}\left(\Omega_{t} \wedge \bar{\Omega}_{t}\right)$. Therefore, $k_{t} \equiv 0$ on this domain.

For $\left\{\varepsilon^{-\frac{1}{2}}<r<2 \varepsilon^{-\frac{1}{2}}\right\}$, we see that
$$\tilde{h}_{t}=g_{\zeta / \varepsilon^{2}}+O\left(\varepsilon^{3}\right)$$
by the similar calculation to the lemma 16. And for the holomorphic 2-form, we have
$$\frac{1}{\varepsilon^{2}} H_{\left(\zeta / \varepsilon^{2}, \varepsilon\right)}^{*} \Omega_{t}=\frac{1}{\varepsilon^{2}} H_{(\dot{\zeta}, \varepsilon)}^{*} \Omega_{0}+O\left(\varepsilon^{2}\right) .$$
Then, in particular, we have $\left\|\nabla k_{t}\right\|=O\left(\varepsilon^{2}\right)$ on this domain.
For $\left\{2 \varepsilon^{-\frac{1}{2}}<r<\frac{1}{2} \varepsilon^{-1}\right\}$, we have
$$\tilde{h}_{t}=\frac{1}{\varepsilon^{2}} H_{\left(\zeta / \varepsilon^{2}, \varepsilon\right)}^{*} \hat{g}_{t}+O\left(\varepsilon^{2}\right)$$
by the similar calculation as the lemma 15. Also, for the holomorphic 2-form, we have
$$\frac{1}{\varepsilon^{2}} H_{\left(\zeta / \varepsilon^{2}, \varepsilon\right)}^{*} \Omega_{t}=\frac{1}{\varepsilon^{2}} H_{(\dot{\zeta}, \varepsilon)}^{*} \Omega_{0}+O\left(\varepsilon^{2}\right)$$
by a similar calculation as the lemma 15. This implies $\left\|\nabla k_{t}\right\|=O\left(\varepsilon^{2}\right)$ on this domain. \(\square\)

We also need the next lemma to derive a fine $C^{0}$ estimates.
Lemma 18.
$$\left\|f_{t}\right\|_{L_{\tilde{g}_{t}}^{p}}<C \varepsilon^{2+\frac{2}{p}}$$
for any $1<p \leq \frac{4}{3}$ with some constant $C>0$ independent of $p$ and $t$
Proof. As $f \equiv 0$ on $X_{t} \backslash U_{r<3 / 4}$ and $U_{r \leq \varepsilon^{1 / 2}}$, we see that
$$\int_{X_{t}}\left|f_{t}\right|^{p} \operatorname{Vol}_{\tilde{g}_{t}}=\int_{U_{\varepsilon^{1 / 2} \leq r \leq 2 \varepsilon^{1 / 2}}}\left|f_{t}\right|^{p}+\int_{U_{2 \varepsilon^{1 / 2} \leq r \leq 1 / 2}}\left|f_{t}\right|^{p}+\int_{U_{1 / 2 \leq r \leq 3 / 4}}\left|f_{t}\right|^{p} .$$
For the first term and the third term, by the estimates (namely inequalities 116 and 139), we obtain
$$\begin{array}{r}
\int_{U_{\varepsilon^{1 / 2} \leq r \leq 2 \varepsilon^{1 / 2}}}\left|f_{t}\right|^{p}<C \varepsilon^{2 p+2}, \\
\int_{U_{1 / 2 \leq r} \leq 3 / 4}\left|f_{t}\right|^{p}<C \varepsilon^{4 p}
\end{array}$$
for some constant $C>0$ independent of $1 \leq p$ and $t$. For the second term, we have
$$\begin{aligned}
\int_{U_{2 \varepsilon^{1 / 2} \leq r \leq 1 / 2}}\left|f_{t}\right|^{p} & <C \varepsilon^{4 p} \int_{2 \varepsilon^{1 / 2}}^{1 / 2} r^{-4 p+3} d r \\
& <C \varepsilon^{2 p+2}
\end{aligned}$$
for some constant $C>0$ independent of $1<p \leq 4 / 3$ and $t$. Therefore, we have
$$\left\|f_{t}\right\|_{p}<C \varepsilon^{2+\frac{2}{p}} .$$ \(\square\)

By the above lemmas, in particular the estimates (115), (131) and (138), we see that $\tilde{g}_{t}$ is a metric on $X_{t}$. As $\tilde{g}_{t}$ is a Kähler metric on $X_{t}$ cohomologous to $\hat{g}_{t}$, we may consider the following Monge-Ampère equation using $\tilde{g}_{t}$ as the initial data:
$$\left\{\begin{array}{rl}
\left(\tilde{\omega}_{t}+d d_{t}^{c} u_{t}\right)^{2} & =e^{f_{t}} \tilde{\omega}_{t}^{2} \\
\int_{X_{t}} u_{t} \tilde{\omega}_{t}^{2} & =0
\end{array},\right.$$
where $f_{t}=\log \left(\frac{\Omega_{t} \wedge \bar{\Omega}_{t}}{\tilde{\omega}_{t}^{2}}\right)$. Recall that $\Omega_{t}$ is the nowhere vanishing holomorphic 2-form on $X_{t}$ such that $\Omega_{t} \wedge \bar{\Omega}_{t}=\hat{\omega}_{t}^{2}$. By the above lemmas, in particular the estimates (116), (132) and (139), we see that $f_{t}$ is $\varepsilon^{2}$ times a smooth function on $X_{t}$ uniformly bounded with respect to $t$.

Using the estimate of $f_{t}$, we derive a $C^{0}$-estimate on $u_{t}$ by following [16].

Proposition 2. Let $u_{t}$ be the solution of the equation (163). Then we have
$$\left\|u_{t}\right\|_{C^{0}\left(X_{t}\right)}<C \varepsilon^{4}$$
for some constant $C>0$ independent of $t$.
Proof. We prove it by Moser's iteration argument. By assumption that $u_{t}$ is the solution, we have
$$\begin{aligned}
\left(1-e^{f_{t}}\right) \tilde{\omega}_{t}^{2} & =\tilde{\omega}_{t}^{2}-\hat{\omega}_{t}^{2} \\
& =-\left(d d_{t}^{c} u_{t}\right) \wedge\left(\tilde{\omega}_{t}+\hat{\omega}_{t}\right) .
\end{aligned}$$
Multiplying $\left|u_{t}\right|^{p-2} u_{t}$ both side (for $p>1$ ) and integration by parts yields that
$$\int_{X_{t}}\left|1-e^{f_{t}}\right|\left|u_{t}\right|^{p-2} u_{t} \tilde{\omega}_{t}^{2} \geq \frac{4(p-1)}{p^{2}} \int_{X_{t}} \sqrt{-1} \partial\left|u_{t}\right|^{\frac{p}{2}} \wedge \bar{\partial}\left|u_{t}\right|^{\frac{p}{2}} \wedge \tilde{\omega}_{t} .$$
Then, as $\left|f_{t}\right|$ is sufficiently small (namely, $\left|f_{t}\right|<C \varepsilon^{2}$ for some $C>0$ independent of $t$ ), we have the following:
$$\int_{X_{t}}\left\|d\left|u_{t}\right|^{\frac{p}{2}}\right\|_{\tilde{g}_{t}}^{2} \operatorname{Vol}_{\tilde{g}_{t}} \leq p C \int_{X_{t}}\left|f_{t}\right|\left|u_{t}\right|^{p-1} \operatorname{Vol}_{\tilde{g}_{t}} .$$
Here, we use the Sobolev inequality on manifolds:
Lemma 19 ([12]). Let $(X, g)$ be a m-dimensional compact Riemannian manifold. Assume that
$$\operatorname{diam}(X, g)^{2} \operatorname{Ric}(g) \geq-\alpha^{2} g$$
for some constant $\alpha>0$. Then there exists a constant $\kappa=\kappa(m, \alpha)>0$ such that
$$\kappa \frac{\operatorname{Vol}(X, g)^{\frac{1}{m}}}{\operatorname{diam}(X, g)}\|u\|_{L^{\frac{2 m}{m-2}}} \leq\|d u\|_{L^{2}}$$
for any $u \in C^{\infty}(X)$ with $\int_{X} u \operatorname{Vol}_{g}=0$.
As the diameters, volumes and Ricci curvatures of $\left\{\tilde{g}_{t}\right\}$ are uniformly bounded, we have a uniform Sobolev constant. Then, applying Sobolev inequality to the left hand side of (167) with $p=2$ and the Hölder inequality for the right hand side, we obtain
$$\left\|u_{t}\right\|_{L^{4}}^{2} \leq C\left\|f_{t}\right\|_{L^{q}}\left\|u_{t}\right\|_{L^{r}}$$
for any $q, r>1$ with $\frac{1}{q}+\frac{1}{r}=1$. By taking $r=4$, we have
$$\left\|u_{t}\right\|_{L^{4}} \leq C \varepsilon^{2+\frac{2}{q}},$$
where $C>0$ is independent of $t$. Therefore, by Moser's iteration argument, we have the $C^{0}$ estimate
$$\left\|u_{t}\right\|_{C^{0}} \leq C \varepsilon^{4} .$$ \(\square\)

As the curvature of $\tilde{g}_{t}$ diverges on $U_{t}$ as $t \rightarrow 0$, we consider the rescaled metrics $\hat{h}_{t}=\frac{1}{\varepsilon^{2}} H_{\left(\varepsilon, \zeta / \varepsilon^{2}\right)}^{*} \hat{g}_{t}$ and $\tilde{h}_{t}=\frac{1}{\varepsilon^{2}} H_{\left(\varepsilon, \zeta / \varepsilon^{2}\right)}^{*} \tilde{g}_{t}$ on $U_{t}$ to get $C^{2}$ and higher order estimates. For these rescaled metrics, we have the following equation:
$$\left(\tilde{\varpi}_{t}+d d_{t}^{c} v_{t}\right)^{2}=e^{k_{t}} \tilde{\varpi}_{t}^{2},$$
where $v_{t}=\frac{1}{{\underset{̨}{\varepsilon}}^{2}} H_{\left(\varepsilon, \zeta / \varepsilon^{2}\right)}^{*} u_{t}, k_{t}=H_{\left(\varepsilon, \zeta / \varepsilon^{2}\right)}^{*} f_{t}$ and $\tilde{\varpi}_{t}$ the Kähler form of $\tilde{h}_{t}$. Note that $\left(Y_{\zeta / \varepsilon, r<1 / \varepsilon}, h_{t}\right)$ converges to $Y_{\dot{\zeta}}$ locally uniformly in $C^{\infty}$ sense (by non-degeneracy assumption), therefore, $\tilde{h}_{t}$ has uniformly bounded curvatures and injectivity radius that approaches to those of the Euclidean metric outside of a compact subset. For $C^{2}$ estimate of $v_{t}$, we use the next equality .

Proposition 3 ([25] Lemma 3.7). Let $(X, g)$ be a Kähler manifold (not necessarily compact!) of dimension $n$. Then, for any Kähler metric $\omega^{\prime}=\omega+d d^{c} u$, the following inequality holds:
$$\Delta_{g^{\prime}}\left(\log \left(\operatorname{Tr}_{g} g^{\prime}\right)\right) \geq A \operatorname{Tr}_{g^{\prime}} g-\frac{g^{j \bar{k}} R_{j \bar{k}}^{\prime}}{\operatorname{Tr}_{g} g^{\prime}},$$
where $R^{\prime}$ is the Ricci curvature of $g^{\prime}$ and $A>0$ is a constant depending on the bisectional curvature of $g$.

We apply the above inequality for $g=\tilde{h}_{t}$ and $u=v_{t}$ (hence $g^{\prime}=\hat{h}_{t}$ ). As $\hat{h}_{t}$ converges to an ALE gravitational instanton $Y_{\dot{\zeta}}$, we may take $A$ independent of $t$. Then we have
$$\Delta_{\hat{h}_{t}}\left(\log \left(\operatorname{Tr}_{\tilde{h}_{t}} \hat{h}_{t}\right)\right) \geq A \operatorname{Tr}_{\hat{h}_{t}} \tilde{h}_{t}$$
as $\hat{h}_{t}$ is a Ricci flat metric. As $u_{t}$ is pluriharmonic and $\log \left(\operatorname{Tr}_{\tilde{g}_{t}} \hat{g}_{t}\right)=$ const. on $3 / 4<$ $r, \max _{X_{t}}\left(\log \left(\operatorname{Tr}_{\tilde{g}_{t}} \hat{g}_{t}\right)-A u_{t}\right)=\max _{U}\left(\log \left(\operatorname{Tr}_{\tilde{g}_{t}} \hat{g}_{t}\right)-A u_{t}\right)$. Assume $\log \left(\operatorname{Tr}_{\tilde{h}_{t}} \hat{h}_{t}\right)-A v_{t}$ attains a maximum value at some point $p \in Y_{\zeta(t) / \varepsilon^{2}, r \leq 1 / \varepsilon}$. Then we have
$$\begin{aligned}
0 & \geq \Delta_{\hat{h}_{t}}\left(\log \left(\operatorname{Tr}_{\tilde{h}_{t}} \hat{h}_{t}\right)-A u_{t}\right)(p) \\
& \geq 2 A\left(\operatorname{Tr}_{\hat{h}_{t}} \tilde{h}_{t}(p)-1\right)
\end{aligned}$$
In particular, we see that
$$\frac{1}{2 A} \geq\left(\operatorname{Tr}_{\tilde{h}_{t}} \hat{h}_{t}\right)(p)$$
with a constant $A>0$ independent of $t$. Therefore, we obtain
$$\sup _{Y_{\zeta(t) / \varepsilon^{2}, r<1 / \varepsilon}} \operatorname{Tr}_{\tilde{h}_{t}} \hat{h}_{t} \leq \exp \left(A_{1}+A_{2}\left\|v_{t}\right\|_{\infty}\right),$$
with constants $A_{i}$ independent of $t$. Therefore, we have a $C^{2}$ estimate of $v_{t}$ :
$$\left\|d d_{t}^{c} v_{t}\right\|_{\tilde{h}_{t}} \leq C,$$
where $C>0$ is a constant independent of $t$ on $Y_{\zeta / \varepsilon^{2}, r<1 / \varepsilon}$. As the same, applying (175) for $g=\tilde{g}_{t}$ and $g^{\prime}=\hat{g}_{t}$, we have a uniform $C^{2}$ estimate on $X_{t} \backslash U$ :
$$\sup _{X_{t} \backslash U} \operatorname{Tr}_{\tilde{g}_{t}} \hat{g}_{t} \leq \exp \left(A_{1}+A_{2}\left\|u_{t}\right\|_{\infty}\right)<C .$$

Proposition 4. In the above situation, we have the following $C^{2}$ estimates:
$$\begin{aligned}
& \left\|d d_{t}^{c} v_{t}\right\|_{\tilde{h}_{t}} \leq C \quad \text { and } \\
& \left\|d d_{t}^{c} u_{t}\right\|_{\tilde{g}_{t}} \leq C,
\end{aligned}$$
for some constant $C>0$ independent of $t$.

By the general theory of non-linear elliptic equation, $v_{t}$ automatically has uniformly bounded $C_{\tilde{h}_{t}}^{2, \alpha}$ norm for some $0<\alpha<1$ depending on $\tilde{h}_{t}, u_{t}, \partial u_{t}, \partial^{2} u_{t}$ (see [13] Theorem 17.14 and [23] Chapter 2 section 4).

Proposition 5. In the above situation, the followings holds:
$$\begin{aligned}
\left\|u_{t}\right\|_{C_{\tilde{g}_{t}}^{2, \alpha}\left(X_{t} \backslash U\right)} & <C, \\
\left\|v_{t}\right\|_{C_{\tilde{h}_{t}}^{2, \alpha}\left(Y_{\zeta / \varepsilon^{2}, r<1 / \varepsilon}\right)} & <C,
\end{aligned}$$
for some constants $C>0$ and $0<\alpha<1$ independent of $t$.
We now consider the following deformation of equation (163):
$$\left\{\begin{array}{c}
\left(\tilde{\omega}_{t}+d d_{t}^{c} u_{t, s}\right)^{2}=e^{s f_{t}} \tilde{\omega}_{t}^{2} \\
\int_{X_{t}} u_{t, s} \tilde{\omega}_{t}^{2}=0
\end{array},\right.$$
where $s \in[0,1]$ is a parameter. Note that we obtain the original equation by letting $s=1$ and obtain an equation which has a trivial solution by letting $s=0$. By differentiating the equation with respect to $s$, we have
$$\left\{\begin{array}{c}
\Delta_{t, s} \frac{\partial u_{t, s}}{\partial s}=f_{t} \\
\int_{X_{t}} \frac{\partial u_{t, s}}{\partial s} \operatorname{Vol}_{g_{t, s}}=0
\end{array},\right.$$
where $\Delta_{t, s}$ is the Laplacian of the Kähler metric $\tilde{g}_{t}+d d_{t}^{c} u_{t, s}$. Also, we consider the linearization of the rescaled equation:
$$\tilde{\Delta}_{t, s}\left(\frac{\partial v_{t, s}}{\partial s}\right)=k_{t} .$$
We obtain the following estimates by the same arguments as above but $f_{t}$ being replaced by $s f_{t}$ :
$$\begin{aligned}
\left\|u_{t, s}\right\|_{C^{0}\left(X_{t}\right)} & <C \varepsilon^{4}, \\
\left\|u_{t, s}\right\|_{C_{\tilde{g}_{t}}^{2, \alpha}\left(X_{t} \backslash U\right)} & <C, \\
\left\|v_{t, s}\right\|_{C_{\tilde{h}_{t}}^{2, \alpha}\left(Y_{\zeta / \varepsilon^{2}, r<1 / \varepsilon}\right)} & <C,
\end{aligned}$$
for some constants $C>0$ and $0<\alpha<1$ independent of $t$ and $s$. We use the Schauder estimate for linear elliptic equations to derive a fine $C^{2}$ estimate for $\frac{\partial u_{t, s}}{\partial s}$.

Proposition 6 ([13] Theorem 6.2). Let $\Omega \subset \mathbb{R}^{n}$ be a bounded domain and let $u \in C^{2, \alpha}(\Omega)$ be a bounded solution of the equation
$$L u=f,$$
where $L=\sum_{l, k} a_{j, k} \partial_{j} \partial_{k}+\sum_{l} b_{l} \partial_{l}+c$ is a strictly elliptic operator with $\left(a_{j, k}\right) \geq \lambda>0$ (as a quadratic form). Assume that
\begin{itemize}
\item[-] $f$ is $\alpha$ - Hölder continuous on $\Omega$ and
\item[-] $\left\|a_{l, k}\right\|_{C^{0, \alpha}(\Omega)},\left\|b_{l}\right\|_{C^{0, \alpha}(\Omega)},\|c\|_{C^{0, \alpha}(\Omega)} \leq \Lambda$.
\end{itemize}

Then, for any open subset $\Omega^{\prime} \subset \subset \Omega$, there exists a (positive) constant $C=C\left(n, \alpha, \lambda, \Lambda, \operatorname{diam}(\Omega), \operatorname{dist}\left(\Omega^{\prime}, \partial \Omega\right)\right)$ so that
$$\|u\|_{C^{2, \alpha}\left(\Omega^{\prime}\right)} \leq C\left(\|u\|_{C^{0}(\Omega)}+\|f\|_{C^{0, \alpha}(\Omega)}\right) .$$

First, we apply the estimate for the equation (185).
Proposition 7. Let $\frac{\partial u_{t, s}}{\partial s}$ be a solution of (185) on the domain $\Omega=X_{t} \backslash U_{r \leq 1}$. Then,
$$\left\|\frac{\partial u_{t, s}}{\partial s}\right\|_{C^{2, \alpha}(\Omega)} \leq C \varepsilon^{2},$$
for some constant $C>0$ independent of $s$ and $t$.
Proof. Apply the inequality (190). In this case, $a_{i, j}=\left(\tilde{g}+d d_{t}^{c} u_{t, s}\right)^{i, j}$, which we already have a uniform estimate (188), and $b_{l}=c=0$. Also, note that multiplying $\frac{\partial u_{t, s}}{\partial s}\left|\frac{\partial u_{t, s}}{\partial s}\right|^{p-2}$ both side of the equation (185) yields the inequality which is same form as (167). By the estimate (188) and an equality $\operatorname{Ric}\left(\tilde{g}_{t}+d d_{t}^{c} u_{t, s}\right)=s \operatorname{Ric}\left(\tilde{g}_{t}\right)$, we have a uniform (with respect to $t$ and $s$ ) Sobolev constant for $\tilde{g}_{t}+d d_{t}^{c} u_{t, s}$ hence we have a uniform $C^{0}$ estimate $\left\|\frac{\partial u_{t, s}}{\partial s}\right\|_{C^{0}\left(X_{t}\right)}<C \varepsilon^{4}$ by the Moser iteration argument again. Then we have a uniform estimate
$$\left\|\frac{\partial u_{t, s}}{\partial s}\right\|_{C^{2, \alpha}(\Omega)} \leq C \varepsilon^{4}+\left\|f_{t}\right\|_{C^{0, \alpha}(\Omega)} \leq C \varepsilon^{2} .$$ \(\square\)

Proposition 8. Let $\frac{\partial v_{t, s}}{\partial s}$ be a solution of (186). Then,
$$\left|\frac{\partial v_{t, s}}{\partial s}\right|_{C_{\tilde{h}_{t}}^{2, \alpha}\left(Y_{\zeta / \varepsilon^{2}, r<1 / \varepsilon}\right)}<C \varepsilon^{2} .$$
Proof. Let $i_{t}$ be the injectivity radius of $\tilde{h}_{t}$. As $\tilde{h}_{t}$ converges to an ALE gravitational instanton $Y_{\dot{\zeta}}$, we have a uniform bound of $i_{t}$. In particular, we may cover $Y_{\zeta / \varepsilon^{2}, r<1 / \varepsilon}$ by geodesic balls $\left\{B\left(y, r_{0}\right)\right\}$ so that $\left\{B\left(y, r_{1}\right)\right\}$ still covers $Y_{\zeta / \varepsilon^{2}, r<1 / \varepsilon}$ for $r_{1}<r_{0}$ (of course, $r_{1}$ and $r_{0}$ are independent of $y$ and $t$ ). Fix $y \in Y_{\zeta / \varepsilon^{2}, r<1 / \varepsilon}$. Apply the inequality (190) to the equation (186) restricted to each ball $B\left(y, r_{0}\right)$, we have the following:
$$\left\|\frac{\partial v_{t, s}}{\partial s}\right\|_{C_{\tilde{h}_{t}}^{2, \alpha}\left(B\left(y, r_{1}\right)\right)}<C\left(\left\|\frac{\partial v_{t, s}}{\partial s}\right\|_{C^{0}\left(B\left(y, r_{0}\right)\right)}+\left\|k_{t}\right\|_{C_{\tilde{h}_{t}}^{0, \alpha}\left(B\left(y, r_{0}\right)\right)}\right)<C \varepsilon^{2}$$
for any $y \in Y_{\zeta / \varepsilon^{2}, r<1 / \varepsilon}$ with a constant $C>0$ independent of $y$ and $t$. \(\square\)

As an application of the above estimates, we prove the next theorem.
Theorem 9. Let $(\mathcal{X}, \mathcal{L}) \rightarrow \Delta$ be an analytic family of polarized K3 surfaces over the unit disc $\Delta \subset \mathbb{C}$ such that the fibre ( $X_{t}, L_{t}$ ) on $t \in \Delta$ is smooth for $t \neq 0$ and singular for $t=0$ with ADE singularities. Assume that the family $\mathcal{X} \rightarrow \Delta$ admits the minimal simultaneous resolution after taking the base change $\Delta_{d} \rightarrow \Delta$. Then
for any smooth function $f$ on $\mathcal{X}$ with its support around a singularity $x_{0} \in X_{0} \cong$ $0 \in \mathbb{C}^{2} / \Gamma$, the function
$$F(t)=\int_{X_{t}} f_{t} c_{2}\left(\hat{g}_{t}\right)$$
on $\Delta \backslash\{0\}$ extends to a Hölder continuous function on $\Delta$ with Hölder exponent at least $\frac{1}{d}$.
Proof. We take the similar strategy as the proof of theorem 7 to prove the theorem 9. Namely, we decompose the function $F$ as follows:
$$F(t)=\int_{X_{t}} f_{t} c_{2}\left(\tilde{g}_{t}\right)+\int_{X_{t}} d d_{t}^{c} f_{t} \wedge \tau,$$
where $\tau$ is the $(1,1)$ form defined by
$$\tau=\frac{1}{4 \pi^{2} \sqrt{-1}} \int_{0}^{1}\left(N_{s}\right)_{11}\left(R_{s}\right)_{22}-\left(N_{s}\right)_{21}\left(R_{s}\right)_{12}+\left(N_{s}\right)_{22}\left(R_{s}\right)_{11}-\left(N_{s}\right)_{12}\left(R_{s}\right)_{21} d s .$$
Here, we use a path $\left\{g_{s}\right\}_{s \in[0,1]}$ from $\tilde{g}_{t}$ to $\hat{g}_{t}$ defined by the solution of the equation (184) (i.e. $g_{s}=g_{t, s}$ ) instead of the linear path. By virtue of the $C^{2}$ estimates of $\frac{\partial u_{t, s}}{\partial s}$ and $\frac{\partial v_{t, s}}{\partial s}$, we may estimate $\int_{X_{t}} d d_{t}^{c} f_{t} \wedge \tau$ in a simpler way.

Lemma 20. $\left|\int_{X_{t}} d d_{t}^{c} f_{t} \wedge \tau\right| \leq C \varepsilon^{2}$.
Proof. By the Hölder inequality and the definition of $\tau$ (195), we have
$$\begin{aligned}
\left|\int_{X_{t}} d d_{t}^{c} f_{t} \wedge \tau\right| & \leq C\left\|d d_{t}^{c} f_{t}\right\|_{L^{2}\left(\tilde{g}_{t}\right)}\|\tau\|_{L^{2}\left(\tilde{g}_{t}\right)} \\
& \leq C\|\tau\|_{L^{2}\left(g_{t, s}\right)} \\
& \leq C \int_{0}^{1}\left\|N_{s}\right\|_{L^{\infty}}\left\|\operatorname{Rm}\left(g_{t, s}\right)\right\|_{L^{2}\left(g_{t, s}\right)} d s
\end{aligned}$$
for some constant $C>0$ independent of $t$. For the $L^{2}$-norm of $\operatorname{Rm}\left(g_{t, s}\right)$, we use the next formula

Lemma 21 (See [6], pp 82). Let $(M, g)$ be a 4-dimensional compact Riemannian manifold. Then the following equality holds:
$$\int_{M}\|\operatorname{Rm}(g)\|^{2}-4\|\operatorname{Ric}(g)\|^{2}+\|\operatorname{Sc}(g)\|^{2} \operatorname{Vol}_{g}=32 \pi^{2} e(M),$$
where $\operatorname{Rm}(g)$ is the total Riemannian curvature tensor, $\operatorname{Ric}(g)$ is the Ricci curvature tensor, $\operatorname{Sc}(g)$ is the scaler curvature and $e(M)$ is the Euler number of $M$.

In particular, applying the formula (197) to $\left(X_{t}, g_{t, s}\right)$, we obtain
$$\left\|\operatorname{Rm}\left(g_{s, t}\right)\right\|_{L^{2}}^{2}=768 \pi^{2}+4\left\|\operatorname{Ric}\left(g_{t, s}\right)\right\|_{L^{2}}^{2}-\left\|\operatorname{Sc}\left(g_{t, s}\right)\right\|_{L^{2}}^{2} .$$
Then by (113), (117) and (133), we have a uniform estimate
$$\left|4\left\|\operatorname{Ric}\left(g_{t, s}\right)\right\|_{L^{2}}^{2}-\left\|\operatorname{Sc}\left(g_{t, s}\right)\right\|_{L^{2}}^{2}\right| \leq C|t| .$$
In particular,
$$\left\|\operatorname{Rm}\left(g_{t, s}\right)\right\|_{L^{2}}<C$$
for a constant $C$ independent of $t$ and $s$. Recall that
$$N_{s}=g_{s}^{j \bar{k}} \frac{\partial\left(g_{s}\right)_{j \bar{k}}}{\partial s}=g_{s}^{j \bar{k}} \partial_{j} \bar{\partial}_{k} \frac{\partial u_{t, s}}{\partial s},$$
where $g_{s}=\tilde{g}_{t}+d d_{t}^{c} u_{t, s}$. The $C^{2}$-estimates for $\frac{\partial u_{t, s}}{\partial s}$ immediately implies the following estimate for $N_{s}$ :
$$\left\|N_{s}\right\|_{L^{\infty}\left(X_{t}\right)} \leq C \varepsilon^{2} .$$
Therefore, we obtain the desired estimate for $\int_{X_{t}} d d_{t}^{c} f_{t} \wedge \tau$. \(\square\)

For the integral $\int_{X_{t}} f_{t} c_{2}\left(\tilde{g}_{t}\right)$, we have the following estimate by (114), (118), (134) and (141) (by the parallel calculation as in the section 3):
$$\int_{X_{t}} f_{t} c_{2}\left(\tilde{g}_{t}\right)=\int_{X_{0}} f_{0} c_{2}\left(\hat{g}_{0}\right)+f\left(x_{0}\right) e_{o r b}\left(Y_{\dot{\zeta}}\right)+O(|t|) .$$
Lemma 20 and the estimate (203) implies the theorem 9. \(\square\)

\section*{References}
\begin{itemize}
\item[] [1] M. Anderson. The $L^{2}$ structure of moduli spaces of Einstein metrics on 4-manifolds. Geom. Funct. Anal., 2(1):29-89, 1992.
\item[] [2] T. Aubin. Equations du type Monge-Ampère sur les variétés kähleriennes compactes. C. R. Acad. Sci. Paris Ser. A, 283:119, 1976.
\item[] [3] S. Bando. Bubbling out of Einstein manifolds. Tohoku Math. J., 42:205-216, 1990.
\item[] [4] S. Bando, A. Kasue, and H. Nakajima. On a construction of coordinates at infinity on manifolds with fast curvature decay and maximal volume growth. Invent. Math., 97(2):313-349, 1989.
\item[] [5] D. Barlet. Développement asymptotique des fonctions obtenues par intégration sur les fibres. Invent. Math., 68(1):129-174, 1982.
\item[] [6] M. Berger, P. Gauduchon, and E. Mazet. Le spectre d'une variété Riemannienne. Lecture Notes in Mathematics. Springer, 1971.
\item[] [7] O. Biquard and Y. Rollin. Smoothing singular constant scalar curvature Kähler surfaces and minimal Lagrangians. Advances in Mathematics, 285:980-1024, 2015.
\item[] [8] R. Bott and S. S. Chern. Hermitian vector bundles and the equidistribution of the zeroes of their holomorphic sections. Acta Math., 114:71-112, 1965.
\item[] [9] X. Chen, S. Donaldson, and S. Sun. Kähler-Einstein metrics on Fano manifolds. I, II, III. J. Amer. Math. Soc., 28:183-278, 2015.
\item[] [10] S. Donaldson and S. Sun. Gromov-Hausdorff limits of Kähler manifolds and algebraic geometry. Acta Math., 213(1):63-106, 2014.
\item[] [11] S. Donaldson and S. Sun. Gromov-Hausdorff limits of Kähler manifolds and algebraic geometry, II. J. Differential Geom., 107(2):327-371, 2017.
\item[] [12] S. Gallot. A Sobolev Inequality and some Geometric Applications. In Spectra of Riemannian manifolds, pages 45-55. Kaigai Publications, 1983.
\item[] [13] D. Gilbarg and N. S. Trudinger. Elliptic Partial Differential Equations of Second Order. Springer, 2001. Reprint of the 1998 edition.
\item[] [14] D. Joyce. Compact manifolds with special holonomy. Oxford Mathematical Monographs. Oxford University Press, 2000.
\item[] [15] J. R. King. The currents defined by analytic varieties. Acta Math., 127(3-4):185-220, 1971.
\item[] [16] R. Kobayashi. Moduli of Einstein metrics on a K3 surface and Degeneration of type I. In T. Ochiai, editor, Kähler Metrics and Moduli Spaces, volume 18-II of Adv. Stud. Pure Math., pages 257-311. Academic Press, 1990.
\item[] [17] R. Kobayashi and A. Todorov. Polarized period map for generalized K3 surfaces and the moduli of Einstein metrics. Tohoku Math. J. (2), 39(3):341-363, 1987.
\end{itemize}
[18] P. B. Kronheimer. The construction of ALE spaces as hyper-Kähler quotients. J. Differential Geom., 29:665-683, 1989.
[19] P. B. Kronheimer. A Torelli-type theorem for gravitational instantons. J. Differential Geom., 29:685-697, 1989.
[20] H. Nakajima. Hausdorff convergence of Einstein 4-manifolds. J. Fac. Sci. Univ. Tokyo, 35:411-424, 1988.
[21] X. Rong and Y. Zhang. Continuity of extremal transitions and flops for Calabi-Yau manifolds. J. Differential Geom., 89(2):233-269, 2011.
[22] X. Rong and Y. Zhang. Degenerations of Ricci-flat Calabi-Yau manifolds. Commun. Contemp. Math., 15(4):1250057, 8, 2013.
[23] Y. T. Siu. Lectures on Hermitian-Einstein metrics for stable bundles and Kähler-Einstein metrics. DMV Seminar 8. Birkhäuser Verlag, Basel, 1987.
[24] P. Slodowy. Four lectures on simple groups and singularities, volume 11 of Comm. of Math. Inst. Rijksuniversiteit, Utrecht, 1980.
[25] G. Székelyhidi. An Introduction to Extremal Kähler Metrics. Graduate Studies in Mathematics. AMS, 2014.
[26] S. T. Yau. On the Ricci curvature of a compact Kähler manifold and the complex Monge-Ampère equation. Comm. Pure Appl. Math., 31:339-411, 1978.

Department of Mathematics, Kyoto University, Kyoto 606-8285. JAPAN
Email address: tazoe.itsuki.52n@st.kyoto-u.ac.jp