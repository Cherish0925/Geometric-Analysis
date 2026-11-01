---
retention_scope: session
part: 3
total_parts: 5
---

[Part 3/5 of: A continuous cusp closing process for negative Kähler- ...]

Lemma 3.11. Abuse notation by denoting $\left(\Psi_{\sigma}^{-1}\right)^{*} \psi_{F S, \sigma}$ by $\psi_{F S, \sigma}$ for all sufficiently small values of $\sigma$, including for $\sigma=0$. This is a Kähler potential on the intersection of $T Y_{\sigma}$ with some fixed neighborhood of the origin in $\mathbb{C}^{3}$. Let $z \in T Y_{0}$ with
$$|\sigma|^{\frac{1}{3}} R \leqslant|z| \leqslant \varepsilon,$$
where $\varepsilon$ is a sufficiently small constant independent of $\sigma$ and $R$ is a large constant as in Lemma 2.5. Let $\omega_{\text {flat }}:=i \partial \bar{\partial}|z|^{2}$ be the flat metric on $\mathbb{C}^{3}$. Then for $k=0,1$ and for $|\sigma|^{-1 / 3}|z| \rightarrow \infty$,
$$\begin{aligned}
\left|\nabla_{\left.\omega_{\text {flat }}\right|_{T Y_{0}}}\left(\Phi_{\sigma}^{*} i \partial_{\sigma} \bar{\partial}_{\sigma} \psi_{F S, \sigma}-i \partial \bar{\partial} \psi_{F S, 0}\right)\right|_{\left.\omega_{\text {flat }}\right|_{T Y_{0}}} & =O\left(|\sigma||z|^{-3-k}\right), \\
\left|\nabla_{\omega_{\text {flat }} \mid T_{Y_{0}}}^{k} i \partial \bar{\partial}\left(\Phi_{\sigma}^{*} \psi_{F S, \sigma}-\psi_{F S, 0}\right)\right|_{\left.\omega_{\text {flat }}\right|_{T Y_{0}}} & =O\left(|\sigma||z|^{-3-k}\right) .
\end{aligned}$$
Proof. We only prove (3.22) as the proof of (3.23) is similar. To prove (3.22), we start with
Claim 3.12. One has
$$\Phi_{\sigma}^{*} i \partial_{\sigma} \bar{\partial}_{\sigma} \psi_{F S, \sigma}-i \partial \bar{\partial} \psi_{F S, 0}=\left.\left(\sum_{|I|+|J|=2} \tilde{O}\left(|\sigma||z|^{-3}\right) d z_{I} \wedge d \bar{z}_{J}\right)\right|_{T Y_{0}},$$
where $\tilde{O}\left(|\sigma||z|^{-3}\right)$ is a function on $B_{\varepsilon}(0) \subset \mathbb{C}^{3}$ such that for all $k \geqslant 0$ and $|\sigma|^{-1 / 3}|z| \rightarrow \infty$,
$$\left|\partial^{k} \tilde{O}\left(|\sigma||z|^{-3}\right)\right|=O\left(|\sigma||z|^{-3-k}\right) .$$
Proof of Claim 3.12. The key is the following expression of $\Phi_{\sigma}$ from Lemma 2.5:
$$\Phi_{\sigma}^{*} z_{i}=z_{i}+\nu_{\sigma}(z) \bar{z}_{i}^{2} \quad(i=1,2,3) .$$
Hence, dropping the restriction symbols for simplicity,
$$\Phi_{\sigma}^{*}\left(d z_{i}\right)=d z_{i}+2 \nu_{\sigma}(z) \bar{z}_{i} d z_{i}+\sum_{j=1}^{3} \frac{\partial \nu_{\sigma}(z)}{\partial z_{j}} \bar{z}_{i}^{2} d z_{j}+\sum_{j=1}^{3} \frac{\partial \nu_{\sigma}(z)}{\partial \bar{z}_{j}} \bar{z}_{i}^{2} d \bar{z}_{j} .$$
From Lemma 2.5 we have for all $\ell \geqslant 0$ and for $|\sigma|^{-1 / 3}|z| \rightarrow \infty$ that
$$\left|\partial^{\ell} \nu_{\sigma}(z)\right|=O\left(|\sigma||z|^{-4-\ell}\right) .$$
Therefore
$$\Phi_{\sigma}^{*}\left(d z_{i}\right)=d z_{i}+\sum_{j=1}^{3} \tilde{O}\left(|\sigma||z|^{-3}\right) d z_{j}+\sum_{j=1}^{3} \tilde{O}\left(|\sigma||z|^{-3}\right) d \bar{z}_{j} .$$

On $\mathbb{C}^{3}$, when $|z| \leqslant \varepsilon$ for some sufficiently small constant $\varepsilon$, we have that
$$i \partial \bar{\partial} \psi_{F S}=\sum_{i, j=1}^{3} a_{i \bar{\jmath}}(z) d z_{i} \wedge d \bar{z}_{j}, \quad a_{i \bar{\jmath}}=\delta_{i \bar{\jmath}}+O\left(|z|^{2}\right) \text { as }|z| \rightarrow 0$$
and $a_{i \bar{\jmath}}(z)$ is actually real-analytic in $z$. Then, from (3.26) and (3.28),
$$\Phi_{\sigma}^{*} a_{i \bar{\jmath}}(z)-a_{i \bar{\jmath}}(z)=\tilde{O}\left(|\sigma||z|^{-1}\right) \text { as }|\sigma|^{-\frac{1}{3}}|z| \rightarrow \infty .$$
For example, if $z_{1}^{2}$ appears in $a_{i \bar{\jmath}}(z)$, then the relevant difference is
$$\begin{aligned}
\left(z_{1}+\nu_{\sigma}(z) \bar{z}_{1}^{2}\right)^{2}-z_{1}^{2} & =2 \nu_{\sigma}(z) z_{1} \bar{z}_{1}^{2}+\nu_{\sigma}(z)^{2} \bar{z}_{1}^{4} \\
& =O\left(|\sigma||z|^{-1}\right)+O\left(|\sigma|^{2}|z|^{-4}\right) \text { as }|\sigma|^{-\frac{1}{3}}|z| \rightarrow \infty,
\end{aligned}$$
which is $O\left(|\sigma||z|^{-1}\right)$ because $|\sigma||z|^{-3}=o(1)$.
Then Claim 3.12 follows from (3.29) and (3.31) because $|z|^{-1} \leqslant \varepsilon^{2}|z|^{-3}$. \(\square\)

Next, we estimate the 2-form (3.24) with respect to the metric $\left.\omega_{\text {flat }}\right|_{T Y_{0}}$. To do so, without loss of generality (using the symmetry of $z_{1}, z_{2}, z_{3}$ ) we may assume that $\left|z_{3}\right| \geqslant \max \left\{\left|z_{1}\right|,\left|z_{2}\right|\right\}$. In particular, we are working on the affine piece $z_{3} \neq 0$. From the defining equation of $T Y_{0}$,
$$d z_{3}=-\frac{z_{1}^{2}}{z_{3}^{2}} d z_{1}-\frac{z_{2}^{2}}{z_{3}^{2}} d z_{2},$$
where we are again dropping the restriction symbols. Thus,
$$\begin{aligned}
\left.\omega_{f l a t}\right|_{T Y_{0}}= & \left(1+\left|\frac{z_{1}}{z_{3}}\right|^{4}\right) d z_{1} \wedge d \bar{z}_{1}+\left(1+\left|\frac{z_{2}}{z_{3}}\right|^{4}\right) d z_{2} \wedge d \bar{z}_{2} \\
& +\left(\frac{z_{1}^{2}}{z_{3}^{2}} \frac{\bar{z}_{2}^{2}}{\bar{z}_{3}^{2}}\right) d z_{1} \wedge d \bar{z}_{2}+\left(\frac{z_{2}^{2}}{z_{3}^{2}} \frac{\bar{z}_{1}^{2}}{\bar{z}_{3}^{2}}\right) d z_{2} \wedge d \bar{z}_{1}
\end{aligned}$$
Viewing $z_{1}, z_{2}$ as local coordinates and denoting the coefficients of the Kähler form in (3.34) by $g_{i \bar{\jmath}}$, it is easy to see that $\operatorname{det}\left(g_{i \bar{\jmath}}\right) \geqslant 1$, so every component of the inverse matrix $g^{\bar{\imath} j}$ is bounded by 2 because $\left|z_{3}\right| \geqslant \max \left\{\left|z_{1}\right|,\left|z_{2}\right|\right\}$. This fact and (3.24) imply the desired estimate (3.22) for $k=0$.

To finish the proof, we also need to estimate the first covariant derivative of (3.24) with respect to $\left.\omega_{\text {flat }}\right|_{T Y_{0}}$. Applying $-z_{3}^{3}=z_{1}^{3}+z_{2}^{3}$ and $\left|z_{3}\right| \geqslant \max \left\{\left|z_{1}\right|,\left|z_{2}\right|\right\}$, we have that
$$\frac{\partial z_{3}}{\partial z_{1}}=-\frac{z_{1}^{2}}{z_{3}^{2}}=O(1), \frac{\partial z_{3}}{\partial z_{2}}=-\frac{z_{2}^{2}}{z_{3}^{2}}=O(1) .$$
Combining the claimed estimates (3.25) and (3.35), it follows from the chain rule that
$$\left|\frac{\partial \tilde{O}\left(|\sigma||z|^{-3}\right)}{\partial z_{i}}\right|+\left|\frac{\partial \tilde{O}\left(|\sigma||z|^{-3}\right)}{\partial \bar{z}_{i}}\right|=O\left(|\sigma||z|^{-4}\right) \quad(i=1,2) .$$
The remaining task is to bound the first covariant derivative of $d z_{1}, d z_{2}, d z_{3}$ with respect to $\left.\omega_{f l a t}\right|_{T Y_{0}}$. Since $g^{\bar{\imath} j}$ is bounded, it is enough to bound the second partials of $z_{1}, z_{2}, z_{3}$ and the first partials of $g_{i \bar{\jmath}}$. This can be done by differentiating (3.35) and (3.34), respectively. Because of homogeneity reasons it is clear that all of these derivatives are bounded by a constant times $|z|^{-1}$. \(\square\)

Lemma 3.13. We work on $T Y_{0}$ and abuse notation by replacing
$$\left(\Psi_{0}^{-1}\right)^{*} \omega_{K E, 0} \rightsquigarrow \omega_{K E, 0}, \quad\left(\Psi_{0}^{-1}\right)^{*} \psi_{0} \rightsquigarrow \psi_{0}, \quad\left(\Psi_{\sigma}^{-1}\right)^{*} \psi_{F S, \sigma} \rightsquigarrow \psi_{F S, \sigma} .$$
Let $N>0$ be a fixed large constant. Then for $k=0,1$ and $t \in[2 \tau,-N]$ we have that
$$\left|\nabla_{\omega_{K E, 0}}^{k} \frac{\left(\Phi_{\sigma}^{*} i \partial_{\sigma} \bar{\partial}_{\sigma}\left(\left(\Phi_{\sigma}^{-1}\right)^{*} \psi_{0}+\psi_{F S, \sigma}\right)\right)^{2}-\omega_{K E, 0}^{2}}{\omega_{K E, 0}^{2}}\right|_{\omega_{K E, 0}}=O\left(e^{-\left(\frac{1}{2}-\varepsilon\right)(t-T)}\right) .$$
Proof. Inserting one more term, we have
$$\begin{array}{r}
\Phi_{\sigma}^{*}\left(i \partial_{\sigma} \bar{\partial}_{\sigma}\left(\left(\Phi_{\sigma}^{-1}\right)^{*} \psi_{0}+\psi_{F S, \sigma}\right)\right)^{2}-\omega_{K E, 0}^{2}=\left(i \partial \bar{\partial}\left(\psi_{0}+\Phi_{\sigma}^{*} \psi_{F S, \sigma}\right)\right)^{2}-\omega_{K E, 0}^{2} \\
+\Phi_{\sigma}^{*}\left(i \partial_{\sigma} \bar{\partial}_{\sigma}\left(\left(\Phi_{\sigma}^{-1}\right)^{*} \psi_{0}+\psi_{F S, \sigma}\right)\right)^{2}-\left(i \partial \bar{\partial}\left(\psi_{0}+\Phi_{\sigma}^{*} \psi_{F S, \sigma}\right)\right)^{2} .
\end{array}$$
We begin by estimating the first line of (3.39). Canceling $i \partial \bar{\partial} \psi_{0}$, one has
$$i \partial \bar{\partial}\left(\psi_{0}+\Phi_{\sigma}^{*} \psi_{F S, \sigma}\right)-\omega_{K E, 0}=i \partial \bar{\partial}\left(\Phi_{\sigma}^{*} \psi_{F S, \sigma}-\psi_{F S, 0}\right) .$$
For 2-forms $\omega_{1}, \omega_{2}$, one has
$$\omega_{1}^{2}-\omega_{2}^{2}=2\left(\omega_{1}-\omega_{2}\right) \wedge \omega_{2}+\left(\omega_{1}-\omega_{2}\right)^{2},$$
which implies that
$$\frac{\left(i \partial \bar{\partial}\left(\psi_{0}+\Phi_{\sigma}^{*} \psi_{F S, \sigma}\right)\right)^{2}-\omega_{K E, 0}^{2}}{\omega_{K E, 0}^{2}}=2 \Delta_{\omega_{K E, 0}}\left(\Phi_{\sigma}^{*} \psi_{F S, \sigma}-\psi_{F S, 0}\right)+\frac{\left(i \partial \bar{\partial}\left(\Phi_{\sigma}^{*} \psi_{F S, \sigma}-\psi_{F S, 0}\right)\right)^{2}}{\omega_{K E, 0}^{2}} .$$
To estimate these terms, we replace the reference metric $\omega_{K E, 0}$ by $\left.\omega_{\text {flat }}\right|_{T Y_{0}}$.
Claim 3.14. For any $j \geqslant 0$ there is a positive integer $K_{j}$ such that as $|z| \rightarrow 0$,
$$\left|\nabla_{\omega_{K E, 0}}^{j}\left(\left.\omega_{\text {flat }}\right|_{T Y_{0}}\right)\right|_{\omega_{K E, 0}}=O\left(|z|^{2}|t|^{K_{j}}\right) .$$
Moreover, for $j=0$ the left-hand side is actually uniformly equivalent to $|z|^{2}|t|^{K_{0}}$.
Proof of Claim 3.14. Thanks to [10, Thm 1.4], $\omega_{\text {cusp }}$ and $\omega_{K E, 0}$ are uniformly equivalent to any order for $t \leqslant-N$, so it suffices to prove the estimate using $\omega_{\text {cusp }}$ as the reference metric.

On $T Y_{0} \backslash\{0\}$ we clearly have that $|z|^{2}=e^{t+\psi}$ for some smooth function $\psi$ on the elliptic curve $E$, viewed as a 0 -homogeneous function on $T Y_{0} \backslash\{0\}$. Thus,
$$\left.\omega_{\text {flat }}\right|_{T Y_{0}}=i \partial \bar{\partial} e^{t+\psi}=e^{t+\psi} i \partial \bar{\partial}(t+\psi)+e^{t+\psi} i \partial(t+\psi) \wedge \bar{\partial}(t+\psi) .$$
For any fixed $t_{*} \leqslant-N$, quasi-coordinates for $\omega_{\text {cusp }}$ on a neighborhood of the hypersurface $\left\{t=t_{*}\right\}$ are given by $(\rho, \check{x}, \check{y}, \check{\theta})$, where $\rho=\log |t|,(\check{x}, \check{y})=\left|t_{*}\right|^{-1 / 2}(x, y)$ for a fixed pair $(x, y)$ of linear coordinates on $E$ and $\check{\theta}=\left|t_{*}\right|^{-1} \theta$ for a fixed angular coordinate $\theta$ along the Hopf circles in $\mathbb{C}^{3}$. Moreover,
$$i \partial \bar{\partial} t=\left|t_{*}\right| \cdot(\text { a fixed } 2 \text {-form in } \check{x}, \check{y}), \partial t=-\frac{1}{2} e^{\rho} d \rho+\left|t_{*}\right| \cdot(\text { a fixed } 1 \text {-form in } \check{x}, \check{y}, \check{\theta}) .$$
Because covariant derivatives with respect to $\omega_{\text {cusp }}$ are equivalent to ordinary partial derivatives with respect to $(\rho, \check{x}, \check{y}, \check{\theta})$, the claim follows from (3.44) and (3.45). \(\square\)

We now estimate the terms on the right-hand side of (3.42). By Lemma 3.11 and Claim 3.14,
$$\begin{aligned}
& \left|\Delta_{\omega_{K E, 0}}\left(\Phi_{\sigma}^{*} \psi_{F S, \sigma}-\psi_{F S, 0}\right)\right| \\
& \leqslant\left|i \partial \bar{\partial}\left(\Phi_{\sigma}^{*} \psi_{F S, \sigma}-\psi_{F S, 0}\right)\right|_{\left.\omega_{f l a t}\right|_{T Y_{0}}} \cdot \operatorname{tr}_{\omega_{K E, 0}}\left(\left.\omega_{f l a t}\right|_{T Y_{0}}\right) \\
& =O\left(|\sigma||z|^{-3}|z|^{2}|t|^{K_{0}}\right)
\end{aligned}$$
as $|\sigma|^{-1 / 3}|z| \sim e^{(1 / 2)(t-T)} \rightarrow \infty$. Because the latter condition is satisfied for $t \in[2 \tau,-N]$, the claimed estimate (3.38) follows for the Laplacian term for $k=0$ (with a good factor of $|\sigma|^{2 / 3}$ to spare). The first derivative of this term can be estimated in a similar fashion:
$$\begin{aligned}
& \left|\nabla_{\omega_{K E, 0}}\left(\Delta_{\omega_{K E, 0}}\left(\Phi_{\sigma}^{*} \psi_{F S, \sigma}-\psi_{F S, 0}\right)\right)\right|_{\omega_{K E, 0}} \\
& \leqslant\left|\nabla_{\omega_{K E, 0}}\left(i \partial \bar{\partial}\left(\Phi_{\sigma}^{*} \psi_{F S, \sigma}-\psi_{F S, 0}\right)\right)\right|_{\omega_{K E, 0}} \\
& \leqslant\left|\nabla_{\omega_{f l a t} \mid T Y_{0}}\left(i \partial \bar{\partial}\left(\Phi_{\sigma}^{*} \psi_{F S, \sigma}-\psi_{F S, 0}\right)\right)\right|_{\omega_{f l a t} \mid T Y_{0}} \cdot\left(\operatorname{tr}_{\omega_{K E, 0}}\left(\left.\omega_{f l a t}\right|_{T Y_{0}}\right)\right)^{\frac{3}{2}} \\
& +\left|\left(i \partial \bar{\partial}\left(\Phi_{\sigma}^{*} \psi_{F S, \sigma}-\psi_{F S, 0}\right)\right)\right|_{\omega_{K E, 0}} \cdot \operatorname{tr}_{\omega_{f l a t} \mid T Y_{0}}\left(\omega_{K E, 0}\right) \cdot\left|\nabla_{\omega_{K E, 0}}\left(\left.\omega_{f l a t}\right|_{T Y_{0}}\right)\right|_{\omega_{K E, 0}} \\
& =O\left(|\sigma||z|^{-4}\left(|z|^{2}|t|^{K_{0}}\right)^{\frac{3}{2}}+|\sigma||z|^{-3}|z|^{-2}|t|^{-K_{0}}|z|^{2}|t|^{K_{1}}\right)
\end{aligned}$$
as $|\sigma|^{-1 / 3}|z| \rightarrow \infty$. This is again of the desired order with a factor of $|\sigma|^{2 / 3}$ to spare. The estimate of the quadratic term and its first derivative is very similar and we omit it.

It remains to estimate the second line of (3.39). Using (3.20) with $f=\left(\Phi_{\sigma}^{-1}\right)^{*} \psi_{0}+\psi_{F S, \sigma}$ and with reference metric $\omega=\omega_{K E, 0}$, and using Lemma 3.8 and [10, Thm 1.4] (to compare $\omega_{\text {cusp }}$ to $\omega_{K E, 0}$ ),
$$\sum_{k=0}^{1}\left|\nabla_{\omega_{K E, 0}}^{k}\left(\Phi_{\sigma}^{*} i \partial_{\sigma} \bar{\partial}_{\sigma} f-i \partial \bar{\partial} \Phi_{\sigma}^{*} f\right)\right|_{\omega_{K E, 0}} \leqslant O\left(e^{-\left(\frac{1}{2}-\varepsilon\right)(t-T)}\right) \sum_{k=1}^{3}\left|\nabla_{\omega_{\text {cusp }}}^{k} \Phi_{\sigma}^{*} f\right|_{\omega_{\text {cusp }}} .$$
We will first show that the three derivatives of $\Phi_{\sigma}^{*} f$ that appear on the right-hand side are $O(1)$.

To this end, observe that
$$\Phi_{\sigma}^{*} f=\left(\psi_{F S, 0}+\psi_{0}\right)+\left(\Phi_{\sigma}^{*} \psi_{F S, \sigma}-\psi_{F S, 0}\right) .$$
The first term is equal to the potential $\psi_{K E, 0}$ of $\omega_{K E, 0}$. Using Proposition 2.14 and quasi-coordinates for $\omega_{\text {cusp }}$, one checks that the $\omega_{\text {cusp }}$-gradient and all higher covariant derivatives of this potential are $O(1)$. For the second term in (3.49), we first show as in the proof of (3.31) that
$$\Phi_{\sigma}^{*} \psi_{F S, \sigma}-\psi_{F S, 0}=\left.\tilde{O}\left(|\sigma||z|^{-1}\right)\right|_{T Y_{0}}$$
as $|\sigma|^{-1 / 3}|z| \rightarrow \infty$, using the fact that $\psi_{F S}(z)$ is real-analytic and $O\left(|z|^{2}\right)$ as $|z| \rightarrow 0$. Second, as in (3.33)-(3.36), we use (3.50) to further estimate the covariant derivatives of this function with respect to $\left.\omega_{\text {flat }}\right|_{T Y_{0}}$. Here we also need the second covariant derivative of $\left.d z_{i}\right|_{T Y_{0}}(i=1,2,3)$, but this is seen to be bounded by a constant times $|z|^{-2}$ by the same argument as after (3.36). Thus,
$$\left|\nabla_{\omega_{f l a t} \mid T Y_{0}}^{k}\left(\Phi_{\sigma}^{*} \psi_{F S, \sigma}-\psi_{F S, 0}\right)\right|_{\omega_{f l a t} \mid T_{T} Y_{0}}=O\left(|\sigma||z|^{-1-k}\right)$$
for $k=1,2,3$ and $|\sigma|^{-1 / 3}|z| \rightarrow \infty$. Lastly, by using (3.43) and following the pattern of (3.46)-(3.47) (i.e., expanding $\nabla_{\omega_{\text {flat } \mid T_{0}}}^{k} u$ in $\omega_{\text {cusp }}$-normal coordinates and solving for $\partial^{k} u=\nabla_{\omega_{\text {cusp }}}^{k} u$ ), we get
$$\left|\nabla_{\omega_{\text {cusp }}}^{k}\left(\Phi_{\sigma}^{*} \psi_{F S, \sigma}-\psi_{F S, 0}\right)\right|_{\omega_{\text {cusp }}}=O\left(|\sigma||z|^{-1}|t|^{K}\right)=o(1)$$
for $k=1,2,3$ and $|\sigma|^{-1 / 3}|z| \rightarrow \infty$, where $K>0$. To summarize, the three derivatives of $\Phi_{\sigma}^{*} f$ on the right-hand side of (3.48) are $O(1)$, and this is sharp due to the contribution of $\nabla_{\omega_{\text {cusp }}} \psi_{K E, 0}$.

To finish the proof of the lemma, we estimate the second line of (3.39) using (3.48). To do so, let us write the second line of (3.39) as $\omega_{1}^{2}-\omega_{2}^{2}$. Then, taking norms with respect to $\omega_{K E, 0}$,
$$\left|\frac{\omega_{1}^{2}-\omega_{2}^{2}}{\omega_{K E, 0}^{2}}\right|=\left|\omega_{1}^{2}-\omega_{2}^{2}\right| \leqslant\left|\omega_{1}-\omega_{2}\right| \cdot\left(2\left|\omega_{2}\right|+\left|\omega_{1}-\omega_{2}\right|\right) .$$
We estimated $\left|\omega_{1}-\omega_{2}\right|$ in (3.48), and $\left|\omega_{2}\right|=O(1)$ because $\omega_{2}=\omega_{K E, 0}+i \partial \bar{\partial}\left(\Phi_{\sigma}^{*} \psi_{F S, \sigma}-\psi_{F S, 0}\right)$ and the $\omega_{K E, 0}$-norm of the second term was proved to be $o(1)$ in (3.46). The first derivative of the second line of (3.39) can be bounded in a similar fashion, using also (3.48) with $k=1$ and (3.47). \(\square\)

Lemma 3.15. Abuse notation by replacing $\left(\Psi_{0}^{-1}\right)^{*} \psi_{0} \rightsquigarrow \psi_{0}$ and $\left(\Psi_{\sigma}^{-1}\right)^{*} \psi_{F S, \sigma} \rightsquigarrow \psi_{F S, \sigma}$. Then:
\begin{itemize}
\item[(1)] For all $k \geqslant 0$ and $t \in[2 \tau, \tau]$, one has
$$\begin{aligned}
& \left|\nabla_{\omega_{\text {cusp }}}^{k}\left(\Phi_{\sigma}^{*} i \partial_{\sigma} \bar{\partial}_{\sigma}\left(\Phi_{\sigma}^{-1}\right)^{*} \psi_{\text {cusp }}-\Phi_{\sigma}^{*} i \partial_{\sigma} \bar{\partial}_{\sigma}\left(\Phi_{\sigma}^{-1}\right)^{*} \psi_{T}\right)\right|_{\omega_{\text {cusp }}} \\
& =O\left(|b||\tau|^{3}\right)+O\left(e^{-\left(\frac{1}{2}-\varepsilon\right)(t-T)}\right) .
\end{aligned}$$
\item[(2)] For $k=0,1$ and $t \in[2 \tau, \tau]$, one has
$$\begin{aligned}
& \left|\nabla_{\omega_{\text {cusp }}}^{k}\left(\Phi_{\sigma}^{*} i \partial_{\sigma} \bar{\partial}_{\sigma}\left(\Phi_{\sigma}^{-1}\right)^{*} \psi_{\text {cusp }}-\Phi_{\sigma}^{*} i \partial_{\sigma} \bar{\partial}_{\sigma}\left(\left(\Phi_{\sigma}^{-1}\right)^{*} \psi_{0}+\psi_{F S, \sigma}\right)\right)\right|_{\omega_{\text {cusp }}} \\
& =O\left(e^{-\delta_{0} \sqrt{-t}}\right)
\end{aligned}$$
\item[(3)] For $k=0,1$ and $t \in\left[T+T_{0}, T+2 T_{0}\right]$, one has
$$\begin{aligned}
& \left|\nabla_{|b|^{\frac{1}{2}} \omega_{\mathcal{C}, \sigma}}^{k}\left(\Phi_{\sigma}^{*} i \partial_{\sigma} \bar{\partial}_{\sigma}\left(\Phi_{\sigma}^{-1}\right)^{*} \psi_{T}-|b|^{\frac{1}{2}} \Phi_{\sigma}^{*} \omega_{T Y, \sigma}\right)\right|_{\omega_{\text {cusp }}} \\
& =O\left(e^{-\delta_{0}(t-T)^{1 / 2}}\right)+O\left(|b|^{\frac{2-k}{4}} T_{0}^{\frac{3(2-k)}{4}}\right) .
\end{aligned}$$
\end{itemize}
Proof. For item (1): By Lemma 2.24, one has for any $k \geqslant 0$ and for $t \in[2 \tau, \tau]$ that
$$\left|\nabla_{\omega_{\text {cusp }}}^{k}\left(\omega_{T}-\omega_{\text {cusp }}\right)\right|_{\omega_{\text {cusp }}} \leqslant C_{k}|b||\tau|^{3} .$$

Here $C_{k}$ does not depend on $b, \tau$. Then by the triangle inequality and Lemma 3.10,
$$\left|\nabla_{\omega_{\text {cusp }}}^{k}\left(\Phi_{\sigma}^{*} i \partial_{\sigma} \bar{\partial}_{\sigma}\left(\Phi_{\sigma}^{-1}\right)^{*} \psi_{\text {cusp }}-\Phi_{\sigma}^{*} i \partial_{\sigma} \bar{\partial}_{\sigma}\left(\Phi_{\sigma}^{-1}\right)^{*} \psi_{T}\right)\right|_{\omega_{\text {cusp }}} \leqslant C_{k}\left(|b||\tau|^{3}+e^{-\left(\frac{1}{2}-\varepsilon\right)(t-T)}\right) .$$

For item (2): By Lemma 3.10, we can replace $\Phi_{\sigma}^{*} i \partial_{\sigma} \bar{\partial}_{\sigma}\left(\Phi_{\sigma}^{-1}\right)^{*} \psi_{\text {cusp }}$ on the left-hand side of the claim by $\omega_{\text {cusp }}$ up to an error of $O\left(e^{-(1 / 2-\varepsilon)(t-T)}\right)$, which is negligible because $(t-T) /|t| \rightarrow \infty$ for $t \in[2 \tau, \tau]$. Similarly, by Lemma 3.11 and (3.43) we can replace $\Phi_{\sigma}^{*} i \partial_{\sigma} \bar{\partial}_{\sigma} \psi_{F S, \sigma}$ by $\omega_{F S, 0}$ (note that a closely related implication was already proved in (3.46)-(3.47)). Next,
$$\omega_{\text {cusp }}-\omega_{F S, 0}=\left(\omega_{\text {cusp }}-\omega_{K E, 0}\right)+i \partial \bar{\partial} \psi_{0},$$
and the first term here was estimated in Proposition 2.14. Thus, it remains to estimate
$$\left|\nabla_{\omega_{\text {cusp }}}^{k}\left(i \partial \bar{\partial} \psi_{0}-\Phi_{\sigma}^{*} i \partial_{\sigma} \bar{\partial}_{\sigma}\left(\left(\Phi_{\sigma}^{-1}\right)^{*} \psi_{0}\right)\right)\right|_{\omega_{\text {cusp }}}$$
for $k=0,1$. To do so, we use (3.20) with $\omega=\omega_{\text {cusp }}$ and $f=\left(\Phi_{\sigma}^{-1}\right)^{*} \psi_{0}$. For this we require a bound on the first three $\omega_{\text {cusp }}$-derivatives of $\Phi_{\sigma}^{*} f=\psi_{0}=\psi_{K E, 0}-\psi_{F S, 0}$. For $\psi_{K E, 0}$, such a bound, which is actually $O(1)$, follows from Proposition 2.14 using quasi-coordinates for $\omega_{\text {cusp }}$. For $\psi_{F S, 0}$, we need to go through the same steps as after (3.58): for $k=1,2,3$ and $|z| \rightarrow 0$ we clearly have that
$$\left|\nabla_{\left.\omega_{\text {flat }}\right|_{T Y_{0}}}^{k} \psi_{F S, 0}\right|_{\left.\omega_{\text {flat }}\right|_{T Y_{0}}}=O\left(|z|^{2-k}\right),$$
and hence, by (3.43) and by computations in $\omega_{\text {cusp }}$-normal coordinates, for some $K>0$,
$$\left|\nabla_{\omega_{\text {cusp }}}^{k} \psi_{F S, 0}\right|_{\omega_{\text {cusp }}}=O\left(|z|^{2}|t|^{K}\right)=o(1) .$$
In sum, all errors are negligible compared to the one from $\omega_{\text {cusp }}-\omega_{K E, 0}$, which is $O\left(e^{-\delta_{0} \sqrt{-t}}\right)$.
For item (3): Using (2.76), (2.197) and Lemma 3.10, one has for $k=0,1$,
$$\begin{aligned}
& \left|\nabla_{|b|^{\frac{1}{2}} \omega_{\mathcal{C}, \sigma}}^{k}\left(\Phi_{\sigma}^{*} i \partial_{\sigma} \bar{\partial}_{\sigma}\left(\Phi_{\sigma}^{-1}\right)^{*} \psi_{T}-|b|^{\frac{1}{2}} \Phi_{\sigma}^{*} \omega_{T Y_{\sigma}}\right)\right|_{|b|^{\frac{1}{2}} \omega_{\mathcal{C}, \sigma}} \\
& =O\left(e^{-\left(\frac{1}{2}-\varepsilon\right)(t-T)}\right)+O\left(|b|^{\frac{2-k}{4}} T_{0}^{\frac{3(2-k)}{4}}\right)+O\left(e^{-\delta_{0}(t-T)^{1 / 2}}\right) .
\end{aligned}$$
When applying (2.76), we absorb the factor $|b|^{(2-k) / 4}$ into $e^{-\delta_{0}(t-T)^{1 / 2}}$ by slightly changing $\delta_{0}$. \(\square\)

Lemma 3.16. Abuse notation by replacing $\left(\Psi_{\sigma}^{-1}\right)^{*} \Omega_{\sigma} \rightsquigarrow \Omega_{\sigma}$. Then for some $K>0$ and for all $\varepsilon>0$, for $T+T_{0} \leqslant t \leqslant-N$, for $j=0,1$ and for $\omega$ equal to either $\omega_{\text {cusp }}$ or $\omega_{T}$, it holds on $T Y_{0}$ that
$$\left|\nabla_{\omega}^{j} \log \frac{\Phi_{\sigma}^{*} \Omega_{\sigma} \wedge \Phi_{\sigma}^{*} \bar{\Omega}_{\sigma}}{\Omega_{0} \wedge \bar{\Omega}_{0}}\right|_{\omega}=O\left(|\sigma||z|^{-3}|t|^{K}\right)=O\left(e^{-\left(\frac{3}{2}-\varepsilon\right)(t-T)}\right) .$$
Proof. In the following, $z_{1}, z_{2}, z_{3}$ and $d z_{1}, d z_{2}, d z_{3}$ are automatically understood to be restricted from $\mathbb{C}^{3}$ to $T Y_{\sigma}$ or $T Y_{0}$. Similarly, $\tilde{O}(\ldots)$ as in (3.25) denotes a function on a neighborhood of the origin in $\mathbb{C}^{3}$, and we will restrict this function to $T Y_{\sigma}$ or $T Y_{0}$ without writing the restriction symbol.

By the proof of Lemma 2.19 we have for all $\sigma$ (including $\sigma=0$ ) that
$$\Omega_{\sigma}=(1+f(z)) \Omega_{T Y_{\sigma}},$$
where $f(z)$ is holomorphic on some neighborhood of the origin in $\mathbb{C}^{3}$ with $f(0)=0$. We may assume without loss of generality that $\left|z_{3}\right| \geqslant \max \left\{\left|z_{1}\right|,\left|z_{2}\right|\right\}$ at the point of $T Y_{0}$ at which we are working. Then $z_{3} \neq 0$ because $t>-\infty$. Also, $\Phi_{\sigma}(z)_{3}=z_{3}+\nu_{\sigma}(z) \bar{z}_{3}^{2} \neq 0$ because otherwise $\left|z_{3}\right|=O\left(|\sigma||z|^{-4}\right)\left|z_{3}\right|^{2}$, so $1=O\left(|\sigma||z|^{-4}\right)\left|z_{3}\right|=O\left(|\sigma||z|^{-3}\right)=o(1)$ because $t-T \rightarrow \infty$, and this is a contradiction. This means that we can use the same Poincaré residue to represent $\left.\Omega_{T Y_{0}}\right|_{z}$ and $\left.\Omega_{T Y_{\sigma}}\right|_{\Phi_{\sigma}(z)}$, i.e.,
$$\left.\Omega_{T Y_{0}}\right|_{z}=\frac{d z_{1} \wedge d z_{2}}{z_{3}^{2}},\left.\quad \Omega_{T Y_{\sigma}}\right|_{\Phi_{\sigma}(z)}=\frac{d z_{1} \wedge d z_{2}}{\Phi_{\sigma}(z)_{3}^{2}} .$$

Then from (3.26) and (3.29) we have that
$$\begin{aligned}
\Phi_{\sigma}^{*}\left(z_{i}\right) & =z_{i}+\tilde{O}\left(|\sigma||z|^{-2}\right) \\
\Phi_{\sigma}^{*}\left(d z_{1}\right) \wedge \Phi_{\sigma}^{*}\left(d z_{2}\right) & =d z_{1} \wedge d z_{2}+\sum_{|I|+|J|=2} \tilde{O}\left(|\sigma||z|^{-3}\right) d z_{I} \wedge d \bar{z}_{J}
\end{aligned}$$
where $I, J$ are multi-indices with values in $\{1,2,3\}$. Combining (3.65), (3.66) and (3.67) with
$$d z_{3}=-\frac{z_{1}^{2}}{z_{3}^{2}} d z_{1}-\frac{z_{2}^{2}}{z_{3}^{2}} d z_{2},$$
which holds identically on $T Y_{0} \cap\left\{z_{3} \neq 0\right\}$, we obtain that
$$\begin{aligned}
\frac{\Phi_{\sigma}^{*} \Omega_{\sigma} \wedge \Phi_{\sigma}^{*} \bar{\Omega}_{\sigma}}{\Omega_{0} \wedge \bar{\Omega}_{0}} & =\left|\frac{1+f\left(\Phi_{\sigma}(z)\right)}{1+f(z)}\right|^{2} \cdot \frac{\Phi_{\sigma}^{*}\left(d z_{1}\right) \wedge \Phi_{\sigma}^{*}\left(d z_{2}\right) \wedge \Phi_{\sigma}^{*}\left(d \bar{z}_{1}\right) \wedge \Phi_{\sigma}^{*}\left(d \bar{z}_{2}\right)}{d z_{1} \wedge d z_{2} \wedge d \bar{z}_{1} \wedge d \bar{z}_{2}} \cdot\left|\frac{z_{3}}{\Phi_{\sigma}^{*}\left(z_{3}\right)}\right|^{4} \\
& =\left|\frac{1+f\left(\Phi_{\sigma}(z)\right)}{1+f(z)}\right|^{2} \cdot\left(1+\operatorname{Re}\left(\tilde{O}\left(|\sigma \| z|^{-3}\right)\left[\frac{z_{1}}{z_{3}}, \frac{z_{2}}{z_{3}}\right]\right)\right) \cdot\left|1+z_{3}^{-1} \tilde{O}\left(|\sigma||z|^{-2}\right)\right|^{-4} .
\end{aligned}$$
The square bracket notation stands for a polynomial in $z_{1} / z_{3}, z_{2} / z_{3}$ with $\tilde{O}\left(|\sigma||z|^{-3}\right)$ coefficients.
We can analyze $\left|\nabla_{\omega}^{j} \log (3.69)\right|_{\omega}$ using the same technique as in the proofs of Lemmas 3.11 and 3.13: First, view $z_{1}, z_{2}$ as local coordinates on $T Y_{0} \cap\left\{z_{3} \neq 0\right\}$, represent $\left.\omega_{\text {flat }}\right|_{T Y_{0}}$ by a matrix and estimate the $\left.\omega_{\text {flat }}\right|_{T Y_{0}}$-covariant derivatives of $\log (3.69)$ in terms of its partial derivatives with respect to $z_{1}, z_{2}$. Here, the properties $-z_{3}^{3}=z_{1}^{3}+z_{2}^{3}$ and $\left|z_{3}\right| \geqslant \max \left\{\left|z_{1}\right|,\left|z_{2}\right|\right\}$ need to be used to eliminate or estimate terms that explicitly depend on $z_{3}$. The upshot is that for $j=0,1$ and $|\sigma|^{-1 / 3}|z| \rightarrow \infty$,
$$\left|\nabla_{\omega_{f l a t} \mid T Y_{0}}^{j} \log \frac{\Phi_{\sigma}^{*} \Omega_{\sigma} \wedge \Phi_{\sigma}^{*} \bar{\Omega}_{\sigma}}{\Omega_{0} \wedge \bar{\Omega}_{0}}\right|_{\left.\omega_{f l a t}\right|_{T Y_{0}}}=O\left(|\sigma||z|^{-3-j}\right) .$$
Secondly, we can rewrite (3.70) in terms of $\omega_{\text {cusp }}$ instead of $\left.\omega_{\text {flat }}\right|_{T Y_{0}}$ by using (3.43). This implies the statement of the lemma for $\omega=\omega_{\text {cusp }}$. For $\omega=\omega_{T}$ we use a reduction as in the proof of Lemma 3.8. Fix a small $\delta>0$. If $t / T \leqslant 1-\delta$, then $\omega_{T}$ and $\omega_{\text {cusp }}$ are uniformly comparable by Proposition 2.26. Thus, the version of the lemma for $\omega_{T}$ follows from the one for $\omega_{\text {cusp }}$ in this case. If $t / T \geqslant 1-\delta$, then $\omega_{T}$ is comparable to $|b|^{1 / 2} \omega_{\mathcal{C}, \sigma}$ by (2.164)-(2.165). Redoing the proof of (3.43) for $\omega_{\mathcal{C}, \sigma}$ instead of $\omega_{\text {cusp }}$ as the reference metric, it is clear that $\left.\left|\omega_{\text {flat }}\right|_{T Y_{0}}\right|_{\omega_{\mathcal{C}, \sigma}}=O\left(|z|^{2}|b|^{-L}(t-T)^{L}\right)$ for some $L>0$ if $|z| \rightarrow 0$ with $t-T \geqslant 1$. Thus, the statement of the lemma again follows from (3.70). \(\square\)

We now finally come to the proof of our main result, Theorem 3.5.
Proof of Theorem 3.5. Firstly, let us recall from (3.8) the expression of the Ricci potential:
$$\left.f_{\sigma}\right|_{\mathcal{Y}_{\sigma}}=\log \left(\frac{\omega_{g l u e, \sigma}^{2}}{\Omega_{\sigma} \wedge \bar{\Omega}_{\sigma}}\right)-\psi_{g l u e, \sigma} .$$
We will do the proof case by case by analyzing this formula.
Region $\Re_{1}$ : In this region, we have that $t>-N$. It follows from the smoothness of $\Omega_{\sigma}$ and $\psi_{F S, \sigma}$ with respect to $\sigma$ and from the Kähler-Einstein equation
$$\log \frac{\omega_{K E, 0}^{2}}{\Omega_{0} \wedge \bar{\Omega}_{0}}=\psi_{K E, 0}$$
that $\left|\nabla_{\omega_{\text {glue }, \sigma}}^{k} f_{\sigma}\right|_{\omega_{\text {glue }, \sigma}}=O(|\sigma|)$ for $k=0,1$.

Region $\Re_{2}$ : For region $\Re_{2}$, as in Lemma 3.13, we omit the pull-back map $\Psi_{\sigma}^{-1}$ for simplicity. In this region, $\tau<t<-N$. Using (3.72), we have that
$$\begin{aligned}
\Phi_{\sigma}^{*} f_{\sigma} & =\log \frac{\Phi_{\sigma}^{*}\left(i \partial_{\sigma} \bar{\partial}_{\sigma} \psi_{g l u e, \sigma}\right)^{2}}{\Phi_{\sigma}^{*} \Omega_{\sigma} \wedge \Phi_{\sigma}^{*} \bar{\Omega}_{\sigma}}+\log \frac{\Omega_{0} \wedge \bar{\Omega}_{0}}{\omega_{K E, 0}^{2}}-\psi_{0}-\Phi_{\sigma}^{*} \psi_{F S, \sigma}+\psi_{K E, 0} \\
& =\log \frac{\Phi_{\sigma}^{*}\left(i \partial_{\sigma} \bar{\partial}_{\sigma} \psi_{g l u e, \sigma}\right)^{2}}{\omega_{K E, 0}^{2}}+\log \frac{\Omega_{0} \wedge \bar{\Omega}_{0}}{\Phi_{\sigma}^{*} \Omega_{\sigma} \wedge \Phi_{\sigma}^{*} \bar{\Omega}_{\sigma}}-\Phi_{\sigma}^{*} \psi_{F S, \sigma}+\psi_{F S, 0} .
\end{aligned}$$
We estimate the three terms separately. By Lemma 3.13, for $k=0,1$, we have that
$$\left|\nabla_{\omega_{K E, 0}}^{k} \log \frac{\Phi_{\sigma}^{*}\left(i \partial_{\sigma} \bar{\partial}_{\sigma} \psi_{g l u e, \sigma}\right)^{2}}{\omega_{K E, 0}^{2}}\right|_{\omega_{K E, 0}}=O\left(e^{-\left(\frac{1}{2}-\varepsilon\right)(t-T)}\right) .$$
By Lemma 3.16, for $k=0,1$, the second term can be estimated as
$$\left|\nabla_{\omega_{K E, 0}}^{k} \log \frac{\Phi_{\sigma}^{*} \Omega_{\sigma} \wedge \Phi_{\sigma}^{*} \bar{\Omega}_{\sigma}}{\Omega_{0} \wedge \bar{\Omega}_{0}}\right|_{\omega_{K E, 0}}=O\left(e^{-\left(\frac{3}{2}-\varepsilon\right)(t-T)}\right) .$$
For the third term, for $k=0,1$, by (3.58) and Proposition 2.14,
$$\left|\nabla_{\omega_{K E, 0}}^{k}\left(\Phi_{\sigma}^{*} \psi_{F S, \sigma}-\psi_{F S, 0}\right)\right|_{\omega_{K E, 0}}=O\left(|\sigma \| z|^{-1}|t|^{K}\right)=O\left(|z|^{2} e^{-\left(\frac{3}{2}-\varepsilon\right)(t-T)}\right) .$$
Dropping the smaller terms, we get
$$\left|\nabla_{\omega_{K E, 0}}^{k} \Phi_{\sigma}^{*} f_{\sigma}\right|_{\omega_{K E, 0}}=O\left(e^{-\left(\frac{1}{2}-\varepsilon\right)(t-T)}\right)(k=0,1) .$$
Using the metric equivalence of $\Phi_{\sigma}^{*} g_{g l u e, \sigma}$ and $g_{K E, 0}$ in this region, which follows from Lemmas 3.8 and 3.10 (using also (3.52) to compare the term $\psi_{F S, \sigma}$ in $\psi_{g l u e, \sigma}$ to $\psi_{F S, 0}$ ), we conclude that
$$\left|\nabla_{\omega_{g l u e, \sigma}}^{k} f_{\sigma}\right|_{\omega_{g l u e, \sigma}}=O\left(e^{-\left(\frac{1}{2}-\varepsilon\right)(t-T)}\right)(k=0,1) .$$
Region $\Re_{4}$ : In this case $\psi_{\text {glue }, \sigma}=\left(\Phi_{\sigma}^{-1}\right)^{*} \psi_{T}$ and $\omega_{\text {glue }, \sigma}=i \partial_{\sigma} \bar{\partial}_{\sigma}\left(\Phi_{\sigma}^{-1}\right)^{*} \psi_{T}$. So we have
$$f_{\sigma}=\log \frac{\left(i \partial_{\sigma} \bar{\partial}_{\sigma} \psi_{g l u e, \sigma}\right)^{2}}{\Omega_{\sigma} \wedge \bar{\Omega}_{\sigma}}-\left(\Phi_{\sigma}^{-1}\right)^{*} \psi_{T} .$$
Hence
$$\begin{aligned}
\Phi_{\sigma}^{*} f_{\sigma} & =\log \frac{\Phi_{\sigma}^{*}\left(i \partial_{\sigma} \bar{\partial}_{\sigma} \psi_{\text {glue }, \sigma}\right)^{2}}{\Phi_{\sigma}^{*} \Omega_{\sigma} \wedge \Phi_{\sigma}^{*} \bar{\Omega}_{\sigma}}-\psi_{T} \\
& =\log \frac{\Phi_{\sigma}^{*}\left(i \partial_{\sigma} \bar{\partial}_{\sigma} \psi_{\text {glue }, \sigma}\right)^{2}}{\omega_{T}^{2}}+\log \frac{\Omega_{0} \wedge \bar{\Omega}_{0}}{\Phi_{\sigma}^{*} \Omega_{\sigma} \wedge \Phi_{\sigma}^{*} \bar{\Omega}_{\sigma}}+\log \frac{\Omega_{\mathcal{C}} \wedge \bar{\Omega}_{\mathcal{C}}}{\Omega_{0} \wedge \bar{\Omega}_{0}}+\log \frac{\omega_{T}^{2}}{\Omega_{\mathcal{C}} \wedge \bar{\Omega}_{\mathcal{C}}}-\psi_{T} .
\end{aligned}$$
By equation (2.46), the last two terms combine to zero.
Now we estimate the first three terms one by one. Using Lemma 3.10, for $j=0,1$ one has
$$\left|\nabla_{\omega_{T}}^{j}\left(\log \frac{\Phi_{\sigma}^{*}\left(i \partial_{\sigma} \bar{\partial}_{\sigma} \psi_{g l u e, \sigma}\right)^{2}}{\omega_{T}^{2}}\right)\right|_{\omega_{T}}=O\left(e^{-\left(\frac{1}{2}-\varepsilon\right)(t-T)}\right) .$$
By Lemma 3.16, for $j=0,1$, we estimate the second term by
$$\left|\nabla_{\omega_{T}}^{j}\left(\log \frac{\Phi_{\sigma}^{*} \Omega_{\sigma} \wedge \Phi_{\sigma}^{*} \bar{\Omega}_{\sigma}}{\Omega_{0} \wedge \bar{\Omega}_{0}}\right)\right|_{\omega_{T}}=O\left(e^{-\left(\frac{3}{2}-\varepsilon\right)(t-T)}\right) .$$
By (2.49) and (2.50) with $C=1$, for $j=0,1$ we estimate the third term by
$$\left|\nabla_{\omega_{T}}^{j}\left(\log \frac{\Omega_{\mathcal{C}} \wedge \bar{\Omega}_{\mathcal{C}}}{\Omega_{0} \wedge \bar{\Omega}_{0}}\right)\right|_{\omega_{T}}=O\left(e^{\frac{(1-\varepsilon) t}{2}}\right) .$$

Dropping the smaller term, one has
$$\left|\nabla_{\omega_{T}}^{j} \Phi_{\sigma}^{*} f_{\sigma}\right|_{\omega_{T}}=O\left(e^{-\left(\frac{1}{2}-\varepsilon\right)(t-T)}\right)+O\left(e^{\left(\frac{1}{2}-\varepsilon\right) t}\right)(j=0,1) .$$
Using the metric equivalence of $\Phi_{\sigma}^{*} g_{g l u e, \sigma}$ and $g_{T}$ in this region, we conclude that
$$\left|\nabla_{\omega_{\text {glue }, \sigma}}^{j} f_{\sigma}\right|_{\omega_{g l u e, \sigma}}=O\left(e^{-\left(\frac{1}{2}-\varepsilon\right)(t-T)}\right)+O\left(e^{\left(\frac{1}{2}-\varepsilon\right) t}\right)(j=0,1) .$$
Regions $\Re_{6}, \Re_{7}$ : For regions $\Re_{6}, \Re_{7}$ we estimate $f_{\sigma}$ directly on $T Y_{\sigma}$. In these two cases, one has
$$f_{\sigma}=\log \frac{\left(\mathfrak{c}|b|^{\frac{1}{2}} m_{\sigma}^{*} i \partial \bar{\partial} \psi_{T Y_{1}}\right)^{2}}{\Omega_{\sigma} \wedge \bar{\Omega}_{\sigma}}-\mathfrak{c}|b|^{\frac{1}{2}} m_{\sigma}^{*} i \partial \bar{\partial} \psi_{T Y_{1}}-\psi_{T}(T) .$$
It follows from
$$\left(m_{\sigma}^{*} i \partial \bar{\partial} \psi_{T Y_{1}}\right)^{2}=m_{\sigma}^{*} \Omega_{T Y_{1}} \wedge m_{\sigma}^{*} \bar{\Omega}_{T Y_{1}}$$
that
$$\log \frac{\left(\mathfrak{c}|b|^{\frac{1}{2}} m_{\sigma}^{*} i \partial \bar{\partial} \psi_{T Y_{1}}\right)^{2}}{\Omega_{\sigma} \wedge \bar{\Omega}_{\sigma}}-\psi_{T}(T)=\log \left(\mathfrak{c}^{2}|b|\left|F_{\sigma}\right|^{2} e^{-\psi_{T}(T)}\right),$$
where
$$F_{\sigma}:=\frac{m_{\sigma}^{*} \Omega_{T Y_{1}}}{\Omega_{\sigma}} .$$

Now we claim that
$$\mathfrak{c}^{2}|b|=e^{\psi_{T}(T)} .$$
This can easily be checked as follows: Using the fact that $\mathfrak{c}=\sqrt{2}$ in dimension $n=2$ and that
$$e^{\psi_{T}(T)+a}+b=0,$$
we see that (3.90) is equivalent to $a=-\log 2$, which follows from the equation
$$e^{-\psi_{\text {cusp }}} \omega_{\text {cusp }}^{2}=\Omega_{\mathcal{C}} \wedge \bar{\Omega}_{\mathcal{C}}=\omega_{\mathcal{C}}^{2}$$
and from the explicit form of $\psi_{\text {cusp }}, \psi_{\mathcal{C}}$ in (2.45), (2.177) respectively.
Hence
$$\log \left(\mathfrak{c}^{2}|b|\left|F_{\sigma}\right|^{2} e^{-\psi_{T}(T)}\right)=\log \left|F_{\sigma}\right|^{2} .$$
On $T Y_{1}$, if $|z| \gg 1$, then $|z|^{2}$ is uniformly comparable to $h=e^{t}$. Recall that $m_{\sigma}(z)=\sigma^{-1 / 3} z$. So on $T Y_{\sigma}$, points in regions $\Re_{6}$ and $\Re_{7}$ satisfy, for some constant $C$ independent of $\sigma$,
$$|z|^{2} \leqslant C|\sigma|^{\frac{2}{3}} e^{T_{0}}=C e^{T+T_{0}} .$$
Using Lemma 2.19, one has
$$\log \left|F_{\sigma}\right|=\log \left|\frac{m_{\sigma}^{*} \Omega_{T Y_{1}}}{\Omega_{\sigma}}\right|=\tilde{O}(|z|)=O\left(e^{\frac{T+T_{0}}{2}}\right) .$$
Noticing that $\mathfrak{c}|b|^{1 / 2} m_{\sigma}^{*} i \partial \bar{\partial} \psi_{T Y_{1}}$ is Ricci-flat, we can deduce from the Cheng-Yau gradient estimate for harmonic functions [7, p.350, Thm 6] and from (3.95) that
$$\left|\nabla_{\mathfrak{c}|b|^{\frac{1}{2}} m_{\sigma}^{*} \omega_{T Y_{1}}}\left(\log \left|F_{\sigma}\right|^{2}\right)\right|_{\mathfrak{c}|b|^{\frac{1}{2}} m_{\sigma}^{*} \omega_{T Y_{1}}}=O\left(|b|^{-\frac{1}{4}} e^{\frac{T+T_{0}}{2}}\right) .$$
Using that $|b|$ is comparable to $|T|^{-3}$, we have
$$\mathfrak{c}|b|^{\frac{1}{2}} m_{\sigma}^{*} \psi_{T Y_{1}}=O\left(\left(T_{0} /|T|\right)^{\frac{3}{2}}\right) .$$
Also, for $\log h \leqslant T_{0}$,
$$\left|\nabla_{\omega_{T Y_{1}}} \psi_{T Y_{1}}\right|_{\omega_{T Y_{1}}}=O\left(T_{0}^{\frac{3}{4}}\right),$$
and hence
$$\left.\left.\left|\nabla_{\mathfrak{c}|b|^{\frac{1}{2}} m_{\sigma}^{*} \psi_{T Y_{1}}} \mathfrak{c}\right| b\right|^{\frac{1}{2}} m_{\sigma}^{*} \psi_{T Y_{1}}\right|_{\mathfrak{c}|b|^{\frac{1}{2}} m_{\sigma}^{*} \psi_{T Y_{1}}}=O\left(|b|^{\frac{1}{4}} T_{0}^{\frac{3}{4}}\right) .$$
Thus, combining the $C^{0}$ norm and the $C^{1}$ seminorm (weighted by $\mathbf{r}_{\sigma}$ ) and dropping the smaller terms (3.95)-(3.96), we finish the proof of the case of regions $\Re_{6}$ and $\Re_{7}$.

Region $\Re_{3}$ : In this region, we glue the two Kähler-Einstein metrics $\omega_{K E, 0}$ and $\omega_{T}$. Set $\psi_{1}, \psi_{2}$ to be the expression of $\Phi_{\sigma}^{*} \psi_{\text {glue }, \sigma}$ in regions $\Re_{2}, \Re_{4}$ respectively. By (3.73) and (3.75),
$$\Phi_{\sigma}^{*} f_{\sigma}=\log \frac{\Phi_{\sigma}^{*}\left(i \partial_{\sigma} \bar{\partial}_{\sigma}\left(\left(\Phi_{\sigma}^{-1}\right)^{*}\left(\psi_{2}+\chi_{2}\left(\psi_{1}-\psi_{2}\right)\right)\right)\right)^{2}}{\omega_{K E, 0}^{2}}-\left(\psi_{2}+\chi_{2}\left(\psi_{1}-\psi_{2}\right)\right)+O\left(e^{-\left(\frac{3}{2}-\varepsilon\right)(t-T)}\right) .$$
If the error term $\chi_{2}\left(\psi_{1}-\psi_{2}\right)$ vanishes, this is exactly the case of region $\Re_{4}$, see (3.85). In general, we first apply (3.20) to change $\Phi_{\sigma}^{*} i \partial_{\sigma} \bar{\partial}_{\sigma} f$ to $i \partial \bar{\partial} \Phi_{\sigma}^{*} f$ for $f=\left(\Phi_{\sigma}^{-1}\right)^{*}\left(\psi_{2}+\chi_{2}\left(\psi_{1}-\psi_{2}\right)\right)$. Then we only need to estimate the following additional terms:
$$\frac{2 i \partial \bar{\partial} \psi_{2} \wedge i \partial \bar{\partial}\left(\chi_{2}\left(\psi_{1}-\psi_{2}\right)\right)+\left(i \partial \bar{\partial}\left(\chi_{2}\left(\psi_{1}-\psi_{2}\right)\right)\right)^{2}}{\omega_{K E, 0}^{2}}-\chi_{2}\left(\psi_{1}-\psi_{2}\right) .$$

As $t \in[2 \tau, \tau]$, we have, for all $j \geqslant 0$,
$$\left|\chi_{2}^{(j)}(t)\right| \leqslant C_{j}|\tau|^{-j} .$$
Applying the quasi-coordinates (2.109), we obtain that
$$\left|\nabla_{\omega_{K E, 0}}^{j} \chi_{2}\right| \leqslant C_{j} .$$
Combining (3.103) with the estimate of $\psi_{1}-\psi_{2}$ from Proposition 2.14 and (2.111), we deduce that
$$\left|\nabla_{\omega_{K E, 0}}^{j}\left(\chi_{2}\left(\psi_{1}-\psi_{2}\right)\right)\right| \leqslant C_{j}\left(|b||\tau|^{3}+e^{-\delta_{0} \sqrt{-t}}\right) \quad(j=0,1) .$$
Thus, since $g_{K E, 0}$ and $\Phi_{\sigma}^{*} g_{g l u e, \sigma}$ are uniformly equivalent for $t \in[2 \tau, \tau]$,
$$\left|\nabla_{\Phi_{\sigma}^{*} g_{g l u e, \sigma}}^{j}\left(\chi_{2}\left(\psi_{1}-\psi_{2}\right)\right)\right| \leqslant C_{j}\left(|b||\tau|^{3}+e^{-\delta_{0} \sqrt{-t}}\right) \quad(j=0,1) .$$
This provides the required estimate of the cutoff errors (3.101).
Region $\Re_{5}$ : The situation is similar to $\Re_{3}$. Here we glue $\mathfrak{c}|b|^{1 / 2} m_{\sigma}^{*} \omega_{T Y_{1}}$ and $\omega_{T}$. From the estimate (3.97) in region $\Re_{6}$ and elementary inequalities, we deduce that
$$\left|f_{\sigma}\right|+\mathbf{r}_{\sigma}\left|\nabla_{\omega_{g l u e, \sigma}} f_{\sigma}\right|_{\omega_{g l u e, \sigma}} \leqslant C\left(T_{0} /|T|\right)^{\frac{3}{2}}+\left|i \partial \bar{\partial}\left(\chi_{1} E\right)\right|_{|b|^{\frac{1}{2}} \omega_{\mathcal{C}}}+\mathbf{r}_{\sigma}\left|\nabla_{|b|^{\frac{1}{2}} \omega_{\mathcal{C}}} i \partial \bar{\partial}\left(\chi_{1} E\right)\right|_{|b|^{\frac{1}{2}} \omega_{\mathcal{C}}},$$
where $E(t):=\psi_{T}(t)-\psi_{T}(T)-\mathfrak{c}|b|^{\frac{1}{2}} \psi_{\mathcal{C}}(t)$ is the difference of Kähler potentials defined in (2.179). We estimate $\chi_{1} E$ as follows, using the same idea as in Proposition 2.34. Firstly, for $t-T \in\left[T_{0}, 2 T_{0}\right]$,
$$\left|\chi_{1}^{(j)}(t)\right| \leqslant C_{j} T_{0}^{-j} \quad(j \geqslant 0) .$$
Using the estimate of $E$ from (2.198), we further deduce that there exists a $C$ such that, for $t-T \in$ $\left[T_{0}, 2 T_{0}\right]$ and $j=0,1,2,3$,
$$\left|\left((t-T) \partial_{t}\right)^{j}\left(\chi_{1} E\right)\right| \leqslant C|b| T_{0}^{3} .$$
Using quasi-coordinates, we have, for $t-T \in\left[T_{0}, 2 T_{0}\right]$ and $j=0,1$,
$$\left|\nabla_{|b|^{\frac{1}{2}} \omega_{\mathcal{C}}}^{j}\left(i \partial \bar{\partial}\left(\chi_{1} E\right)\right)\right|_{|b|^{\frac{1}{2}} \omega_{\mathcal{C}}} \leqslant C|b|^{\frac{1}{4}(2-j)} T_{0}^{\frac{3}{4}(2-j)} .$$
The claimed estimate in region $\Re_{5}$ now follows from (3.106) and (3.109).
This completes the proof of Theorem 3.5. \(\square\)
3.3. Definition of the weight functions and weighted Hölder norms. We have set up the preglued manifold $\left(\mathcal{X}_{\sigma}, \omega_{g l u e, \sigma}\right)$ and the relevant Monge-Ampère equation in (3.4)-(3.6) and estimated its right-hand side, i.e., the Ricci potential $f_{\sigma}$ of $\omega_{g l u e, \sigma}$, in Theorem 3.5. In Remark 3.7 we discussed what can be said about the solution $u_{\sigma}$ using off-the-shelf arguments. This was insufficient (only) on the Tian-Yau region, motivating the development of a weighted Hölder space theory.

Definition 3.17. Fix a parameter $\delta>0$. In the rest of the paper $\delta$ will always be chosen arbitrarily close to zero. With this in mind we define two weight functions $w_{\sigma}, \tilde{w}_{\sigma}: \mathcal{X}_{\sigma} \rightarrow \mathbb{R}^{+}$as follows:
$$\begin{aligned}
& w_{\sigma}:= \begin{cases}|T|^{-\delta} & \text { on } \Psi_{\sigma}^{-1}\left(\Phi_{\sigma}(\{t>-N\})\right) \cup\left(\mathcal{X}_{\sigma} \backslash \operatorname{dom} \Psi_{\sigma}\right), \\
\Psi_{\sigma}^{*}\left(\Phi_{\sigma}^{-1}\right)^{*}\left((t-T)^{-\delta}\right) & \text { on } \Psi_{\sigma}^{-1}\left(\Phi_{\sigma}(\{t<-N\})\right), \\
1 & \text { on } \Re_{7},\end{cases} \\
& \tilde{w}_{\sigma}:=\mathbf{r}_{\sigma}^{-2} w_{\sigma} .
\end{aligned}$$

Definition 3.18. With the weight $w_{\sigma}$ from (3.110) and the regularity scale $\mathbf{r}_{\sigma}$ from (3.9) we define for all $0 \leqslant k \leqslant 4$ and for all locally $C^{k}$ functions $\phi$ on $\mathcal{X}_{\sigma}$ :
$$\|\phi\|_{C_{w}^{k}}:=\sum_{j=0}^{k}\left\|w_{\sigma}^{-1} \mathbf{r}_{\sigma}^{j}\left|\nabla_{\omega_{\text {glue }, \sigma}}^{j} \phi\right|_{\omega_{g l u e, \sigma}}\right\|_{L^{\infty}\left(\mathcal{X}_{\sigma}\right)} .$$

Moreover, for all $0 \leqslant k \leqslant 3$ and $\bar{\alpha} \in(0,1)$ and for all locally $C^{k, \bar{\alpha}}$ functions $\phi$ on $\mathcal{X}_{\sigma}$,
$$[\phi]_{C_{w}^{k, \bar{\alpha}}}:=\sup \left\{\frac{\mathbf{r}_{\sigma}(p)^{k+\bar{\alpha}}}{w_{\sigma}(p)} \frac{\left|\left(\nabla_{\omega_{\text {glue }, \sigma}}^{k} \phi\right)(p)-\left(\nabla_{\omega_{\text {glue }, \sigma}}^{k} \phi\right)(q)\right|_{\omega_{\text {glue }, \sigma}}}{d_{\omega_{\text {glue }, \sigma}}(p, q)^{\bar{\alpha}}}: 0<d_{\omega_{\text {glue }, \sigma}}(p, q)<\mathbf{r}_{\sigma}(p)\right\} .$$

Here the numerator of the difference quotient is to be understood using the trivialization of the tangent bundle in quasi-coordinates. Given this, we define
$$\|\phi\|_{C_{w}^{k, \bar{\alpha}}}:=\|\phi\|_{C_{w}^{k}}+[\phi]_{C_{w}^{k, \bar{\alpha}}} .$$

Replacing $w_{\sigma}$ by $\tilde{w}_{\sigma}$, we may similarly define a weighted $C_{\tilde{w}}^{k}$ and $C_{\tilde{w}}^{k, \bar{\alpha}}$ norm. For us, $\bar{\alpha}$ will always be an arbitrary number in $(0,1)$ whose choice affects neither the arguments nor the results.

Table 2 summarizes the behavior of the scale and weight functions and of the Ricci potential in a simplified manner (ignoring constant factors and allowing slightly suboptimal exponents). The only remaining geometric parameters are $|T| \sim|\log | \sigma|\mid$ and $| \tau \mid \sim(\log |T|)^{2}$. This information is sufficient to understand almost all of the numerology in Sections 4-5.

\begin{table}
\captionsetup{labelformat=empty}
\caption{Table 2. Regularity scale $\mathbf{r}_{\sigma}$, weights $w_{\sigma}, \tilde{w}_{\sigma}$, Ricci potential $f_{\sigma}$.}
\begin{tabular}[t]{|l|l|l|l|l|l|l|}
\hline Region & $\Re_{1}$ & $\Re_{2}$ & $\Re_{3}$ & $\Re_{4}$ & $\Re_{5} \cup \Re_{6}$ & $\Re_{7}$ \\
\hline Range of $t$ & & ( $\tau,-N$ ) & $(2 \tau, \tau)$ & $\left(T+2|T|^{\alpha}, 2 \tau\right)$ & $\left(T+\log R, T+2|T|^{\alpha}\right)$ & \\
\hline $\mathbf{r}_{\sigma}$ & 1 & 1 & 1 & $(1-t / T)^{\frac{3}{4}}$ & $(1-t / T)^{\frac{3}{4}}$ & $|T|^{-\frac{3}{4}}$ \\
\hline $w_{\sigma}$ & $|T|^{-\delta}$ & $|T|^{-\delta}$ & $|T|^{-\delta}$ & $(t-T)^{-\delta}$ & $(t-T)^{-\delta}$ & 1 \\
\hline $\tilde{w}_{\sigma}$ & $|T|^{-\delta}$ & $|T|^{-\delta}$ & $|T|^{-\delta}$ & $|T|^{\frac{3}{2}}(t-T)^{-\frac{3}{2}-\delta}$ & $|T|^{\frac{3}{2}}(t-T)^{-\frac{3}{2}-\delta}$ & $|T|^{\frac{3}{2}}$ \\
\hline $f_{\sigma}$ & $e^{-1.5|T|}$ & $e^{-0.4|T|}$ & $|\tau|^{3}|T|^{-3}$ & $|T|^{-\log |T|}$ & $|T|^{-\frac{3}{2}(1-\alpha)}$ & $|T|^{-\frac{3}{2}(1-\alpha)}$ \\
\hline
\end{tabular}
\end{table}

It is clear from standard Schauder theory on a ball of radius $\mathbf{r}_{\sigma}$ in $\mathbb{C}^{2}$ that for every $\bar{\alpha} \in(0,1)$ there exists a constant $C(\bar{\alpha})$ independent of $\sigma$ such that the linearization
$$L_{\sigma}:=\Delta_{\omega_{\text {glue }, \sigma}}-\mathrm{Id}$$
of the complex Monge-Ampère operator satisfies the estimate
$$\|\phi\|_{C_{w}^{2, \bar{\alpha}}} \leqslant C(\bar{\alpha})\left(\left\|L_{\sigma} \phi\right\|_{C_{\tilde{w}}^{0, \bar{\alpha}}}+\|\phi\|_{C_{w}^{0}}\right)$$
for all functions $\phi$. It is also clear that $L_{\sigma}$ is invertible and that we have a uniform $L^{2}$ bound for $L_{\sigma}^{-1}$, i.e., $\|\phi\|_{L^{2}} \leqslant\left\|L_{\sigma} \phi\right\|_{L^{2}}$ for all $\phi$ with respect to the $L^{2}\left(\mathcal{X}_{\sigma}, \omega_{\text {glue }, \sigma}\right)$ norm on both sides. However, we will see in Section 4 that the obvious desirable strengthening, $\|\phi\|_{C_{w}^{0}} \leqslant C\left\|L_{\sigma} \phi\right\|_{C_{\tilde{w}}^{0}}$, does not hold for all $\phi$ for any $C$ independent of $\sigma$. This requires us to introduce an obstruction space.

\section*{4. Uniform estimate of the inverse of the linearization modulo obstructions}

In Section 4.1 we construct a 1-dimensional function space $\mathbb{R} \cdot \hat{u}_{\sigma} \subset C^{\infty}\left(\mathcal{X}_{\sigma}\right)$ such that there is a chance of proving uniform weighted Hölder estimates for the inverse of the restriction of $L_{\sigma}$ to the $L^{2}\left(\mathcal{X}_{\sigma}, \omega_{\text {glue }, \sigma}\right)$-orthogonal complement of $\mathbb{R} \cdot \hat{u}_{\sigma}$. In the rest of this section, starting in Section 4.2, we then prove via a standard blowup-and-contradiction scheme that these uniform estimates are actually true. The lack of uniformity on the obstruction space $\mathbb{R} \cdot \hat{u}_{\sigma}$ will be dealt with in Section 5.
4.1. Definition of the obstruction space. We first sketch the idea: $\hat{u}_{\sigma}$ is constant to the left and zero to the right of the middle neck $\Re_{4}$, and converges in a sufficiently strong sense to $\hat{u}$, a solution to an ODE $L_{\infty} \hat{u}=0$ on the half-line $\mathbb{R}^{+}=\mathrm{GH} \lim _{\sigma \rightarrow 0} \Re_{4}$ with boundary values 1 on the left and 0 on the right. The solution $\hat{u}$ is uniquely determined by these conditions and is precisely the obstruction that breaks the obvious attempt at proving uniform estimates for $L_{\sigma}^{-1}$ via blowup and contradiction. However, going from $\hat{u}$ to $\hat{u}_{\sigma}$ turns out to be quite complicated because $\hat{u}_{\sigma}$ is not uniquely defined by the properties we need it to satisfy, so there is no canonical choice of $\hat{u}_{\sigma}$ and we need to come up with some construction that works. We now describe our solution to this problem.

The first step is to construct good coordinates on the neck $\Re_{4}$, which will be used throughout this subsection and which will allow us to state the crucial Proposition 4.2.

As in Corollary 2.29 and Proposition 2.30, we parametrize the model neck by
$$s=1-\frac{t}{T} \in(0,1) \text { and } \eta=1-s=\frac{t}{T} \in(0,1) .$$
For any $s_{1}<s_{2}$ in $(0,1)$ we introduce coordinates on the universal cover of $\left\{s_{1}<s<s_{2}\right\}$ via
$$\begin{array}{r}
\left(\check{x}_{\alpha}, \check{y}_{\alpha}, \check{x}, \check{\theta}\right):=\left(\left(-t_{*}\right)^{-\frac{1}{2}} x_{\alpha},\left(-t_{*}\right)^{-\frac{1}{2}} y_{\alpha},-t_{*} x,\left(-t_{*}\right)^{-1} \theta\right), \\
t_{*}:=\left(1-\frac{s_{1}+s_{2}}{2}\right) T, x:=-\frac{1}{t} .
\end{array}$$
Note that, as a function on the universal cover,
$$s=s(\check{x})=1-\frac{1-\frac{s_{1}+s_{2}}{2}}{\check{x}}$$
is increasing in $\check{x}$, and is uniformly smoothly bounded in the chart (4.2) if $s_{1}, s_{2}$ are fixed.
Convention 4.1. From now on we identify the middle neck $\Re_{4} \subset \mathcal{X}_{\sigma}$ with $\left\{T+2 T_{0}<t<2 \tau\right\} \subset T Y_{0}$ via the diffeomorphism $\Phi_{\sigma}^{-1} \circ \Psi_{\sigma}$. Then $s, \eta$ naturally become functions on $\Re_{4}$ and $\check{x}_{\alpha}, \check{y}_{\alpha}, \check{x}, \check{\theta}$ become functions on the universal cover of $\Re_{4}$. The range of $s$ on $\Re_{4}$ is an open interval which exhausts all of $(0,1)$ as $\sigma \rightarrow 0$. Also, the $J_{\sigma}$-Kähler metric $\omega_{g l u e, \sigma}$ on $\Re_{4}$ then has the same Kähler potential, $\psi_{T}$, as the $J_{0}$-Kähler metric $\omega_{T}$. By Lemma 3.10, the difference of the associated metric tensors $g_{g l u e, \sigma}$ and $g_{T}$ measured with respect to either of them is $O\left(e^{-(1 / 2-\varepsilon)(t-T)}\right)$ including all covariant derivatives.

In addition to defining the obstruction function $\hat{u}_{\sigma}$ (which will be done in Definition 4.9), our final goal in this subsection is to prove the following property of $\hat{u}_{\sigma}$, a key result of this paper. The main cause of complication in our definition of $\hat{u}_{\sigma}$ is the need to ensure that this is true. Recall the radial volume density $\mu_{\infty}(s)$ from Lemma 2.31 and the weight $w_{\sigma}$ from Definition 3.17.

Proposition 4.2. For $\sigma_{i} \rightarrow 0$ let $x_{i} \in \Re_{4} \subset \mathcal{X}_{\sigma_{i}}$ satisfy $s\left(x_{i}\right) \rightarrow c \in(0,1)$ and let $\psi_{i} \in C^{0}\left(\mathcal{X}_{\sigma_{i}}\right)$ satisfy $w_{\sigma_{i}}\left(x_{i}\right)\left|\psi_{i}\right| \leqslant w_{\sigma_{i}}$ on $\mathcal{X}_{\sigma_{i}}$. Assume that there exists $\psi_{\infty}:(0,1) \rightarrow \mathbb{R}$ such that for all $s_{1}<s_{2}$ in ( 0,1 ), $\psi_{i} \rightarrow \psi_{\infty} \circ s$ uniformly in the coordinates (4.2) on the universal cover of $\left\{s_{1}<s<s_{2}\right\}$. Then
$$\lim _{i \rightarrow \infty}\left|T_{i}\right|^{2} \int_{\mathcal{X}_{\sigma_{i}}} \psi_{i} \hat{u}_{\sigma_{i}} \omega_{g l u e, \sigma_{i}}^{2}=2 \pi \operatorname{Vol}(E) \int_{0}^{1} \psi_{\infty}(s) \hat{u}(s) \mu_{\infty}(s) d s$$

The remaining steps are now roughly as follows:
\begin{itemize}
\item[-] In Lemma 4.3 we prove that as $\sigma \rightarrow 0$ the operators $\left.L_{\sigma}\right|_{\Re_{4}}$ collapse to a second-order ordinary differential operator $L_{\infty}$ on the interval $s \in(0,1)$. Moreover, $L_{\infty}$ is asymptotic to an explicit model operator $L_{\infty}^{ \pm}$near each of the two endpoints.
\item[-] Fundamental solutions for $L_{\infty}^{ \pm}$can be calculated explicitly (Lemma 4.4).
\item[-] These endpoint asymptotics imply a Liouville theorem (Lemma 4.5) of independent interest: up to scalar multiples there exists a unique entire solution $\hat{u}$ to $L_{\infty} \hat{u}=0$ compatible with our weights $w_{\sigma}$, and we have that $\hat{u}(s) \rightarrow 1$ as $s \rightarrow 0^{+}$and $\hat{u}(s) \rightarrow 0$ as $s \rightarrow 1^{-}$.
\item[-] The inhomogeneous ODE $L_{\infty} \hat{v}=\hat{u}$ has a unique solution $\hat{v}$ satisfying $\hat{v}(s) \rightarrow 0$ as $s \rightarrow 1^{-}$and satisfying a Neumann type boundary condition as $s \rightarrow 0^{+}$(Lemma 4.8).
\item[-] We transplant $\hat{v}$ to a function $\hat{v}_{\sigma}$ on $\mathcal{X}_{\sigma}$ using radial cutoff functions and define $\hat{u}_{\sigma}:=L_{\sigma} \hat{v}_{\sigma}$ (Definition 4.9). These functions $\hat{u}_{\sigma}$ converge back to $\hat{u}$ as $\sigma \rightarrow 0$ (Lemma 4.10).
\item[-] Using the Neumann property of $\hat{v}$, we prove that $\hat{u}_{\sigma}$ also satisfies Proposition 4.2.
\end{itemize}
We will carry out these steps in the following sub-subsections.
4.1.1. Collapse to an ODE on an interval. The study of the limit ODE operator $L_{\infty}$ requires careful attention to various fractional exponents. We work in the general $n$-dimensional setting because the values of these exponents might look like random numbers for $n=2$.

Lemma 4.3. There exists a smooth second-order linear differential operator $L_{\infty}$ on $(0,1)$ such that:
\begin{itemize}
\item[(1)] Let $\sigma_{i} \rightarrow 0$ as $i \rightarrow \infty$. Let $\psi_{i} \in C^{2}\left(\mathcal{X}_{\sigma_{i}}\right)$ be such that for any fixed $s_{1}<s_{2}$ in (0, 1),
$$\sup _{\left\{s_{1}<s<s_{2}\right\}}\left|\psi_{i}\right|=O_{s_{1}, s_{2}}(1) \text { and } \sup _{\left\{s_{1}<s<s_{2}\right\}}\left|L_{\sigma_{i}} \psi_{i}\right|=o_{s_{1}, s_{2}}(1) \text { as } i \rightarrow \infty .$$
Then there is a smooth function $\psi_{\infty}:(0,1) \rightarrow \mathbb{R}$ such that $L_{\infty} \psi_{\infty}=0$ and, after passing to a subsequence and pulling back to the universal cover, we have for all $s_{1}<s_{2}$ that $\psi_{i} \rightarrow \psi_{\infty} \circ s$ weakly in $W_{\text {loc }}^{2, p}$ and strongly in $C_{\text {loc }}^{1, \beta}$ with respect to the coordinates (4.2) for all $p$ and $\beta$.
\item[(2)] While there is no simple formula for $L_{\infty}$ globally on (0, 1), at the endpoints we have that
$$\begin{aligned}
& L_{\infty}=\frac{1}{n+1} L_{\infty}^{+}+O\left(\eta^{n+1}\right) \text { as } \eta=1-s \rightarrow 0^{+} \\
& L_{\infty}=\frac{1}{d(n)} L_{\infty}^{-}+O\left(s^{\frac{n+1}{n}}\right) \text { as } s \rightarrow 0^{+}, d(n):=\left(\frac{n}{n+1}\right)^{\frac{1}{n}} c(n)^{\frac{n+1}{n}} .
\end{aligned}$$
Here the $O$ notation is to be understood in the sense of Definition 2.27, $c(n)$ is as in (2.90), and the two model operators $L_{\infty}^{ \pm}$are given by
$$\begin{aligned}
& L_{\infty}^{+}:=\eta^{2} \partial_{\eta \eta}^{2}-(n-1) \eta \partial_{\eta}-(n+1) \cdot \mathrm{Id}, \\
& L_{\infty}^{-}:=n s^{\frac{n-1}{n}} \partial_{s s}^{2}+(n-1) s^{-\frac{1}{n}} \partial_{s}-d(n) \cdot \mathrm{Id} .
\end{aligned}$$
\end{itemize}

Proof. The chart $\left(\check{x}, \check{\theta}, \check{x}_{\alpha}, \check{y}_{\alpha}\right)$ identifies the universal cover of $\left\{s_{1}<s<s_{2}\right\}$ with
$$\left(\frac{1-\frac{s_{1}+s_{2}}{2}}{1-s_{1}}, \frac{1-\frac{s_{1}+s_{2}}{2}}{1-s_{2}}\right) \times \mathbb{R}^{2 n-1}$$
where the interval is compactly contained in (0, 1). As recalled in Convention 4.1, $g_{g l u e, \sigma}$ and $g_{T}$ are uniformly smoothly bounded on this coordinate slab and differ from each other by
$$O\left(e^{-\left(\frac{1}{2}-\varepsilon\right)(t-T)}\right) \text { with } t-T \geqslant 2|T|^{\alpha} \text { as } \sigma \rightarrow 0,$$
including all derivatives. Also, by construction, $g_{g l u e, \sigma_{i}}, g_{T_{i}}$ and $\psi_{i}$ are invariant under the deck group $\Gamma_{i}$ of the universal cover, which preserves $\check{x}$ and acts as a discrete Heisenberg group with fundamental domain diameter $\sim\left(-t_{*, i}\right)^{-1 / 2} \sim\left|T_{i}\right|^{-1 / 2} \sim|\log | \sigma_{i}| |^{-1 / 2}$ on the coordinates $\left(\check{\theta}_{1} \check{x}_{\alpha}, \check{y}_{\alpha}\right) \in \mathbb{R}^{2 n-1}$.

By assumption, the $\Gamma_{i}$-invariant functions $\left|\psi_{i}\right|$ are uniformly bounded and the $\Gamma_{i}$-invariant functions $\left|L_{\sigma_{i}} \psi_{i}\right|$ uniformly converge to zero as $i \rightarrow \infty$. Here, $L_{\sigma_{i}}=\Delta_{\omega_{g l u e, \sigma_{i}}}-$ Id is a uniformly elliptic sequence of differential operators whose coefficients are uniformly smoothly bounded with respect to $i$. Thus, by standard $L^{p}$ elliptic regularity theory on balls, $\psi_{i}$ is locally uniformly bounded in $W^{2, p}$ for every $p \in(1, \infty)$ and hence, by Morrey embedding, in $C^{1, \beta}$ for every $\beta \in(0,1)$. By applying the Alaoglu and Arzelà-Ascoli compactness theorems and passing to a diagonal subsequence, we have that $\psi_{i} \rightarrow \psi_{\infty}$ locally weakly in $W^{2, p}$ for all $p \in(1, \infty)$ and strongly in $C^{1, \beta}$ for all $\beta \in(0,1)$. The subsequence can be taken to be independent of $s_{1}, s_{2}$ by letting $s_{1} \rightarrow 0, s_{2} \rightarrow 1$ and diagonalizing. Moreover, for any points $p, q$ in our chart with $s(p)=s(q)$, we can estimate $\left|\psi_{i}(p)-\psi_{i}(q)\right|$ as follows: Without loss of generality, $p, q$ lie in a fundamental domain of $\Gamma_{i}$ (because $\psi_{i}$ is invariant under $\Gamma_{i}$ ) and are joined by a curve $\gamma$ with $s \circ \gamma=$ const whose $\omega_{\text {glue }, \sigma_{i}}$-length is $O\left(\left(-t_{*, i}\right)^{-1 / 2}\right)=O\left(|\log | \sigma_{i}| |^{-1 / 2}\right) \rightarrow 0$. Since the gradient of $\psi_{i}$ with respect to $\omega_{g l u e, \sigma_{i}}$ is uniformly bounded, this implies that $\left|\psi_{i}(p)-\psi_{i}(q)\right|=O\left(|\log | \sigma_{i}| |^{-1 / 2}\right)$ and hence $\psi_{\infty}(p)=\psi_{\infty}(q)$. Thus, $\psi_{\infty}$ depends only on the radial coordinate $s$. This means that the first-order classical derivatives $\psi_{\infty, \check{x}_{\alpha}}, \psi_{\infty, \check{y}_{\alpha}}, \psi_{\infty, \check{\theta}}$ are identically zero, so their weak gradients, which exist locally in $L^{p}$, are zero a.e. Thus, the corresponding first-order derivatives of $\psi_{i}$ go to zero strongly in $C_{\text {loc }}^{0, \beta}$ for every $\beta$ and their gradients go to zero weakly in $L_{\text {loc }}^{p}$ for every $p$.

We now argue that $\psi_{\infty}$ is a weak, hence classical, solution of an ODE $L_{\infty} \psi_{\infty}=0$, where $L_{\infty}$ is a smooth second-order linear differential operator in $s \in(0,1)$ which is independent of the sequence $\psi_{i}$ and is asymptotically modeled by $L_{\infty}^{ \pm}$at the two endpoints. The key to this are Corollary 2.29 and Proposition 2.30. Written in terms of $\left(\eta, \check{x}_{\alpha}, \check{y}_{\alpha}, \check{\theta}\right)$, the former says that for $\eta \leqslant \delta<1$,
$$\begin{aligned}
\Delta_{\omega_{T_{i}}} & =\frac{1}{n+1}\left(\eta^{2} \partial_{\eta \eta}^{2}-(n-1) \eta \partial_{\eta}\right) \cdot e^{O_{\delta}\left(\eta^{n+1}\right)} \\
& +\check{C} \eta^{2} \partial_{\check{\theta} \check{\theta}}^{2}+\eta \check{T}+\left(-t_{*, i}\right)^{-\frac{1}{2}} \eta \check{H}_{i}+O_{\delta}\left(\left|b_{i}\right|^{\frac{1}{n+1}} \tau_{i}\right),
\end{aligned}$$
where $\check{C}>0$ is a constant, $\check{T}$ is a constant coefficient Laplacian in the $\check{x}_{\alpha}, \check{y}_{\alpha}$ coordinates on $\mathbb{R}^{2 n-2}$, and $\check{H}_{i}$ is a differential operator linear homogeneous in
$$\partial_{\check{x}_{\alpha} \check{\theta}}^{2}, \partial_{\check{y}_{\alpha} \check{\theta}}^{2},\left(-t_{*, i}\right)^{-\frac{1}{2}} \partial_{\check{\theta} \check{\theta}}^{2}$$
with coefficients that are uniformly smoothly bounded and $\Gamma_{i}$-invariant functions of $\check{x}_{\alpha}, \check{y}_{\alpha}$. Applying the identity (4.12) to $\psi_{i}$ and subtracting $\psi_{i}$, we now observe the following:
\begin{itemize}
\item[-] The left-hand side can be written as
$$\left(\Delta_{\omega_{T_{i}}}-\mathrm{Id}\right) \psi_{i}=L_{\sigma_{i}} \psi_{i}+O\left(e^{-\frac{1}{2}\left|T_{i}\right|^{\alpha}}\right) \circledast\left(\check{\partial} \psi_{i}, \check{\partial}^{2} \psi_{i}\right),$$
with $\check{\partial}$ the standard gradient operator in our fixed coordinate chart. The first term uniformly converges to zero by assumption. The second term goes to zero strongly in $L_{\text {loc }}^{p}$ for every $p$.
\end{itemize}
\begin{itemize}
\item[-] On the right-hand side, every term with at least one tangential derivative, i.e., the second line of (4.12) applied to $\psi_{i}$, goes to zero weakly in $L_{\text {loc }}^{p}$ for every $p$.
\end{itemize}

This shows that $L_{\infty} \psi_{\infty}=0$ weakly, hence classically, with $L_{\infty}+\mathrm{Id}$ the smooth ordinary differential operator in the first line of (4.12). The claim (4.6) is also clear from this. For the behavior of $L_{\infty}$ as $s \rightarrow 0^{+}$we can run a similar argument based on Proposition 2.30. \(\square\)
4.1.2. Fundamental solutions of the endpoint model operators. These are computed in Lemma 4.4. What makes our life difficult in this paper is precisely the fact that both fundamental solutions of $L_{\infty}^{-}$ are bounded as $s \rightarrow 0^{+}$: if one of them was at least $\geqslant s^{-\delta}$ for some $\delta>0$, which might be one's first guess based on experience with other singularities, then the gluing would be unobstructed.

Lemma 4.4. Recall that if $h_{1}, h_{2}$ are two fundamental solutions of a second order linear ODE, then their Wronskian is defined as $w=h_{1} h_{2}^{\prime}-h_{1}^{\prime} h_{2}$. Then the following hold.
\begin{itemize}
\item[(1)] Two fundamental solutions of $L_{\infty}^{+}$and their Wronskian are
$$h_{1}^{+}(\eta)=\eta^{n+1}, \quad h_{2}^{+}(\eta)=\eta^{-1}, \quad w^{+}(\eta)=-(n+2) \eta^{n-1} .$$
\item[(2)] Denote $\lambda=\left(\frac{4 n}{(n+1)^{2}} \cdot d(n)\right)^{1 / 2}$ with $d(n)$ defined in (4.7). Recall the modified Bessel functions $I_{\frac{1}{n+1}}, K_{\frac{1}{n+1}}$ of order $\frac{1}{n+1}$. Write $\mathbb{R}\left\{y_{1}, \ldots, y_{k}\right\}$ to denote the ring of convergent power series in $y_{1}, \ldots, y_{k}$ with real coefficients. Two fundamental solutions of $L_{\infty}^{-}$and their Wronskian are
$$\begin{aligned}
h_{1}^{-}(s)=s^{\frac{1}{2 n}} I_{\frac{1}{n+1}}\left(\lambda s^{\frac{n+1}{2 n}}\right) \in s^{\frac{1}{n}} \cdot \mathbb{R}\left\{s^{\frac{n+1}{n}}\right\} & \subset \mathbb{R}\left\{s^{\frac{1}{n}}, s^{\frac{n+1}{n}}\right\}, \\
h_{2}^{-}(s)=s^{\frac{1}{2 n}} K_{\frac{1}{n+1}}\left(\lambda s^{\frac{n+1}{2 n}}\right) \in \mathbb{R}\left\{s^{\frac{n+1}{n}}\right\}+s^{\frac{1}{n}} \cdot \mathbb{R}\left\{s^{\frac{n+1}{n}}\right\} & \subset \mathbb{R}\left\{s^{\frac{1}{n}}, s^{\frac{n+1}{n}}\right\}, \\
w^{-}(s) & =-\frac{n+1}{2 n} s^{\frac{1-n}{n}} .
\end{aligned}$$
\end{itemize}

Proof. The computations for $L_{\infty}^{+}$are straightforward. For $L_{\infty}^{-}$, a lengthy computation shows that $u(s)$ solves $L_{\infty}^{-} u=0$ if and only $u(s)=s^{\frac{1}{2 n}} v\left(\lambda \cdot s^{\frac{n+1}{2 n}}\right)$, where $v(y)$ solves the modified Bessel equation
$$y^{2} v^{\prime \prime}(y)+y v^{\prime}(y)-\left(\frac{1}{(n+1)^{2}}+y^{2}\right) v(y)=0 .$$
This yields the fundamental solutions $h_{1}^{-}(s), h_{2}^{-}(s)$ above. Their Wronskian is easily calculated using the fact that the Wronskian of the modified Bessel functions $I(y), K(y)$ (of any order) is $-\frac{1}{y}$. \(\square\)
4.1.3. A Liouville theorem for the limit ODE. The ODE $L_{\infty} u=0$ on the whole limit neck $(0,1)$ has a 2-dimensional vector space of solutions. Our goal is to prove that the weight $s^{-\delta}$ that we will impose as an upper bound in our blowup argument singles out a 1-dimensional subspace. Again, experience with other gluing problems suggests that by choosing $0<\delta \ll 1$ all solutions to $L_{\infty} u=0$ are ruled out, but here we are left with a 1-dimensional obstruction space no matter how small we choose $\delta$.

Lemma 4.5. There is a unique solution $\hat{u}(s)$ to the homogeneous $O D E L_{\infty} \hat{u}=0$ on $(0,1)$ such that $\hat{u}(s) \rightarrow 1$ as $s \rightarrow 0^{+}$and $\hat{u}(s) \rightarrow 0$ as $s \rightarrow 1^{-}$. This satisfies the following properties:
\begin{itemize}
\item[(1)] $\hat{u}(s)$ is strictly decreasing in $s$.
\item[(2)] As $\eta \rightarrow 0^{+}$we have that $\hat{u}(1-\eta)=O\left(\eta^{n+1}\right)$.
\item[(3)] As $s \rightarrow 0^{+}$we have that $\hat{u}(s)=1-C_{1} s^{\frac{1}{n}}+C_{2} s^{\frac{n+1}{n}}+R(s)$ with $C_{1}, C_{2}>0$ and
$$|R(s)|+s\left|R^{\prime}(s)\right|+s^{2}\left|R^{\prime \prime}(s)\right|=O\left(s^{\frac{n+2}{n}}\right) .$$
\item[(4)] If $L_{\infty} u=0$ and $|u(s)| \leqslant C s^{-\delta}$ for some $\delta \in(0,1)$, then $u$ is a scalar multiple of $\hat{u}$.
\end{itemize}

Proof. The uniqueness of $\hat{u}$ is clear by the maximum principle.
If $\hat{u}$ exists, then (1) can be proved as follows: First note that $\hat{u} \geqslant 0$ because otherwise there is a global interior minimum with $\hat{u}<0$ and this contradicts the maximum principle. Next, we prove that $\hat{u}$ is weakly decreasing. Otherwise there exist $s_{1}<s_{2}$ in $(0,1)$ with $\hat{u}\left(s_{1}\right)<\hat{u}\left(s_{2}\right)$. Both of these values are nonnegative by what we said before. By the intermediate value theorem, there is an $s_{2}^{\prime} \in\left(s_{2}, 1\right)$ such that $\hat{u}\left(s_{1}\right)=\hat{u}\left(s_{2}^{\prime}\right)$, but then $\hat{u}$ attains a strictly positive interior maximum on $\left[s_{1}, s_{2}^{\prime}\right]$, contradicting the maximum principle. Thus, $\hat{u}$ is weakly decreasing. Next, we prove that $\hat{u}$ is strictly decreasing. If this is false, then $\hat{u}$ must be constant on some interval $\left[s_{1}, s_{2}\right] \subset(0,1)$ with $s_{1}<s_{2}$. From the ODE, $\hat{u}=0$ on $\left[s_{1}, s_{2}\right]$. Hence $\hat{u}=0$ on ( 0,1 ) by interior analyticity, which contradicts $\hat{u}(0)=1$.

To prove the existence of $\hat{u}$, we solve $L_{\infty} \hat{u}_{\varepsilon}=0$ on $[\varepsilon, 1-\varepsilon]$ with $\hat{u}_{\varepsilon}(\varepsilon)=1$ and $\hat{u}_{\varepsilon}(1-\varepsilon)=0$ for any fixed $\varepsilon \in\left(0, \frac{1}{2}\right)$. This is possible by the standard Dirichlet problem for nonsingular ODEs. The same argument as above shows that $\hat{u}_{\varepsilon}$ is strictly decreasing, hence in particular bounded by 0 and 1. Then, also by standard ODE theory, $\hat{u}_{\varepsilon}$ satisfies uniform derivative bounds to all orders on every fixed compact interval contained in (0, 1). Thus, up to subsequences, $\hat{u}_{\varepsilon} \rightarrow \hat{u}$ locally smoothly on (0, 1), where $L_{\infty} \hat{u}=0$. The issue is to prove that $\hat{u}$ is not identically zero, and, indeed, that it satisfies the correct boundary conditions as $s \rightarrow 0$ and $s \rightarrow 1$. This will be done using a barrier argument.

First consider $\hat{u}_{\text {sub }}(s):=1-C_{1} s^{1 / n}+C_{2} s^{\gamma}$ for $C_{1}, C_{2}>0$ and $\gamma>1 / n$ to be determined. Fix an $s_{*} \in(0,1)$ such that the $O\left(s^{(n+1) / n}\right)$ in (4.7) is explicitly bounded by $C_{*} s^{(n+1) / n}$ for all $s \in\left(0, s_{*}\right]$. Here $s_{*}, C_{*}$ can be chosen to depend only on $n$. By choosing $C_{1}, C_{2}$ such that $C_{1} s_{*}{ }^{1 / n}=2$ and $C_{2} s_{*}{ }^{\gamma}=1$, we get $\hat{u}_{s u b}\left(s_{*}\right)=0$. It remains to check that $\hat{u}_{s u b}$ is a subsolution on $\left(0, s_{*}\right]$ because then the maximum principle shows that $\hat{u}_{\varepsilon} \geqslant \hat{u}_{s u b}$ on $\left[\varepsilon, s_{*}\right]$, and so $\hat{u} \geqslant \hat{u}_{s u b}$, proving that $\hat{u}$ is not identically zero and in fact $\lim _{s \rightarrow 0^{+}} \hat{u}(s)=1$. To this end we calculate on $\left(0, s_{*}\right]$, using (4.7) and the observation that $s^{1 / n}$ is a homogeneous solution of the operator $L_{\infty}+\mathrm{Id}$ :
$$L_{\infty} \hat{u}_{s u b} \geqslant\left(-1+C_{1} s^{\frac{1}{n}}-C_{2} s^{\gamma}\right)+\left(0-C_{*}^{\prime} C_{1} s^{\frac{1}{n}}\right)+\left(C_{*}^{\prime \prime} C_{2}(n \gamma-1) s^{\gamma-\frac{n+1}{n}}-C_{*}^{\prime \prime \prime} C_{2} s^{\gamma}\right) .$$
Here, $C_{*}^{\prime}>0$ depends only on $n$ while $C_{*}^{\prime \prime}, C_{*}^{\prime \prime \prime}>0$ depend on $n$ and $\gamma$. Thus, as long as $\frac{1}{n}<\gamma \leqslant \frac{n+1}{n}$, we can arrange that $(4.21) \geqslant 0$ on $\left(0, s_{*}\right]$ by making $s_{*}$ smaller if necessary. To be precise, we first let $\gamma=\frac{n+1}{n}$ and then choose $s_{*}$ so small that $C_{2}=1 / s_{*}^{\gamma}$ satisfies $C_{*}^{\prime \prime} C_{2}(n \gamma-1) \geqslant 2+2 C_{*}^{\prime}+C_{*}^{\prime \prime \prime}$.

Next, we need to prove that $\hat{u}(s) \rightarrow 0$ as $s \rightarrow 1^{-}$. In fact, by applying another barrier argument to the approximating functions $\hat{u}_{\varepsilon}$, we will prove that (2) holds. For this we again choose a $C_{*}>0$ and an $\eta_{*} \in(0,1)$ depending only on $n$ such that the $O\left(\eta^{n+1}\right)$ in (4.6) is bounded by $C_{*} \eta^{n+1}$ for all $\eta \in\left(0, \eta_{*}\right]$. Then we consider the function $\hat{u}^{\text {sup }}(1-\eta):=C_{1} \eta^{n+1}-C_{2} \eta^{\gamma}$ for $C_{1}, C_{2}>0$ and $\gamma>n+1$ to be determined. We set $C_{1} \eta_{*}^{n+1}=2$ and $C_{2} \eta_{*}^{\gamma}=1$, thus arranging that $\hat{u}^{\text {sup }}\left(1-\eta_{*}\right)=1$. To apply the maximum principle on $\left[1-\eta_{*}, 1\right)$, we need to check that $\hat{u}^{\text {sup }}$ is a supersolution for $\eta \in\left(0, \eta_{*}\right]$ after making $\eta_{*}$ smaller if necessary. For this we compute for $\eta \in\left(0, \eta_{*}\right]$ using (4.6):
$$L_{\infty} \hat{u}^{s u p} \leqslant\left(-C_{1} \eta^{n+1}+C_{2} \eta^{\gamma}\right)+\left(C_{1} \eta^{n+1}+C_{*}^{\prime} C_{1} \eta^{2 n+2}\right)+\left(-\frac{\gamma(\gamma-n)}{n+1} C_{2} \eta^{\gamma}+C_{*}^{\prime \prime \prime} C_{2} \eta^{\gamma+n+1}\right),$$
where $C_{*}^{\prime}>0$ depends only on $n$ and $C_{*}^{\prime \prime \prime}>0$ depends only on $n, \gamma$. Thus, as long as $\gamma \leqslant 2 n+2$ and $1-\gamma(\gamma-n) /(n+1)<0$ (equivalently, $\gamma>n+1$ ), we can make (4.22) $\leqslant 0$. More precisely, it is enough to set $\gamma=2 n+2$ and choose $\eta_{*}$ so small that $\left(2 C_{*}^{\prime}+C_{*}^{\prime \prime \prime}\right) \eta_{*}^{n+1} \leqslant \gamma(\gamma-n) /(n+1)-1$.