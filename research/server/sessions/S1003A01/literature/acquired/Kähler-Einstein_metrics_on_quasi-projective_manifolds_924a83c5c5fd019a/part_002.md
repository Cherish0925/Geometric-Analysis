---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: Kähler-Einstein metrics on quasi-projective manifolds]

Lemma 5.5. There is a constant $A>0$ independent of $\epsilon, k$ such that for $j_{1}, j_{2}$ big enough, we have
$$\mathbf{1}_{\left\{u_{j_{1}, k} \leq u_{j_{2}, k}-M\right\}}\left(d d^{c} u_{j_{1}, k}+\theta_{\epsilon}^{\prime}\right)^{n} \leq \mathbf{1}_{\left\{u_{j_{1}, k} \leq u_{j_{2}, k}-M\right\}} e^{-M}\left(d d^{c} u_{j_{2}, k}+\theta_{\epsilon}^{\prime}\right)^{n}+R_{j_{1}},$$
where $R_{j_{1}}$ is a positive measure whose mass is given by
$$c\left(j_{1}, k, \epsilon\right):=\left\|R_{j_{1}}\right\|=A \epsilon+\int_{\left\{u_{j_{1}} \leq V_{\theta_{\epsilon}^{\prime}}-k\right\}}\left(d d^{c} u_{j_{1}, k}+\theta_{\epsilon}^{\prime}\right)^{n} .$$

Proof. Observe
$$\left\{u_{j_{1}, k} \leq u_{j_{2}, k}-M\right\} \subset K:=\left\{u_{j_{1}} \leq u_{j_{2}}-M\right\} \cap\left\{u_{j_{2}}>V_{\theta_{\epsilon}^{\prime}}-k\right\} .$$
Thus
$$\begin{aligned}
\mathbf{1}_{K}\left(d d^{c} u_{j_{1}, k}+\theta_{\epsilon}^{\prime}\right)^{n} \leq & \mathbf{1}_{K \cap\left\{u_{j_{1}}>V_{\theta_{\epsilon}^{\prime}}-k\right\}}\left(d d^{c} u_{j_{1}}+\theta_{\epsilon}^{\prime}\right)^{n}+\mathbf{1}_{K \cap\left\{u_{j_{1}} \leq V_{\theta_{\epsilon}^{\prime}}-k\right\}}\left(d d^{c} u_{j_{1}, k}+\theta_{\epsilon}^{\prime}\right)^{n} \\
\leq & \mathbf{1}_{K \cap\left\{u_{j_{1}}>V_{\theta_{\epsilon}^{\prime}}-k\right\}} e^{-M}\left(d d^{c} u_{j_{2}, k}+\theta_{\epsilon}^{\prime}\right)^{n} \\
& +O(\epsilon)+\mathbf{1}_{K \cap\left\{u_{j_{1}} \leq V_{\theta_{\epsilon}^{\prime}}-k\right\}}\left(d d^{c} u_{j_{1}, k}+\theta_{\epsilon}^{\prime}\right)^{n} .
\end{aligned}$$
This finishes the proof. \(\square\)

If we want to apply the quantitative domination principle to $u_{\epsilon_{j}, k}$, we need to check that $c\left(j_{1}, k, \epsilon\right)$ is "small", precisely,
$$\limsup _{k \rightarrow \infty} \limsup _{\epsilon \rightarrow 0} \limsup _{j_{1} \rightarrow \infty} c\left(j_{1}, k, \epsilon\right)=0 .$$
Verifying this limit is one of the main difficulties in our proof. We will go into detail in the next sections.

\subsection*{5.2 Low energy estimate}

We start with a fact about energy. The following monotonicity of energy is a direct consequence of [24, Lemma 3.2] (see also [28]).

Lemma 5.6. Let $\eta$ be a smooth closed $(1,1)$-form in a big cohomology class. Let $u, v \in \mathcal{E}(X, \eta)$ such that $u \leq v$. Let $\chi: \mathbb{R}_{\leq 0} \rightarrow \mathbb{R}_{\leq 0}$ be a convex increasing function such that $\chi(0)=0$. Then we have
$$-\int_{X} \chi\left(v-V_{\eta}\right)\left(d d^{c} v+\eta\right)^{k} \wedge \omega^{n-k} \leq-2^{k} \int_{X} \chi\left(u-V_{\eta}\right)\left(d d^{c} u+\eta\right)^{k} \wedge \omega^{n-k}$$

Let $\epsilon>0$ be a small constant. Let $\theta_{\epsilon}^{\prime}:=\theta+\epsilon \omega$. Let $j_{\epsilon} \in \mathbb{N}$ be such that $\theta_{j} \leq \theta_{\epsilon}^{\prime}$ for every $j \geq j_{\epsilon}$. Hence $u_{j}$ is $\theta_{\epsilon}^{\prime}$-psh for $j \geq j_{\epsilon}$. Note that $u_{j} \in \mathcal{E}\left(X, \theta_{j}\right)$. Let
$$u_{j, \epsilon}^{\prime \prime}:=\lim _{k \rightarrow \infty} P_{\theta_{\epsilon}^{\prime}}\left(\min \left\{u_{j}, \ldots, u_{k}\right\}\right),$$
for $j \geq j_{\epsilon}$. By Corollary 3.6, we have that $u_{j, \epsilon}^{\prime \prime}$ is a well-defined $\theta_{\epsilon}^{\prime}$-psh function and increases to some $\theta_{\epsilon}^{\prime}$-psh function $u_{\epsilon}^{\prime \prime}$ as $j \rightarrow \infty$ satisfying that $u_{\epsilon}^{\prime \prime}$ decreases to some $\theta$-psh function $u^{\prime \prime} \in \mathcal{E}(X, \theta)$ as $\epsilon$ decreases to 0.

Let $\tau: \mathbb{R}_{\leq 0} \rightarrow \mathbb{R}_{\leq 0}$ be an increasing convex function such that $\tau(0)=0$ and $\tau(-\infty)=$ $-\infty$ and
$$-\int_{X} \tau\left(u^{\prime \prime}-V_{\theta}\right)\left(d d^{c} u^{\prime \prime}+\theta\right)^{n}<\infty .$$
Observe that $u_{j} \geq u_{j, \epsilon}^{\prime \prime}$ for every $j \geq j_{\epsilon}$. Let
$$u_{j, k}:=\max \left\{u_{j}, V_{\theta_{\epsilon}^{\prime}}-k\right\}, \quad u_{j, \epsilon, k}^{\prime \prime}:=\max \left\{u_{j, \epsilon, k}^{\prime \prime}, V_{\theta_{\epsilon}^{\prime}}-k\right\}$$
for $k>0$. We define $u_{\epsilon, k}^{\prime \prime}$ and $u_{k}^{\prime \prime}$ respectively for $u_{\epsilon}^{\prime \prime}$ and $u^{\prime \prime}$ similarly.
Lemma 5.7. We have
$$\limsup _{j \rightarrow \infty} \int_{X}-\tau\left(u_{j, k}-V_{\theta_{\epsilon}^{\prime}}\right)\left(d d^{c} u_{j, k}+\theta_{\epsilon}^{\prime}\right)^{n} \leq 4^{n} \int_{X}-\tau\left(u_{k}^{\prime \prime}-V_{\theta_{\epsilon}^{\prime}}\right)\left(d d^{c} u_{k}^{\prime \prime}+\theta_{\epsilon}^{\prime}\right)^{n} .$$
for every $k \geq 0$.
Proof. We have $u_{j, k} \geq u_{j, \epsilon, k}^{\prime \prime}$. Hence using Lemma 5.6 gives
$$\int_{X}-\tau\left(u_{j, k}-V_{\theta_{\epsilon}^{\prime}}\right)\left(d d^{c} u_{j, k}+\theta_{\epsilon}^{\prime}\right)^{n} \leq 2^{n} \int_{X}-\tau\left(u_{j, \epsilon, k}^{\prime \prime}-V_{\theta_{\epsilon}^{\prime}}\right)\left(d d^{c} u_{j, \epsilon, k}^{\prime \prime}+\theta_{\epsilon}^{\prime}\right)^{n} .$$
Letting $j \rightarrow \infty$ and using the fact that $u_{j, \epsilon, k}^{\prime \prime}$ increases to $u_{\epsilon, k}^{\prime \prime}$ (hence we get correspondingly the continuity of energy), one gets
$$\limsup _{j \rightarrow \infty} \int_{X}-\tau\left(u_{j, k}-V_{\theta_{\epsilon}^{\prime}}\right)\left(d d^{c} u_{j, k}+\theta_{\epsilon}^{\prime}\right)^{n} \leq 2^{n} \limsup _{j \rightarrow \infty} \int_{X}-\tau\left(u_{j, \epsilon, k}^{\prime \prime}-V_{\theta_{\epsilon}^{\prime}}\right)\left(d d^{c} u_{j, \epsilon, k}^{\prime \prime}+\theta_{\epsilon}^{\prime}\right)^{n}$$
which is equal to $2^{n} I_{\epsilon, k}$, where
$$I_{\epsilon, k}:=\int_{X}-\tau\left(u_{\epsilon, k}^{\prime \prime}-V_{\theta_{\epsilon}^{\prime}}\right)\left(d d^{c} u_{\epsilon, k}^{\prime \prime}+\theta_{\epsilon}^{\prime}\right)^{n}$$
Now observe that $u_{\epsilon, k}^{\prime \prime}$ decreases to $u_{k}^{\prime \prime}$. It follows that
$$I_{\epsilon, k} \leq 2^{n} \int_{X}-\tau\left(u_{k}^{\prime \prime}-V_{\theta_{\epsilon}^{\prime}}\right)\left(d d^{c} u_{k}^{\prime \prime}+\theta_{\epsilon}^{\prime}\right)^{n}$$
The proof is thus complete. \(\square\)

Lemma 5.8. There exists a constant $C>0$ such that we have
$$\limsup _{\epsilon \rightarrow 0} \int_{X}-\tau\left(u_{k}^{\prime \prime}-V_{\theta_{\epsilon}^{\prime}}\right)\left(d d^{c} u_{k}^{\prime \prime}+\theta_{\epsilon}^{\prime}\right)^{n} \leq C,$$
for every $k \geq 0$.
Proof. Let $v_{k}^{\prime \prime}:=\max \left\{u^{\prime \prime}, V_{\theta}-k\right\} \geq u^{\prime \prime}$. We note that $u_{k}^{\prime \prime}$ depends on $\epsilon$ but $v_{k}^{\prime \prime}$ does not. Furthermore, we have $u_{k}^{\prime \prime}=v_{k}^{\prime \prime}$ on $\left\{u^{\prime \prime}>V_{\theta_{\epsilon}^{\prime}}-k\right\}$ (because $V_{\theta} \leq V_{\theta_{\epsilon}^{\prime}}$ ). Consequently, one can decompose
$$\begin{aligned}
\int_{X}-\tau\left(u_{k}^{\prime \prime}-V_{\theta_{\epsilon}^{\prime}}\right)\left(d d^{c} u_{k}^{\prime \prime}+\theta_{\epsilon}^{\prime}\right)^{n}= & \int_{\left\{u^{\prime \prime}>V_{\theta_{\epsilon}^{\prime}}-k\right\}}-\tau\left(u_{k}^{\prime \prime}-V_{\theta_{\epsilon}^{\prime}}\right)\left(d d^{c} u_{k}^{\prime \prime}+\theta_{\epsilon}^{\prime}\right)^{n}+ \\
& \int_{\left\{u^{\prime \prime} \leq V_{\theta_{\epsilon}^{\prime}}-k\right\}}-\tau\left(u_{k}^{\prime \prime}-V_{\theta_{\epsilon}^{\prime}}\right)\left(d d^{c} u_{k}^{\prime \prime}+\theta_{\epsilon}^{\prime}\right)^{n} \\
= & \int_{\left\{u^{\prime \prime}>V_{\theta_{\epsilon}^{\prime}}-k\right\}}-\tau\left(v_{k}^{\prime \prime}-V_{\theta_{\epsilon}^{\prime}}\right)\left(d d^{c} v_{k}^{\prime \prime}+\theta_{\epsilon}^{\prime}\right)^{n} \\
& -\tau(-k) \int_{\left\{u^{\prime \prime} \leq V_{\theta_{\epsilon}^{\prime}}-k\right\}}\left(d d^{c} u_{k}^{\prime \prime}+\theta_{\epsilon}^{\prime}\right)^{n} .
\end{aligned}$$
Denote by $I_{1}, I_{2}$ the first and the second term on the right-hand side of the last equality.
Recall that $T=d d^{c} \rho+\theta$ is a Kähler current with analytic singularities in the class of $\theta$, where $\rho \leq 0$. Since $d d^{c} \rho+\theta \geq \delta \omega$ for $\delta>0$ we see that $\epsilon^{1 / 2} \rho+\left(1-\epsilon^{1 / 2}\right) V_{\theta_{\epsilon}^{\prime}}$ is a negative $\theta$-psh function for $\epsilon$ small enough. Since the latter is less than $V_{\theta}$, we infer
$$V_{\theta_{\epsilon}^{\prime}} \leq\left(1-\epsilon^{1 / 2}\right)^{-1} V_{\theta}-\epsilon^{1 / 2}\left(1-\epsilon^{1 / 2}\right)^{-1} \rho \leq V_{\theta}-2 \epsilon^{1 / 2} \rho,$$
for $\epsilon>0$ small enough. Since $\tau$ is convex and $\tau(0)=0$, one sees that
$$\tau(b+c) \geq \tau(b)+\tau(c)$$
for every $b, c \in \mathbb{R}_{\leq 0}$. Applying the last inequality to $b:=v_{k}^{\prime \prime}-V_{\theta}$ and $c:=V_{\theta}-V_{\theta_{\epsilon}^{\prime}}$, one obtains
$$-\tau\left(v_{k}^{\prime \prime}-V_{\theta_{\epsilon}^{\prime}}\right) \leq-\tau\left(v_{k}^{\prime \prime}-V_{\theta}\right)-\tau\left(V_{\theta}-V_{\theta_{\epsilon}^{\prime}}\right) \leq-\tau\left(v_{k}^{\prime \prime}-V_{\theta}\right)-\tau\left(2 \epsilon^{1 / 2} \rho\right) .$$

It follows that
$$I_{1} \leq \int_{X}-\tau\left(v_{k}^{\prime \prime}-V_{\theta}\right)\left(d d^{c} v_{k}^{\prime \prime}+\theta_{\epsilon}^{\prime}\right)^{n}-\int_{X} \tau\left(2 \epsilon^{1 / 2} \rho\right)\left(d d^{c} u_{k}^{\prime \prime}+\theta_{\epsilon}^{\prime}\right)^{n}$$
Letting $\epsilon \rightarrow 0$ gives
$$\limsup _{\epsilon \rightarrow 0} I_{1} \leq \int_{X}-\tau\left(v_{k}^{\prime \prime}-V_{\theta}\right)\left(d d^{c} v_{k}^{\prime \prime}+\theta\right)^{n} \leq 2^{n} \int_{X}-\tau\left(u^{\prime \prime}-V_{\theta}\right)\left(d d^{c} u^{\prime \prime}+\theta\right)^{n}$$
because $\tau(0)=0$ and $\left(d d^{c} u_{k}^{\prime \prime}+\theta\right)^{n}$ is a Monge-Ampère measure of bounded potentials.
We treat $I_{2}$. Direct computations show
$$\begin{aligned}
I_{2} & =-\tau(-k) \int_{X}\left(d d^{c} u_{k}^{\prime \prime}+\theta_{\epsilon}^{\prime}\right)^{n}+\tau(-k) \int_{\left\{u^{\prime \prime}>V_{\theta_{\epsilon}^{\prime}}-k\right\}}\left(d d^{c} u_{k}^{\prime \prime}+\theta_{\epsilon}^{\prime}\right)^{n} \\
& =-\tau(-k) \int_{X}\left(d d^{c} V_{\theta_{\epsilon}^{\prime}}+\theta_{\epsilon}^{\prime}\right)^{n}+\tau(-k) \int_{\left\{u^{\prime \prime}>V_{\theta_{\epsilon}^{\prime}}-k\right\}}\left(d d^{c} u^{\prime \prime}+\theta_{\epsilon}^{\prime}\right)^{n} \\
& \leq-\tau(-k)\left(\operatorname{vol}\left(\left\{\theta_{\epsilon}^{\prime}\right\}\right)-\operatorname{vol}(\{\theta\})+\operatorname{vol}(\{\theta\})-\int_{\left\{u^{\prime \prime}>V_{\theta_{\epsilon}^{\prime}}-k\right\}}\left(d d^{c} u^{\prime \prime}+\theta\right)^{n}\right) \\
& =-\tau(-k)\left(\operatorname{vol}\left(\left\{\theta_{\epsilon}^{\prime}\right\}\right)-\operatorname{vol}(\{\theta\})+\int_{\left\{u^{\prime \prime} \leq V_{\theta_{\epsilon}^{\prime}}-k\right\}}\left(d d^{c} u^{\prime \prime}+\theta\right)^{n}\right) \\
& \leq-\tau(-k)\left(\operatorname{vol}\left(\left\{\theta_{\epsilon}^{\prime}\right\}\right)-\operatorname{vol}(\{\theta\})+|\tau(-k)|^{-1} \int_{\left\{u^{\prime \prime} \leq V_{\theta_{\epsilon}^{\prime}}-k\right\}}-\tau\left(u^{\prime \prime}-V_{\theta_{\epsilon}^{\prime}}\right)\left(d d^{c} u^{\prime \prime}+\theta\right)^{n}\right) \\
& \leq-\tau(-k)\left(\operatorname{vol}\left(\left\{\theta_{\epsilon}^{\prime}\right\}\right)-\operatorname{vol}(\{\theta\})\right)+\int_{X}-\tau\left(u^{\prime \prime}-V_{\theta_{\epsilon}^{\prime}}\right)\left(d d^{c} u^{\prime \prime}+\theta\right)^{n}
\end{aligned}$$
whose limsup as $\epsilon \rightarrow 0$ is bounded by a constant independent of $k$, due to (5.8). Combining (5.10) and (5.9) gives the desired assertion. \(\square\)

Combining Lemmas 5.8 and 5.7, we obtain the following crucial estimate.
Proposition 5.9. There exists a constant $C>0$ independent of $k$ such that we have
$$\limsup _{\epsilon \rightarrow 0} \limsup _{j \rightarrow \infty} \int_{X}-\tau\left(u_{j, k}-V_{\theta_{\epsilon}^{\prime}}\right)\left(d d^{c} u_{j, k}+\theta_{\epsilon}^{\prime}\right)^{n} \leq C .$$

Corollary 5.10. Let $c\left(j_{1}, k, \epsilon\right)$ be the term defined in Lemma 5.5 Then we have
$$\limsup _{k \rightarrow \infty} \limsup _{\epsilon \rightarrow 0} \limsup _{j_{1} \rightarrow \infty} c\left(j_{1}, k, \epsilon\right)=0$$
Proof. Observe
$$\begin{aligned}
\limsup _{\epsilon \rightarrow 0} \limsup _{j_{1} \rightarrow \infty} c\left(j_{1}, k, \epsilon\right) & =\limsup _{\epsilon \rightarrow 0} \limsup _{j_{1} \rightarrow \infty} \int_{\left\{u_{j_{1}, k} \leq V_{\theta_{\epsilon}^{\prime}}-k\right\}}\left(d d^{c} u_{j_{1}, k}+\theta_{\epsilon}^{\prime}\right)^{n} \\
& \leq|\tau(-k)|^{-1} \limsup _{\epsilon \rightarrow 0} \limsup _{j_{1} \rightarrow \infty} \int_{\left\{u_{j_{1}} \leq V_{\theta_{\epsilon}^{\prime}}-k\right\}}-\tau\left(u_{j_{1}, k}-V_{\theta_{\epsilon}^{\prime}}\right)\left(d d^{c} u_{j_{1}, k}+\theta_{\epsilon}^{\prime}\right)^{n} \\
& \leq|\tau(-k)|^{-1} C
\end{aligned}$$
by Proposition 5.9. Letting $k \rightarrow \infty$ gives the desired equality. \(\square\)

We now finish the proof of Theorem 5.1.
End of the proof of Theorem 5.1. We apply the quantitative domination principle to $u_{j, k}$ in the class of $\left\{\theta_{\epsilon}^{\prime}\right\}$ and $\tilde{\chi}:=\tau$ (we can certainly choose $\tau$ so that $\tau(-1)=-1$ ). Let
$$B\left(j_{1}, j_{2}, k, \epsilon\right):=-\int_{X} \tau\left(u_{j_{1}, k}-V_{\theta_{\epsilon}^{\prime}}\right)\left(d d^{c} u_{j_{1}, k}+\theta_{\epsilon}^{\prime}\right)-\int_{X} \tau\left(u_{j_{2}, k}-V_{\theta_{\epsilon}^{\prime}}\right)\left(d d^{c} u_{j_{2}, k}+\theta_{\epsilon}^{\prime}\right) .$$
By Proposition 5.9, one has
$$\limsup _{\epsilon \rightarrow 0} \limsup _{j_{1}, j_{2} \rightarrow \infty} B\left(j_{1}, j_{2}, k, \epsilon\right) \leq C,$$
where $C>0$ is a constant independent of $k$. Let $0<\kappa \leq 1 / 4$ be a constant. By Theorem 2.2 applied to $u_{j_{1}, k}, u_{j_{2}, k}-\kappa$ (noticing also Lemma 5.5), there exists a constant $C_{1}>0$ independent of $j_{1}, j_{2}, k, \epsilon, \kappa$ such that
$$\operatorname{cap}_{\omega}\left(u_{j_{1}, k}-u_{j_{2}, k} \leq-2 \kappa\right) \leq C_{1} \kappa^{-2} \frac{\left(B\left(j_{1}, j_{2}, k, \epsilon\right)\right)^{2}+1}{h^{\circ n}\left(1 / c\left(j_{1}, k, \epsilon\right)\right)},$$
with $h(t):=(-\tau(-t))^{1 / 2}$, and $j_{1}, j_{2}>j_{\epsilon}$ big enough. Since
$$\operatorname{cap}_{\omega}\left(u_{j}<V_{\theta_{\epsilon}^{\prime}}-k\right) \leq \operatorname{cap}_{\omega}\left(u_{j}<-k\right) \lesssim k^{-1},$$
one infers
$$\operatorname{cap}_{\omega}\left(u_{j_{1}}-u_{j_{2}} \leq-2 \kappa\right) \lesssim \kappa^{-2} \frac{\left(B\left(j_{1}, j_{2}, k, \epsilon\right)\right)^{2}+1}{h^{\circ n}\left(1 / c\left(j_{1}, k, \epsilon\right)\right)}+k^{-1} .$$
Hence
$$\limsup _{j_{1}, j_{2} \rightarrow \infty} \operatorname{cap}_{\omega}\left(u_{j_{1}}-u_{j_{2}} \leq-\kappa\right) \lesssim \kappa^{-2} \limsup _{j_{1}, j_{2} \rightarrow \infty} \frac{\left(B\left(j_{1}, j_{2}, k, \epsilon\right)\right)^{2}+1}{h^{\circ n}\left(1 / c\left(j_{1}, k, \epsilon\right)\right)}+k^{-1}$$
for every $\epsilon \in(0,1]$ and $k \in \mathbb{N}$. Letting $\epsilon \rightarrow 0$ and using (5.11), we get
$$\limsup _{j_{1}, j_{2} \rightarrow \infty} \operatorname{cap}_{\omega}\left(u_{j_{1}}-u_{j_{2}} \leq-\kappa\right) \lesssim \kappa^{-2} \frac{1}{h^{\circ n}(1 / c(k))}+k^{-1},$$
for every $k$, where
$$c(k):=\limsup _{\epsilon \rightarrow 0} \limsup _{j_{1} \rightarrow \infty} c\left(j_{1}, k, \epsilon\right) .$$
By Corollary 5.10, we get $\limsup _{k \rightarrow \infty} c(k)=0$. It follows that
$$\limsup _{j_{1}, j_{2} \rightarrow \infty} \operatorname{cap}_{\omega}\left(u_{j_{1}}-u_{j_{2}} \leq-\kappa\right) \lesssim \limsup _{k \rightarrow \infty} \kappa^{-1} \frac{1}{h^{\circ n}(1 / c(k))}+k^{-1}=0,$$
for every constant $\kappa>0$. In other words, the sequence $\left(u_{j}\right)_{j}$ is decreasing in capacity. Let $\psi_{\gamma}$ be the function defined right before Corollary 3.5. Since $u_{j} \geq \psi_{\gamma}$ which is locally bounded outside the union $W$ of $D$ and the non-Kähler locus of $\{\theta\}$, we see that $\left(u_{j}\right)_{j}$
admits a subsequence converging in $L^{1}$. Let $u$ be, hence, a $L^{1}$-limit of $\left(u_{j}\right)_{j}$. Corollary 3.5 tells us that $u \in \mathcal{E}(X, \theta)$.

Since $u_{j} \geq \psi_{\gamma}$, we also get $u \geq \psi_{\gamma}$ and hence $u$ is locally bounded outside $W$. Proposition 2.4 now implies that
$$\left(d d^{c} u_{j}+\theta_{j}\right)^{n} \rightarrow\left(d d^{c} u+\theta\right)^{n}$$
weakly on $X \backslash W$ as $j \rightarrow \infty$. It follows that
$$\left(d d^{c} u+\theta\right)^{n}=e^{u}|s|_{h}^{-2} f \omega^{n}$$
on $X \backslash W$. The equality holds indeed on $X$ because the non-pluripolar products have no mass on $W$, which is a pluripolar set. Hence we get $\left(d d^{c} u+\theta\right)^{n}=e^{u}|s|_{h}^{-2} f \omega^{n}$ on $X$ and $u \in \mathcal{E}(X, \theta)$. This is, at most, one such $u$ by the domination principle. This yields that $u_{j} \rightarrow u$ in $L^{1}$ and $u$ satisfies the required Monge-Ampère equation. This ends the proof of Theorem 5.1. \(\square\)

\section*{References}
[1] H. Auvray, Metrics of Poincaré type with constant scalar curvature: a topological constraint, J. Lond. Math. Soc. (2), 87 (2013), pp. 607-621. 2
[2] -, Asymptotic properties of extremal Kähler metrics of Poincaré type, Proc. Lond. Math. Soc. (3), 115 (2017), pp. 813-853. 2
[3] -, The space of Poincaré type Kähler metrics on the complement of a divisor, J. Reine Angew. Math., 722 (2017), pp. 1-64. 2
[4] S. Bando, Einstein Kähler metrics of negative Ricci curvature on open Kähler manifolds, in Kähler metric and moduli spaces, vol. 18-II of Adv. Stud. Pure Math., Academic Press, Boston, MA, 1990, pp. 105-136. 2
[5] E. Bedford and B. A. Taylor, A new capacity for plurisubharmonic functions, Acta Math., 149 (1982), pp. 1-40. 7
[6] -, Fine topology, Šilov boundary, and $\left(d d^{c}\right)^{n}$, J. Funct. Anal., 72 (1987), pp. 225-251. [5]
[7] R. J. Berman, S. Boucksom, and M. Jonsson, A variational approach to the Yau-Tian-Donaldson conjecture, J. Amer. Math. Soc., 34 (2021), pp. 605-652. 1
[8] R. J. Berman and H. Guenancia, Kähler-Einstein metrics on stable varieties and log canonical pairs, Geom. Funct. Anal., 24 (2014), pp. 1683-1730. 1, 2, 3, 20
[9] O. Biquard and H. Guenancia, Degenerating Kähler-Einstein cones, locally symmetric cusps, and the Tian-Yau metric, Invent. Math., 230 (2022), pp. 1101-1163. 2, 3
[10] S. Boucksom, P. Eyssidieux, V. Guedj, and A. Zeriahi, Monge-Ampère equations in big cohomology classes, Acta Math., 205 (2010), pp. 199-262. 1, 2, 3, 5, 9, 19, 20, 21
\begin{itemize}
\item[] [11] S. Brendle, Ricci flat Kähler metrics with edge singularities, Int. Math. Res. Not. IMRN, (2013), pp. 5727-5766. 3
\item[] [12] F. Campana, H. Guenancia, and M. Păun, Metrics with cone singularities along normal crossing divisors and holomorphic tensor fields, Ann. Sci. Éc. Norm. Supér. (4), 46 (2013), pp. 879-916. 3
\item[] [13] S. Y. Cheng and S. T. Yau, On the existence of a complete Kähler metric on noncompact complex manifolds and the regularity of Fefferman's equation, Comm. Pure Appl. Math., 33 (1980), pp. 507-544. 1 , 15
\item[] [14] D. Coman, V. Guedj, and A. Zeriahi, Domains of definition of Monge-Ampère operators on compact Kähler manifolds, Math. Z., 259 (2008), pp. 393-418. 12
\item[] [15] Q.-T. Dang, Continuity of Monge-Ampère potentials in big cohomology classes, Int. Math. Res. Not. IMRN, (2022), pp. 11180-11201. 16
\item[] [16] T. Darvas, E. Di Nezza, and C. H. Lu, Monotonicity of nonpluripolar products and complex Monge-Ampère equations with prescribed singularity, Anal. PDE, 11 (2018), pp. 2049-2087. 5, 6, 12, 13
\item[] [17] T. Darvas, E. Di Nezza, and C. H. Lu, Log-concavity of volume and complex Monge-Ampère equations with prescribed singularity, Math. Ann., 379 (2021), pp. 95-132. [13]
\item[] [18] V. Datar, X. Fu, and J. Song, Kähler-Einstein metrics near an isolated log-canonical singularity, J. Reine Angew. Math., 797 (2023), pp. 79-116. 2
\item[] [19] J.-P. Demailly, Complex analytic and differential geometry. http://www.fourier.ujf-grenoble.fr/ ${ }^{\sim}$ demailly, 7
\item[] [20] -, Regularization of closed positive currents and intersection theory, J. Algebraic Geom., 1 (1992), pp. 361-409. 8
\item[] [21] E. Di Nezza, V. Guedj, and H. Guenancia, Families of singular Kähler-Einstein metrics, J. Eur. Math. Soc. (JEMS), 25 (2023), pp. 2697-2762. 4, 8, 10, 11
\item[] [22] E. Di Nezza and C. H. Lu, Complex Monge-Ampère equations on quasi-projective varieties, J. Reine Angew. Math., 727 (2017), pp. 145-167. 2, 16
\item[] [23] S. Dinew, Uniqueness in $\mathcal{E}(X, \omega)$, J. Funct. Anal., 256 (2009), pp. 2113-2122. 19
\item[] [24] D. T. Do and D.-V. Vu, Complex Monge-Ampère equations with solutions in finite energy classes, Math. Res. Lett., 29 (2022), pp. 1659-1683. 23
\item[] [25] H.-S. Do and D.-V. Vu, Quantitative stability for the complex Monge-Ampère equations I. arXiv:2405. 17491 to appear in Analysis and PDE, 2024. 4, 6, 21
\end{itemize}
\begin{itemize}
\item[] [26] H. Fang and X. Fu, On the construction of a complete Kähler-Einstein metric with negative scalar curvature near an isolated log-canonical singularity, Proc. Amer. Math. Soc., 149 (2021), pp. 3965-3976. 2
\item[] [27] P. Griffiths and J. Harris, Principles of algebraic geometry, Pure and Applied Mathematics, Wiley-Interscience [John Wiley \& Sons], New York, 1978. 10, 19
\item[] [28] V. Guedj and A. Zeriahi, The weighted Monge-Ampère energy of quasiplurisubharmonic functions, J. Funct. Anal., 250 (2007), pp. 442-482. 12, 23
\item[] [29] \_\_\_\_, Degenerate complex Monge-Ampère equations, vol. 26 of EMS Tracts in Mathematics, European Mathematical Society (EMS), Zürich, 2017. 8
\item[] [30] H. Guenancia, Kähler-Einstein metrics with cone singularities on klt pairs, Internat. J. Math., 24 (2013), pp. 1350035, 19. 3
\item[] [31] \_\_\_\_, Kähler-Einstein metrics: from cones to cusps, J. Reine Angew. Math., 759 (2020), pp. 1-27. 2, 3
\item[] [32] H. Guenancia and M. Păun, Conic singularities metrics with prescribed Ricci curvature: general cone angles along normal crossing divisors, J. Differential Geom., 103 (2016), pp. 15-57. 3, 20
\item[] [33] H. Guenancia and D. Wu, On the boundary behavior of Kähler-Einstein metrics on log canonical pairs, Math. Ann., 366 (2016), pp. 101-120. 2, 3
\item[] [34] T. Jeffres, R. Mazzeo, and Y. A. Rubinstein, Kähler-Einstein metrics with edge singularities, Ann. of Math. (2), 183 (2016), pp. 95-176. 3
\item[] [35] R. Kobayashi, Kähler-Einstein metric on an open algebraic manifold, Osaka J. Math., 21 (1984), pp. 399-418. 1, 2, 19
\item[] [36] S. KoŁodziej, The complex Monge-Ampère equation, Acta Math., 180 (1998), pp. 69-117. 3
\item[] [37] \_\_\_\_, The complex Monge-Ampère equation and pluripotential theory, Mem. Amer. Math. Soc., 178 (2005), pp. x+64. 11
\item[] [38] C. Li and S. Sun, Conical Kähler-Einstein metrics revisited, Comm. Math. Phys., 331 (2014), pp. 927-973. 3
\item[] [39] N. Mok and S.-T. Yau, Completeness of the Kähler-Einstein metric on bounded domains and the characterization of domains of holomorphy by curvature conditions, in The mathematical heritage of Henri Poincaré, Part 1 (Bloomington, Ind., 1980), vol. 39 of Proc. Sympos. Pure Math., Amer. Math. Soc., Providence, RI, 1983, pp. 41-59. 1
\item[] [40] Y. T. Siu, Lectures on Hermitian-Einstein metrics for stable bundles and Kähler-Einstein metrics, vol. 8 of DMV Seminar, Birkhäuser Verlag, Basel, 1987. 17, 18
\end{itemize}
\begin{itemize}
\item[] [41] G. Székelyhidi, A remark on conical Kähler-Einstein metrics, Math. Res. Lett., 20 (2013), pp. 581-590. 3
\item[] [42] G. Tian and S.-T. Yau, Existence of Kähler-Einstein metrics on complete Kähler manifolds and their applications to algebraic geometry, in Mathematical aspects of string theory (San Diego, Calif., 1986), vol. 1 of Adv. Ser. Math. Phys., World Sci. Publishing, Singapore, 1987, pp. 574-628. 1, 2, 15
\item[] [43] V. Tosatti, A general Schwarz lemma for almost-Hermitian manifolds, Comm. Anal. Geom., 15 (2007), pp. 1063-1086. 14, 15
\item[] [44] N. S. Trudinger, Fully nonlinear, uniformly elliptic equations under natural structure conditions, Trans. Amer. Math. Soc., 278 (1983), pp. 751-769. 18
\item[] [45] X.-J. Wang and Y. Wu, A new proof for the regularity of Monge-Ampère type equations, J. Differential Geom., 116 (2020), pp. 543-553. 18
\item[] [46] D. Wu, Kähler-Einstein metrics of negative Ricci curvature on general quasi-projective manifolds, Comm. Anal. Geom., 16 (2008), pp. 395-435. 2
\item[] [47] D. Wu and S.-T. Yau, Invariant metrics on negatively pinched complete Kähler manifolds, J. Amer. Math. Soc., 33 (2020), pp. 103-133. 2
\item[] [48] S. T. Yau, A general Schwarz lemma for Kähler manifolds, Amer. J. Math., 100 (1978), pp. 197-203. 1, 14, 15
\item[] [49] \_\_\_\_, On the Ricci curvature of a compact Kähler manifold and the complex Monge-Ampère equation. I, Comm. Pure Appl. Math., 31 (1978). 3
\end{itemize}

Quang-Tuan Dang, The Abdus Salam International Centre for Theoretical Physics (ICTP), Str.
Costiera, 11, 34151 Trieste, TS, Italy
E-mail address: qdang@ictp.it

Duc-Viet Vu, University of Cologne, Division of Mathematics, Department of Mathematics and Computer Science, Weyertal 86-90, 50931, Köln, Germany
E-mail address: dvu@uni-koeln.de