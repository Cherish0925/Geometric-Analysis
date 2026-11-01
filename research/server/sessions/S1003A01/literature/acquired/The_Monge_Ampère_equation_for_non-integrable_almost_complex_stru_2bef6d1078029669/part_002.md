---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: The Monge–Ampère equation for non-integrable almost complex structures]

We will use four lemmas to complete the proof. The first deals with the relatively harmless part of the bad term (5.19).

Lemma 5.5. Assuming that $A$ is larger than $6 n \sup _{M}|\partial \varphi|_{g}^{2}$, we have
$$-(1+\varepsilon) \sum_{i \in I} \frac{\tilde{g}^{i \bar{i}}\left|e_{i}\left(\varphi_{V_{1} V_{1}}\right)\right|^{2}}{\lambda_{1}^{2}} \geqslant-\sum_{i} \tilde{g}^{i \bar{i}}-\left.\left.2\left(h^{\prime}\right)^{2} \sum_{i \in I} \tilde{g}^{i \bar{i}}\left|e_{i}\right| \partial \varphi\right|_{g} ^{2}\right|^{2} .$$

Proof. Using the fact that the first derivative of $\hat{Q}$ vanishes at $x_{0}$, as in (5.20), we compute
$$\begin{aligned}
& -(1+\varepsilon) \sum_{i \in I} \frac{\tilde{g}^{i \bar{i}}\left|e_{i}\left(\varphi_{V_{1} V_{1}}\right)\right|^{2}}{\lambda_{1}^{2}} \\
& =-(1+\varepsilon) \sum_{i \in I} \tilde{g}^{i \bar{i}}\left|A e^{-A \varphi} e_{i}(\varphi)-h^{\prime} e_{i}\left(|\partial \varphi|_{g}^{2}\right)\right|^{2} \\
& \geqslant-6\left(\sup _{M}|\partial \varphi|_{g}^{2}\right) A^{2} e^{-2 A \varphi} \sum_{i \in I} \tilde{g}^{i \bar{i}}-\left.\left.2\left(h^{\prime}\right)^{2} \sum_{i \in I} \tilde{g}^{i \bar{i}}\left|e_{i}\right| \partial \varphi\right|_{g} ^{2}\right|^{2} \\
& \geqslant-\frac{6 n\left(\sup _{M}|\partial \varphi|_{g}^{2}\right) \tilde{g}^{n \bar{n}}}{A}-\left.\left.2\left(h^{\prime}\right)^{2} \sum_{i \in I} \tilde{g}^{i \bar{i}}\left|e_{i}\right| \partial \varphi\right|_{g} ^{2}\right|^{2} \\
& \geqslant-\sum_{i} \tilde{g}^{i \bar{i}}-\left.\left.2\left(h^{\prime}\right)^{2} \sum_{i \in I} \tilde{g}^{i \bar{i}}\left|e_{i}\right| \partial \varphi\right|_{g} ^{2}\right|^{2},
\end{aligned}$$
where in the last line we used the assumption $A \geqslant 6 n \sup _{M}|\partial \varphi|_{g}^{2}$. \(\square\)

The next lemma shows that, roughly speaking, and modulo terms of order $O\left(\lambda_{1}^{-1}\right)$, the largest eigenvector $V_{1}$ lies in the directions where the Hermitian metric $\left(\tilde{g}_{i \bar{i}}\right)$ at $x_{0}$ is not too small. More precisely, we define in our coordinate patch a $(1,0)$ vector field by
$$\tilde{e}_{1}:=\frac{1}{\sqrt{2}}\left(V_{1}-\sqrt{-1} J V_{1}\right) .$$
We write at $x_{0}$,
$$\tilde{e}_{1}=\sum_{q=1}^{n} \nu_{q} e_{q}, \quad \sum_{q=1}^{n}\left|\nu_{q}\right|^{2}=1,$$
for complex numbers $\nu_{1}, \ldots, \nu_{n}$, where the second equation follows from the fact that $\tilde{e}_{1}$ is $g$-unit at $x_{0}$. Then we have:

Lemma 5.6. For a uniform constant $C_{A}$ depending on $A$, we have
$$\left|\nu_{q}\right| \leqslant \frac{C_{A}}{\lambda_{1}}, \quad \text { for all } q \notin I,$$
where the $\nu_{q}$ are given by (5.29).
Proof. To prove the claim, we see from
$$\frac{h^{\prime}}{4} \sum_{k} \tilde{g}^{i \bar{i}}\left(\left|e_{i} e_{k}(\varphi)\right|^{2}+\left|e_{i} \bar{e}_{k}(\varphi)\right|^{2}\right) \leqslant 6\left(\sup _{M}|\partial \varphi|_{g}^{2}\right) A^{2} e^{-2 A \varphi} \sum_{i} \tilde{g}^{i \bar{i}},$$
that
$$\frac{h^{\prime}}{4} \sum_{k} \sum_{i \notin I} \tilde{g}^{i \bar{i}}\left(\left|e_{i} e_{k}(\varphi)\right|^{2}+\left|e_{i} \bar{e}_{k}(\varphi)\right|^{2}\right) \leqslant 6 n\left(\sup _{M}|\partial \varphi|_{g}^{2}\right) A^{2} e^{-2 A \varphi} \tilde{g}^{n \bar{n}} .$$

Hence by the definition of $I$,
$$\sum_{k} \sum_{i \notin I}\left(\left|e_{i} e_{k}(\varphi)\right|^{2}+\left|e_{i} \bar{e}_{k}(\varphi)\right|^{2}\right) \leqslant \frac{24 n A^{5} e^{-4 A \varphi}}{h^{\prime}} \sup _{M}|\partial \varphi|_{g}^{2} .$$
For convenience, write $I=\{1,2, \ldots, j\}$ for some $j$ with $1 \leqslant j<n$. Then, arguing exactly as in (5.21), (5.22), (5.23), the estimate (5.30) implies that
$$\sum_{\alpha=2 j+1}^{2 n} \sum_{\beta=1}^{2 n}\left|\nabla_{\alpha \beta}^{2} \varphi\right| \leqslant C_{A},$$
where we write $C_{A}$ for a uniform constant depending on $A$ (recall that $A$ is yet to be determined, but will be chosen uniformly).

In terms of the matrix $\Phi^{\alpha}{ }_{\beta}$, defined by (5.7), the inequality (5.31) implies that at $x_{0}$,
$$\left|\Phi^{\alpha}{ }_{\beta}\right| \leqslant C_{A}, \quad \text { whenever } 2 j+1 \leqslant \alpha \leqslant 2 n, 1 \leqslant \beta \leqslant 2 n .$$
Since $V_{1}=\left(V_{1}^{\alpha}\right)_{\alpha=1}^{2 n}$ is a unit eigenvector for $\Phi$ with eigenvalue $\lambda_{1}$ we have $\Phi\left(V_{1}\right)=\lambda_{1} V_{1}$ and hence
$$\left|V_{1}^{\alpha}\right|=\left|\frac{1}{\lambda_{1}} \sum_{\beta=1}^{2 n} \Phi_{\beta}^{\alpha} V_{1}^{\beta}\right| \leqslant \frac{C_{A}}{\lambda_{1}}, \quad \text { for } 2 j+1 \leqslant \alpha \leqslant 2 n .$$
The lemma then follows easily from the definition of the $e_{i}$. \(\square\)

The goal for our last two lemmas is to obtain a lower bound for the first three terms on the right hand side of (5.17), excluding those bounded by Lemma 5.5. The first of these two lemmas is a technical intermediate step. We make use of real numbers $\mu_{2}, \mu_{3}, \ldots, \mu_{2 n}$ defined by
$$J V_{1}=\sum_{\alpha>1} \mu_{\alpha} V_{\alpha}, \quad \sum_{\alpha>1} \mu_{\alpha}^{2}=1, \quad \text { at } x_{0},$$
where we recall that at $x_{0}$ the vector $J V_{1}$ is $g$-unit and $g$-orthogonal to $V_{1}$.
Lemma 5.7. For any $\gamma>0$, at $x_{0}$,
$$\begin{aligned}
& \sum_{\alpha>1} \tilde{g}^{i \bar{i}} \frac{\left|e_{i}\left(\varphi_{V_{\alpha} V_{1}}\right)\right|^{2}}{\lambda_{1}\left(\lambda_{1}-\lambda_{\alpha}\right)}+\frac{\tilde{g}^{p \bar{p}} \tilde{g}^{q \bar{q}}\left|V_{1}\left(\tilde{g}_{p \bar{q}}\right)\right|^{2}}{\lambda_{1}}-(1+\varepsilon) \sum_{i \notin I} \frac{\tilde{g}^{i \bar{i}}\left|e_{i}\left(\varphi_{V_{1} V_{1}}\right)\right|^{2}}{\lambda_{1}^{2}} \\
& \quad \geqslant \sum_{i \notin I} \sum_{\alpha>1} \frac{\tilde{g}^{i \bar{i}}}{\lambda_{1}^{2}}\left(\frac{(2-\varepsilon) \lambda_{1}}{\lambda_{1}-\lambda_{\alpha}}\left|e_{i}\left(\varphi_{V_{\alpha} V_{1}}\right)\right|^{2}\right)+2 \sum_{q \in I} \sum_{i \notin I} \tilde{g}^{i \bar{i}} \tilde{g}^{q \bar{q}} \frac{\left|V_{1}\left(\tilde{g}_{i \bar{q}}\right)\right|^{2}}{\lambda_{1}} \\
& \quad-3 \varepsilon \sum_{i \notin I} \frac{\tilde{g}^{i \bar{i}}\left|e_{i}\left(\varphi_{V_{1} V_{1}}\right)\right|^{2}}{\lambda_{1}^{2}}-(1-\varepsilon)(1+\gamma) \tilde{g}_{\overline{1} \overline{1}} \sum_{q \in I} \sum_{i \notin I} \frac{2 \tilde{g}^{i \bar{i}} \tilde{g}^{q \bar{q}}}{\lambda_{1}^{2}}\left|V_{1}\left(\tilde{g}_{i \bar{q}}\right)\right|^{2} \\
& \quad-\frac{C}{\varepsilon} \sum_{i} \tilde{g}^{i \bar{i}}-(1-\varepsilon)\left(1+\frac{1}{\gamma}\right)\left(\lambda_{1}-\sum_{\alpha>1} \lambda_{\alpha} \mu_{\alpha}^{2}\right) \sum_{i \notin I} \sum_{\alpha>1} \frac{\tilde{g}^{i \bar{i}}}{\lambda_{1}^{2}} \frac{\left|e_{i}\left(\varphi_{V_{\alpha} V_{1}}\right)\right|^{2}}{\lambda_{1}-\lambda_{\alpha}},
\end{aligned}$$
assuming without loss of generality that at $x_{0}, \lambda_{1} \geqslant C_{A} / \varepsilon$ for a uniform $C_{A}>0$ depending on $A$. Here we are writing $\tilde{g}_{\widetilde{1} \overline{1}}:=\tilde{g}\left(\tilde{e}_{1}, \overline{\bar{e}}_{1}\right)$.
Proof. We first claim that
$$e_{i}\left(\varphi_{V_{1} V_{1}}\right)=\sqrt{2} \sum_{q} \overline{\nu_{q}} V_{1}\left(\tilde{g}_{i \bar{q}}\right)-\sqrt{-1} \sum_{\alpha>1} \mu_{\alpha} e_{i}\left(\varphi_{V_{1} V_{\alpha}}\right)+E,$$
where $E$ denotes a term satisfying $|E| \leqslant C \lambda_{1}$ for a uniform $C$. Defining $\varphi_{V_{1} \bar{\varepsilon}_{1}}$ in the obvious way, we have at $x_{0}$,
$$e_{i}\left(\varphi_{V_{1} V_{1}}\right)=\sqrt{2} e_{i}\left(\varphi_{V_{1} \bar{e}_{1}}\right)-\sqrt{-1} e_{i}\left(\varphi_{V_{1} J V_{1}}\right),$$
since $\overline{\tilde{e}}_{1}=\frac{1}{\sqrt{2}}\left(V_{1}+\sqrt{-1} J V_{1}\right)$. Next,
$$e_{i}\left(\varphi_{V_{1} \bar{e}_{1}}\right)=e_{i} V_{1} \overline{\tilde{e}}_{1}(\varphi)-e_{i}\left(\nabla_{V_{1}} \overline{\tilde{e}}_{1}\right)(\varphi)=\overline{\tilde{e}}_{1} e_{i} V_{1}(\varphi)+E,$$
since the error terms arising from switching the order of operators give terms involving only two derivatives of $\varphi$.

With $\nu_{1}, \ldots, \nu_{n} \in \mathbb{C}$ as in (5.29), we have at $x_{0}$,
$$\begin{aligned}
\overline{\tilde{e}}_{1} e_{i} V_{1}(\varphi) & =\sum_{q} \overline{\nu_{q}} \bar{e}_{q} e_{i} V_{1}(\varphi)=\sum_{q} \overline{\nu_{q}} V_{1} e_{i} \bar{e}_{q}(\varphi)+E \\
& =\sum_{q} \overline{\nu_{q}} V_{1}\left(\tilde{g}_{i \bar{q}}\right)+E .
\end{aligned}$$
Recalling (5.32),
$$\begin{aligned}
e_{i}\left(\varphi_{V_{1} J V_{1}}\right) & =e_{i} V_{1} J V_{1}(\varphi)-e_{i}\left(\nabla_{V_{1}}\left(J V_{1}\right)\right)(\varphi)=J V_{1} e_{i} V_{1}(\varphi)+E \\
& =\sum_{\alpha>1} \mu_{\alpha} V_{\alpha} e_{i} V_{1}(\varphi)+E=\sum_{\alpha>1} \mu_{\alpha} e_{i}\left(\varphi_{V_{1} V_{\alpha}}\right)+E .
\end{aligned}$$
Combining (5.34), (5.35), (5.36) and (5.37) proves the claim (5.33).
Hence, for a uniform $C$,
$$\begin{aligned}
& (1+\varepsilon) \sum_{i \notin I} \frac{\tilde{g}^{i \bar{i}}\left|e_{i}\left(\varphi_{V_{1}} V_{1}\right)\right|^{2}}{\lambda_{1}^{2}}=3 \varepsilon \sum_{i \notin I} \frac{\tilde{g}^{i \bar{i}}\left|e_{i}\left(\varphi_{V_{1} V_{1}}\right)\right|^{2}}{\lambda_{1}^{2}} \\
& \quad+(1-2 \varepsilon) \sum_{i \notin I} \frac{\tilde{g}^{i \bar{i}}\left|\sqrt{2} \sum_{q=1}^{n} \overline{\nu_{q}} V_{1}\left(\tilde{g}_{i \bar{q}}\right)-\sqrt{-1} \sum_{\alpha>1} \mu_{\alpha} e_{i}\left(\varphi_{V_{1} V_{\alpha}}\right)+E\right|^{2}}{\lambda_{1}^{2}} \\
& \quad \leqslant 3 \varepsilon \sum_{i \notin I} \frac{\tilde{g}^{i \bar{i}}\left|e_{i}\left(\varphi_{V_{1} V_{1}}\right)\right|^{2}}{\lambda_{1}^{2}} \\
& \quad+(1-\varepsilon) \sum_{i \notin I} \frac{\tilde{g}^{i \bar{i}}\left|\sqrt{2} \sum_{q \in I} \overline{\nu_{q}} V_{1}\left(\tilde{g}_{i \bar{q}}\right)-\sqrt{-1} \sum_{\alpha>1} \mu_{\alpha} e_{i}\left(\varphi_{V_{1} V_{\alpha}}\right)\right|^{2}}{\lambda_{1}^{2}} \\
& \quad+\frac{C_{A}}{\varepsilon} \sum_{i \notin I} \sum_{q \notin I} \frac{\tilde{g}^{i \bar{i}}\left|V_{1}\left(\tilde{g}_{i \bar{q}}\right)\right|^{2}}{\lambda_{1}^{4}}+\frac{C}{\varepsilon} \sum_{i} \tilde{g}^{i \bar{i}},
\end{aligned}$$
using Lemma 5.6.
For $\gamma>0$, we bound
$$\begin{aligned}
& (1-\varepsilon) \sum_{i \notin I} \frac{\tilde{g}^{i \bar{i}}\left|\sqrt{2} \sum_{q \in I} \overline{\nu_{q}} V_{1}\left(\tilde{g}_{i \bar{q}}\right)-\sqrt{-1} \sum_{\alpha>1} \mu_{\alpha} e_{i}\left(\varphi_{V_{1} V_{\alpha}}\right)\right|^{2}}{\lambda_{1}^{2}} \\
& \leqslant(1-\varepsilon)(1+\gamma) \sum_{i \notin I} \frac{2 \tilde{g}^{i \bar{i}}}{\lambda_{1}^{2}}\left|\sum_{q \in I} \overline{\nu_{q}} V_{1}\left(\tilde{g}_{i \bar{q}}\right)\right|^{2}+(1-\varepsilon)\left(1+\frac{1}{\gamma}\right) \sum_{i \notin I} \frac{\tilde{g}^{i \bar{i}}}{\lambda_{1}^{2}}\left|\sum_{\alpha>1} \mu_{\alpha} e_{i}\left(\varphi_{V_{1} V_{\alpha}}\right)\right|^{2} .
\end{aligned}$$
But we also have, by the Cauchy-Schwarz inequality,
$$\left|\sum_{q \in I} \overline{\nu_{q}} V_{1}\left(\tilde{g}_{i \bar{q}}\right)\right|^{2} \leqslant\left(\sum_{q=1}^{n}\left|\nu_{q}\right|^{2} \tilde{g}_{q \bar{q}}\right)\left(\sum_{q \in I} \tilde{g}^{q \bar{q}}\left|V_{1}\left(\tilde{g}_{i \bar{q}}\right)\right|^{2}\right)=\tilde{g}\left(\tilde{e}_{1}, \overline{\tilde{e}}_{1}\right)\left(\sum_{q \in I} \tilde{g}^{q \bar{q}}\left|V_{1}\left(\tilde{g}_{i \bar{q}}\right)\right|^{2}\right),$$
and
$$\begin{aligned}
\left|\sum_{\alpha>1} \mu_{\alpha} e_{i}\left(\varphi_{V_{\alpha} V_{1}}\right)\right|^{2} & \leqslant\left(\sum_{\alpha>1}\left(\lambda_{1}-\lambda_{\alpha}\right) \mu_{\alpha}^{2}\right)\left(\sum_{\alpha>1} \frac{\left|e_{i}\left(\varphi_{V_{\alpha} V_{1}}\right)\right|^{2}}{\lambda_{1}-\lambda_{\alpha}}\right) \\
& =\left(\lambda_{1}-\sum_{\alpha>1} \lambda_{\alpha} \mu_{\alpha}^{2}\right)\left(\sum_{\alpha>1} \frac{\left|e_{i}\left(\varphi_{V_{\alpha} V_{1}}\right)\right|^{2}}{\lambda_{1}-\lambda_{\alpha}}\right),
\end{aligned}$$
recalling that we have $\sum_{\alpha>1} \mu_{\alpha}^{2}=1$. So the conclusion is that
$$\begin{aligned}
& (1-\varepsilon) \sum_{i \notin I} \frac{\tilde{g}^{i \bar{i}}\left|\sqrt{2} \sum_{q \in I} \overline{\nu_{q}} V_{1}\left(\tilde{g}_{i \bar{q}}\right)-\sqrt{-1} \sum_{\alpha>1} \mu_{\alpha} e_{i}\left(\varphi_{V_{1} V_{\alpha}}\right)\right|^{2}}{\lambda_{1}^{2}} \\
& \leqslant(1-\varepsilon)(1+\gamma) \tilde{g}_{\overline{1} \overline{1}} \sum_{q \in I} \sum_{i \notin I} \frac{2 \tilde{g}^{i \bar{i}} \tilde{g}^{q \bar{q}}}{\lambda_{1}^{2}}\left|V_{1}\left(\tilde{g}_{i \bar{q}}\right)\right|^{2} \\
& +(1-\varepsilon)\left(1+\frac{1}{\gamma}\right)\left(\lambda_{1}-\sum_{\alpha>1} \lambda_{\alpha} \mu_{\alpha}^{2}\right) \sum_{i \notin I} \sum_{\alpha>1} \frac{\tilde{g}^{i \bar{i}}}{\lambda_{1}^{2}} \frac{\left|e_{i}\left(\varphi_{V_{\alpha} V_{1}}\right)\right|^{2}}{\lambda_{1}-\lambda_{\alpha}} .
\end{aligned}$$
Also, using (4.1), we see that at $x_{0}$ we have
$$\tilde{g}_{q \bar{q}} \leqslant \tilde{g}_{1 \overline{1}} \leqslant C+e_{1} \bar{e}_{1}(\varphi) \leqslant C^{\prime} \lambda_{1},$$
for any $q$, using that $\lambda_{1}$ may be assumed to be large. Therefore, if $\lambda_{1} \geqslant \frac{C_{A}}{\varepsilon}$ for the constant $C_{A}$ of (5.38), and if also $\lambda_{1} \geqslant C^{\prime}$, then we have
$$\frac{C_{A}}{\varepsilon \lambda_{1}^{3}} \leqslant \tilde{g}^{q \bar{q}}$$

Therefore we obtain the inequality
$$\begin{aligned}
\frac{\tilde{g}^{p \bar{p}} \tilde{g}^{q \bar{q}}\left|V_{1}\left(\tilde{g}_{p \bar{q}}\right)\right|^{2}}{\lambda_{1}} \geqslant & 2 \sum_{q \in I} \sum_{i \notin I} \tilde{g}^{i \bar{i}} \tilde{g}^{q \bar{q}} \frac{\left|V_{1}\left(\tilde{g}_{i \bar{q}}\right)\right|^{2}}{\lambda_{1}} \\
& +\frac{C_{A}}{\varepsilon} \sum_{q \notin I} \sum_{i \notin I} \frac{\tilde{g}^{i \bar{i}}\left|V_{1}\left(\tilde{g}_{i \bar{q}}\right)\right|^{2}}{\lambda_{1}^{4}} .
\end{aligned}$$
Combining (5.38), (5.40) and (5.41) completes the proof of the lemma. \(\square\)

We use this to prove the final lemma:
Lemma 5.8. At $x_{0}$ we have
$$\begin{aligned}
& (2-\varepsilon) \sum_{\alpha>1} \tilde{g}^{i \bar{i}} \frac{\left|e_{i}\left(\varphi_{V_{\alpha} V_{1}}\right)\right|^{2}}{\lambda_{1}\left(\lambda_{1}-\lambda_{\alpha}\right)}+\frac{\tilde{g}^{p \bar{p}} \tilde{g}^{q \bar{q}}\left|V_{1}\left(\tilde{g}_{p \bar{q}}\right)\right|^{2}}{\lambda_{1}}-(1+\varepsilon) \sum_{i \notin I} \frac{\tilde{g}^{i \bar{i}}\left|e_{i}\left(\varphi_{V_{1} V_{1}}\right)\right|^{2}}{\lambda_{1}^{2}} \\
& \quad \geqslant-6 \varepsilon A^{2} e^{-2 A \varphi} \tilde{g}^{i \bar{i}}\left|e_{i}(\varphi)\right|^{2}-\left.\left.6 \varepsilon\left(h^{\prime}\right)^{2} \sum_{i \notin I} \tilde{g}^{i \bar{i}}\left|e_{i}\right| \partial \varphi\right|_{g} ^{2}\right|^{2}-\frac{C}{\varepsilon} \sum_{i} \tilde{g}^{i \bar{i}},
\end{aligned}$$
for a uniform constant $C>0$, assuming without loss of generality that at $x_{0}$ we have $\lambda_{1} \geqslant \frac{C}{\varepsilon^{3}}$.

Proof. It suffices to show that, at $x_{0}$,
$$\begin{aligned}
& (2-\varepsilon) \sum_{\alpha>1} \tilde{g}^{i \bar{i}} \frac{\left|e_{i}\left(\varphi_{V_{\alpha} V_{1}}\right)\right|^{2}}{\lambda_{1}\left(\lambda_{1}-\lambda_{\alpha}\right)}+\frac{\tilde{g}^{p \bar{p}} \tilde{g}^{q \bar{q}}\left|V_{1}\left(\tilde{g}_{p \bar{q}}\right)\right|^{2}}{\lambda_{1}}-(1+\varepsilon) \sum_{i \notin I} \frac{\tilde{g}^{i \bar{i}}\left|e_{i}\left(\varphi_{V_{1} V_{1}}\right)\right|^{2}}{\lambda_{1}^{2}} \\
& \quad \geqslant-3 \varepsilon \sum_{i \notin I} \frac{\tilde{g}^{i \bar{i}}\left|e_{i}\left(\varphi_{V_{1} V_{1}}\right)\right|^{2}}{\lambda_{1}^{2}}-\frac{C}{\varepsilon} \sum_{i} \tilde{g}^{i \bar{i}}
\end{aligned}$$
since, using $\left.d \hat{Q}\right|_{x_{0}}=0$,
$$\begin{aligned}
-3 \varepsilon \sum_{i \notin I} \frac{\tilde{g}^{i \bar{i}}\left|e_{i}\left(\varphi_{V_{1} V_{1}}\right)\right|^{2}}{\lambda_{1}^{2}} & =-3 \varepsilon \sum_{i \notin I} \tilde{g}^{i \bar{i}}\left|A e^{-A \varphi} e_{i}(\varphi)-h^{\prime} e_{i}\left(|\partial \varphi|_{g}^{2}\right)\right|^{2} \\
& \geqslant-6 \varepsilon A^{2} e^{-2 A \varphi} \tilde{g}^{i \bar{i}}\left|e_{i}(\varphi)\right|^{2}-\left.\left.6 \varepsilon\left(h^{\prime}\right)^{2} \sum_{i \notin I} \tilde{g}^{i \bar{i}}\left|e_{i}\right| \partial \varphi\right|_{g} ^{2}\right|^{2} .
\end{aligned}$$

We now prove (5.42). At $x_{0}$ we have
$$\begin{aligned}
0<\tilde{g}_{\tilde{1} \overline{1}}= & \tilde{g}\left(\tilde{e}_{1}, \overline{\bar{e}}_{1}\right)=g\left(\tilde{e}_{1}, \overline{\tilde{e}}_{1}\right)+\tilde{e}_{1} \overline{\tilde{e}}_{1}(\varphi)-\left[\tilde{e}_{1}, \overline{\tilde{e}}_{1}\right]^{(0,1)}(\varphi) \\
= & 1+\frac{1}{2}\left(V_{1} V_{1}(\varphi)+\left(J V_{1}\right)\left(J V_{1}\right)(\varphi)+\sqrt{-1}\left[V_{1}, J V_{1}\right](\varphi)\right)-\left[\tilde{e}_{1}, \overline{\tilde{e}}_{1}\right]^{(0,1)}(\varphi) \\
= & 1+\frac{1}{2}\left(\varphi_{V_{1} V_{1}}+\varphi_{J V_{1} J V_{1}}+\left(\nabla_{V_{1}} V_{1}\right)(\varphi)+\left(\nabla_{J V_{1}} J V_{1}\right)(\varphi)\right. \\
& \left.\quad+\sqrt{-1}\left[V_{1}, J V_{1}\right](\varphi)\right)-\left[\tilde{e}_{1}, \overline{\tilde{e}}_{1}\right]^{(0,1)}(\varphi) \\
\leqslant & \frac{1}{2}\left(\lambda_{1}+\sum_{\alpha>1} \lambda_{\alpha} \mu_{\alpha}^{2}\right)+C,
\end{aligned}$$
using that at $x_{0}$ we have, recalling (5.7) and (5.32),
$$\varphi_{V_{1} V_{1}}=g\left(\Phi\left(V_{1}\right), V_{1}\right)=\lambda_{1}, \quad \varphi_{J V_{1} J V_{1}}=g\left(\Phi\left(J V_{1}\right), J V_{1}\right)+B\left(J V_{1}, J V_{1}\right)=\sum_{\alpha>1} \lambda_{\alpha} \mu_{\alpha}^{2}+1 .$$
The proof splits into two cases.
Case (i). Assume that at $x_{0}$ we have
$$\frac{1}{2}\left(\lambda_{1}+\sum_{\alpha>1} \lambda_{\alpha} \mu_{\alpha}^{2}\right) \geqslant(1-\varepsilon) \tilde{g}_{\tilde{1} \tilde{1}}>0 .$$
Then Lemma 5.7 gives
$$\begin{aligned}
& (2-\varepsilon) \sum_{\alpha>1} \tilde{g}^{i \bar{i}} \frac{\left|e_{i}\left(\varphi_{V_{\alpha} V_{1}}\right)\right|^{2}}{\lambda_{1}\left(\lambda_{1}-\lambda_{\alpha}\right)}+\frac{\tilde{g}^{p \bar{p}} \tilde{g}^{q \bar{q}}\left|V_{1}\left(\tilde{g}_{p \bar{q}}\right)\right|^{2}}{\lambda_{1}}-(1+\varepsilon) \sum_{i \notin I} \frac{\tilde{g}^{i \bar{i}}\left|e_{i}\left(\varphi_{V_{1} V_{1}}\right)\right|^{2}}{\lambda_{1}^{2}} \\
& \quad \geqslant \sum_{i \notin I} \sum_{\alpha>1} \frac{\tilde{g}^{i \bar{i}}}{\lambda_{1}^{2}}\left(\frac{(2-\varepsilon) \lambda_{1}}{\lambda_{1}-\lambda_{\alpha}}\left|e_{i}\left(\varphi_{V_{\alpha} V_{1}}\right)\right|^{2}\right)+2 \sum_{q \in I} \sum_{i \notin I} \tilde{g}^{i \bar{i}} \tilde{g}^{q \bar{q}} \frac{\left|V_{1}\left(\tilde{g}_{i \bar{q}}\right)\right|^{2}}{\lambda_{1}} \\
& \quad-3 \varepsilon \sum_{i \notin I} \frac{\tilde{g}^{i \bar{i}}\left|e_{i}\left(\varphi_{V_{1} V_{1}}\right)\right|^{2}}{\lambda_{1}^{2}}-(1+\gamma)\left(\lambda_{1}+\sum_{\alpha>1} \lambda_{\alpha} \mu_{\alpha}^{2}\right) \sum_{q \in I} \sum_{i \notin I} \frac{\tilde{g}^{i \bar{i}} \tilde{g}^{q \bar{q}}}{\lambda_{1}^{2}}\left|V_{1}\left(\tilde{g}_{i \bar{q}}\right)\right|^{2} \\
& \quad-\frac{C}{\varepsilon} \sum_{i} \tilde{g}^{i \bar{i}}-(1-\varepsilon)\left(1+\frac{1}{\gamma}\right)\left(\lambda_{1}-\sum_{\alpha>1} \lambda_{\alpha} \mu_{\alpha}^{2}\right) \sum_{i \notin I} \sum_{\alpha>1} \frac{\tilde{g}^{i \bar{i}}}{\lambda_{1}^{2}} \frac{\left|e_{i}\left(\varphi_{V_{\alpha} V_{1}}\right)\right|^{2}}{\lambda_{1}-\lambda_{\alpha}},
\end{aligned}$$
and we can now choose
$$\gamma=\frac{\lambda_{1}-\sum_{\alpha>1} \lambda_{\alpha} \mu_{\alpha}^{2}}{\lambda_{1}+\sum_{\alpha>1} \lambda_{\alpha} \mu_{\alpha}^{2}}>0,$$
so that the second and fourth term on the right hand side cancel each other, while the first term dominates the last one, and this establishes (5.42).

Case (ii). Assume on the other hand that at $x_{0}$ we have
$$\frac{1}{2}\left(\lambda_{1}+\sum_{\alpha>1} \lambda_{\alpha} \mu_{\alpha}^{2}\right)<(1-\varepsilon) \tilde{g}_{\tilde{1} \tilde{1}} .$$
Then (5.43) gives
$$\tilde{g}_{\tilde{1} \tilde{1}} \leqslant \frac{1}{2}\left(\lambda_{1}+\sum_{\alpha>1} \lambda_{\alpha} \mu_{\alpha}^{2}\right)+C \leqslant(1-\varepsilon) \tilde{g}_{\tilde{1} \tilde{1}}+C,$$
and so
$$\tilde{g}_{\tilde{1} \overline{1}} \leqslant \frac{C}{\varepsilon} .$$
In general, (5.43) implies that
$$\lambda_{1}+\sum_{\alpha>1} \lambda_{\alpha} \mu_{\alpha}^{2} \geqslant-C,$$
and so
$$0<\lambda_{1}-\sum_{\alpha>1} \lambda_{\alpha} \mu_{\alpha}^{2} \leqslant 2 \lambda_{1}+C \leqslant\left(2+2 \varepsilon^{2}\right) \lambda_{1},$$
as long as $2 \lambda_{1} \geqslant C / \varepsilon^{2}$.
We now choose
$$\gamma=\frac{1}{\varepsilon^{2}},$$
where $\varepsilon$ still has to be chosen. This gives
$$\begin{aligned}
(1-\varepsilon)\left(1+\frac{1}{\gamma}\right)\left(\lambda_{1}-\sum_{\alpha>1} \lambda_{\alpha} \mu_{\alpha}^{2}\right) & \leqslant 2(1-\varepsilon)\left(1+\frac{1}{\gamma}\right)\left(1+\varepsilon^{2}\right) \lambda_{1} \\
& =2(1-\varepsilon)\left(1+\varepsilon^{2}\right)^{2} \lambda_{1} \leqslant(2-\varepsilon) \lambda_{1}
\end{aligned}$$
if $\varepsilon \leqslant \frac{1}{6}$, and from Lemma 5.7 we get
$$\begin{aligned}
& (2-\varepsilon) \sum_{\alpha>1} \tilde{g}^{i \bar{i}} \frac{\left|e_{i}\left(\varphi_{V_{\alpha} V_{1}}\right)\right|^{2}}{\lambda_{1}\left(\lambda_{1}-\lambda_{\alpha}\right)}+\frac{\tilde{g}^{p \bar{p}} \tilde{g}^{q \bar{q}}\left|V_{1}\left(\tilde{g}_{p \bar{q}}\right)\right|^{2}}{\lambda_{1}}-(1+\varepsilon) \sum_{i \notin I} \frac{\tilde{g}^{i \bar{i}}\left|e_{i}\left(\varphi_{V_{1} V_{1}}\right)\right|^{2}}{\lambda_{1}^{2}} \\
& \quad \geqslant 2 \sum_{q \in I} \sum_{i \notin I} \tilde{g}^{i \bar{i}} \tilde{g}^{q \bar{q}} \frac{\left|V_{1}\left(\tilde{g}_{i \bar{q}}\right)\right|^{2}}{\lambda_{1}}-3 \varepsilon \sum_{i \notin I} \frac{\tilde{g}^{i \bar{i}}\left|e_{i}\left(\varphi_{V_{1} V_{1}}\right)\right|^{2}}{\lambda_{1}^{2}} \\
& \quad-(1-\varepsilon)\left(1+\frac{1}{\varepsilon^{2}}\right) \tilde{g}_{\tilde{1} \bar{i}} \sum_{q \in I} \sum_{i \notin I} \frac{2 \tilde{g}^{i} \tilde{g}^{q \bar{q}}}{\lambda_{1}^{2}}\left|V_{1}\left(\tilde{g}_{i \bar{q}}\right)\right|^{2}-\frac{C}{\varepsilon} \sum_{i} \tilde{g}^{i \bar{i}}
\end{aligned}$$
But thanks to (5.46) we have
$$(1-\varepsilon)\left(1+\frac{1}{\varepsilon^{2}}\right) \tilde{g}_{\tilde{1} \tilde{1}} \leqslant(1-\varepsilon)\left(1+\frac{1}{\varepsilon^{2}}\right) \frac{C}{\varepsilon} \leqslant \frac{C}{\varepsilon^{3}},$$
and so
$$\begin{aligned}
& (2-\varepsilon) \sum_{\alpha>1} \tilde{g}^{i \bar{i}} \frac{\left|e_{i}\left(\varphi_{V_{\alpha} V_{1}}\right)\right|^{2}}{\lambda_{1}\left(\lambda_{1}-\lambda_{\alpha}\right)}+\frac{\tilde{g}^{p \bar{p}} \tilde{g}^{q \bar{q}}\left|V_{1}\left(\tilde{g}_{p \bar{q}}\right)\right|^{2}}{\lambda_{1}}-(1+\varepsilon) \sum_{i \notin I} \frac{\tilde{g}^{i \bar{i}}\left|e_{i}\left(\varphi_{V_{1} V_{1}}\right)\right|^{2}}{\lambda_{1}^{2}} \\
& \quad \geqslant\left(\lambda_{1}-\frac{C}{\varepsilon^{3}}\right) 2 \sum_{q \in I} \sum_{i \notin I} \tilde{g}^{i \bar{i}} \tilde{g}^{q \bar{q}} \frac{\left|V_{1}\left(\tilde{g}_{i \bar{q}}\right)\right|^{2}}{\lambda_{1}^{2}}-3 \varepsilon \sum_{i \notin I} \frac{\tilde{g}^{i \bar{i}}\left|e_{i}\left(\varphi_{V_{1} V_{1}}\right)\right|^{2}}{\lambda_{1}^{2}}-\frac{C}{\varepsilon} \sum_{i} \tilde{g}^{i \bar{i}} \\
& \quad \geqslant-3 \varepsilon \sum_{i \notin I} \frac{\tilde{g}^{i \bar{i}}\left|e_{i}\left(\varphi_{V_{1} V_{1}}\right)\right|^{2}}{\lambda_{1}^{2}}-\frac{C}{\varepsilon} \sum_{i} \tilde{g}^{i \bar{i}},
\end{aligned}$$
provided $\lambda_{1} \geqslant \frac{C}{\varepsilon^{3}}$ at $x_{0}$. \(\square\)

We now complete the proof of Proposition 5.1. Combining Lemmas 5.4. 5.5 and 5.8, and recalling that $h^{\prime \prime}=2\left(h^{\prime}\right)^{2}$, we have
$$\begin{aligned}
0 \geqslant & -6 \varepsilon A^{2} e^{-2 A \varphi} \tilde{g}^{i \bar{i}}\left|e_{i}(\varphi)\right|^{2}-\left.\left.6 \varepsilon\left(h^{\prime}\right)^{2} \sum_{i \notin I} \tilde{g}^{i \bar{i}}\left|e_{i}\right| \partial \varphi\right|_{g} ^{2}\right|^{2} \\
& -\left.\left.2\left(h^{\prime}\right)^{2} \sum_{i \in I} \tilde{g}^{i \bar{i}}\left|e_{i}\right| \partial \varphi\right|_{g} ^{2}\right|^{2}+\frac{h^{\prime}}{2} \sum_{k} \tilde{g}^{i \bar{i}}\left(\left|e_{i} e_{k}(\varphi)\right|^{2}+\left|e_{i} \bar{e}_{k}(\varphi)\right|^{2}\right) \\
& +\left.\left.h^{\prime \prime} \tilde{g}^{i \bar{i}}\left|e_{i}\right| \partial \varphi\right|_{g} ^{2}\right|^{2}+\left(A e^{-A \varphi}-\frac{C_{1}}{\varepsilon}\right) \sum_{i} \tilde{g}^{i \bar{i}}+A^{2} e^{-A \varphi} \tilde{g}^{i \bar{i}}\left|e_{i}(\varphi)\right|^{2}-A n e^{-A \varphi} \\
& \geqslant\left(A e^{-A \varphi}-\frac{C_{1}}{\varepsilon}\right) \sum_{i} \tilde{g}^{i \bar{i}}+\frac{h^{\prime}}{2} \sum_{k} \tilde{g}^{i \bar{i}}\left(\left|e_{i} e_{k}(\varphi)\right|^{2}+\left|e_{i} \bar{e}_{k}(\varphi)\right|^{2}\right) \\
& +\left(A^{2} e^{-A \varphi}-6 \varepsilon A^{2} e^{-2 A \varphi}\right) \tilde{g}^{i \bar{i}}\left|e_{i}(\varphi)\right|^{2}-A n e^{-A \varphi},
\end{aligned}$$
as long as $\varepsilon \leqslant \frac{1}{6}$, where $C_{1}$ is uniform constant. We now make our choices of $A$ and $\varepsilon$. First choose
$$A=6 C_{1}+1,$$
and, at the expense of increasing $C_{1}$, we may assume that
$$A \geqslant \max \left(C_{0}+1,6 n \sup _{M}|\partial \varphi|_{g}^{2}\right)$$
which we needed earlier in (5.25) and Lemma 5.5. Next pick
$$\varepsilon=\frac{e^{A \varphi\left(x_{0}\right)}}{6} \leqslant \frac{1}{6},$$
so that
$$A e^{-A \varphi\left(x_{0}\right)}-\frac{C_{1}}{\varepsilon}=e^{-A \varphi\left(x_{0}\right)} \geqslant 1, \quad A^{2} e^{-A \varphi\left(x_{0}\right)}-6 \varepsilon A^{2} e^{-2 A \varphi\left(x_{0}\right)}=0 .$$
Note that now that the values of $\varepsilon$ and $A$ have been fixed, we may indeed assume without loss of generality that at $x_{0}$ we have $\lambda_{1} \geqslant \frac{C}{\varepsilon^{3}}$ and $\lambda_{1} \geqslant \frac{C_{A}}{\varepsilon}$. We conclude that at $x_{0}$ we have
$$\sum_{i} \tilde{g}^{i \bar{i}}+\frac{h^{\prime}}{2} \sum_{k} \tilde{g}^{i \bar{i}}\left(\left|e_{i} e_{k}(\varphi)\right|^{2}+\left|e_{i} \bar{e}_{k}(\varphi)\right|^{2}\right) \leqslant C .$$

From this it follows that at $x_{0}$ we have $\sum_{i} \tilde{g}^{i \bar{i}} \leqslant C$, and so using again (5.26) we see that $\tilde{g}$ is uniformly equivalent to $g$, and from (5.47) we have $\sum_{i, k}\left(\left|e_{i} e_{k}(\varphi)\right|^{2}+\left|e_{i} \bar{e}_{k}(\varphi)\right|^{2}\right) \leqslant C$, which (as in (5.21), (5.22), (5.23)) implies that $\sum_{\alpha, \beta}\left|\nabla_{\alpha \beta}^{2} \varphi\right| \leqslant C$, and so $\lambda_{1}\left(x_{0}\right) \leqslant C$, and hence $Q\left(x_{0}\right) \leqslant C$, as desired. \(\square\)

\section*{6. Completion of the proofs of the Main Theorems}

In this section, we complete the proofs of the main results stated in the introduction.

Proof of Theorem 1.2. Thanks to Propositions 3.1 and 5.1, we can obtain a priori $C^{2, \alpha}$ estimates from the main result of [44], for some $0<\alpha<1$ (and in fact for all $0<\alpha<1$ by [10]). Higher order estimates follow after differentiating the equation and applying the usual bootstrapping method. \(\square\)

Our main result now follows easily:
Proof of Theorem 1.1. Now we have Theorem 1.2, we can follow closely the arguments of [45]. Indeed, we will see that the $(1,1)$ form $\sqrt{-1} \partial \bar{\partial} \varphi=$ $\frac{1}{2}(d(J d \varphi))^{(1,1)}$ has the right properties for this part of the proof to go through essentially unchanged from the integrable case. We include the brief arguments for the sake of completeness. Consider the family of equations
$$\left(\omega+\sqrt{-1} \partial \bar{\partial} \varphi_{t}\right)^{n}=e^{t F+b_{t}} \omega^{n}, \quad \omega+\sqrt{-1} \partial \bar{\partial} \varphi_{t}>0,$$
for $t \in[0,1]$, where $b_{t} \in \mathbb{R}$. For a fixed $\alpha \in(0,1)$, we define $\mathcal{T}$ to be the set of $t \in[0,1]$ such that (6.1) admits a solution $\left(\varphi_{t}, b_{t}\right) \in C^{3, \alpha}(M) \times \mathbb{R}$. Clearly $0 \in \mathcal{T}$. We will show that $\mathcal{T}$ is open and closed, since this will show that $1 \in \mathcal{T}$, and then adding a constant to $\varphi_{1}$ we will obtain a solution of (1.3).

To prove that $\mathcal{T}$ is open, fix $\hat{t} \in \mathcal{T}$, and write $\hat{\omega}:=\omega+\sqrt{-1} \partial \bar{\partial} \varphi_{\hat{t}}$. From Theorem 2.1, there exists a smooth $\hat{u}$ such that $e^{\hat{u}} \hat{\omega}$ is Gauduchon, and we may assume that $\int_{M} e^{(n-1) \hat{u}} \hat{\omega}^{n}=1$. Define a map $\Psi$ by
$$\Psi(\psi)=\log \frac{(\hat{\omega}+\sqrt{-1} \partial \bar{\partial} \psi)^{n}}{\hat{\omega}^{n}}-\log \left(\int_{M} e^{(n-1) \hat{u}}(\hat{\omega}+\sqrt{-1} \partial \bar{\partial} \psi)^{n}\right),$$
which takes $\psi \in C^{3, \alpha}(M)$ with $\int_{M} \psi e^{(n-1) \hat{u}} \hat{\omega}^{n}=0$ and $\hat{\omega}+\sqrt{-1} \partial \bar{\partial} \psi>0$ to a $C^{1, \alpha}(M)$ function $h$ satisfying $\int_{M} e^{h} e^{(n-1) \hat{u}} \hat{\omega}^{n}=1$. For $t$ close to $\hat{t}$ we wish to solve
$$\Psi\left(\psi_{t}\right)=(t-\hat{t}) F-\log \left(\int_{M} e^{(t-\hat{t}) F} e^{(n-1) \hat{u}} \hat{\omega}^{n}\right) .$$
Observe that $\Psi(0)=0$, and that the linearization of $\Psi$ at $\psi=0$ is given by the canonical Laplacian (see (2.4)) of $\hat{\omega}$,
$$\eta \mapsto \Delta_{\hat{\omega}}^{C} \eta,$$
since $\int_{M} \sqrt{-1} \partial \bar{\partial} \eta \wedge e^{(n-1) \hat{u}} \hat{\omega}^{n-1}=0$ (which follows from integration by parts, as in (2.10), and the fact that $e^{\hat{u}} \hat{\omega}$ is Gauduchon). By Theorem 2.2, the operator (6.3) is an invertible map of the tangent spaces, and so by the Inverse Function Theorem we obtain $\psi_{t}$ solving (6.2) for $t$ close to $\hat{t}$. Then $\varphi_{t}=\varphi_{\hat{t}}+\psi_{t}$ solves (6.1) for $t$ close to $\hat{t}$, for $b_{t} \in \mathbb{R}$, showing that $\mathcal{T}$ is open.

To prove that $\mathcal{T}$ is closed we will apply Theorem 1.2. Suppose $\varphi_{t} \in$ $C^{3, \alpha}(M)$ solves (6.1). Then, as above, we can differentiate the equation and bootstrap to obtain that $\varphi_{t}$ is smooth. Applying the maximum principle (2.11) to $\varphi_{t}$ in (6.1) we obtain the bound $\left|b_{t}\right| \leqslant \sup _{M}|F|$. We may add a $t$-dependent constant to $\varphi_{t}$ solving (6.1) so that $\sup _{M} \varphi_{t}=0$. Now we apply Theorem 1.2 to $\varphi_{t}$ to obtain $C^{3, \alpha}$ (in fact, $C^{\infty}$ ) estimates which are independent of $t$. This shows that $\mathcal{T}$ is closed. Hence we have proved the existence of a $C^{3, \alpha}$, and hence smooth, solution of (1.3).

It remains to prove uniqueness. Assume that we have two solutions $(\varphi, b)$ and $\left(\varphi^{\prime}, b^{\prime}\right)$ of (1.3). Writing $\theta=\varphi-\varphi^{\prime}$, we have
$$\frac{\left(\omega+\sqrt{-1} \partial \bar{\partial} \varphi^{\prime}+\sqrt{-1} \partial \bar{\partial} \theta\right)^{n}}{\left(\omega+\sqrt{-1} \partial \bar{\partial} \varphi^{\prime}\right)^{n}}=e^{b-b^{\prime}} .$$
Applying (2.11) at the extrema of $\theta$ we obtain $b=b^{\prime}$. Then
$$(\omega+\sqrt{-1} \partial \bar{\partial} \varphi)^{n}=\left(\omega+\sqrt{-1} \partial \bar{\partial} \varphi^{\prime}\right)^{n}$$
and so
$$\sqrt{-1} \partial \bar{\partial} \partial \wedge \sum_{i=0}^{n-1}(\omega+\sqrt{-1} \partial \bar{\partial} \varphi)^{i} \wedge\left(\omega+\sqrt{-1} \partial \bar{\partial} \varphi^{\prime}\right)^{n-1-i}=0$$
The strong maximum principle (together with the fact that $\sup _{M} \varphi=\sup _{M} \varphi^{\prime}=$ 0) implies that $\theta=0$, namely $\varphi=\varphi^{\prime}$. This completes the proof. \(\square\)

\section*{References}
\begin{itemize}
\item[] [1] Alesker, S., Shelukhin, E. On a uniform estimate for the quaternionic Calabi problem, Israel J. Math. 197 (2013), no. 1, 309-327.
\item[] [2] Besse, A.L. Einstein manifolds, Classics in Mathematics. Springer-Verlag, Berlin, 2008.
\item[] [3] Błocki, Z. On uniform estimate in Calabi-Yau theorem, Sci. China Ser. A 48 (2005), suppl., 244-247.
\item[] [4] Błocki, Z. On the uniform estimate in the Calabi-Yau theorem, II, Sci. China Math. 54 (2011), no. 7, 1375-1377.
\item[] [5] Błocki, Z. On geodesics in the space of Kähler metrics, in Advances in geometric analysis, 3-19, Adv. Lect. Math. (ALM), 21, Int. Press, Somerville, MA, 2012.
\item[] [6] Buzano, E., Fino, A., Vezzoni, L. The Calabi-Yau equation on the Kodaira-Thurston manifold, viewed as an $S^{1}$-bundle over a 3-torus, J. Differential Geom. 101 (2015), no. 2, 175-195.
\item[] [7] Cao, H.-D., Deformation of Kähler metrics to Kähler-Einstein metrics on compact Kähler manifolds, Invent. Math. 81 (1985), no. 2, 359-372.
\item[] [8] Cherrier, P. Équations de Monge-Ampère sur les variétés Hermitiennes compactes, Bull. Sc. Math. (2) 111 (1987), 343-385.
\end{itemize}
\begin{itemize}
\item[] [9] Chu, J. The complex Monge-Ampère equation on some compact Hermitian manifolds, Pacific J. Math. 276 (2015), no. 2, 369-386.
\item[] [10] Chu, J. $C^{2, \alpha}$ regularities and estimates for nonlinear elliptic and parabolic equations in geometry, Calc. Var. Partial Differential Equations 55 (2016), no. 1, 55:8.
\item[] [11] Coupet, B., Gaussier, H., Sukhov, A. Some aspects of analysis on almost complex manifolds with boundary, Complex analysis, J. Math. Sci. (N. Y.) 154 (2008), no. 6, 923-986.
\item[] [12] Delanöe, P. Sur l'analogue presque-complexe de l'équation de Calabi-Yau, Osaka J. Math. 33 (1996), no. 4, 829-846.
\item[] [13] Delanöe, P. An $L^{\infty}$ a priori estimate for the Calabi-Yau operator on compact almost-Kähler manifolds, Gen. Math. 5 (1997), 145-149.
\item[] [14] Dinew, S., Kołodziej, S. Pluripotential estimates on compact Hermitian manifolds, in Advances in geometric analysis, 69-86, Adv. Lect. Math. (ALM), 21, Int. Press, Somerville, MA, 2012.
\item[] [15] Donaldson, S.K. Two-forms on four-manifolds and elliptic equations, in Inspired by S.S. Chern, World Scientific, 2006.
\item[] [16] Fino, A., Li, Y.Y., Salamon, S., Vezzoni, L. The Calabi-Yau equation on 4-manifolds over 2-tori, Trans. Amer. Math. Soc. 365 (2013), no. 3, 1551-1575.
\item[] [17] Fu, J., Wang, Z., Wu, D. Form-type Calabi-Yau equations, Math. Res. Lett. 17 (2010), no. 5, 887-903.
\item[] [18] Fu, J., Wang, Z., Wu, D. Form-type Calabi-Yau equations on Kähler manifolds of nonnegative orthogonal bisectional curvature, Calc. Var. Partial Differential Equations 52 (2015), no. 1-2, 327-344.
\item[] [19] Fu, J., Yau, S.-T. The theory of superstring with flux on non-Kähler manifolds and the complex Monge-Ampère equation, J. Differential Geom. 78 (2008), no. 3, 369-428.
\item[] [20] Gauduchon, P. Le théorème de l'excentricité nulle, C. R. Acad. Sci. Paris Sér. A-B 285 (1977), no. 5, A387-A390.
\item[] [21] Gauduchon, P. La 1-forme de torsion d'une variété hermitienne compacte, Math. Ann. 267 (1984), 495-518.
\item[] [22] Gauduchon, P. Calabi's extremal Kähler metrics: An elementary introduction, book in preparation.
\item[] [23] Gill, M. Convergence of the parabolic complex Monge-Ampère equation on compact Hermitian manifolds, Comm. Anal. Geom. 19 (2011), no. 2, 277-303.
\item[] [24] Guan, B., Li, Q. Complex Monge-Ampère equations and totally real submanifolds, Adv. Math. 225 (2010), no. 3, 1185-1223.
\item[] [25] Haggui, F. Fonctions PSH sur une variété presque complexe, C. R. Math. Acad. Sci. Paris 335 (2002), no. 6, 509-514.
\item[] [26] Harvey, F. R., Lawson, H. B. Dirichlet duality and the nonlinear Dirichlet problem on Riemannian manifolds, J. Differential Geom. 88 (2011), no. 3, 395-482.
\item[] [27] Harvey, F.R., Lawson, H.B. Potential theory on almost complex manifolds, Ann. Inst. Fourier (Grenoble) 65 (2015), no. 1, 171-210.
\item[] [28] Harvey, F.R., Lawson, H.B., Pliś, S. Smooth approximation of plurisubharmonic functions on almost complex manifolds, Math. Ann. 366 (2016), no. 3-4, 929-940.
\item[] [29] Kołodziej, S., Nguyen, N.C. Weak solutions to the complex Monge-Ampère equation on Hermitian manifolds, in Analysis, complex geometry, and mathematical physics: in honor of Duong H. Phong, 141-158, Contemp. Math., 644, Amer. Math. Soc., Providence, RI, 2015.
\item[] [30] Kołodziej, S., Nguyen, N.C. Stability and regularity of solutions of the Monge-Ampère equation on Hermitian manifolds, preprint, arXiv:1501.05749
\item[] [31] Li, J., Yau, S.-T. The existence of supersymmetric string theory with torsion, J. Differential Geom. 70 (2005), no. 1, 143-181.
\item[] [32] Nguyen, N.C. The complex Monge-Ampère type equation on compact Hermitian manifolds and applications, Adv. Math. 286 (2016), 240-285.
\end{itemize}
\begin{itemize}
\item[] [33] Pali, N. Fonctions plurisousharmoniques et courants positifs de type $(1,1)$ sur une variété presque complexe, Manuscripta Math. 118 (2005), no. 3, 311-337.
\item[] [34] Phong, D.H., Picard, S., Zhang, X. On estimates for the Fu-Yau generalization of a Strominger system, to appear in J. reine angew. Math.
\item[] [35] Phong, D.H., Song, J., Sturm, J. Complex Monge Ampère Equations, in Surveys in Differential Geometry 17, 327-411, International Press, 2012.
\item[] [36] Pliś, S. The Monge-Ampère equation on almost complex manifolds, Math. Z. 276 (2014), 969-983.
\item[] [37] Pliś, S. Monge-Ampère operator on four dimensional almost complex manifolds, J. Geom. Anal. 26 (2016), no. 4, 2503-2518.
\item[] [38] Popovici, D. Aeppli cohomology classes associated with Gauduchon metrics on compact complex manifolds, Bull. Soc. Math. France 143 (2015), no. 4, 763-800.
\item[] [39] Spruck, J. Geometric aspects of the theory of fully nonlinear elliptic equations, Global theory of minimal surfaces, Amer. Math. Soc., Providence, RI, 2005, 283-309.
\item[] [40] Székelyhidi, G. Fully non-linear elliptic equations on compact Hermitian manifolds, to appear in J. Differential Geom.
\item[] [41] Székelyhidi, G., Tosatti, V., Weinkove, B. Gauduchon metrics with prescribed volume form, preprint, arXiv:1503.04491
\item[] [42] Tian, G., Zhang, Z. On the Kähler-Ricci flow on projective manifolds of general type, Chinese Ann. Math. Ser. B 27 (2006), no. 2, 179-192.
\item[] [43] Tosatti, V. A general Schwarz lemma for almost-Hermitian manifolds, Comm. Anal. Geom. 15 (2007), no. 5, 1063-1086.
\item[] [44] Tosatti, V., Wang, Y., Weinkove, B., Yang, X. $C^{2, \alpha}$ estimates for nonlinear elliptic equations in complex and almost complex geometry, Calc. Var. Partial Differential Equations 54 (2015), no. 1, 431-453.
\item[] [45] Tosatti, V., Weinkove, B. Estimates for the complex Monge-Ampère equation on Hermitian and balanced manifolds, Asian J. Math. 14 (2010), no. 1, 19-40.
\item[] [46] Tosatti, V., Weinkove, B. The complex Monge-Ampère equation on compact Hermitian manifolds, J. Amer. Math. Soc. 23 (2010), no.4, 1187-1195.
\item[] [47] Tosatti, V., Weinkove, B. The Calabi-Yau equation, symplectic forms and almost complex structures, in Geometry and Analysis, No. 1, 475-493, Advanced Lectures in Math. 17, International Press, 2011.
\item[] [48] Tosatti, V., Weinkove, B. The Calabi-Yau equation on the Kodaira-Thurston manifold, J. Inst. Math. Jussieu 10 (2011), no. 2 437-447.
\item[] [49] Tosatti, V., Weinkove, B. On the evolution of a Hermitian metric by its Chern-Ricci form, J. Differential Geom. 99 (2015), no. 1, 125-163.
\item[] [50] Tosatti, V., Weinkove, B. The Monge-Ampère equation for (n-1)-plurisubharmonic functions on a compact Kähler manifold, J. Amer. Math. Soc. 30 (2017), no.2, 311-346.
\item[] [51] Tosatti, V., Weinkove, B. Hermitian metrics, (n-1,n-1) forms and Monge-Ampère equations, to appear in J. reine angew. Math.
\item[] [52] Tosatti, V., Weinkove, B., Yau, S.-T. Taming symplectic forms and the Calabi-Yau equation, Proc. London Math. Soc. 97 (2008), no. 2, 401-424.
\item[] [53] Wang, H., Zhu, P. On a generalized Calabi-Yau equation, Ann. Inst. Fourier (Grenoble) 60 (2010), no. 5, 1595-1615.
\item[] [54] Warren, M., Yuan, Y. Hessian estimates for the sigma-2 equation in dimension 3, Comm. Pure Appl. Math. 62 (2009), no. 3, 305-321.
\item[] [55] Weinkove, B. The Calabi-Yau equation on almost-Kähler four-manifolds, J. Differential Geom. 76 (2007), no. 2, 317-349.
\item[] [56] Yau, S.-T. On the Ricci curvature of a compact Kähler manifold and the complex Monge-Ampère equation, I, Comm. Pure Appl. Math. 31 (1978), no. 3, 339-411.
\item[] [57] Zhang, X. A priori estimates for complex Monge-Ampère equation on Hermitian manifolds, Int. Math. Res. Not. IMRN 2010, no. 19, 3814-3836.
\end{itemize}
\begin{itemize}
\item[] [58] Zhang, X., Zhang, X. Regularity estimates of solutions to complex Monge-Ampère equations on Hermitian manifolds, J. Funct. Anal. 260 (2011), no. 7, 2004-2026.
\end{itemize}

School of Mathematical Sciences, Peking University, Yiheyuan Road 5, Beijing, P.R.China, 100871

Department of Mathematics, Northwestern University, 2033 Sheridan Road, Evanston, IL 60208

Department of Mathematics, Northwestern University, 2033 Sheridan Road, Evanston, IL 60208