---
retention_scope: session
part: 3
total_parts: 3
---

[Part 3/3 of: EXISTENCE AND COMPACTNESS THEORY FOR ALE SCALAR-FLAT KÄHLER SURFACES]

In this section, we prove Corollary 1.7, Theorem 1.10, Theorem 1.11, and Corollary 1.12
6.1. Proof of Corollary 1.7. For any Kähler class $\kappa \in \mathcal{K}(J)$, let $g_{b, 1} \in \mathcal{P}(J)$ with $\left[g_{b, 1}\right]=\kappa$. Consider the family of background ALE Kähler metrics $g_{b, t}=(1-t) g_{0}+t g_{b, 1}$ for $t \in[0,1]$. We want to construct a family of ALE SFK metrics $g_{t}$ for $t \in[0,1]$, and $\left[g_{t}\right]=\left[g_{b, t}\right]$, with $g_{t}-g_{0} \in C_{\delta}^{k, \alpha}\left(g_{0}\right)$. Let $S \subset[0,1]$ be the subset where such ALE SFK metric exists. By the openness result in [HV16], $S$ is an open subset. By Theorem 1.5, $S$ is closed, so $S=[0,1]$ and the desired ALE SFK metric exists, which completes the proof.
6.2. Theorem 1.10: construction of background ALE Kähler metrics. Let $\left(X, J_{1}\right)$ be a complex surface, where $J_{1} \in \mathcal{J}_{k}^{M}(k>0)$. Our goal is to construct an ALE Kähler metric $g_{1}$ on $\left(X, J_{1}\right)$. Outside of a compact subset $K \subset X, X \backslash K$ has a universal cover $\overline{X \backslash K}$, which can be compactified analytically to an open surface $S$ by attaching a divisor $D \simeq \mathbb{P}^{1}$ to its end. By Pinkham [Pin78], the surface $\left(S, J_{1}\right)$ is a deformation of $\left(S, J_{\text {std }}\right)$ (which is a subset in $\mathbb{P}^{2}$ ), and the deformation fixes the divisor $D$. The $k$ th-order formal infinitesimal neighborhood of $D$ is defined as $\mathcal{O}_{S}^{(k)}=\mathcal{O}_{S} / \mathcal{I}^{k}$, where $\mathcal{I}$ is the ideal sheaf of $D$. By [Pin78], we know that $D$ has the same first-order infinitesimal neighborhood in $\left(S, J_{1}\right)$ and $\left(S, J_{\text {std }}\right)$, i.e., $\mathcal{O}_{S}^{(1)}$ is identical with respect to different complex structures. (Indeed, $\mathcal{O}_{S}^{(3)}$ is identical with respect to different complex structures.) The divisor $D$ is associated with a line bundle $L$ over $\left(S, J_{\text {std }}\right)$, and a line bundle $L^{\prime}$ over $\left(S, J_{1}\right)$. There exists a defining section of $D \sigma_{0} \in H^{0}\left(S, \mathcal{O}\left(L^{\prime}\right)\right)$ with $\left.\sigma_{0}\right|_{D}=0$, and smooth sections $\zeta_{1}, \zeta_{2} \in \Gamma\left(S, \mathcal{A}\left(L^{\prime}\right)\right)$, of which the restriction of $\zeta_{1}, \zeta_{2}$ on $D$ are generators of $H^{0}(D, \mathcal{O}(L))$. We can use $\left(\sigma_{0}, \zeta_{1}, \zeta_{2}\right)$ to map $S$ into $\mathbb{P}^{2}$, and denote the pull-back of the complex structure on $\mathbb{P}^{2}$ by $J_{\text {std }}$ on $S$. Since $\bar{\partial} \zeta_{j}=O\left(\left|\sigma_{0}\right|\right)$ for $j=1,2$, where $\bar{\partial}$ is with respect to $J_{1}$, this implies that
$$J_{1} \sim J_{s t d}+O\left(\left|\sigma_{0}\right|\right)$$
The functions $\frac{\zeta_{1}}{\sigma_{0}}, \frac{\zeta_{2}}{\sigma_{0}}$ are well-defined smooth functions on $S \backslash D$. We use
$$x^{1}=\operatorname{Re}\left(\frac{\zeta_{1}}{\sigma_{0}}\right), x^{2}=\operatorname{Im}\left(\frac{\zeta_{1}}{\sigma_{0}}\right), x^{3}=\operatorname{Re}\left(\frac{\zeta_{2}}{\sigma_{0}}\right), x^{4}=\operatorname{Im}\left(\frac{\zeta_{2}}{\sigma_{0}}\right)$$
as coordinate functions of $\overline{X \backslash K}$. Be aware that $\left(x^{1}+\sqrt{-1} x^{2}, x^{3}+\sqrt{-1} x^{4}\right)$ are holomorphic functions with respect to $J_{\text {std }}$. Then
$$\omega_{E u c}=\frac{\sqrt{-1}}{2} \partial_{s t d} \bar{\partial}_{s t d}\left(\left|\frac{\zeta_{1}}{\sigma_{0}}\right|^{2}+\left|\frac{\zeta_{2}}{\sigma_{0}}\right|^{2}\right)$$
defines a positive (1, 1)-form on $\left(S \backslash D, J_{\text {std }}\right)$, which is the Kähler form associated to the Euclidean metric under the coordinate $\left(x^{1}, x^{2}, x^{3}, x^{4}\right)$.

Moreover by (6.1),
$$\bar{\partial}-\bar{\partial}_{s t d}=O\left(|x|^{-1}\right)$$
Then
$$\frac{\sqrt{-1}}{2} \partial \bar{\partial}\left(\left|\frac{\zeta_{1}}{\sigma_{0}}\right|^{2}+\left|\frac{\zeta_{2}}{\sigma_{0}}\right|^{2}\right)=\omega_{E u c}+O\left(|x|^{-1}\right)$$
By taking $|x|$ sufficiently large, we can assume $\frac{\sqrt{-1}}{2} \partial \bar{\partial}\left(\left|\frac{\zeta_{1}}{\sigma_{0}}\right|^{2}+\left|\frac{\zeta_{2}}{\sigma_{0}}\right|^{2}\right)$ is positive definite, therefore a Kähler form. Averaging with the $\Gamma^{\prime}$-action, we can assume $\left|\frac{\zeta_{1}}{\sigma_{0}}\right|^{2}+\left|\frac{\zeta_{2}}{\sigma_{0}}\right|^{2}$ is $\Gamma^{\prime}$ -invariant, and can be pushed down to $X \backslash K$.

After contracting all exceptional divisors on $X$, there exists a Stein space $X^{\prime}$. Without loss of generality, assume $p \in X^{\prime}$ is the only singular point. We will also identify $X$ with $X^{\prime}$ away from the exceptional divisors and $p$. Furthermore, there exists an integer $k^{\prime}>0$, such that $L^{\prime k^{\prime}}$ can be extended to a line bundle on the analytic compactification $\hat{X}$ (which is an orbifold), $\mathcal{O}\left(L^{\prime k^{\prime}}\right)$ is globally generated, and there exists a basis $s_{0}, \ldots, s_{N} \in H^{0}\left(\hat{X}, \mathcal{O}\left(L^{\prime k^{\prime}}\right)\right)$ which embeds $X^{\prime}$ into $\mathbb{C}^{N}$. We have
$$\varphi=\left(1+\left|u^{1}\right|^{2}+\ldots+\left|u^{N}\right|^{2}\right)^{\alpha},$$
where $u^{j}=s_{j} / s_{0}, 0<\alpha<1$, and $\varphi$ is a strictly pluri-subharmonic function on $X^{\prime} \backslash p$.
Let $K^{\prime} \subset X$ be a compact subset and $K \subset K^{\prime}$. Let $\chi$ be a smooth cutoff function defined on $X$, such that $\chi=0$ on $K$, and $\chi=1$ on $X \backslash K^{\prime}$. Define the (1,1)-form $\omega_{1}^{\prime}$ as:
$$\omega_{1}^{\prime}=A \cdot \sqrt{-1} \partial \bar{\partial} \varphi+\frac{\sqrt{-1}}{2} \partial \bar{\partial}\left(\chi \cdot\left(\left|\frac{\zeta_{1}}{\sigma_{0}}\right|^{2}+\left|\frac{\zeta_{2}}{\sigma_{0}}\right|^{2}\right)\right)$$
By choosing $A$ to be sufficiently large, $\omega_{1}^{\prime}$ is positive definite on $X^{\prime} \backslash\{p\}$. By choosing $0<\alpha<1$ to be sufficiently small, $\omega_{1}^{\prime}$ is an ALE Kähler form with asymptotic rate of at least $O\left(r^{-\nu}\right)$, for any $0<\nu<1$, with respect to the coordinate:
$$\Psi: \overline{X \backslash K} \xrightarrow{\left(x^{1}, x^{2}, x^{3}, x^{4}\right)} \mathbb{R}^{4}$$
By using the gluing argument used in the proof of Lemma 2.11 locally near $p$, we can modify $\omega_{1}^{\prime}$ to be an ALE Kähler metric $\omega_{1}$ on $X$.

By [HV16, (4.7)], we have
$$J_{1}=J_{E u c}+\operatorname{Re}(\phi)+Q,$$
where $\phi \in \Gamma\left(X, \Lambda^{0,1} \otimes T^{1,0}\right)$ and satisfies the integrablity condition $\bar{\partial} \phi+[\phi, \phi]=0$, where $Q \sim \phi * \nabla \phi$ as $|\phi| \rightarrow 0$, and $\phi \sim O\left(r^{-\nu}\right)$. Noting that proof of [HV16, Lemma 5.3] remains valid under the weaker assumption that $\delta<0$, we may use a sublinear growth vector field $Y$ in that argument to assume that $\phi$ is divergence free, i.e., $\bar{\partial}^{*} \phi=0$. Then $\left(\bar{\partial}^{*} \bar{\partial}+\bar{\partial} \bar{\partial}^{*}\right) \phi=\bar{\partial}^{*}[\phi, \phi]=O\left(r^{-3+\epsilon}\right)$ for any small $\epsilon>0$. By standard elliptic estimate, we have $\phi \sim O\left(r^{-2+\epsilon}\right)$ and $J_{1}-J_{E u c} \sim O\left(r^{-\mu}\right)$. Furthermore, by formula (6.7), the asymptotic rate of $g_{1}$ can be improved to $O\left(r^{-\mu}\right),-2<-\mu<-1$. The argument above completes the proof of Theorem 1.10.

Remark 6.1. When $(X, J)$ is a Stein ALE Kähler surface, then the Kähler cone $\mathcal{K}(X, J)$ (see Definition 1.3) is isomorphic to the entire space $H^{2}(X, \mathbb{R})$. This can be shown by the following. Let $\omega_{0}$ be the fixed background Kähler form. By weighted Hodge theory, any element in $H^{2}(X, \mathbb{R})$ can be represented by a harmonic (1,1)-form $h=O\left(r^{-3}\right)$, as $r \rightarrow \infty$. Clearly, $\omega_{0}+h$ is a positive (1, 1)-form outside of a compact set. As mentioned above, the function $\varphi=\left(1+\left|u^{1}\right|^{2}+\ldots+\left|u^{N}\right|^{2}\right)^{\alpha}(0<\alpha<1)$ is a strictly pluri-subharmonic function on $X$, since $(X, J)$ is assumed to be Stein. Then there exists a constant $C>0$, such that $\omega_{h}=\omega_{0}+h+C \cdot \sqrt{-1} \partial \bar{\partial} \varphi$ is a Kähler form on $X$. We can choose $\alpha$ to be small enough, such that $\omega_{h}$ is an ALE Kähler metric of order $O\left(r^{-\mu}\right),-2<-\mu<-1$.
6.3. Smoothing of the M-resolution. In this subsection, we will construct a deformation which will be used in the proof of Theorem 6.2 below. Following the definition in Section 2.3, we have the deformation to the normal cone $\hat{\mathcal{X}}^{\prime} \subset \operatorname{Proj}(R[z]) \times \mathbb{C}$. For $t \in \Delta^{*}$, the punctured unit disc in $\mathbb{C}$, there is a simultaneous resolution of $\mathcal{X}^{\prime}, \hat{\mathcal{X}} \rightarrow \Delta^{*}$, and we identify $\hat{\mathcal{X}}_{1}$ with $\hat{X}$. Then we can apply a $\mathbb{C}^{*}$-action such that
$$\left(s_{0}, \ldots, s_{N}\right) \rightarrow\left(t^{k^{\prime}} s_{0}, s_{1}, \ldots, s_{N}\right)$$
which induces a map from $\hat{\mathcal{X}}_{t}^{\prime}$ to $\hat{X}_{1}^{\prime}$, which can be lifted to a diffeomorphism: $f_{t}: \mathcal{X}_{t} \rightarrow \mathcal{X}_{1}$, which furthermore induces a sequence of ALE Kähler metrics:
$$\left(\mathcal{X}_{t}, g_{t}, J_{t}\right)=\left(\mathcal{X}_{t},|t|^{2} \cdot f_{t}^{*} g_{1}, f_{t}^{*} J_{1}\right) .$$
Note that $\left(\mathcal{X}_{t}, J_{t}\right)$ extends to a deformation of complex structure, with central fiber isomorphic to $\mathbb{C}^{2} / \Gamma$, i.e., $\mathbb{C}^{2} / \Gamma \hookrightarrow \mathcal{Y} \rightarrow \Delta$. Without loss of generality, assume $\mathcal{Y} \rightarrow \Delta$ is in the
versal deformation of $\mathbb{C}^{2} / \Gamma$. Furthermore, as $t \rightarrow 0$, there are basepoints $x_{t} \in \mathcal{X}_{t}$ such that $\left(\mathcal{X}_{t}, g_{t}, J_{t}, x_{t}\right)$ converges to $\left(\mathbb{C}^{2} / \Gamma, g_{E u c}, J_{E u c}, 0\right)$ in the sense of pointed Cheeger-Gromov convergence with uniform ALE asymptotic rate. After a base change
![](https://cdn.mathpix.com/cropped/ec5502a0-6013-4c66-bceb-e9419fe0c6d9-37.jpg?height=181&width=220&top_left_y=424&top_left_x=952)
we have a partial-resolution $\pi: \mathcal{Z} \rightarrow \mathcal{Y}$, such that the central fiber $\mathcal{Z}_{0}$ is a $M$-resolution, and $\mathcal{Z} \rightarrow \Delta$ is a $\mathbb{Q}$-Gorenstein deformation of Type $T$ singularities.

By assumption $\mathcal{Z}_{0}$ admits an orbifold ALE SFK metric $g_{0}$, with $\pi$ as the ALE coordinate, and of ALE asymptotic rate $O\left(r^{-\mu}\right)$. Without loss of generality, assume that there is only one orbifold point in $z_{0} \in \mathcal{Z}_{0}$. By the convergence above, for each $0<t \leq 1$, there exists a diffeomorphism
$$\psi_{t}: \mathbb{C}^{2} / \Gamma \backslash B_{\eta}(0) \rightarrow \mathcal{X}_{t}$$
where $B_{\eta}(0)$ is with respect to the Euclidean distance, such that $\psi_{t}^{*} g_{t}$ converges to $g_{E u c}$ under $C_{-\mu}^{k, \alpha}\left(\mathbb{C}^{2} / \Gamma \backslash B_{\eta}(0), g_{E u c}\right)$-norm for any integer $k>0$, and $0<\alpha<1$. Let $U_{\eta}=\pi^{-1}\left(B_{\eta}(0)\right) \subset$ $\mathcal{Z}_{0}$ be the lifting of the unit ball of $\mathbb{C}^{2} / \Gamma$. Then the map $\psi_{t}$ can be lifted to a map
$$\tilde{\psi}_{t}: \mathcal{Z}_{0} \backslash U_{\eta} \rightarrow \mathcal{X}_{t}$$
We can assume that $U_{\eta}$ is contained in the unit geodesic ball $B_{1}\left(z_{0}, g_{0}\right)$ in $\mathcal{Z}_{0}$. We have
$$\left\|\tilde{\psi}_{t}^{*} J_{t}-\tilde{J}_{0}\right\|_{C_{-\mu}^{k, \alpha}\left(g_{0}\right)} \sim O\left(|t|^{d}\right)$$
where the norm is taken on the domain on $\mathcal{Z}_{0} \backslash B_{1}\left(z_{0}\right)$ as $|t| \rightarrow 0$. This is because, the family $\mathcal{Y} \rightarrow \Delta$ is a deformation of ALE Kähler metrics. By a standard argument (normalizing each annulus $A_{2^{k}, 2^{k+1}}\left(z_{0}\right)$ to unit size), it is not hard to see that along this deformation, away from the singularity, the complex structure has a convergence rate of $O\left(|t|^{d} \cdot r^{-\mu}\right)$. The power $d$ comes from the base change. Exactly as is [BR15, Lemma 15], the estimate (6.15) will be needed below to control the perturbation of the Kähler form and complex structure. Moreover, since our base space is non-compact, we also need to control the asymptotic behavior as $r \rightarrow \infty$.
6.4. Smoothing of ALE SFK orbifold metrics. In [BR15], Biquard-Rollin use a gluing method to construct the smoothing of a CscK orbifold along a one-parameter non-degenerate $\mathbb{Q}$-Gorenstein deformation. We will adapt their proof under the ALE setting, which will produce a family of ALE SFK metrics that degenerate to an orbifold metric at the central fiber.

Theorem 6.2. Let $\mathcal{Z} \rightarrow \Delta$ be the $\mathbb{Q}$-Gorenstein deformation from above, where the central fiber $\mathcal{Z}_{0}$ a $M$-resolution (or a $P$-resolution), and $p \in \mathcal{Z}_{0}$ is the only singularity in $\mathcal{Z}_{0}$, which is of type $T_{0}$ (of type $T$ ). Assume there exists an ALE SFK orbifold metric ( $\mathcal{Z}_{0}, J_{0}, g_{0}$ ). Then along this deformation, there exists a smooth family of ALE SFK metrics $\left(\mathcal{Z}_{t}, J_{t}, g_{t}\right)$ of order $O\left(r^{-\mu}\right)$ that degenerates to the orbifold metric $\left(\mathcal{Z}_{0}, J_{0}, g_{0}\right)$ as $t \rightarrow 0$.

Proof. Without loss of generality, assume that $t$ real, and let $\epsilon(t)=t^{\frac{d}{2}}$. Denote $\left(A_{s}, g_{A_{s}}\right)$ as a $\mathbb{Z}_{n}$-quotient of a $A_{n-1}$-type gravitational instanton $\left(\bar{A}_{s}, g_{\bar{A}_{s}}\right)$ that associated to the type
$T_{0}$ singularity $\{p\} \in B$ of the form $\frac{1}{n^{2}}(1, n a-1)$. For the family of gravitational instantons $\left(\bar{A}_{s}, g_{\bar{A}_{s}}\right)$, Kronheimer's construction gives the expansion
$$F_{\epsilon(s)}^{*} g_{\bar{A}_{s}}=g_{E u c}+\xi(s)$$
where $\xi(s)=O\left(s^{2} \cdot R^{-4}\right)$, and $F$ is a diffeomorphism from $\bar{A}_{s}$ to the minimal resolution of $\mathbb{C}^{2} / \frac{1}{n}(1, n-1)$ (see more details in [Kro89] and [BR15, Section 2]). In the current setting, $s=t^{d}$. The $C_{-\mu}^{k, \alpha}\left(A_{t}, g_{A_{t}}\right)$-norm is defined as in Definition 2.1 for the weighted Hölder norm on ALE manifolds. Let $U \subset \mathcal{Z}_{0}$ be an open neighborhood of $p$, which is isomorphic to an open neighborhood of $\{0\} \in \mathbb{C}^{2} / \frac{1}{n^{2}}(1, n a-1)$. Let $r \in C^{0}\left(\mathcal{Z}_{0}\right) \cap C^{\infty}\left(\mathcal{Z}_{0} \backslash\{p\}\right)$ be a function such that $r(p)$ is the Euclidean distance to $p$ in $U$ and coincides with the radius of the ALE metric $g_{0}$ outside of a compact subset. Define the weighted Hölder norm $C_{-\mu}^{k, \alpha}\left(\mathcal{Z}_{0}, g_{0}\right)$ as in Definition 2.1, where $r$ is defined as above. For any $u \in C_{-\mu}^{k, \alpha}\left(\mathcal{Z}_{0}, g_{0}\right)$, when $r \rightarrow 0$ or $r \rightarrow \infty$, $u=O\left(r^{-\mu}\right)$. We can define $C_{-\mu}^{k, \alpha}\left(\mathcal{Z}_{t}, g_{t}\right)$ in a similar way.

Define the gluing scale $b(t)=\epsilon(t)^{\beta}$, where $\beta=\frac{2}{2+\mu},-2<-\mu<-1$ is the ALE asymptotic rate of the metric constructed such that $\beta$ is close to $\frac{1}{2}$. Let $\chi: \mathbb{R}^{+} \rightarrow \mathbb{R}^{+}$be a smooth nondecreasing function
$$\chi(t)= \begin{cases}0 & t<1 / 2 \\ 1 & t \geq 1\end{cases}$$
Let $H_{\epsilon^{-1}}$ be the homothety that identifies $b \leq r \leq 4 b$ in $\mathcal{Z}_{t}$ with $\frac{b}{\epsilon} \leq R \leq \frac{4 b}{\epsilon}$ in $A_{t}$. Attach $A_{t}$ and $\mathcal{Z}_{t}$ together by $H_{\epsilon^{-1}}$ to obtain a manifold $\mathcal{X}_{t}$, which is diffeomorphic to $\mathcal{Z}_{t}$. Define a Riemannian metric on $\mathcal{X}_{t}$
$$\tilde{h}_{t}= \begin{cases}\epsilon^{2} \cdot H_{\epsilon^{-1}}^{*}\left(g_{E u c}+\epsilon^{-2} \xi\left(\epsilon^{2}\right)\right) & r \leq b \\ g_{t} & r \geq 4 b \\ \epsilon^{2} \cdot H_{\epsilon^{-1}}^{*}\left(g_{E u c}+\left(1-\chi\left(\frac{\epsilon}{b} R-1\right)\right) \epsilon^{-2} \xi\left(\epsilon^{2}\right)\right) & b \leq r \leq 2 b .\end{cases}$$
Define the Hermitian metric $h_{t}=\frac{1}{2}\left(\tilde{h}_{t}+\tilde{h}_{t}\left(J_{t} \cdot, J_{t} \cdot\right)\right)$. Note that as $\epsilon \rightarrow 0$, the limit of $g_{E u c}+\epsilon^{-2} \xi\left(\epsilon^{2}\right)$ is called the tangent graviton to the deformation in [BR15]. The weighted Hölder norm $C_{-\mu}^{k, \alpha}\left(\mathcal{X}_{t}, h_{t}\right)$ can be defined by using $\chi$ to separate a function on $\mathcal{X}_{t}$ into functions supported separately on $A_{t}$ and $\mathcal{Z}_{t}$, and adding the corresponding norms together. See more details in [BR15, Section 3.3.3]. Denote $\bar{\omega}_{t}$ as the (1, 1)-form corresponding to the Hermitian metric $h_{t}$. By the same calculation as done in [BR15, Section 3.4], when $\beta$ is close to $\frac{1}{2}$, using (6.15), it follows that
$$\begin{aligned}
\left\|d \bar{\omega}_{t}\right\|_{C_{-\mu}^{k, \alpha}\left(\mathcal{X}_{t}, h_{t}\right)} & \leq C_{k} \cdot \epsilon^{2} \\
\left\|\nabla^{L C} J_{t}\right\|_{C_{-\mu-1}^{k, \alpha}}\left(\mathcal{X}_{t}, h_{t}\right) & \leq C_{k} \cdot \epsilon^{2} .
\end{aligned}$$
We next employ these estimates to perturb $h_{t}$ into to a Kähler metric. As in [BR15, Section 3.5], there is a map of spaces of harmonic (1, 1)-forms
$$H_{A_{t}}^{1,1} \oplus H_{\mathcal{Z}_{0}}^{1,1} \rightarrow K_{t}^{1,1},$$
where elements in $K_{t}^{1,1}$ are very close to harmonic elements in $H^{1,1}\left(\mathcal{X}_{t}\right)$. This implies an $L^{2}$ - "almost orthogonal" decomposition for 2-forms on $\mathcal{X}_{t}$. The $\bar{\partial}_{t}$-Laplacian $\square_{t}=\bar{\partial}_{t} \bar{\partial}_{t}^{*}+\bar{\partial}_{t}^{*} \bar{\partial}_{t}$ is defined by using the background hermitian form $\bar{\omega}_{t}$, which is a Fredholm operator with respect to the $C_{-\mu}^{k, \alpha}$-norm. Then $H^{1,1}\left(\mathcal{X}_{t}\right)$ is represented by $\bar{\partial}_{t}$-harmonic forms in $\mathcal{H}_{-\mu}\left(\mathcal{X}_{t}, \Lambda^{1,1}\right)$.

Since $\mathcal{X}_{t}$ is Kähler outside of a compact subset, by a similar proof as in [HV16, Proposition 3.5], $\mathcal{H}_{-\mu}\left(\mathcal{X}_{t}, \Lambda^{1,1}\right) \simeq \mathcal{H}_{-3}\left(\mathcal{X}_{t}, \Lambda^{1,1}\right)$, so that the $L^{2}$-orthogonal decomposition still makes sense under the ALE setting.

By the perturbation argument in [BR15, Section 3.5], there exists a (1, 1)-form $\gamma_{t}$ which is "almost orthogonal" to $K_{t}^{1,1}$, such that $\bar{\omega}_{t}-\gamma_{t}$ is $\square_{t}$-closed, and
$$\left\|\gamma_{t}\right\|_{C_{-\mu}^{k+2, \alpha}\left(\mathcal{X}_{t}\right)} \leq C_{k} \cdot\left\|\square_{t} \bar{\omega}_{t}\right\|_{C_{-\mu-2}^{k, \alpha}\left(\mathcal{X}_{t}\right)} .$$
Exactly as in [BR15, Lemma 26], $\bar{\omega}_{t}-\gamma_{t}$ can then be perturbed to a $d$-closed (1, 1)-form, whose real part $\omega_{t^{\prime}}$, is a Kähler form. The adaptation of Biquard-Rollin's argument to the ALE case is entirely analogous to [HV16, Section 7].

By an implicit function type argument as in [BR15, Section 4] adapted to the ALE case in [HV16, Section 8], we can solve the equation $R\left(\omega_{t}\right)=0(t>0)$ where each $\omega_{t}$ is a small perturbation of $\omega_{t}^{\prime}$. It should be emphasized here that, in the compact case, there is an obstruction to the smoothing of a CscK orbifold which is given by holomorphic vector fields on $\mathcal{X}_{t}$ for $t>0$ small. However, under the ALE setting, the scalar curvature defines a 4th-order nonlinear PDE
$$\begin{aligned}
R: C_{a}^{k, \alpha}\left(\mathcal{X}_{t}\right) & \rightarrow C_{a-4}^{k-4, \alpha}\left(\mathcal{X}_{t}\right) \\
\varphi & \rightarrow R\left(\omega_{b, t}+\sqrt{-1} \partial \bar{\partial} \varphi\right)
\end{aligned}$$
where $0<a, \alpha<1, k \geq 4, t>0$ is sufficiently small. The cokernel of the linearization of $R$ corresponds to the space of decaying holomorphic vector fields on $\mathcal{X}_{t}$, which is trivial as proved in [HV16, Proposition 3.3]. As a result, there is no obstruction in the ALE case. We have therefore obtained a family of ALE SFK metrics $\omega_{t}$, which, by construction, degenerate to the original ALE SFK orbifold metric on the $M$-resolution as $t \rightarrow 0$. \(\square\)

Remark 6.3. In case of a $P$-resolution, for Theorem 6.2, we require the direction of the deformation $\mathcal{Z} \rightarrow \Delta_{\mathbb{R}}$ to be away from the discriminant locus (the subset of $\mathcal{J}_{k}^{P}$ where the Weyl group does not act freely.) See more details in [BR15].
6.5. Completion of proof of Theorem 1.11. For the proof of (a), over the Artin component $\mathcal{J}_{0}$, an initial ALE SFK metric $\left(X, J_{0}, g_{0}\right)$ on the minimal resolution of $\mathbb{C}^{2} / \Gamma$ can be constructed by using [CS04] in the cyclic case, and [LV19] in the general case. By [HV16, Theorem 1.4], there exists an open neighborhood of $J_{0}$ in $\mathcal{J}_{0}$, such that for any complex structure $J$ in this open neighborhood, there exists an ALE SFK metric on $(X, J)$. We then apply the $\mathbb{C}^{*}$-action on $\mathcal{J}_{0}$. As in (6.11), by the pull-back under the $\mathbb{C}^{*}$-action, and a rescaling of metrics such that the ALE coordinate is fixed, we can construct an ALE SFK metric in $\mathcal{K}(J)$ for any $J$ in $\mathcal{J}_{0}$.

For the proof of (b), take $J \in \mathcal{J}_{k}^{M}$. By the assumption of (b), there exists an ALE SFK orbifold metric on the associated $M$-resolution $Z_{k}^{M}$. Then there exists an open neighborhood $U \subset \mathcal{J}_{k}^{M}$ of $\mathcal{Z}_{0}$, such that for any complex structure $J \in U \backslash\{0\}$, there exists a ALE SFK metric on $(X, J)$, by applying Theorem 6.2. By the pull-back of the $\mathbb{C}^{*}$-action, and a rescaling of metrics to fix the ALE coordinate, we can also construct a ALE SFK metric for some Kähler class in $\mathcal{K}(J)$, for all $J \in \mathcal{J}_{k}^{M} \backslash\{0\}$.

For the proof of (c), denote $\mathcal{J}_{k}^{P^{\prime}} \subset \mathcal{J}_{k}^{P}$ as the subset away from the discriminant locus, with $\mathcal{J}_{k}^{P^{\prime}}$ is open and dense in $\mathcal{J}_{k}^{P}$. Following exactly Case (b), we can construct an ALE SFK metric for some Kähler class in $\mathcal{K}(J)$, for all $J \in \mathcal{J}_{k}^{P^{\prime}}$.
6.6. Proof of Corollary 1.12. The Artin component follows from Case (a) in Theorem 1.11. Next, assume $J \in \mathcal{J}_{k}^{M}$ with $k>0$. We can obtain an ALE SFK orbifold metric on the corresponding $M$-resolution $X_{0}$ using the Calderbank-Singer construction. To see this, notice that the $M$-resolution of $\mathbb{C}^{2} / \Gamma$ is toric. Let $\pi: \widetilde{X_{0}} \rightarrow X_{0}$ be its minimal resolution. In the corresponding moment polygon of $\widetilde{X_{0}}$, each segment in the boundary represents an exceptional divisor in $\widetilde{X_{0}}$. By using Joyce's construction as done in [CS04], there exists a family of ALE SFK metrics on $\widetilde{X_{0}}$, which is parameterized by lengths of boundary segments. By decreasing the lengths of segments that correspond to the exceptional divisors contracted by $\pi$ to 0, the Gromov-Hausdorff limit will be the desired ALE SFK orbifold metric on $X_{0}$. Equivalently, these orbifolds can be directly constructed by choosing the lengths of the corresponding boundary segments to be exactly zero, in which case the Calderbank-Singer metrics are ALE SFK metrics with orbifold singularities. Corollary 1.12 is then a consequence of this observation and Case (b) in Theorem 1.11.

\section*{7. Examples}

In this section, we give the details of the examples in Subsection 1.2 from the Introduction. Namely, we prove Theorems 1.13 and 1.16. First we recall some important details of cyclic quotient singularities.
7.1. Cyclic quotient singularities. Let $1 \leq q<p$ be relatively prime integers. For a type $\frac{1}{p}(1, q)$-action, let $\widetilde{X}$ be the minimal resolution of $\mathbb{C}^{2} / \Gamma(q, p)$. Integers $k$ and $e_{i}, i=1 \ldots k$, are defined by the following Hirzebruch-Jung modified Euclidean algorithm:
$$p=e_{1} q-a_{1}, q=e_{2} a_{1}-a_{2}, \ldots, a_{k-3}=e_{k-1} a_{k-2}-1, a_{k-2}=e_{k} a_{k-1}=e_{k},$$
where the numbers $e_{i} \geq 2$ and $0 \leq a_{i}<a_{i-1}, i=1 \ldots k$, see [Hir53]. The integer $k$ is called the length of the modified Euclidean algorithm. This can also be written as the continued fraction expansion
$$\frac{q}{p}=\frac{1}{e_{1}-\frac{1}{e_{2}-\cdots \frac{1}{e_{k}}}} \equiv\left[e_{1}, e_{2}, \ldots, e_{k}\right] .$$

Recall that exceptional divsor in $\widetilde{X}$ is a string of rational curves, $E_{i}$ for $i=1 \ldots k$ with $E_{i} \cdot E_{i}=-e_{i}$, and each curve has intersection +1 with the adjacent curve, where it has a simple normal crossing singularity. This is represented by the following graph.
$$-e_{1} \quad-e_{2} \quad-------\stackrel{\longrightarrow}{-}$$
which we will also denote as $\left(e_{1}, \ldots, e_{k}\right)$. For details on cyclic quotient singularities see [Rie74].

For $\Gamma=\frac{1}{p}(1, q)$, the following formula is proved in [AI08, LV15]
$$\eta\left(S^{3} / \Gamma\right)=\frac{1}{3}\left(\sum_{i=1}^{k} e_{i}+\frac{q^{-1 ; p}+q}{p}\right)-k,$$
where the $e_{i}$ and $k$ are as defined in (7.1), and $q^{-1 ; p}$ denotes the inverse of $q \bmod p$.
7.2. Artin component examples. In these cases, we will next discuss the topological condition $\mathcal{C}(X)>0$. First, we consider the case that $\Gamma \subset \operatorname{SU}(2)$, and $X$ is diffeomorphic to the minimal resolution of $\mathbb{C}^{2} / \Gamma$. In this case, we have equality in Nakajima's Hitchin-Thorpe inequality [Nak90], so we have
$$2 \chi(X)+3 \tau(X)=\frac{2}{|\Gamma|}+3 \eta\left(S^{3} / \Gamma\right) .$$
The left hand side is equal to $2-b_{2}(X)$, so we obtain
$$\mathcal{C}(X)=\frac{4}{|\Gamma|}>0 .$$

Next, consider the cases in Theorem 1.13. For the Artin component, if $\Gamma$ is cyclic it follows from (7.3) that
$$\mathcal{C}(X)=2-b_{2}(X)+\frac{2}{p}-3 \eta\left(\frac{1}{p}(1, q)\right)=2-\sum_{i=1}^{k}\left(e_{i}-2\right)+\frac{2-q^{-1 ; p}-q}{p} .$$

For $\Gamma=\frac{1}{3}(1,1)$, we have $p=3, q=1, e_{1}=3, k=1,1^{-1 ; 3}=1$. If $X$ is in the Artin component of $\Gamma$, then (7.6) yields $\mathcal{C}(X)=1>0$.

For $\Gamma=\frac{1}{5}(1,2)$, the dual graph is (3, 2), and we have $p=5, q=2, k=2,2^{-1 ; 5}=3$. If $X$ is in the Artin component of $\Gamma$, then (7.6) yields $\mathcal{C}(X)=\frac{2}{5}>0$.

For $\Gamma=\frac{1}{7}(1,3)$, the dual graph is (3, 2, 2), and we have $p=7, q=3, k=3,3^{-1 ; 7}=5$. If $X$ is in the Artin component of $\Gamma$, then (7.6) yields $\mathcal{C}(X)=\frac{1}{7}>0$.

Below, we will consider various non-Artin components of cyclic quotient singularities. For these, we will have $b_{2}(X)<k$. The modification to the formula for $\mathcal{C}(X)$ is simply the following
$$\mathcal{C}(X)=2+\left(k-b_{2}(X)\right)-\sum_{i=1}^{k}\left(e_{i}-2\right)+\frac{2-q^{-1 ; p}-q}{p} .$$
7.3. Type T cyclic quotient singularities. We recall the main definition from [KSB88].

Definition 7.1. If $\Gamma=\frac{1}{r^{2} s}(1, r s d-1)$ where $r \geq 2, s \geq 1,(r, d)=1$, then $\Gamma$ is said to be of type $T_{s-1}$.

We will also denote this action by $T(r, s, d)$. For type $T$ singularities, there exists non-Artin component such that the corresponding space $X$ satisfies $b_{2}(X)=s-1$. Note that this group is covered by the group $\tilde{\Gamma}=\frac{1}{r s}(1, r s-1)$, quotiented by a $\mathbb{Z}_{r}$-action. The spaces $X$ in the non-Artin component admit Ricci-flat metrics which are isometric quotients of an $A_{r s-1}$ hyperkähler metric [Suv12, Wri12]. We also note that the embedding dimension is $r+3$, and the base of the non-Artin component has dimension $s$ [KSB88, BC94]. The following Proposition gives a useful description of the type T singularity in terms of their dual graphs.

Proposition 7.2. If $\left(e_{1}, \ldots, e_{k}\right)$ is of type $T_{s-1}$, then the graphs $\left(2, e_{1}, e_{2}, \ldots, e_{k-1}, e_{k}+1\right)$ and $\left(e_{1}+1, e_{2}, \ldots, e_{k-1}, e_{k}, 2\right)$. are also of Type $T_{s-1}$. Type $T_{0}$ are those obtained starting from (-4). Type $T_{1}$ are those obtained starting from (3, 3). In general, for $s>2$, type $T_{s-1}$ are those obtained starting from $(3, \underbrace{2, \ldots, 2}_{s-2})$ and iterating the above procedure $(r-2)$ times.

Using this characterization, we can prove the following.
Proposition 7.3. Let $\Gamma$ be of type $T(r, s, d), \ell$ denote the total number of exceptional curves in the minimal resolution of $\mathbb{C}^{2} / \Gamma$, and $-e_{i}$ denote the self-intersection number of the $i$ th curve, $i=1 \ldots l$. Then
$$\begin{aligned}
\ell & =r+s-2 \\
\sum_{i=1}^{\ell} e_{i} & =3 r+2 s-4
\end{aligned}$$
Furthermore, we have
$$\begin{aligned}
\eta(\Gamma) & =\frac{1}{3}\left(3-s-\frac{2}{r^{2} s}\right) \\
\mathcal{C}(X) & =\frac{4}{r^{2} s}
\end{aligned}$$
Proof. The first two formulas follow easily from the description in Proposition 7.2. Without loss of generality, assume that $1 \leq d \leq r-1$. Then the inverse of $r s d-1$ modulo $r^{2} s$ is given by $r s(r-d)-1$. To see this,
$$(r s d-1)(r s(r-d)-1)-1=-r^{2} s\left(1+d^{2} s-r s d\right) \equiv 0 \bmod r^{2} s .$$
Therefore, letting $p=r^{2} s$, and $q=r s d-1$, and using (7.3), we have
$$\eta(\Gamma)=\frac{1}{3}\left(\sum_{i=1}^{\ell} e_{i}+\frac{q^{-1 ; p}+q}{p}\right)-k=\frac{1}{3}\left(3-s-\frac{2}{r^{2} s}\right) .$$
Finally, by (7.7), we have
$$\mathcal{C}(X)=2-(s-1)+\frac{2}{r^{2} s}-\left(3-s-\frac{2}{r^{2} s}\right)=\frac{4}{r^{2} s} .$$ \(\square\)

Remark 7.4. Note that $\mathcal{C}(X)=\frac{4}{|\Gamma|}$, something that we already knew had to be true from the Nakajima-Hitchin-Thorpe inequality, similarly to (7.5).

Remark 7.5. Without loss of generality, we can assume that $1 \leq d \leq r-1$. We showed above that
$$\frac{1}{r^{2} s}(1, r s d-1) \sim \frac{1}{r^{2} s}(1, r s(r-d)-1) .$$
This means that $T(r, s, d) \sim T(r, s, r-d)$ are equivalent singularities, but note that the ordering of the self-intersection numbers $e_{i}$ is reversed in each case.
7.4. Add a single (-2)-curve to a type $T$. Given $\left(e_{1}, \ldots, e_{k}\right)$ of Type $T_{s-1}$, we consider the graph $\left(2, e_{1}, \ldots, e_{k}\right)$. Note that, we could also put the (-2) curve on the right hand side. However, this would give an equivalent singularity taking the conjugate Type $T$ singularity (from Remark 7.5), which reverses the order of the self-intersection numbers, and still putting the (-2) curve on the left. So let us write the type $T$ string as $T(r, s, r-d)$, and attach the (-2) curve on the left. For this type $T$ singularity, we have
$$\frac{r s(r-d)-1}{r^{2} s}=\left[e_{1}, \ldots, e_{k}\right] .$$

So to determine what the new cyclic singularity is, we have
$$\frac{q}{p}=\left[2, e_{1}, \ldots, e_{k}\right]=\frac{1}{2-\frac{r s(r-d)-1}{r^{2} s}}=\frac{r^{2} s}{1+d r s+r^{2} s} .$$
So this singularity is of type $\frac{1}{1+d r s+r^{2} s}\left(1, r^{2} s\right)$.
Proposition 7.6. We have
$$\begin{aligned}
q^{-1 ; p} & =d s r+d^{2} s-1 \\
\eta\left(\frac{1}{p}(1, q)\right) & =\frac{1}{3} \frac{s\left(-1+d^{2}+2 d r+2 r^{2}-r(d+r) s\right.}{1+d r s+r^{2} s} .
\end{aligned}$$
Proof. A simple computation shows that
$$r^{2} s\left(d s r+d^{2} s-1\right)-1=(-1+d r s)\left(1+d r s+r^{2} s\right) .$$
Note also that $1 \leq d s r+d^{2} s-1<r^{2} s+d r s+1$.
Next, using Proposition 7.3 we have
$$\begin{aligned}
\eta(\Gamma) & =\frac{1}{3}\left(3 r+2 s-4+\tilde{2}+\frac{r^{2} s+d s r+d^{2} s-1}{1+d r s+r^{2} s}\right)-(r+s-2+\tilde{1}) \\
& =\frac{1}{3} \frac{s\left(-1+d^{2}+2 d r+2 r^{2}-r(d+r) s\right.}{1+d r s+r^{2} s} .
\end{aligned}$$
Note that the $\tilde{2}$ and $\tilde{1}$ terms are there because we added a single (-2) curve. \(\square\)

Next, we will blow-down the Type $T$ singularity, and let $X$ denote the corresponding $\mathbb{Q}$-Gorenstein smoothing, which exists by [BC94, KSB88].

Proposition 7.7. We have
$$\mathcal{C}(X)=\frac{4-d^{2} s}{1+d r s+r^{2} s} .$$
Proof. The $\eta$-invariant was determined in the previous proposition, since the group at infinity is the same. Note also that $b_{2}(X)=s-1+1=s$, since the smoothing of the type $T$ singularity contributes $s-1$ and the (-2) curves donates another 1 to this. We then have
$$\mathcal{C}(X)=2-s+\frac{2}{1+d r s+r^{2} s}-\frac{s\left(-1+d^{2}+2 d r+2 r^{2}-r(d+r) s\right.}{1+d r s+r^{2} s}=\frac{4-d^{2} s}{1+d r s+r^{2} s} .$$ \(\square\)

Clearly, for this to be positive, we require $d=1$, in which case we have
$$\mathcal{C}(X)=\frac{4-s}{1+r s+r^{2} s},$$
which is positive for $s=1,2,3$. Note that from Proposition 7.6, the group at infinity is equivalent to
$$\Gamma=\frac{1}{1+r s+r^{2} s}(1, s(r+1)-1),$$
which yields the following.

Theorem 7.8. Let $\Gamma \subset \mathrm{U}(2)$ be any of the following groups for $r \geq 2$
$$\begin{aligned}
& \Gamma=\frac{1}{r^{2}+r+1}(1, r) \\
& \Gamma=\frac{1}{2 r^{2}+2 r+1}(1,2 r+1) \\
& \Gamma=\frac{1}{3 r^{2}+3 r+1}(1,3 r+2) .
\end{aligned}$$
There is a non-Artin component $\mathcal{J}_{i}$ of the versal deformation space $\mathbb{C}^{2} / \Gamma$ with $b_{2}=i$ in Case $(i), i=1,2,3$ which has $\mathcal{C}\left(\mathcal{J}_{i}\right)>0$.

Note the first case is a $M$-resolution, but the second and third cases are $P$-resolutions, but not $M$-resolutions. The dual graphs of the minimal resolutions in these cases look like the following.

For $s=1, r \geq 2:(\overbrace{2, \ldots, 2}^{r-1}, r+2)$.
For $s=2, r \geq 2:(\overbrace{2, \ldots, 2}^{r-1}, 3, r+1)$.
For $s=3, r \geq 2:(\overbrace{2, \ldots, 2}^{r-1}, 3,2, r+1)$.
7.5. Add two (-2)-curves to a type $T$. We will write the type $T$ string as $T(r, s, r-d)$, with dual graph $\left(e_{1}, \ldots, e_{k}\right)$, and attach the two (-2) curves on the left. To determine $p$ and $q$, we have
$$\frac{q}{p}=\left[2,2, e_{1}, \ldots, e_{k}\right]=\frac{1}{2-\frac{1}{2-\frac{r s(r-d)-1}{r^{2} s}}}=\frac{1+d r s+r^{2} s}{2+2 d r s+r^{2} s} .$$
So this singularity is of type $\frac{1}{2+2 d r s+r^{2} s}\left(1,1+d r s+r^{2} s\right)$.
Proposition 7.9. We have
$$\begin{aligned}
q^{-1 ; p} & =d s r+2 d^{2} s-1 \\
\eta\left(\frac{1}{p}(1, q)\right) & =\frac{1}{3} \frac{s\left(-2+2 d^{2}+2 d r+r^{2}-r(2 d+r) s\right)}{2+2 d r s+r^{2} s} .
\end{aligned}$$
Proof. A simple computation shows that
$$\left(1+d r s+r^{2} s\right)\left(d s r+2 d^{2} s-1\right)-1=\left(-1+d^{2} s+d r s\right)\left(2+2 d r s+r^{2} s\right) .$$
Note also that $1 \leq d s r+2 d^{2} s-1<r^{2} s+2 d r s+2$.
Next, using Proposition 7.3, we have
$$\begin{aligned}
\eta(\Gamma) & =\frac{1}{3}\left(3 r+2 s-4+\tilde{4}+\frac{r^{2} s+d r s+1+d r s+2 d^{2} s-1}{2+2 d r s+r^{2} s}\right)-(r+s-2+\tilde{2}) \\
& =\frac{1}{3} \frac{s\left(-2+2 d^{2}+2 d r+r^{2}-r(2 d+r) s\right)}{2+2 d r s+r^{2} s} .
\end{aligned}$$
Note that the $\tilde{4}$ and $\tilde{2}$ terms are there because we added a two (-2) curves. \(\square\)

Next, we will blow-down the Type $T$ singularity, and let $X$ denote the corresponding $\mathbb{Q}$-Gorenstein smoothing, which exists by [BC94, KSB88].

Proposition 7.10. We have
$$\mathcal{C}(X)=\frac{4-2 d^{2} s}{2+2 d r s+r^{2} s} .$$
Proof. The $\eta$-invariant was determined in Proposition 7.9, since the group at infinity is the same. Also, $b_{2}(X)=s-1+2=s+1$, since the smoothing of the type $T$ singularity contributes $s-1$ and the (-2) curves donate another 2 to this. Then
$$\begin{aligned}
\mathcal{C}(X) & =2-(s+1)+\frac{2}{2+2 d r s+r^{2} s}-\frac{s\left(-2+2 d^{2}+2 d r+r^{2}-r(2 d+r) s\right)}{2+2 d r s+r^{2} s} \\
& =\frac{4-2 d^{2} s}{2+2 d r s+r^{2} s} .
\end{aligned}$$ \(\square\)

Clearly, for this to be positive, we require $d=1$, in which case we have
$$\mathcal{C}(X)=\frac{4-2 s}{2+2 r s+r^{2} s},$$
which is only positive for $s=1$. Also, by Proposition 7.9, the group at infinity is
$$\Gamma=\frac{1}{2+2 r+r^{2} s}(1, r+1),$$
which yields the following.
Theorem 7.11. Let $\Gamma \subset \mathrm{U}(2)$ be any of the following groups for $r \geq 2$
$$\Gamma=\frac{1}{r^{2}+2 r+2}(1, r+1) .$$
Then there is a non-Artin component $\mathcal{J}_{k}$ of the versal deformation space $\mathbb{C}^{2} / \Gamma$ with $b_{2}=2$ which has $\mathcal{C}\left(\mathcal{J}_{k}\right)>0$.

The dual graph of the minimal resolution of the $M$-resolution in these cases looks like the following.

For $r \geq 2:(\overbrace{2, \ldots, 2}^{r}, r+2)$.
7.6. Add three (-2)-curves to a type $T$. We write the type $T$ string as $T(r, s, r-d)$, with dual graph $\left(e_{1}, \ldots, e_{k}\right)$, and attach the three (-2) curves on the left. To determine $p$ and $q$ we have
$$\frac{q}{p}=\left[2,2,2, e_{1}, \ldots, e_{k}\right]=\frac{1}{2-\frac{1}{2-\frac{1}{2-\frac{r s(r-d)-1}{r^{2} s}}}}=\frac{2+2 d r s+r^{2} s}{3+3 d r s+r^{2} s} .$$
So this singularity is of type $\frac{1}{3+3 d r s+r^{2} s}\left(1,2+2 d r s+r^{2} s\right)$.

Proposition 7.12. We have
$$\begin{aligned}
q^{-1 ; p} & =d s r+3 d^{2} s-1 \\
\eta\left(\frac{1}{p}(1, q)\right) & =\frac{1}{3} \frac{-2-s\left(3-3 d^{2}+r(3 d+r) s\right)}{3+3 d r s+r^{2} s} .
\end{aligned}$$
Proof. A simple computation shows that
$$\left(2+2 d r s+r^{2} s\right)\left(d s r+3 d^{2} s-1\right)-1=\left(-1+2 d^{2} s+d r s\right)\left(3+3 d r s+r^{2} s\right) .$$
Note also that $1 \leq d s r+3 d^{2} s-1<r^{2} s+3 d r s+3$.
Next, using Proposition 7.3, we have
$$\begin{aligned}
\eta(\Gamma) & =\frac{1}{3}\left(3 r+2 s-4+\tilde{6}+\frac{2+2 d r s+r^{2} s+d s r+3 d^{2} s-1}{3+3 d r s+r^{2} s}\right)-(r+s-2+\tilde{3}) \\
& =\frac{1}{3} \frac{-2-s\left(3-3 d^{2}+r(3 d+r) s\right)}{3+3 d r s+r^{2} s} .
\end{aligned}$$
Note that the $\tilde{6}$ and $\tilde{3}$ terms are there because we added a three $(-2)$ curves. \(\square\)

Next, we will blow-down the Type $T$ singularity, and let $X$ denote the corresponding $\mathbb{Q}$-Gorenstein smoothing, which exists by [BC94, KSB88].

Proposition 7.13. We have
$$\mathcal{C}(X)=\frac{4-2 d^{2} s}{2+2 d r s+r^{2} s} .$$
Proof. The $\eta$-invariant term was determined in Proposition 7.12, since the group at infinity is the same. Also, $b_{2}(X)=s-1+3=s+2$, since the smoothing of the type $T$ singularity contributes $s-1$ and the (-2) curves donate another 3 to this. Then
$$\begin{aligned}
\mathcal{C}(X) & =2-(s+2)+\frac{2}{3+3 d r s+r^{2} s}-\frac{-2-s\left(3-3 d^{2}+r(3 d+r) s\right)}{3+3 d r s+r^{2} s} \\
& =\frac{4-3 d^{2} s}{3+3 d r s+r^{2} s}
\end{aligned}$$ \(\square\)

Clearly, for this to be positive, we require $d=1$, in which case we have
$$\mathcal{C}(X)=\frac{4-3 s}{3+3 r s+r^{2} s},$$
which is only positive for $s=1$. By Proposition 7.12, the group at infinity is equivalent to
$$\Gamma=\frac{1}{3+3 r+r^{2}}(1, r+2),$$
which yields the following.
Theorem 7.14. Let $\Gamma \subset \mathrm{U}(2)$ be any of the following groups for $r \geq 2$
$$\Gamma=\frac{1}{r^{2}+3 r+3}(1, r+2) .$$
Then there is a non-Artin component $\mathcal{J}_{k}$ of the versal deformation space $\mathbb{C}^{2} / \Gamma$ with $b_{2}=3$ which has $\mathcal{C}\left(\mathcal{J}_{k}\right)>0$.

The dual graph of the minimal resolution of the $M$-resolution in these cases is the following. For $r \geq 2:(\overbrace{2, \ldots, 2}^{r+1}, r+2)$.
7.7. Completion of proof of Theorems 1.13 and 1.16. All of the groups in Theorems 1.13 and 1.16 are cyclic groups. By Corollary 1.12, there exists an ALE SFK metric in some Kähler class, for any $J \in \mathcal{J}^{M}(i)$ away from the central fiber. By Subsection 7.2, and Theorems 7.8, 7.11, and 7.14, all cases in Theorems 1.13 and 1.16 satisfy $\mathcal{C}\left(\mathcal{J}^{M}(i)\right)>0$. By Subsection 2.4, assumption 1.6 is satisfied. By Corollary 1.7, it follows that there exists an ALE SFK metric in any Kähler class.

\section*{8. Conclusion}

In this section, we give a family of examples which shows that smoothings of non-minimal orbifolds can occur as limits of minimal ALE scalar-flat Kähler surfaces. In particular, the moduli space of SFK ALE metrics exhibits new phenomena which do not occur in the hyperkähler case $\Gamma \subset \operatorname{SU}(2)$.

Theorem 8.1. There exists sequences $g_{i}$ of $S F K$ ALE metrics on $\mathcal{O}_{\mathbb{C} P^{1}}(-n)$ with respect to complex structures $J_{i}$ in the Artin component of $\mathbb{C}^{2} / \Gamma$, where $\Gamma=\frac{1}{n}(1,1)$, such that
$$\left(\mathcal{O}_{\mathbb{C} P^{1}}(-n), g_{i}, J_{i}, x_{i}\right) \rightarrow\left(X_{\infty}, g_{\infty}, J_{\infty}, x_{\infty}\right)$$
in the pointed Cheeger-Gromov sense to a limiting SFK ALE orbifold ( $X_{\infty}, g_{\infty}, J_{\infty}$ ) such that the limit $\left(X_{\infty}, J_{\infty}\right)$ is birational to $\left(\mathbb{C}^{2} / \mathbb{Z}_{n}, J_{\text {euc }}\right)$, but is not dominated by the minimal resolution.

Proof. For $n \geq 3$, take $\mathcal{O}(-n)$, perform the interated blowup which obtained from $(n-2)$ blow-ups starting on the $(-n)$-curve then blow-down all curves except for the $(-1)$-curve on the end, which yields a type $T_{0}$ singularity. The dual graphs are as follows.

For $n=3:(-1,-4)$.
For $n=4:(-1,-2,-5)$.
For $n \geq 5:(-1, \overbrace{2, \ldots, 2}^{n-3}, n+1)$.
For each $n \geq 3$, denote the blow-down space with a type $T_{0}$ singularity as $Z$. Notice that $Z$ is not an $M$-resolution. However, we will show next that the smoothing of the type $T_{0}$ singularity is unobstructed. The smoothing has $b_{2}=1$, and must lie in the Artin component. This is because there are no non-Artin components for $n \neq 4$, and for $n=4$, the non-Artin component has $b_{2}=0$.

Note that $Z$ is obtained by blow-ups of $\mathcal{O}_{\mathbb{C} P^{1}}(-n)$, and then blow-downs. Since $\mathcal{O}_{\mathbb{C} P^{1}}(-n)$ is toric, and each blow-up is at a point fixed by the torus action, it follows that $Z$ is toric. As in Subsection 7.7, by Calderbank-Singer's construction, there exists a SFK ALE orbifold metric $g_{0}$ on $Z$. We will to apply the smoothing construction as we did in Section 6.4 to find the desired smooth SFK ALE metrics near this orbifold metric.

First we want to show that there is no local-to-global obstruction for the deformation of the quotient singularity. Let $X=Z \cup D$ be the analytic compactification of $Z$, where $D$ is a $(+n)$-curve. We want to smooth out the type $T_{0}$ singularity in $X$ while fixing the divisor $D$. Denote $T_{X}=\mathscr{H}_{o m_{\mathcal{O}_{X}}}\left(\Omega^{1}, \mathcal{O}_{X}\right)$ as the dual sheaf of the ( 1,0 )-form sheaf on $X$, and denote
$T_{X}(-\log (D))$ as the subsheaf of $T X$ where near each point of $D, T_{X}(-\log (D))$ is generated by $(1,0)$-vectors tangent to $D$. We have the following exact sequence
$$\begin{aligned}
H^{1}\left(X, T_{X}(-\log (D))\right) & \rightarrow \operatorname{Ext}\left(\Omega^{1}(\log (D)), \mathcal{O}_{X}\right) \rightarrow \\
& H^{0}\left(X, \mathscr{E} x t_{\mathcal{O}_{X}}^{1}\left(\Omega^{1}(\log (D)), \mathcal{O}_{X}\right)\right) \rightarrow H^{2}\left(X, T_{X}(-\log (D))\right)
\end{aligned}$$
Following the proof of [LP07, Theorem 2], the obstruction to the deformation we want lies in $H^{2}\left(X, T_{X}(-\log (D))\right) \simeq H^{2}\left(\widetilde{X}, T_{\widetilde{X}}(-\log (D+E))\right) \simeq H^{0}\left(\widetilde{X}, K_{\widetilde{X}} \otimes \Omega_{\widetilde{X}}^{1}(\log (D+E))\right)$, where $\widetilde{X}$ is the minimal resolution of $X, E=\cup_{j=0}^{n-3} E_{j}$ is union of the exception divisors resolved from the $T_{0}$-singularity, and the last isomorphism is due to Serre duality. The $E_{j}$ is ordered from the right to the left in the graph above, with $E_{0} \cdot E_{0}=-(n+1), E_{j} \cdot E_{j}=-2$ for $1 \leq j \leq n-3$. Note that $\widetilde{X}$ is obtained by blow-ups of the Hirzebruch surface $F_{n}$. Denote $F$ as the generic fiber, and $E^{\prime}$ as the (-1)-curve in the dual graph above. The canonical divisor can be represented as $K_{\tilde{X}}=(n-2) F-2 D+\sum_{j=1}^{n-3}\left(j E_{j}\right)+(n-2) E^{\prime}$, and the divisor $D=n F+\sum_{j=0}^{n-3} E_{j}+E^{\prime}$. By the definition of $\Omega_{\widetilde{X}}^{1}(l o g(D+E))$, it is a subsheaf of $\Omega_{\widetilde{X}}^{1}(D+E)$. Then
$$\begin{aligned}
& h^{0}\left(\widetilde{X}, K_{\widetilde{X}} \otimes \Omega_{\widetilde{X}}(\log (D+E))\right) \leq h^{0}\left(\widetilde{X}, K_{\widetilde{X}}, K_{\widetilde{X}} \otimes \Omega_{\widetilde{X}}^{1}(D+E)\right)= \\
& h^{0}\left(\widetilde{X},\left((n-2) F-2 D+\sum_{j=1}^{n-3}\left(j E_{j}\right)+(n-2) E^{\prime}\right) \otimes \Omega_{\widetilde{X}}^{1}\left(D+\sum_{j=0}^{n-3} E_{j}\right)\right) \\
& =h^{0}\left(\widetilde{X}, \Omega_{\widetilde{X}}^{1}\left(-2 F+\sum_{j=1}^{n-3}\left(j E_{j}\right)+(n-3) E^{\prime}\right)\right) \leq h^{0}\left(\widetilde{X} \backslash\left(E \cup E^{\prime}\right), \Omega_{\widetilde{X}}^{1}(-2 F)\right)=0 .
\end{aligned}$$
The last equality holds because $F$ can be a generic fiber, so the holomorphic section vanishes generically and thus vanishes everywhere. This implies that there is no local-to-global obstruction for deformations of $X$ which preserve the divisor $D$. The fixed divisor $D$ can be used to construct the deformation to the normal cone. As a result, there exists a deformation $\mathcal{Z} \rightarrow \Delta$, where $\mathcal{Z}_{0} \simeq Z$ and $\Delta \subset \mathbb{C}$, and each smooth fiber $\mathcal{Z}_{t}$ is a Stein manifold diffeomorphic to $\mathcal{O}_{\mathbb{C} P^{1}}(-n)$. Then by using the argument as in Section 6, we can construct a family of SFK ALE metrics which degenerates to the orbifold metric on $Z$. \(\square\)

\section*{References}
\begin{itemize}
\item[] [AB04] Kazuo Akutagawa and Boris Botvinnik, The Yamabe invariants of orbifolds and cylindrical manifolds, and $L^{2}$-harmonic spinors, J. Reine Angew. Math. 574 (2004), 121-146.
\item[] [AI08] Tadashi Ashikaga and Mizuho Ishizaka, Another form of the reciprocity law of Dedekind sum, Hokkaido University EPrints Server, no. 908, http://eprints3.math.sci.hokudai.ac.jp/1849/, 2008.
\item[] [Aku12] Kazuo Akutagawa, Computations of the orbifold Yamabe invariant, Math. Z. 271 (2012), no. 3-4, 611-625.
\item[] [ALM14] Claudio Arezzo, Riccardo Lena, and Lorenzo Mazzieri, On the resolution of constant scalar curvature Kähler orbifolds, arXiv.org:1402.5919, 2014.
\item[] [And89] Michael T. Anderson, Ricci curvature bounds and Einstein metrics on compact manifolds, J. Amer. Math. Soc. 2 (1989), no. 3, 455-490.
\item[] [AP06] Claudio Arezzo and Frank Pacard, Blowing up and desingularizing constant scalar curvature Kähler manifolds, Acta Math. 196 (2006), no. 2, 179-228.
\item[] [Art74] M. Artin, Algebraic construction of Brieskorn's resolutions, J. Algebra 29 (1974), 330-348.
\item[] [AV12] Antonio G. Ache and Jeff A. Viaclovsky, Obstruction-flat asymptotically locally Euclidean metrics, Geom. Funct. Anal. 22 (2012), no. 4, 832-877.
\end{itemize}
[Ban90] Shigetoshi Bando, Bubbling out of Einstein manifolds, Tohoku Math. J. (2) 42 (1990), no. 2, 205-216.
[Bar86] Robert Bartnik, The mass of an asymptotically flat manifold, Comm. Pure Appl. Math. 39 (1986), no. 5, 661-693.
[BC94] Kurt Behnke and Jan Arthur Christophersen, $M$-resolutions and deformations of quotient singularities, Amer. J. Math. 116 (1994), no. 4, 881-903.
[BKN89] Shigetoshi Bando, Atsushi Kasue, and Hiraku Nakajima, On a construction of coordinates at infinity on manifolds with fast curvature decay and maximal volume growth, Invent. Math. 97 (1989), no. 2, 313-349.
[BR15] Olivier Biquard and Yann Rollin, Smoothing singular extremal Kähler surfaces and minimal Lagrangians, Advances in Math. 285 (2015), 980-1024.
[Bur86] Daniel Burns, Twistors and harmonic maps, Talk in Charlotte, N.C., October 1986.
[Cal79] E. Calabi, Métriques kählériennes et fibrés holomorphes, Ann. Sci. École Norm. Sup. (4) 12 (1979), no. 2, 269-294.
[CLW08] Xiuxiong Chen, Claude Lebrun, and Brian Weber, On conformally Kähler, Einstein manifolds, J. Amer. Math. Soc. 21 (2008), no. 4, 1137-1168.
[CS04] David M. J. Calderbank and Michael A. Singer, Einstein metrics and complex singularities, Invent. Math. 156 (2004), no. 2, 405-443.
[Elk74] Renée Elkik, Solution d'équations au-dessus d'anneaux henséliens, Quelques problèmes de modules (Sém. Géom. Anal., École Norm. Sup., Paris, 1971-1972), Astérisque, vol. 16, Soc. Math. France, Paris, 1974, pp. 116-132.
[GK82] Robert E. Greene and Steven G. Krantz, Deformation of complex structures, estimates for the $\bar{\partial}$ equation, and stability of the Bergman kernel, Adv. in Math. 43 (1982), no. 1, 1-86.
[GLS07] G.-M. Greuel, C. Lossen, and E. Shustin, Introduction to singularities and deformations, Springer Monographs in Mathematics, Springer, Berlin, 2007.
[GR84] Hans Grauert and Reinhold Remmert, Coherent analytic sheaves, Springer-Verlag, 1984.
[Gra72] Hans Grauert, über die Deformation isolierter Singularitäten analytischer Mengen, Invent. Math. 15 (1972), 171-198.
[Heb96] Emmanuel Hebey, Sobolev spaces on Riemannian manifolds, Lecture Notes in Mathematics, vol. 1635, Springer-Verlag, Berlin, 1996.
[Hir53] Friedrich Hirzebruch, Über vierdimensionale Riemannsche Flächen mehrdeutiger analytischer Funktionen von zwei komplexen Veränderlichen, Math. Ann. 126 (1953), 1-22.
[Hit97] N. J. Hitchin, Einstein metrics and the eta-invariant, Boll. Un. Mat. Ital. B (7) 11 (1997), no. 2, suppl., 95-105.
[HL75] F. Reese Harvey and H. Blaine Lawson, Jr., On boundaries of complex analytic varieties. I, Ann. of Math. (2) 102 (1975), no. 2, 223-290. MR 0425173
[HL16] Hans-Joachim Hein and Claude LeBrun, Mass in Kähler geometry, Comm. Math. Phys. 347 (2016), no. 1, 183-221.
[HRŞ16] Hans-Joachim Hein, Rares Rasdeaconu, and Ioana Şuvaina, On the classification of ALE Kähler manifolds, arXiv:1610.05239, 2016.
[HV16] Jiyuan Han and Jeff Viaclovsky, Deformation theory of scalar-flat Kähler ALE surfaces, arXiv.org:1605.05267 (to appear in American Journal of Mathematics), 2016.
[Joy00] Dominic D. Joyce, Compact manifolds with special holonomy, Oxford Mathematical Monographs, Oxford University Press, Oxford, 2000.
[Kaw81] Tetsuro Kawasaki, The index of elliptic operators over V-manifolds, Nagoya Math. J. 84 (1981), 135-157.
[Kro89] P. B. Kronheimer, The construction of ALE spaces as hyper-Kähler quotients, J. Differential Geom. 29 (1989), no. 3, 665-683.
[KSB88] J. Kollár and N. I. Shepherd-Barron, Threefolds and deformations of surface singularities, Invent. Math. 91 (1988), no. 2, 299-338.
[Lau79] Henry B. Laufer, Ambient deformations for exceptional sets in two-manifolds, Invent. Math. 55 (1979), no. 1, 1-36.
[Lem92] László Lempert, On three-dimensional Cauchy-Riemann manifolds, J. Amer. Math. Soc. 5 (1992), no. 4, 923-969.
[Lem94] \_\_\_\_, Embeddings of three-dimensional Cauchy-Riemann manifolds, Math. Ann. 300 (1994), no. 1, 1-15.
[Li14] Chi Li, On sharp rates and analytic compactifications of asymptotically conical Kähler metrics, arXiv.org:1405.2433, 2014.
[LM08] Claude LeBrun and Bernard Maskit, On optimal 4-dimensional metrics, J. Geom. Anal. 18 (2008), no. 2, 537-564.
[LP07] Yongnam Lee and Jongil Park, A simply connected surface of general type with $p_{g}=0$ and $K^{2}=2$, Invent. Math. 170 (2007), no. 3, 483-505.
[LV15] Michael T. Lock and Jeff A. Viaclovsky, Anti-self-dual orbifolds with cyclic quotient singularities, J. Eur. Math. Soc. (JEMS) 17 (2015), no. 11, 2805-2841.
[LV19] \_\_\_\_, A smörgåsbord of scalar-flat Kähler ALE surfaces, J. Reine Angew. Math. 746 (2019), 171-208.
[Nak90] Hiraku Nakajima, Self-duality of ALE Ricci-flat 4-manifolds and positive mass theorem, Recent topics in differential and analytic geometry, Academic Press, Boston, MA, 1990, pp. 385-396.
[Nak94] \_\_\_\_, A convergence theorem for Einstein metrics and the ALE spaces, Selected papers on number theory, algebraic geometry, and differential geometry, Amer. Math. Soc. Transl. Ser. 2, vol. 160, Amer. Math. Soc., Providence, RI, 1994, pp. 79-94.
[Nar62a] Raghavan Narasimhan, The Levi problem for complex spaces. II, Math. Ann. 146 (1962), 195-216.
[Nar62b] \_\_\_\_, A note on Stein spaces and their normalisations, Ann. Scuola Norm. Sup. Pisa (3) 16 (1962), 327-333.
[Pet94] Th. Peternell, Pseudoconvexity, the Levi problem and vanishing theorems, Several complex variables, VII, Encyclopaedia Math. Sci., vol. 74, Springer, Berlin, 1994, pp. 221-257.
[Pin78] Henry Pinkham, Deformations of normal surface singularities with $C^{*}$ action, Math. Ann. 232 (1978), no. 1, 65-84.
[Rie74] Oswald Riemenschneider, Deformationen von Quotientensingularitäten (nach zyklischen Gruppen), Math. Ann. 209 (1974), 211-248.
[Ros63] Hugo Rossi, Vector fields on analytic spaces, Ann. of Math. (2) 78 (1963), 455-467.
[Str10] Jeffrey Streets, Asymptotic curvature decay and removal of singularities of Bach-flat metrics, Trans. Amer. Math. Soc. 362 (2010), no. 3, 1301-1324.
[Şuv12] Ioana Şuvaina, ALE Ricci-flat Kähler metrics and deformations of quotient surface singularities, Ann. Global Anal. Geom. 41 (2012), no. 1, 109-123.
[Tia90] G. Tian, On Calabi's conjecture for complex surfaces with positive first Chern class, Invent. Math. 101 (1990), no. 1, 101-172.
[TV05a] Gang Tian and Jeff Viaclovsky, Bach-flat asymptotically locally Euclidean metrics, Invent. Math. 160 (2005), no. 2, 357-415.
[TV05b] \_\_\_\_, Moduli spaces of critical Riemannian metrics in dimension four, Adv. Math. 196 (2005), no. 2, 346-372.
[TV08] \_\_\_\_, Volume growth, curvature decay, and critical metrics, Comment. Math. Helv. 83 (2008), no. 4, 889-911.
[Via10] Jeff Viaclovsky, Monopole metrics and the orbifold Yamabe problem, Annales de L'Institut Fourier 60 (2010), no. 7, 2503-2543.
[Wah79] Jonathan M. Wahl, Simultaneous resolution of rational singularities, Compositio Math. 38 (1979), no. 1, 43-54.
[Wri12] Evan P. Wright, Quotients of gravitational instantons, Ann. Global Anal. Geom. 41 (2012), no. 1, 91-108.

Department of Mathematics, Purdue University, West Lafayette, IN, 47907
E-mail address: han556@purdue.edu
Department of Mathematics, University of California, Irvine, CA, 92697
E-mail address: jviaclov@uci.edu