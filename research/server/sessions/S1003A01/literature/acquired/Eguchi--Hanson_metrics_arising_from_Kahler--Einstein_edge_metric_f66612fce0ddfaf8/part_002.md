---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: Eguchi--Hanson metrics arising from Kahler--Einstein edge metrics]

Lemma 7.2. For $\beta_{1}>0$ and close to zero, $T=T\left(\beta_{1}\right)=1+O\left(\beta_{1}\right)$.
Proof. By Proposition 4.4, $T\left(\beta_{1}\right)$ is determined by $\beta_{1}$, and $T\left(\beta_{1}\right)$ is the first root of the polynomial in (4.12). We rewrite the polynomial in (4.12) as
$$P(\tau)=\frac{k \beta_{1}-n}{k(n+1)}(\tau-1)\left(\tau^{n}+\frac{k \beta_{1}+1}{k \beta_{1}-n}\left(\tau^{n-1}+\cdots+1\right)\right) .$$
Letting $y=\tau-1$,
$$\begin{aligned}
P(y) & =\frac{k \beta_{1}-n}{k(n+1)} y\left((y+1)^{n}+\frac{k \beta_{1}+1}{k \beta_{1}-n}\left((y+1)^{n-1}+\cdots+(y+1)+1\right)\right) \\
& =\frac{k \beta_{1}-n}{k(n+1)} y\left(y^{n}+\ldots+y\left(n+\frac{k \beta_{1}+1}{k \beta_{1}-n}(1+\ldots+n-1)\right)+\frac{k(n+1) \beta_{1}}{k \beta_{1}-n}\right) \\
& =\frac{k \beta_{1}-n}{k(n+1)} y\left(y Q(y)+\frac{k(n+1) \beta_{1}}{k \beta_{1}-n}\right),
\end{aligned}$$
where $Q(y)$ is a polynomial of degree $n-1$ whose coefficients depend on $\beta_{1}$ and whose constant term is
$$Q(0)=n+\frac{k \beta_{1}+1}{k \beta_{1}-n}(1+\ldots+n-1)=n \frac{(n-1)\left(k \beta_{1}+1\right)}{2\left(k \beta_{1}-n\right)}=\frac{n+1}{2} \frac{n k \beta_{1}-n}{k \beta_{1}-n} .$$
By Proposition 4.4, $T-1$ is a root of the term in the parenthesis of the second equation in (7.2), i.e.,
$$0=(T-1) Q(T-1)+\frac{k(n+1) \beta_{1}}{k \beta_{1}-n} .$$
In particular, it follows that $Q(T-1) \neq 0$ for small enough $\beta_{1}$. Thus, dividing we obtain
$$T-1=\frac{k(n+1) \beta_{1}}{\left(-k \beta_{1}+n\right) Q(T-1)} .$$
By (7.1) $\lim _{\beta_{1} \searrow 0} T=1$, and so $\lim _{\beta_{1} \searrow 0} Q(T-1)=(n+1) / 2$ by (7.3). Altogether,
$$T-1=\frac{2 k}{n} \beta_{1}+o\left(\beta_{1}\right),$$
as claimed. \(\square\)

Remark 7.3. The last display generalizes [14, (5.1)] from the surface case $n=2$ to any dimension. Note that in op. cit. $n$ corresponds to our $k$

It follows that in the small angle limit, both angles approach zero at the same rate:
Lemma 7.4. For $\beta_{1}>0$ and close to zero, $\beta_{2}=\beta_{2}\left(\beta_{1}\right)=\beta_{1}+O\left(\beta_{1}^{2}\right)$.
Proof. Combining (7.1) and (5.9) it follows that $\lim _{\beta_{1} \searrow 0} \beta_{2}=0$. Using this, and plugging (7.4), in (5.9) we find that
$$\beta_{1}+\frac{1}{k}=\frac{1}{k}+2 \beta_{1}-\beta_{2}+o\left(\beta_{1}\right),$$
so $\beta_{2}=\beta_{1}+o\left(\beta_{1}\right)$, and so bootstrapping we obtain $\beta_{2}=\beta_{1}+O\left(\beta_{1}^{2}\right)$, as claimed. \(\square\)

Lemma 7.4 motivates treating the angles $2 \pi \beta_{1}$ and $2 \pi \beta_{2}$ on the same footing in the small angle regime, so that it reasonable to hope that under some appropriate rescaling the fibers converge to cylinders, as in [13, 14]. This is precisely what we prove next.

We change variable from $\tau \in(1, T)$ in (4.2) and (4.8) to
$$x:=\frac{\tau-1-\frac{k \beta_{1}}{n}}{\frac{k \beta_{1}^{2}}{n}},$$
with $x \in\left(-\frac{1}{\beta_{1}}, \frac{1}{\beta_{1}}+O(1)\right)$ by (7.4). Note that $x=0$ roughly corresponds to the middle section between $Z_{n, k}$ and $Z_{n,-k}$. By (4.8) and (7.5),
$$\varphi(x)=\frac{k}{2 n} \beta_{1}^{2}+\frac{k}{n} \beta_{1}^{3} x+o\left(\beta_{1}^{2}\right), \quad x \in\left(-\frac{1}{\beta_{1}}, \frac{1}{\beta_{1}}+O(1)\right) .$$

Let $p \in \mathbb{F}_{n, k}$ be a fixed base point chosen from the section $\{x=0\}$, which will serve as the base point we use later for pointed Gromov-Hausdorff convergence.

To find a fiberwise-rescaled limit, we next rescale the metric $\eta_{\beta_{1}}$ in (4.2) along each fiber, i.e., we define
$$\widetilde{\eta_{\beta_{1}}}:=k \tau \pi_{1}^{*} \omega_{\mathrm{FS}}+\frac{1}{\beta_{1}^{2}} \varphi \pi_{2}^{*} \omega_{\mathrm{Cyl}}+\varphi(\sqrt{-1} \alpha \wedge \bar{\alpha}+\sqrt{-1} \alpha \wedge \overline{\mathrm{~d} w / w}+\sqrt{-1} \mathrm{~d} w / w \wedge \bar{\alpha}) .$$

Remark 7.5. This fiberwise rescaled metric is no longer Kähler. Indeed, since the metric $\eta_{\beta_{1}}$ in (4.2) is Kähler, i.e., $\mathrm{d} \eta_{\beta_{1}}=0$, there holds
$$\begin{aligned}
\mathrm{d} \widetilde{\eta_{\beta_{1}}} & =\mathrm{d}\left(\eta_{\beta_{1}}-\left(1-\frac{1}{\beta_{1}^{2}}\right) \varphi \pi_{2}^{*} \omega_{\mathrm{Cyl}}\right) \\
& =-\left(1-\frac{1}{\beta_{1}^{2}}\right) \mathrm{d} \varphi \wedge \pi_{2}^{*} \omega_{\mathrm{Cyl}} \\
& \neq 0 .
\end{aligned}$$

Theorem 7.6. As $\beta_{1} \searrow 0,\left(\mathbb{F}_{n, k}, \widetilde{\eta_{1}}, p\right)$ converges in the pointed Gromov-Hausdorff sense to $\left(\mathbb{P}^{n-1} \times \mathbb{C}^{*}, \frac{k}{n}\left(n \pi_{1}^{*} \omega_{\mathrm{FS}}+\pi_{2}^{*} \omega_{\mathrm{Cyl}}\right), p\right)$.

Proof. We first show on compact subsets, the following pointwise convergence holds:
Claim 7.7. The restriction of $\widetilde{\eta_{\beta_{1}}}$ to a fiber converges to a cylindrical metric pointwise on compact subsets. More precisely,
$$\lim _{\beta_{1} \searrow 0} \frac{1}{\beta_{1}^{2}} \varphi \pi_{2}^{*} \omega_{\mathrm{Cyl}}=\frac{k}{n} \pi_{2}^{*} \omega_{\mathrm{Cyl}} .$$

Proof of the Claim. As shown in (4.4), the restriction of $\eta_{\beta_{1}}$ is given by
$$\frac{1}{2 \varphi(\tau)} \mathrm{d} \tau^{2}+2 \varphi(\tau) \mathrm{d} \theta^{2},$$
thus the restriction of $\widetilde{\eta_{\beta_{1}}}$ to a fiber, using the new coordinates (7.5) is given by
$$\frac{k^{2} \beta_{1}^{2}}{2 n^{2} \varphi(x)} \mathrm{d} x^{2}+\frac{2 \varphi(x)}{\beta_{1}^{2}} \mathrm{~d} \theta^{2} .$$
As $\beta_{1} \searrow 0$, by (7.6), (7.8) converges pointwise on compact subsets to
$$\frac{k}{n} \mathrm{~d} x^{2}+\frac{k}{n} \mathrm{~d} \theta^{2}=\frac{k}{n} \omega_{\mathrm{Cyl}},$$
as claimed. \(\square\)

By the collapsing arguments in the proof of Theorem 7.1 and the claim above, we have shown $\widetilde{\eta_{\beta_{1}}}$ converges pointwise to $\frac{k}{n}\left(n \pi_{1}^{*} \omega_{\mathrm{FS}}+\pi_{2}^{*} \omega_{\mathrm{Cyl}}\right)$ on compact subsets as $\beta_{1} \searrow 0$. It remains to prove the pointed Gromov-Hausdorff convergence. Indeed, by arguments in the proof of Proposition 5.2, the distance between $Z_{n, k}$ and $\{x=0\}$ and the distance between $Z_{n,-k}$ and $\{x=0\}$ tend to infinity under the metric $\widetilde{\eta_{\beta_{1}}}$. Thus in the limit $\beta_{1} \searrow 0$, we get the product differential structure on $\mathbb{P}^{n-1} \times \mathbb{C}^{*}$ as claimed. Choosing the point $p$ as the base point, the pointwise convergence result implies that
$$\lim _{\beta_{1} \searrow 0} \widetilde{\eta_{\beta_{1}}}=\frac{k}{n}\left(n \pi_{1}^{*} \omega_{\mathrm{FS}}+\pi_{2}^{*} \omega_{\mathrm{Cyl}}\right)$$
in the pointed Gromov-Hausdorff sense. \(\square\)

The $\beta_{2} \searrow 0$ case for $\xi_{\beta_{2}}$ is similar to Theorem 7.1 and Theorem 7.6.
The asymptotic behaviors of $t\left(\beta_{2}\right)$ and $\beta_{1}\left(\beta_{2}\right)$ when $\beta_{2} \searrow 0$ are similar to those described in Lemma 7.2 and Lemma 7.4. We collected them as follows.

Lemma 7.8. For $\beta_{2}>0$ and close to zero,
$$t=t\left(\beta_{1}\right)=1-\frac{2 k}{n} \beta_{2}+o\left(\beta_{2}\right) .$$

Lemma 7.9. For $\beta_{2}>0$ and close to zero,
$$\beta_{1}=\beta_{1}\left(\beta_{2}\right)=\beta_{2}+O\left(\beta_{2}^{2}\right) .$$

Now we state the non-rescaling limit of $\xi_{\beta_{2}}$ as $\beta_{2} \searrow 0$.
Theorem 7.10. As $\beta_{2}$ tends to $0,\left(\mathbb{F}_{n, k}, \xi_{\beta_{2}}\right)$ converges in the Gromov-Hausdorff sense to $\left(\mathbb{P}^{n-1}, k \omega_{\mathrm{FS}}\right)$.

Proof. By Proposition 4.5 and Proposition 4.6, $t$ tends to 1 as $\beta_{2} \searrow 0$. The remaining proof is similar to that of Theorem 7.1. \(\square\)

To obtain a non-collapsed metric in the limit, we consider rescaling $\xi_{\beta_{2}}$ in the way of (7.7) and denote the rescaled metric by $\widetilde{\xi_{\beta_{2}}}$ :
$$\widetilde{\xi_{\beta_{2}}}:=k \tau \pi_{1}^{*} \omega_{\mathrm{FS}}+\frac{1}{\beta_{2}^{2}} \varphi \pi_{2}^{*} \omega_{\mathrm{Cyl}}+\varphi(\sqrt{-1} \alpha \wedge \bar{\alpha}-\sqrt{-1} \alpha \wedge \overline{\mathrm{~d} u / u}-\sqrt{-1} \mathrm{~d} u / u \wedge \bar{\alpha}) .$$

Moreover, we consider a change of variable as (7.5):
$$u:=\frac{\tau-1+\frac{k}{n} \beta_{2}}{\frac{k}{n} \beta_{2}^{2}} .$$
As before, we choose a fixed base point from the section $\{u=0\}$.
Theorem 7.11. As $\beta_{2} \searrow 0,\left(\mathbb{F}_{n, k}, \widetilde{\xi_{\beta_{2}}}, q\right)$ converges in the pointed Gromov-Hausdorff sense to $\left(\mathbb{P}^{n-1} \times \mathbb{C}^{*}, \frac{k}{n}\left(n \pi_{1}^{*} \omega_{\mathrm{FS}}-\pi_{2}^{*} \omega_{\mathrm{Cyl}}\right), q\right)$.

Proof. By Lemma 7.8 and Lemma 7.9, we have similar asymptotic behaviors as Lemma 7.2 and Lemma 7.4 in the $\beta_{2}$ case. Then we can apply similar arguments as in the proof of Theorem 7.6. \(\square\)

\section*{A A brief review on Eguchi-Hanson metrics}

In this section, we give a brief review of the construction of Eguchi-Hanson metrics [8]. They are Ricci-flat Kähler metrics defined on the total space of the line bundle $-2 H_{\mathbb{P}^{1}}$.

For $\left(x_{1}+\sqrt{-1} y_{1}, x_{2}+\sqrt{-1} y_{2}\right) \in \mathbb{C}^{2}$, the Hopf coordinates are defined as:
$$\begin{aligned}
& x_{1}+\sqrt{-1} y_{1}=\xi \cos \frac{\theta}{2} e^{\frac{\sqrt{-1}}{2}(\psi+\phi)}, \\
& x_{2}+\sqrt{-1} y_{2}=\xi \sin \frac{\theta}{2} e^{\frac{\sqrt{-1}}{2}(\psi-\phi)},
\end{aligned}$$
where $\xi \geq 0, \theta \in[0, \pi], \psi \in[0,4 \pi]$ and $\phi \in[0,2 \pi]$. Define one-forms on $\mathbb{C}^{2}$ by
$$\begin{aligned}
& \sigma_{1}:=\frac{1}{\xi^{2}}\left(x_{1} \mathrm{~d} y_{2}-y_{2} \mathrm{~d} x_{1}+y_{1} \mathrm{~d} x_{2}-x_{2} \mathrm{~d} y_{1}\right)=\frac{1}{2}(\sin \psi \mathrm{~d} \theta-\sin \theta \cos \psi \mathrm{d} \phi), \\
& \sigma_{2}:=\frac{1}{\xi^{2}}\left(y_{1} \mathrm{~d} y_{2}-y_{2} \mathrm{~d} y_{1}+x_{2} \mathrm{~d} x_{1}-x_{1} \mathrm{~d} x_{2}\right)=\frac{1}{2}(-\cos \psi \mathrm{d} \theta-\sin \theta \sin \psi \mathrm{d} \phi), \\
& \sigma_{3}:=\frac{1}{\xi^{2}}\left(x_{2} \mathrm{~d} y_{2}-y_{1} \mathrm{~d} x_{2}+x_{1} \mathrm{~d} y_{1}-y_{1} \mathrm{~d} x_{1}\right)=\frac{1}{2}(\mathrm{~d} \psi+\cos \theta \mathrm{d} \phi) .
\end{aligned}$$
Direct calculations yield:
$$\begin{aligned}
\mathrm{d} \sigma_{1} & =2 \sigma_{2} \wedge \sigma_{3}, \\
\mathrm{~d} \sigma_{2} & =2 \sigma_{3} \wedge \sigma_{1}, \\
\mathrm{~d} \sigma_{3} & =2 \sigma_{1} \wedge \sigma_{2} .
\end{aligned}$$
The standard Euclidean metric on $\mathbb{C}^{2}$ can be written as
$$\mathrm{d} x_{1}^{2}+\mathrm{d} y_{1}^{2}+\mathrm{d} x_{2}^{2}+\mathrm{d} y_{2}^{2}=\mathrm{d} \xi^{2}+\xi^{2}\left(\sigma_{1}^{2}+\sigma_{2}^{2}+\sigma_{3}^{2}\right) .$$
The Eguchi-Hanson metric with parameter $\epsilon>0$ is defined by
$$g_{\mathrm{EH}, \epsilon}:=\left(1-\frac{\epsilon^{4}}{\xi^{4}}\right)^{-1} \mathrm{~d} \xi^{2}+\xi^{2}\left(\sigma_{1}^{2}+\sigma_{2}^{2}+\left(1-\frac{\epsilon^{4}}{\xi^{4}}\right) \sigma_{3}^{2}\right), \quad \xi \geq \epsilon .$$

Proposition A.1. Eguchi-Hanson metrics defined in (A.3) are Ricci-flat.
Proof. We provide a proof by directly calculating connection forms and curvature forms of the metric. See Remark A. 2 for another proof using Kähler forms of Eguchi-Hanson metrics. Consider a change of variable $\zeta=\zeta(\xi)$ such that $\mathrm{d} \zeta=\left(1-(\epsilon / \xi)^{4}\right)^{-1 / 2} d \xi$. Then we can write (A.3) in the form
$$g_{\mathrm{EH}, \epsilon}=\mathrm{d} \zeta^{2}+f^{2}(\zeta)\left(\sigma_{1}^{2}+\sigma_{2}^{2}+g^{2}(\zeta) \sigma_{3}^{2}\right),$$
where $f=\xi$ and $g=\left(1-(\epsilon / \xi)^{4}\right)^{1 / 2}$. Consider an orthonormal basis
$$\left(\omega^{0}, \omega^{1}, \omega^{2}, \omega^{3}\right)=\left(\mathrm{d} \zeta, f g \sigma_{3}, f \sigma_{1}, f \sigma_{2}\right) .$$
Then $g_{\mathrm{EH}, \epsilon}=\sum_{i=0}^{3}\left(\omega^{i}\right)^{2}$ and $\left\{\omega^{i}\right\}_{i=0}^{3}$ satisfy the following equations:
$$\begin{aligned}
& \mathrm{d} \omega^{i}=\omega^{j} \wedge \omega_{j}^{i}, \quad \text { for } i=0,1,2,3, \\
& \omega_{i}^{j}+\omega_{j}^{i}=0, \quad \text { for } i, j=0,1,2,3,
\end{aligned}$$
where $\left\{\omega_{i}^{j}\right\}_{i, j=0}^{3}$ are connection forms with respect to $\left\{\omega^{i}\right\}_{i=0}^{3}$. Next let us determine connection forms. For $i=1$, we have
$$\mathrm{d} \omega^{1}=\frac{f^{\prime} g+f g^{\prime}}{f g} \omega^{0} \wedge \omega^{1}+\frac{2 g}{f} \omega^{2} \wedge \omega^{3},$$
where $f^{\prime}$ and $g^{\prime}$ denote the derivative with respect to $\zeta$. Without loss of generality, we let
$$\begin{aligned}
\omega_{0}^{1} & =\frac{f^{\prime} g+f g^{\prime}}{f g} \omega^{1}, \\
\omega_{2}^{1} & =\frac{g}{f} \omega^{3}, \\
\omega_{3}^{1} & =-\frac{g}{f} \omega^{2} .
\end{aligned}$$
It remains to find $\omega_{0}^{2}, \omega_{0}^{3}$ and $\omega_{2}^{3}$ due to the skew-symmetry of connection forms. By similar calculations we have
$$\begin{aligned}
& \mathrm{d} \omega^{2}=\frac{f^{\prime}}{f} \omega^{0} \wedge \omega^{2}+\frac{2}{f g} \omega^{3} \wedge \omega^{1}, \\
& \mathrm{~d} \omega^{3}=\frac{f^{\prime}}{f} \omega^{0} \wedge \omega^{3}+\frac{2}{f g} \omega^{1} \wedge \omega^{2} .
\end{aligned}$$
Thus, combining (A.4) and (A.5) we obtain
$$\begin{aligned}
& \omega_{0}^{2}=\frac{f^{\prime}}{f} \omega^{2}, \\
& \omega_{0}^{3}=\frac{f^{\prime}}{f} \omega^{3}, \\
& \omega_{2}^{3}=\frac{g^{2}-2}{f g} .
\end{aligned}$$
Notice that
$$\begin{aligned}
& f^{\prime}=\frac{\mathrm{d} \xi}{\mathrm{~d} \zeta}=\left(1-(\epsilon / \xi)^{4}\right)^{1 / 2}=g \\
& g^{\prime}=2 \epsilon^{4} f^{-5}
\end{aligned}$$

Combining (A.4), (A.6) and (A.7) we see
$$\begin{aligned}
& \omega_{0}^{1}=-\omega_{2}^{3}, \\
& \omega_{2}^{1}=\omega_{0}^{3}, \\
& \omega_{3}^{1}=-\omega_{0}^{2} .
\end{aligned}$$
By (A.8) and the fact that $R_{i}^{j}=\mathrm{d} \omega_{i}^{j}-\omega_{i}^{k} \wedge \omega_{k}^{j}$, for $i, j=0,1,2,3$, we obtain that the curvature forms also satisfy
$$\begin{aligned}
& R_{0}^{1}=-R_{2}^{3}, \\
& R_{2}^{1}=R_{0}^{3}, \\
& R_{3}^{1}=-R_{0}^{2} .
\end{aligned}$$
Finally, the Ricci-flatness comes from the formula $\operatorname{Ric}_{i j}=\sum_{k=0}^{3} R_{i k j}^{k}$ and the first Bianchi identity. \(\square\)

Introduce
$$r^{4}=\xi^{4}-\epsilon^{4}, \quad \xi \geq \epsilon,$$
then (A.3) can be written as
$$g_{\mathrm{EH}, \epsilon}=\frac{r^{2}}{\left(\epsilon^{4}+r^{4}\right)^{\frac{1}{2}}}\left(\mathrm{~d} r^{2}+r^{2} \sigma_{3}^{2}\right)+\left(\epsilon^{4}+r^{4}\right)^{\frac{1}{2}}\left(\sigma_{1}^{2}+\sigma_{2}^{2}\right), \quad r \geq 0$$
From (A.9) we are able to convert Eguchi-Hanson metrics into complex form by letting $\left(z_{1}, z_{2}\right) \in \mathbb{C}^{2}$ satisfy
$$\begin{aligned}
& z_{1}=r \cos \frac{\theta}{2} e^{\frac{\sqrt{-1}}{2}(\psi+\phi)}, \\
& z_{2}=r \sin \frac{\theta}{2} e^{\frac{\sqrt{-1}}{2}(\psi-\phi)} .
\end{aligned}$$
Denote by $\omega_{\mathrm{EH}, \epsilon}$ the Kähler form corresponding to $g_{\mathrm{EH}, \epsilon}$. Then by (A.9) we have in complex coordinates,
$$\begin{aligned}
\omega_{\mathrm{EH}, \epsilon} & =\sqrt{-1} \partial \bar{\partial}\left[\sqrt{r^{4}+\epsilon^{4}}+\log r^{2}-\log \left(\epsilon^{2}+\sqrt{r^{4}+\epsilon^{4}}\right)\right] \\
& =\frac{\sqrt{-1} r^{2}}{\sqrt{r^{4}+\epsilon^{4}}}\left(\mathrm{~d} z_{1} \wedge \mathrm{~d} \bar{z}_{1}+\mathrm{d} z_{2} \wedge \mathrm{~d} \bar{z}_{2}\right)+\frac{\epsilon^{4}}{\sqrt{r^{4}+\epsilon^{4}}} \sqrt{-1} \partial \bar{\partial} \log \left(r^{2}\right) .
\end{aligned}$$
Remark A.2. By calculating the Ricci form of $\omega_{\mathrm{EH}, \epsilon}$ as in (A.12), we can also derive the Ricci-
flatness of Eguchi-Hanson metrics. Indeed, from (A.12) we calculate
$$\begin{aligned}
\operatorname{Ric} \omega_{\mathrm{EH}, \epsilon} & =\operatorname{Ric} \sqrt{-1}\left(\left[\frac{r^{2}}{\sqrt{r^{4}+\epsilon^{4}}}+\frac{\epsilon^{4}\left|z_{2}\right|^{2}}{\sqrt{r^{4}+\epsilon^{4} r^{4}}}\right] \mathrm{d} z_{1} \wedge \mathrm{~d} \bar{z}_{1}\right. \\
& -\frac{\epsilon^{4} z_{2} \bar{z}_{1}}{\sqrt{r^{4}+\epsilon^{4} r^{4}}} \mathrm{~d} z_{1} \wedge \mathrm{~d} \bar{z}_{2}-\frac{\epsilon^{4} z_{1} \bar{z}_{2}}{\sqrt{r^{4}+\epsilon^{4} r^{4}}} \mathrm{~d} z_{2} \wedge \mathrm{~d} \bar{z}_{1} \\
& \left.+\left[\frac{r^{2}}{\sqrt{r^{4}+\epsilon^{4}}}+\frac{\epsilon^{4}\left|z_{1}\right|^{2}}{\sqrt{r^{4}+\epsilon^{4}} r^{4}}\right] \mathrm{d} z_{2} \wedge \mathrm{~d} \bar{z}_{2}\right) \\
& =-\sqrt{-1} \partial \bar{\partial} \log \left(\left[\frac{r^{2}}{\sqrt{r^{4}+\epsilon^{4}}}+\frac{\epsilon^{4}\left|z_{2}\right|^{2}}{\sqrt{r^{4}+\epsilon^{4} r^{4}}}\right]^{2}\right. \\
& \left.-\frac{\epsilon^{4}\left|z_{1}\right|^{2}\left|z_{2}\right|^{2}}{\left(r^{4}+\epsilon^{4}\right) r^{8}}\right) \\
& =-\sqrt{-1} \partial \bar{\partial} \log 1 \\
& =0
\end{aligned}$$

From (A.9) one finds that $g_{\mathrm{EH}, \epsilon}$ is defined on $\mathbb{C}^{2}$ with possible singularity at $r=0$. Since $g_{\mathrm{EH}, \epsilon}$ is invariant under the antipodal reflection, we have an induced metric on $\left(\mathbb{C}^{2} \backslash\{0\}\right) / \mathbb{Z}_{2}$ that admits no singularity. Consider the blow-up of $\left(\mathbb{C}^{2} \backslash\{0\}\right) / \mathbb{Z}_{2}$ at the origin, which is biholomorphic to the total space of the line bundle $-2 H_{\mathbb{P}^{1}}$, then a calculation in (B.4) below shows that $\sigma_{1}^{2}+\sigma_{2}^{2}$ is the pull-back of the Fubini-Study metric from the exceptional divisor. Hence $g_{\mathrm{EH}, \epsilon}$ extends to a metric on the total space $-2 H_{\mathbb{P}^{1}}$ by letting $r=0$ when restricting $g_{\mathrm{EH}, \epsilon}$ to the exceptional divisor.

\section*{B Eguchi-Hanson metrics as Gromov-Hausdorff limits of Kähler-Einstein edge metrics}

In this section we give a direct proof of a special case of Theorem 6.1 when $n=k=2$. We already know we will obtain Eguchi-Hanson metrics in the limit.

Recall in (4.2) we denote by $\eta$ a Kähler-Einstein edge metric on Calabi-Hirzebruch manifolds $\mathbb{F}_{n, k}$ that has the following form:
$$\eta=k \tau \pi_{1}^{*} \omega_{\mathrm{FS}}+\varphi\left(\pi_{2}^{*} \omega_{\mathrm{Cyl}}+\sqrt{-1} \alpha \wedge \bar{\alpha}+\sqrt{-1} \alpha \wedge \frac{\mathrm{~d} \bar{w}}{\bar{w}}+\sqrt{-1} \frac{\mathrm{~d} w}{w} \wedge \bar{\alpha}\right),$$
where $\pi_{1}, \pi_{2}$ and $\alpha$ are defined below (4.2).
From now on, we assume $k=2$ and $n=2$, i.e., consider the second Hirzebruch surface $\mathbb{F}_{2}$. To build a connection between $g_{\mathrm{EH}, \epsilon}$ and the Kähler edge metric $\eta$ on $\mathbb{F}_{2}$, we first write $\eta$ in terms of one forms introduced in (A.1).

Consider a change of coordinate $w=v^{2}$. The reason to do this is that $w$ is the coordinate along each fiber of the line bundle $-2 H_{\mathbb{P}^{1}}$. Recall (A.10), then we have the following correspondence:
$$\begin{aligned}
z_{1}=v z & =r \cos \frac{\theta}{2} e^{\frac{\sqrt{-1}}{2}(\psi+\phi)}, \\
z_{2}=v & =r \sin \frac{\theta}{2} e^{\frac{\sqrt{-1}}{2}(\psi-\phi)} .
\end{aligned}$$

In particular,
$$\begin{aligned}
r^{2} & =|v|^{2}\left(1+|z|^{2}\right) \\
& =|w|\left(1+|z|^{2}\right) .
\end{aligned}$$
By the definition of $\alpha$ in (4.2), (1, 1)-forms that appear in $\eta$ are
$$\frac{\mathrm{d} z \wedge \mathrm{~d} \bar{z}}{\left(1+|z|^{2}\right)^{2}}, \alpha \wedge \bar{\alpha}, \frac{4 \mathrm{~d} v \wedge \mathrm{~d} \bar{v}}{|v|^{2}}, \alpha \wedge \frac{2 \mathrm{~d} \bar{v}}{\bar{v}}, \frac{2 \mathrm{~d} v}{v} \wedge \bar{\alpha} .$$

Let us first calculate $\sigma_{1}^{2}+\sigma_{2}^{2}$ in terms of the coordinate $z$ and $v$. By (A.1) and (B.2) we have
$$\begin{aligned}
\sigma_{1}^{2}+\sigma_{2}^{2} & =\frac{1}{4} \mathrm{~d} \theta^{2}+\frac{1}{4} \sin ^{2} \theta \mathrm{~d} \phi^{2} \\
& =\frac{1}{4}\left(-\frac{|z| \mathrm{d} z}{\left(1+|z|^{2}\right) z}-\frac{|z| \mathrm{d} \bar{z}}{\left(1+|z|^{2}\right) \bar{z}}\right)^{2}+ \\
& \frac{1}{4}\left(\frac{2|z|}{1+|z|^{2}}\right)^{2} \cdot\left(\frac{1}{2 \sqrt{-1}}\left(\frac{\mathrm{~d} z}{z}-\frac{\mathrm{d} \bar{z}}{\bar{z}}\right)\right)^{2} \\
& =\operatorname{Re} \frac{\mathrm{d} z \otimes \mathrm{~d} \bar{z}}{\left(1+|z|^{2}\right)^{2}} .
\end{aligned}$$

For $\mathrm{d} r^{2}$ and $\sigma_{3}$, By (A.1) and (B.2) we have
$$\begin{aligned}
4 r^{2} \mathrm{~d} r^{2} & =\frac{r^{4}}{4}\left(\alpha+\bar{\alpha}+\frac{2 \mathrm{~d} v}{v}+\frac{2 \mathrm{~d} \bar{v}}{\bar{v}}\right)^{2}, \\
\sigma_{3}^{2} & =-\frac{1}{16}\left(\alpha-\bar{\alpha}+\frac{2 \mathrm{~d} v}{v}-\frac{2 d \bar{v}}{\bar{v}}\right)^{2} . \\
\mathrm{d} r^{2}+r^{2} \sigma_{3}^{2} & =\frac{r^{2}}{4} \operatorname{Re}\left(\frac{4 \mathrm{~d} v \otimes \mathrm{~d} \bar{v}}{|v|^{2}}+\alpha \otimes \bar{\alpha}+\alpha \otimes \frac{2 \mathrm{~d} \bar{v}}{\bar{v}}+\frac{2 \mathrm{~d} v}{v} \otimes \bar{\alpha}\right) .
\end{aligned}$$
Denote by $g_{\eta}$ the corresponding Riemannian metric on $-2 H_{\mathbb{P}^{1}}$ with respect to $\eta$. Then combining (B.1), (B.4) and (B.5) we obtain
$$g_{\eta}=2 \tau\left(\sigma_{1}^{2}+\sigma_{2}^{2}\right)+\varphi \cdot \frac{4}{r^{2}}\left(\mathrm{~d} r^{2}+r^{2} \sigma_{3}^{2}\right) .$$

For $\tau$ and $\varphi$ in (B.6), results in Section 4 apply after we fix $n=k=2$ there. A key feature when $n=2$ is the right hand side in (4.8) is a cubic polynomial, which is easy to handle. In other words, we will be able to derive more precise dependence of $T$ and $\beta_{2}$ on $\beta_{1}$ comparing to results in Proposition 5.1 and Proposition 5.3. Indeed, this was done in the work of [14]. In this and the next section, we fix $n=2$ and make use of several results obtained in [14].

Since $n=k=2$, we find $\beta_{1} \in(0,1)$. We will study the asymptotic behaviors of Kähler-Einstein edge metrics $\eta$ when $\beta_{1} \rightarrow 1$. Recall [14, (4.20)]
$$\beta_{2}=\frac{1}{4}\left(2 \beta_{1}+\sqrt{3\left(3-2 \beta_{1}\right)\left(1+2 \beta_{1}\right)}-3\right) .$$
So we have $\beta_{2} \rightarrow \frac{1}{2}$ as $\beta_{1} \rightarrow 1$. Recall, $\tau$ ranges from $[1, T]$ and $T$ is given by [14, (5.1)]
$$T=1+3 \frac{\sqrt{1+\frac{4}{3} \beta_{1}-\frac{4}{3} \beta_{1}^{2}}+2 \beta_{1}-1}{4-4 \beta_{1}} .$$

Thus, $T \rightarrow+\infty$ as $\beta_{1} \rightarrow 1$. Moreover, recall in (4.8) $\varphi(\tau)$ is given by
$$\begin{aligned}
\varphi(\tau) & =\frac{1}{2} \frac{\tau^{2}-1}{\tau}+\frac{1}{3}\left(\beta_{1}-1\right) \frac{\tau^{3}-1}{\tau} \\
& =\frac{1}{3}\left(\beta_{1}-1\right)(\tau-1)\left(\tau-\alpha_{1}\right)(\tau-T) / \tau, \quad \text { for } \tau \in[1, T],
\end{aligned}$$
where $\alpha_{1}$ is given in [14, (5.2)] by $\alpha_{1}=1+3 \frac{-\sqrt{1+\frac{4}{3} \beta_{1}-\frac{4}{3} \beta_{1}^{2}}+2 \beta_{1}-1}{4-4 \beta_{1}}$ and $\alpha_{1}$ tends to -1 as $\beta_{1} \rightarrow 1$. Below we first show as $\beta_{1} \rightarrow 1$, the divisor $Z_{-2}$ gets pushed-off to infinity. This result is a special case of Proposition 5.2, and for the reader's convenience we include a proof here.

Proposition B.1. The length of the path on each fiber between the intersection point of the fiber with $Z_{2}$ and that of the fiber with $Z_{-2}$ tends to infinity as $\beta_{1} \rightarrow 1$.
Proof. Restricted to the fiber $\{z=0\}$, by (B.1) $\eta=\varphi \sqrt{-1} \mathrm{~d} w \wedge \mathrm{~d} \bar{w} /|w|^{2}$ gives a metric
$$g=\frac{1}{2 \varphi(\tau)} \mathrm{d} \tau^{2}+2 \varphi(\tau) \mathrm{d} \theta^{2}$$
Up to some constant, the distance between $\{\tau=1\}$ and $\{\tau=T\}$ is given by
$$\begin{aligned}
\int_{1}^{T} \frac{1}{\sqrt{\varphi(\tau)}} \mathrm{d} \tau & =\int_{1}^{T} \frac{\sqrt{\tau} \mathrm{~d} \tau}{\sqrt{\frac{1}{3}\left(\beta_{1}-1\right)(\tau-1)\left(\tau-\alpha_{1}\right)(\tau-T)}} \\
& =\frac{1}{\sqrt{\frac{1}{3}\left(1-\beta_{1}\right)}} \int_{1}^{T} \frac{\sqrt{\tau} \mathrm{~d} \tau}{\sqrt{(\tau-1)\left(\tau-\alpha_{1}\right)(T-\tau)}} \\
& \stackrel{\xi=\tau-1}{=} \frac{1}{\sqrt{\frac{1}{3}\left(1-\beta_{1}\right)}} \int_{0}^{T-1} \frac{\sqrt{\xi+1} \mathrm{~d} \xi}{\sqrt{\xi\left(\xi+1-\alpha_{1}\right)(T-1-\xi)}} \\
& =: \int_{0}^{T-1} I \mathrm{~d} \xi
\end{aligned}$$
Near $\xi=0$, terms $\sqrt{\xi+1}$ and $\sqrt{\xi+1-\alpha_{1}}$ are uniformly bounded as $\beta_{1} \rightarrow 1$. (B.8) satisfies
$$\int_{0}^{\epsilon} I \mathrm{~d} \xi \leq\left. C \cdot \frac{1}{\sqrt{1-\beta_{1}}} \cdot \frac{1}{\sqrt{\frac{1}{1-\beta_{1}}}} \cdot \sqrt{\xi}\right|_{0} ^{\epsilon}$$
for some uniform constant $C>0$ and any small $\epsilon>0$. Thus the integration in (B.8) does not blow up near $\xi=0$. Near $\xi=T-1$, in (B.8) for any fixed $\epsilon>0$, we can find $\beta_{1}$ close to 1 such that for $\xi \in(T-1-\epsilon, T-1)$, we have
$$\begin{aligned}
& \sqrt{\xi+1} \geq \sqrt{T-\epsilon} \geq \frac{1}{2} T, \\
& \sqrt{\xi\left(\xi+1-\alpha_{1}\right)} \leq \sqrt{(T-1)\left(T-\alpha_{1}\right)} \leq \sqrt{2} T .
\end{aligned}$$
Then we have
$$\begin{aligned}
\int_{T-1-\epsilon}^{T-1} I \mathrm{~d} \xi & \geq C \cdot \frac{1}{\sqrt{1-\beta_{1}}} \cdot \frac{1-\beta_{1}}{\sqrt{1-\beta_{1}}} \cdot \int_{T-1-\epsilon}^{T-1} \frac{\mathrm{~d} \xi}{\sqrt{T-1-\xi}} \\
& =\left.C \cdot \frac{1}{\sqrt{1-\beta_{1}}} \cdot \frac{1-\beta_{1}}{\sqrt{1-\beta_{1}}} \cdot \sqrt{\xi}\right|_{0} ^{\epsilon}
\end{aligned}$$
for a uniform constant $C>0$ and arbitrary $\epsilon>0$. Since we can choose arbitrary large $\epsilon$ in (B.9), the integration in (B.8) does not converge as $T \rightarrow \infty$. Combining the discussions above we see that $\int_{0}^{T-1} I \mathrm{~d} \xi$ tends to $\infty$ as $\beta_{1} \rightarrow 1$, i.e., $Z_{-2}$ gets pushed-off to infinity. \(\square\)

From now on, we use $\beta_{1}$ as a subscript to emphasize the dependence on angles. By (B.1) and (B.7), on any compact subsets of $\mathbb{F}_{2}$ we have the following convergence in the $C^{k}$-norm for every $k$ :
$$\begin{aligned}
\eta_{\infty}: & =\lim _{\beta_{1} \rightarrow 1} \eta_{\beta_{1}} \\
& =2 \tau_{\beta_{1}} \frac{\sqrt{-1} \mathrm{~d} z \wedge \mathrm{~d} \bar{z}}{\left(1+|z|^{2}\right)^{2}}+\frac{1}{2}\left(\tau_{\beta_{1}}-\frac{1}{\tau_{\beta_{1}}}\right)\left(\frac{\sqrt{-1} \mathrm{~d} w \wedge \mathrm{~d} \bar{w}}{|w|^{2}}+\sqrt{-1} \alpha \wedge \bar{\alpha}\right. \\
& \left.+\sqrt{-1} \alpha \wedge \frac{\mathrm{~d} \bar{w}}{\bar{w}}+\sqrt{-1} \frac{\mathrm{~d} w}{w} \wedge \bar{\alpha}\right) .
\end{aligned}$$
Recall the Ricci curvature tensor of $\eta_{\beta_{1}}$ is given by
$$\begin{aligned}
\operatorname{Ric} \eta_{\beta_{1}} & =\left(1-\beta_{1}\right)\left[C_{1}\right]+\left(1-\beta_{2}\right)\left[C_{2}\right]+2 \frac{\sqrt{-1} \mathrm{~d} z \wedge \mathrm{~d} \bar{z}}{\left(1+|z|^{2}\right)^{2}}-\sqrt{-1} \partial \bar{\partial} \log \tau_{\beta_{1}} \\
& -\sqrt{-1} \partial \bar{\partial} \log \varphi_{\beta_{1}} .
\end{aligned}$$
The Ricci curvature $\lambda_{\beta_{1}}$ of $\eta_{\beta_{1}}$ is given by $\lambda_{\beta_{1}}=1-\beta_{1}$. Notice that $\lambda_{\beta_{1}} \rightarrow 0$ as $\beta_{1} \rightarrow 1$. Hence, by (B.11) and facts that $\varphi \rightarrow\left(\tau^{2}-1\right) / 2 \tau$ in the limit and $\tau$ is a function of $r^{4}=|w|^{2}\left(1+|z|^{2}\right)^{2}$ (recall (B.3)) we have
$$\begin{aligned}
& 2 \frac{\sqrt{-1} \mathrm{~d} z \wedge \mathrm{~d} \bar{z}}{\left(1+|z|^{2}\right)^{2}}-\sqrt{-1} \partial \bar{\partial} \log \tau_{\infty}-\sqrt{-1} \partial \bar{\partial} \log \varphi_{\infty}=0, \\
\Rightarrow & \tau_{\infty} \varphi_{\infty}=C|w|^{2}\left(1+|z|^{2}\right)^{2}, \\
\Rightarrow & \tau_{\infty}=C^{-\frac{1}{2}}\left(C+r^{4}\right)^{\frac{1}{2}}, \quad \text { for some constant } C>0 .
\end{aligned}$$
Replacing $\tau$ and $\varphi$ in (B.6) using (B.12), we have
$$\eta_{\infty}=2 C^{-\frac{1}{2}}\left(\left(C+r^{4}\right)^{\frac{1}{2}}\left(\sigma_{1}^{2}+\sigma_{2}^{2}\right)+\frac{r^{2}}{\left(C+r^{4}\right)^{\frac{1}{2}}}\left(\mathrm{~d} r^{2}+r^{2} \sigma_{3}^{2}\right)\right) .$$
Comparing (B.13) to (A.9) we see $\eta$ converges on compact subsets to an Eguchi-Hanson metric as $\beta_{1} \rightarrow 1$. Summarizing discussions above, we have shown the following result. It is a special case of Theorem 6.1 and provides a new way of understanding Eguchi-Hanson metrics.
Theorem B.2. Fix an arbitrary base point $p$ on the zero section. The Kähler-Einstein edge metric $\left(\mathbb{F}_{2}, \eta_{\beta_{1}}, p\right)$ on $\mathbb{F}_{2}$ converges in the pointed Gromov-Hausdorff sense to the following Eguchi-Hanson metric $\left(-2 H_{\mathbb{P}^{1}}, \eta_{\infty}\right), p$ on $-2 H_{\mathbb{P}^{1}}$ as $\beta_{1} \rightarrow 1$ :
$$\eta_{\infty}=2 C^{-\frac{1}{2}}\left(\left(C+r^{4}\right)^{\frac{1}{2}}\left(\sigma_{1}^{2}+\sigma_{2}^{2}\right)+\frac{r^{2}}{\left(C+r^{4}\right)^{\frac{1}{2}}}\left(d r^{2}+r^{2} \sigma_{3}^{2}\right)\right),$$
where $C>0$ is a constant.
Proof. The convergence on any compact subset of $-2 H_{\mathbb{P}^{1}}$ of such $\eta$ to an Eguchi-Hanson metric in $C^{k}$-norm for every $k$ can be seen from (B.13). Combining this fact, the fact that $Z_{-2}$ gets pushed-off to infinity as $\beta_{1} \rightarrow 1$ and choosing an arbitrary base point from the exceptional divisor $Z_{2}$, we obtain the convergence in the pointed Gromov-Hausdorff sense by considering convergence of $\eta$ to an Eguchi-Hanson metric on compact geodesic balls centered at the base point. \(\square\)

\section*{C Examples of limit of Kähler-Einstein edge metrics}

In this section, we fix $k=1$ and $n=2$. Then we follow Section 5 and Section 6 to give more concrete examples as limit of Kähler-Einstein edge metrics. In the previous work, we treated the case $\beta_{1} \searrow 0$ and $\beta_{1} \rightarrow 1$ [14]. In this section, we consider the several cases: $\beta_{1} \nearrow 2$, $\beta_{2} \nearrow 1$ with no rescaling and $\beta_{2} \nearrow 1$ with rescaling. The asymptotic behaviors in such cases are summarized in Table 1.

Under the assumption $k=1$ and $n=2, \beta_{1}$ ranges from $(0,2) . \tau$ ranges from $[1, T]$. We will study the limiting behaviors of Kähler-Einstein edge metrics when $\beta_{1} \rightarrow 2$.

By (4.8) $\varphi(\tau)$ satisfies
$$\begin{aligned}
\varphi(\tau) & =\frac{\tau^{2}-1}{\tau}+\frac{1}{3}\left(\beta_{1}-2\right)\left(\tau^{3}-1\right) \\
& =\frac{1}{3}\left(\beta_{1}-2\right)(\tau-1)\left(\tau-\alpha_{1}\right)(\tau-T) / \tau,
\end{aligned}$$
where $T$ and $\alpha_{1}$ satisfy [14, (5.1), (5.2)]
$$\begin{aligned}
& T=1+3 \frac{\sqrt{1+\frac{2}{3} \beta_{1}-\frac{1}{3} \beta_{1}^{2}}+\beta_{1}-1}{4-2 \beta_{1}}, \\
& \alpha_{1}=1+3 \frac{-\sqrt{1+\frac{2}{3} \beta_{1}-\frac{1}{3} \beta_{1}^{2}}+\beta_{1}-1}{4-2 \beta_{1}} .
\end{aligned}$$
Obviously $T \rightarrow+\infty$ and $\alpha_{1} \rightarrow-1$ as $\beta_{1} \rightarrow 2$. $\beta_{2}$ is given by [14, (4.20)]
$$\beta_{2}=\frac{\beta_{1}-3+3 \sqrt{1+\frac{2}{3} \beta_{1}-\frac{1}{3} \beta_{1}^{2}}}{2} .$$
Thus $\beta_{2} \rightarrow 1$ as $\beta_{1} \rightarrow 2$. More precisely, we have the following asymptotic behavior of $\beta_{2}\left(\beta_{1}\right)$ :
Lemma C.1. For $\beta_{1}<2$ and close to $2, \beta_{2}\left(\beta_{1}\right)=\frac{1}{2} \beta_{1}+o(1)$.
The length of the path on each fiber between the intersection point of the fiber with $Z_{1}$ and that of the fiber with $Z_{-1}$ is given by the integration of $\varphi(\tau)$ from 1 to $T$. A similar calculation as in the proof of Proposition B. 1 shows the following result.
Proposition C.2. The length of the path on each fiber between the intersection point of the fiber with $Z_{1}$ and that of the fiber with $Z_{-1}$ tends to infinity as $\beta_{1} \rightarrow 2$.

Recall we assume Kähler-Einstein edge metrics on $\mathbb{F}_{1}$ have the form as in (B.1). The Ricci curvature form of such Kähler-Einstein edge metrics, denoted by $\eta$, is given by (B.11). From now on, we denote by $\eta_{\beta_{1}}, \tau_{\beta_{1}}$ and $\varphi_{\beta_{1}}$ to emphasize the dependence of metrics and coordinates on $\beta_{1}$. Let us consider on any compact subsets of $\mathbb{F}_{1}$,
$$\begin{aligned}
\lim _{\beta_{1} \rightarrow 2} \eta_{\beta_{1}} & =\lim _{\beta_{1} \rightarrow 2} \tau \frac{\sqrt{-1} \mathrm{~d} z \wedge \mathrm{~d} \bar{z}}{\left(1+|z|^{2}\right)^{2}}+\left(\frac{\tau^{2}-1}{\tau}+\frac{1}{3}\left(\beta_{1}-2\right)\left(\tau^{3}-1\right)\right)\left(\frac{\sqrt{-1} \mathrm{~d} w \wedge \mathrm{~d} \bar{w}}{|w|^{2}}\right. \\
& \left.+\sqrt{-1} \alpha \wedge \bar{\alpha}+\sqrt{-1} \alpha \wedge \frac{\mathrm{~d} \bar{w}}{\bar{w}}+\sqrt{-1} \frac{\mathrm{~d} w}{w} \wedge \bar{\alpha}\right) \\
& =\tau \frac{\sqrt{-1} \mathrm{~d} z \wedge \mathrm{~d} \bar{z}}{\left(1+|z|^{2}\right)^{2}}+\frac{\tau^{2}-1}{\tau}\left(\frac{\sqrt{-1} \mathrm{~d} w \wedge \mathrm{~d} \bar{w}}{|w|^{2}}+\sqrt{-1} \alpha \wedge \bar{\alpha}+\sqrt{-1} \alpha \wedge \frac{\mathrm{~d} \bar{w}}{\bar{w}}\right. \\
& \left.+\sqrt{-1} \frac{\mathrm{~d} w}{w} \wedge \bar{\alpha}\right) . \\
& =: \eta_{\infty}
\end{aligned}$$

The Ricci curvature $\lambda_{\beta_{1}}$ of $\eta_{\beta_{1}}$ is given by $\lambda_{\beta_{1}}=2-\beta_{1}$. As $\beta_{1} \rightarrow 2$, the Ricci curvature $\lambda_{\beta_{1}}$ tends to 0. Thus, the limit metric $\eta_{\infty}$ has Ricci curvature 0. Hence by (B.11), $\tau_{\infty}$ and $\varphi_{\infty}$ satisfy
$$\begin{aligned}
& 2 \frac{\sqrt{-1} \mathrm{~d} z \wedge \mathrm{~d} \bar{z}}{\left(1+|z|^{2}\right)^{2}}-\sqrt{-1} \partial \bar{\partial} \log \tau_{\infty}-\sqrt{-1} \partial \bar{\partial} \log \varphi_{\infty}=0, \\
\Rightarrow & \tau_{\infty} \varphi_{\infty}=C|w|^{4}\left(1+|z|^{2}\right)^{2}, \\
\Rightarrow & \tau_{\infty}=\left(1+C|w|^{4}\left(1+|z|^{2}\right)^{2}\right)^{\frac{1}{2}}, \quad \text { for some constant } C>0 .
\end{aligned}$$
Thus we obtain the following theorem, which is a special case of Theorem 6.1.
Theorem C.3. Fix an arbitrary base point $p$ on $Z_{1} \subset \mathbb{F}_{1}$. As $\beta_{1} \rightarrow 2$, the Kähler-Einstein edge metric $\left(\mathbb{F}_{1}, \eta_{\beta_{1}}, p\right)$ on $\mathbb{F}_{1}$ converges in the pointed Gromov-Hausdorff sense to a Ricci-flat metric $\left(-H_{\mathbb{P}^{1}}, \eta_{\infty}, p\right)$ on $-H_{\mathbb{P}^{1}}$ with conic singularity of angle $4 \pi$ along $Z_{1}$.

Proof. By (C.2), the limit metric $\eta_{\infty}$ has the form
$$\begin{aligned}
\eta_{\infty}= & \left(1+C|w|^{4}\left(1+|z|^{2}\right)^{2}\right)^{\frac{1}{2}} \frac{\sqrt{-1} \mathrm{~d} z \wedge \mathrm{~d} \bar{z}}{\left(1+|z|^{2}\right)^{2}} \\
& +\frac{C|w|^{4}\left(1+|z|^{2}\right)^{2}}{\left(1+C|w|^{4}\left(1+|z|^{2}\right)^{2^{\frac{1}{2}}}\right.}\left(\frac{\sqrt{-1} \mathrm{~d} w \wedge \mathrm{~d} \bar{w}}{|w|^{2}}+\sqrt{-1} \alpha \wedge \bar{\alpha}+\sqrt{-1} \alpha \wedge \frac{\mathrm{~d} \bar{w}}{\bar{w}}\right. \\
& \left.+\sqrt{-1} \frac{\mathrm{~d} w}{w} \wedge \bar{\alpha}\right),
\end{aligned}$$
for some constant $C>0$. Thus $\eta_{\infty}$ has edge singularity of angle $4 \pi$ along $Z_{1}$. For a fixed base point on $Z_{1}$, Proposition C. 2 shows that $Z_{-1}$ gets pushed-off to infinity in the limit. The remaining proof is the same as that of Theorem B.2. \(\square\)

\section*{C. 1 Calculations in terms of $\beta_{2}$}

In this section, we choose a base point from the infinity section and then study the limiti behavior of the Kähler-Einstein edge metrics. In the language of Section 5, we will consider the Kähler-Einstein edge metrics that are parametrized by $\beta_{2}$.

As in Section 5, we consider $u:=1 / w$ as the fiber coordinate. Then $\{u=0\}$ is the infinity section and $\{u=\infty\}$ is the zero section. We still define $s$ as follows:
$$s=\log \left(1+|z|^{2}\right)-\log |u|^{2} .$$
Then as before $\{s=-\infty\}$ still corresponds to the zero section while $\{s=+\infty\}$ corresponds to the infinity section.

Denote now by $\xi$ the Kähler-Einstein edge metric that we seek on $\mathbb{F}_{1}$. Assume $\xi=$ $\sqrt{-1} \partial \bar{\partial} f(s)$ for some smooth function $f(s)$. As (4.14) we calculate
$$\eta=\sqrt{-1} \partial \bar{\partial} f(s)=\tau \pi_{1}^{*} \omega_{\mathrm{FS}}+\varphi\left(\frac{\sqrt{-1} \mathrm{~d} u \wedge \mathrm{~d} \bar{u}}{|u|^{2}}+\alpha \wedge \bar{\alpha}-\alpha \wedge \frac{\mathrm{d} \bar{u}}{\bar{u}}-\frac{\mathrm{d} u}{u} \wedge \bar{\alpha}\right),$$
where $\alpha:=\bar{z} \mathrm{~d} z / 1+|z|^{2}, \tau=f^{\prime}(s)$ and $\varphi=f^{\prime \prime}(s)$ as before. As in Section 5, after a renormalization of the metric we may assume
$$\sup f^{\prime}(s)=1 .$$

We also assume $\inf f^{\prime}(s)=t$, for some $t>0$. In other words, $\tau$ ranges from $[t, 1]$.
Now we calculate the Ricci curvature form $\eta$ using coordinates $u$ and $z$ :
$$\begin{aligned}
\operatorname{Ric} \eta & =-\sqrt{-1} \partial \bar{\partial} \log \eta^{2} \\
& =-\sqrt{-1} \partial \bar{\partial} \log \frac{\tau \varphi}{|u|^{2}\left(1+|z|^{2}\right)^{2}} \\
& =\left(1-\beta_{1}\right)\left[Z_{1}\right]+\left(1-\beta_{2}\right)\left[Z_{-1}\right]+2 \pi_{1}^{*} \omega_{\mathrm{FS}}-\sqrt{-1} \partial \bar{\partial} \log \tau \\
& -\sqrt{-1} \partial \bar{\partial} \log \varphi .
\end{aligned}$$
Denote the Ricci curvature by $\mu$. The Kähler-Einstein edge equation
$$\operatorname{Ric} \eta=\mu \eta+\left(1-\beta_{1}\right)\left[Z_{1}\right]+\left(1-\beta_{2}\right)\left[Z_{-1}\right]$$
is equivalent to
$$2-\varphi_{\tau}-\varphi / \tau=\mu \tau, \quad \tau \in[t, 1] .$$
Note that (C.3) gives us the same ODE derived in [14, (4.12)]. Now let us determine boundary conditions satisfied by $\varphi(\tau)$. The same arguments in [14, Proposition 3.3] give us that
$$\varphi(t)=\varphi(1)=0, \quad \varphi^{\prime}(t)=\beta_{1}, \quad \varphi^{\prime}(1)=-\beta_{2} .$$
Plugging boundary conditions in (C.3) implies that
$$\mu=2+\beta_{2} .$$
The solution to (C.3) is
$$\varphi(\tau)=\frac{\tau^{2}-1}{\tau}+\frac{2+\beta_{2}}{3} \frac{1-\tau^{3}}{\tau} .$$
Combining (C.4) and (C.5), we obtain the dependence of $t$ and $\beta_{1}$ on $\beta_{2}$ :
$$\begin{aligned}
t & =\frac{1-\beta_{2}+\sqrt{\left(\beta_{2}-1\right)\left(-3 \beta_{2}-9\right)}}{2\left(2+\beta_{2}\right)}, \\
\beta_{1} & =\frac{3}{2}+\frac{1}{2} \beta_{2}-\frac{1}{2} \sqrt{\left(1-\beta_{2}\right)\left(3 \beta_{2}+9\right)} .
\end{aligned}$$
Next, inspired by the result in Theorem C.3, we study the limiting behavior of Kähler-Einstein edge metrics when $\beta_{2}$ tends to 1.

Proposition C.4. The length of the path on each fiber between the intersection point of the fiber with $Z_{1}$ and that of the fiber with $Z_{-1}$ converges to a finite number as $\beta_{2} \rightarrow 1$.

Proof. As shown in Proposition B.1, when restricted to the fiber $\{z=0\}$, the distance between $\{\tau=t\}$ and $\{\tau=1\}$ is given by
$$\int_{t}^{1} \frac{1}{\sqrt{\varphi(\tau)}} \mathrm{d} \tau=\int_{t}^{1} \frac{\sqrt{\tau}}{\sqrt{\left(2+\beta_{2}\right) / 3} \sqrt{(1-\tau)\left(\tau-\alpha_{1}\right)(\tau-t)}} \mathrm{d} \tau .$$
It remains to show the integral in (C.7) converges uniformly as $\beta_{2} \rightarrow 1$. Near $\tau=1, \sqrt{\tau} /(\tau-$ $\left.\alpha_{1}\right)(\tau-t)$ in (C.7) is uniformly bounded as $\beta_{2} \rightarrow 1$. Thus for $\epsilon>0$,
$$\begin{aligned}
& \int_{1-\epsilon}^{1} \frac{\sqrt{\tau}}{\sqrt{\left(2+\beta_{2}\right) / 3} \sqrt{(1-\tau)\left(\tau-\alpha_{1}\right)(\tau-t)}} \mathrm{d} \tau \\
& \leq C \int_{1-\epsilon}^{1} \frac{1}{\sqrt{1-\tau}} \mathrm{d} \tau<\infty
\end{aligned}$$
for some uniform constant $C>0$. In other words, the integral (C.7) does not blow up near $\tau=1$. It remains to study (C.7) near $\tau=t$. We consider a change of coordinate $\xi:=\tau-t$. Then for $\epsilon>0$,
$$\int_{t}^{t+\epsilon} \frac{\sqrt{\tau}}{\sqrt{\left(2+\beta_{2}\right) / 3} \sqrt{(1-\tau)\left(\tau-\alpha_{1}\right)(\tau-t)}} \mathrm{d} \tau \leq C \int_{0}^{\epsilon} \frac{\sqrt{\xi+t}}{\sqrt{\xi\left(\xi+t-\alpha_{1}\right)}},$$
for some uniform constant $C>0$. Since
$$\lim _{\xi \rightarrow 0} \frac{\sqrt{\xi+t}}{\xi+t-\alpha_{1}}=\frac{\sqrt{t}}{\sqrt{t-\alpha_{1}}} \leq C,$$
for some uniform constant $C>0$ when $\beta_{2} \rightarrow 1$, we conclude that the integral (C.7) converges as $\int_{0}^{\epsilon} 1 / \sqrt{\xi}$ near $\tau=t$. Hence we have finished the proof. \(\square\)

From now on, we denote by $\xi_{\beta_{2}}, \tau_{\beta_{2}}$ and $\varphi_{\beta_{2}}$ to indicate the dependence of metrics and coordinates on $\beta_{2}$.

Theorem C.5. Fix an arbitrary base point $p$ on $Z_{-1} \subset \mathbb{F}_{1}$. As $\beta_{2} \rightarrow 1$, the Kähler-Einstein edge metric $\left(\mathbb{F}_{1}, \xi_{\beta_{2}}, p\right)$ on $\mathbb{F}_{1}$ converge in the pointed Gromov-Hausdorff sense to the Fubini-Study metric $\left(\mathbb{P}^{2}, \omega_{\mathrm{FS}}, p\right)$. We will show that $\xi_{\beta_{2}}$ converges pointwise smoothly to a degenerate metric tensor that is the pull-back of the Fubini-Study metric under the blow-up map on $\mathbb{F}_{1}$.

Proof. Denote by $\xi_{\infty}, \tau_{\infty}$ and $\varphi_{\infty}$ the metric and coordinates in the limit when $\beta_{2} \rightarrow 1$. To find a relation between $\tau_{\infty}, \varphi_{\infty}$ and $s$, consider the ODE satisfied by $s$ and $\tau_{\beta_{2}}$ :
$$\frac{\mathrm{d} s}{\mathrm{~d} \tau_{\beta_{2}}}=\frac{1}{\varphi_{\beta_{2}}}=\frac{\tau_{\beta_{2}}}{\left(\frac{2+\beta_{2}}{3}\right)\left(1-\tau_{\beta_{2}}^{3}\right)+\tau_{\beta_{2}}^{2}-1} .$$
Letting $\beta_{2} \rightarrow 1$ in (C.8), we obtain (up to a constant that can be chosen to be 0)
$$s=\log \frac{\tau_{\infty}}{1-\tau_{\infty}}, \quad \tau_{\infty} \in(0,1),$$
where $\tau_{\infty}$ ranges from $(0,1)$ since $t \rightarrow 0$ as $\beta_{2} \rightarrow 1$. Obviously there holds
$$\varphi_{\infty}=\tau_{\infty}\left(1-\tau_{\infty}\right) .$$
Recall $s=\log \left(1+|z|^{2}\right)-\log |u|^{2}$. Combining (C.9) and (C.10), the limit metric $\xi_{\infty}$ has the form:
$$\begin{aligned}
\xi_{\infty} & =\tau_{\infty} \pi_{1}^{*} \omega_{\mathrm{FS}}+\varphi_{\infty}\left(\pi_{2}^{*} \omega_{\mathrm{Cyl}}+\sqrt{-1} \alpha \wedge \bar{\alpha}-\sqrt{-1} \alpha \wedge \frac{\mathrm{~d} \bar{u}}{\bar{u}}-\sqrt{-1} \frac{\mathrm{~d} u}{u} \wedge \bar{\alpha}\right) \\
& =\frac{1+|z|^{2}}{|u|^{2}+1+|z|^{2}} \pi_{1}^{*} \omega_{\mathrm{FS}}+\frac{1+|z|^{2}}{\left(|u|^{2}+1+|z|^{2}\right)^{2}} \sqrt{-1} \mathrm{~d} u \wedge \mathrm{~d} \bar{u} \\
& +\frac{|u|^{2}\left(1+|z|^{2}\right)}{\left(|u|^{2}+1+|z|^{2}\right)^{2}}\left(\sqrt{-1} \alpha \wedge \bar{\alpha}-\sqrt{-1} \alpha \wedge \frac{\mathrm{~d} \bar{u}}{\bar{u}}-\sqrt{-1} \frac{\mathrm{~d} u}{u} \wedge \bar{\alpha}\right) .
\end{aligned}$$

Next, we derive the explicit formula for $\xi_{\infty}$. Recall,
$$\alpha=\frac{\bar{z} \mathrm{~d} z}{1+|z|^{2}} .$$

Plugging (C.12) in (C.11) and by calculations:
$$\begin{aligned}
\xi_{\infty} & =\frac{1+|z|^{2}}{|u|^{2}+1+|z|^{2}} \cdot \frac{\sqrt{-1} \mathrm{~d} z \wedge \mathrm{~d} \bar{z}}{\left(1+|z|^{2}\right)^{2}}+\frac{1+|z|^{2}}{\left(|u|^{2}+1+|z|^{2}\right)^{2}} \sqrt{-1} \mathrm{~d} u \wedge \mathrm{~d} \bar{u} \\
& +\frac{|u|^{2}\left(1+|z|^{2}\right)}{\left(|u|^{2}+1+|z|^{2}\right)^{2}}\left(\sqrt{-1} \cdot \frac{|z|^{2} \mathrm{~d} z \wedge \mathrm{~d} \bar{z}}{\left(1+|z|^{2}\right)^{2}}-\sqrt{-1} \frac{\bar{z} \mathrm{~d} z}{1+|z|^{2}} \wedge \frac{\mathrm{~d} \bar{u}}{\bar{u}}-\sqrt{-1} \frac{\mathrm{~d} u}{u} \wedge \frac{z \mathrm{~d} \bar{z}}{1+|z|^{2}}\right) \\
& =\sqrt{-1}\left(\frac{1+|u|^{2}}{\left(1+|u|^{2}+|z|^{2}\right)^{2}} \mathrm{~d} z \wedge \mathrm{~d} \bar{z}-\frac{\bar{z} u}{\left(1+|u|^{2}+|z|^{2}\right)^{2}} \mathrm{~d} z \wedge \mathrm{~d} \bar{u}-\frac{\bar{u} z}{\left(1+|u|^{2}+|z|^{2}\right)^{2}} \mathrm{~d} u \wedge \mathrm{~d} \bar{z}\right. \\
& \left.+\frac{1+|z|^{2}}{\left(1+|u|^{2}+|z|^{2}\right)^{2}} \mathrm{~d} u \wedge \mathrm{~d} \bar{u}\right) \\
& =\sqrt{-1} \partial \bar{\partial} \log \left(1+|u|^{2}+|z|^{2}\right) .
\end{aligned}$$

This limit metric does not have singularity along $Z_{-} 1$ since $\beta_{2} \rightarrow 1$ in the limit. Moreover, $\xi_{\infty}$ has Ricci curvature 3 since $\mu_{\beta_{2}}$ tends to 3 when $\beta_{2} \rightarrow 1$. Moreover, the metric $\xi_{\infty}$ degenerates along $Z_{1}=\{u=\infty\}$ as $\xi_{\infty} \rightarrow 0$ as $|u| \rightarrow+\infty$.

We next show that $\xi_{\infty}$ is the pull-back of the Fubini-Study metric $\omega_{\mathrm{FS}}$ on $\mathbb{P}^{2}$ under the blow-down map $\pi: \mathbb{F}_{1} \rightarrow \mathbb{P}^{2}$. Figure 2 shows the blow up of $\mathbb{P}^{2}(1,1, k)$ at $p$ giving rise to $\mathbb{F}_{1}$. To see this, we regard $\mathbb{F}_{1}$, which is the blow-up of $\mathbb{P}^{2}$ at one point $p$ (WLOG assuming $p=[1: 0: 0])$, as the variety embedded in $\mathbb{P}^{2} \times \mathbb{P}^{1}$ :
$$\mathbb{F}_{1}=\left\{\left(\left[x_{0}: x_{1}: x_{2}\right],\left[y_{0}: y_{1}\right]\right) \in \mathbb{P}^{2} \times \mathbb{P}^{1}: x_{1} y_{1}=x_{2} y_{0}\right\} .$$
Then the blow-down map $\pi$ is given by:
$$\begin{aligned}
\pi: \mathbb{F}_{1} & \rightarrow \mathbb{P}^{2} \\
\left(\left[x_{0}: x_{1}: x_{2}\right],\left[y_{0}: y_{1}\right]\right) & \mapsto\left[x_{0}: x_{1}: x_{2}\right] .
\end{aligned}$$
Restricted on the chart $\left\{x_{1} \neq 0\right\}$, there hold:
$$u=\frac{x_{0}}{x_{1}}, \quad z=\frac{x_{2}}{x_{1}}$$
and
$$\pi(u, z)=(u, z) \in \mathbb{P}^{2} .$$
Recall the Fubini-Study metric on $\mathbb{P}^{2}$ (restriced to the chart $\left\{x_{1} \neq 0\right\}$ ) has the formula
$$\omega_{\mathrm{FS}}=\sqrt{-1} \log \left(1+|u|^{2}+|z|^{2}\right) .$$
Thus by (C.13) and (C.14) we have shown,
$$\xi_{\infty}=\pi^{*} \omega_{\mathrm{FS}},$$
confirming that $\xi_{\infty}$ degenerates along the exceptional curve $Z_{1}$.
We have shown $\xi_{\beta_{2}}$ converges on any compact subset of $\mathbb{F}_{1}$ to $\xi_{\infty}$. Now fix an arbitrary base point on $Z_{-1} \subset \mathbb{F}_{1}$. By Proposition C.4, the length between $Z_{1}$ and $Z_{-1}$ remains to be finite when $\beta_{2} \rightarrow 1$. Thus $\left(\mathbb{F}_{1}, \xi_{\beta_{2}}, p\right)$ converges in the pointed Gromov-Hausdorff sense to $\left(\mathbb{P}^{2}, \omega_{\mathrm{FS}}, p\right)$ when $\beta_{2} \rightarrow 1$. \(\square\)

Next, we consider the limiting behavior of properly renormalized Kähler-Einstein edge metrics on $\mathbb{F}_{1}$ when $\beta_{2} \rightarrow 1$.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/59facd2c-e2e3-4682-b142-baa3b5352b01-37.jpg?height=383&width=952&top_left_y=244&top_left_x=600}
\captionsetup{labelformat=empty}
\caption{Figure 2: Blow up of $\mathbb{P}^{2}(1,1, k)$ at $p$ (with $k>1$ ).}
\end{figure}

Lemma C.6. Rescaling the metric $\xi$ by a factor $2\left(2+\beta_{2}\right) /\left(1-\beta_{2}+\sqrt{\left(1-\beta_{2}\right)\left(3 \beta_{2}+9\right)}\right)$, the interval of definition of $\tau$ will change from $[t, 1]$ to $[1, T]$ as in (C.1).

Proof. When we calculate in terms of $\beta_{1}$, we have
$$\begin{aligned}
\beta_{2} & =\frac{\beta_{1}-3+3 \sqrt{1+\frac{2}{3} \beta_{1}-\frac{1}{3} \beta_{1}^{2}}}{2}, \\
T & =1+3 \frac{\sqrt{1+\frac{2}{3} \beta_{1}-\frac{1}{3} \beta_{1}^{2}}+\beta_{1}-1}{4-2 \beta_{1}} .
\end{aligned}$$
When we calculate in terms of $\beta_{2}$, we have
$$\begin{aligned}
\beta_{1} & =\frac{3}{2}+\frac{1}{2} \beta_{2}-\frac{1}{2} \sqrt{\left(\beta_{2}-1\right)\left(-3 \beta_{2}-9\right)} \\
t & =\frac{1-\beta_{2}+\sqrt{\left(\beta_{2}-1\right)\left(-3 \beta_{2}-9\right)}}{2\left(2+\beta_{2}\right)} .
\end{aligned}$$
Direct calculation shows (C.15) and (C.17) are equivalent. Combining (C.15) and (C.16), we have
$$T=\frac{2\left(2+\beta_{2}\right)}{4-2 \beta_{1}} .$$
Combining (C.17) and (C.18), we have
$$t=\frac{4-2 \beta_{1}}{2\left(2+\beta_{2}\right)} .$$
Thus, $T=1 / t$ and we can rescale the metric $\eta$ by the factor $1 / t$ to change the domain of $\tau$ from $[t, 1]$ to $[1, T]$. \(\square\)

Inspired by Lemma C.6, we normalize $\xi_{\beta_{2}}$ by the factor $\sqrt{3} / \sqrt{1-\beta_{2}}$ and study its limiting behavior when $\beta_{2}$ tends to 1.

Theorem C.7. Rescaling the metric $\xi_{\beta_{2}}$ by $\sqrt{3} / \sqrt{1-\beta_{2}}$, then as $\beta_{2} \rightarrow 1$, the renormalized metric converges in the pointed Gromov-Hausdorff sense to a Ricci-flat metric on $-H_{\mathbb{P}^{1}}$, where the base point is chosen from $Z_{1}$. See the proof for an explicit explanation. This metric coincides with the one obtained in Theorem C.3.

Proof. Consider the change of coordinate $y_{\beta_{2}}:=\sqrt{3} \tau_{\beta_{2}} / \sqrt{1-\beta_{2}}$ in the following ODE:
$$\frac{\mathrm{d} s}{\mathrm{~d} \tau_{\beta_{2}}}=\frac{1}{\varphi_{\beta_{2}}\left(\tau_{\beta_{2}}\right)},$$
In the following equations, we omit the subscript $\beta_{2}$ :
$$\begin{aligned}
& \frac{\mathrm{d} s}{\mathrm{~d} y} \frac{\mathrm{~d} y}{\mathrm{~d} \tau}=\frac{1}{\varphi(y)} \\
& \Rightarrow \frac{\mathrm{d} s}{\mathrm{~d} y}=\frac{\sqrt{3}}{3} \cdot \frac{\left(1-\beta_{2}\right) y}{\left(\sqrt{1-\beta_{2}} y\right)^{2}-1+\frac{2+\beta_{2}}{3}\left(1-\left(\sqrt{1-\beta_{2}} y\right)^{3}\right)} .
\end{aligned}$$
By an abuse of notation, still denote by $y$ the coordinate in the limit. As $\beta_{2} \rightarrow 1$, there holds
$$\frac{\mathrm{d} s}{\mathrm{~d} y}=\frac{y}{y^{2}-1}, \quad y \in(1,+\infty),$$
where the range of $y$ comes from (C.18). Recall the renormalized metric $\sqrt{3} \xi_{\beta_{2}} / \sqrt{1-\beta_{2}}$ reads
$$\begin{aligned}
\frac{\sqrt{3} \xi_{\beta_{2}}}{\sqrt{1-\beta_{2}}} & =\frac{\sqrt{3} \tau_{\beta_{2}}}{\sqrt{1-\beta_{2}}} \pi_{1}^{*} \omega_{\mathrm{FS}}+\frac{\sqrt{3} \varphi_{\beta_{2}}}{\sqrt{1-\beta_{2}}}\left(\pi_{2}^{*} \omega_{\mathrm{Cyl}}+\sqrt{-1} \alpha \wedge \bar{\alpha}-\sqrt{-1} \alpha \wedge \frac{\mathrm{~d} \bar{u}}{\bar{u}}\right. \\
& \left.-\sqrt{-1} \frac{\mathrm{~d} u}{u} \wedge \alpha\right) .
\end{aligned}$$
Combining (C.19) and (C.20) we obtain the limit metric
$$\begin{aligned}
\tilde{\xi}_{\infty} & =\sqrt{e^{2 s}+1} \pi_{1}^{*} \omega_{\mathrm{FS}}+\frac{e^{2 s}}{\sqrt{e^{2 s}+1}}\left(\pi_{2}^{*} \omega_{\mathrm{Cyl}}+\sqrt{-1} \alpha \wedge \bar{\alpha}-\sqrt{-1} \alpha \wedge \frac{\mathrm{~d} \bar{u}}{\bar{u}}\right. \\
& \left.-\sqrt{-1} \frac{\mathrm{~d} u}{u} \wedge \alpha\right) .
\end{aligned}$$
Note that this limit metric is Ricci-flat. It coincides with the metric obatined in Theorem C. 3 if we choose $C=1$ there. We have shown the renormalized Kähler-Einstein edge metrics converge to $\tilde{\xi}_{\infty}$ in smooth local sense. Next, fix a base point from the zero section $Z_{1}$. Then by Proposition C.4, we conclude that the infinity section $Z_{-1}$ gets pushed-off to infinity in the limit. Combining this fact with the local smooth convergence, we conclude the pointed Gromov-Hausdorff limit of $\left(\mathbb{F}_{1}, \sqrt{3} \eta_{\xi_{2}} / \sqrt{1-\beta_{2}}\right)$ is $\left(-H_{\mathbb{P}^{1}}, \tilde{\xi}_{\infty}\right)$. \(\square\)

\section*{References}
[1] M. Abreu, Kähler metrics on toric orbifolds, J. Differential Geom. 58(2001), 151-187.
[2] M. Atiyah, C. Lebrun, Curvature, cones and characteristic numbers, Math. Proc. Cambridge Philos. Soc. 155(2013), 13-37.
[3] O. Biquard, H. Guenancia, Degenerating Kähler-Einstein cones, locally symmetric cusps, and the Tian-Yau metric, Invent. Math. 230(2022), 1101-1163.
[4] E. Calabi, Métriques kählériennes et fibrés holomorphes, Ann. Sci. École Norm. Sup. (4), 12(1979), 269-294.
\begin{itemize}
\item[] [5] E. Calabi, Extremal Kähler metrics, in: Seminar on Differential Geometry, vol. 102 of Ann. of Math. Stud., Princeton Univ. Press, Princeton, N.J., 1982, pp. 259-290.
\item[] [6] I.A. Cheltsov, Y.A. Rubinstein, Asymptotically log Fano varieties, Adv. Math. 285(2015), 1241-1300.
\item[] [7] S.K. Donaldson, Kähler metrics with cone singularities along a divisor, in: Essays in mathematics and its applications, Springer, Heidelberg, 2012, pp. 49-79.
\item[] [8] T. Eguchi, A.J. Hanson, Self-dual solutions to Euclidean gravity, Ann. Physics 120(1979), 82-106.
\item[] [9] F. Hirzebruch, Über eine Klasse von einfachzusammenhängenden komplexen Mannigfaltigkeiten, Math. Ann. 124(1951), 77-86.
\item[] [10] T. Jeffres, R. Mazzeo, Y.A. Rubinstein, Kähler-Einstein metrics with edge singularities, (with an appendix by C. Li and Y.A. Rubinstein), Ann. of Math. 183(2016), 95-176.
\item[] [11] R. Mazzeo, Kähler-Einstein metrics singular along a smooth divisor, in: Journées "Équations aux Dérivées Partielles" (Saint-Jean-de-Monts, 1999), Univ. Nantes, Nantes, 1999, pp. Exp. No. VI, 10.
\item[] [12] Y.A. Rubinstein, Smooth and singular Kähler-Einstein metrics, in: Geometric and spectral analysis, vol. 630 of Contemp. Math., Amer. Math. Soc., Providence, RI, 2014, pp. 45-138.
\item[] [13] Y.A. Rubinstein, K. Zhang, Small angle limits of Hamilton's footballs, Bull. Lond. Math. Soc. 52(2020), 189-199.
\item[] [14] Y.A. Rubinstein, K. Zhang, Angle deformation of Kähler-Einstein edge metrics on Hirzebruch surfaces, Pure Appl. Math. Q. 18, special issue in honor of Bernard Shiffman (2022), 343-366.
\item[] [15] G. Tian, Kähler-Einstein metrics on algebraic manifolds, in: Transcendental methods in algebraic geometry (Cetraro, 1994), vol. 1646 of Lecture Notes in Math., Springer, Berlin, 1996, pp. 143-185.
\end{itemize}

University of Maryland
yxji@umd.edu, yanir@alum.mit.edu
Laboratory of Mathematics and Complex Systems, School of Mathematical Sciences, Beijing Normal University, Beijing, 100875, P. R. China.
kwzhang@bnu.edu.cn