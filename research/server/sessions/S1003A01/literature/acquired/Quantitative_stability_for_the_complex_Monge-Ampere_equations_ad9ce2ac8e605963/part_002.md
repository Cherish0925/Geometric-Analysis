---
retention_scope: session
part: 2
total_parts: 3
---

[Part 2/3 of: Quantitative stability for the complex Monge-Ampere equations]

Proof. Let $u_{j}, \psi_{j}(j=1,2)$ be as in the statement of Theorem 3.1. For every $k>0$, we denote $u_{j, k}:=\max \left\{u_{j}, \phi-k\right\}$ and $\psi_{j, k}=\max \left\{\psi_{j}, \phi-k\right\}$. By Lemma 2.7, there exists a constant $C_{1}>0$ depending only on $n$ and $M$ such that
$$E_{\tilde{\chi}, \theta, \phi}^{0}\left(u_{j, k}\right)+E_{\tilde{\chi}, \theta, \phi}^{0}\left(\psi_{j, k}\right) \leq C_{1} B,$$
for $j=1,2$ and for every $k>0$. Therefore, by the assumption, there exists a constant $C_{2}>0$ depending only on $n$ and $M$ such that
$$\int_{X}-\chi\left(u_{1, k}-u_{2, k}\right)\left(\theta_{\psi_{1, l}}^{n}-\theta_{\psi_{2, l}}^{n}\right) \leq C_{2} \varrho B^{2}(1-\tilde{\chi}(-1))^{2} Q^{\circ(n)}\left(I_{\chi}^{0}\left(u_{1, k}, u_{2, k}\right)\right),$$
for every $k, l>0$. Letting $l \rightarrow \infty$ and using [18, Theorem 2.2], we get
$$\int_{X}-\chi\left(u_{1, k}-u_{2, k}\right)\left(\theta_{\psi_{1}}^{n}-\theta_{\psi_{2}}^{n}\right) \leq C_{2} \varrho B^{2}(1-\tilde{\chi}(-1))^{2} Q^{\circ(n)}\left(I_{\chi}^{0}\left(u_{1, k}, u_{2, k}\right)\right)$$
for every $k>0$. We will show that
$$I_{\chi}\left(u_{1}, u_{2}\right)=\lim _{k \rightarrow \infty} I_{\chi}\left(u_{1, k}, u_{2, k}\right) .$$
Denote
$$f:=\chi\left(u_{1}-u_{2}\right)\left(\theta_{u_{2}}^{n}-\theta_{u_{1}}^{n}\right), \quad f_{k}:=\chi\left(u_{1, k}-u_{2, k}\right)\left(\theta_{u_{2, k}}^{n}-\theta_{u_{1, k}}^{n}\right) .$$

We have
$$\begin{aligned}
I_{\chi}\left(u_{1, k}, u_{2, k}\right)=\int_{X} f_{k} & =\int_{\left\{u_{1}>\phi-k\right\}} f_{k}+\int_{\left\{u_{1} \leq \phi-k\right\}} f_{k} \\
& =\int_{\left\{u_{1}>\phi-k\right\}} f+\int_{\left\{u_{1} \leq \phi-k\right\}} f_{k} \\
& =I_{\chi}\left(u_{1}, u_{2}\right)-\int_{\left\{u_{1} \leq \phi-k\right\}} f+\int_{\left\{u_{1} \leq \phi-k\right\}} f_{k} .
\end{aligned}$$
Then
$$\begin{aligned}
\left|I_{\chi}\left(u_{1, k}, u_{2, k}\right)-I_{\chi}\left(u_{1}, u_{2}\right)\right| & =\left|\int_{\left\{u_{1} \leq \phi-k\right\}} f+\int_{\left\{u_{1} \leq \phi-k\right\}} f_{k}\right| \\
& \leq \int_{\left\{u_{1} \leq \phi-k\right\}} \mu+\int_{\left\{u_{1} \leq \phi-k\right\}}-\chi\left(u_{1, k}-u_{2, k}\right)\left(\theta_{u_{2, k}}^{n}+\theta_{u_{1, k}}^{n}\right) \\
& \leq \int_{\left\{u_{1} \leq \phi-k\right\}} \mu+\int_{\left\{u_{1} \leq \phi-k\right\}}-\chi(-k)\left(\theta_{u_{2, k}}^{n}+\theta_{u_{1, k}}^{n}\right),
\end{aligned}$$
where $\mu=-\chi\left(u_{1}-\phi\right)\left(\theta_{u_{1}}^{n}+\theta_{u_{2}}^{n}\right)$. By Lemma 2.7, we have $\int_{X} \mu<\infty$. Then it follows from Lebesgue's dominated convergence theorem that $\lim _{k \rightarrow \infty} \int_{\left\{u_{1} \leq \phi-k\right\}} \mu=0$. Therefore,
$$\limsup _{k \rightarrow \infty}\left|I_{\chi}\left(u_{1, k}, u_{2, k}\right)-I_{\chi}\left(u_{1}, u_{2}\right)\right| \leq \limsup _{k \rightarrow \infty} \int_{\left\{u_{1} \leq \phi-k\right\}}-\chi(-k)\left(\theta_{u_{1, k}}^{n}+\theta_{u_{2, k}}^{n}\right) .$$
By the fact that
$$\int_{X} \theta_{u_{1, k}}^{n}=\int_{X} \theta_{u_{1, k}}^{n}=\int_{X} \theta_{\phi}^{n}, \quad \mathbf{1}_{\left\{u_{1} \leq \phi-k\right\}} \theta_{u_{j, k}}^{n}=\mathbf{1}_{\left\{u_{1} \leq \phi-k\right\}} \theta_{u_{j}}^{n} \quad(j=1,2),$$
we have
$$-\chi(-k) \int_{\left\{u_{1} \leq \phi-k\right\}}\left(\theta_{u_{1, k}}^{n}+\theta_{u_{2, k}}^{n}\right)=-\chi(-k) \int_{\left\{u_{1} \leq \phi-k\right\}}\left(\theta_{u_{1}}^{n}+\theta_{u_{2}}^{n}\right) \leq \int_{\left\{u_{1} \leq \phi-k\right\}} \mu .$$
By using (3.6), (3.7) and the fact $\lim _{k \rightarrow \infty} \int_{\left\{u_{1} \leq \phi-k\right\}} \mu=0$, we get (3.5). Now, combining (3.4) and (3.5), we obtain
$$\int_{X}-\chi\left(u_{1}-u_{2}\right)\left(\theta_{\psi_{1}}^{n}-\theta_{\psi_{2}}^{n}\right) \leq C_{2} \varrho B^{2}(1-\tilde{\chi}(-1))^{2} Q^{\circ(n)}\left(I_{\chi}^{0}\left(u_{1}, u_{2}\right)\right) .$$
The proof is completed. \(\square\)

Lemma 3.4. Let $M \geq 1$ and $\chi, \tilde{\chi} \in \widetilde{\mathcal{W}}^{-} \cup \mathcal{W}_{M}^{+}$such that $\tilde{\chi} \leq \chi$ and $\chi \in \mathscr{C}^{1}(\mathbb{R})$. Let $u_{1}, u_{2}, \ldots, u_{n+2} \in \mathcal{E}(X, \theta, \phi)$ such that $u_{1} \leq u_{2}$ and $u_{j}-\phi$ is bounded $(j=1,2, \ldots, n+2)$, where $\phi$ is a negative $\theta$-psh function satisfying $\varrho:=\operatorname{vol}\left(\theta_{\phi}\right)>0$. Denote
$$T=\theta_{u_{4}} \wedge \ldots \wedge \theta_{u_{n+2}}, \quad I=\left|\int_{X} \chi^{\prime}\left(u_{1}-u_{2}\right) d\left(u_{1}-u_{2}\right) \wedge d^{c}\left(u_{1}-u_{3}\right) \wedge T\right|,$$
and
$$J=\int_{X} \chi^{\prime}\left(u_{1}-u_{2}\right) d\left(u_{1}-u_{2}\right) \wedge d^{c}\left(u_{1}-u_{2}\right) \wedge T .$$
Then there exists $C>0$ depending only on $n$ and $M$ such that
$$I \leq C \varrho B(1-\tilde{\chi}(-1)) Q(J / \varrho),$$
where $B:=\sum_{j=1}^{n+2} \max \left\{E_{\tilde{\chi}, \theta, \phi}^{0}\left(u_{j}\right), 1\right\}$ and $Q$ is defined by (3.1).
Clearly if $\chi \in \widetilde{\mathcal{W}}^{-}$, then the above constant $C$ does not depend on $M$.
Proof. In this proof, we use the symbols $\lesssim$ and $\gtrsim$ for inequalities modulo a constant depending only on $n$ and $M$. By Theorem 2.2 and Lemma 2.7, we have
$$I=\left|\int_{X}-\chi\left(u_{1}-u_{2}\right) d d^{c}\left(u_{1}-u_{3}\right) \wedge T\right| \lesssim \varrho B=\varrho B Q(1) .$$
Therefore, without loss of generality, we can assume that $J / \varrho<1$. Approximating $u_{3}$ by $u_{3}-\delta$ with $\delta \searrow 0$, we can assume that $u_{3}<\phi$ on $X$.

For each $0<\epsilon<1 / 2$ we denote
$$U(\epsilon)=\left\{u_{1}-u_{2}<\epsilon\left(u_{1}+u_{3}-2 \phi\right)\right\}, V(\epsilon)=\left\{u_{1}-u_{2}>\epsilon\left(u_{1}+u_{3}-2 \phi\right)\right\},$$
and $\Gamma(\epsilon)=\left\{u_{1}-u_{2}=\epsilon\left(u_{1}+u_{3}-2 \phi\right)\right\}$. Since $\Gamma\left(\epsilon_{1}\right) \cap \Gamma\left(\epsilon_{2}\right)=\emptyset$ for every $\epsilon_{1} \neq \epsilon_{2}$ (note $u_{3}<\phi$ ), we have
$$\int_{\Gamma(\epsilon)} d\left(u_{1}-u_{3}\right) \wedge d^{c}\left(u_{1}-u_{3}\right) \wedge T=0$$
for almost everywhere $\epsilon \in(0,1 / 2)$.
Let $0<\epsilon<1 / 2$ be a constant satisfying (3.8). To simplify the notation, from now on, we write $U, V, \Gamma$ for $U(\epsilon), V(\epsilon), \Gamma(\epsilon)$ respectively. Denote
$$\tilde{u}_{1}=\frac{u_{1}+\epsilon u_{3}}{1+\epsilon}, \quad \tilde{u}_{2}=\max \left\{\frac{u_{2}+\epsilon u_{3}}{1+\epsilon}, \quad \frac{(1-\epsilon) u_{1}+2 \epsilon \phi}{1+\epsilon}\right\} \quad \text { and } \quad \tilde{\varphi}=\tilde{u}_{1}-\tilde{u}_{2} .$$
Then $\varphi:=\left(u_{1}-u_{2}\right)=(1+\epsilon) \tilde{\varphi}$ on $U$. Hence
$$\begin{aligned}
I & =\left|\int_{X}-\chi(\varphi) d d^{c}\left(u_{1}-u_{3}\right) \wedge T\right| \\
& \leq\left|\int_{U}-\chi(\varphi) d d^{c}\left(u_{1}-u_{3}\right) \wedge T\right|+\left|\int_{X \backslash U}-\chi(\varphi) d d^{c}\left(u_{1}-u_{3}\right) \wedge T\right| \\
& \leq\left|\int_{U}-\chi((1+\epsilon) \tilde{\varphi}) d d^{c}\left(u_{1}-u_{3}\right) \wedge T\right|+\left|\int_{X \backslash U}-\chi(\varphi)\left(\theta_{u_{1}}+\theta_{u_{3}}\right) \wedge T\right| \\
& \leq\left|\int_{U}-\chi((1+\epsilon) \tilde{\varphi}) d d^{c}\left(u_{1}-u_{3}\right) \wedge T\right|+\left|\int_{X \backslash U}-\chi\left(\epsilon\left(u_{1}+u_{3}-2 \phi\right)\right)\left(\theta_{u_{1}}+\theta_{u_{3}}\right) \wedge T\right| \\
& :=I_{1}+I_{2}
\end{aligned}$$
where in the last inequality we used the fact that $\chi$ is increasing and $\varphi \geq \epsilon\left(u_{1}+u_{2}-2 \phi\right)$ on $X \backslash U$. By Lemma 2.7, we have $E_{\tilde{\chi}, \theta, \phi}^{0}\left(\frac{u_{1}+u_{3}}{2}\right) \lesssim B$. Therefore, it follows from Lemma 2.8 that
$$I_{2} \leq 2 \int_{X}-\chi\left(2 \epsilon\left(\frac{u_{1}+u_{3}}{2}-\phi\right)\right) \theta_{\left(u_{1}+u_{3}\right) / 2} \wedge T \lesssim B \varrho(1-\tilde{\chi}(-1)) Q_{0}(2 \epsilon) .$$
In order to estimate $I_{1}$, we divide it into two terms
$$\begin{aligned}
I_{1} & \leq\left|\int_{X}-\chi((1+\epsilon) \tilde{\varphi}) d d^{c}\left(u_{1}-u_{3}\right) \wedge T\right|+\left|\int_{X \backslash U}-\chi((1+\epsilon) \tilde{\varphi}) d d^{c}\left(u_{1}-u_{3}\right) \wedge T\right| \\
& :=I_{3}+I_{4}
\end{aligned}$$

Note that $\tilde{u}_{1}-\tilde{u}_{2}=\epsilon\left(u_{1}+u_{3}-2 \phi\right) /(1+\epsilon)$ on $X \backslash U$. Hence
$$I_{4} \leq \int_{X \backslash U}-\chi((1+\epsilon) \tilde{\varphi})\left(\theta_{u_{1}}+\theta_{u_{3}}\right) \wedge T \leq \int_{X \backslash U}-\chi\left(\epsilon\left(u_{1}+u_{2}-2 \phi\right)\right)\left(\theta_{u_{1}}+\theta_{u_{3}}\right) \wedge T .$$
Using Lemma 2.8 again, we get
$$I_{4} \lesssim B \varrho(1-\tilde{\chi}(-1)) Q_{0}(2 \epsilon) .$$
Using integration by parts, we have
$$I_{3}=(1+\epsilon)\left|\int_{X} \chi^{\prime}((1+\epsilon) \tilde{\varphi}) d \tilde{\varphi} \wedge d^{c}\left(u_{1}-u_{3}\right) \wedge T\right| .$$
Moreover, by Cauchy-Schwarz inequality and by the choice of $\epsilon$ (see (3.8)), we get
$$\int_{\Gamma} \chi^{\prime}((1+\epsilon) \tilde{\varphi}) d \tilde{\varphi} \wedge d^{c}\left(u_{1}-u_{3}\right) \wedge T=0$$
Hence
$$I_{3}=(1+\epsilon)\left|\int_{U \cup V} \chi^{\prime}((1+\epsilon) \tilde{\varphi}) d \tilde{\varphi} \wedge d^{c}\left(u_{1}-u_{3}\right) \wedge T\right| \leq(1+\epsilon)\left(I_{5} I_{6}\right)^{1 / 2}$$
where
$$I_{5}=\int_{U \cup V} \chi^{\prime}((1+\epsilon) \tilde{\varphi}) d\left(u_{1}-u_{3}\right) \wedge d^{c}\left(u_{1}-u_{3}\right) \wedge T,$$
and
$$I_{6}=\int_{U \cup V} \chi^{\prime}((1+\epsilon) \tilde{\varphi}) d \tilde{\varphi} \wedge d^{c} \tilde{\varphi} \wedge T .$$

Since $(1+\epsilon) \tilde{\varphi} \leq \epsilon\left(u_{1}+u_{3}-2 \phi\right)$, if $\chi \in \widetilde{\mathcal{W}}^{-}$(hence $\chi^{\prime}$ is nonnegative and increasing on $\mathbb{R}_{\leq 0}$ ) then
$$\begin{aligned}
I_{5} & \leq \int_{X} \chi^{\prime}\left(\epsilon\left(u_{1}+u_{3}-2 \phi\right)\right) d\left(u_{1}-u_{3}\right) \wedge d^{c}\left(u_{1}-u_{3}\right) \wedge T \\
& \lesssim \int_{X} \chi^{\prime}\left(\epsilon\left(u_{1}+u_{3}-2 \phi\right)\right) d\left(u_{1}-\phi\right) \wedge d^{c}\left(u_{1}-\phi\right) \wedge T \\
& +\int_{X} \chi^{\prime}\left(\epsilon\left(u_{1}+u_{3}-2 \phi\right)\right) d\left(u_{3}-\phi\right) \wedge d^{c}\left(u_{3}-\phi\right) \wedge T \\
& \leq \int_{X} \chi^{\prime}\left(\epsilon\left(u_{1}-\phi\right)\right) d\left(u_{1}-\phi\right) \wedge d^{c}\left(u_{1}-\phi\right) \wedge T+\int_{X} \chi^{\prime}\left(\epsilon\left(u_{3}-\phi\right)\right) d\left(u_{3}-\phi\right) \wedge d^{c}\left(u_{3}-\phi\right) \wedge T \\
& =\epsilon^{-1} \int_{X} \chi\left(\epsilon\left(u_{1}-\phi\right)\right) d d^{c}\left(u_{1}-\phi\right) \wedge T+\epsilon^{-1} \int_{X} \chi\left(\epsilon\left(u_{3}-\phi\right)\right) d d^{c}\left(u_{3}-\phi\right) \wedge T \\
& \lesssim B \varrho(1-\tilde{\chi}(-1)) \epsilon^{-1} Q_{0}(\epsilon),
\end{aligned}$$
where the last estimate holds due to Lemma 2.8.
Denote $v_{1}:=\left(u_{1}+2 u_{3}\right) / 3$ and $v_{2}:=\left(2 u_{1}+u_{3}\right) / 3$. Since
$$(1+\epsilon)\left(\tilde{u}_{1}-\tilde{u}_{2}\right) \geq u_{1}+u_{3}-2 \phi, \quad u_{1}-u_{3}=-\left(v_{1}-v_{2}\right) / 3,$$
one sees that if $\chi \in \mathcal{W}_{M}^{+}$(hence $\chi^{\prime}$ is nonnegative and decreasing in $\mathbb{R}_{\leq 0}$ ) then
$$\begin{aligned}
I_{5} & \leq \int_{X} \chi^{\prime}\left(\left(u_{1}+u_{3}-2 \phi\right)\right) d\left(u_{1}-u_{3}\right) \wedge d^{c}\left(u_{1}-u_{3}\right) \wedge T \\
& \lesssim \int_{X} \chi^{\prime}\left(\left(u_{1}+u_{3}-2 \phi\right)\right)\left(d\left(v_{1}-\phi\right) \wedge d^{c}\left(v_{1}-\phi\right)+d\left(v_{2}-\phi\right) \wedge d^{c}\left(v_{2}-\phi\right)\right) \wedge T \\
& \leq \int_{X} \chi^{\prime}\left(3\left(v_{1}-\phi\right)\right) d\left(v_{1}-\phi\right) \wedge d^{c}\left(v_{1}-\phi\right) \wedge T+\int_{X} \chi^{\prime}\left(3\left(v_{2}-\phi\right)\right) d\left(v_{2}-\phi\right) \wedge d^{c}\left(v_{2}-\phi\right) \wedge T \\
& =\frac{1}{3} \int_{X}-\chi\left(3\left(v_{1}-\phi\right)\right) d d^{c}\left(v_{1}-\phi\right) \wedge T+\frac{1}{3} \int_{X}-\chi\left(3\left(v_{2}-\phi\right)\right) d d^{c}\left(v_{2}-\phi\right) \wedge T \\
& \leq \int_{X}-\chi\left(3\left(v_{1}-\phi\right)\right)\left(\theta_{v_{1}}+\theta_{\phi}\right) \wedge T+\int_{X}-\chi\left(3\left(v_{2}-\phi\right)\right)\left(\theta_{v_{1}}+\theta_{\phi}\right) \wedge T \\
& \leq 3^{M} \int_{X}-\chi\left(v_{1}-\phi\right)\left(\theta_{v_{1}}+\theta_{\phi}\right) \wedge T+3^{M} \int_{X}-\chi\left(v_{2}-\phi\right)\left(\theta_{v_{1}}+\theta_{\phi}\right) \wedge T \\
& \lesssim B \varrho
\end{aligned}$$
where the two last estimates hold due to Lemma 2.7 and the fact
$$\log (-\chi(3 t))-\log (-\chi(t))=\int_{t}^{3 t} \frac{\chi^{\prime}(s)}{\chi(s)} d s \leq \int_{t}^{3 t} \frac{M}{s} d s=M \log 3$$
for every $\chi \in \mathcal{W}_{M}^{+}$and $t \leq 0$. Combining the estimates in both cases, we obtain
$$I_{5} \lesssim B \varrho(1-\tilde{\chi}(-1)) \frac{Q(\epsilon)^{2}}{\epsilon},$$
where we used the inequality $Q(\epsilon) \geq \epsilon^{1 / 2}$ if $\chi \in \widetilde{W}^{-}$. Now, we estimate $I_{6}$. Since $U, V$ are open in the plurifine topology and
$$(1+\epsilon) \tilde{\varphi}=\left\{\begin{array}{l}
\varphi \quad \text { on } \quad U \\
\epsilon\left(u_{1}+u_{3}-2 \varphi\right) \quad \text { on } \quad V
\end{array},\right.$$
we have
$$\begin{aligned}
I_{6} & =\int_{U} \chi^{\prime}((1+\epsilon) \tilde{\varphi}) d \tilde{\varphi} \wedge d^{c} \tilde{\varphi} \wedge T+\int_{V} \chi^{\prime}((1+\epsilon) \tilde{\varphi}) d \tilde{\varphi} \wedge d^{c} \tilde{\varphi} \wedge T \\
& =(1+\epsilon)^{-2} \int_{U} \chi^{\prime}(\varphi) d \varphi \wedge d^{c} \varphi \wedge T \\
& +\frac{\epsilon^{2}}{(1+\epsilon)^{2}} \int_{V} \chi^{\prime}\left(\epsilon\left(u_{1}+u_{3}-2 \varphi\right)\right) d\left(u_{1}+u_{3}-2 \varphi\right) \wedge d^{c}\left(u_{1}+u_{3}-2 \varphi\right) \wedge T \\
& \leq J+\epsilon^{2} \int_{X} \chi^{\prime}\left(\epsilon\left(u_{1}+u_{3}-2 \varphi\right)\right) d\left(u_{1}+u_{3}-2 \varphi\right) \wedge d^{c}\left(u_{1}+u_{3}-2 \varphi\right) \wedge T \\
& =J+\epsilon \int_{X}-\chi\left(\epsilon\left(u_{1}+u_{3}-2 \varphi\right)\right) d d^{c}\left(u_{1}+u_{3}-2 \varphi\right) \wedge T
\end{aligned}$$
Therefore, it follows from Lemma 2.8 that
$$I_{6} \lesssim J+B \varrho(1-\tilde{\chi}(-1)) \epsilon Q_{0}(2 \epsilon) .$$
Combining (3.9), (3.11), (3.10), (3.12) and (3.13), we get
$$\begin{aligned}
I \leq I_{1}+I_{2} & \leq I_{3}+I_{4}+I_{2} \\
& \lesssim\left(I_{5} I_{6}\right)^{1 / 2}+I_{4}+I_{2} \\
& \lesssim\left(B \varrho(1-\tilde{\chi}(-1)) \epsilon^{-1} J\right)^{1 / 2} Q(\epsilon)+B \varrho(1-\tilde{\chi}(-1)) \epsilon Q(2 \epsilon)^{2} .
\end{aligned}$$
Letting $\epsilon \searrow J /(2 \varrho)$ (and $\epsilon$ satisfies (3.8)), we obtain
$$I \lesssim B \varrho(1-\tilde{\chi}(-1)) Q(J / \varrho) .$$
The proof is completed. \(\square\)

Proposition 3.5. Let $\chi, \tilde{\chi} \in \widetilde{\mathcal{W}}^{-} \cup \mathcal{W}_{M}^{+}$such that $\tilde{\chi} \leq \chi$ and $\chi \in \mathscr{C}^{1}(\mathbb{R})$. Let $u_{1}, u_{2}, u_{3} \in$ $\mathcal{E}(X, \theta, \phi)$ such that $u_{1} \leq u_{2}$ and $u_{j}-\phi$ is bounded $(j=1,2,3)$, where $\phi$ is a negative $\theta$-psh function satisfying $\varrho:=\operatorname{vol}\left(\theta_{\phi}\right)>0$. Then there exists a constant $C_{n}>0$ depending only on $n$ and $M$ such that
$$\int_{X} \chi^{\prime}\left(u_{1}-u_{2}\right) d\left(u_{1}-u_{2}\right) \wedge d^{c}\left(u_{1}-u_{2}\right) \wedge \theta_{u_{3}}^{n-1} \leq C_{n} \varrho B^{2}(1-\tilde{\chi}(-1))^{2} Q^{\circ(n-1)}\left(I_{\chi}^{0}\left(u_{1}, u_{2}\right)\right),$$
where $B:=\sum_{j=1}^{3} \max \left\{E_{\tilde{\chi}, \theta, \phi}^{0}\left(u_{j}\right), 1\right\}$ and $Q$ is defined by (3.1).

Proof. Let
$$\varphi:=u_{1}-u_{2}, \quad T:=\sum_{j=1}^{n-1} \theta_{u_{1}}^{j} \wedge \theta_{u_{2}}^{n-1-j},$$
and
$$T_{k, l}:=\theta_{u_{1}}^{k} \wedge \theta_{u_{2}}^{l} \wedge \theta_{u_{3}}^{n-k-l-1}, \quad L_{k, l}:=\int_{X} \chi^{\prime}(\varphi) d \varphi \wedge d^{c} \varphi \wedge T_{k, l} .$$
Observe
$$\theta_{u_{2}}^{n}-\theta_{u_{1}}^{n}=-d d^{c} \varphi \wedge T$$
and
$$L_{k, n-1-k} \leq \int_{X} \chi^{\prime}(\varphi) d \varphi \wedge d^{c} \varphi \wedge T=\varrho I_{\chi}^{0}\left(u_{1}, u_{2}\right)$$
by integration by parts. We now prove by inverse induction on $m:=k+l$ that
$$L_{k, l} \leq C_{m, n} \varrho B^{2}(1-\tilde{\chi}(-1))^{2} Q^{\circ(n-1-k-l)}\left(I_{\chi}^{0}\left(u_{1}, u_{2}\right)\right),$$
for some constant $C_{m, n}>1$ depending only on $m, n$ and $M$. The desired assertion (3.14) is the case where $k=l=0$. In what follows we use the symbols $\lesssim$ and $\gtrsim$ for inequalities modulo a constant depending only on $n$ and $M$. We have checked (3.16) for $k+l=n-1$. Suppose that (3.16) holds for $k+l=m$ with $0<m \leq n-1$. We will verify it for $L_{k-1, l}$, where $k+l=m$ and $k>1$. The case $L_{k, l-1}$ is done similarly.

Denote $S_{k-1, l}=\theta_{u_{1}}^{k-1} \wedge \theta_{u_{2}}^{l} \wedge \theta_{u_{3}}^{n-k-l-1}$. Then
$$L_{k-1, l}-L_{k, l}=\int_{X} \chi^{\prime}(\varphi) d \varphi \wedge d^{c} \varphi \wedge d d^{c}\left(u_{3}-u_{1}\right) \wedge S_{k-1, l} .$$
Using integration by parts, we have
$$\begin{aligned}
L_{k-1, l}-L_{k, l} & =\int_{X}-\chi(\varphi) d d^{c}(\varphi) \wedge d d^{c}\left(u_{3}-u_{1}\right) \wedge S_{k-1, l} \\
& =\int_{X}-\chi(\varphi) d d^{c}\left(u_{3}-u_{1}\right) \wedge T_{k, l}-\int_{X}-\chi(\varphi) d d^{c}\left(u_{3}-u_{1}\right) \wedge T_{k-1, l+1} \\
& =\int_{X} \chi^{\prime}(\varphi) d \varphi \wedge d^{c}\left(u_{3}-u_{1}\right) \wedge T_{k, l}-\int_{X} \chi^{\prime}(\varphi) d \varphi \wedge d^{c}\left(u_{3}-u_{1}\right) \wedge T_{k-1, l+1}
\end{aligned}$$
Therefore, it follows from Lemma 3.4 that
$$L_{k-1, l}-L_{k, l} \lesssim \varrho B(1-\tilde{\chi}(-1))\left(Q\left(L_{k, l} / \varrho\right)+Q\left(L_{k-1, l+1} / \varrho\right)\right) .$$
Hence, by using the inductive hypothesis, we get
$$\begin{aligned}
L_{k-1, l} & \lesssim \varrho B^{2}(1-\tilde{\chi}(-1))^{2} Q^{\circ(n-1-m)}\left(I_{\chi}^{0}\left(u_{1}, u_{2}\right)\right) \\
& +\varrho B(1-\tilde{\chi}(-1)) Q\left(C_{m, n} B^{2}(1-\tilde{\chi}(-1))^{2} Q^{\circ(n-1-m)}\left(I_{\chi}^{0}\left(u_{1}, u_{2}\right)\right)\right) \\
& \lesssim \varrho B^{2}(1-\tilde{\chi}(-1))^{2} Q^{\circ(n-m)}\left(I_{\chi}^{0}\left(u_{1}, u_{2}\right)\right) .
\end{aligned}$$
Here we use the fact $Q\left(t_{1}\right) \leq\left(t_{1} / t_{2}\right)^{1 / 2} Q\left(t_{2}\right)$ for every $t_{1}>t_{2}>0$ (see Lemma 3.6).
Thus, (3.16) holds for $L_{k-1, l}$. This finishes the proof. \(\square\)

Lemma 3.6. The function $h(t)=\frac{(Q(t))^{2}}{t}$ is non-increasing in $\mathbb{R}_{>0}$.
Proof. If $\chi \in \mathcal{W}_{M}^{+}$then we have
$$h(t)=\left\{\begin{array}{lll}
\frac{1}{t} & \text { if } & t \geq 1, \\
1 & \text { if } & 0<t<1,
\end{array}\right.$$
is a non-increasing function.
We consider the case $\chi \in \widetilde{\mathcal{W}}^{-}$. We have
$$h(t)=\left\{\begin{array}{l}
\frac{1}{t} \quad \text { if } \quad t \geq 1, \\
\frac{Q_{0}(t)}{t Q_{0}(1)} \quad \text { if } \quad 0<t<1 .
\end{array}\right.$$
It is clear that $h$ is decreasing in $[1, \infty)$. We need to show that $h$ is non-increasing in (0, 1). Since $\chi$ is convex, we have
$$\frac{\chi\left(t_{1} s\right)}{t_{1} s} \leq \frac{\chi\left(t_{2} s\right)}{t_{2} s},$$
for every $0<t_{2}<t_{1}<1$ and $s<0$. Dividing both sides of the last estimate by $\tilde{\chi}(s) / s$, we get
$$\frac{\chi\left(t_{1} s\right)}{t_{1} \tilde{\chi}(s)} \leq \frac{\chi\left(t_{2} s\right)}{t_{2} \tilde{\chi}(s)} .$$
Taking the supremum of both sides, we obtain
$$\frac{Q_{0}\left(t_{1}\right)}{t_{1}}=\sup _{s \leq-1} \frac{\chi\left(t_{1} s\right)}{t_{1} \tilde{\chi}(s)} \leq \sup _{s \leq-1} \frac{\chi\left(t_{2} s\right)}{t_{2} \tilde{\chi}(s)}=\frac{Q_{0}\left(t_{2}\right)}{t_{2}} .$$
Then $h\left(t_{1}\right) \leq h\left(t_{2}\right)$. Hence, $h$ is non-increasing in ( 0,1 ). The proof is completed. \(\square\)

End of the proof of Theorem 3.1 By Lemma 3.3 and Lemma 2.6, the problem is reduced to the case where $\chi \in \mathscr{C}^{1}(\mathbb{R})$ and $u_{j}, \psi_{j}$ are of the same singularity type as $\phi$.

Let $L$ be the left-hand side of the desired inequality. We have
$$\begin{aligned}
L & =\int_{X}-\chi\left(u_{1}-u_{2}\right)\left(\theta_{\psi_{1}}^{n}-\theta_{u_{1}}^{n}\right)-\int_{X}-\chi\left(u_{1}-u_{2}\right)\left(\theta_{\psi_{2}}^{n}-\theta_{u_{1}}^{n}\right) \\
& =\int_{X}-\chi\left(u_{1}-u_{2}\right) d d^{c}\left(\psi_{1}-u_{1}\right) \wedge T_{1}-\int_{X}-\chi\left(u_{1}-u_{2}\right) d d^{c}\left(\psi_{2}-u_{1}\right) \wedge T_{2} \\
& =L_{1}-L_{2},
\end{aligned}$$
where $T_{j}=\sum_{l=0}^{n-1} \theta_{\psi_{j}}^{l} \wedge \theta_{u_{1}}^{n-l-1}$. Using integration by parts and Lemma 3.4, we get
$$\begin{aligned}
L_{1} & =\int_{X} \chi^{\prime}\left(u_{1}-u_{2}\right) d\left(u_{1}-u_{2}\right) \wedge d^{c}\left(\psi_{1}-u_{1}\right) \wedge T_{1} \\
& \leq C_{1} \varrho B(1-\tilde{\chi}(-1)) Q\left(\varrho^{-1} \int_{X} \chi^{\prime}\left(u_{1}-u_{2}\right) d\left(u_{1}-u_{2}\right) \wedge d^{c}\left(u_{1}-u_{2}\right) \wedge T_{1}\right),
\end{aligned}$$
where $C_{1}>0$ depends only on $n$ and $M$. Moreover, it follows from Proposition 3.5 that $\varrho^{-1} \int_{X} \chi^{\prime}\left(u_{1}-u_{2}\right) d\left(u_{1}-u_{2}\right) \wedge d^{c}\left(u_{1}-u_{2}\right) \wedge T_{1} \leq C_{2} B^{2}(1-\tilde{\chi}(-1))^{2} Q^{\circ(n-1)}\left(I_{\chi}^{0}\left(u_{1}, u_{2}\right)\right)$, where $C_{2}>1$ depends only on $n$ and $M$. Then
$$L_{1} \leq C_{3} \varrho B^{2}(1-\tilde{\chi}(-1))^{2} Q^{\circ n}\left(I_{\chi}^{0}\left(u_{1}, u_{2}\right)\right),$$
where $C_{3}>0$ depends only on $n$ and $M$. Here we use the fact $Q\left(t_{1}\right) \leq\left(t_{1} / t_{2}\right)^{1 / 2} Q\left(t_{2}\right)$ for every $t_{1}>t_{2}>0$.

By the same arguments, we also have
$$-L_{2} \leq C_{4} \varrho B^{2}(1-\tilde{\chi}(-1))^{2} Q^{\circ n}\left(I_{\chi}^{0}\left(u_{1}, u_{2}\right)\right),$$
where $C_{4}>0$ depends only on $n$ and $M$.
Hence
$$L=L_{1}-L_{2} \leq\left(C_{3}+C_{4}\right) \varrho B^{2}(1-\tilde{\chi}(-1))^{2} Q^{\circ n}\left(I_{\chi}^{0}\left(u_{1}, u_{2}\right)\right) .$$
The proof is completed. \(\square\)

\subsection*{3.3 Proof of Theorem 3.2}

Recall that for every Borel set $E$ in $X$, we define
$$\operatorname{cap}_{\theta, \phi}(E):=\sup \left\{\int_{E} \theta_{h}^{n}: \quad h \in \operatorname{PSH}(X, \theta), \quad \phi-1 \leq h \leq \phi\right\} .$$
The following is an improvement of results from [17, 16] (see also [8, 42]).
Theorem 3.7. Let $A \geq 1$ be a constant and let $\theta$ be a closed smooth real (1,1)-form such that $\theta \leq A \omega$. Let $\phi \in \operatorname{PSH}(X, \theta)$ and $0 \leq f \in L^{p}(X)$ for some constant $p>1$ such that $\phi=P[\phi]$ and $0<\int_{X} f \omega^{n}=\int_{X} \theta_{\phi}^{n}:=\varrho$. Assume $u \in \mathcal{E}(X, \theta, \phi)$ satisfies $\sup _{X}(u-\phi)=0$ and $\theta_{u}^{n}=f d V$. Then, there exists a constant $C \geq 1$ depending only on $X, \omega, n$ and $p$ such that
$$u \geq \phi-C A\left(\log \left\|f \operatorname{vol}_{\omega}(X)^{q} / \varrho\right\|_{L^{p}}+\log A+1\right),$$
where $\operatorname{vol}_{\omega}(X):=\int_{X} \omega^{n}$ and $q=\frac{p}{p-1}$.
By Hölder inequalities, one sees that
$$1=\int_{X} \frac{f}{\varrho} \omega^{n} \leq\|f / \varrho\|_{L^{p}}\left(\operatorname{vol}_{\omega}(X)\right)^{q},$$
and then $\log \left\|f \operatorname{vol}_{\omega}(X)^{q} / \varrho\right\|_{L^{p}} \geq 0$.
Proof. Without loss of generality, we can assume that $\operatorname{vol}_{\omega}(X)=1$. Recall that there exists a constant $\nu>0$ depending only on $X, \omega$ such that
$$\int_{X} \exp (-\psi / \nu) \omega^{n} \leq C_{0}^{2},$$
for every $\psi \in \operatorname{PSH}(X, \omega)$ with $\sup _{X} \psi=0$, where $C_{0}>0$ is a constant depending only on $X$ and $\omega$. Consequently, one gets
$$\int_{X} \exp (-\psi /(A \nu)) \omega^{n} \leq C_{0}^{2}$$
for every $\psi \in \operatorname{PSH}(X, \theta) \subset \operatorname{PSH}(X, A \omega)$ with $\sup _{X} \psi=0$. By the same arguments as in the proof of [16, Proposition 4.30] (use [17, Lemma 3.9] instead of [16, Lemma 4.9]), we have
$$\int_{E} \omega^{n} \leq C_{0} \exp \left(-\frac{1}{2 A \nu}\left(\frac{\operatorname{cap}_{\theta, \phi}(E)}{\varrho}\right)^{-1 / n}\right),$$
for every Borel set $E \subset X$. Therefore, by the Hölder inequality and the fact $e^{-1 / t} \leq m!t^{m}$ for every $m \in \mathbb{N}$ and every $t>0$, there exists $A_{0}>0$ depending only on $X, \omega, n$ and $p$ such that
$$\varrho^{-1} \int_{E} \theta_{u}^{n}=\int_{E}(f / \varrho) \omega^{n} \leq\|f / \varrho\|_{L^{p}}\left(\int_{E} \omega^{n}\right)^{1 / q} \leq A_{0} A^{2 n}\|f / \varrho\|_{L^{p}} \frac{\operatorname{cap}_{\theta, \phi}(E)^{2}}{\varrho^{2}},$$
for every Borel set $E \subset X$, where $1 / p+1 / q=1$. On the other hand, denoting $b=(A \nu q)^{-1}$ and $B_{0}=\left(C_{0}\right)^{1 / q}$, we have
$$\varrho^{-1} \int_{X} e^{-b w} \theta_{u}^{n} \leq\|f / \varrho\|_{L^{p}}\left(\int_{X} e^{-b q w} d V\right)^{1 / q} \leq B_{0}\|f / \varrho\|_{L^{p}},$$
for every $w \in \operatorname{PSH}(X, \theta)$ with $\sup _{X} w=0$.
For every $h \in \operatorname{PSH}(X, \theta)$ with $\phi-1 \leq h \leq \phi$, for each $0 \leq t \leq 1$ and $s>0$, we have
$$\begin{aligned}
t^{n} \int_{\{u<\phi-t-s\}} \theta_{h}^{n} \leq \int_{\{u<(1-t) \phi+t h-s\}} \theta_{(1-t) \phi+t h}^{n} & \leq \int_{\{u<(1-t) \phi+t h-s\}} \theta_{u}^{n} \\
& \leq \int_{\{u<\phi-s\}} \theta_{u}^{n}
\end{aligned}$$
where the third estimate holds due to the comparison principle [17, Lemma 2.3]. Then
$$t^{n} \operatorname{cap}_{\phi}(u<\phi-t-s) \leq \int_{\{u<\phi-s\}} \theta_{u}^{n},$$
for every $0 \leq t \leq 1, s>0$. Therefore, it follows from (3.18) that
$$t^{n} \varrho^{-1} \operatorname{cap}_{\phi}(u<\phi-t-s) \leq A_{1} \varrho^{-2} \operatorname{cap}_{\phi}(u<\phi-s)^{2},$$
where $A_{1}=A_{0} A^{2 n}\|f / \varrho\|_{L^{p}}$. Putting $g(s)=\varrho^{-1 / n} \operatorname{cap}_{\phi}(u<\phi-s)^{1 / n}$, the above inequality becomes
$$t g(t+s) \leq A_{1}^{1 / n} g(s)^{2} .$$

Hence, it follows from [33, Lemma 2.4 and Remark 2.5] that if $g\left(s_{0}\right)<1 /\left(2 A_{1}^{1 / n}\right)$ then $g(s)=0$ for all $s \geq s_{0}+2$. Moreover, by (3.20) and the condition (3.19), we have
$$g(s+1)^{n} \leq \varrho^{-1} \int_{\{u<\phi-s\}} \theta_{u}^{n} \leq \varrho^{-1} \int_{X} e^{b(\phi-u-s)} \theta_{u}^{n} \leq B_{1} e^{-b s},$$
for every $s>0$, where $B_{1}=B_{0}\|f / \varrho\|_{L^{p}}$. Then $g(s+1)<1 /\left(2 A_{1}^{1 / n}\right)$ provided that
$$s>\frac{n \log 2+\log A_{1}}{b}+\frac{\log B_{1}}{b} .$$
Hence $g(s)=0$ for every
$$s \geq \frac{n \log 2+\log A_{1}}{b}+\frac{\log B_{1}}{b}+4 .$$
Thus
$$u \geq \phi-\left(\frac{n \log 2+\log A_{1}}{b}+\frac{\log B_{1}}{b}+4\right)=\phi-C_{1} \log \|f / \varrho\|_{L^{p}}-C_{2},$$
where $C_{1}=\frac{2}{b}=2 \nu q A$ and
$$\begin{aligned}
C_{2} & =4+\frac{n \log 2+\log A_{0}+\log B_{0}+2 n \log A}{b} \\
& =4+2 \nu q\left(n \log 2+\log A_{0}+\log B_{0}+2 n \log A\right) A .
\end{aligned}$$
The proof is finished. \(\square\)

Lemma 3.8. There exists a constant $C>0$ depending only on $n, X$ and $\omega$ such that for every $u \in \operatorname{PSH}(X, \omega)$ satisfying $\sup _{X} u=0$ and for every constant $0<t \leq 1$, one has
$$\int_{\{u>-t\}} \omega^{n} \geq C t^{2 n} .$$
Proof. Let $\left(U_{j}, \varphi_{j}\right)_{j=1}^{m}$ such that $U_{j} \subset X$ are open, $\varphi_{j}: 4 \mathbb{B} \longrightarrow U_{j}$ are biholomorphic and $\cup_{j=1}^{m} \varphi_{j}(\mathbb{B})=X$ (where $\mathbb{B}$ is the open unit ball in $\mathbb{C}^{n}$ ), and there is a smooth psh function $\rho_{j}$ in $U_{j}$ such that $d d^{c} \rho_{j}=\omega$ for $1 \leq j \leq m$. Denote
$$C_{\rho}=\sup _{1 \leq j \leq m} \sup _{2 \mathbb{B}}\left\|\nabla\left(\rho_{j} \circ \varphi_{j}\right)\right\| .$$
Assume $u\left(z_{0}\right)=0$. Then there exists $1 \leq j_{0} \leq m$ such that $z_{0} \in \varphi_{j_{0}}(\mathbb{B})$. Denote $w_{0}=\varphi_{j_{0}}^{-1}\left(z_{0}\right), \widehat{u}(w)=u \circ \varphi_{j_{0}}(w)$ and $\widehat{\rho}(w)=\rho_{j_{0}} \circ \varphi_{j_{0}}(w)-\rho_{j_{0}} \circ \varphi_{j_{0}}\left(w_{0}\right)$. By the plurisub-
harmonicity of $\widehat{u}+\widehat{\rho}$, for every $t>0$ and $0<r<1$, we have
$$\begin{aligned}
0=(\widehat{u}+\widehat{\rho})\left(w_{0}\right) & \leq \frac{1}{\operatorname{vol}_{\mathbb{C}^{n}}(r \mathbb{B})} \int_{r \mathbb{B}}(\widehat{u}+\widehat{\rho}) d V_{2 n} \\
& \leq C_{\rho} r+\frac{1}{c_{2 n} r^{2 n}} \int_{r \mathbb{B}} \widehat{u} d V_{2 n} \\
& \leq C_{\rho} r-\frac{t}{c_{2 n} r^{2 n}} \int_{r \mathbb{B} \cap\{\widehat{u} \leq-t\}} d V_{2 n} \\
& \leq C_{\rho} r-t+\frac{t}{c_{2 n} r^{2 n}} \int_{r \mathbb{B} \cap\{\widehat{u}>-t\}} d V_{2 n} \\
& \leq C_{\rho} r-t+\frac{C_{\omega} t}{r^{2 n}} \operatorname{vol}_{\omega}(\{u>-t\}),
\end{aligned}$$
where $c_{2 n}=\operatorname{vol}_{\mathbb{C}^{n}}(\mathbb{B})$ and $C_{\omega}>0$ is a constant depending only on $n, X, \omega$. It follows that
$$\operatorname{vol}_{\omega}(\{u>-t\}) \geq \frac{r^{2 n}}{C_{\omega}}\left(1-\frac{C_{\rho} r}{t}\right) .$$
Hence, for every $0<t<1$, by choosing $r=\frac{t}{1+C_{\rho}}$, we have
$$\operatorname{vol}_{\omega}(\{u>-t\}) \geq C t^{2 n},$$
where $C=\frac{1}{C_{\omega}\left(1+C_{\rho}\right)^{2 n+1}}$ depends only on $n, X$ and $\omega$. \(\square\)

End of the proof of Theorem 3.2 Without loss of generality, we can assume that $u_{1} \leq u_{2}$. Denote $W_{t}=\left\{u_{1}>a_{1}-t\right\}$ for $0<t \leq 1$. We have
$$\int_{W_{t}}-\chi\left(u_{1}-u_{2}\right) \omega^{n} \leq \int_{W_{t}}-\chi\left(u_{1}-a_{2}\right) \omega^{n} \leq-b_{t} \chi\left(a_{1}-a_{2}-t\right),$$
where $b_{t}:=\operatorname{vol}\left(W_{t}\right)$.
It follows from Lemma 3.8 that $W_{t} \neq \emptyset$. Moreover,
$$b_{t}:=\int_{W_{t}} \omega^{n} \geq C_{1}\left(\frac{t}{A}\right)^{2 n},$$
where $C_{1}>0$ is a constant depending only on $n, X$ and $\omega$. By [17, Theorem A] (see also [32, Theorem 3]), there exists a unique $\varphi \in \mathcal{E}(X, \theta, \phi)$ with $\sup _{X}(\varphi-\phi)=0$ such that
$$\theta_{\varphi}^{n}=\frac{\varrho}{b_{t}} \mathbf{1}_{W_{t}} \omega^{n} .$$
It follows from Theorem 3.7 that
$$\phi-C_{2} A(-\log t+\log A+1) \leq \varphi \leq \phi,$$
for some constant $C_{2} \geq 1$ depending only on $n, X$ and $\omega$. Thus, we have
$$E_{\tilde{\chi}, \theta, \phi}^{0}(\varphi) \leq-\tilde{\chi}\left(C_{2} A(-\log t+\log A+1)\right) \leq-C_{3}\left(\log \frac{A e}{t}\right)^{M} \tilde{\chi}(-A),$$
where $C_{3}>0$ depends only on $n, X, \omega$ and $M$.
Hence, it follows from Theorem 3.1 that
$$\int_{X}-\chi\left(u_{1}-u_{2}\right)\left(\theta_{\psi}^{n}-\theta_{\varphi}^{n}\right) \leq C_{4} \varrho\left(\log \frac{A e}{t}\right)^{2 M}(B-\tilde{\chi}(-A))^{2}(1-\tilde{\chi}(-1))^{2} \lambda,$$
where $\lambda=Q^{\circ(n)}\left(I_{\chi}^{0}\left(u_{1}, u_{2}\right)\right)$ and $C_{4}>0$ depends only on $n, X, \omega$ and $M$.
Combining (3.22) and (3.25), we get
$$\int_{X}-\chi\left(u_{1}-u_{2}\right) \theta_{\psi}^{n} \leq-\varrho \chi\left(a_{1}-a_{2}-t\right)+C_{4} \varrho\left(\log \frac{A e}{t}\right)^{2 M}(B-\tilde{\chi}(-A))^{2}(1-\tilde{\chi}(-1))^{2} \lambda .$$
Letting $t \rightarrow \lambda^{m}$, we get
$$\begin{aligned}
\int_{X}-\chi\left(u_{1}-u_{2}\right) \theta_{\psi}^{n} & \leq-\varrho \chi\left(a_{1}-a_{2}-\lambda^{m}\right)+C_{4} \varrho\left(\log \frac{A e}{\lambda^{m}}\right)^{2 M}(B-\tilde{\chi}(-A))^{2}(1-\tilde{\chi}(-1))^{2} \lambda \\
& \leq-\varrho \chi\left(a_{1}-a_{2}-\lambda^{m}\right)+C_{5} \varrho \frac{A^{(1-\gamma) / m}}{\lambda^{1-\gamma}}(B-\tilde{\chi}(-A))^{2}(1-\tilde{\chi}(-1))^{2} \lambda \\
& \leq-\varrho \chi\left(a_{1}-a_{2}-\lambda^{m}\right)+C_{5} \varrho A^{(1-\gamma) / m} \lambda^{1-\gamma}(B-\tilde{\chi}(-A))^{2}(1-\tilde{\chi}(-1))^{2} \lambda^{\gamma},
\end{aligned}$$
where $C_{5}>0$ depends only on $n, X, \omega, M, m$ and $\gamma$.
The proof is completed. \(\square\)

\subsection*{3.4 Applications}

\subsection*{3.4.1 Quantitative version for the domination principle}

Theorem 3.9. Let $A \geq 1$ be a constant and let $\theta \leq A \omega$ be a closed smooth real (1, 1)-form and $\phi$ be a model $\theta$-psh function, and $\varrho:=\operatorname{vol}\left(\theta_{\phi}\right)>0$. Let $B \geq 1$ be a constant, $\tilde{\chi} \in \widetilde{\mathcal{W}}^{-}$and $u_{1}, u_{2} \in \mathcal{E}(X, \theta, \phi)$ such that $\tilde{\chi}(-1)=-1$ and
$$E_{\tilde{\chi}, \theta, \phi}^{0}\left(u_{1}\right)+E_{\tilde{\chi}, \theta, \phi}^{0}\left(u_{2}\right) \leq B .$$
Assume that there exists a constant $0 \leq c<1$ and a Radon measure $\mu$ on $X$ satisfying $\theta_{u_{1}}^{n} \leq c \theta_{u_{2}}^{n}+\varrho \mu$ on $\left\{u_{1}<u_{2}\right\}$ and $c_{\mu}:=\int_{\left\{u_{1}<u_{2}\right\}} d \mu \leq 1$. Then there exists a constant $C>0$ depending only on $n, X$ and $\omega$ such that
$$\operatorname{cap}_{\omega}\left\{u_{1}<u_{2}-\epsilon\right\} \leq \frac{C \operatorname{vol}(X)(A+B)^{2}}{\epsilon(1-c) h^{\circ n}\left(1 / c_{\mu}\right)},$$
for every $0<\epsilon<1$, where $h(s)=(-\tilde{\chi}(-s))^{1 / 2}$ for every $0 \leq s \leq \infty$.
In particular, if $c_{\mu}=0$ then $\operatorname{cap}_{\omega}\left\{u_{1}<u_{2}-\epsilon\right\}=0$ for every $\epsilon>0$, and then $u_{1} \geq u_{2}$ on whole $X$.

The standard domination principle corresponds to the case where $c=0$ and $\mu:=0$. A non-quantitative version of this domination principle (i.e, for $\mu=0$ ) in the non-Kähler setting was obtained in [49]. In order to prove Theorem 3.9, we need the following result which is an immediate consequence of the Chern-Levine-Nirenberg inequality:

Proposition 3.10. Let $\theta \leq A \omega$ be a closed smooth real (1, 1)-form (where $A \geq 1$ is a constant) and $\phi$ be a model $\theta$-psh function with $\varrho:=\int_{X} \theta_{\phi}^{n}>0$. Let $0 \leq w \leq 1$ is an $\omega$-psh function and $\psi$ is the unique solution to the problem
$$\left\{\begin{array}{l}
u \in \mathcal{E}(X, \theta, \phi) \\
\theta_{u}^{n}=\frac{\varrho}{\operatorname{vol}(X)}\left(d d^{c} w+\omega\right)^{n} \\
\sup _{X} u=0
\end{array}\right.$$
Then there exists a constant $C>0$ depending only on $X$ and $\omega$ such that
$$\int_{X}|\psi| \theta_{\psi}^{n} \leq C A \varrho .$$
Proof of Theorem 3.9 Let $w$ be an arbitrary $\omega$-psh function satisfying $0 \leq w \leq 1$ and $\psi$ is the unique solution to (3.26). Denote $v=\max \left\{u_{1}, u_{2}\right\}$ and $\chi(t)=\max \{t,-1\} \geq \tilde{\chi}(t)$. By Theorem 3.1 and Proposition 3.10, there exists a constant $C_{1}>0$ depending only on $n, X$ an $\omega$ such that
$$I_{1}:=\int_{X}-\chi\left(u_{1}-v\right)\left(\theta_{\psi}^{n}-\theta_{u_{1}}^{n}\right) \leq C_{1} \varrho(A+B)^{2} Q^{\circ(n)}\left(I_{\chi}^{0}\left(u_{1}, v\right)\right),$$
and
$$I_{2}:=\int_{X}-\chi\left(u_{1}-v\right)\left(\theta_{u_{2}}^{n}-\theta_{u_{1}}^{n}\right) \leq C_{1} \varrho(A+B)^{2} Q^{\circ(n)}\left(I_{\chi}^{0}\left(u_{1}, v\right)\right) .$$
Moreover, by the fact $\theta_{v}^{n}=\theta_{u_{2}}^{n}$ on $\left\{u_{1}<u_{2}\right\}$ and by the assumption $\theta_{u_{1}}^{n} \leq c \theta_{u_{2}}^{n}+\varrho \mu$ on $\left\{u_{1}<u_{2}\right\}$, we have
$$I_{\chi}^{0}\left(u_{1}, v\right)=\varrho^{-1} \int_{\left\{u_{1}<u_{2}\right\}}-\chi\left(u_{1}-v\right)\left(\theta_{u_{1}}^{n}-\theta_{u_{2}}^{n}\right) \leq \varrho^{-1} \int_{\left\{u_{1}<u_{2}\right\}}-\chi\left(u_{1}-v\right)\left(\theta_{u_{1}}^{n}-c \theta_{u_{2}}^{n}\right) \leq c_{\mu} .$$
Combining (3.27), (3.28) and (3.29), we get
$$\begin{aligned}
(1-c) \int_{X}-\chi\left(u_{1}-v\right) \theta_{\psi}^{n} & =\int_{X}-\chi\left(u_{1}-v\right)\left(\theta_{u_{1}}^{n}-c \theta_{u_{2}}^{n}\right)+(1-c) I_{1}+c I_{2} \\
& \leq \int_{X}-\chi\left(u_{1}-v\right)\left(\theta_{u_{1}}^{n}-c \theta_{u_{2}}^{n}\right)+C_{1} \varrho(A+B)^{2}(1-\tilde{\chi}(-1))^{2} Q^{\circ n}\left(c_{\mu}\right) \\
& \leq \varrho c_{\mu}+C_{1} \varrho(A+B)^{2} Q^{\circ n}\left(c_{\mu}\right) \\
& \leq C \varrho(A+B)^{2} Q^{\circ n}\left(c_{\mu}\right),
\end{aligned}$$
where $C=C_{1}+1$. Hence
$$\int_{\left\{u_{1}<u_{2}-\epsilon\right\}} \theta_{w}^{n}=\frac{\operatorname{vol}(X)}{\varrho} \int_{\left\{u_{1}<u_{2}-\epsilon\right\}} \theta_{\psi}^{n} \leq \frac{C \operatorname{vol}(X)(A+B)^{2} Q^{\circ n}\left(c_{\mu}\right)}{(1-c) \epsilon},$$
for every $0<\epsilon<1$. Since $w$ is arbitrary, it follows that
$$\operatorname{cap}_{\omega}\left\{u_{1}<u_{2}-\epsilon\right\} \leq \frac{C \operatorname{vol}(X)(A+B)^{2} Q^{\circ n}\left(c_{\mu}\right)}{(1-c) \epsilon} .$$
Moreover, by the definition of $\chi$ and the formula of $Q$, we have
$$Q(s)=\frac{1}{(-\tilde{\chi}(-1 / s))^{1 / 2}}=\frac{1}{h(1 / s)},$$
for every $0<s \leq 1$, and $Q(0)=0$. Then
$$Q^{\circ n}(s)=\frac{1}{h^{\circ n}(1 / s)},$$
for every $0 \leq s \leq 1$. The proof is completed. \(\square\)

\subsection*{3.4.2 Quantitative version of Dinew's uniqueness theorem}

Theorem 3.11. Let $A \geq 1$ be a constant. Let $\theta \leq A \omega$ be a closed smooth real (1, 1)-form and let $\phi$ be a model $\theta$-psh function such that $\varrho:=\operatorname{vol}\left(\theta_{\phi}\right)>0$. Let $B \geq 1, \tilde{\chi} \in \mathcal{W}^{-}$and $u_{1}, u_{2} \in \mathcal{E}(X, \theta, \phi)$ such that $\tilde{\chi}(-1)=-1$ and
$$E_{\tilde{\chi}, \theta, \phi}^{0}\left(u_{1}\right)+E_{\tilde{\chi}, \theta, \phi}^{0}\left(u_{2}\right) \leq B .$$
Then, for every $0<\gamma<1$, there exists $C>0$ depending only on $n, X, \omega$ and $\gamma$ such that
$$d_{\text {cap }}\left(u_{1}, u_{2}\right)^{2} \leq C\left(A+\left|a_{1}-a_{2}\right|\right)\left(\left|a_{1}-a_{2}\right|+A(A+B)^{2} \tau^{\gamma}\right),$$
where $a_{j}:=\sup _{X} u_{j}, \tau=\frac{1}{h^{\circ n}\left(\varrho /\left\|\theta_{u_{1}}^{n}-\theta_{u_{2}}^{n}\right\|\right)}$ and $h(s)=(-\tilde{\chi}(-s))^{1 / 2}$.
Note that if $\chi(t)=\max \{t,-1\}$ then $I_{\chi}^{0}\left(u_{1}, u_{2}\right) \leq \varrho^{-1}\left\|\theta_{u_{1}}^{n}-\theta_{u_{2}}^{n}\right\|$. Therefore, Theorem 3.11 is a consequence of the following:

Theorem 3.12. Let $\theta \leq A \omega$ be a closed smooth real (1, 1)-form ( $A \geq 1$ ) and let $\phi$ be a model $\theta$-psh function such that $\operatorname{vol}\left(\theta_{\phi}\right)>0$. Let $B \geq 1, \tilde{\chi} \in \widetilde{\mathcal{W}}^{-}$and $u_{1}, u_{2} \in \mathcal{E}(X, \theta, \phi)$ such that $\tilde{\chi}(-1)=-1$ and
$$E_{\tilde{\chi}, \theta, \phi}^{0}\left(u_{1}\right)+E_{\tilde{\chi}, \theta, \phi}^{0}\left(u_{2}\right) \leq B .$$
Denote $\chi(t)=\max \{t,-1\}$. Then, for every $0<\gamma<1$, there exists $C>0$ depending only on $n, X, \omega$ and $\gamma$ such that
$$d_{\text {cap }}\left(u_{1}, u_{2}\right)^{2} \leq C\left(A+\left|a_{1}-a_{2}\right|\right)\left(\left|a_{1}-a_{2}\right|+A(A+B)^{2} \lambda^{\gamma}\right),$$
where $a_{j}:=\sup _{X} u_{j}, \lambda=\frac{1}{h^{\circ n}\left(1 / I_{\chi}^{0}\left(u_{1}, u_{2}\right)\right)}$ and $h(s)=(-\tilde{\chi}(-s))^{1 / 2}$.

Proof. Suppose that $w$ is an arbitrary $\omega$-psh function satisfying $0 \leq w \leq 1$ and $\psi$ is the unique solution to the problem
$$\left\{\begin{array}{l}
u \in \mathcal{E}(X, \theta, \phi) \\
\theta_{u}^{n}=\frac{\varrho}{\operatorname{vol}(X)}\left(d d^{c} w+\omega\right)^{n} \\
\sup _{X} u=0
\end{array}\right.$$
Recall that $\lambda=Q_{\chi, \tilde{\chi}}^{\circ n}\left(I_{\chi}^{0}\left(u_{1}, u_{2}\right)\right)$, and one has $-\tilde{\chi}(-A) \leq A$ because $\tilde{\chi}(-1)=-1$. It follows from Theorem 3.2 and Proposition 3.10 that, for every $0<\gamma<1$, there exists $C_{1}>0$ depending only on $n, X, \omega$ and $\gamma$ such that
$$I:=\int_{X}-\chi\left(-\left|u_{1}-u_{2}\right|\right) \theta_{\psi}^{n} \leq-\varrho \chi\left(-\left|a_{1}-a_{2}\right|-\lambda\right)+C_{1} \varrho A(A+B)^{2} \lambda^{\gamma} .$$
Moreover
$$\begin{aligned}
\frac{\varrho}{\operatorname{vol}(X)} \int_{X}\left|u_{1}-u_{2}\right|^{1 / 2}\left(\omega+d d^{c} w\right)^{n} & =\int_{X}\left|u_{1}-u_{2}\right|^{1 / 2} \theta_{\psi}^{n} \\
& =\int_{\left\{\left|u_{1}-u_{2}\right| \leq 1\right\}}\left|u_{1}-u_{2}\right|^{1 / 2} \theta_{\psi}^{n}+\int_{\left\{\left|u_{1}-u_{2}\right|>1\right\}}\left|u_{1}-u_{2}\right|^{1 / 2} \theta_{\psi}^{n}
\end{aligned}$$
which is less than or equal to
$$\leq I^{1 / 2}\left(\left(\int_{\left\{\left|u_{1}-u_{2}\right| \leq 1\right\}} \theta_{\psi}^{n}\right)^{1 / 2}+\left(\int_{\left\{\left|u_{1}-u_{2}\right|>1\right\}}\left|u_{1}-u_{2}\right| \theta_{\psi}^{n}\right)^{1 / 2}\right),$$
where the last estimate holds due to the Cauchy-Schwarz inequality. Moreover, it follows from Chern-Levine-Nirenberg inequality ([43]) that
$$\begin{aligned}
\int_{X}\left|u_{1}-a_{1}-u_{2}+a_{2}\right| \theta_{\psi}^{n} & =\frac{\varrho}{\operatorname{vol}(X)} \int_{X}\left|u_{1}-a_{1}-u_{2}+a_{2}\right|\left(d d^{c} w+\omega\right)^{n} \\
& \leq C_{2} \varrho\left(\left\|u_{1}-a_{1}\right\|_{L^{1}(X)}+\left\|u_{2}-a_{2}\right\|_{L^{1}(X)}\right) \\
& \leq \varrho C_{3} A,
\end{aligned}$$
where $C_{2}, C_{3}>0$ depend only on $X$ and $\omega$. Here, the last estimate holds due to the compactness of $\left\{u \in \operatorname{PSH}(X, \omega): \sup _{X} u=0\right\}$ in $L^{1}(X)$.

Hence, we have
$$\frac{\varrho}{\operatorname{vol}(X)} \int_{X}\left|u_{1}-u_{2}\right|^{1 / 2}\left(\omega+d d^{c} w\right)^{n} \leq C_{4} I^{1 / 2} \varrho^{1 / 2}\left(A+\left|a_{1}-a_{2}\right|\right)^{1 / 2},$$
where $C_{4}>0$ depends only on $X$ and $\omega$.
Combining (3.34) and (3.35), we get
$$\begin{aligned}
\left(\int_{X}\left|u_{1}-u_{2}\right|^{1 / 2}\left(\omega+d d^{c} w\right)^{n}\right)^{2} & \leq C_{5}\left(A+\left|a_{1}-a_{2}\right|\right)\left(-\chi\left(-\left|a_{1}-a_{2}\right|-\lambda\right)+A(A+B)^{2} \lambda^{\gamma}\right) \\
& \leq C_{5}\left(A+\left|a_{1}-a_{2}\right|\right)\left(\left|a_{1}-a_{2}\right|+\lambda+A(A+B)^{2} \lambda^{\gamma}\right) \\
& \leq C_{6}\left(A+\left|a_{1}-a_{2}\right|\right)\left(\left|a_{1}-a_{2}\right|+A(A+B)^{2} \lambda^{\gamma}\right),
\end{aligned}$$
where $C_{5}, C_{6}>0$ depend only on $n, X, \omega$ and $\gamma$. Since $w$ is arbitrary, we obtain desired inequality. The proof is completed. \(\square\)

Remark 3.13. If $B \geq A$ then the inequality (3.32) is equivalent to
$$d_{\text {cap }}\left(u_{1}, u_{2}\right)^{2} \leq \widetilde{C}\left(A+\left|a_{1}-a_{2}\right|\right)\left(\left|a_{1}-a_{2}\right|+A B^{2} \lambda^{\gamma}\right),$$
where $\tilde{C}>0$ depends only on $n, X, \omega$ and $\gamma$.

\subsection*{3.4.3 Relation to Darvas's metrics on the space of potentials of finite energy}

Let $\chi \in \mathcal{W}^{-} \cup \mathcal{W}_{M}^{+}$. Let $\theta$ be a closed smooth real (1, 1)-form in a big cohomology class. When $\theta$ is Kähler, it was proved in [11, 12, 14] that there is a natural metric $d_{\chi}$ on $\mathcal{E}_{\chi}(X, \theta)$ which makes the last space to be a complete metric space. When $\chi(t)=t$, such metrics have a long history and play an important role in the study of complex Monge-Ampère equations. We refer to these last references and [3, 4] for more details. We now draw the connection between $I_{\chi}(u, v)$ and the metric on $\mathcal{E}_{\chi}(X, \theta)$. Let
$$\tilde{I}_{\chi}(u, v)=\int_{\{u<v\}}-\chi(u-v)\left(\theta_{v}^{n}+\theta_{u}^{n}\right)+\int_{\{u>v\}}-\chi(v-u)\left(\theta_{u}^{n}+\theta_{v}^{n}\right) \geq I_{\chi}(u, v) .$$
By [11, 12, 14], there exists a constant $C>0$ such that
$$C^{-1} \tilde{I}_{\chi}(u, v) \leq d_{\chi}(u, v) \leq C \tilde{I}_{\chi}(u, v)$$
for every $u, v \in \mathcal{E}_{\chi}(X, \theta)$ and $\theta$ is Kähler. It was proved in [37] (and also [11, 15, 21, 62, 70]) that $\tilde{I}_{\chi}(u, v)$ satisfies a quasi-triangle inequality, and the convergence in $\tilde{I}_{\chi}(u, v)$ implies the convergence in capacity by using the plurisubharmonic envelope. Such a method is not quantitative. We present below quantitative version of this fact by using our approach.

Theorem 3.14. Let $\theta \leq A \omega$ be a closed smooth real (1, 1)-form ( $A \geq 1$ is a constant) and $\phi$ be a model $\theta$-psh function with $\varrho:=\operatorname{vol}\left(\theta_{\phi}\right)>0$. Let $B \geq 1, \tilde{\chi} \in \mathcal{W}^{-}$and $u_{1}, u_{2} \in \mathcal{E}(X, \theta, \phi)$ such that $\left|\sup _{X} u_{1}-\sup _{X} u_{2}\right| \leq A, \tilde{\chi}(-1)=-1$ and
$$E_{\tilde{\chi}, \theta, \phi}^{0}\left(u_{1}\right)+E_{\tilde{\chi}, \theta, \phi}^{0}\left(u_{2}\right) \leq B .$$
Then there exist $C>0$ depending only on $n, X$ and $\omega$ such that
$$d_{c a p}\left(u_{1}, u_{2}\right)^{2} \leq \frac{C A(A+B)^{2}}{h^{\circ n}\left(\varrho / \tilde{I}_{\tilde{\chi}}\left(u_{1}, u_{2}\right)\right)},$$
where $h(s)=(-\tilde{\chi}(-s))^{1 / 2}$ for every $0 \leq s \leq \infty$.
One sees from the above estimate that if $\tilde{I}_{\tilde{\chi}}\left(u_{1}, u_{2}\right)$ is small, then so is $d_{\text {cap }}\left(u_{1}, u_{2}\right)$ (uniformly in $u_{1}, u_{2} \in \mathcal{E}(X, \theta, \phi)$ of $\tilde{\chi}$-energy bounded by a fixed constant).

Proof. Let $\chi(t)=\max \{t,-1\}$. Suppose that $w$ is an arbitrary $\omega$-psh function satisfying $0 \leq w \leq 1$. By the proof of Theorem 3.12 (see (3.35)), there exists $C_{1}>0$ depending only on $X$ and $\omega$ such that
$$\left(\int_{X}\left|u_{1}-u_{2}\right|^{1 / 2}\left(\omega+d d^{c} w\right)^{n}\right)^{2} \leq C_{1} A \varrho^{-1} \int_{X}-\chi\left(-\left|u_{1}-u_{2}\right|\right) \theta_{\psi}^{n},$$
where $\psi$ is defined by (3.33). Moreover, it follows from Theorem 3.1 and Proposition 3.10 that
$$\int_{X}-\chi\left(-\left|u_{1}-u_{2}\right|\right) \theta_{\psi}^{n} \leq \tilde{I}_{\chi}\left(u_{1}, u_{2}\right)+C_{2} \varrho(A+B)^{2} Q_{\chi, \tilde{\chi}}^{\circ(n)}\left(I_{\chi}^{0}\left(u_{1}, u_{2}\right)\right),$$
where $C_{2}>0$ depends only on $n$. Therefore, by the facts $Q^{\circ(n)}(s)=\frac{1}{h^{\circ(n)}(1 / s)}$ and $\left.I_{\chi}\left(u_{1}, u_{2}\right) \leq \tilde{I}_{\chi}\left(u_{1}, u_{2}\right) \leq \tilde{I}_{\tilde{\chi}}\left(u_{1}, u_{2}\right)\right)$, we obtain
$$\int_{X}-\chi\left(-\left|u_{1}-u_{2}\right|\right) \theta_{\psi}^{n} \leq \frac{C_{3} \varrho(A+B)^{2}}{h^{\circ(n)}\left(\varrho / \tilde{I}_{\tilde{\chi}}\left(u_{1}, u_{2}\right)\right)},$$
where $C_{3}>0$ depends only on $n, X$ and $\omega$. Combining (3.36) and (3.37), we get
$$\left(\int_{X}\left|u_{1}-u_{2}\right|^{1 / 2}\left(\omega+d d^{c} w\right)^{n}\right)^{2} \leq \frac{C A(A+B)^{2}}{h^{\circ(n)}\left(\varrho / \tilde{I}_{\tilde{\chi}}\left(u_{1}, u_{2}\right)\right)},$$
where $C>0$ depends only on $n, X$ and $\omega$. Since $w$ is arbitrary, we get the desired inequality. The proof is completed. \(\square\)

When $\tilde{\chi} \in \mathcal{W}_{M}^{+}$, our estimate is more explicit.
Theorem 3.15. Let $\theta \leq A \omega$ be a closed smooth real (1, 1)-form ( $A \geq 1$ ) and $\phi$ be a model $\theta$ -psh function such that $\varrho:=\operatorname{vol}\left(\theta_{\phi}\right)>0$. Let $B \geq 1, \tilde{\chi} \in \mathcal{W}_{M}^{+}(M \geq 1)$ and $u_{1}, u_{2} \in \mathcal{E}(X, \theta, \phi)$ such that $\tilde{\chi}(-1)=-1$ and
$$E_{\tilde{\chi}, \theta, \phi}^{0}\left(u_{1}\right)+E_{\tilde{\chi}, \theta, \phi}^{0}\left(u_{2}\right) \leq B .$$
Then there exists $C>0$ depending only on $n$ and $M$ such that
$$\int_{X}-\tilde{\chi}\left(-\left|u_{1}-u_{2}\right|\right) \theta_{\psi}^{n} \leq C \varrho B^{2}\left(\tilde{I}_{\tilde{\chi}}\left(u_{1}, u_{2}\right) / \varrho\right)^{2^{-n}},$$
for every $\psi \in \operatorname{PSH}(X, \theta)$ with $\phi-1 \leq \psi \leq \phi$. Moreover, if $\sup _{X} u_{1}=\sup _{X} u_{2}$ then there exists $C^{\prime}>0$ depending on $n, X, \omega, A$ and $M$ such that
$$\tilde{I}_{\tilde{\chi}}\left(u_{1}, u_{2}\right) \leq C^{\prime} \varrho A^{1 / 2} B^{2}\left(I_{\tilde{\chi}}^{0}\left(u_{1}, u_{2}\right)\right)^{2^{-n-1}} .$$
Proof. The case $I_{\tilde{\chi}}^{0}\left(u_{1}, u_{2}\right) \geq 1$ is trivial. It remains to consider the case $I_{\tilde{\chi}}^{0}\left(u_{1}, u_{2}\right)<1$.
Denote $v=\max \left\{u_{1}, u_{2}\right\}$. By Lemma 2.7, we have $v \in \mathcal{E}(X, \theta, \phi)$ and $E_{\tilde{\chi}, \theta, \phi}^{0}(v) \leq C_{1} B$, where $C_{1}>0$ depends only on $n$ and $M$. Taking $\chi=\tilde{\chi}$ and using Theorem 3.1, we get
$$\int_{X}-\tilde{\chi}\left(u_{j}-v\right) \theta_{\psi}^{n} \leq \int_{X}-\tilde{\chi}\left(u_{j}-v\right) \theta_{u_{j}}^{n}+C_{2} \varrho B^{2}\left(I_{\tilde{\chi}}^{0}\left(u_{j}, v\right)\right)^{2^{-n}},$$
for $j=1,2$, where $C_{2}>0$ depends on $n$ and $M$. Note that
$$\int_{X}-\tilde{\chi}\left(u_{1}-v\right) \theta_{u_{1}}^{n}+\int_{X}-\tilde{\chi}\left(u_{2}-v\right) \theta_{u_{2}}^{n} \leq \int_{X}-\tilde{\chi}\left(-\left|u_{1}-u_{2}\right|\right)\left(\theta_{u_{1}}^{n}+\theta_{u_{2}}^{n}\right)=\tilde{I}_{\tilde{\chi}}\left(u_{1}, u_{2}\right),$$
and
$$I_{\tilde{\chi}}^{0}\left(u_{1}, v\right)+I_{\tilde{\chi}}^{0}\left(u_{2}, v\right)=I_{\tilde{\chi}}^{0}\left(u_{1}, u_{2}\right) \leq \varrho^{-1} \tilde{I}_{\tilde{\chi}}\left(u_{1}, u_{2}\right) .$$
Hence, by (3.38), we get
$$\begin{aligned}
\int_{X}-\tilde{\chi}\left(-\left|u_{1}-u_{2}\right|\right) \theta_{\psi}^{n} & =\int_{X}-\tilde{\chi}\left(u_{1}-v\right) \theta_{\psi}^{n}+\int_{X}-\tilde{\chi}\left(u_{2}-v\right) \theta_{\psi}^{n} \\
& \leq \int_{X}-\tilde{\chi}\left(u_{1}-v\right) \theta_{u_{1}}^{n}+\int_{X}-\tilde{\chi}\left(u_{2}-v\right) \theta_{u_{2}}^{n} \\
& +C_{2} \varrho B^{2}\left(\left(I_{\tilde{\chi}}^{0}\left(u_{1}, v\right)\right)^{2^{-n}}+\left(I_{\tilde{\chi}}^{0}\left(u_{2}, v\right)\right)^{2^{-n}}\right) \\
& \leq \tilde{I}_{\tilde{\chi}}\left(u_{1}, u_{2}\right)+2 C_{2} \varrho B^{2}\left(\tilde{I}_{\tilde{\chi}}\left(u_{1}, u_{2}\right) / \varrho\right)^{2^{-n}} \\
& \leq C_{3} \varrho B^{2}\left(\tilde{I}_{\tilde{\chi}}\left(u_{1}, u_{2}\right) / \varrho\right)^{2^{-n}},
\end{aligned}$$
where $C_{3}>0$ depends on $n$ and $M$. Here, the last estimate holds due to the fact $\tilde{I}_{\tilde{\chi}}\left(u_{1}, u_{2}\right) \leq$ $\varrho B$.

Now, we consider the case $\sup _{X} u_{1}=\sup _{X} u_{2}$. By Theorem 3.2 (choose $m=1$ and $\gamma=1 / 2$ ), there exists $C_{4}>0$ depending only on $n, X, \omega$ and $M$ such that
$$\begin{aligned}
\tilde{I}_{\tilde{\chi}}\left(u_{1}, u_{2}\right) & \leq \int_{X}-\tilde{\chi}\left(-\left|u_{1}-u_{2}\right|\right)\left(\theta_{u_{1}}^{n}+\theta_{u_{2}}^{n}\right) \\
& \leq-2 \varrho \tilde{\chi}\left(-\left(I_{\tilde{\chi}}^{0}\left(u_{1}, u_{2}\right)\right)^{2^{-n}}\right)+C_{4} \varrho A^{1 / 2} B^{2}\left(I_{\tilde{\chi}}^{0}\left(u_{1}, u_{2}\right)\right)^{2^{-n-1}} .
\end{aligned}$$
Moreover, since $\tilde{\chi}$ is concave, we have
$$\frac{\tilde{\chi}(t)}{t} \leq \frac{\tilde{\chi}(-1)}{-1}=1,$$
for every $-1<t<0$. Hence, by (3.39), we have
$$\begin{aligned}
\tilde{I}_{\tilde{\chi}}\left(u_{1}, u_{2}\right) & \leq 2 \varrho\left(I_{\tilde{\chi}}^{0}\left(u_{1}, u_{2}\right)\right)^{2^{-n}}+C_{4} \varrho A^{1 / 2} B^{2}\left(I_{\tilde{\chi}}^{0}\left(u_{1}, u_{2}\right)\right)^{2^{-n-1}} \\
& \leq\left(2+C_{4}\right) \varrho A^{1 / 2} B^{2}\left(I_{\tilde{\chi}}^{0}\left(u_{1}, u_{2}\right)\right)^{2^{-n-1}} .
\end{aligned}$$
The proof is completed. \(\square\)

\subsection*{3.4.4 Comparison of capacities}

For every Borel subset $E$ in $X$ and for every $\varphi \in \mathrm{PSH}(X, \theta)$, one denotes
$$\operatorname{cap}_{\theta, \varphi}(E):=\sup \left\{\int_{E} \theta_{\psi}^{n}: \psi \in \operatorname{PSH}(X, \theta), \quad \varphi-1 \leq \psi \leq \varphi\right\} .$$

In [48], Lu showed that if $\varphi_{j}(j=1,2)$ is a $\theta_{j}$-psh function with $\int_{X}\left(\theta_{j}+d d^{c} \varphi_{j}\right)^{n}>0$ then there exists a continuous function $f: \mathbb{R}_{\leq 0} \rightarrow \mathbb{R}_{\geq 0}$ with $f(0)=0$ such that $\operatorname{cap}_{\theta_{1}, \varphi_{1}}(E) \leq$ $f\left(\operatorname{cap}_{\theta_{2}, \varphi_{2}}(E)\right)$ for every Borel set $E \subset X$. As an application of Theorem 3.2, by giving a very explicit form for $f$, we will strengthen Lu's result for the case where $\varphi_{j}$ is a model $\theta_{j}$-psh function.

First, we need the following lemma:
Lemma 3.16. Let $A, B>0$ be constants. Let $\theta$ be a closed smooth real (1, 1)-form representing a big cohomology class such that $\theta \leq A \omega$. Assume that $u, v$ are $\theta$-psh functions satisfying $v \leq u \leq v+B$. Then,
$$\int_{X}(-\psi) \theta_{u}^{n} \leq \int_{X}(-\psi) \theta_{v}^{n}+n A^{n} B \int_{X} \omega^{n},$$
for every negative $A \omega$-psh function $\psi$.
Proof. Using approximations, we can assume that $\psi$ is smooth. Denote
$$T=\sum_{l=0}^{n-1} \theta_{u}^{l} \wedge \theta_{v}^{n-l-1} .$$
We have $\theta_{u}^{n}-\theta_{v}^{n}=d d^{c}(u-v) \wedge T$. Moreover, using integration by parts (Theorem 2.2), we get
$$\int_{X}(-\psi) d d^{c}(u-v) \wedge T=\int_{X}(u-v) d d^{c}(-\psi) \wedge T \leq A \int_{X}(u-v) \omega \wedge T \leq n A^{n} B \int_{X} \omega^{n} .$$
Hence
$$\int_{X}(-\psi) \theta_{u}^{n} \leq \int_{X}(-\psi) \theta_{v}^{n}+n A^{n} B \int_{X} \omega^{n} .$$ \(\square\)

Theorem 3.17. (Comparison of capacities) Assume that $\theta_{1}, \theta_{2} \leq A \omega$ are closed smooth real (1, 1)-forms representing big cohomology classes and, for $j=1,2, \phi_{j}$ is a model $\theta_{j}$-psh function satisfying $\int_{X}\left(\theta_{j}+d d^{c} \phi_{j}\right)^{n}=\varrho_{j}>0$. Then, for every $0<\gamma<1$, there exists $C>0$ depending only on $n, X, \omega, A$ and $\gamma$ such that
$$\frac{\operatorname{cap}_{\theta_{1}, \phi_{1}}(E)}{\varrho_{1}} \leq C\left(\frac{\operatorname{cap}_{\theta_{2}, \phi_{2}}(E)}{\varrho_{2}}\right)^{2^{-n} \gamma},$$
for every Borel set $E \subset X$.
Proof. By the inner regularity of capacities (see [16, Lemma 4.2]), we only need consider the case where $E$ is compact. Since the case $\operatorname{cap}_{\theta_{2}, \phi_{2}}(E)=\varrho_{2}$ is trivial, we can also assume that $\operatorname{cap}_{\theta_{2}, \phi_{2}}(E)<\varrho_{2}$. In particular, by [17, Proposition 3.7] and [18, Lemma 2.7], we have
$$\sup _{X} h_{E, \theta_{2}, \phi_{2}}^{*}=\sup _{X}\left(h_{E, \theta_{2}, \phi_{2}}^{*}-\phi_{2}\right)=0,$$
where
$$h_{E, \theta_{2}, \phi_{2}}=\sup \left\{w \in \operatorname{PSH}\left(X, \theta_{2}\right):\left.w\right|_{E} \leq \phi_{2}-1, w \leq \phi_{2}\right\} .$$
Set $\chi(t)=\tilde{\chi}(t)=t$. We will use Theorem 3.2 for $u_{1}=\left(h_{E, \theta_{2}, \phi_{2}}\right)^{*}$ and $u_{2}=\phi_{2}$. It is clear that $E_{\tilde{\chi}, \theta_{2}, \phi_{2}}^{0}\left(u_{2}\right)=0$ and $u_{1}=u_{2}-1$ on $E \backslash N$, where $N$ is a pluripolar set. Moreover, it follows from [17, Proposition 3.7] that
$$I_{\chi}^{0}\left(u_{1}, u_{2}\right) \leq E_{\tilde{\chi}, \theta_{2}, \phi_{2}}^{0}\left(u_{1}\right)=\varrho_{2}^{-1} \operatorname{cap}_{\theta_{2}, \phi_{2}}(E) \leq 1 .$$
By Theorem 3.2, for every $0<\gamma<1$ and $B \geq 1$, there exists $C>0$ depending only on $X, \omega, n, A$ and $\gamma$ such that
$$\int_{E} \theta_{\psi}^{n} \leq \int_{X} \chi\left(-\left|u_{1}-u_{2}\right|\right) \theta_{\psi}^{n} \leq C \varrho_{2} A(A+B)^{2}\left(\operatorname{cap}_{\theta_{2}, \phi_{2}}(E) / \varrho_{2}\right)^{2^{-n} \gamma},$$
for every compact set $E$ and for each $\psi \in \mathcal{E}\left(X, \theta_{2}, \phi_{2}\right)$ with $E_{\tilde{\chi}, \theta_{2}, \phi_{2}}^{0}(\psi) \leq B$. Let $\varphi \in$ $\mathcal{E}\left(X, \theta_{1}, \phi_{1}\right)$ such that $\phi_{1}-1 \leq \varphi \leq \phi_{1}$ and $\int_{E}\left(\theta_{1}+d d^{c} \varphi\right)^{n} \geq \frac{1}{2} \operatorname{cap}_{\theta_{1}, \phi_{1}}(E)$. By [17], there exists a unique function $\psi_{0} \in \mathcal{E}\left(X, \theta_{2}, \phi_{2}\right)$ such that $\sup _{X} \psi_{0}=0$ and $\left(\theta_{2}+d d^{c} \psi_{0}\right)^{n}=$ $\frac{\varrho_{2}}{\varrho_{1}}\left(\theta_{1}+d d^{c} \varphi\right)^{n}$. When $\psi=\psi_{0}$, we have
$$\int_{E} \theta_{\psi}^{n} \geq \frac{\varrho_{2}}{2 \varrho_{1}} \operatorname{cap}_{\theta_{1}, \phi_{1}}(E) .$$
Moreover, by using Lemma 3.16 for $\varphi, \phi_{1}$ and using the fact that $\left(\theta_{2}+d d^{c} \phi_{2}\right)^{n} \leq \mathbf{1}_{\left\{\phi_{2}=0\right\}} \theta_{2}^{n}$ (see [16, Theorem 3.8]), we have
$$\varrho_{1} E_{\tilde{\chi}, \theta_{2}, \phi_{2}}^{0}\left(\psi_{0}\right)=\int_{X}\left(\phi_{2}-\psi_{0}\right)\left(\theta_{1}+d d^{c} \varphi\right)^{n} \leq \int_{X}\left(-\psi_{0}\right)\left(\theta_{1}+d d^{c} \phi_{1}\right)^{n}+n A^{n} \int_{X} \omega^{n} \leq B,$$
where $B \geq 1$ depends only on $A, X, \omega, n$. Combining (3.40), (3.41) and (3.42), we get
$$\begin{aligned}
\operatorname{cap}_{\theta_{1}, \phi_{1}}(E) \leq \frac{2 \varrho_{1}}{\varrho_{2}} \int_{E} \theta_{\psi_{0}}^{n} & \leq \frac{2 \varrho_{1}}{\varrho_{2}} \int_{X} \chi\left(-\left|u_{1}-u_{2}\right|\right) \theta_{\psi_{0}}^{n} \\
& \leq 2 C \varrho_{1} A(A+B)^{2}\left(\operatorname{cap}_{\theta_{2}, \phi_{2}}(E) / \varrho_{2}\right)^{2^{-n} \gamma} .
\end{aligned}$$
The proof is completed. \(\square\)

\section*{4 Stability estimates for varied singularity type and cohomology class}

\subsection*{4.1 Pseudo-metric on the space of singularity types}

We first recall some facts about the pseudo-metric on the space of singularity types. Let $\alpha$ be a big cohomology class and $\theta$ a smooth closed (1,1)-form in $\alpha$. Let $\mathcal{S}(\theta)$ be the space of singularity types of $\theta$-psh functions and
$$\mathcal{S}_{\delta}(\theta):=\left\{[u] \in \mathcal{S}(\theta): \int_{X} \theta_{u}^{n} \geq \delta\right\} .$$

The pseudo-distance $d_{\mathcal{S}}$ on $\mathcal{S}$ was introduced in [18], and it satisfies
$$d_{\mathcal{S}(\theta)}([u],[v]) \leq \sum_{j=0}^{n}\left(2 \int_{X} \theta_{V_{\theta}}^{j} \wedge \theta_{\max \{u, v\}}^{n-j}-\int_{X} \theta_{V_{\theta}}^{j} \wedge \theta_{u}^{n-j}-\int_{X} \theta_{V_{\theta}}^{j} \wedge \theta_{v}^{n-j}\right) \leq C d_{\mathcal{S}(\theta)}([u],[v]),$$
where $C>1$ depends only on $n$. Here $V_{\theta}$ is the upper envelope of all non-positive $\theta$-psh functions:
$$V_{\theta}:=\sup \{\varphi \in \operatorname{PSH}(X, \theta): \varphi \leq 0 \quad \text { on } \quad X\} .$$

For all $\theta$-psh functions $u, v$, we put
$$d_{\theta}(u, v):=2 \int_{X} \theta_{\max \{u, v\}}^{n}-\int_{X} \theta_{u}^{n}-\int_{X} \theta_{v}^{n} .$$
In particular, if $u \leq v$ then $d_{\theta}(u, v)=\int_{X} \theta_{v}^{n}-\int_{X} \theta_{u}^{n}$. By (4.1), we have
$$d_{\theta}(u, v) \leq C d_{\mathcal{S}(\theta)}([u],[v]),$$
where $C=C(n)>0$. Moreover, if $\theta=A \omega$ for some $A>0$ then, we have
$$d_{\mathcal{S}(A \omega)}([u],[v]) \leq A^{n} d_{(A+1) \omega}(u, v),$$
for every $u, v \in \operatorname{PSH}(X, A \omega)$. In the sequel, we provide more properties of $d_{\theta}$.
Lemma 4.1. Let $u_{1}, u_{2}$ be $\theta$-psh functions. Let $\theta^{\prime}$ be a smooth real closed $(1,1)$-form such that $\theta^{\prime} \geq \theta$. Then
$$d_{\theta}\left(u_{1}, u_{2}\right) \leq d_{\theta^{\prime}}\left(u_{1}, u_{2}\right) .$$
Proof. By the fact $d_{\eta}\left(u_{1}, u_{2}\right)=d_{\eta}\left(u_{1}, \max \left\{u_{1}, u_{2}\right\}\right)+d_{\eta}\left(u_{2}, \max \left\{u_{1}, u_{2}\right\}\right)$ for $\eta=\theta, \theta^{\prime}$, the problem is reduced to the case $u_{1} \leq u_{2}$. Then we have
$$d_{\eta}\left(u_{1}, u_{2}\right)=\int_{X}\left(\eta+d d^{c} u_{2}\right)^{n}-\int_{X}\left(\eta+d d^{c} u_{1}\right)^{n},$$
for $\eta=\theta, \theta^{\prime}$. Moreover,
$$\left(\theta^{\prime}+d d^{c} u_{j}\right)^{n}-\left(\theta+d d^{c} u_{j}\right)^{n}=\left(\theta^{\prime}-\theta\right) \wedge \sum_{l=0}^{n-1}\left(\theta^{\prime}+d d^{c} u_{j}\right)^{l} \wedge\left(\theta+d d^{c} u_{j}\right)^{n-l-1},$$
for $j=1,2$. Hence
$$d_{\theta^{\prime}}\left(u_{1}, u_{2}\right)-d_{\theta}\left(u_{1}, u_{2}\right)=\int_{X}\left(\theta^{\prime}-\theta\right) \wedge T_{2}-\int_{X}\left(\theta^{\prime}-\theta\right) \wedge T_{1},$$
where
$$T_{j}=\sum_{l=0}^{n-1}\left(\theta^{\prime}+d d^{c} u_{j}\right)^{l} \wedge\left(\theta+d d^{c} u_{j}\right)^{n-l-1} .$$
Thus, by the monotonicity of non-pluripolar products [16, Theorem 1.1], we obtain
$$d_{\theta^{\prime}}\left(u_{1}, u_{2}\right)-d_{\theta}\left(u_{1}, u_{2}\right) \geq 0 .$$
The proof is completed. \(\square\)

Lemma 4.2. Let $\delta>0, A>0$ be constants. Let $u, v$ be $\theta$-psh functions such that $u \leq v$ and $\int_{X} \theta_{u}^{n} \geq \delta$. Let $\psi$ be an $\eta$-psh function, where $\eta$ is a closed smooth (1,1)-form. Assume that $\theta \leq A \omega, \eta \leq A \omega$. Then there exists a constant $C$ depending only on $n, \omega$ such that
$$\left|\int_{X} \theta_{u}^{m} \wedge \eta_{\psi}^{n-m}-\int_{X} \theta_{v}^{m} \wedge \eta_{\psi}^{n-m}\right| \leq C A^{n}\left(\frac{d_{\theta}(u, v)}{\delta}\right)^{1 / n} .$$
Proof. This is essentially the proof of [18, Proposition 4.8]. Note that by monotonicity we have
$$d_{\theta}(u, v)=\int_{X} \theta_{v}^{n}-\int_{X} \theta_{u}^{n}, \quad \int_{X} \theta_{v}^{m} \wedge \eta_{\psi}^{n-m} \geq \int_{X} \theta_{u}^{m} \wedge \eta_{\psi}^{n-m} .$$
Without loss of generality, we can assume $d_{\theta}(u, v) \leq \delta / 2^{n+2}$. If $d_{\theta}(u, v)=0$, then using $u \leq v$ and [16], we get $P_{\theta}[u]=P_{\theta}[v]$. In this case the left-hand side of the desired inequality is also zero. Hence from now on we assume $d_{\theta}(u, v)>0$.

Let $b>2$ be a constant such that $\delta / d_{\theta}(u, v)<2 b^{n}<2 \delta / d_{\theta}(u, v)$. We have
$$b^{n} \int_{X} \theta_{u}^{n} \geq\left(b^{n}-1\right) \int_{X} \theta_{v}^{n} .$$
By this and [18, Lemma 4.3], we obtain $w_{b}:=P_{\theta}(b u+(1-b) v) \in \operatorname{PSH}(X, \theta)$. Observe
$$b^{-1} w_{b}+\left(1-b^{-1}\right) v \leq b^{-1}(b u+(1-b) v)+\left(1-b^{-1}\right) v=u .$$
Combining this with monotonicity of non-pluripolar products gives
$$\int_{X} \theta_{u}^{m} \wedge \eta_{\psi}^{n-m} \geq \int_{X} \theta_{b^{-1} w_{b}+\left(1-b^{-1}\right) v}^{m} \wedge \eta_{\psi}^{n-m} \geq\left(1-b^{-1}\right)^{m} \int_{X} \theta_{v}^{m} \wedge \eta_{\psi}^{n-m} .$$
It follows that
$$\int_{X} \theta_{u}^{m} \wedge \eta_{\psi}^{n-m}-\int_{X} \theta_{v}^{m} \wedge \eta_{\psi}^{n-m} \geq-m b^{-1} \int_{X} \theta_{v}^{m} \wedge \eta_{\psi}^{n-m} \geq-n b^{-1} A^{n} \int_{X} \omega^{n}$$
by monotonicity. Hence
$$\left|\int_{X} \theta_{u}^{m} \wedge \eta_{\psi}^{n-m}-\int_{X} \theta_{v}^{m} \wedge \eta_{\psi}^{n-m}\right| \leq C b^{-1} \leq 2^{1 / n} C\left(\frac{d_{\theta}(u, v)}{\delta}\right)^{1 / n},$$
where $C:=n A^{n} \int_{X} \omega^{n}$. This finishes the proof. \(\square\)

By Lemma 4.2, we have
Proposition 4.3. Let $\alpha, \theta$ be as above. Then there exists a constant $C>0$ such that
$$C^{-1} \delta d_{\mathcal{S}(\theta)}([u],[v])^{n} \leq d_{\theta}(u, v) \leq C d_{\mathcal{S}(\theta)}([u],[v])$$
for every $[u],[v] \in \mathcal{S}_{\delta}(\alpha)$. Moreover if $\theta^{\prime}$ is a smooth real closed $(1,1)$-form and $A$ is a positive constant such that
$$\theta^{\prime} \leq A \omega, \quad \theta \leq A \omega,$$
for some constant $A>0$, then there exists a constant $C_{1}>0$ depending only on $A, \omega$ such that
$$\delta\left(d_{\theta^{\prime}}(u, v)\right)^{n} \leq C_{1} d_{\theta}(u, v),$$
for every $u, v \in \mathcal{S}_{\delta}(\alpha)$.

Proof. The first desired assertion is clear from Lemma 4.2. Also by the same lemma, one gets
$$\delta\left(d_{A \omega}(u, v)\right)^{n} \leq C_{1} d_{\theta}(u, v),$$
for every $u, v \in \mathcal{S}_{\delta}(\alpha)$, and some constant $C_{1}$ independent of $u, v, \delta$. This coupled with Lemma 4.1 gives the last desired inequality. The proof is complete. \(\square\)

If $\theta^{\prime}$ is another closed smooth form in $\alpha$, then $\mathcal{S}_{\delta}(\theta)$ and $\mathcal{S}_{\delta}\left(\theta^{\prime}\right)$ are isometric under the map $u \mapsto u+\varphi$, where $\varphi$ is a smooth function such that $d d^{c} \varphi=\theta^{\prime}-\theta$. Hence in general in order to study singularity types in $\alpha$, it is enough to fix a smooth form in $\alpha$.

\subsection*{4.2 The case of fixed cohomology}

In this subsection, we will study the stability question when solutions are in the same cohomology class.

\subsection*{4.2.1 Proof of Theorem 1.2}

Let $\theta, \eta$ be closed smooth real (1, 1)-forms representing big cohomology classes. For every $\chi \in \widetilde{\mathcal{W}}^{-}$and $u \in \operatorname{PSH}(X, \theta)$, we denote
$$\tilde{E}_{\chi, \eta, \theta}(u)=\sup \left\{\int_{X}-\chi(\psi) \theta_{u}^{n}: \psi \in \mathrm{PSH}^{-}(X, \eta), \sup _{X} \psi=0\right\},$$
where we recall that $\mathrm{PSH}^{-}(X, \eta)$ is the space of negative $\eta$-psh functions on $X$. If $\chi$ is bounded then it is clear that $\tilde{E}_{\chi, \eta, \theta}(u)<\infty$ for every $u \in \operatorname{PSH}(X, \theta)$. Moreover, it follows from [8, Proposition 3.2] that for every $u \in \operatorname{PSH}(X, \theta)$, there exists $\chi \in \mathcal{W}^{-}$such that $\tilde{E}_{\chi, \eta, \theta}(u)<\infty$.

For every constant $B>0$ and for every $\chi \in \widetilde{\mathcal{W}}^{-}$, we define
$$\tilde{\mathcal{E}}_{\chi, \eta, B}(X, \theta)=\left\{u \in \mathrm{PSH}^{-}(X, \theta): \tilde{E}_{\chi, \eta, \theta}(u) \leq B\right\} .$$
For the convenience, in the case $\eta=\theta$, we denote $\tilde{E}_{\chi, \theta}(u):=\tilde{E}_{\chi, \theta, \theta}(u)$ and $\tilde{\mathcal{E}}_{\chi, B}(X, \theta)=$ $\tilde{\mathcal{E}}_{\chi, \theta, B}(X, \theta)$.

If $u, v \in \tilde{\mathcal{E}}_{\chi, B}(X, \theta)$ then we also denote
$$I_{\chi}(u, v)=\int_{\{u<v\}}-\chi(u-v)\left(\theta_{u}^{n}-\theta_{v}^{n}\right)+\int_{\{v<u\}}-\chi(v-u)\left(\theta_{v}^{n}-\theta_{u}^{n}\right) .$$
In general, $I_{\chi}(u, v)$ may be negative. However, by Lemma 4.7 below (observer that there always exists $\tilde{\chi} \in \mathcal{W}^{-}$such that both $\tilde{E}_{\tilde{\chi}, \theta}(u), \tilde{E}_{\tilde{\chi}, \theta}(v)$ are finite), if inf $\chi=-1$ then $I_{\chi}(u, v)$ is bounded from below by $-d_{\theta}(u, v)$.
Lemma 4.4. Let $\chi \in \widetilde{\mathcal{W}}^{-}$. Assume that $u, \phi$ are negative $\theta$-psh functions satisfying $u \leq \phi$. Denote $u_{k}=\max \{u, \phi-k\}$ for every $k>0$. Then
$$\int_{X}-\chi\left(u_{k}-\phi\right) \theta_{u_{k}}^{n}=\int_{X}-\chi(u-\phi) \theta_{u}^{n}-\chi(-k) d_{\theta}(u, \phi),$$
for every $k>0$.

Proof. Since $\theta_{u_{k}}^{n}=\theta_{u}^{n}$ in $\{u>\phi-k\}$ and $u_{k}=\phi-k$ in $\{u \leq \phi-k\}$, we have
$$\int_{X}-\chi\left(u_{k}-\phi\right) \theta_{u_{k}}^{n}=\int_{\{u \leq \phi-k\}}-\chi(-k) \theta_{u_{k}}^{n}+\int_{\{u>\phi-k\}}-\chi(u-\phi) \theta_{u}^{n} .$$
Since $\int_{X} \theta_{\phi}^{n}=\int_{X} \theta_{u_{k}}^{n}$, we have
$$\begin{aligned}
\int_{\{u \leq \phi-k\}}-\chi(-k) \theta_{u_{k}}^{n} & =\int_{X}-\chi(-k) \theta_{u_{k}}^{n}+\int_{\{u>\phi-k\}} \chi(-k) \theta_{u_{k}}^{n} \\
& =\int_{X}-\chi(-k) \theta_{\phi}^{n}+\int_{\{u>\phi-k\}} \chi(-k) \theta_{u}^{n} .
\end{aligned}$$
Combining (4.5) and (4.6), we get
$$\begin{aligned}
\int_{X}-\chi\left(u_{k}-\phi\right) \theta_{u_{k}}^{n} & =\int_{X}-\chi(-k) \theta_{\phi}^{n}+\int_{\{u>\phi-k\}} \chi(-k) \theta_{u}^{n}+\int_{\{u>\phi-k\}}-\chi(u-\phi) \theta_{u}^{n} \\
& =-\chi(-k) d_{\theta}(\phi, u)+\int_{\{u \leq \phi-k\}}-\chi(-k) \theta_{u}^{n}+\int_{\{u>\phi-k\}}-\chi(u-\phi) \theta_{u}^{n} \\
& =-\chi(-k) d_{\theta}(\phi, u)+\int_{X}-\chi(u-\phi) \theta_{u}^{n} .
\end{aligned}$$
The proof is completed. \(\square\)

Lemma 4.5. Let $\chi, \tilde{\chi} \in \widetilde{\mathcal{W}}^{-}$such that $\inf _{\mathbb{R}_{<0} \chi=-1 \text {. Assume that } u_{1}, u_{2}, u_{3}, \phi \text { are negative }}$ $\theta$-psh functions satisfying $u_{1} \leq u_{2} \leq \phi$ and $u_{1} \leq u_{3} \leq \phi$. Denote $u_{j, k}=\max \left\{u_{j}, \phi-k\right\}$ for every $k>1$ and $j=1,2,3$. Then
$$\int_{X}-\chi\left(u_{1, k}-u_{2, k}\right) \theta_{u_{3, k}}^{n} \leq \int_{X}-\chi\left(u_{1}-u_{2}\right) \theta_{u_{3}}^{n}+d_{\theta}\left(u_{3}, \phi\right)+\frac{1}{\tilde{\chi}(-k)} \int_{X} \tilde{\chi}\left(u_{1}-\phi\right) \theta_{u_{3}}^{n},$$
for every $k>1$. In particular, if $\sup _{X} u_{1}=0$ and $u_{3} \in \tilde{\mathcal{E}}_{\tilde{\chi}, B}(X, \theta)$ for some $B>0$ then
$$\int_{X}-\chi\left(u_{1, k}-u_{2, k}\right) \theta_{u_{3, k}}^{n} \leq \int_{X}-\chi\left(u_{1}-u_{2}\right) \theta_{u_{3}}^{n}+d_{\theta}\left(u_{3}, \phi\right)-\frac{B}{\tilde{\chi}(-k)},$$
for every $k>1$.
Proof. Denote
$$I_{k}:=\int_{X}-\chi\left(u_{1, k}-u_{2, k}\right) \theta_{u_{3, k}}^{n} .$$
Since $\theta_{u_{3, k}}^{n}=\theta_{u_{3}}^{n}$ in $\left\{u_{1}>\phi-k\right\} \subset\left\{u_{3}>\phi-k\right\}$, we have
$$\begin{aligned}
I_{k} & =\int_{\left\{u_{1}>\phi-k\right\}}-\chi\left(u_{1}-u_{2}\right) \theta_{u_{3}}^{n}+\int_{\left\{u_{1} \leq \phi-k\right\}}-\chi\left(u_{1, k}-u_{2, k}\right) \theta_{u_{3, k}}^{n} \\
& \leq \int_{\left\{u_{1}>\phi-k\right\}}-\chi\left(u_{1}-u_{2}\right) \theta_{u_{3}}^{n}+\int_{\left\{u_{1} \leq \phi-k\right\}}-\chi(-k) \theta_{u_{3, k}}^{n} \\
& =\int_{\left\{u_{1}>\phi-k\right\}}-\chi\left(u_{1}-u_{2}\right) \theta_{u_{3}}^{n}+\int_{\left\{u_{1} \leq \phi-k\right\}} \theta_{u_{3, k}}^{n} .
\end{aligned}$$

Then, by the fact $\int_{X} \theta_{\phi}^{n}=\int_{X} \theta_{u_{3, k}}^{n}$, we get
$$\begin{aligned}
I_{k} & \leq \int_{\left\{u_{1}>\phi-k\right\}}-\chi\left(u_{1}-u_{2}\right) \theta_{u_{3}}^{n}+\int_{X} \theta_{\phi}^{n}-\int_{\left\{u_{1}>\phi-k\right\}} \theta_{u_{3}}^{n} \\
& =\int_{\left\{u_{1}>\phi-k\right\}}-\chi\left(u_{1}-u_{2}\right) \theta_{u_{3}}^{n}+d_{\theta}\left(u_{3}, \phi\right)+\int_{\left\{u_{1} \leq \phi-k\right\}} \theta_{u_{3}}^{n} \\
& \leq \int_{X}-\chi\left(u_{1}-u_{2}\right) \theta_{u_{3}}^{n}+d_{\theta}\left(u_{3}, \phi\right)+\frac{1}{\tilde{\chi}(-k)} \int_{X} \tilde{\chi}\left(u_{1}-\phi\right) \theta_{u_{3}}^{n} .
\end{aligned}$$
The proof is completed. \(\square\)