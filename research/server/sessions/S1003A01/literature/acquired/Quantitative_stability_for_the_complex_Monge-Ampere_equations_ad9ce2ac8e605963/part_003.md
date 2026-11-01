---
retention_scope: session
part: 3
total_parts: 3
---

[Part 3/3 of: Quantitative stability for the complex Monge-Ampere equations]

Lemma 4.6. Let $\chi, \tilde{\chi} \in \widetilde{\mathcal{W}}^{-}$such that $\inf _{\mathbb{R}_{<0}} \chi=-1$. Assume that $u_{1}, u_{2}, u_{3}, \phi$ are negative $\theta$-psh functions satisfying $u_{1} \leq u_{2} \leq \phi$ and $u_{1} \leq u_{3} \leq \phi$. Denote $u_{j, k}=\max \left\{u_{j}, \phi-k\right\}$ for every $k>1$ and $j=1,2,3$. Then
$$\int_{X}-\chi\left(u_{1, k}-u_{2, k}\right) \theta_{u_{3, k}}^{n} \geq \int_{X}-\chi\left(u_{1}-u_{2}\right) \theta_{u_{3}}^{n}-\frac{1}{\tilde{\chi}(-k)} \int_{X} \tilde{\chi}\left(u_{1}-\phi\right) \theta_{u_{3}}^{n},$$
for every $k>1$. In particular, if $\sup _{X} u_{1}=0$ and $u_{3} \in \tilde{\mathcal{E}}_{\tilde{\chi}, B}(X, \theta)$ for some $B>0$ then
$$\int_{X}-\chi\left(u_{1, k}-u_{2, k}\right) \theta_{u_{3, k}}^{n} \geq \int_{X}-\chi\left(u_{1}-u_{2}\right) \theta_{u_{3}}^{n}+\frac{B}{\tilde{\chi}(-k)},$$
for every $k>1$.
Proof. Since $\theta_{u_{3, k}}^{n}=\theta_{u_{3}}^{n}$ in $\left\{u_{1}>\phi-k\right\}$, we have
$$\begin{aligned}
\int_{X}-\chi\left(u_{1, k}-u_{2, k}\right) \theta_{u_{3, k}}^{n} & \geq \int_{\left\{u_{1}>\phi-k\right\}}-\chi\left(u_{1, k}-u_{2, k}\right) \theta_{u_{3, k}}^{n} \\
& =\int_{\left\{u_{1}>\phi-k\right\}}-\chi\left(u_{1}-u_{2}\right) \theta_{u_{3}}^{n} \\
& =\int_{X}-\chi\left(u_{1}-u_{2}\right) \theta_{u_{3}}^{n}-\int_{\left\{u_{1} \leq \phi-k\right\}}-\chi\left(u_{1}-u_{2}\right) \theta_{u_{3}}^{n} \\
& \geq \int_{X}-\chi\left(u_{1}-u_{2}\right) \theta_{u_{3}}^{n}-\int_{\left\{u_{1} \leq \phi-k\right\}} \theta_{u_{3}}^{n} \\
& \geq \int_{X}-\chi\left(u_{1}-u_{2}\right) \theta_{u_{3}}^{n}-\frac{1}{\tilde{\chi}(-k)} \int_{X} \tilde{\chi}\left(u_{1}-\phi\right) \theta_{u_{3}}^{n} .
\end{aligned}$$
This finishes the proof. \(\square\)

Lemma 4.7. Let $\theta$ be a closed smooth real (1, 1)-form representing a big cohomology class. Let $\chi, \tilde{\chi} \in \widetilde{\mathcal{W}}^{-}$such that $\inf _{\mathbb{R}_{<0}} \chi=-1$. Assume that $B>0$ and $u_{1}, u_{2} \in \tilde{\mathcal{E}}_{\tilde{\chi}, B}(X, \theta)$ with $\sup _{X} u_{1}=\sup _{X} u_{2}=0$. Denote $\phi=P_{\theta}\left[\max \left\{u_{1}, u_{2}\right\}\right]$ and $u_{j, k}=\max \left\{u_{j}, \phi-k\right\}$ for every $k>1$ and $j=1,2$. Then
$$E_{\tilde{\chi}, \theta, \phi}\left(u_{j, k}\right) \leq B-\tilde{\chi}(-k) d_{\theta}\left(u_{j}, \phi\right),$$
and
$$\frac{4 B}{\tilde{\chi}(-k)} \leq I_{\chi}\left(u_{1, k}, u_{2, k}\right)-I_{\chi}\left(u_{1}, u_{2}\right) \leq-\frac{4 B}{\tilde{\chi}(-k)}+d_{\theta}\left(u_{1}, u_{2}\right),$$
for every $k>1$.
Proof. The first inequality is obtained directly from Lemma 4.4. It remains to prove (4.8). For $j=1,2$ and $k>1$, we denote
$$I_{1, j}=\int_{\left\{u_{1}<u_{2}\right\}}-\chi\left(u_{1, k}-u_{2, k}\right) \theta_{u_{j, k}}^{n}+\int_{\left\{u_{1}<u_{2}\right\}} \chi\left(u_{1}-u_{2}\right) \theta_{u_{j}}^{n},$$
and
$$I_{2, j}=\int_{\left\{u_{2}<u_{1}\right\}}-\chi\left(u_{2, k}-u_{1, k}\right) \theta_{u_{j, k}}^{n}+\int_{\left\{u_{1}<u_{2}\right\}} \chi\left(u_{2}-u_{1}\right) \theta_{u_{j}}^{n} .$$
We have
$$I_{\chi}\left(u_{1, k}, u_{2, k}\right)-I_{\chi}\left(u_{1}, u_{2}\right)=\left(I_{1,1}-I_{1,2}\right)+\left(I_{2,2}-I_{2,1}\right):=I_{1}+I_{2} .$$
We will estimate $I_{1}$ and $I_{2}$. By Lemmas 4.5 and 4.6 (replace $u_{2}, u_{3}$ and $\phi$, respectively, by $\max \left\{u_{1}, u_{2}\right\}, u_{1}$ and $\max \left\{u_{1}, u_{2}\right\}$ ), we have
$$\frac{B}{\tilde{\chi}(-k)} \leq I_{1,1} \leq d_{\theta}\left(u_{1}, \max \left\{u_{1}, u_{2}\right\}\right)-\frac{B}{\tilde{\chi}(-k)} .$$
Using Lemmas 4.5 and 4.6 again (replace $u_{2}, u_{3}$ and $\phi$ by $\max \left\{u_{1}, u_{2}\right\}$ ), we get
$$\frac{B}{\tilde{\chi}(-k)} \leq \int_{\left\{u_{1}<u_{2}\right\}}-\chi\left(u_{1, k}-u_{2, k}\right) \theta_{u_{2, k}}^{n}+\int_{\left\{u_{1}<u_{2}\right\}} \chi\left(u_{1}-u_{2}\right) \theta_{u_{2}}^{n} \leq-\frac{B}{\tilde{\chi}(-k)} .$$
Combining (4.10) and (4.11), we obtain
$$\frac{2 B}{\tilde{\chi}(-k)} \leq I_{1} \leq-\frac{2 B}{\tilde{\chi}(-k)}+d_{\theta}\left(u_{1}, \max \left\{u_{1}, u_{2}\right\}\right) .$$
Similar, we have
$$\frac{2 B}{\tilde{\chi}(-k)} \leq I_{2} \leq-\frac{2 B}{\tilde{\chi}(-k)}+d_{\theta}\left(u_{2}, \max \left\{u_{1}, u_{2}\right\}\right) .$$
Combining (4.9), (4.12) and (4.13), we have
$$\frac{4 B}{\tilde{\chi}(-k)} \leq I_{\chi}\left(u_{1, k}, u_{2, k}\right)-I_{\chi}\left(u_{1}, u_{2}\right) \leq-\frac{4 B}{\tilde{\chi}(-k)}+d_{\theta}\left(u_{1}, u_{2}\right) .$$
The proof is completed. \(\square\)

The following theorem is the key step to prove the main results in the case of fixed cohomology:

Theorem 4.8. Let $\theta \leq A \omega$ be a closed smooth real (1, 1)-form representing a big cohomology class $(A \geq 1)$. Let $0<\delta<1, B \geq A, \tilde{\chi} \in \widetilde{\mathcal{W}}^{-}$and $u_{1}, u_{2} \in \tilde{\mathcal{E}}_{\tilde{\chi}, B \delta}(X, \theta)$ such that $\inf \tilde{\chi}<\tilde{\chi}(-1)=-1, \sup _{X} u_{1}=\sup _{X} u_{2}=0$ and $\int_{X} \theta_{u_{1}}^{n}+\int_{X} \theta_{u_{2}}^{n} \geq 2 \delta$. Let $\epsilon>0$ be a constant such that
$$\inf \tilde{\chi}<\frac{-4 B \delta}{\epsilon+d_{\theta}\left(u_{1}, u_{2}\right)} .$$
Then, for every $0<\gamma<1$, there exists $C>0$ depending only on $n, X, \omega$ and $\gamma$ such that
$$d_{\text {cap }}\left(u_{1}, u_{2}\right)^{2} \leq C(A B)^{2}\left(h^{\circ n}\left(\frac{\delta}{\left|I_{\chi}\left(u_{1}, u_{2}\right)\right|+\epsilon+d_{\theta}\left(u_{1}, u_{2}\right)}\right)\right)^{-\gamma},$$
where $\chi(t)=\max \{t,-1\}$ and $h(s)=(-\tilde{\chi}(-s))^{1 / 2}$.
Proof. Without loss of generality, we can assume that
$$\frac{4 B \delta}{\epsilon+d_{\theta}\left(u_{1}, u_{2}\right)} \geq 1 .$$
Denote $\phi=P_{\theta}\left[\max \left\{u_{1}, u_{2}\right\}\right]$ and $u_{j, k}=\max \left\{u_{j}, \phi-k\right\}$ for every $k>1$ and $j=1,2$. By Theorem 3.12, Remark 3.13 and Lemma 4.7, we get
$$d_{\text {cap }}\left(u_{1, k}, u_{2, k}\right)^{2} \leq C_{1} A^{2}\left(B-\frac{\tilde{\chi}(-k) d_{\theta}\left(u_{1}, u_{2}\right)}{\delta}\right)^{2}\left(h^{\circ n}\left(\frac{\delta}{I_{\chi}\left(u_{1}, u_{2}\right)-\frac{4 B \delta}{\tilde{\chi}(-k)}+d_{\theta}\left(u_{1}, u_{2}\right)}\right)\right)^{-\gamma},$$
for every $k>1$, where $C_{1}>0$ depends only on $n, X, \omega$ and $\gamma$.
Let $k_{0}>1$ such that $\tilde{\chi}\left(-k_{0}\right)=\frac{-4 B \delta}{\epsilon+d_{\theta}\left(u_{1}, u_{2}\right)}$. We have
$$d_{\text {cap }}\left(u_{1, k_{0}}, u_{2, k_{0}}\right)^{2} \leq 25 C_{1}(A B)^{2}\left(h^{\circ(n)}\left(\frac{\delta}{I_{\chi}\left(u_{1}, u_{2}\right)+\epsilon+2 d_{\theta}\left(u_{1}, u_{2}\right)}\right)\right)^{-\gamma} .$$
On the other hand, for every $\varphi \in \operatorname{PSH}(X, \omega)$ with $0 \leq \varphi \leq 1$, we have,
$$\begin{aligned}
\left(\int_{X}\left|u_{j}-u_{j, k_{0}}\right|^{1 / 2} \omega_{\varphi}^{n}\right)^{2} & =\left(\int_{\left\{u_{j}<\phi-k_{0}\right\}}\left|u_{j}-u_{j, k_{0}}\right|^{1 / 2} \omega_{\varphi}^{n}\right)^{2} \\
& \leq \frac{1}{k_{0}}\left(\int_{\left\{u_{j}<\phi-k_{0}\right\}}\left|u_{j}\right| \omega_{\varphi}^{n}\right)^{2} \\
& \leq \frac{C_{2} A^{2}}{k_{0}},
\end{aligned}$$
for $j=1,2$, where $C_{2}>0$ depends only on $X$ and $\omega$. The last inequality holds due to the Chern-Levine-Nirenberg inequality.

Hence, by the facts $t \geq-\tilde{\chi}(-t)$ for every $t \geq 1$ and $s \leq h(s)$ for every $0<s<1$, we get
$$d_{\text {cap }}\left(u_{j}, u_{j, k_{0}}\right)^{2} \leq \frac{C_{2} A^{2}}{k_{0}} \leq \frac{C_{2} A^{2}\left(\epsilon+d_{\theta}\left(u_{1}, u_{2}\right)\right)}{4 B \delta} \leq C_{2} A^{2}\left(h^{\circ n}\left(\frac{\delta}{\epsilon+d_{\theta}\left(u_{1}, u_{2}\right)}\right)\right)^{-1} .$$

Combining (4.14) and (4.15), we obtain
$$d_{\text {cap }}\left(u_{1}, u_{2}\right)^{2} \leq C_{3}(A B)^{2}\left(h^{\circ n}\left(\frac{\delta}{\left|I_{\chi}\left(u_{1}, u_{2}\right)\right|+\epsilon+d_{\theta}\left(u_{1}, u_{2}\right)}\right)\right)^{-\gamma},$$
where $C_{3}>0$ depends only on $n, X, \omega$ and $\gamma$.
The proof is completed. \(\square\)

Now, we prove Theorem 1.2 for the case of fixed cohomology:
Theorem 4.9. Let $\theta \leq A \omega$ be a closed smooth real (1, 1)-form representing a big cohomology class ( $A \geq 1$ ). Let $u \in \operatorname{PSH}(X, \theta)$ such that $\sup _{X} u=0$ and $\int_{X} \theta_{u}^{n}:=\delta>0$. Assume $u \in \tilde{\mathcal{E}}_{\tilde{\chi}, B \delta}(X, \theta)$, where $B \geq A$ is a given constant and $\tilde{\chi} \in \mathcal{W}^{-}$with $\tilde{\chi}(-1)=-1$. Then, for every $0<\gamma<1$, there exists $C>0$ depending only on $n, X, \omega$ and $\gamma$ such that
$$d_{c a p}(u, v)^{2} \leq C(A B)^{2}\left(h^{\circ n}\left(\frac{\delta}{\left\|\theta_{u}^{n}-\theta_{v}^{n}\right\|+d_{\theta}(u, v)}\right)\right)^{-\gamma},$$
for every $v \in \operatorname{PSH}(X, \theta)$ with $\sup _{X} v=0$, where $h(s)=(-\tilde{\chi}(-s))^{1 / 2}$.
Proof. Put
$$t_{0}=\left\|\theta_{u}^{n}-\theta_{v}^{n}\right\|+d_{\theta}(u, v) .$$
Denote
$$M=\frac{5 B \delta}{t_{0}}, \quad \tilde{\chi}_{M}(s)=\max \{\tilde{\chi}(s),-M\} \quad \text { and } \quad h_{M}(s)=\left(-\tilde{\chi}_{M}(-s)\right)^{1 / 2} .$$
We have $v \in \tilde{E}_{\tilde{\chi}_{M}, B \delta+M t_{0}}(X, \theta)$ and $M t_{0}=5 B \delta$. Since inf $\tilde{\chi}_{M}=-M<\frac{-4 B \delta}{\left\|\theta_{u}^{n}-\theta_{v}^{n}\right\|+d_{\theta}(u, v)}$, it follows from Theorem 4.8 that
$$d_{\text {cap }}(u, v)^{2} \leq C_{1}(A B)^{2}\left(h_{M}^{\circ n}\left(\frac{\delta}{\left|I_{\chi}(u, v)\right|+\left\|\theta_{u}^{n}-\theta_{v}^{n}\right\|+d_{\theta}(u, v)}\right)\right)^{-\gamma},$$
where $\chi(s)=\max \{s,-1\}$ and $C_{1}>0$ depends only on $n, X, \omega$ and $\gamma$. Since $\left|I_{\chi}(u, v)\right| \leq$ $\left\|\theta_{u}^{n}-\theta_{v}^{n}\right\|$ and $B \geq 1$, it follows that
$$d_{\text {cap }}(u, v)^{2} \leq C_{2}(A B)^{2}\left(h_{M}^{\circ n}\left(\frac{\delta}{\left\|\theta_{u}^{n}-\theta_{v}^{n}\right\|+d_{\theta}(u, v)}\right)\right)^{-\gamma},$$
where $C_{2}=4 C_{1}$. By the fact $h_{M}(t)=h(t) \leq M$ for every $0<t \leq M$, we obtain
$$d_{\text {cap }}(u, v)^{2} \leq C_{2}(A B)^{2}\left(h^{\circ n}\left(\frac{\delta}{\left\|\theta_{u}^{n}-\theta_{v}^{n}\right\|+d_{\theta}(u, v)}\right)\right)^{-\gamma} .$$
The proof is completed. \(\square\)

\subsection*{4.2.2 Proof of Theorems 1.3 and 1.4}

In order to prove the next main results, we need several auxiliary lemmas.
Lemma 4.10. Let $u: B_{R+r}:=\left\{z \in \mathbb{C}^{n}:|z|<R+r\right\} \rightarrow[-\infty, 0]$ be a measurable function such that $A:=\int_{B_{R+r}} e^{-u} d V<\infty$, where $R>r>0$ and $d V$ denotes the Lebesgue measure on $\mathbb{C}^{n}$. Assume that $h$ is a non-negative smooth function on $\mathbb{C}^{n}$ satisfying $\int_{\mathbb{C}^{n}} h d V=1$ and $\operatorname{Supp}(h) \subset B_{\epsilon}$ for some $\epsilon \in(0, r)$. Then, for every $0<a<1$, there exists $C>0$ depending only on $R, n, a$ and $A$ such that
$$\left|\int_{B_{R}}(u * h-u) d V\right| \leq C \epsilon^{a} .$$
Proof. We have
$$\begin{aligned}
\left|\int_{B_{R}}(u * h-u) d V\right| & =\left|\int_{B_{R}} \int_{B_{\epsilon}} h(w)(u(z-w)-u(z)) d V_{w} d V_{z}\right| \\
& =\left|\int_{B_{\epsilon}} h(w) \int_{B_{R}}(u(z-w)-u(z)) d V_{w} d V_{z}\right| \\
& \leq \int_{B_{\epsilon}} h(w)|\hat{u}(-w)-\hat{u}(0)| d V_{w},
\end{aligned}$$
where $\hat{u}(w)=\int_{\{|\xi-w|<R\}}(-u)(\xi) d V_{\xi}$. Moreover, for every $w \in B_{\epsilon}$ and $k>0$, we have
$$\begin{aligned}
& \left|\int_{B_{R}} \max \{u(z-w), k\} d V_{z}-\int_{B_{R}} \max \{u(z), k\} d V_{z}\right| \\
& \quad=\left|\int_{B_{R}(-w)} \max \{u(z), k\} d V_{z}-\int_{B_{R}} \max \{u(z), k\} d V_{z}\right| \leq C_{n} R^{2 n-1} k|w|,
\end{aligned}$$
where $C_{n}>0$ is a constant depending only on $n$, and
$$\int_{B_{R}}|u(z-w)-\max \{u(z-w),-k\}| d V_{z} \leq \int_{\{u<-k\}}(-u-k) d V \leq \int_{B_{R+r}} e^{-u-k} d V=A e^{-k} .$$
Then
$$\left|\int_{B_{R}}(u * h-u) d V\right| \leq \int_{B_{\epsilon}} h(w)|\hat{u}(-w)-\hat{u}(0)| d V_{w} \leq C_{n} R^{2 n-1} k \epsilon+A e^{-k} .$$
Choosing $k=\epsilon^{a-1}$, we get the desired inequality. \(\square\)

Lemma 4.11. Let $(X, \omega)$ be a compact Kähler manifold and let $\mu$ be a Randon measure on $X$ such that
$$\int_{X} \min \left\{\left|u_{1}-u_{2}\right|, 1\right\} d \mu \leq H\left(\left\|u_{1}-u_{2}\right\|_{L^{1}(X)}\right),$$
for all $u_{1}, u_{2} \in \operatorname{PSH}(X, \omega)$, where $H: \mathbb{R}_{\geq 0} \rightarrow \mathbb{R}_{\geq 0}$ is an increasing function. Let $\Omega \subset X$ such that there exists a biholomorphic mapping $\varphi: 2 \mathbb{B} \rightarrow \Omega$, where $\mathbb{B}$ is the unit ball in $\mathbb{C}^{n}$. Then there exists a constant $C \geq 1$ depending only on $X, \omega, \Omega$ and $\varphi$ such that
$$\int_{\varphi(\mathbb{B})}\left|(u-v) \circ \varphi^{-1}\right| d \mu \leq C M H\left(\left\|(u-v) \circ \varphi^{-1}\right\|_{L^{1}(\varphi(2 \mathbb{B}))}\right) .$$
for every $M \geq 1$ and for all psh functions $u, v \in \operatorname{PSH}(2 \mathbb{B})$ with $-M \leq u, v \leq 0$.
Proof. Let $u^{\prime}:=\max \left\{u, M|z|^{2}-2 M\right\}$. We have $u=u^{\prime}$ on $\mathbb{B}$ and $u^{\prime}=M|z|^{2}-2 M$ outside $\sqrt{2} \mathbb{B}$. Let $\phi \in \mathscr{C}_{0}^{\infty}(2 \mathbb{B})$ such that $0 \leq \phi \leq 1$ and $\phi \equiv 1$ on $\frac{3}{2} \mathbb{B}$. Then $\tilde{u}=\left(\phi u^{\prime}\right) \circ \varphi^{-1}$ is a ( $C M \omega$ )-psh function on $X$, where $C \geq 1$ depends only on $X, \omega, \varphi$ and $\phi$. We do similarly for $v$ to obtain $\tilde{v}$. By the assumption, we get
$$\int_{X} \frac{|\tilde{u}-\tilde{v}|}{8 C M} d \mu \leq H\left(\frac{\|\tilde{u}-\tilde{v}\|_{L^{1}(X)}}{8 C M}\right) .$$
Since $\tilde{u}=\tilde{v}$ outside $\varphi(\sqrt{2} \mathbb{B})$, we have
$$\|\tilde{u}-\tilde{v}\|_{L^{1}(X)}=\|\tilde{u}-\tilde{v}\|_{L^{1}(\varphi(\sqrt{2} \mathbb{B}))} \leq\left\|(u-v) \circ \varphi^{-1}\right\|_{L^{1}(\varphi(2 \mathbb{B}))},$$
Thus, we obtain
$$\int_{\varphi(\mathbb{B})}\left|(u-v) \circ \varphi^{-1}\right| d \mu \leq \int_{X}|\tilde{u}-\tilde{v}| d \mu \leq 8 C M H\left(\left\|(u-v) \circ \varphi^{-1}\right\|_{L^{1}(\varphi(2 \mathbb{B}))}\right)$$
The proof is completed. \(\square\)

Theorem 4.12. Let $(X, \omega)$ be a compact Kähler manifold and let $\mu$ be a Randon measure on $X$ such that
$$\int_{X} \min \left\{\left|u_{1}-u_{2}\right|, 1\right\} d \mu \leq H\left(\left\|u_{1}-u_{2}\right\|_{L^{1}(X)}\right),$$
for all $u_{1}, u_{2} \in \operatorname{PSH}(X, \omega)$, where $H: \mathbb{R}_{\geq 0} \rightarrow \mathbb{R}_{\geq 0}$ is an increasing function. Assume that $\Omega$ is an open subset of $X$ and $K$ is a compact subset of $\Omega$. Then, there exists a constant $C>0$ depending only on $n, X, \omega, K$ and $\Omega$ such that
$$\int_{K} \min \{|u-v|, 1\} d \mu \leq C M H\left(\|u-v\|_{L^{1}(\Omega)}\right)+\int_{K \cap\{u<-M\}} d \mu+\int_{K \cap\{v<-M\}} d \mu$$
for all negative $\omega$-psh function $u, v$ in $\Omega$ and for every $M \geq 1$.
Proof. By using a suitable open cover of $\Omega$, we can assume that there exists a biholomorphic mapping $\varphi: 2 \mathbb{B} \rightarrow \Omega$ such that $K \subset \varphi(\mathbb{B})$. Put $u_{M}:=\max \{u,-M\}$ and $v_{M}:=\max \{v,-M\}$. We have
$$\begin{aligned}
\min \{|u-v|, 1\} & \leq\left|u_{M}-v_{M}\right|+\min \left\{\left|u-u_{M}\right|, 1\right\}+\min \left\{\left|v-v_{M}\right|, 1\right\} \\
& \leq\left|u_{M}-v_{M}\right|+\left|u_{M+1}-u_{M}\right|+\left|v_{M+1}-v_{M}\right| .
\end{aligned}$$
Then
$$\int_{K} \min \{|u-v|, 1\} d \mu \leq \int_{K}\left|u_{M}-v_{M}\right| d \mu+\int_{K}\left|u_{M+1}-u_{M}\right| d \mu+\int_{K}\left|v_{M+1}-v_{M}\right| d \mu$$
By Lemma 4.11, we have
$$\int_{K}\left|u_{M}-v_{M}\right| d \mu \leq C M H\left(\|u-v\|_{L^{1}(\Omega)}\right),$$
where $C \geq 1$ depends only on $n, X, \omega$ and $\varphi$.
Moreover
$$\int_{K}\left|u_{M+1}-u_{M}\right| d \mu \leq \int_{K \cap\{u<-M\}} d \mu$$
and
$$\int_{K}\left|v_{M+1}-v_{M}\right| d \mu \leq \int_{K \cap\{v<-M\}} d \mu$$

Therefore
$$\int_{K} \min \{|u-v|, 1\} d \mu \leq C M H\left(\|u-v\|_{L^{1}(\Omega)}\right)+\int_{K \cap\{u<-M\}} d \mu+\int_{K \cap\{v<-M\}} d \mu$$

This finishes the proof. \(\square\)

The following result can be considered as a generalization of Theorems 1.3 and 1.4 for the case of fixed cohomology:

Theorem 4.13. Let $\theta$ be a closed smooth real (1, 1)-form such that $\theta \leq A \omega$ for a given constant $A \geq 1$. Let $0<\delta \leq 1, B \geq A, \tilde{\chi} \in \mathcal{W}^{-}$and $u_{1}, u_{2} \in \tilde{\mathcal{E}}_{\tilde{\chi}, B \delta}(X, \theta)$ such that $\tilde{\chi}(-1)=-1$, $\sup _{X} u_{1}=\sup _{X} u_{2}=0$ and $\int_{X} \theta_{u_{1}}^{n}+\int_{X} \theta_{u_{2}}^{n} \geq 2 \delta$. Assume that there exists a concave increasing function $H: \mathbb{R}_{\geq 0} \rightarrow \mathbb{R}_{\geq 0}$ such that, for $j=1,2$,
$$\int_{X} \min \left\{\left|\psi_{1}-\psi_{2}\right|, 1\right\} \theta_{u_{j}}^{n} \leq H\left(\left\|\psi_{1}-\psi_{2}\right\|_{L^{1}(X)}\right),$$
for every $\psi_{1}, \psi_{2} \in \operatorname{PSH}(X, \omega)$. Then, for every $0<a, b, \gamma<1$ and $m>0$, there exists $C>0$ depending only on $n, X, \omega, H(1), a, b, \gamma$ and $m$ such that
$$d_{\text {cap }}\left(u_{1}, u_{2}\right)^{2} \leq C(A B)^{2}\left(h^{\circ n}\left(\frac{\delta}{A G(x)+d_{\theta}\left(u_{1}, u_{2}\right)}\right)\right)^{-\gamma},$$
where
$$x:=\operatorname{dist}_{-1}\left(\theta_{u_{1}}^{n}, \theta_{u_{2}}^{n}\right), \quad G(x)=A^{2} H^{a}\left(A x^{a(1-b)}\right)+H\left(H^{m}\left(x^{1-b}\right)\right)+x^{a b},$$
and $h(s)=(-\tilde{\chi}(-s))^{1 / 2}$.
Proof. Without loss of generality, we can assume that $0<x:=\operatorname{dist}_{-1}\left(\theta_{u_{1}}^{n}, \theta_{u_{2}}^{n}\right)<1$. Denote $\chi(t)=\max \{t,-1\}$. Since $\inf \tilde{\chi}=-\infty$, it follows from Theorem 4.8 that
$$d_{\text {cap }}\left(u_{1}, u_{2}\right)^{2} \leq C_{0}(A B)^{2}\left(h^{\circ n}\left(\frac{\delta}{\left|I_{\chi}\left(u_{1}, u_{2}\right)\right|+d_{\theta}\left(u_{1}, u_{2}\right)}\right)\right)^{-\gamma},$$
where $C_{0}>0$ depends only on $n, X, \omega$ and $\gamma$. We will estimate $\left|I_{\chi}\left(u_{1}, u_{2}\right)\right|$.
For every $k>0$ and $j=1,2$, it follows from the Skoda integrability theorem that
$$\int_{\left\{u_{j}<-k\right\}} \omega^{n} \leq \int_{X} \exp \left(\frac{-c_{0}\left(u_{j}+k\right)}{A}\right) \omega^{n} \leq C_{1} \exp \left(\frac{-c_{0} k}{A}\right),$$
where $c_{0}, C_{1}>0$ depend only on $X$ and $\omega$. For every $k>0$ and for each $0<\epsilon<1$, by using the standard convolution and a partition of unit, we can find a smooth function $u_{j, k, \epsilon}$ such that $\max \left\{u_{j},-k\right\}-\epsilon \leq u_{j, k, \epsilon} \leq 0$ and
$$\left\|u_{j, k, \epsilon}\right\|_{C^{1}(X)} \leq \frac{C_{2} k}{\epsilon},$$
and
$$\left\|u_{j, k, \epsilon}-\max \left\{u_{j},-k\right\}\right\|_{L^{1}(X)} \leq C_{3} A \epsilon^{a},$$
where $0<a<1, C_{2}=C_{2}(X, \omega)>0$ and $C_{3}=C_{3}(X, \omega, a)>0$. Here, the last inequality holds due to Lemma 4.10. Moreover, there exists a finite open cover $\left\{U_{l}\right\}$ of $X$ such that $u_{j, k, \epsilon}$ is $(A+1) \omega$-psh on $U_{l}$ for every $l$. It follows from Theorem 4.12 that
$$\begin{aligned}
\int_{X} \min \left\{\left|u_{j}-u_{j, k, \epsilon}\right|, 2\right\} d \mu & \leq \int_{X} \min \left\{\left|\max \left\{u_{j},-k-3\right\}-u_{j, k, \epsilon}\right|, 2\right\} d \mu \\
& \leq C_{4} A M H\left(\left\|\max \left\{u_{j},-k-3\right\}-u_{j, k, \epsilon}\right\|_{L^{1}(X)}\right)+4 \int_{\left\{u_{j}, u_{j, k, \epsilon}<-M\right\}} d \mu \\
& \leq C_{4} A M H\left(\left\|\max \left\{u_{j},-k-3\right\}-u_{j, k, \epsilon}\right\|_{L^{1}(X)}\right)+4 \int_{\left\{u_{j}<-M+1\right\}} d \mu
\end{aligned}$$
for every $k, M \geq 1, j=1,2$ and $0<\epsilon<1$, where $\mu=\theta_{u_{1}}^{n}+\theta_{u_{2}}^{n}$ and $C_{4}>0$ is a constant depending only on $n, X$ and $\omega$. Therefore, by (4.18) and (4.20), we have
$$\int_{X} \min \left\{\left|u_{j}-u_{j, k, \epsilon}\right|, 2\right\} d \mu \leq C_{5} A M H\left(A \epsilon^{a}+\exp \left(\frac{-c_{0} k}{A}\right)\right)+4 \int_{\left\{u_{j}<-M+1\right\}} d \mu$$
where $C_{5}>0$ depends on $n, X, \omega$ and $a$. Using the fact $\mathbf{1}_{\left\{u_{j}<-M+1\right\}} \leq \mid \max \left\{u_{j},-M+1\right\}-$ $\max \left\{u_{j},-M+2\right\} \mid \leq \mathbf{1}_{\left\{u_{j}<-M+2\right\}}$, we have
$$\int_{\left\{u_{j}<-M+1\right\}} d \mu \leq \int_{X}\left|\max \left\{u_{j},-M+1\right\}-\max \left\{u_{j},-M+2\right\}\right| d \mu \leq 2 A H\left(\int_{\left\{u_{j}<-M+2\right\}} \omega^{n}\right)$$
Then, by (4.18), we get
$$\int_{\left\{u_{j}<-M+1\right\}} d \mu \leq C_{6} A H\left(\exp \left(\frac{-c_{0} M}{A}\right)\right),$$
where $C_{6}>0$ depends only on $X$ and $\omega$. Combining (4.21) and (4.22), we get
$$\int_{X} \min \left\{\left|u_{j}-u_{j, k, \epsilon}\right|, 2\right\} d \mu \leq C_{5} A M H\left(A \epsilon^{a}+\exp \left(\frac{-c_{0} k}{A}\right)\right)+C_{6} A H\left(\exp \left(\frac{-c_{0} M}{A}\right)\right)$$
Recall that
$$\begin{aligned}
I_{\chi}\left(u_{1}, u_{2}\right) & =\int_{\left\{u_{1}<u_{2}\right\}} \min \left\{\left|u_{1}-u_{2}\right|, 1\right\}\left(\theta_{u_{1}}^{n}-\theta_{u_{2}}^{n}\right)+\int_{\left\{u_{2}<u_{1}\right\}} \min \left\{\left|u_{1}-u_{2}\right|, 1\right\}\left(\theta_{u_{2}}^{n}-\theta_{u_{1}}^{n}\right) \\
& =\int_{X} \max \left\{\min \left\{u_{2}-u_{1}, 1\right\},-1\right\}\left(\theta_{u_{1}}^{n}-\theta_{u_{2}}^{n}\right) .
\end{aligned}$$

By the fact that
$$\max \left\{t_{1}, t_{3}\right\}-\max \left\{t_{2}, t_{3}\right\}=\min \left\{-t_{2},-t_{3}\right\}-\min \left\{-t_{1},-t_{3}\right\} \leq \max \left\{t_{1}-t_{2}, 0\right\},$$
we have
$$\left|\max \left\{\min \left\{u_{2}-u_{1}, 1\right\},-1\right\}-\max \left\{\min \left\{u_{2, k, \epsilon}-u_{1, k, \epsilon}, 1\right\},-1\right\}\right| \leq\left|u_{2}-u_{1}-u_{2, k, \epsilon}+u_{1, k, \epsilon}\right|,$$
for every $k>0$ and $0<\epsilon<1$. Since the LHS of the last inequality is bounded by 2 , it follows that
$$\left|\max \left\{\min \left\{u_{2}-u_{1}, 1\right\},-1\right\}-\max \left\{\min \left\{u_{2, k, \epsilon}-u_{1, k, \epsilon}, 1\right\},-1\right\}\right| \leq \Psi_{k, \epsilon},$$
where
$$\Psi_{k, \epsilon}=\min \left\{\left|u_{2}-u_{1}-u_{2, k, \epsilon}+u_{1, k, \epsilon}\right|, 2\right\} .$$
Therefore
$$\left|I_{\chi}\left(u_{1}, u_{2}\right)\right| \leq\left|\int_{X} \Phi_{k, \epsilon}\left(\theta_{u_{1}}^{n}-\theta_{u_{2}}^{n}\right)\right|+\int_{X} \Psi_{k, \epsilon}\left(\theta_{u_{1}}^{n}+\theta_{u_{2}}^{n}\right),$$
where $\Phi_{k, \epsilon}=\max \left\{\min \left\{u_{2, k, \epsilon}-u_{1, k, \epsilon}, 1\right\},-1\right\}$. By (4.19), we have
$$\left|\int_{X} \Phi_{k, \epsilon}\left(\theta_{u_{1}}^{n}-\theta_{u_{2}}^{n}\right)\right| \leq \frac{C_{2} k}{\epsilon} \operatorname{dist}_{-1}\left(\theta_{u_{1}}^{n}, \theta_{u_{2}}^{n}\right) .$$
Combining (4.23), (4.24), (4.25), and choosing $\epsilon=x^{1-b}, M=-\frac{A m \log (H(\epsilon) / H(1))}{c_{0}}$, $k=-\frac{A \log \epsilon}{c_{0}}$, we get
$$\left|I_{\chi}\left(u_{1}, u_{2}\right)\right| \leq C_{7} A\left(A^{2} H^{a}\left(A x^{a(1-b)}\right)+H\left(H^{m}\left(x^{1-b}\right)\right)+x^{a b}\right),$$
where $C_{7}>1$ depends only on $n, X, \omega, a, b, m$ and $H(1)$. Combining (4.17) and (4.26), we obtain the desired inequality.

The proof is completed. \(\square\)

\subsection*{4.3 Application to the space of singularity types}

In this part we apply quantitative stability theorems in the previous subsection to deduce some properties of the pseudometric space of singularity types in a big cohomology class.

Proposition 4.14. Let $\theta \leq A \omega$ be a closed smooth real (1,1)-form representing a big cohomology class $(A \geq 1)$. Assume that $u_{1}$ and $u_{2}$ are model $\theta$-psh functions such that $\int_{X} \theta_{u_{1}}^{n}+$ $\int_{X} \theta_{u_{2}}^{n} \geq 2 \delta>0$, where $\delta>0$ is a constant. Then, for every $0<\gamma<1$, there exists $C>0$ depending only on $n, X, \omega$ and $\gamma$ such that
$$d_{\text {cap }}\left(u_{1}, u_{2}\right)^{2} \leq C \frac{A^{2 n+4}}{\delta^{2}}\left(\frac{d_{\theta}\left(u_{1}, u_{2}\right)}{\delta}\right)^{2^{-n} \gamma} .$$

The above result implies in particular that for model potentials, the convergence in $d_{\mathcal{S}}$ is stronger than that in capacity. The last non-quantitative fact follows also from [18, Theorem 5.6].

Proof. By [16, Theorem 3.8], we have
$$\theta_{u_{j}}^{n} \leq \mathbf{1}_{\left\{u_{j}=0\right\}} \theta^{n} \leq A^{n} \omega^{n},$$
for $j=1,2$. Therefore, there exists $C_{1}>0$ depending only on $X$ and $\omega$ such that
$$\int_{X}(-\psi) \theta_{u_{j}}^{n} \leq C_{1} A^{n+1},$$
for every $\psi \in \operatorname{PSH}(X, \theta) \subset \operatorname{PSH}(X, A \omega)$ with $\sup _{X} \psi=0$. Using Theorem 4.8 for $\tilde{\chi}(t)=t$, we get
$$d_{\text {cap }}\left(u_{1}, u_{2}\right)^{2} \leq C_{2}\left(A \frac{C_{1} A^{n+1}}{\delta}\right)^{2}\left(\frac{\left|I_{\chi}\left(u_{1}, u_{2}\right)\right|+d_{\theta}\left(u_{1}, u_{2}\right)}{\delta}\right)^{2^{-n} \gamma},$$
where $\chi(t)=\max \{t,-1\}$ and $C_{2}>0$ is a constant depending only on $n, X, \omega$ and $\gamma$. Since $\theta_{u_{j}}^{n} \leq \mathbf{1}_{\left\{u_{j}=0\right\}} \theta^{n}$, we have
$$\int_{\left\{u_{1}<u_{2}\right\}}-\chi\left(u_{1}-u_{2}\right) \theta_{u_{1}}^{n}=\int_{\left\{u_{2}<u_{1}\right\}}-\chi\left(u_{2}-u_{1}\right) \theta_{u_{2}}^{n}=0 .$$
Therefore
$$I_{\chi}\left(u_{1}, u_{2}\right) \leq 0 .$$
Moreover, it follows from Lemma 4.7 that
$$I_{\chi}\left(u_{1}, u_{2}\right) \geq-d_{\theta}\left(u_{1}, u_{2}\right) .$$
Combining (4.27), (4.28) and (4.29), we obtain
$$d_{\text {cap }}\left(u_{1}, u_{2}\right)^{2} \leq C_{3} \frac{A^{2 n+4}}{\delta^{2}}\left(\frac{d_{\theta}\left(u_{1}, u_{2}\right)}{\delta}\right)^{2^{-n} \gamma},$$
where $C_{3}>0$ depends only on $n, X, \omega$ and $\gamma$. The proof is completed. \(\square\)

By using Proposition 4.14, we recover the following result which is obtained in [18] (with a different proof).

Proposition 4.15. Let $\delta>0$ be a constant. Let $\mathcal{S}_{\delta}(\theta)$ be the subset of $\mathcal{S}(\theta)$ consisting of $[u] \in \mathcal{S}_{\theta}$ such that $\int_{X} \theta_{u}^{n} \geq \delta$. Then $\left(\mathcal{S}_{\delta}(\theta), d_{\mathcal{S}}\right)$ is a complete (pseudo)-metric space.

Proof. Let $\left(\left[u_{j}\right]\right)_{j}$ be a Cauchy sequence in $\mathcal{S}_{\delta}(\theta)$ (recall $\left[u_{j}\right]$ denotes the singularity type of a $\theta$-psh function $u_{j}$ with $\sup _{X} u_{j}=0$ ), i.e, for every constant $\epsilon>0$, there exists $k_{\epsilon} \in \mathbb{N}$ such that $d_{\theta}\left(u_{j}, u_{k}\right) \leq \epsilon$ for every $j \geq k_{\epsilon}$, and $k \geq k_{\epsilon}$. We need to prove that there exists a class
$\left[u_{\infty}\right] \in \mathcal{S}_{\delta}(\theta)$ so that $d_{\theta}\left(u_{j}, u_{\infty}\right) \rightarrow 0$ as $j \rightarrow \infty$. By using contradiction, it suffices to prove it for some subsequence of $\left(u_{j}\right)_{j}$. Hence we can assume safely that
$$d_{\theta}\left(u_{j}, u_{j+1}\right) \leq 4^{-n 2^{n+1}},$$
because one can always extract a subsequence of $\left(u_{j}\right)_{j}$ with that property.
Since $d_{\theta}\left(u, P_{\theta}[u]\right)=0$ for every $u \in \operatorname{PSH}(X, \theta)$, without loss of generality, we can assume that $u_{j}=P_{\theta}\left[u_{j}\right]$ for every $j \in \mathbb{N}$, in other words, $u_{j}$ 's are model $\theta$-psh functions. Consequently, by Proposition 4.14 (with $\gamma=1 / 2$ ), we get
$$d_{\text {cap }}\left(u_{j}, u_{j+1}\right) \leq 2^{-n} C_{1},$$
for every $j$, where $C_{1}>0$ is a constant depending only on $n, X, \omega, \theta$ and $\delta$. Therefore, there exists a $\theta$-psh function $u_{\infty}$ such that $u_{j}$ converges to $u_{\infty}$ in capacity as $j \rightarrow \infty$.

Moreover, it follows from [16, Theorem 3.8] that
$$\theta_{u_{j}}^{n} \leq \mathbf{1}_{\left\{u_{j}=0\right\}} \theta^{n} \leq C_{2} \omega^{n},$$
for some constant $C_{2}>0$ independent of $j$. This coupled with Lemma 4.16 below yields that
$$\theta_{u_{j}}^{n} \rightarrow \theta_{u_{\infty}}^{n},$$
as $j \rightarrow \infty$. It is clear that $\int_{X} \theta_{u_{\infty}}^{n} \geq \delta$. It remains to show that $d_{\theta}\left(u_{j}, u_{\infty}\right) \rightarrow 0$ as $j \rightarrow \infty$.
Since
$$d_{\theta}\left(u_{j}, u_{k}\right)=2 \int_{X} \theta_{\max \left\{u_{j}, u_{k}\right\}}^{n}-\int_{X} \theta_{u_{j}}^{n}-\int_{X} \theta_{u_{k}}^{n},$$
using (4.31) and the fact that $\max \left\{u_{j}, u_{k}\right\} \rightarrow \max \left\{u_{j}, u_{\infty}\right\}$ in capacity as $k \rightarrow \infty$ (for $u_{k} \rightarrow u_{\infty}$ in capacity), one gets
$$\liminf _{k \rightarrow \infty} d_{\theta}\left(u_{j}, u_{k}\right) \geq 2 \int_{X} \theta_{\max \left\{u_{j}, u_{\infty}\right\}}^{n}-\int_{X} \theta_{u_{j}}^{n}-\int_{X} \theta_{u_{\infty}}^{n}=d_{\theta}\left(u_{j}, u_{\infty}\right) .$$
It follows that $d_{\theta}\left(u_{j}, u_{\infty}\right) \rightarrow 0$ as $j \rightarrow \infty$. In other words, $\left[u_{j}\right] \rightarrow\left[u_{\infty}\right]$ in the topology induced by the pseudo-metric $d_{\mathcal{S}}$ (we note that $\left[u_{\infty}\right]$ might not be unique, but the singularity type of its envelope $P_{\theta}\left[u_{\infty}\right]$ is unique). \(\square\)

The following lemma is probably known. We present a proof for readers' convenience.
Lemma 4.16. Let $\Omega$ be an open subset in $\mathbb{C}^{n}$. Let $\left(u_{j}\right)_{j}$ be a sequence of psh functions converging to a psh function $u_{\infty}$ in capacity in $\Omega$. Assume that the non-pluripolar product $\left(d d^{c} u_{j}\right)^{n}$ is well-defined for $1 \leq j \leq \infty$, and there exists a non-pluripolar Radon measure $\mu$ on $\Omega$ such that $\left(d d^{c} u_{j}\right)^{n} \leq \mu$ for every $j$. Then $\left(d d^{c} u_{j}\right)^{n}$ converges weakly to $\left(d d^{c} u_{\infty}\right)^{n}$ as $j \rightarrow \infty$.

Proof. Let $\nu$ be a limit measure of the sequence $\left(\left(d d^{c} u_{j}\right)^{n}\right)_{j}$ as $j \rightarrow \infty$. We need to check that $\nu=\left(d d^{c} u_{\infty}\right)^{n}$. Observe that $\nu \geq\left(d d^{c} u_{\infty}\right)^{n}$ because $u_{j} \rightarrow u_{\infty}$ in capacity. It remains to verify the converse inequality.

Let $g \geq 0$ be a smooth function with compact support in $\Omega$. Put $u_{j k}:=\max \left\{u_{j},-k\right\}$ for $1 \leq j \leq \infty$. We get $u_{j k} \rightarrow u_{\infty k}$ in the capacity as $j \rightarrow \infty$. It follows that $\left(d d^{c} u_{j k}\right)^{n} \rightarrow$ $\left(d d^{c} u_{\infty k}\right)^{n}$ as $j \rightarrow \infty$, and
$$\limsup _{j \rightarrow \infty} \int_{\Omega} g \mathbf{1}_{\left\{u_{j} \geq-k+1\right\}}\left(d d^{c} u_{j k}\right)^{n} \leq \int_{\Omega} g \mathbf{1}_{\left\{u_{\infty} \geq-k+1\right\}}\left(d d^{c} u_{\infty k}\right)^{n} .$$
By this and the equality $\mathbf{1}_{\left\{u_{j}>-k\right\}}\left(d d^{c} u_{j k}\right)^{n}=\left(d d^{c} u_{j}\right)^{n}$, we get
$$\limsup _{j \rightarrow \infty} \int_{\Omega} g \mathbf{1}_{\left\{u_{j}>-k+1\right\}}\left(d d^{c} u_{j}\right)^{n} \leq \int_{\Omega} g \mathbf{1}_{\left\{u_{\infty}>-k\right\}}\left(d d^{c} u_{\infty k}\right)^{n}=\int_{\Omega} g \mathbf{1}_{\left\{u_{\infty}>-k\right\}}\left(d d^{c} u_{\infty}\right)^{n}$$
which converges to 0 as $k \rightarrow \infty$. On the other hand, by hypothesis, one gets
$$\mathbf{1}_{\left\{u_{j}<-k\right\}}\left(d d^{c} u_{j}\right)^{n} \leq \mathbf{1}_{\left\{u_{j}<-k\right\}} \mu \leq \mathbf{1}_{\{u<-k\}} \mu+\mathbf{1}_{\left\{u_{j}-u \leq 1\right\}} \mu .$$
Combining this with [34, Lemma 4.5] (we use here the fact that $\mu$ is non-pluripolar) gives
$$\limsup _{j \rightarrow \infty} \int_{\Omega} g \mathbf{1}_{\left\{u_{j}<-k\right\}}\left(d d^{c} u_{j}\right)^{n} \leq \int_{\Omega} g \mathbf{1}_{\{u<-k\}} \mu$$
Letting $k \rightarrow \infty$, we obtain
$$\limsup _{j \rightarrow \infty} \int_{\Omega} g \mathbf{1}_{\left\{u_{j}<-k\right\}}\left(d d^{c} u_{j}\right)^{n} \rightarrow 0$$
as $k \rightarrow \infty$. Combining the last inequality with (4.32) yields
$$\limsup _{j \rightarrow \infty} \int_{\Omega} g\left(d d^{c} u_{j}\right)^{n} \leq \int_{\Omega} g\left(d d^{c} u_{\infty}\right)^{n} .$$
Hence $\left(d d^{c} u_{j}\right)^{n} \rightarrow d d^{c} u_{\infty}$ as $j \rightarrow \infty$. This finishes the proof. \(\square\)

\subsection*{4.4 The case of varied cohomology}

We now present the proof of Theorem 1.2.
End of the proof of Theorem 1.2 Put $\epsilon=\|\theta-\eta\|_{\mathscr{C}^{0}}$. Then, there exists $C_{1} \geq 1$ depending only on $X$ and $\omega$ such that
$$\theta \leq \eta+C_{1} \epsilon \omega \leq \theta+2 C_{1} \epsilon \omega .$$
Note that, by Chern-Levine-Nirenberg inequality and by the compactness of $\{w \in \operatorname{PSH}(X, \omega)$ : $\left.\sup _{X} w=0\right\}$ in $L^{1}(X)$, there exists $C_{\omega}>0$ depending only on $X$ and $\omega$ such that
$$d_{\text {cap }}(u, v)^{2} \leq C_{\omega} A .$$

Therefore, if $0<\frac{\delta}{2 C_{1}} \leq \epsilon$ then the desired inequality (1.7) holds. Hence, without loss of generality, we can assume that
$$\epsilon<\frac{\delta}{2 C_{1}},$$
and, as a consequence, we have $\tilde{\theta}:=\theta+C_{1} \epsilon \omega \leq(A+1) \omega$.
It follows from [17, Theorem 4.7] that there exists a unique $\tilde{u} \in \mathcal{E}\left(X, \tilde{\theta}, P_{\tilde{\theta}}[u]\right)$ such that
$$\left\{\begin{array}{l}
\tilde{\theta}_{\widetilde{u}}^{n}=c \theta_{u}^{n}, \\
\sup _{X} \tilde{u}=0,
\end{array}\right.$$
where $c=\frac{\int_{X} \tilde{\theta}_{u}^{n}}{\int_{X} \theta_{u}^{n}} \geq 1$. Observe that $\int_{X} \tilde{\theta}_{\tilde{u}}^{n} \geq c \delta$ and $\tilde{u} \in \tilde{E}_{\tilde{\chi}, B c \delta}(X, \tilde{\theta})$. It follows from Theorem 4.9 that
$$d_{\text {cap }}(\tilde{u}, u)^{2} \leq C_{2}(A+1)^{2} B^{2}\left(h^{\circ n}\left(\frac{\delta}{\left\|\tilde{\theta}_{\tilde{u}}^{n}-\tilde{\theta}_{u}^{n}\right\|+d_{\tilde{\theta}}(\tilde{u}, u)}\right)\right)^{-\gamma},$$
and
$$d_{\text {cap }}(\tilde{u}, v)^{2} \leq C_{2}(A+1)^{2} B^{2}\left(h^{\circ n}\left(\frac{\delta}{\left\|\tilde{\theta}_{\tilde{u}}^{n}-\tilde{\theta}_{v}^{n}\right\|+d_{\tilde{\theta}}(\tilde{u}, v)}\right)\right)^{-\gamma},$$
where $C_{2}>0$ depends only on $n, X, \omega$ and $\gamma$. Since $P_{\tilde{\theta}}[u]=P_{\tilde{\theta}}[\tilde{u}]$, we have
$$d_{\tilde{\theta}}(\tilde{u}, u)=0 \quad \text { and } \quad d_{\tilde{\theta}}(\tilde{u}, v)=d_{\tilde{\theta}}(u, v) \text {. }$$
Combining (4.35), (4.36) and (4.37), we get
$$d_{\text {cap }}(u, v)^{2} \leq C_{3}(A B)^{2}\left(h^{\circ n}\left(\frac{\delta}{\left\|\tilde{\theta}_{\tilde{u}}^{n}-\tilde{\theta}_{u}^{n}\right\|+\left\|\tilde{\theta}_{\tilde{u}}^{n}-\tilde{\theta}_{v}^{n}\right\|+d_{\tilde{\theta}}(u, v)}\right)\right)^{-\gamma},$$
where $C_{3}>0$ depends only on $n, X, \omega$ and $\gamma$. By (4.33), we have
$$\theta_{u}^{n} \leq \tilde{\theta}_{u}^{n} \leq \theta_{u}^{n}+C_{4} \epsilon\left(\theta_{u}+\omega\right)^{n},$$
and
$$\eta_{v}^{n} \leq \tilde{\theta}_{v}^{n} \leq\left(\eta_{v}+2 C_{1} \epsilon \omega\right)^{n} \leq \eta_{v}^{n}+C_{4} \epsilon\left(\eta_{v}+\omega\right)^{n},$$
where $C_{4}>0$ depends only on $X$ and $\omega$. Therefore
$$\left\|\theta_{u}^{n}-\tilde{\theta}_{u}^{n}\right\|+\left\|\eta_{v}^{n}-\tilde{\theta}_{v}^{n}\right\| \leq C_{5}(A+1)^{n} \operatorname{vol}(X) \epsilon,$$
where $C_{5}>0$ depends only on $X$ and $\omega$. Moreover,
$$\left\|\theta_{u}^{n}-\tilde{\theta}_{\tilde{u}}^{n}\right\|=(c-1) \int_{X} \theta_{u}^{n}=\int_{X}\left(\tilde{\theta}_{u}^{n}-\theta_{u}^{n}\right) \leq\left\|\theta_{u}^{n}-\tilde{\theta}_{u}^{n}\right\| .$$

Combining (4.39) and (4.40), we get
$$\begin{aligned}
\left\|\tilde{\theta}_{\tilde{u}}^{n}-\tilde{\theta}_{u}^{n}\right\|+\left\|\tilde{\theta}_{\tilde{u}}^{n}-\tilde{\theta}_{v}^{n}\right\| & \leq\left\|\theta_{u}^{n}-\tilde{\theta}_{u}^{n}\right\|+2\left\|\theta_{u}^{n}-\tilde{\theta}_{\tilde{u}}^{n}\right\|+\left\|\theta_{u}^{n}-\eta_{v}^{n}\right\|+\left\|\eta_{v}^{n}-\tilde{\theta}_{v}^{n}\right\| \\
& \leq 3\left\|\theta_{u}^{n}-\tilde{\theta}_{u}^{n}\right\|+\left\|\eta_{v}^{n}-\tilde{\theta}_{v}^{n}\right\|+\left\|\theta_{u}^{n}-\eta_{v}^{n}\right\| \\
& \leq 3 C_{5}(A+1)^{n} \operatorname{vol}(X) \epsilon+\left\|\theta_{u}^{n}-\eta_{v}^{n}\right\| .
\end{aligned}$$
Hence, by (4.38), we obtain
$$\begin{aligned}
d_{\text {cap }}(u, v)^{2} & \leq C_{3}(A B)^{2}\left(h^{\circ n}\left(\frac{\delta}{3 C_{5}(A+1)^{n} \operatorname{vol}(X) \epsilon+\left\|\theta_{u}^{n}-\eta_{v}^{n}\right\|+d_{\tilde{\theta}}(u, v)}\right)\right)^{-\gamma} \\
& \leq C_{6}(A B)^{2}\left(h^{\circ n}\left(\frac{\delta}{A^{n} \epsilon+\left\|\theta_{u}^{n}-\eta_{v}^{n}\right\|+d_{(A+1) \omega}(u, v)}\right)\right)^{-\gamma},
\end{aligned}$$
where $C_{6}>0$ depends only on $n, X, \omega$ and $\gamma$. Here we use the facts $d_{\tilde{\theta}}(u, v) \leq d_{(A+1) \omega}(u, v)$ (see Lemma 4.1) and $h(t) \leq h(M t) \leq M h(t)$ for every $M \geq 1$ and $t>0$. The proof is completed. \(\square\)

We give here a consequence of Theorem 1.2.
Theorem 4.17. Let $\left(\theta_{j}\right)_{j \in \mathbb{N} \cup\{\infty\}}$ be a sequence of closed smooth real (1, 1)-forms in $X$ such that $\theta_{j} \rightarrow \theta_{\infty}$ in $\mathscr{C}^{0}$ topology as $j \rightarrow \infty$. Let $\phi_{j}$ be a model $\theta_{j}$-psh function for $j \in \mathbb{N} \cup\{\infty\}$ such that
$$d_{\mathcal{S}}\left(\phi_{j}, \phi_{\infty}\right) \rightarrow 0$$
as $j \rightarrow \infty$. Let $\mu_{j}$ be a non-pluripolar measure on $X$ such that
$$\mu_{j}(X)=\int_{X}\left(d d^{c} \phi_{j}+\theta_{j}\right)^{n}$$
for every $j$ and $\mu_{j} \rightarrow \mu_{\infty}$ in the mass norm. Let $u_{j}$ be the $\theta$-psh function satisfying
$$\left(d d^{c} u_{j}+\theta_{j}\right)^{n}=\mu_{j}, \quad \sup _{X}\left(u_{j}-\phi_{j}\right)=0$$
for $j \in \mathbb{N} \cup\{\infty\}$. Then $u_{j} \rightarrow u_{\infty}$ in capacity as $j \rightarrow \infty$.
Here by $d_{S}\left(\phi_{j}, \phi_{\infty}\right)$ we mean the pseudodistance $d_{\mathcal{S}(A \omega)}$ between the ( $A \omega$ )-singularity types of $\phi_{j}$ and $\phi_{\infty}$, where $A>0$ is a big enough constant such that $\theta_{j} \leq A \omega$ for every $j$. The property $d_{\mathcal{S}}\left(\phi_{j}, \phi_{\infty}\right) \rightarrow 0$ is independent of the choice of $A$. Moreover, as mentioned above when $\theta_{j}$ is equal to a fixed $\theta$, the pseudometric $d_{\mathcal{S}(A \omega)}$ is comparable with $d_{\mathcal{S}(\theta)}$.

Proof. Since $\theta_{j} \rightarrow \theta_{\infty}$ in $\mathscr{C}^{0}$-norm, there exists a constant $A \geq 1$ so that $\theta_{j} \leq A \omega$ for every $j \in \mathbb{N} \cup\{\infty\}$. By [8, Proposition 3.2], there exists $\tilde{\chi} \in \mathcal{W}^{-}$such that
$$\sup _{\psi \in \operatorname{PSH}(X,(A+1) \omega): \sup _{X} \psi=0} \int_{X}-\tilde{\chi}(\psi) d \mu_{\infty}<\infty .$$
By considering $\tilde{\chi} /|\tilde{\chi}(-1)|$ instead of $\tilde{\chi}$, we can assume that $\tilde{\chi}(-1)=-1$. This allows us to apply Theorem 1.2 to $u:=u_{\infty}, v:=u_{j}, \theta:=\theta_{\infty}$, and $\eta:=\theta_{j}$, and we note that
$$d_{(A+1) \omega}(u, v)=d_{(A+1) \omega}\left(u_{j}, u_{\infty}\right)=d_{(A+1) \omega}\left(\phi_{j}, \phi_{\infty}\right) \rightarrow 0$$
as $j \rightarrow \infty$ by the hypothesis. We thus obtain $d_{\text {cap }}\left(u_{j}, u_{\infty}\right) \rightarrow 0$ as $j \rightarrow \infty$. The desired convergence hence follows. The proof is finished. \(\square\)

Theorem 4.17 considerably extends [35, Proposition A] (which treats the case where the cohomology class is fixed, $\left(\phi_{j}\right)_{j}$ is constant and of minimal singularity types, and only the convergence in $L^{1}$ was obtained) and [18, Theorem 1.4] which treats the case where again the cohomology class is fixed, and $\mu_{j}$ has $L^{p}$ density with respect to $\omega^{n}$; see also [22, Theorem 2.14] for a particular version of Theorem 4.17. The assumption that $\mu_{j}$ has $L^{p}$ density is crucial in the plurisubharmonic envelope approach in [18, Theorem 1.4]. We note furthermore that in [63, 61] the convergence of solutions were also obtained under more restrictive conditions that the sequence of measures $\left(\mu_{j}\right)_{j}$ are of uniformly bounded $E^{1}$ energy (i.e, the corresponding solutions $\left(u_{j}\right)_{j}$ are of uniformly bounded $\chi$-energy for $\chi(t)=t$, see below for the definition) and the sequence of prescribed singularities is totally ordered.

It is well-known that it is not possible to have $u_{j} \rightarrow u_{\infty}$ in $L^{1}$ if $\mu_{j}$ only converges weakly to $\mu_{\infty}$ in general (see [10, 35] and references therein for examples).

In the sequel, we will proceed to prove Theorems 1.3 and 1.4.
Theorem 4.18. Let $\theta_{1}, \theta_{2} \leq A \omega$ be closed smooth real (1, 1)-forms $(A \geq 1)$. Let $0<\delta \leq 1$, $B \geq 1, \tilde{\chi} \in \mathcal{W}^{-}$and $u_{j} \in \tilde{\mathcal{E}}_{\tilde{\chi},(A+1) \omega, B \delta}\left(X, \theta_{j}\right)(j=1,2)$ such that $\tilde{\chi}(-1)=-1, \sup _{X} u_{j}=0$ and $\int_{X} \theta_{u_{j}}^{n} \geq \delta$. Assume that there exists a concave increasing function $H: \mathbb{R}_{\geq 0} \rightarrow \mathbb{R}_{\geq 0}$ such that, for $j=1,2$,
$$\int_{X} \min \left\{\left|\psi_{1}-\psi_{2}\right|, 1\right\}\left(\theta_{j}+d d^{c} u_{j}\right)^{n} \leq H\left(\left\|\psi_{1}-\psi_{2}\right\|_{L^{1}(X)}\right),$$
for every $\psi_{1}, \psi_{2} \in \operatorname{PSH}(X, \omega)$. Then, for every $0<a, b, \gamma<1$ and $m>0$, there exists $C>0$ depending only on $n, X, \omega, H(1), a, b, \gamma$ and $m$ such that
$$d_{c a p}\left(u_{1}, u_{2}\right)^{2} \leq C(A B)^{2}\left(h^{\circ n}\left(\frac{\delta}{A G(\tau)+A^{n}\left\|\theta_{1}-\theta_{2}\right\|_{\mathscr{C}^{0}}+d_{(A+1) \omega}\left(u_{1}, u_{2}\right)}\right)\right)^{-\gamma},$$
where $\tau=\operatorname{dist}_{-1}\left(\left(\theta_{1}+d d^{c} u_{1}\right)^{n},\left(\theta_{2}+d d^{c} u_{2}\right)^{n}\right), G(\tau)=A^{2} H^{a}\left(A \tau^{a(1-b)}\right)+H\left(H^{m}\left(\tau^{1-b}\right)\right)+\tau^{a b}$ and $h(s)=(-\tilde{\chi}(-s))^{1 / 2}$.

Proof. Without loss of generality, we can assume that $\int_{X}\left(\theta_{2}+d d^{c} u_{2}\right)^{n} \geq \int_{X}\left(\theta_{1}+d d^{c} u_{1}\right)^{n}$. Denote $\mu_{1}=\left(\theta_{1}+d d^{c} u_{1}\right)^{n}, \mu_{2}=\left(\theta_{2}+d d^{c} u_{2}\right)^{n}$ and $c=\frac{\mu_{1}(X)}{\mu_{2}(X)} \leq 1$. It follows from [17, Theorem 4.7] that there exists a unique $u_{3} \in \mathcal{E}\left(X, \theta_{1}, P_{\theta_{1}}\left[u_{1}\right]\right)$ such that
$$\left\{\begin{array}{l}
\left(\theta_{1}+d d^{c} u_{3}\right)^{n}=c \mu_{2}, \\
\sup _{X} u_{3}=0 .
\end{array}\right.$$
By Theorem 4.13, we have
$$d_{\text {cap }}\left(u_{1}, u_{3}\right)^{2} \leq C_{1}(A B)^{2}\left(h^{\circ n}\left(\frac{\delta}{A G(x)+d_{\theta_{1}}\left(u_{1}, u_{3}\right)}\right)\right)^{-\gamma},$$
where $x:=\operatorname{dist}_{-1}\left(\mu_{1}, c \mu_{2}\right)$ and $C_{1}>0$ depends only on $n, X, \omega, H(1), a, b, \gamma$ and $m$.
By Theorem 1.2, we have
$$d_{\text {cap }}\left(u_{2}, u_{3}\right)^{2} \leq C_{2}(A B)^{2}\left(h^{\circ n}\left(\frac{\delta}{(1-c)\left\|\mu_{2}\right\|+A^{n}\left\|\theta_{1}-\theta_{2}\right\|_{\mathscr{C}^{0}}+d_{(A+1) \omega}\left(u_{2}, u_{3}\right)}\right)\right)^{-\gamma}$$
where $C_{2}>0$ depends only on $n, X, \omega$ and $\gamma$.
Combining (4.43), (4.44) and using the fact $d_{\theta_{1}}\left(u_{1}, u_{3}\right)=d_{(A+1) \omega}\left(u_{1}, u_{3}\right)=0$, we get
$$d_{\text {cap }}\left(u_{1}, u_{2}\right)^{2} \leq C_{3}(A B)^{2}\left(h^{\circ n}\left(\frac{\delta}{A G(x)+(1-c)\left\|\mu_{2}\right\|+R}\right)\right)^{-\gamma},$$
where $R=A^{n}\left\|\theta_{1}-\theta_{2}\right\|_{\mathscr{C}^{0}}+d_{(A+1) \omega}\left(u_{1}, u_{2}\right)$ and $C_{2}>0$ is a constant depending only on $n, X, \omega, H(1), a, b, \gamma$ and $m$.

Note that
$$(1-c)\left\|\mu_{2}\right\|=\int_{X} d \mu_{2}-\int_{X} d \mu_{1} \leq \operatorname{dist}_{-1}\left(\mu_{1}, \mu_{2}\right)=\tau$$
Then
$$x=\operatorname{dist}_{-1}\left(\mu_{1}, c \mu_{2}\right) \leq \operatorname{dist}_{-1}\left(\mu_{1}, \mu_{2}\right)+(1-c)\left\|\mu_{2}\right\| \leq 2 \operatorname{dist}_{-1}\left(\mu_{1}, \mu_{2}\right)=2 \tau .$$
Combining (4.45), (4.46) and (4.47), we get
$$d_{\text {cap }}\left(u_{1}, u_{2}\right)^{2} \leq C_{3}(A B)^{2}\left(h^{\circ n}\left(\frac{\delta}{A G(\tau)+A^{n}\left\|\theta_{1}-\theta_{2}\right\|_{\mathscr{C}^{0}}+d_{(A+1) \omega}\left(u_{1}, u_{2}\right)}\right)\right)^{-\gamma},$$
where $C_{3}>0$ depends only on $n, X, \omega, H(1), a, b, \gamma$ and $m$.
This finishes the proof. \(\square\)

End of the proof of Theorem 1.3 By the assumption and by [27, Lemma 3.3], we have $\mu_{j}:=$ $\left(\theta_{j}+d d^{c} u_{j}\right)^{n}$ satisfies (4.41) for $H(t)=\tilde{M} \delta t^{\beta}$ and $j=1,2$, where $\tilde{M}>0$ is a constant depending only on $X, \omega$ and $M$. Moreover, it follows from [27, Proposition 4.4] that, for every $\psi \in \operatorname{PSH}(X, \omega)$ with $\sup _{X} \psi=0$,
$$\int_{X}-\psi \mu_{j} \leq B \delta,$$
where $B>0$ depends on $X, \omega, M$ and $\beta$. Hence, by using Theorem 4.18 (choose $a=\gamma^{1 / 2}$, $b=\frac{a \beta}{a \beta+1}$ and $m=\frac{a b}{(1-b) \beta^{2}}$ ), we have
$$d_{\text {cap }}\left(u_{1}, u_{2}\right)^{2} \leq C\left(\frac{\tau^{\gamma \beta /(\beta+1)}+\left\|\theta_{1}-\theta_{2}\right\|_{\mathscr{C} 0}+d_{(A+1) \omega}\left(u_{1}, u_{2}\right)}{\delta}\right)^{2^{-n} \gamma},$$
where $\tau=\operatorname{dist}_{-1}\left(\mu_{1}, \mu_{2}\right)$ and $C>0$ is a constant depending only on $n, X, \omega, A, M, \gamma$ and $\beta$.

The proof is completed. \(\square\)

In order to prove Theorem 1.4, we need again several auxiliary lemmas.
Lemma 4.19. Let $\mu$ be a Radon measure on $X$ vanishing on every pluripolar set. Assume that $u_{j}, j \in \mathbb{N} \cup\{\infty\}$, are negative $\theta$-psh functions satisfying $u_{j} \rightarrow u_{\infty}$ in $L^{1}(X)$ as $j \rightarrow \infty$. Then
$$\int_{X} \min \left\{\left|u_{j}-u_{\infty}\right|, 1\right\} d \mu \rightarrow 0$$
as $j \rightarrow \infty$.
Proof. Denote $B=\sup _{j}\left\|u_{j}\right\|_{L^{1}}$. By Chern-Levine-Nirenberg inequality, there exists $C>0$ such that
$$\operatorname{cap}\left\{u_{j}<-k\right\} \leq \frac{B C}{k},$$
for every $j \in \mathbb{N} \cup\{\infty\}$ and $k>0$. Since $\mu$ vanishes on pluripolar sets, by [34, Lemma 4.5], there exists $w \in \operatorname{PSH}(X, \omega) \cap L^{\infty}(X)$ such that $\mu=f \omega_{w}^{n}$ for some nonnegative function $f \in L^{1}\left(\omega_{w}^{n}\right)$. Let $M>0$ be a big enough constant such that
$$\int_{\{f>M\}} d \mu<\epsilon / 6 .$$
We have
$$\begin{aligned}
\mu\left(\left\{u_{j}<-k\right\}\right) & =\int_{\{f>M\} \cap\left\{u_{j}<-k\right\}} d \mu+\int_{\{f>M\} \cap\left\{u_{j}<-k\right\}} d \mu \\
& \leq \int_{\{f \leq M\} \cap\left\{u_{j}<-k\right\}} d \mu+\int_{\{f>M\}} d \mu \\
& \leq M\left(\sup _{X} w-\inf _{X} w\right) \operatorname{cap}\left\{u_{j}<-k\right\}+\epsilon / 6
\end{aligned}$$
It follows that for each $\epsilon>0$, there exists $k_{0} \geq 1$ such that
$$\mu\left(\left\{u_{j}<-k\right\}\right) \leq \epsilon / 3$$
for every $j \in \mathbb{N} \cup\{\infty\}$ and $k \geq k_{0}$. Denote $u_{j, k}=\max \left\{u_{j},-k\right\}$ and $v_{j, k}=\max \left\{u_{j, k}, u_{\infty, k}\right\}$. Thus for every $k$, we have $u_{j, k} \rightarrow u_{\infty, k}$ in $L^{1}(X)$ and $v_{j, k} \rightarrow u_{\infty, k}$ in capacity as $j \rightarrow \infty$. It follows from [36, Lemma 11.5] that
$$\int_{X} \max \left\{u_{j, k}-u_{\infty, k}, 0\right\} d \mu=\int_{X}\left(v_{j, k}-u_{\infty, k}\right) d \mu \rightarrow 0$$
and
$$\int_{X}\left(u_{j, k}-u_{\infty, k}\right) d \mu \rightarrow 0$$
as $j \rightarrow \infty$. Combining the last two convergences gives
$$\int_{X}\left|u_{j, k}-u_{\infty, k}\right| d \mu \rightarrow 0$$
as $j \rightarrow \infty$. Choose $j_{0}$ such that
$$\int_{X}\left|u_{j, k_{0}}-u_{\infty, k_{0}}\right| d \mu<\frac{\epsilon}{3}$$
for every $j>j_{0}$. Using the last inequality and (4.48), we have
$$\begin{aligned}
\int_{X} \min \left\{\left|u_{j}-u_{\infty}\right|, 1\right\} d \mu & \leq \int_{\left\{u_{j}, u_{\infty} \geq-k_{0}\right\}}\left|u_{j}-u_{\infty}\right| d \mu+\mu\left(\left\{u_{j}<-k\right\}\right)+\mu\left(\left\{u_{\infty}<-k\right\}\right) \\
& \leq \int_{\left\{u_{j}, u_{\infty} \geq-k_{0}\right\}}\left|u_{j, k_{0}}-u_{\infty, k_{0}}\right| d \mu+\frac{2 \epsilon}{3} \leq \epsilon,
\end{aligned}$$
for every $j>j_{0}$. Thus $\int_{X} \min \left\{\left|u_{a_{j}}-u_{\infty}\right|, 1\right\} d \mu \rightarrow 0$ as $j \rightarrow \infty$. \(\square\)

Lemma 4.20. Let $\mu$ be a Radon measure on $X$ vanishing on every pluripolar set. Then, there exists a concave, non-decreasing function $H: \mathbb{R}_{\geq 0} \rightarrow \mathbb{R}_{\geq 0}$ with $H(0)=0$ such that
$$\int_{X} \min \{|u-v|, 1\} d \mu \leq H\left(\|u-v\|_{L^{1}(X)}\right)$$
for every $u, v \in \operatorname{PSH}(X, \omega)$.
Proof. For every $t>0$, we denote
$$h(t)=\sup \left\{\int_{X} \min \{|u-v|, 1\} d \mu: u, v \in \operatorname{PSH}(X, \omega),\|u-v\|_{L^{1}(X)} \leq t\right\} .$$
Then $h$ is non-decreasing. We will show that
$$\lim _{t \rightarrow 0^{+}} h(t)=0 .$$
Indeed, if $\lim _{t \rightarrow 0^{+}} h(t)=2 \epsilon>0$ then there exist sequences $u_{j}, v_{j} \in \operatorname{PSH}(X, \omega)$ such that $\left\|u_{j}-v_{j}\right\|_{L^{1}(X)} \rightarrow 0$ as $j \rightarrow \infty$ and
$$\int_{X} \min \left\{\left|u_{j}-v_{j}\right|, 1\right\} d \mu \geq \epsilon$$
for every $j$. Without loss of generality, we can assume that $c_{j}:=\sup _{X} v_{j} \leq \sup _{X} u_{j}=0$
By the compactness of $\operatorname{PSH}_{\text {sup }}(X, \omega):=\left\{\varphi \in \operatorname{PSH}(X, \omega): \sup _{X} \varphi=0\right\}$ in $L^{1}(X)$, we can assume that $u_{j}, v_{j}-c_{j} \rightarrow w \in \operatorname{PSH}_{\text {sup }}(X, \omega)$ as $j \rightarrow \infty$. In particular,
$$c_{j} \int_{X} \omega^{n} \leq\left\|u_{j}-v_{j}\right\|_{L^{1}(X)}+\left\|u_{j}-w\right\|_{L^{1}(X)}+\left\|v_{j}-c_{j}-w\right\|_{L^{1}(X)} \xrightarrow{j \rightarrow \infty} 0 .$$
Moreover, it follows from Lemma 4.19 that
$$\lim _{j \rightarrow \infty} \int_{X} \min \left\{\left|u_{j}-w\right|, 1\right\} d \mu=\lim _{j \rightarrow \infty} \int_{X} \min \left\{\left|v_{j}-c_{j}-w\right|, 1\right\} d \mu=0$$
and it follows that
$$\lim _{j \rightarrow \infty} \int_{X} \min \left\{\left|u_{j}-v_{j}-c_{j}\right|, 1\right\} d \mu=0$$
Combining (4.51) and (4.52), we get
$$\lim _{j \rightarrow \infty} \int_{X} \min \left\{\left|u_{j}-v_{j}\right|, 1\right\} d \mu=0$$
This contradicts with (4.50). Hence, (4.49) is true.
Now, we put
$$\tilde{h}(t)=\left\{\begin{array}{l}
h(t) \quad \text { if } \quad 0<t<1, \\
\int_{X} \mu \quad \text { if } \quad t \geq 1 .
\end{array}\right.$$
For every $m>1$, we also define
$$k_{m}=\sup \left\{\frac{\tilde{h}(s)}{s}: \frac{1}{m} \leq t\right\} \quad \text { and } \quad H_{m}(t)=k_{m} t+h(1 / m) .$$
Then $H_{m}(t) \geq h(t)$ for every $t \geq 0$ and $\lim _{t \rightarrow 0^{+}} H_{m}(t)=h(1 / m)$. Set $H(t)=\inf _{m>1} H_{m}(t)$. We have $H$ is a concave, non-decreasing function satisfying $H(0)=0$ and $H \geq h$. In particular,
$$\int_{X} \min \{|u-v|, 1\} d \mu \leq H\left(\|u-v\|_{L^{1}(X)}\right),$$
for every $u, v \in \operatorname{PSH}(X, \omega)$.
The proof is completed. \(\square\)

End of the proof of Theorem 1.4 By Lemma 4.20, there exists a concave, non-decreasing function $H: \mathbb{R}_{\geq 0} \rightarrow \mathbb{R}_{\geq 0}$ depending only on $\mu, X$ and $\omega$ such that $H(0)=0$ and
$$\int_{X} \min \left\{\left|\psi_{1}-\psi_{2}\right|, 1\right\} d \mu \leq H\left(\left\|\psi_{1}-\psi_{2}\right\|_{L^{1}(X)}\right)$$
for every $\psi_{1}, \psi_{2} \in \operatorname{PSH}(X, \omega)$.
Moreover, it follows from [8, Proposition 3.2] that there exist a constant $B>0$ and a function $\tilde{\chi} \in \mathcal{W}^{-}$depending on $X, \omega$ and $\mu$ such that
$$\int-\tilde{\chi}(\psi) d \mu \leq B$$
for every $\psi \in \operatorname{PSH}(X, \omega)$ with $\sup _{X} \psi=0$. In particular, $u_{j} \in \tilde{\mathcal{E}}_{\tilde{\chi},(A+1) \omega,(A+1) B}\left(X, \theta_{j}\right)$ for $j=1,2$. Hence, by Theorem 4.18, there exists $C>0$ depending only on $n, X, \omega$ and $H(1)$ such that
$$d_{\text {cap }}\left(u_{1}, u_{2}\right)^{2} \leq \frac{C(A+1)^{2} B^{2}}{\delta^{2}}\left(h^{\circ n}\left(\frac{\delta}{A G(\tau)+A^{n}\left\|\theta_{1}-\theta_{2}\right\|_{\mathscr{C}^{0}}+d_{(A+1) \omega}\left(u_{1}, u_{2}\right)}\right)\right)^{-1 / 2},$$
where $\tau=\operatorname{dist}_{-1}\left(\mu_{1}, \mu_{2}\right), G(\tau)=A^{2} H^{1 / 2}\left(A \tau^{1 / 4}\right)+H\left(H\left(\tau^{1 / 2}\right)\right)+\tau^{1 / 4}$ and $h(s)=(-\tilde{\chi}(-s))^{1 / 2}$. Denote
$$f_{\mu}(t)=\frac{C(A+1)^{2} B^{2}}{\delta^{2}}\left(h^{\circ n}\left(\frac{\delta}{A G(t)+A^{n} t}\right)\right)^{-1 / 2} .$$

We obtain
$$d_{\text {cap }}\left(u_{1}, u_{2}\right)^{2} \leq f_{\mu}\left(\text { dist }_{-1}\left(\mu_{1}, \mu_{2}\right)+\left\|\theta_{1}-\theta_{2}\right\|_{\mathscr{C}^{0}}+d_{(A+1) \omega}\left(u_{1}, u_{2}\right)\right) .$$
The proof is completed. \(\square\)

Remark 4.21. We explain how to prove Proposition 4.15 using either Theorem 1.4 or 1.3 (in place of Proposition 4.14). This is almost identical to the proof of Proposition 4.15 presented above: the new point is to show that there is a subsequence of $\left(u_{j}\right)_{j}$ which is convergent in capacity. To this end, we can assume $u_{j}$ 's are model as we did in the above proof of Proposition 4.15 Next we extract a subsequence $\left(u_{j_{s}}\right)_{s}$ of $\left(u_{j}\right)_{j}$ such that $u_{j_{s}}$ converges to some $u$ in $L^{1}$, and $\theta_{u_{j_{s}}}^{n}$ is convergent. Now applying either Theorem 1.4 or 1.3 (thanks to (4.30)), one sees that the sequence $\left(u_{j_{s}}\right)_{s}$ is convergent in capacity. Consequently $u_{j_{s}} \rightarrow u$ in capacity (see, e.g., [26, Lemma 2.2]).

\section*{References}
\begin{itemize}
\item[] [1] E. Bedford and B. A. Taylor, Fine topology, Šilov boundary, and $\left(d d^{c}\right)^{n}$, J. Funct. Anal., 72 (1987), pp. 225-251.
\item[] [2] R. J. Berman, S. Boucksom, V. Guedj, and A. Zeriahi, A variational approach to complex Monge-Ampère equations, Publ. Math. Inst. Hautes Études Sci., 117 (2013), pp. 179-245.
\item[] [3] R. J. Berman, S. Boucksom, and M. Jonsson, A variational approach to the Yau-Tian-Donaldson conjecture, J. Am. Math. Soc., 34 (2021), pp. 605-652.
\item[] [4] R. J. Berman, T. Darvas, and C. H. Lu, Regularity of weak minimizers of the $K$ -energy and applications to properness and $K$-stability, Ann. Sci. Éc. Norm. Supér. (4), 53 (2020), pp. 267-289.
\item[] [5] F. Berteloot, Bifurcation currents in holomorphic families of rational maps, in Pluripotential theory, vol. 2075 of Lecture Notes in Math., Springer, Heidelberg, 2013, pp. 1-93.
\item[] [6] O. Biquard and H. Guenancia, Degenerating Kähler-Einstein cones, locally symmetric cusps, and the Tian-Yau metric, Invent. Math., 230 (2022), pp. 1101-1163.
\item[] [7] Z. BŁOCKI, Uniqueness and stability for the complex Monge-Ampère equation on compact Kähler manifolds, Indiana Univ. Math. J., 52 (2003).
\item[] [8] S. Boucksom, P. Eyssidieux, V. Guedj, and A. Zeriahi, Monge-Ampère equations in big cohomology classes, Acta Math., 205 (2010), pp. 199-262.
\item[] [9] U. Cegrell, Pluricomplex energy, Acta Math., 180 (1998), pp. 187-217.
\item[] [10] U. Cegrell and S. Kolodziej, The equation of complex Monge-Ampère type and stability of solutions, Math. Ann., 334 (2006), pp. 713-729.
\end{itemize}
[11] T. Darvas, The Mabuchi geometry of finite energy classes, Adv. Math., 285 (2015), pp. 182-219.
[12] \_\_\_\_, The Mabuchi completion of the space of Kähler potentials, Amer. J. Math., 139 (2017), pp. 1275-1313.
[13] \_\_\_\_, Geometric pluripotential theory on Kähler manifolds, in Advances in complex geometry, vol. 735 of Contemp. Math., Amer. Math. Soc., Providence, RI, 2019, pp. 1-104.
[14] T. Darvas, The Mabuchi geometry of low energy classes. arXiv:2109.11581, 2021.
[15] T. Darvas, E. Di Nezza, and C. H. Lu, $L^{1}$ metric geometry of big cohomology classes, Ann. Inst. Fourier (Grenoble), 68 (2018), pp. 3053-3086.
[16] \_\_\_\_, Monotonicity of nonpluripolar products and complex Monge-Ampère equations with prescribed singularity, Anal. PDE, 11 (2018), pp. 2049-2087.
[17] T. Darvas, E. Di Nezza, and C. H. Lu, Log-concavity of volume and complex Monge-Ampère equations with prescribed singularity, Math. Ann., 379 (2021), pp. 95-132.
[18] T. Darvas, E. Di Nezza, and H.-C. Lu, The metric geometry of singularity types, J. Reine Angew. Math., 771 (2021), pp. 137-170.
[19] J.-P. Demailly, S. Dinew, V. Guedj, H. H. Pham, S. Kolodziej, and A. Zeriahi, Hölder continuous solutions to Monge-Ampère equations, J. Eur. Math. Soc. (JEMS), 16 (2014), pp. 619-647.
[20] E. Di Nezza, V. Guedj, and H. Guenancia, Families of singular Kähler-Einstein metrics. arXiv: 2003. 08178, 2020. to appear in J. Eur. Math. Soc.
[21] E. Di Nezza and C. H. Lu, $L^{p}$ metric geometry of big and nef cohomology classes, Acta Math. Vietnam., 45 (2020), pp. 53-69.
[22] E. Di Nezza and C. H. Lu, Geodesic distance and Monge-Ampére measures on contact sets, Anal. Math., 48 (2022), pp. 451-488.
[23] S. Dinew, Uniqueness in $\mathcal{E}(X, \omega)$, J. Funct. Anal., 256 (2009), pp. 2113-2122.
[24] S. Dinew and Z. Zhang, On stability and continuity of bounded solutions of degenerate complex Monge-Ampère equations over compact Kähler manifolds, Adv. Math., 225 (2010).
[25] T.-C. Dinh, S. Kolodziej, and N. C. Nguyen, The complex Sobolev space and Hölder continuous solutions to Monge-Ampère equations. arXiv:2008.00260, 2020.
[26] T.-C. Dinh, G. Marinescu, and D.-V. Vu, Moser-Trudinger inequalities and Monge-Ampère equations. arXiv:2006.07979, 2020. to appear in Ann. Sc. Norm. Super. Pisa Cl. Sci. (5).
\begin{itemize}
\item[] [27] T.-C. Dinh and V.-A. NGuyên, Characterization of Monge-Ampère measures with Hölder continuous potentials, J. Funct. Anal., 266 (2014), pp. 67-84.
\item[] [28] T.-C. Dinh, V.-A. Nguyên, and T. T. Truong, Equidistribution for meromorphic maps with dominant topological degree, Indiana Univ. Math. J., 64 (2015), pp. 1805-1828.
\item[] [29] T.-C. Dinh and N. Sibony, Distribution des valeurs de transformations méromorphes et applications, Comment. Math. Helv., 81 (2006), pp. 221-258.
\item[] [30] \_\_\_\_, Super-potentials of positive closed currents, intersection theory and dynamics, Acta Math., 203 (2009), pp. 1-82.
\item[] [31] \_\_\_\_, Dynamics in several complex variables: endomorphisms of projective spaces and polynomial-like mappings, in Holomorphic dynamical systems, vol. 1998 of Lecture Notes in Math., Springer, Berlin, 2010, pp. 165-294.
\item[] [32] D. T. Do and D.-V. Vu, Complex Monge-Ampère equations with solutions in finite energy classes. arXiv:2010.08619, 2020. to appear in Math. Res. Lett.
\item[] [33] P. Eyssidieux, V. Guedj, and A. Zeriahi, Singular Kähler-Einstein metrics, J. Amer. Math. Soc., 22 (2009), pp. 607-639.
\item[] [34] V. Guedj and A. Zeriahi, The weighted Monge-Ampère energy of quasiplurisubharmonic functions, J. Funct. Anal., 250 (2007), pp. 442-482.
\item[] [35] \_\_\_\_, Stability of solutions to complex Monge-Ampère equations in big cohomology classes, Math. Res. Lett., 19 (2012), pp. 1025-1042.
\item[] [36] \_\_\_\_, Degenerate complex Monge-Ampère equations, vol. 26 of EMS Tracts in Mathematics, European Mathematical Society (EMS), Zürich, 2017.
\item[] [37] P. Gupta, A complete metric topology on relative low energy spaces. arXiv:2206.03999, 2022.
\item[] [38] H.-J. Hein and V. Tosatti, Higher-order estimates for collapsing Calabi-Yau metrics, Camb. J. Math., 8 (2020), pp. 683-773.
\item[] [39] H.-J. Hein and V. Tosatti, Smooth asymptotics for collapsing Calabi-Yau metrics. arXiv:2102.03978, 2021.
\item[] [40] P. H. Hiep, Hölder continuity of solutions to the Monge-Ampère equations on compact Kähler manifolds, Ann. Inst. Fourier (Grenoble), 60 (2010), pp. 1857-1869.
\item[] [41] S. KoŁodziej, The complex Monge-Ampère equation, Acta Math., 180 (1998), pp. 69-117.
\item[] [42] \_\_\_\_, The Monge-Ampère equation on compact Kähler manifolds, Indiana Univ. Math. J., 52 (2003).
\end{itemize}
\begin{itemize}
\item[] [43] \_\_\_\_, The complex Monge-Ampère equation and pluripotential theory, Mem. Amer. Math. Soc., 178 (2005), pp. x+64.
\item[] [44] \_\_\_\_, Hölder continuity of solutions to the complex Monge-Ampère equation with the right-hand side in $L^{p}$ : the case of compact Kähler manifolds, Math. Ann., 342 (2008).
\item[] [45] S. Kolodziej and N. C. Nguyen, Weak solutions to the complex Monge-Ampère equation on Hermitian manifolds, in Analysis, complex geometry, and mathematical physics: in honor of Duong H. Phong, vol. 644 of Contemp. Math., Amer. Math. Soc., Providence, RI, 2015, pp. 141-158.
\item[] [46] \_\_\_\_, Hölder continuous solutions of the Monge-Ampère equation on compact Hermitian manifolds, Ann. Inst. Fourier (Grenoble), 68 (2018), pp. 2951-2964.
\item[] [47] \_\_\_\_, Continuous solutions to Monge-Ampère equations on Hermitian manifolds for measures dominated by capacity, Calc. Var. Partial Differential Equations, 60 (2021).
\item[] [48] C. H. Lu, Comparison of Monge-Ampère capacities, Ann. Polon. Math., 126 (2021), pp. 31-53.
\item[] [49] H.-C. Lu and V. Guedj, Quasi-plurisubharmonic envelopes 3: Solving Monge-Ampère equations on Hermitian manifolds. arXiv:2107.01938, 2021.
\item[] [50] H.-C. Lu, T.-T. Phung, and T.-D. Tô, Stability and Hölder regularity of solutions to complex Monge-Ampère equations on compact Hermitian manifolds. arXiv:2003.08417, 2020. to appear in Annales de l'Institut Fourier.
\item[] [51] A. Lunardi, Interpolation theory, Appunti. Scuola Normale Superiore di Pisa (Nuova Serie). [Lecture Notes. Scuola Normale Superiore di Pisa (New Series)], Edizioni della Normale, Pisa, second ed., 2009.
\item[] [52] N. C. NGuyen, On the Hölder continuous subsolution problem for the complex Monge-Ampère equation, Calc. Var. Partial Differential Equations, 57 (2018), pp. Paper No. 8, 15.
\item[] [53] \_\_\_\_, On the Hölder continuous subsolution problem for the complex Monge-Ampère equation, II, Anal. PDE, 13 (2020), pp. 435-453.
\item[] [54] J. Ross and D. Witt Nyström, Analytic test configurations and geodesic rays, J. Symplectic Geom., 12 (2014), pp. 125-169.
\item[] [55] V. Tosatti, Limits of Calabi-Yau metrics when the Kähler class degenerates, J. Eur. Math. Soc. (JEMS), 11 (2009), pp. 755-776.
\item[] [56] \_\_\_\_, Adiabatic limits of Ricci-flat Kähler metrics, J. Differential Geom., 84 (2010), pp. 427-453.
\item[] [57] \_\_\_\_, Ricci-flat metrics and dynamics on K3 surfaces, Boll. Unione Mat. Ital., 14 (2021), pp. 191-209.
\end{itemize}
\begin{itemize}
\item[] [58] V. Tosatti and B. Weinkove, The complex Monge-Ampère equation on compact Hermitian manifolds, J. Amer. Math. Soc., 23 (2010), pp. 1187-1195.
\item[] [59] V. Tosatti, B. Weinkove, and X. Yang, The Kähler-Ricci flow, Ricci-flat metrics and collapsing limits, Amer. J. Math., 140 (2018), pp. 653-698.
\item[] [60] H. Triebel, Interpolation theory, function spaces, differential operators, Johann Ambrosius Barth, Heidelberg, second ed., 1995.
\item[] [61] A. Trusiani, Continuity method with movable singularities for classical complex Monge-Ampère equations. arXiv:2006.09120, 2022. to appear in Indiana University Mathematics Journal.
\item[] [62] \_\_\_\_, $L^{1}$ metric geometry of potentials with prescribed singularities on compact Kähler manifolds, J. Geom. Anal., 32 (2022), pp. Paper No. 37, 37.
\item[] [63] \_\_\_\_, The strong topology of $\omega$-plurisubharmonic functions. arXiv:2002.00665, 2022. to appear in Anal. PDE.
\item[] [64] C. Villani, Optimal transport, vol. 338 of Grundlehren der mathematischen Wissenschaften [Fundamental Principles of Mathematical Sciences], Springer-Verlag, Berlin, 2009. Old and new.
\item[] [65] D.-V. Vu, Complex Monge-Ampère equation for measures supported on real submanifolds, Math. Ann., 372 (2018), pp. 321-367.
\item[] [66] \_\_\_\_, Families of Monge-Ampère measures with Hölder continuous potentials, Proc. Amer. Math. Soc., 146 (2018), pp. 4275-4282.
\item[] [67] \_\_\_\_, Relative non-pluripolar product of currents, Ann. Global Anal. Geom., 60 (2021), pp. 269-311.
\item[] [68] \_\_\_\_, Convexity of the class of currents with finite relative energy, Ann. Pol. Math., 128 (2022), pp. 275-288.
\item[] [69] D. Witt Nyström, Monotonicity of non-pluripolar Monge-Ampère masses, Indiana Univ. Math. J., 68 (2019), pp. 579-591.
\item[] [70] M. Xia, Mabuchi geometry of big cohomology classes with prescribed singularities. arXiv:1907.07234, 2021.
\item[] [71] Y. Xing, Continuity of the complex Monge-Ampère operator on compact Kähler manifolds, Math. Z., 263 (2009), pp. 331-344.
\item[] [72] S. T. YAU, On the Ricci curvature of a compact Kähler manifold and the complex Monge-Ampère equation. I, Comm. Pure Appl. Math., 31 (1978).
\end{itemize}

Duc-Viet Vu, University of Cologne, Division of Mathematics, Department of Mathematics and
Computer Science, Weyertal 86-90, 50931, Köln, Germany
E-mail address: vuviet@math.uni-koeln.de
Hoang-Son Do, Vietnam Academy of Science and Technology, Institute of Mathematics, 18
Hoang Quoc Viet road, Cau Giay, Hanoi, Vietnam
E-mail address: dhson@math.ac.vn