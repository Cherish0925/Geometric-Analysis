---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: Smoothing Singular Extremal Kähler Surfaces and Minimal Lagrangians]

On the compact part, we have an estimate $J_{0}-J_{t}=\mathcal{O}\left(\varepsilon^{2}\right)$. So the estimate $\left|\square_{t} \Psi_{t}\left(\Omega_{B}\right)\right|=\mathcal{O}\left(\varepsilon^{2}\right)$ on the compact domain follows.

The second part of the lemma follows. The third inequality is obvious.
For the last statement, we just notice that the same estimates hold in the case of 1-forms. We merely have to replace $\delta$ by $\delta+1$ ). So we have the estimate $\mathcal{O}\left(\varepsilon^{-\beta(\delta+1)}\right)$ on the annulus $b \leq r \leq 4 b$, the estimate $\mathcal{O}\left(\varepsilon^{4-\beta(5+\delta)}\right)$ on the annulus $4 b \leq r \leq 1$ and $\mathcal{O}\left(\varepsilon^{2}\right)$ on the compact domain. \(\square\)

Let $P_{t}: \mathcal{H}^{1,1}\left(\widehat{X}, J_{t}\right) \rightarrow \mathcal{K}_{t}^{1,1}$ be the $L^{2}$-orthogonal projection (deduced from $h_{t}$ ) on the space $\mathcal{K}_{t}^{1,1}$. Similarly, we denote $P_{t}: \mathcal{H}^{0,1}\left(\widehat{X}, J_{t}\right) \rightarrow \mathcal{K}_{t}^{0,1}$. This projection is very close to the identity in the sense of the following corollary.

Corollary 23. Suppose $-2<\delta<0$ with $\delta$ sufficiently close to -2. There exists a constant $c>0$ such that for all $\gamma_{t} \in \mathcal{H}^{1,1}\left(\widehat{X}, J_{t}\right)$
$$\left\|\gamma_{t}-P_{t}\left(\gamma_{t}\right)\right\|_{C_{\delta}^{2, \alpha}} \leq c \varepsilon^{\beta_{1}}\left\|P_{t}\left(\gamma_{t}\right)\right\|_{C_{\delta}^{2, \alpha}} .$$
Similarly, if $\gamma_{t}$ denote a family $\gamma_{t} \in \mathcal{H}^{0,1}\left(\widehat{X}, J_{t}\right)$ we have
$$\left\|\gamma_{t}-P_{t}\left(\gamma_{t}\right)\right\|_{C_{\delta+1}^{2, \alpha}} \leq c \varepsilon^{-\beta(\delta+1))}\left\|P_{t}\left(\gamma_{t}\right)\right\|_{C_{\delta+1}^{2, \alpha}} .$$
Proof. We write $P_{t}\left(\gamma_{t}\right)=\Psi_{t}\left(\Omega_{t}\right)$ and consider the form $\eta_{t}=P_{t}\left(\gamma_{t}\right)-\gamma_{t}$. By definition $\eta_{t}$ is orthogonal to $\mathcal{K}_{t}$ and $\square_{t} \eta_{t}=\square_{t} P_{t}\left(\gamma_{t}\right)=\square_{t} \Psi_{t}\left(\Omega_{t}\right)$. Lemma 22 applied to $\Psi_{t}\left(\Omega_{t}\right)$ followed by Lemma 20 and Proposition 21 give the result. \(\square\)

In conclusion, $P_{t}$ is an isomorphism and the operator norm $\left\|P_{t}-\mathrm{id}\right\|_{C_{\delta}^{2, \alpha}}$ is $\mathcal{O}\left(\varepsilon^{\beta_{1}}\right)$ (and $\mathcal{O}\left(\varepsilon^{-\beta(\delta+1)}\right)$ in the case of 1-forms) and the proposition below follows.

Proposition 24. For all $k \geq 0$ there exists a constant $c>0$ such that for all $\delta \in(-2,0)$ sufficiently close to $-2, t>0$ and every $(1,1)$-form $\beta$ orthogonal to harmonic forms on $\left(\widehat{X}, J_{t}, h_{t}\right)$, and we have
$$c\|\beta\|_{C_{\delta}^{2+k, \alpha}(t)} \leq\left\|\square_{t} \beta\right\|_{C_{\delta-2}^{k, \alpha}(t)} .$$
In the case of $(0,1)$-forms orthogonal to harmonic forms, we have a similar estimate with
$$c\|\beta\|_{C_{\delta+1}^{2+k, \alpha}(t)} \leq\left\|\square_{t} \beta\right\|_{C_{\delta-1}^{k, \alpha}(t)} .$$
3.6. Background Kähler structure. Recall that $\left(J_{t}, h_{t}\right)$ is a Hermitian structure on $\widehat{X}$. However $h_{t}$ is not a priori Kähler. We shall look for a nearby Hermitian metric which is Kähler.

For $t>0$, the Kähler form $\varpi_{t}$ of $h_{t}$ admits a decomposition of the form
$$\varpi_{t}=\varpi_{t}^{H}+\varpi_{t}^{\perp}$$
where $\varpi_{t}^{H}$ is a $\square_{t}$-harmonic (1,1)-form on $\left(\widehat{X}, J_{t}\right)$ and $\varpi_{t}^{\perp}$ is $L^{2}$-orthogonal to $\square_{t}$-harmonic forms.

From this point, one can prove that the following proposition
Proposition 25. Assuming that $\delta \in(-2,0)$ and sufficiently close to -2 , we have $\left\|\varpi_{t}-\varpi_{t}^{H}\right\|_{C_{\delta}^{2, \alpha}(\widehat{X}, t)}=\mathcal{O}\left(\varepsilon^{2}\right)$.

Proof. By definition, $\varpi_{t}-\varpi_{t}^{H}=\varpi_{t}^{\perp}$ and $\square_{t} \varpi_{t}^{\perp}=\square_{t} \varpi_{t}$. by Proposition 24, we have
$$\left\|\varpi_{t}-\varpi_{t}^{H}\right\|_{C_{\delta}^{2, \alpha}(\widehat{X}, t)}=\mathcal{O}\left(\left\|\square_{t} \varpi_{t}\right\|_{C_{\delta-2}^{0, \alpha}(\widehat{X}, t)}\right) .$$
The proposition follows from Corollary 16. \(\square\)

By definition $\bar{\partial}_{t} \varpi_{t}^{H}=0$ but it is not a priori $d$-closed. We remedy to this problem with the following lemma

Lemma 26. There exists a (1,1)-form $\gamma_{t}$ on $\left(\widehat{X}, J_{t}\right)$ in the cohomology class of $\varpi_{t}^{H}$ such that $d \gamma_{t}=0$ and $\left\|\gamma_{t}-\varpi_{t}^{H}\right\|_{C_{\delta}^{2, \alpha}(t)}=\mathcal{O}\left(\varepsilon^{2}\right)$.

Proof. Since $\left(\widehat{X}, J_{t}\right)$ is Kähler, the Frölicher exact sequence degenerates at the first page. In particular $\partial_{t} \varpi_{t}^{H}=\bar{\partial}_{t} \alpha_{t}$, for $\alpha_{t}$ a ( 2,0 )-form w.r.t $J_{t}$. Here we may choose a form such that $\bar{\partial}_{t}^{*} \alpha_{t}=0$ and $\alpha_{t}$ is orthogonal to $\square_{t}$-harmonic forms.

So $\bar{\partial}_{t} \bar{\alpha}_{t}=0$ because we are working in complex dimension 2. So $\bar{\alpha}_{t}$ defines a class in $H^{0,2}\left(\widehat{X}, J_{t}\right)$ and we can write $\bar{\alpha}_{t}=\bar{\mu}_{t}+\bar{\partial}_{t} \beta_{t}$, where $\mu_{t}$ is a holomorphic (2,0)form, $\beta_{t}$ is a (0, 1)-form orthogonal to harmonic forms which satisfies $\bar{\partial}_{t}^{*} \beta_{t}=0$. Put $\gamma_{t}=\varpi_{t}^{H}+\bar{\partial}_{t} \bar{\beta}_{t}$. Then $\bar{\partial}_{t} \gamma_{t}=\bar{\partial}_{t} \varpi_{t}^{H}=0$ and $\partial_{t} \gamma_{t}=\partial_{t} \varpi_{t}^{H}+\partial_{t} \bar{\partial}_{t} \bar{\beta}_{t}=0$.

The next step is to estimate $\beta_{t}$. Using the identities $\bar{\partial}_{t}^{*} \partial_{t} \varpi_{t}^{H}=\bar{\partial}_{t}^{*} \bar{\partial}_{t} \alpha_{t}$ and $\bar{\partial}_{t}^{*} \alpha_{t}=0$ we obtain $\bar{\partial}_{t}^{*} \partial_{t} \varpi_{t}^{H}=\square_{t} \alpha_{t}$.

Now
$$\left\|\bar{\partial}_{t}^{*} \partial_{t}\left(\varpi_{t}^{H}-\varpi_{t}\right)\right\|_{C_{\delta-2}^{0, \alpha}}=\mathcal{O}\left(\varepsilon^{2}\right)$$
according to Proposition 25. Therefore
$$\left\|\bar{\partial}_{t}^{*} \partial_{t} \varpi_{t}^{H}\right\|_{C_{\delta-2}^{0, \alpha}} \leq\left\|\bar{\partial}_{t}^{*} \partial_{t} \varpi_{t}^{H}\right\|_{C_{\delta-2}^{0, \alpha}}+\mathcal{O}\left(\varepsilon^{2}\right) .$$
Using Lemma 15 we obtain the estimate $\left\|\bar{\partial}_{t}^{*} \partial_{t} \varpi_{t}^{H}\right\|_{C_{-2}^{0, \alpha}}=\mathcal{O}\left(\varepsilon^{2}\right)$ and we deduce
$$\left\|\square_{t} \alpha_{t}\right\|_{C_{\delta-2}^{0, \alpha}}=\mathcal{O}\left(\varepsilon^{2}\right) .$$
Proposition 24 provides the estimate
$$\left\|\alpha_{t}\right\|_{C_{\delta}^{2, \alpha}}=\mathcal{O}\left(\varepsilon^{2}\right) .$$

Eventually, we would like to estimate the (0,1)-forms $\beta_{t}$. We have $\bar{\partial}_{t}^{*} \alpha_{t}=$ $\bar{\partial}_{t}^{*} \bar{\partial}_{t} \beta_{t}=\square_{t} \beta_{t}$ using the fact that $\bar{\mu}$ is harmonic and $\bar{\partial}_{t}^{*} \beta_{t}=0$.

The estimate (3.7) provides an estimate $\left\|\bar{\partial}_{t}^{*} \alpha_{t}\right\|_{C_{\delta-1}^{1, \alpha}}=\mathcal{O}\left(\varepsilon^{2}\right)$ and it follows that
$$\left\|\square_{t} \beta_{t}\right\|_{C_{\delta-1}^{1, \alpha}}=\mathcal{O}\left(\varepsilon^{2}\right) .$$
Using the fact that $\beta_{t}$ is orthogonal to harmonic forms and Proposition 24, we get the estimate
$$\left\|\beta_{t}\right\|_{C_{\delta+1}^{3, \alpha}}=\mathcal{O}\left(\varepsilon^{2}\right) .$$
In particular this implies
$$\left\|\bar{\partial}_{t} \bar{\beta}_{t}\right\|_{C_{\delta}^{2, \alpha}}=\mathcal{O}\left(\varepsilon^{2}\right)$$
which proves the lemma. \(\square\)

Thus we define the real closed form $\omega_{t}^{\prime}$ of type $(1,1)$ on $\left(\widehat{X}, J_{t}\right)$ by taking
$$\omega_{t}^{\prime}=\operatorname{Re}\left(\gamma_{t}\right)$$
were $\gamma_{t}^{\prime}$ is given by Lemma 26.
Corollary 27. Fix $-2<\delta<0$ sufficiently close to -2. Define $\omega_{t}^{\prime}$ to be the real part of $\gamma_{t}$. Then for all $t>0$ sufficiently small, $\omega_{t}^{\prime}$ defines a Kähler metric $g_{t}^{\prime}$ on $\left(\widehat{X}, J_{t}\right)$ such that $\left\|\varpi_{t}-\omega_{t}^{\prime}\right\|_{C_{\delta}^{2, \alpha}(t)}=\mathcal{O}\left(\varepsilon^{2}\right)$.

Proof. By definition we have $\left\|\varpi_{t}-\omega_{t}^{\prime}\right\|_{C_{\delta}^{2, \alpha}(t)}=\mathcal{O}\left(\varepsilon^{2}\right)$. So we only need to check that the estimate is good enough to ensure that the real (1, 1)-form $\omega_{t}^{\prime}$ defines a metric.

On the domain $\rho \leq 4 b$ of $\widehat{U}$, using the homothety $H_{\varepsilon^{-1}}$, we find an estimate
$$\left\|\omega_{\varepsilon^{-2} \eta(t)}^{\bmod }-\varepsilon^{-2}\left(H_{\varepsilon^{-1}}\right)_{*} \omega_{t}^{\prime}\right\|_{C_{\delta}^{2, \alpha}\left(\rho_{A} \leq 4 \varepsilon^{-\frac{1}{2}, t}\right)}=\mathcal{O}\left(\varepsilon^{2+\delta}\right)$$
Since $2+\delta>0$ the form $\omega_{t}^{\prime}$ is definite positive for $t$ sufficiently small. A similar estimate on the domains $4 \varepsilon^{\frac{1}{2}} \leq \rho \leq 1$ and $\widehat{X} \backslash \widehat{U}$ proves the lemma. \(\square\)

Although they need not agree, the Kähler class $\left[\omega_{t}^{\prime}\right]$ is very close to $\Omega_{t}$ according to the following result:

Lemma 28. The cohomology class $\left[\omega_{t}^{\prime}\right] \in H^{2}(\widehat{X}, \mathbb{R})$ satisfies
$$\left\|\Omega_{t}-\left[\omega_{t}^{\prime}\right]\right\|_{\delta, t}=\mathcal{O}\left(\varepsilon^{2}\right) .$$
Proof. We have the decompositions $\Omega_{t}=\Omega_{t, A}+\Omega_{t, B}$ and $\left[\omega_{t}^{\prime}\right]^{=}\left[\omega_{t}^{\prime}\right]_{A}+\left[\omega_{t}^{\prime}\right]_{B}$ together with the estimate $\left\|\omega_{t}^{\prime}-\varpi_{t}\right\|_{C_{\delta}^{2, \alpha}(t)}=\mathcal{O}\left(\varepsilon^{2}\right)$. On the ALE part, the form $\varpi_{t}$ is closed and represents $\Omega_{A, t}$. From $\left|\omega_{t}^{\prime}-\varpi_{t}\right|=\mathcal{O}\left(\varepsilon^{2+\delta}\right)$ and the fact that the spheres representing the homology classes have $\varpi_{t}$-volume $\mathcal{O}\left(\varepsilon^{2}\right)$, we deduce that
$$\left|\left[\omega_{t}^{\prime}\right]_{A}-\Omega_{t, A}\right|=\mathcal{O}\left(\varepsilon^{4+\delta}\right) .$$
On the compact part, we have $\left|\omega_{t}^{\prime}-\varpi_{t}\right|=\mathcal{O}\left(\varepsilon^{2}\right)$ and by assumption $\left|\Omega_{t, B}-\Omega_{0}\right|=$ $\mathcal{O}\left(\varepsilon^{2}\right)$. Therefore
$$\left|\left[\omega_{t}^{\prime}\right]_{B}-\Omega_{t, B}\right|=\mathcal{O}\left(\varepsilon^{2}\right) .$$
These two estimates together prove the lemma. \(\square\)
3.7. Harmonic forms and Kähler form. We shall now use the family of Kähler metrics $g_{t}^{\prime}$ with Kähler form $\omega_{t}^{\prime}$ on $\left(\widehat{X}, J_{t}\right)$ provided by Corollary 27 as our favorite background metric for some $\delta \in(-2,0)$ sufficiently close to -2. Its Laplacians will be denoted as well $\square_{t}$ and $\Delta_{t}=2 \square_{t}$.

The Mayer-Vietoris isomorphism $H^{2}(\widehat{X}) \rightarrow H^{2}(\bar{X}) \oplus H^{2}\left(\widehat{\mathbb{C}^{2} / \Gamma}\right)$, gives a corresponding decomposition $\Xi_{A} \oplus \Xi_{B}$ for each cohomology class $\Xi \in H^{2}(\widehat{X})$. The family of norms $\left\|\Xi_{A} \oplus \Xi_{B}\right\|_{\delta, t}$ defined at §3.3 provides a norm on $H^{2}(\widehat{X})$ denoted $\|\Xi\|_{\delta, t}$ as well.

Then we have the following result
Proposition 29. There are constants $c_{1}, c_{2}>0$ such that for every family $\gamma_{t}$ of $g_{t}^{\prime}$-harmonic 2-forms on $\widehat{X}$ with cohomology class $\Xi_{t}$, we have
$$c_{1}\left\|\gamma_{t}\right\|_{C_{\delta}^{0, \alpha}(t)} \geq\left\|\Xi_{t}\right\|_{t, \delta} \geq c_{2}\left\|\gamma_{t}\right\|_{C_{\delta}^{0, \alpha}(t)} .$$

Proof. The proof is done by contradiction. If the second inequality does not hold, there exists a family $t_{j} \rightarrow 0$ and $g_{t_{j}}^{\prime}$-harmonic 2-forms $\gamma_{t_{j}}$ such that $\left\|\Xi_{t_{j}}\right\|_{\delta, t_{j}} \rightarrow 0$ and $\left\|\gamma_{t_{j}}\right\|_{C_{\delta}^{0, \alpha}\left(t_{j}\right)}=1$.

Elliptic regularity gives a uniforms $C_{\delta}^{2, \alpha}$ estimate on $\gamma_{t_{j}}$ by Proposition 21. Arguing exactly as in the proof of of the second part of Proposition 21 by extracting converging subsequences, we show that either
\begin{itemize}
\item[(1)] $\Xi_{B, t_{j}}$ converges to a non vanishing cohomology class in $H^{2}(\widehat{X}, \mathbb{R})$
\item[(2)] or $\varepsilon_{j}^{-2-\delta} \Xi_{A, t_{i}}$ converges to a non vanishing cohomology class in $H^{2}(\widehat{X}, \mathbb{R})$.
\end{itemize}

This contradicts the fact that $\lim \left\|\Xi_{t_{j}}\right\|_{\delta, t_{j}}=0$.
For the first part of the inequality, a similar proof gives the result. \(\square\)

We do not control exactly the Kähler class $\left[\omega_{t}^{\prime}\right]$ of the Kähler metric $g_{t}^{\prime}$ that was just constructed. We will construct a nearby Kähler metric $g_{t}$ with the Kähler class $\Omega_{t}$ by perturbing $g_{t}^{\prime}$.

Proposition 30. For every $t>0$ sufficiently small, the $g_{t}^{\prime}$-harmonic representative $\omega_{t}$ of the Kähler class $\Omega_{t}$ defines a Kähler metric $g_{t}$, satisfying the estimate
$$\left\|\omega_{t}-\omega_{t}^{\prime}\right\|_{C_{\delta}^{2, \alpha}(t)}=\mathcal{O}\left(\varepsilon^{2}\right) .$$

Proof. According to Lemma 28
$$\left\|\Omega_{t}-\left[\omega_{t}\right]\right\|_{\delta, t}=\mathcal{O}\left(\varepsilon^{2}\right) .$$
Then by Proposition 29 one has $\left\|\omega_{t}^{\prime}-\omega_{t}\right\|_{C_{\delta}^{2, \alpha}(t)}=\mathcal{O}\left(\varepsilon^{2}\right)$. The worst value of the weight is $\varepsilon^{-\delta}$, so it implies $\varepsilon^{-\delta}\left|\omega_{t}^{\prime}-\omega_{t}\right|=\mathcal{O}\left(\varepsilon^{2}\right)$, that is
$$\left|\omega_{t}^{\prime}-\omega_{t}\right|=\mathcal{O}\left(\varepsilon^{2+\delta}\right) .$$
Since $-2<\delta<0$, this goes to zero and $\omega_{t}^{\prime}$ is a Kähler form for $t$ small enough. The proposition follows. \(\square\)

We summarize the results of the current section in the following theorem
Theorem 31. Let $\mathcal{X} \hookrightarrow \mathcal{M} \rightarrow \Delta$ be a family of deformations of a compact complex surfaces with canonical singularities. Let $\bar{\omega}$ be an orbifold Kähler metric on $\mathcal{X}$ with Kähler class $\Omega_{0}$ and $\Omega$ a family of Kähler classes supported by a simultaneous resolution $\widehat{\mathcal{X}} \rightarrow \widehat{\mathcal{M}} \rightarrow \Delta_{d}$ degenerating toward $\Omega_{0}$, such that the variation of Kähler class and complex structure non degenerate.

Let $\phi: \Delta_{d} \times \widehat{X} \rightarrow \widehat{\mathcal{M}}$ be a smooth trivialization of the family and $h_{t}$ the family of Hermitian metrics on $\left(\widehat{X}, J_{t}\right)$ with Kähler form $\varpi_{t}$ constructed at §3.2 for all $t \in \Delta_{d} \cap \mathbb{R}^{+}$sufficiently small.

Then, there exists a family of Kähler metrics $g_{t}$ with Kähler form $\omega_{t}$ on $\left(\widehat{X}, J_{t}\right)$ defined for $t \in \Delta_{d} \cap \mathbb{R}^{+}$for all $t$ sufficiently small with the property that
\begin{itemize}
\item[-] $\left[\omega_{t}\right]=\Omega_{t}$
\item[-] for all $\delta \in(-2,0)$ sufficiently close to -2, we have $\left\|\omega_{t}-\varpi_{t}\right\|_{C_{\delta}^{2, \alpha}}=\mathcal{O}\left(\varepsilon^{2}\right)$.
\end{itemize}

Proof of Proposition 11. Since $h_{t}$ converges smoothly toward $\bar{g}$ on every compact set of $X$, the proposition is an immediate corollary of Theorem 31. \(\square\)

\section*{4. CSCK metrics}

Let $\mathcal{X} \hookrightarrow \mathcal{M} \rightarrow \Delta$ be a flat deformation and $\widehat{\mathcal{X}} \hookrightarrow \widehat{\mathcal{M}} \rightarrow \Delta_{d}$ a simultaneous resolution after passing to a ramified cover. Suppose that $\mathcal{X}$ is endowed with a CSCK orbifold metric $\bar{g}$ with Kähler class $\Omega_{0}$. Let $\Omega$ be a family of Kähler classes supported by the simultaneous resolution degenerating toward $\Omega_{0}$, with non degenerate variation at each singularity.

Let $g_{t}$ be the family of Kähler metrics on $\mathcal{M}_{t}$ with Kähler class $\Omega_{t}$ obtained in § 3. In this section, we show that $g_{t}$ can be perturbed into a CSCK metric. This kind of result is now well-known by the work of Arezzo-Pacard, see also Székelyhidi whose proof is closer to ours. Our setting is slightly different, because we vary the complex structure as well. Therefore we shall give quickly some steps of the proof, but omit most technical proofs since they are similar to that in the literature.
4.1. Scalar curvature estimates. We begin by the following estimate on the scalar curvature of the Kähler metric $g_{t}^{\prime}$.

Proposition 32. Let $\kappa$ be the (constant) scalar curvature of the orbifold Kähler metric on $\bar{X}$. For all $\delta \in(-2,0)$, the Kähler metric $g_{t}^{\prime}$ with Kähler class $\Omega_{t}$ satisfies the estimate
$$\left\|\operatorname{scal}\left(g_{t}^{\prime}\right)-\kappa\right\|_{C_{\delta-2}^{0, \alpha}(t)}=\mathcal{O}\left(\varepsilon^{2}\right) .$$
Proof. As an immediate consequence of Proposition 30 and Corollary 27, we have the estimate
$$\left\|\operatorname{scal}\left(g_{t}^{\prime}\right)-\operatorname{scal}\left(h_{t}\right)\right\|_{C_{\delta-2}^{0, \alpha}(t)}=\mathcal{O}\left(\varepsilon^{2}\right) .$$
Then the proposition will be the consequence of the estimate
$$\left\|\operatorname{scal}\left(h_{t}\right)-\kappa\right\|_{C_{\delta-2}^{0, \alpha}(t)}=\mathcal{O}\left(\varepsilon^{2}\right),$$
that we now prove.
By construction $\operatorname{scal}\left(g_{B}\right)=\kappa$ on the domain $\rho_{B} \geq 4 b$ and $\operatorname{scal}\left(g_{B}\right)=\mathcal{O}(1)$ on the annulus $2 b \leq r \leq 4 b$. On the other hand $\operatorname{scal}\left(g_{A, t}\right)=0$ on the domain $R \leq b / \varepsilon$ and $\operatorname{scal}\left(g_{A, t}\right)=\mathcal{O}\left(\varepsilon^{6} b^{-6}\right)$ on the annulus $b / \varepsilon \leq R \leq 2 b / \varepsilon$. Hence the metric $\tilde{h}_{t}$ obtained by gluing together $g_{A}$ and $g_{B}$ satisfies $\left|\operatorname{scal}\left(\tilde{h}_{t}\right)\right|=\mathcal{O}\left(\varepsilon^{4} b^{-6}\right)+\mathcal{O}(1)$ on the annulus $b \leq r \leq 2 b$. Therefore $r^{2-\delta}\left|\operatorname{scal}\left(\tilde{h}_{t}\right)\right|=\mathcal{O}\left(\varepsilon^{4} b^{4-\delta}\right)+\mathcal{O}\left(b^{2-\delta}\right)=$ $\mathcal{O}\left(\varepsilon^{4-\beta(2+\delta)}\right)+\mathcal{O}\left(\varepsilon^{\beta(2-\delta)}\right)$ on the annulus. By definition $\beta \delta=2$, hence
$$\rho^{2-\delta}\left|\operatorname{scal}\left(\tilde{h}_{t}\right)-\kappa\right|=\mathcal{O}\left(\varepsilon^{4-\beta(2+\delta)}\right)+\mathcal{O}\left(\varepsilon^{2}\right)$$
on the annulus $b \leq \rho \leq 4 b$ which give an estimate
$$\left\|\operatorname{scal}\left(\tilde{h}_{t}\right)-\kappa\right\|_{C_{\delta-2}^{0, \alpha}(t)}=\mathcal{O}\left(\varepsilon^{2}\right)$$
on $\widehat{X}$ for $\delta$ sufficiently close to -2.
The metric $h_{t}$ is obtained by projecting $\tilde{h}_{t}$ onto its $J_{t}$-invariant component. The estimate (4.1) follows from the estimates on $J_{t}-J_{0}$ with a proof along the same lines of Lemma 22. \(\square\)
4.2. Construction of the metrics. It is convenient to work with the family of complex structure $J_{t}$ on a fixed smooth manifold $\widehat{X}$ as in $\S 3$. Then, we consider
$$\omega_{t, \phi}=\omega_{t}+d d_{J_{t}}^{c} \phi .$$
where $\phi$ is a function on $\widehat{X}$. If $\phi$ is small enough, $\omega_{t, \phi}$ is also the Kähler form of a Kähler metric $g_{t, \phi}$ on $\left(\widehat{X}, J_{t}\right)$ representing $\Omega_{t}$. More specifically, we have the following result:

Lemma 33. Let $C$ be a positive constant and $\delta \in(-2,0)$ sufficiently close to -2. Then for every $t>0$ sufficiently small and every function $\phi$ such that $\|\phi\|_{C_{\delta+2}^{4, \alpha}} \leq$ $C \varepsilon^{2-\beta(\delta+2)}$, the form $\omega_{t, \phi}$ is definite positive.

Proof. We deduce an estimate $\left\|\omega_{t}-\omega_{t, \phi}\right\|_{C_{\delta}^{2, \alpha}}=\mathcal{O}\left(\varepsilon^{2-\beta(\delta+2)}\right)$. The worst value of the weight is $\varepsilon^{-\delta}$ so we have an estimate $\varepsilon^{-\delta}\left|\omega_{t}-\omega_{t, \phi}\right|=\mathcal{O}\left(\varepsilon^{2-\beta(\delta+2)}\right)$, hence $\left|\omega_{t}-\omega_{t, \phi}\right|=\mathcal{O}\left(\varepsilon^{(1-\beta)(\delta+2)}\right)$. Since $(1-\beta)(\delta+2)>0, \omega_{\phi, t}$ is definite positive for $t$ sufficiently small. \(\square\)

We want to solve the equation
$$\operatorname{scal}\left(g_{t, \phi}\right)=c s t$$
where $\operatorname{scal}\left(g_{t, \phi}\right)$ is the scalar curvature of the metric $g_{t, \phi}$. The linearization of this equation at $\phi=0$ is given by a fourth order elliptic operator $L_{t}$, the Lichnerowicz operator. The idea is to apply a suitable version of the implicit function theorem in order to solve (4.2).

Proposition 34. Suppose that $\mathcal{X}$ does not carry any nontrivial holomorphic vector field. If $-2<\delta<0$, then for sufficiently small $t>0$ the operator
$$\begin{aligned}
P_{t}: \mathbb{R} \times C_{\delta+2}^{4, \alpha}(\widehat{X}, t) & \rightarrow C_{\delta-2}^{0, \alpha}(\widehat{X}, t) \\
(v, \phi) & \mapsto v+L_{t} \phi
\end{aligned}$$
admits a right inverse $Q_{t}$ with norm satisfying $\left\|Q_{t}\right\| \leq c \varepsilon^{-\beta(\delta+2)}$ for some constant $c$ independent of $t$.

From that and the initial control on the scalar curvature, it follows:
Corollary 35. Suppose that $\mathcal{X}$ does not carry any nontrivial holomorphic vector field. For all $\delta \in(-2,0)$ sufficiently close to -2, there exists a constant $C>0$ such that for all $t>0$ sufficiently small, there is a unique solution $\phi_{t}$, up to a constant, to the equation $\operatorname{scal}\left(g_{t, \phi}\right)=\operatorname{cst}$ with the condition that $\left\|\phi_{t}\right\|_{C_{\delta+2}^{4, \alpha}} \leq C \varepsilon^{2-\beta(\delta+2)}$.

Proof. We solve the problem via the fixed point method. The equation we are interested in can be written $\operatorname{scal}\left(g_{t, \phi}\right)+v=\kappa_{0}$, which can be written
$$P_{t}(v, \phi)+N(v, \phi)=\kappa-\operatorname{scal}\left(h_{t}\right)$$
where $N$ is the non linear term of the equation.
We are looking for a solution of the form $(v, \phi)=Q_{t}(f)$ and the equation reads
$$f=\kappa-\operatorname{scal}\left(h_{t}\right)-N_{t} \circ Q_{t}(f)=: T_{t}(f) .$$
Applying the fixed point theorem, the Corollary is a consequence of the following claim.

Claim. There exists $C>0$, such that for all $t>0$ sufficiently small, the operator $T_{t}$ maps the ball $\|f\|_{C_{\delta-2}^{0, \alpha}} \leq C \varepsilon^{2}$ to itself and is $\frac{1}{2}$-contractant.
Let us now prove the claim. The map $N_{t}(v, \phi)$ depends only on $\phi$ so we can write it $N_{t}(\phi)$. Then there exists $c_{2}, C_{2}>0$ such that if
$$\|\phi\|_{C_{2}^{4, \alpha}},\|\psi\|_{C_{2}^{4, \alpha}} \leq c_{2},$$
then
$$\left\|N_{t}(\phi)-N_{t}(\psi)\right\|_{C_{\delta-2}^{0, \alpha}} \leq C_{2}\left(\|\phi\|_{C_{2}^{4, \alpha}}+\|\psi\|_{C_{2}^{4, \alpha}}\right)\|\phi-\psi\|_{C_{\delta+2}^{4, \alpha}}$$
(cf. [12, Lemma 19] and notice that the condition $\delta<0$ required there is not needed).

By Proposition 32,
$$\left\|\operatorname{scal}\left(h_{t}\right)-\kappa\right\|_{C_{S-2}^{0, \alpha}} \leq \frac{1}{2} C \varepsilon^{2}$$
for some constant $C>0$. Using Proposition 34, the bound $\|f\|_{C_{\delta-2}^{0, \alpha}} \leq C \varepsilon^{2}$ gives on $\phi=Q_{t} f$ a bound $\|\phi\|_{C_{+2}^{4, \alpha}} \leq C \varepsilon^{2-\beta(\delta+2)}$ and we deduce that
$$\|\phi\|_{C_{2}^{4, \alpha}} \leq C \varepsilon^{2+\delta-\beta(\delta+2)}=C \varepsilon^{(\delta+2)(1-\beta)}$$
Since $\delta+2>0$ and $1-\beta>0$, we conclude that $\|\phi\|_{C_{2}^{4, \alpha}}=o(1)$. Using (4.5), we deduce that for $t>0$ small enough, the map $T_{t}$ is 1/2-contractant on the ball $\|f\|_{C_{\delta-2}^{0, \alpha}} \leq C \varepsilon^{2}$. The map $T_{t}$ preserves the ball since
$$\begin{aligned}
\left\|T_{t}(f)\right\|_{C_{\delta-2}^{0, \alpha}} & \leq\left\|T_{t}(f)-T_{t}(0)\right\|_{C_{\delta-2}^{0, \alpha}}+\left\|T_{t}(0)\right\|_{C_{\delta-2}^{0, \alpha}} \\
& \leq \frac{1}{2}\|f\|_{C_{\delta-2}^{0, \alpha}}+\left\|\operatorname{scal}\left(h_{t}\right)-\kappa\right\|_{C_{\delta-2}^{0, \alpha}} \\
& \leq C \varepsilon^{2} .
\end{aligned}$$ \(\square\)

Proof of Proposition 34. This proposition is close to [12, Proposition 20], with the difference that the complex structure is deformed and the sign of the weight $\delta+2$ is opposite to that of [12]. The change of complex structure just gives an additional error term in the estimates so is not a substantial change. The choice of opposite sign of the weight is more important, and we explain briefly how to deal with it.

In this kind of problem, one obtains a right inverse for $P_{t}$ by gluing a right inverse on the ALE space $Y_{t}$ with a right inverse on the orbifold part $\mathcal{X}$. The point is that we consider the weight $\delta+2>0$. This immediately implies that on the ALE space $Y_{t}$, the operator
$$L: C_{\delta+2}^{4, \alpha} \longrightarrow C_{\delta-2}^{\alpha}$$
is surjective (by duality the cokernel is the kernel of $L$ in $C_{-\delta-2}^{4, \alpha}$, which is 0 because $-\delta-2<0$ ).

Dually, the same operator $L: C_{\delta+2}^{4, \alpha} \longrightarrow C_{\delta-2}^{\alpha}$ on the orbifold has no kernel since $\delta+2>0$ rules out the constants near the punctures, and $\mathcal{X}$ has no holomorphic vector field. But $L$ has a cokernel: since $L$ is selfadjoint, index theory in weighted
spaces gives that the index of $L$ is the opposite of the number of punctures $k$. Define a space $\hat{C}_{\delta+2}^{4, \alpha}=C_{\delta+2}^{4, \alpha} \oplus \mathbb{R}^{k}$ of functions of the form
$$u+\sum_{1}^{k} \lambda_{i} \chi_{i}, \quad u \in C_{\delta+2}^{4, \alpha},\left(\lambda_{i}\right) \in \mathbb{R}^{k}$$
where $\chi_{i}$ is a cutoff function which vanishes outside a small ball around the puncture $x_{i}$. For example, we can equip the space $\hat{C}_{\delta+2}^{4, \alpha}$ with the norm
$$\|f\|_{\hat{C}_{\delta+2}^{4, \alpha}}=\sum_{1}^{k}\left|f\left(x_{i}\right)\right|+\|d f\|_{C_{\delta+1}^{3, \alpha}} .$$
Then saying that $L$ has index $-k$ translates to the fact that
$$\tilde{L}: \mathbb{R}^{k} \oplus \hat{C}_{\delta+2}^{4, \alpha} \longrightarrow C_{\delta-2}^{\alpha}$$
has index 0 . Since its kernel is now reduced to the constants, its cokernel is also reduced to the constants.

Now an inverse for this operator (orthogonally to the constants), combined with the inverses of the operators at the punctures, can be used to construct an approximate right inverse for $P_{t}$. One deduces that $P_{t}$ has a right inverse $Q_{t}$. The only tricky point is to estimate the norm $\left\|Q_{t}\right\|$, because of the constants at the punctures which appear in the space $\hat{C}_{\delta+2}^{4, \alpha}$. These constants are bounded in the space $\hat{C}_{\delta+2}^{4, \alpha}$, but on the glued manifold, they blow up in the $C_{\delta+2}^{4, \alpha}$ norm. Since they are cut around the radius $r=\varepsilon^{\beta}$, they contribute at most by a factor $\left(\varepsilon^{\beta}\right)^{-2-\delta}=$ $\varepsilon^{-\beta(\delta+2)}$ which explains the norm estimate given for $Q_{t}$ in the statement of the proposition. \(\square\)

\section*{5. Hamiltonian stationary spheres}

We now construct the Hamiltonian stationary spheres and prove Theorem D in the case of canonical singularities. The spheres are obtained as deformations of a Lagrangian sphere in the tangent graviton, which is holomorphic for another complex structure in the hyperKähler family, so is Hamiltonian stationary.
5.1. Deformation theory. As we shall now see, the deformation theory of Hamiltonian stationary spheres is our case is very simple. Let us remind some basic facts about Hamiltonian stationary surfaces in a Kähler 4-manifold $(X, \omega)$. A Hamiltonian stationary surface is a Lagrangian surface which is a critical point of the area for Hamiltonian deformations. This gives an equation that can be written in the following way: given an embedded surface $\iota_{S}: S \subset X$, let $H$ be its mean curvature vector and $\alpha=H\lrcorner \omega$, then $\alpha_{S}=\iota_{S}^{*} \alpha$ is a 1-form on $S$ satisfying the equation $d \alpha_{S}=\iota_{S}^{*}$ Ric. Then $S$ is Hamiltonian stationary if on $S$ one has
$$\delta \alpha_{S}=0 .$$

In the hyperKähler case, one has $\alpha_{S}=-d \theta$, where $\theta$ is the phase defined from the holomorphic symplectic form $\Omega$ by $\iota_{S}^{*} \Omega=e^{i \theta} d V o l_{g_{S}}$, and the equation is equivalent to $\Delta \theta=0$. If $S$ is holomorphic for another complex structure in the hyperKähler family, then $S$ is minimal so obviously Hamiltonian stationary. Moreover, in that case, one obtains readily that the linearization of the equation is given by $f \mapsto \Delta_{S}^{2} f$, where the infinitesimal deformations are parameterized by a function $f$ on $S$ (the graph of $d f$ in $T^{*} S$ giving the infinitesimal Lagrangian
deformation). The important point here is that this linearization is automatically an isomorphism
$$C^{k, \alpha}(S) / \mathbb{R} \longrightarrow C_{0}^{k-4, \alpha}(S),$$
where $C_{0}$ denote the functions $f$ on $S$ such that $\int_{S} f d V o l_{g_{S}}=0$, and the quotient by $\mathbb{R}$ is natural since constants give trivial deformations. From this we deduce immediately the following lemma:

Lemma 36. Suppose $S$ is a Lagrangian sphere in a hyperKähler 4-manifold $(X, \omega)$, which is holomorphic with respect to one of the complex structures of $X$. If $(Y, \xi)$ is a Kähler manifold, sufficiently close to $(X, \omega)$ in $C^{2, \alpha}$ norm, such that $[S]$ remains a Lagrangian homology class for $\xi([\xi][S]=0)$, then in $(Y, \xi)$, in a small $C^{3, \alpha}$ neighborhood of $S$, there exists a unique Hamiltonian stationary sphere $T$ such that $[T]=[S]$.

Proof. The proof relies on two facts: if the homology class remains Lagrangian, it can be represented by a nearby Lagrangian surface ; and the linearization under Hamiltonian deformations is an isomorphism (see above). So the proof is standard, but we give a short argument where the two aspects are treated simultaneously.

We look at maps $f: S \rightarrow X$ which are deformations of the given inclusion $\iota_{S}: S \subset X$, and consider the operator
$$\left.\Phi(f, \xi)=\left(f^{*} \xi, \delta_{f^{*} g_{\xi}}\left(H_{f, \xi}\right\lrcorner \xi\right)\right),$$
for $\xi$ a nearby Kähler structure (the complex structure is also deformed), and $H_{f, \xi}$ denotes the mean curvature vector of $f(S)$ for the metric $\xi$. It is clear that $f(S)$ is Lagrangian stationary if and only if $\Phi(f)=0$.

A tangent vector to the space of maps $f: S \rightarrow X$ is a section $n$ of the normal bundle of $S$, but we find more convenient to represent it by the 1-form $\alpha=n\lrcorner \omega$ on $S$. Then at the inclusion $\iota_{S}$ one has
$$\frac{\partial \Phi}{\partial f}(\alpha)=(d \alpha, \delta \Delta \alpha) .$$
To avoid the difference of the orders of the differential operators, we consider instead of $\Phi$ the operator
$$\left.\Psi(f, \xi)=\left(f^{*} \xi, \Delta_{f^{*} g_{\xi}}^{-1} \delta_{f^{*} g_{\xi}}\left(H_{f, \xi}\right\lrcorner \xi\right)\right),$$
so that
$$\frac{\partial \Psi}{\partial f}(\alpha)=\left(d \alpha, \Delta^{-1} \delta \Delta \alpha\right)=(d \alpha, \delta \alpha) .$$
Then $\Psi$ is a smooth operator $C^{3, \eta} \times C^{2, \eta} \rightarrow C_{0}^{2, \eta} \times C_{0}^{2, \eta}$, where each time the index 0 means with zero integral over $S$ (for the metric $f^{*} g_{\xi}$ ); here we have used the hypothesis that $\Sigma$ remains Lagrangian, so $\int_{S} f^{*} \xi=0$. The differential $\frac{\partial \Psi}{\partial f}$ is obviously an isomorphism at $(f, \xi)=\left(\iota_{S}, \omega\right)$, since it identifies with $d+\delta$ : $\Omega^{1}(S) \rightarrow \Omega^{2}(S)_{0}+\Omega^{0}(S)_{0}$. The result is a consequence of the implicit function theorem. \(\square\)

This lemma is useful because of the following remark:
Lemma 37. If $Y_{\zeta}$ is a gravitational instanton for some $\zeta=\left(\zeta_{1}, \zeta_{2}, \zeta_{3}\right) \in \mathfrak{h} \otimes \mathbb{R}^{3}$, and $\theta$ is a positive root such that $\zeta_{1} \in \operatorname{ker} \theta$, then the Lagrangian homology class corresponding to $\theta$ is represented by a holomorphic cycle for a complex structure orthogonal to $I_{1}$ (and therefore Lagrangian for $I_{1}$ ).

Proof. Because $\theta\left(\zeta_{1}\right)=0$, there exists an angle $\varphi$, such that
$$u=\left(\begin{array}{ccc}
0 & -\cos \varphi & \sin \varphi \\
1 & 0 & 0 \\
0 & \sin \varphi & \cos \varphi
\end{array}\right) \in S O_{3}$$
sends $\zeta$ to $\xi=\left(\xi_{1}, \xi_{c}\right)$ such that $\theta\left(\xi_{c}\right)=0$. By the second statement in Lemma 6, the homology class corresponding to $\theta$ is represented by a holomorphic cycle for the complex structure $u^{-1}\left(I_{1}\right)=-\cos \varphi I_{2}+\sin \varphi I_{3}$. \(\square\)

Together with Lemma 36 we deduce:
Corollary 38. Under the hypotheses of Theorem $C$, fix a singular point $x \in \mathcal{X}$, with tangent graviton $Y_{\zeta_{r}, \zeta_{c}}$. Let $\theta$ be a positive root, such that $\zeta \in \operatorname{ker} \theta$ and $\theta$ is primitive for this property, so that $\Sigma$ is represented in $Y_{\zeta_{r}, \zeta_{c}}$ by a Hamiltonian stationary sphere $S_{0}$ (Lemma 6). Finally suppose that the 2-homology class $\Sigma \in$ $H_{2}\left(\widehat{\mathcal{M}}_{t}, \mathbb{Z}\right)$ defined by $\theta$ remains Lagrangian, that is $\Omega_{t} \cdot \Sigma=0$.

If $\omega_{t}$ is the CSCK metric on $X_{t}$ in the class $\Omega_{t}$, then for $t$ small enough, $\Sigma$ can be represented by a Lagrangian stationary sphere, close to $S_{0}$.

Here we use that $\omega_{t}$ is a CSCK metric only through the estimates that it satisfies. The conclusion holds also for every metric in the class $\Omega_{t}$ satisfying the same estimates; the CSCK metric is a canonical example of such a metric.

Proof. We blow up the metrics $\omega_{t}$ : from Corollary 35, on every compact, the Kähler metrics $\frac{\omega_{t}}{t^{p}}$ converge to the gravitational instanton $Y_{\zeta_{r}, \zeta_{c}}$ in $C^{2, \alpha}$ (actually in $C^{\infty}$ ). Then we apply Lemma 36. \(\square\)
5.2. Minimizing property. We now prove the minimizing property of the spheres that we constructed, which is stated in Theorem D. The idea is that a sequence of minimizers in the homotopy class must converge to a minimizer in the tangent graviton $Y_{\zeta_{1}, \zeta_{c}}$. But since our minimizer $S_{0} \subset Y_{\zeta_{1}, \zeta_{c}}$ is calibrated, it is unique, so the sequence of minimizers must converge to $S_{0}$. But then in a neighborhood of $S_{0}$ we have a uniqueness statement for our Lagrangian stationary sphere. Of course the whole process relies strongly on the fundamental results of Schoen-Wolfson [9].

Let us now give more details. For each $t>0$, by [9] the free homotopy class of $\Sigma$ can be represented by a $\omega_{t}$ Hamiltonian stationary, weakly conformal map $s_{t}: S^{2} \rightarrow X_{t}$, each being area minimizing in the homotopy class.

Of course the same map works for $\varpi_{t}=\frac{\omega_{t}}{t^{p}}$, which we now choose as the metric on $\widehat{\mathcal{M}}_{t}$. Since the area of the Hamiltonian stationary sphere that we constructed is $O(t)$ for $\omega_{t}$, it is bounded for $\varpi_{t}$, and so is the area of the collection $s_{t}$ which is not bigger.

The local geometry of $\left(\widehat{\mathcal{M}}_{t}, \varpi_{t}\right)$ is controlled: indeed, on the ALE part, $\left(\widehat{\mathcal{M}}_{t}, \varpi_{t}\right)$ converges to $Y_{\zeta_{1}, \zeta_{c}}$, while on the rest of the manifold, the curvature of $\varpi_{t}=\frac{\omega_{t}}{t^{p}}$ goes to zero. Moreover the injectivity radius of $\varpi_{t}$ remains bounded below. It follows that the local regularity results in [9] apply uniformly in $t$, in particular [9, Theorem 2.8] there is a uniform Hölder bound on the $s_{t}$. Since $\Sigma^{2} \neq 0$, the image of $s_{t}$ must cut $S_{0}$, and it follows that for $t$ small enough, the image of $s_{t}$ is completely included in a bounded domain of the ALE part.

Now we again claim that the compactness theorem [9, Theorem 5.8] applies in our context, because the geometry is controlled. This implies that some sequence $s_{t_{j}}$ for $t_{j} \rightarrow 0$ converges to a Lagrangian stationary, weakly conformal $W^{1,2}$ map
$s_{0}: S^{2} \rightarrow Y_{\zeta_{1}, \zeta_{c}}$, still representing the same homotopy class. Since $S_{0}$ is calibrated, the family must identify to the sphere $S_{0} \subset Y_{\zeta_{1}, \zeta_{c}}$. Since all $s_{t}$ are Lagrangian stationary, by regularity [9, Theorem 4.10] the convergence is smooth. Therefore for each $t>0$ small enough, $s_{t, 1}: S^{2} \rightarrow \widehat{\mathcal{M}}_{t}$ is an embedding converging to the standard embedding $S_{0} \rightarrow Y_{\zeta_{1}, \zeta_{c}}$. By the uniqueness statement in Lemma 36 it must coincide with the Hamiltonian stationary sphere that we constructed.

\section*{6. $T$-singularities and $\mathbb{Q}$-Gorenstein smoothings}
6.1. CSCK metrics. We extend our results in the setting of $\mathbb{Q}$-Gorenstein smoothings. The singularities that can appear are rational double points on one hand, on the other hand cyclic singularities of type $\frac{1}{d n^{2}}(1, d n m-1)$, where $n$ and $m$ are coprime integers. The last one is actually a $\mathbb{Z}_{n}$ quotient of the rational double point $\frac{1}{d n}(1,-1)$ by the action generated by $\left(\xi, \xi^{d n m-1}\right)$, for $\xi=e^{\frac{2 \pi i}{d n^{2}}}$.

We now explain why the results of the previous sections extend. Roughly speaking, the deformation theory of $\mathbb{Q}$-Gorenstein smoothings is the $\mathbb{Z}_{n}$ invariant part of the deformation theory for $A_{d n-1}$ singularities, and the models we glue are the $\mathbb{Z}_{n}$ quotients of $A_{d n-1}$ gravitational instantons. These models (the tangent gravitons) are no more hyperKähler ALE spaces, but only Kähler Ricci flat ALE spaces, and are given explicitly the Gibbons-Hawking ansatz, see [11]. Nevertheless everything done in sections 2-5 extends just by quotienting the local models by the action of $\mathbb{Z}_{n}$. This gives immediately Theorem A and Theorem B in the general case of $T$ singularities.
6.2. Hamiltonian stationary spheres. Here there are some interesting phenomenons happening in the case of $T$ singularities. The starting point is the same: in the setting of Theorem D, near a singular point $x \in \mathcal{X} \hookrightarrow \mathcal{M} \rightarrow \Delta$, we have, up to a covering of group $\mathbb{Z}_{n}$, a graviton $Y_{\zeta_{1}, \zeta_{c}}$, where $\zeta_{1} \in \mathfrak{h}_{\mathbb{R}}^{\mathbb{Z}_{n}}, \zeta_{c} \in \mathfrak{h}_{\mathbb{C}}^{\mathbb{Z}_{n}}$, and the space $\mathcal{M}_{t}$ is made by gluing $Y_{\zeta_{1}, \zeta_{c}} / \mathbb{Z}_{n}$ with the orbifold $\mathcal{X}$. In particular, given a large $\mathbb{Z}_{n}$ invariant region $V \subset Y_{\zeta_{1}, \zeta_{c}}$, one can identify $V / \mathbb{Z}_{n}$ with some region in $U \subset \mathcal{M}_{t}$ such that the metric $\frac{\omega_{t}}{t^{p}}$ converges to the restriction to $V / \mathbb{Z}_{n}$ of the ALE Ricci flat metric. Denote this projection $p: V \rightarrow U$.

If we have a root $\theta \in \Re^{+}$, such that $\langle\theta, \dot{\zeta}\rangle=0$ and $\theta$ is primitive for this property, and moreover $\left\langle\zeta_{1}(t), \theta\right\rangle=0$ for all $t$, then in the local $\mathbb{Z}_{n}$-covering $V$ the root $\theta$ represents a $p^{*} \Omega_{t}$ Lagrangian class. Corollary 38 applies as well, and $\theta$ can be represented by a $p^{*} \omega_{t}$ Hamiltonian stationary sphere $S_{t} \subset V$, converging to a sphere $S_{0}$ of the graviton $Y_{\zeta_{1}, \zeta_{c}}$, which is holomorphic with respect to a complex structure, orthogonal to $I_{1}$. Then $p\left(S_{t}\right)$ is a Hamiltonian stationary surface in $\left(\mathcal{M}_{t}, \omega_{t}\right)$, but $p\left(S_{t}\right)$ might be not embedded. This depends only on the model: $p\left(S_{t}\right)$ is embedded if $p\left(S_{0}\right)$ is, so we have to analyze the model.

Denote $\vartheta=\frac{1}{n} \sum_{g \in \mathbb{Z}_{n}} g \cdot \theta$. We claim that, if $\vartheta \neq 0$, then $p\left(S_{0}\right)$ is embedded, and we get a Hamiltonian stationary sphere in the homology class $p_{*} \vartheta$. This will end the proof of Theorem D. At the end of the section, we will also see some examples of behaviors when $\vartheta=0$, resulting in the construction of a $\mathbb{R} P^{2}$ or a $S^{2}$ with a double point.

Fortunately the possible spheres $S_{0}$ are explicit in the Gibbons-Hawking ansatz, so we merely have to check the above claim. Therefore we remind briefly what we need [11, §5].

We consider $k+1$ distinct points $p_{0}, \ldots, p_{k} \in \mathbb{R}^{3}$, and the harmonic function $V(x)=\frac{1}{2} \sum_{i} \frac{1}{\left|x-p_{i}\right|}$. Then $* d V$ is a closed 2-form on $\mathbb{R}^{3} \backslash\left\{p_{i}\right\}$, which is furthermore integral (indeed, the integral of $* d V$ on a small sphere around $p_{i}$ is 1 ). Therefore $* d V=d \eta$, where $\eta$ is the connection 1-form on the total space of a circle bundle $L \rightarrow \mathbb{R}^{3} \backslash\left\{p_{i}\right\}$. Because of the topology of $L$ near each $p_{i}$, the restriction of $L$ to a small 2 -sphere around $p_{i}$ is diffeomorphic to a 3 -sphere, and one can compactify $L$ into a smooth manifold $M$, equipped with a projection $\pi: M \rightarrow \mathbb{R}^{3}$, by adding just one point above each $p_{i}$. Then it turns out that
$$g=V\left(d x_{1}^{2}+d x_{2}^{2}+d x_{3}^{2}\right)+V^{-1} \eta^{2}$$
is a smooth hyperKähler metric on $M$, whose three complex structures are given by
$$I_{i} d x_{i}=V^{-1} \eta, \quad I_{i} d x_{j}=d x_{k},$$
where $(i, j, k)$ is a circular permutation of $(1,2,3)$. More generally, for any $\xi=$ $\left(\xi_{1}, \xi_{2}, \xi_{3}\right) \in S^{2}$, we have a complex structure $I_{\xi}$ such that $I_{\xi} \sum \xi_{i} d x_{i}=V^{-1} \eta$ and $I_{\xi}$ is a rotation of angle $\frac{\pi}{2}$ in the plane $\left(\sum \xi_{i} d x_{i}\right)^{\perp} \subset\left(\mathbb{R}^{3}\right)^{*}$; the corresponding Kähler form is $\omega_{\xi}=\sum_{i} \xi_{i}\left(d x_{i} \wedge \eta+V d x_{j} \wedge d x_{k}\right)$. All the structures are invariant under the circle action.

If the segment $\left[p_{a}, p_{b}\right]$ does not contain another point $p_{c}$, then $\pi^{-1}[a, b]$ is a 2-sphere, which is holomorphic for the complex structure $I_{\xi}$, where $\xi=\frac{a-b}{|a-b|}$, and Lagrangian for the Kähler forms $\omega_{\zeta}$ for $\zeta \perp \xi$. It follows immediately that $\pi^{-1}[a, b]$ is Hamiltonian stationary for the Kähler metric $\left(M, I_{\zeta}, \omega_{\zeta}\right)$, where $\zeta \perp \xi$, and this gives our model spheres in the case of $A_{k}$ singularities.

It is also interesting to describe the cohomology in this model: define the 2-form
$$\chi_{i}=d f_{i} \wedge \eta+* d f_{i}, \quad f_{i}(x)=\frac{1}{2 V(x)\left|x-p_{i}\right|}$$
It is easy to check that $\chi_{i}$ is a smooth closed antiselfdual 2-form on $M$, and $\sum \chi_{i}=$ 0 . This is the only relation and one gets the representation of the cohomology of $M$ by harmonic forms:
$$H^{2}(M, \mathbb{R})=\left\{\sum_{i} c_{i} \chi_{i}, \sum_{i} c_{i}=0\right\} .$$
(This actually describes the $L^{2}$ cohomology of $M$, which turns out to be equal to the ordinary cohomology.) The form $\chi_{i}$ evaluated on the 2 -sphere $\pi^{-1}\left[p_{a}, p_{b}\right]$ gives
$$\left\langle\chi_{i}, \pi^{-1}\left[p_{a}, p_{b}\right]\right\rangle=2 \pi\left(f_{i}\left(p_{a}\right)-f_{i}\left(p_{b}\right)\right)=2 \pi\left(\delta_{i a}-\delta_{i b}\right) .$$
This formula justifies the equality (6.1).
In the case of $T$ singularities, we start from a $A_{d n-1}$ gravitational instanton, given from the Gibbons-Hawking ansatz with $k+1=d n$ points. For a careful choice of the points $p_{a}$, there is a free isometric action of $\mathbb{Z}_{n}$ which is holomorphic for one of the complex structures: denote $z=x_{1}+i x_{2}$ (this a $I_{3}$ holomorphic function), we consider the action of a generator $\varpi=e^{\frac{2 i \pi}{n}}$ of $\mathbb{Z}_{n}$ given by
$$\varpi \cdot z=\varpi z, \quad \varpi \cdot \theta=\varpi^{m} \theta,$$
where $\theta$ is the angular coordinate, and $n$ and $m$ are coprime. Of course this action is well defined only if the configuration of the $d n$ points is invariant under $z \mapsto \varpi z$, that is if they are organized into a collection of $d$ regular centered $n$ polygons in planes orthogonal to the vector $\partial_{x_{3}}$. This gives all the ALE Ricci flat
models that we need for singularities of class $T$. Incidentally, the parameters are a collection of $d$ points (one in each polygon), that is $3 d$ real parameters, modulo the translation in the $\partial_{x_{3}}$ direction, so finally $3 d-1$ parameters as expected ( $d$ complex parameters and $d-1$ real parameters). In particular, from (6.1), the $\mathbb{Z}_{n}$ invariant part of $H^{2}(M, \mathbb{R})$ has dimension $d-1$.

We can now describe Hamiltonian stationary spheres: as we have seen, these are given by $\pi^{-1}\left[p_{a}, p_{b}\right]$, where $p_{a}-p_{b} \perp \partial_{x_{3}}$, that is by the segments in the planes of the polygons. Here there are two cases:
\begin{itemize}
\item[-] a segment $\left[p_{a}, p_{b}\right]$ between two points of two distinct polygons (which is possible only if the two polygons are in the same plane): if we change the point $p_{b}$ in the same polygon, we do not change the homology class in the quotient, because the sides of the polygon go to zero in the homology of the quotient; therefore we can choose $p_{b}$ to be the closest vertex to $p_{a}$, so that the images under $\mathbb{Z}_{n}$ of the segment $\left[p_{a}, p_{b}\right]$ are disjoint; therefore in the quotient we still obtain a 2-sphere with nonzero class in homology (indeed the pairing with $\frac{1}{n} \sum_{g \in \mathbb{Z}_{n}} g \cdot\left(\chi_{a}-\chi_{b}\right)$ is nonzero);
\item[-] a segment $\left[p_{a}, p_{b}\right]$ between two points of the same polygon: we consider only the two following cases (the images of the other spheres have more complicated crossings):
\begin{itemize}
\item[-] $\left[p_{a}, p_{b}\right]$ is an edge of the polygon; then in the quotient, the points $p_{a}$ and $p_{b}$ represent the same point and we obtain an immersed 2-sphere with one double point;
\item[] $-n=2$ and $p_{b}=-p_{a}$ : then the image of $\pi^{-1}\left[p_{a}, p_{b}\right]$ is an embedded $\mathbb{R} P^{2}$.
\end{itemize}
\end{itemize}
The other segments $\left[p_{a}, p_{b}\right]$ are more complicated since for a $g \in \mathbb{Z}_{n}$, the segment $g \cdot\left[p_{a}, p_{b}\right]$ might meet $\left[p_{a}, p_{b}\right]$ in an interior point, which means that one gets a double circle.

\section*{7. Applications}
7.1. Del Pezzo surfaces. Our result is applied to produce extremal metrics on $\mathbb{Q}$ -Gorenstein smoothings of singular extremal Del Pezzo surfaces with no nontrivial holomorphic vector field.

More precisely, let $\mathcal{X}$ be a normal Del Pezzo surface. If $\mathcal{X}$ admits a $\mathbb{Q}$-Gorenstein smoothing, then all the singularities of $\mathcal{X}$ must be of class $T$. So it is natural to assume that every singularity of $\mathcal{X}$ is of such type. Locally, we may pick a one parameter $\mathbb{Q}$-Gorenstein smoothing for each singularity of $\mathcal{X}$. It turns out that such local smoothing can always be globalized. In other words, one can find a $\mathbb{Q}$-Gorenstein smoothing $\mathcal{X} \hookrightarrow \mathcal{M} \rightarrow \Delta$ such that the germs of deformations of the singularities are the one we started with. This result is due to the fact that $H^{2}(\mathcal{X}, T \mathcal{X})=0$, hence there is no local to global obstruction to deformation theory as proved in [3, Proposition 3.1].

In particular, we can always construct in this way a one parameter $\mathbb{Q}$-Gorenstein smoothing $\mathcal{X} \hookrightarrow \mathcal{M} \rightarrow \Delta$ satisfying the non degeneracy condition in the sense of Definition 1. Suppose that $\mathcal{X}$ admits an extremal Kähler metric and no nontrivial holomorphic vector field (hence the metric must be CSCK) and that $\Omega_{t}$ is a family of Kähler classes on $\mathcal{M}_{t}$ that degenerates toward the orbifold Kähler class. Then, by Theorem A, the smoothing $\mathcal{M}_{t}$ admits a CSCK metric with Kähler class $\Omega_{t}$ for all $t>0$ sufficiently small.

For instance, consider the Del Pezzo orbifold $\mathcal{X}=\left(\mathbb{C P}^{1} \times \mathbb{C P}^{1}\right) / \mathbb{Z}_{4}$, where the action of $\mathbb{Z}_{4}$ on the product is spanned by
$$\left(\left[u_{1}: v_{1}\right],\left[u_{2}, v_{2}\right]\right) \mapsto\left(\left[i u_{1}: v_{1}\right],\left[i u_{2}, v_{2}\right]\right) .$$
The quotient contains exactly four singularities. Two of them are $A_{3}$ singularities whereas the two others are of type $T$, modelled on cyclic quotients of the form $\frac{1}{4}(1,1)$.

We construct a nondegenerate family of smoothings $\mathcal{X} \hookrightarrow \mathcal{M} \rightarrow \Delta$ as explained above. Quite interestingly, a smoothing $\mathcal{M}_{t}$ for $t \neq 0$ is not diffeomorphic to the minimal resolution $\widehat{\mathcal{X}}$ of $\mathcal{X}$. In such a situation $\mathcal{M}_{t}$, as a smooth manifold, is obtained by removing a neighborhood of the -4 exceptional spheres in $\widehat{\mathcal{X}}$ and gluing back two copies of the rational homology ball $T^{*} S^{2} / \mathbb{Z}_{2}=T^{*} \mathbb{R} \mathbb{P}^{2}$. Such an operation is known under the name of rational blowdown. Thus, $\mathcal{M}_{t}$ is the rational blowdown of $\widehat{\mathcal{X}}$ for $t \neq 0$. As $\widehat{\mathcal{X}}$ is an eight-point iterated blow-up of $\mathbb{C P}^{1} \times \mathbb{C P}^{1}$, one can show that $\mathcal{M}_{t}$ is a six-point blow up of $\mathbb{C P}^{1} \times \mathbb{C P}^{1}$.

The product $\mathbb{C P}^{1} \times \mathbb{C P}^{1}$ can be endowed with a CSCK metric by choosing a multiple of the standard Fubini-Study metric on each factor. The group $\mathbb{Z}_{4}$ acts isometrically on the product, thus we obtain a CSCK orbifold metric on $\mathcal{X}$.

Then we pick any family of Kähler classes $\Omega_{t}$ on $\mathcal{M}_{t}$ for $t>0$ that degenerates toward the orbifold Kähler class. At the point, we are ready to apply Theorem A. Unfortunately, $\mathcal{X}$ does admit nontrivial holomorphic vector fields. To get around this issue, we work equivariantly, modulo an additional symmetry. There is a $\mathbb{Z}_{2}$ action on $\mathbb{C P}^{1} \times \mathbb{C P}^{1}$ spanned by
$$\left(\left[u_{1}: v_{1}\right],\left[u_{2}: v_{2}\right]\right) \mapsto\left(\left[v_{1}: u_{1}\right],\left[v_{2}: u_{2}\right]\right) .$$
This action descends to the quotient $\mathcal{X}=\left(\mathbb{C P}^{1} \times \mathbb{C P}^{1}\right) / \mathbb{Z}_{4}$. The main point is that $\mathcal{X}$ does not carry any nontrivial holomorphic vector field. Such a $\mathbb{Z}_{2}$-action on $\mathcal{X}$ extends as a $\mathbb{Z}_{2}$ fiberwise-action on the smoothing $\mathcal{M} \rightarrow \Delta$. We may restrict our attention to $\mathbb{Z}_{2}$-equivariant smoothing (i.e. such that $\mathbb{Z}_{2}$ acts trivially on $\Delta$ ) and $\mathbb{Z}_{2}$-invariant Kähler classes $\Omega_{t}$. The proof of Theorem A can be done in this $\mathbb{Z}_{2}$-equivariant context. It follows that $\mathcal{M}_{t}$ admits a CSCK metric with Kähler class $\Omega_{t}$ for all $t>0$ sufficiently small.

In conclusion $\mathcal{M}_{t}$ carries aKähler-Einstein metric for all $t$ sufficiently small. It should be pointed out that $\mathcal{M}_{t}$ is not diffeomorphic to the minimal resolution of $\mathcal{X}$ for $t \neq 0$. In fact $\mathcal{M}_{t}$ is the full rational blow-down of $\widehat{\mathcal{X}}$ which is diffeomorphic to a 6-point blow-up of $\mathbb{C} \mathbb{P}^{1} \times \mathbb{C P}^{1}$.

Working with a Kähler-Einstein orbifold metric on $\mathcal{X}$ and $\Omega_{t}=c_{1}\left(\mathcal{M}_{t}\right)$ we recover Tian's metric for certain special Fano surfaces very close to the boundary of the moduli space, diffeomorphic to $\mathbb{C} \mathbb{P}^{1} \times \mathbb{C P}^{1}$ blown up six times. In addition Theorem D applies in this setting. Let $E$ the homology class of an exceptional holomorphic sphere in the resolution $\widehat{\mathcal{X}}$. Then $E$ can be represented by a stationary Lagrangian sphere in $\mathcal{M}_{t}$ for $t>0$ sufficiently small with respect to the Kähler-Einstein metric. It is also possible to prove that $\mathcal{M}_{t}$ contains two stationary Lagrangian $\mathbb{R P}^{2}$ obtained by perturbing the zero section of the tangent graviton $T^{*} \mathbb{R} \mathbb{P}^{2}$.

Similar examples can be constructed by considering the CSCK orbifold $\mathcal{X}=$ $\left(\mathbb{C P}^{1} \times \mathbb{C P}^{1}\right) / \mathbb{Z}_{2}$, an example considered by Spotti [10]. In this case $\mathcal{X}$ has four $A_{1}$ singularities and the smoothings are diffeomorphic to the minimal resolution $\widehat{\mathcal{X}}$. The construction above provides a construction of CSCK metrics on certain
four-point blowups of $\mathbb{C P}^{1} \times \mathbb{C P}^{1}$. In particular, we can apply this to the KählerEinstein case. Again, we prove that the -2 exceptional spheres can be deformed to get stationary Lagrangian spheres in the smoothing endowed with its KählerEinstein metric.
7.2. Geometrically ruled CSCK orbifold surfaces. A large class of geometrically ruled CSCK orbifolds can be constructed via representation theory. The idea is to consider an orbifold Riemann surface $\bar{\Sigma}$ and a twisted product $\mathcal{X}=\bar{\Sigma} \times_{\rho} \mathbb{C} \mathbb{P}^{1}$ where $\rho$ is a morphism $\rho: \pi_{1}^{\text {orb }}(\bar{\Sigma}) \rightarrow \mathrm{SU}_{2} / \mathbb{Z}_{2}$, where $\pi_{1}^{\text {orb }}(\bar{\Sigma})$ is the orbifold fundamental group. Here we require that if $p_{i}$ is a singular point of order $q_{i}$ in $\bar{\Sigma}$ and $l_{i}$ is the homotopy class of a small loop around $p_{i}$, then $\rho\left(l_{i}\right)$ is of order $q_{i}$.

If $\bar{\Sigma}$ has only orbifold points of order 2, then $\mathcal{X}$ has isolated singularities of type $A_{1}$. Suppose that $\bar{\Sigma}$ carries a CSCK metric (we just have to exclude the case of a teardrop with exactly one singularity of order 2). Then the local product metric provides a CSCK orbifold metric on $\mathcal{X}$.

Under the assumption that $\pi_{1}^{\text {orb }}(\bar{\Sigma})$ acts transitively on $\mathbb{C P}^{1}$ via $\rho$ and that $\bar{\Sigma}$ is not the football, the orbifold $\mathcal{X}$ does not carry any nontrivial holomorphic vector field [8].

In the next section, we show that is is always possible to find a nondegenerate $\mathbb{Q}$-Gorenstein smoothing of $\mathcal{X}$. In particular Theorem A and Theorem D apply and we may construct some new CSCK metrics on blownup ruled surfaces with stationary Lagrangian spheres.
7.3. Smoothing model for orbifold ruled surfaces. The example of ruled orbifold $\mathcal{X} \rightarrow \bar{\Sigma}$ given in the previous section has singularities that come by pair above each orbifold point in $\bar{\Sigma}$.

More precisely, the local model is given by an orbifold surface $\mathcal{Y} \rightarrow \mathbb{C} / \mathbb{Z}_{2}$ where $\mathcal{Y}=\left(\mathbb{C} \times \mathbb{C P}^{1}\right) / \mathbb{Z}_{2}$, the action of $\mathbb{Z}_{2}$ is spanned by $(u,[v: w]) \mapsto(-u,[-v: w])$ and the projection map $\mathcal{Y} \rightarrow \mathbb{C} / \mathbb{Z}_{2}$ is just induced by the first canonical projection.

Using the coordinates $(u,[v: w])$ on the ramified cover $\mathbb{C} \times \mathbb{C P}^{1}$, we see that $\mathbb{Z}_{2}$-invariant polynomials in the chart $w \neq 0$ are generated by
$$\left\{\begin{array}{l}
x_{1}=u^{2} \\
y_{1}=\left(\frac{v}{w}\right)^{2} \\
z_{1}=\frac{u v}{w}
\end{array}\right.$$
and the equation of $\mathcal{Y}$ in this chart is given by
$$x_{1} y_{1}=z_{1}^{2}$$
which is the equation of an $A_{1}$ singularity. Similarly, in the chart $v \neq 0$, we have the invariant polynomials
$$\left\{\begin{array}{l}
x_{2}=u^{2} \\
y_{2}=\left(\frac{w}{v}\right)^{2} \\
z_{2}=\frac{u w}{v}
\end{array}\right.$$
and the equation
$$x_{2} y_{2}=z_{2}^{2}$$
giving a second $A_{1}$ singularity.
Putting together (7.1) and (7.2), we conclude that $\mathcal{Y}$ is the subvariety of $\mathbb{C} \times \mathbb{C P}^{2}$ given by the equation
$$x \alpha \beta=\gamma^{2}$$
where $(x,[\alpha: \beta: \gamma]) \in \mathbb{C} \times \mathbb{C P}^{2}, x=x_{1}=x_{2}, \frac{\alpha}{\beta}=y_{1}=\frac{1}{y_{2}}, \frac{\gamma}{\beta}=z_{1}$ and $\frac{\gamma}{\alpha}=z_{2}$.
We introduce a family of deformation $\mathcal{Y} \hookrightarrow \mathcal{N} \rightarrow \mathbb{C}^{2}$ where $\mathcal{N}$ is the subvariety with points $\left(x,[\alpha: \beta: \gamma], \varepsilon_{1}, \varepsilon_{2}\right) \in \mathbb{C} \times \mathbb{C P}^{2} \times \mathbb{C}^{2}$ given by the equation
$$\varepsilon_{1} \alpha^{2}+\varepsilon_{2} \beta^{2}+x \alpha \beta=\gamma^{2}$$
and the map $\mathcal{N} \rightarrow \mathbb{C}^{2}$ is induced by the canonical projection $\left(x,[\alpha: \beta: \gamma], \varepsilon_{1}, \varepsilon_{2}\right) \mapsto$ $\varepsilon=\left(\varepsilon_{1}, \varepsilon_{2}\right)$. The singular locus of $\mathcal{N}$ is contained in the hypersurface $\varepsilon_{1} \varepsilon_{2}=0$ and if neither $\varepsilon_{1}$ nor $\varepsilon_{2}$ vanish, then the fiber $\mathcal{N}_{\varepsilon}$ is a smooth deformation of $\mathcal{Y}$.

Using affine coordinates, one can check that the parameters $\varepsilon_{i}$ correspond to the parameters of the semi-universal family of smoothings for the $A_{1}$ singularity. In particular, if we choose a line in $\mathbb{C}^{2}$ distinct of the lines $\varepsilon_{1}=0$ or $\varepsilon_{2}=0$, we obtain a nondegenerate family of smoothings of $\left(\mathbb{C} \times \mathbb{C P}^{1}\right) / \mathbb{Z}_{2}$.

We have a canonical projection $\mathcal{N} \rightarrow \mathbb{C}$ given by the coordinate $x$. The restriction of this map $\mathcal{N}_{\varepsilon} \rightarrow \mathbb{C}$ defines a ruled surface over $\mathbb{C}$ and it is smooth unless $\varepsilon_{1} \varepsilon_{2}=0$. One can also check that the fibers of the ruling are all $\mathbb{C P}^{1}$ except when $x^{2}=4 \varepsilon_{1} \varepsilon_{2}$ where the polynomial $\varepsilon_{1} \alpha^{2}+\varepsilon_{2} \beta^{2}+x \alpha \beta-\gamma^{2}$ splits as a product of two polynomials of degree 1 in $(\alpha, \beta, \gamma)$. If $\varepsilon_{1} \varepsilon_{2} \neq 0$, there are two distinct fibers that consist of a union of two $\mathbb{C P}^{1}$ with normal crossing at one point. Topological considerations imply that the curves have selfintersection -1. In conclusion, assuming $\varepsilon_{1} \varepsilon_{2} \neq 0$, the ruled surface $\mathcal{N}_{\varepsilon} \rightarrow \mathbb{C}$ is a two point blowup of $\mathbb{C} \times \mathbb{C P}^{1}$ at two distinct fibers.

Let $\Delta_{1 / 2}^{2}$ be the ball of radius $1 / 2$ is $\mathbb{C}^{2}$, so that $\left|\varepsilon_{1} \varepsilon_{2}\right|<1 / 4$ for $\varepsilon \in \Delta_{1 / 2}^{2}$. Let $\mathcal{N}^{\prime}$ (resp. $\mathcal{N}^{\prime \prime}$ ) be the restriction of $\mathcal{N}$ to the domain $|x| \leq 2$ and $\varepsilon \in \Delta_{1 / 2}^{2}$ (resp. $x \in A=\{1<|x| \leq 2\}$ and $\varepsilon \in \Delta_{1 / 2}^{2}$ ). Accordingly, we shall denote $\mathcal{Y}^{\prime}=\mathcal{N}_{0}^{\prime}$ and $\mathcal{Y}^{\prime \prime}=\mathcal{N}_{0}^{\prime \prime}$.

By definition, $\mathcal{N}^{\prime \prime}$ is equipped with a projection $\mathcal{N}^{\prime \prime} \rightarrow A \times \Delta_{1 / 2}^{2}$. This projection is a geometric ruling (a submersive holomorphic map with fibers $\mathbb{C P}^{1}$ ) for reducible curves appear only for $x^{2}=4 \varepsilon_{1} \varepsilon_{2}$. Hence there exists a biholomorphism
$$\phi: \mathcal{N}^{\prime \prime} \rightarrow A \times \Delta_{1 / 2}^{2} \times \mathbb{C} \mathbb{P}^{1}$$
which commutes with the projection maps to $A \times \Delta_{1 / 2}^{2}$.
The restriction of the map $\phi$ induces an isomorphism $\mathcal{Y}^{\prime \prime} \rightarrow A \times \mathbb{C} \mathbb{P}^{1}$. Taking the product with the identity, we deduce an isomorphism
$$\psi: \Delta_{1 / 2}^{2} \times \mathcal{Y}^{\prime \prime} \rightarrow A \times \Delta_{1 / 2}^{2} \times \mathbb{C} \mathbb{P}^{1} .$$
We shall the maps $\phi$ and $\psi$ to construct deformations of orbifold ruled surfaces in the next section.
7.4. Construction of deformations. Let $\mathcal{X}$ be a compact complex orbifold surface with a holomorphic embedding
$$j: \mathcal{Y}^{\prime} \hookrightarrow \mathcal{X}$$
where $\mathcal{Y}^{\prime}=\mathcal{N}_{0}^{\prime}$. We shall construct a smoothing of $\mathcal{X}$ using the smoothing $\mathcal{N}^{\prime}$ described in the previous section.

Let $\mathcal{X}^{\prime}$ be the complement in $\mathcal{X}$ of the domain $|x| \leq 1$ of $\mathcal{Y}^{\prime}$. In particular, we have the restriction $j: \mathcal{Y}^{\prime \prime} \hookrightarrow \mathcal{X}^{\prime}$. We introduce
$$\mathcal{M}=\left(\Delta_{1 / 2}^{2} \times \mathcal{X}^{\prime}\right) \sqcup \mathcal{N}^{\prime} / \sim$$

The equivalence relation is given as follows: if $(\varepsilon, m) \in \Delta_{1 / 2}^{2} \times \mathcal{X}^{\prime}$ is such that $m=j(y)$ for some $y \in \mathcal{Y}^{\prime \prime}$, we identify the point $(\varepsilon, m)$ with $z \in \mathcal{N}^{\prime \prime} \subset \mathcal{N}^{\prime}$ provided $\psi(\varepsilon, m)=\phi(z)$.

The complex variety $\mathcal{M}$ endowed with the canonical maps $\mathcal{X} \hookrightarrow \mathcal{M} \rightarrow \Delta_{1 / 2}^{2}$ is a flat deformation of $\mathcal{X}$ and it is non degenerate in the sense of Definition 1.

We deduce the following proposition by applying Theorem A and Theorem D to the family of smoothings $\mathcal{X} \hookrightarrow \mathcal{M} \rightarrow \Delta$.

Proposition 39. Let $\mathcal{X}=\bar{\Sigma} \times_{\rho} \mathbb{C P}^{1}$ be a CSCK geometrically ruled surface with singularities of type $A_{1}$ and no nontrivial holomorphic vector fields as described in §7.2

Then there exists one parameter families of nondegenerate smoothings $\mathcal{X} \hookrightarrow$ $\mathcal{M} \rightarrow \Delta$. In particular, $\mathcal{X}$ admits CSCK smoothings with stationary Lagrangian spheres representing the vanishing Lagrangian cycles.

\section*{References}
\begin{itemize}
\item[] [1] C. Arezzo and F. Pacard. Blowing up and desingularizing constant scalar curvature Kähler manifolds. Acta Math., 196(2):179-228, 2006.
\item[] [2] C. Arezzo and F. Pacard. Blowing up Kähler manifolds with constant scalar curvature. II. Ann. of Math. (2), 170(2):685-738, 2009.
\item[] [3] P. Hacking and Y. Prokhorov. Smoothable del Pezzo surfaces with quotient singularities. Compos. Math., 146(1):169-192, 2010.
\item[] [4] F. Huikeshoven. On the versal resolutions of deformations of rational double points. Invent. Math., 20:15-33, 1973.
\item[] [5] D. D. Joyce. Compact manifolds with special holonomy. Oxford Mathematical Monographs. Oxford University Press, Oxford, 2000.
\item[] [6] A. Kas and M. Schlessinger. On the versal deformation of a complex space with an isolated singularity. Math. Ann., 196:23-29, 1972.
\item[] [7] J. Kollár and N. I. Shepherd-Barron. Threefolds and deformations of surface singularities. Invent. Math., 91(2):299-338, 1988.
\item[] [8] Y. Rollin and M. Singer. Non-minimal scalar-flat Kähler surfaces and parabolic stability. Invent. Math., 162(2):235-270, 2005.
\item[] [9] R. Schoen and J. Wolfson. Minimizing area among Lagrangian surfaces: the mapping problem. J. Differential Geom., 58(1):1-86, 2001.
\item[] [10] C. Spotti. Deformations of nodal Kähler-Einstein Del Pezzo surfaces with discrete automorphism groups. ArXiv:1211.5344, 2012.
\item[] [11] I. Şuvaina. ALE Ricci-flat Kähler metrics and deformations of quotient surface singularities. Ann. Global Anal. Geom., 41(1):109-123, 2012.
\item[] [12] G. Székelyhidi. On blowing up extremal Kähler manifolds. Duke Math. J., 161(8):1411-1453, 2012.
\item[] [13] G. Tian. On Calabi's conjecture for complex surfaces with positive first Chern class. Invent. Math., 101(1):101-172, 1990.
\end{itemize}

Olivier Biquard, UPMC Université Paris 6 et École Normale Supérieure
E-mail address: olivier.biquard@upmc.fr
Yann Rollin, Laboratoire Jean Leray, Université de Nantes
E-mail address: yann.rollin@univ-nantes.fr