---
retention_scope: session
part: 2
total_parts: 3
---

[Part 2/3 of: SMOOTH YAMABE INVARIANT AND SURGERY]

If we write this equation in terms of the metric $g_{\mathrm{WS}}$ we get a perturbed version of the Yamabe equation for $g_{\mathrm{WS}}$. We assume that we have a smooth positive solution $u$ of the equation
$$L^{g_{\mathrm{WS}}} u=a \Delta^{g_{\mathrm{WS}}} u+\mathrm{Scal}^{g_{\mathrm{WS}}} u=\mu u^{p-1}+d^{*} A(d u)+X u+\epsilon \partial_{t} u-s u$$
where $s, \epsilon \in C^{\infty}(P), A \in \operatorname{End}\left(T^{*} P\right)$, and $X \in \Gamma(T P)$ are perturbation terms coming from the difference between $G$ and $g_{\text {WS }}$. We assume that the endomorphism $A$ is symmetric and that $X$ and $A$ are vertical, that is $d t(X)=0$ and $A(d t)=0$.

Theorem 5.2. Assume that $P$ carries a metric $g_{\mathrm{WS}}$ of the form (14). Let $\alpha, \beta \in \mathbb{R}$ be such that $[\alpha, \beta] \subset I$. Assume further that for each $t \in I$ either condition $\left(A_{t}\right)$ or condition $\left(B_{t}\right)$ is true. We also assume that $u$ is a positive solution of (17) satisfying
$$\mu\|u\|_{L^{\infty}(P)}^{p-2} \leq \frac{(n-k-2)^{2}(n-1)}{8(n-2)} .$$
Then there exists $c_{0}>0$ independent of $\alpha, \beta$, and $\varphi$, such that if
$$\|A\|_{L^{\infty}(P)},\|X\|_{L^{\infty}(P)},\|s\|_{L^{\infty}(P)},\|\epsilon\|_{L^{\infty}(P)},\left\|e\left(h_{t}\right)\right\|_{L^{\infty}(P)} \leq c_{0}$$
then
$$\int_{\pi^{-1}((\alpha+\gamma, \beta-\gamma))} u^{2} d v^{g_{\mathrm{WS}}} \leq \frac{4\|u\|_{L^{\infty}}^{2}}{n-k-2}\left(\operatorname{Vol}^{g_{\alpha}}\left(F_{\alpha}\right)+\operatorname{Vol}^{g_{\beta}}\left(F_{\beta}\right)\right)$$
where $\gamma:=\frac{\sqrt{32}}{n-k-2}$.
Note that this theorem only gives information when $\beta-\alpha>2 \gamma$.
5.2. Proof of Theorem 5.2. For the proof of Theorem 5.2 we need the following lemma.

Lemma 5.3. Let $T$ and $\gamma$ be positive numbers, and assume that $w:[-T-$ $\gamma, T+\gamma] \rightarrow \mathbb{R}$ is a smooth positive function satisfying
$$w^{\prime \prime}(t) \geq \frac{w(t)}{\gamma^{2}} .$$
Then
$$\int_{-T}^{T} w(t)^{m} d t \leq \frac{\gamma}{m}\left((w(T+\gamma))^{m}+(w(-T-\gamma))^{m}\right)$$
for all $m \geq 1$.
Proof. Assume that $\left.w\right|_{[-T-\gamma, T+\gamma]}$ attains its minimum at $t_{0}$. Since $w^{\prime \prime} \geq w / \gamma^{2}>0$ we have $w^{\prime}(t)>0$ for $t \in\left(t_{0}, T+\gamma\right)$, and $w^{\prime}(t)<0$ for $t \in\left(-T-\gamma, t_{0}\right)$. We first study the case when $t_{0} \in(-T, T)$. We define
$W(t):=w(t)+\gamma w^{\prime}(t)$. As $w$ and $w^{\prime}$ are increasing on $\left(t_{0}, T+\gamma\right)$, we get
$$\begin{aligned}
W(T) & =w(T)+\int_{T}^{T+\gamma} w^{\prime}(T) d t \\
& \leq w(T)+\int_{T}^{T+\gamma} w^{\prime}(t) d t \\
& =w(T+\gamma)
\end{aligned}$$
From (19) we see that $W^{\prime}(t) \geq W(t) / \gamma$, or $\partial_{t} \ln W(t) \geq 1 / \gamma$. Integrating this relation between $t \in\left(t_{0}, T\right)$ and $T$ we get
$$W(t) \leq e^{-\frac{T-t}{\gamma}} W(T) .$$
Using that $w \leq W$ on $\left(t_{0}, T\right)$ together with (21) we obtain
$$w(t) \leq W(t) \leq e^{-\frac{T-t}{\gamma}} w(T+\gamma),$$
and hence
$$w(t)^{m} \leq e^{-m \frac{T-t}{\gamma}}(w(T+\gamma))^{m}$$
for all $t \in\left[t_{0}, T\right]$ and $m \geq 1$. Integrating this relation over $t \in\left[t_{0}, T\right]$ we get
$$\int_{t_{0}}^{T} w(t)^{m} d t \leq \frac{\gamma\left(1-e^{-m \frac{T-t_{0}}{\gamma}}\right)}{m}(w(T+\gamma))^{m} \leq \frac{\gamma}{m}(w(T+\gamma))^{m} .$$
Similarly we conclude that
$$\int_{-T}^{t_{0}} w(t)^{m} d t \leq \frac{\gamma}{m}(w(-T-\gamma))^{m} .$$
This proves relation (20) in this case. In the case that $t_{0} \leq-T$ relation (22) remains valid. Using
$$\int_{-T}^{T} w(t)^{m} d t \leq \int_{t_{0}}^{T} w(t)^{m} d t$$
and
$$(w(T+\gamma))^{m} \leq(w(T+\gamma))^{m}+(w(-T-\gamma))^{m},$$
we obtain relation (20). We proceed in a similar way using (23) in case $t_{0} \geq T$. This ends the proof of Lemma 5.3. \(\square\)

Proof of Theorem 5.2. The Laplacian $\Delta^{g_{\mathrm{WS}}}$ on $P$ is related to the Laplacian $\Delta^{g_{t}}$ on $F_{t}$ through the formula
$$\Delta^{g_{\mathrm{WS}}}=\Delta^{g_{t}}-\partial_{t}^{2}+(n-1) H_{t} \partial_{t},$$
so
$$\begin{aligned}
\int_{F_{t}} u \Delta^{g_{\mathrm{WS}}} u d v^{g_{t}} & =\int_{F_{t}}\left(u \Delta^{g_{t}} u-u\left(\partial_{t}^{2} u\right)+(n-1) H_{t} u\left(\partial_{t} u\right)\right) d v^{g_{t}} \\
& =\int_{F_{t}}\left(\left|d_{\mathrm{vert}} u\right|^{2}-u\left(\partial_{t}^{2} u\right)+(n-1) H_{t} u\left(\partial_{t} u\right)\right) d v^{g_{t}} .
\end{aligned}$$

Together with (17) we get
$$\begin{aligned}
a \int_{F_{t}} u \partial_{t}^{2} u d v^{g_{t}}= & \int_{F_{t}}\left(a\left|d_{\mathrm{vert}} u\right|^{2}+a(n-1) H_{t} u \partial_{t} u\right. \\
& -\left\langle d_{\mathrm{vert}} u, A\left(d_{\mathrm{vert}} u\right)\right\rangle-u X u-\epsilon u \partial_{t} u \\
& \left.+\left(\text { Scal }{ }^{g_{\mathrm{WS}}}+s\right) u^{2}-\mu u^{p}\right) d v^{g_{t}} .
\end{aligned}$$
In the following we denote by $\delta\left(c_{0}\right)$ a positive constant that goes to 0 if $c_{0}$ tends to 0 and whose convergence depends only on $n, \mu$, and $h$. We set $S_{t}:=\inf _{F_{t}} \operatorname{Scal}^{g_{\mathrm{WS}}}$. If we use the inequality $2 \int|a b| \leq \int\left(a^{2}+b^{2}\right)$ to simplify the terms involving $X$ and $\epsilon$ we obtain
$$\begin{aligned}
a \int_{F_{t}} u \partial_{t}^{2} u d v^{g_{t}} \geq \int_{F_{t}} & \left(\left(a-\delta\left(c_{0}\right)\right)\left|d_{\mathrm{vert}} u\right|^{2}+a(n-1) H_{t} u \partial_{t} u\right. \\
& \left.-\delta\left(c_{0}\right)\left(\partial_{t} u\right)^{2}+\left(S_{t}-\delta\left(c_{0}\right)\right) u^{2}-\mu u^{p}\right) d v^{g_{t}}
\end{aligned}$$
If $c_{0}$ is small enough so that $a-\delta\left(c_{0}\right)>0$ we conclude that
$$\begin{aligned}
a \int_{F_{t}}\left(u \partial_{t}^{2} u-(n-1) H_{t} u\left(\partial_{t} u\right)\right) d v^{g_{t}} \geq & \left(S_{t}-\delta\left(c_{0}\right)\right) w(t)^{2} \\
& -\int_{F_{t}}\left(\delta\left(c_{0}\right)\left(\partial_{t} u\right)^{2}+\mu u^{p}\right) d v^{g_{t}}
\end{aligned}$$
where we define
$$w(t):=\|u\|_{L^{2}\left(F_{t}\right)}=\left(\int_{F_{t}} u^{2} d v^{g_{t}}\right)^{1 / 2} .$$
Differentiating this we get
$$\begin{aligned}
2 w^{\prime}(t) w(t) & =\partial_{t} \int_{F_{t}} u^{2} d v^{g_{t}} \\
& =\int_{F_{t}}\left(2 u\left(\partial_{t} u\right)-(n-1) H_{t} u^{2}\right) d v^{g_{t}}
\end{aligned}$$

We now assume that $\left(A_{t}\right)$ holds. Then (15) tells us that
$$H_{t}=-\frac{k}{n-1} \varphi^{\prime}(t),$$
so (25) becomes
$$w^{\prime}(t) w(t)=\int_{F_{t}} u\left(\partial_{t} u\right) d v^{g_{t}}+\frac{k}{2} \varphi^{\prime}(t) w(t)^{2} .$$

We differentiate this and obtain
$$\begin{aligned}
w^{\prime}(t)^{2}+w^{\prime \prime}(t) w(t)= & \int_{F_{t}}\left(\partial_{t} u\right)^{2} d v^{g_{t}} \\
& +\int_{F_{t}}\left(u \partial_{t}^{2} u-(n-1) H_{t} u \partial_{t} u\right) d v^{g_{t}} \\
& +\frac{k}{2} \varphi^{\prime \prime}(t) w(t)^{2}+k \varphi^{\prime}(t) w^{\prime}(t) w(t)
\end{aligned}$$
From (24) we get
$$\begin{aligned}
w^{\prime}(t)^{2}+w^{\prime \prime}(t) w(t) \geq & \left(1-\frac{\delta\left(c_{0}\right)}{a}\right) \int_{F_{t}}\left(\partial_{t} u\right)^{2} d v^{g_{t}} \\
& +\left(\frac{1}{a}\left(S_{t}-\delta\left(c_{0}\right)\right)+\frac{k}{2} \varphi^{\prime \prime}(t)\right) w(t)^{2} \\
& -\frac{1}{a} \int_{F_{t}} \mu u^{p} d v^{g_{t}}+k \varphi^{\prime}(t) w^{\prime}(t) w(t) .
\end{aligned}$$
We now use Cauchy-Schwarz and (26) to get
$$\begin{aligned}
w(t)^{2} \int_{F_{t}}\left(\partial_{t} u\right)^{2} d v^{g_{t}} & \geq\left(\int_{F_{t}} u\left(\partial_{t} u\right) d v^{g_{t}}\right)^{2} \\
& =\left(w^{\prime}(t) w(t)-\frac{k}{2} \varphi^{\prime}(t) w(t)^{2}\right)^{2},
\end{aligned}$$
and thus
$$\int_{F_{t}}\left(\partial_{t} u\right)^{2} d v^{g_{t}} \geq\left(w^{\prime}(t)-\frac{k}{2} \varphi^{\prime}(t) w(t)\right)^{2} .$$
From assumption (18) it follows that
$$\frac{\mu}{a} \int_{F_{t}} u^{p} d v^{g_{t}} \leq \frac{(n-k-2)^{2}}{32} w(t)^{2} .$$
Inserting (28) and (29) into (27) we obtain
$$\begin{aligned}
w^{\prime}(t)^{2}+w^{\prime \prime}(t) w(t) \geq & \left(1-\frac{\delta\left(c_{0}\right)}{a}\right)\left(w^{\prime}(t)-\frac{k}{2} \varphi^{\prime}(t) w(t)\right)^{2} \\
& +\left(\frac{1}{a}\left(S_{t}-\delta\left(c_{0}\right)\right)+\frac{k}{2} \varphi^{\prime \prime}(t)\right) w(t)^{2} \\
& -\frac{(n-k-2)^{2}}{32} w(t)^{2}+k \varphi^{\prime}(t) w^{\prime}(t) w(t),
\end{aligned}$$
or after some rearranging,
$$\begin{aligned}
w^{\prime \prime}(t) w(t) \geq & -\frac{\delta\left(c_{0}\right)}{a}\left(w^{\prime}(t)-\frac{k}{2} \varphi^{\prime}(t) w(t)\right)^{2} \\
& +\left(\frac{1}{a}\left(S_{t}-\delta\left(c_{0}\right)\right)+\frac{k}{2} \varphi^{\prime \prime}(t)+\frac{k^{2}}{4} \varphi^{\prime}(t)^{2}-\frac{(n-k-2)^{2}}{32}\right) w(t)^{2} .
\end{aligned}$$

Next we estimate the coefficient of $w(t)^{2}$ in the last line of (30). We denote this coefficient by $D$. Using (16) and assumption 1.) of $\left(A_{t}\right)$, which tells us that $e\left(h_{t}\right)=0$, we get
$$\begin{aligned}
D= & \frac{1}{a}\left(e^{-2 \varphi(t)} \inf _{x \in W} \operatorname{Scal}^{h_{t}}(x)-k(k+1) \varphi^{\prime}(t)^{2}-2 k \varphi^{\prime \prime}(t)+(n-k-1)(n-k-2)\right) \\
& -\frac{\delta\left(c_{0}\right)}{a}+\frac{k}{2} \varphi^{\prime \prime}(t)+\frac{k^{2}}{4} \varphi^{\prime}(t)^{2}-\frac{(n-k-2)^{2}}{32} \\
= & \frac{1}{a} e^{-2 \varphi(t)} \inf _{x \in W} \operatorname{Scal}^{h_{t}}(x)+\frac{1}{a}\left((n-k-1)(n-k-2)-\delta\left(c_{0}\right)\right)+\frac{k}{2(n-1)} \varphi^{\prime \prime}(t) \\
& -\frac{k}{4(n-1)}(n-k-2) \varphi^{\prime}(t)^{2}-\frac{(n-k-2)^{2}}{32} .
\end{aligned}$$
From assumptions 2.) and 3.) of $\left(A_{t}\right)$ we obtain
$$\begin{aligned}
D \geq & -\frac{n-k-2}{32}+\frac{1}{a}\left((n-k-1)(n-k-2)-\delta\left(c_{0}\right)\right)+\frac{k}{2(n-1)} \varphi^{\prime \prime}(t) \\
& -\frac{k}{4(n-1)}(n-k-2)-\frac{(n-k-2)^{2}}{32} \\
= & \frac{1}{4(n-1)}\left((n-1)(n-k-2)^{2}+2 k \varphi^{\prime \prime}(t)\right) \\
& -\frac{n-k-2}{32}-\frac{(n-k-2)^{2}}{32}-\frac{\delta\left(c_{0}\right)}{a} .
\end{aligned}$$
Using assumption 4.) of $\left(A_{t}\right)$ and $n-k-2 \geq 1$ we further obtain
$$\begin{aligned}
D \geq & \frac{1}{4(n-1)}\left(\frac{1}{2}(n-1)(n-k-2)^{2}\right) \\
& -\frac{(n-k-2)^{2}}{32}-\frac{(n-k-2)^{2}}{32}-\frac{\delta\left(c_{0}\right)}{a} \\
& =\frac{(n-k-2)^{2}}{16}-\frac{\delta\left(c_{0}\right)}{a} .
\end{aligned}$$
Inserting this in (30) we get
$$\begin{aligned}
w^{\prime \prime}(t) w(t) \geq & -\frac{\delta\left(c_{0}\right)}{a}\left(w^{\prime}(t)-\frac{k}{2} \varphi^{\prime}(t) w(t)\right)^{2} \\
& +\left(\frac{(n-k-2)^{2}}{16}-\frac{\delta\left(c_{0}\right)}{a}\right) w(t)^{2} \\
\geq & -\frac{2 \delta\left(c_{0}\right)}{a} w^{\prime}(t)^{2} \\
& +\left(-\frac{2 \delta\left(c_{0}\right)}{a} \frac{k^{2}}{4} \varphi^{\prime}(t)^{2}+\frac{(n-k-2)^{2}}{16}-\frac{\delta\left(c_{0}\right)}{a}\right) w(t)^{2},
\end{aligned}$$
where we also used the elementary inequality $(a-b)^{2} \leq 2 a^{2}+2 b^{2}$. Again using assumption 3.) of $\left(A_{t}\right)$ we conclude
$$\begin{aligned}
w^{\prime \prime}(t) w(t) \geq & -\frac{2 \delta\left(c_{0}\right)}{a} w^{\prime}(t)^{2} \\
& +\left(\frac{(n-k-2)^{2}}{16}-\frac{\delta\left(c_{0}\right)}{a}\left(1+\frac{k^{2}}{2}\right)\right) w(t)^{2} .
\end{aligned}$$
Fix a small positive number $\hat{\delta}$. Choose $c_{0}$ small so that $\delta\left(c_{0}\right)$ is also small. Then (31) tells us that
$$w^{\prime \prime}(t) w(t) \geq \frac{(n-k-2)^{2}}{32} w(t)^{2}-\hat{\delta} w^{\prime}(t)^{2} .$$
Define $v(t):=w(t)^{1+\hat{\delta}}$. This function satisfies
$$\begin{aligned}
v^{\prime \prime}(t) & =(1+\hat{\delta}) w^{\prime \prime}(t) w(t)^{\hat{\delta}}+\hat{\delta}(1+\hat{\delta}) w^{\prime}(t)^{2} w(t)^{\hat{\delta}-1} \\
& \geq(1+\hat{\delta}) \frac{(n-k-2)^{2}}{32} w(t)^{1+\hat{\delta}} \\
& \geq \frac{(n-k-2)^{2}}{32} v(t) .
\end{aligned}$$

Next we assume that $\left(B_{t}\right)$ holds. Then (15) becomes
$$H_{t}=-e\left(h_{t}\right),$$
and from (25) we get
$$w^{\prime}(t) w(t)=\int_{F_{t}}\left(u\left(\partial_{t} u\right)+\frac{n-1}{2} e\left(h_{t}\right) u^{2}\right) d v^{g_{t}} .$$
Differentiating this we get
$$\begin{aligned}
w^{\prime}(t)^{2}+w^{\prime \prime}(t) w(t)= & \int_{F_{t}}\left(\left(\partial_{t} u\right)^{2}+(n-1) e\left(h_{t}\right) u \partial_{t} u\right. \\
& \left.+\left(\frac{(n-1)^{2}}{2} e\left(h_{t}\right)^{2}+\frac{n-1}{2} \partial_{t} e\left(h_{t}\right)\right) u^{2}\right) d v^{g_{t}} \\
& +\int_{F_{t}}\left(u \partial_{t}^{2} u-(n-1) H_{t} u \partial_{t} u\right) d v^{g_{t}} .
\end{aligned}$$

Next we use (24) followed by assumptions 2.) and 3.) of $\left(B_{t}\right)$ to obtain
$$\begin{aligned}
w^{\prime}(t)^{2}+w^{\prime \prime}(t) w(t) \geq & \int_{F_{t}}\left(\left(\partial_{t} u\right)^{2}+(n-1) e\left(h_{t}\right) u \partial_{t} u\right. \\
& +\left(\frac{(n-1)^{2}}{2} e\left(h_{t}\right)^{2}+\frac{n-1}{2} \partial_{t} e\left(h_{t}\right)\right) u^{2} \\
& \left.-\frac{\delta\left(c_{0}\right)}{a}\left(\partial_{t} u\right)^{2}-\frac{\mu}{a} u^{p}\right) d v^{g_{t}} \\
& +\frac{1}{a}\left(S_{t}-\delta\left(c_{0}\right)\right) w(t)^{2} \\
\geq & \int_{F_{t}}\left(\left(1-\frac{\delta\left(c_{0}\right)}{a}\right)\left(\partial_{t} u\right)^{2}+(n-1) e\left(h_{t}\right) u \partial_{t} u-\frac{\mu}{a} u^{p}\right) d v^{g_{t}} \\
& +\left(\frac{1}{2 a}(n-k-1)(n-k-2)-\frac{3}{64}(n-k-2)-\frac{\delta\left(c_{0}\right)}{a}\right) w(t)^{2}
\end{aligned}$$
From (29) we further get, using $k \leq n-3$ in the last step,
$$\begin{aligned}
w^{\prime}(t)^{2}+w^{\prime \prime}(t) w(t) \geq & \int_{F_{t}}\left(\left(1-\frac{\delta\left(c_{0}\right)}{a}\right)\left(\partial_{t} u\right)^{2}+(n-1) e\left(h_{t}\right) u \partial_{t} u\right) d v^{g_{t}} \\
& +\left(\frac{1}{2 a}(n-k-1)(n-k-2)-\frac{3}{64}(n-k-2)\right. \\
& \left.-\frac{1}{32}(n-k-2)^{2}-\frac{\delta\left(c_{0}\right)}{a}\right) w(t)^{2} \\
\geq & \int_{F_{t}}\left(\left(1-\frac{\delta\left(c_{0}\right)}{a}\right)\left(\partial_{t} u\right)^{2}+(n-1) e\left(h_{t}\right) u \partial_{t} u\right) d v^{g_{t}} \\
& +\left(\frac{1}{32}(n-k-2)(n-k-3 / 2)-\frac{\delta\left(c_{0}\right)}{a}\right) w(t)^{2} \\
\geq & \int_{F_{t}}\left(\left(1-\frac{\delta\left(c_{0}\right)}{a}\right)\left(\partial_{t} u\right)^{2}+(n-1) e\left(h_{t}\right) u \partial_{t} u\right) d v^{g_{t}} \\
& +\left(\frac{1}{32}(n-k-2)^{2}+\frac{1}{64}-\frac{\delta\left(c_{0}\right)}{a}\right) w(t)^{2} .
\end{aligned}$$

We set $E_{t}:=\sup _{F_{t}}\left|e\left(h_{t}\right)\right|$ and use (33) to compute
$$\begin{aligned}
w(t)^{2} \int_{F_{t}}\left(\partial_{t} u\right)^{2} d v^{g_{t}} \geq & \left(\int_{F_{t}} u\left(\partial_{t} u\right) d v^{g_{t}}\right)^{2} \\
= & \left(w^{\prime}(t) w(t)-\frac{n-1}{2} \int_{F_{t}} e\left(h_{t}\right) u^{2} d v^{g_{t}}\right)^{2} \\
= & \left(w^{\prime}(t) w(t)\right)^{2}+\left(\frac{n-1}{2} \int_{F_{t}} e\left(h_{t}\right) u^{2} d v^{g_{t}}\right)^{2} \\
& -(n-1) w^{\prime}(t) w(t) \int_{F_{t}} e\left(h_{t}\right) u^{2} d v^{g_{t}} \\
\geq & w^{\prime}(t)^{2} w(t)^{2}-\left(\frac{n-1}{2}\right)^{2} E_{t}^{2} w(t)^{4} \\
& -(n-1)\left|w^{\prime}(t)\right| w(t) \int_{F_{t}}\left|e\left(h_{t}\right)\right| u^{2} d v^{g_{t}} \\
\geq & w^{\prime}(t)^{2} w(t)^{2}-\left(\frac{n-1}{2}\right)^{2} E_{t}^{2} w(t)^{4} \\
& -(n-1) E_{t}\left|w^{\prime}(t)\right| w(t)^{3}
\end{aligned}$$
Next we divide by $w(t)^{2}$ and obtain
$$\begin{aligned}
\int_{F_{t}}\left(\partial_{t} u\right)^{2} d v^{g_{t}} & \geq w^{\prime}(t)^{2}-\left(\frac{n-1}{2}\right)^{2} E_{t}^{2} w(t)^{2}-(n-1) E_{t}\left|w^{\prime}(t)\right| w(t) \\
& \geq w^{\prime}(t)^{2}-\left(\frac{n-1}{2}\right)^{2} E_{t}^{2} w(t)^{2}-\frac{n-1}{2} E_{t}\left(w^{\prime}(t)^{2}+w(t)^{2}\right) \\
& =\left(1-\frac{n-1}{2} E_{t}\right) w^{\prime}(t)^{2}-\left(\frac{n-1}{2} E_{t}+\left(\frac{n-1}{2}\right)^{2} E_{t}^{2}\right) w(t)^{2} .
\end{aligned}$$
Also
$$\begin{aligned}
\left|\int_{F_{t}} e\left(h_{t}\right) u \partial_{t} u d v^{g_{t}}\right| & \leq \int_{F_{t}}\left|e\left(h_{t}\right) u \partial_{t} u\right| d v^{g_{t}} \\
& \leq E_{t} \int_{F_{t}}\left|u \partial_{t} u\right| d v^{g_{t}} \\
& \leq \frac{1}{2} E_{t} \int_{F_{t}}\left(u^{2}+\left(\partial_{t} u\right)^{2}\right) d v^{g_{t}},
\end{aligned}$$
so
$$\int_{F_{t}}(n-1) e\left(h_{t}\right) u \partial_{t} u d v^{g_{t}} \geq-\frac{n-1}{2} E_{t} \int_{F_{t}}\left(u^{2}+\left(\partial_{t} u\right)^{2}\right) d v^{g_{t}} .$$
Fix a small number $\hat{\delta}>0$. We insert (35) and (36) in (34) and choose $c_{0}$ small enough so that $\delta\left(c_{0}\right)$ and $E_{t}$ are small. Then we get that $w(t)$
satisfies the same inequality (32) as we obtained under the assumption $\left(A_{t}\right)$. We have showed that in both cases $\left(A_{t}\right)$ and $\left(B_{t}\right)$ the function $v(t)=w(t)^{1+\hat{\delta}}$ satisfies
$$v^{\prime \prime}(t) \geq v(t) / \gamma^{2}$$
since $\frac{32}{(n-k-2)^{2}}=\gamma^{2}$.
Now we apply Lemma 5.3 to the function $\tilde{v}(t):=v\left(t+\frac{\beta+\alpha}{2}\right)$ with $T=\frac{\beta-\alpha}{2}-\gamma$ and $m=\frac{2}{1+\hat{\delta}}$. From this we obtain
$$\frac{\gamma}{m}\left((\tilde{v}(T+\gamma))^{m}+(\tilde{v}(-T-\gamma))^{m}\right) \geq \int_{-T}^{T} \tilde{v}^{m} d t .$$
With $s=t+\frac{\beta+\alpha}{2}$ we further have
$$\int_{-T}^{T} \tilde{v}^{m} d t=\int_{\alpha+\gamma}^{\beta-\gamma}(w(s))^{(1+\hat{\delta}) m} d t=\int_{\alpha+\gamma}^{\beta-\gamma} w^{2} d s$$
From the definition of $w$ we obtain
$$\int_{-T}^{T} \tilde{v}^{m} d t=\int_{\pi^{-1}((\alpha+\gamma, \beta-\gamma))} u^{2} d v^{g_{\mathrm{WS}}}$$
In addition, we have
$$\begin{aligned}
\left((\tilde{v}(T+\gamma))^{m}+(\tilde{v}(-T-\gamma))^{m}\right) & =\int_{F_{\alpha}} u^{2} d v^{g_{\alpha}}+\int_{F_{\beta}} u^{2} d v^{g_{\beta}} \\
& \leq\|u\|_{L^{\infty}(P)}^{2}\left(\operatorname{Vol}^{g_{\alpha}}\left(F_{\alpha}\right)+\operatorname{Vol}^{g_{\beta}}\left(F_{\beta}\right)\right) .
\end{aligned}$$
Choosing $\hat{\delta}$ small we may assume $m \geq \sqrt{2}$. This together with (37) and $\gamma=\frac{\sqrt{32}}{n-k-2}$ gives us
$$\int_{\pi^{-1}((\alpha+\gamma, \beta-\gamma))} u^{2} d v^{g_{\mathrm{WS}}} \leq \frac{4\|u\|_{L^{\infty}}^{2}}{n-k-2}\left(\operatorname{Vol}^{g_{\alpha}}\left(F_{\alpha}\right)+\operatorname{Vol}^{g_{\beta}}\left(F_{\beta}\right)\right) .$$
This proves Theorem 5.2. \(\square\)

\section*{6. Proof of Theorem 1.3}
6.1. Stronger version of Theorem 1.3. In this section we prove the following Theorem 6.1. By taking the supremum over all conformal classes Theorem 6.1 implies Theorem 1.3.

Theorem 6.1. Suppose that $\left(M_{1}, g_{1}\right)$ and $\left(M_{2}, g_{2}\right)$ are compact Riemannian manifolds of dimension $n$. Let $N$ be obtained from $M_{1}, M_{2}$, by a connected sum along $W$ as described in Section 2. Then there is
a family of metrics $g_{\theta}, \theta \in\left(0, \theta_{0}\right)$ on $N$ satisfying
$$\begin{aligned}
\min \left\{\mu\left(M_{1} \amalg M_{2}, g_{1} \amalg g_{2}\right), \Lambda_{n, k}\right\} & \leq \liminf _{\theta \searrow 0} \mu\left(N, g_{\theta}\right) \\
& \leq \limsup _{\theta \searrow 0} \mu\left(N, g_{\theta}\right) \\
& \leq \mu\left(M_{1} \amalg M_{2}, g_{1} \amalg g_{2}\right) .
\end{aligned}$$

In the following we define suitable metrics $g_{\theta}$, and then we show that they satisfy these inequalities.
6.2. Definition of the metrics $g_{\theta}$. We continue to use the notation of Section 2. In the following, $C$ denotes a constant that might change its value between lines. Recall that $(M, g)=\left(M_{1} \amalg M_{2}, g_{1} \amalg g_{2}\right)$. For $i=$ 1, 2 we define the metric $h_{i}$ as the restriction of $g_{i}$ to $W_{i}^{\prime}=w_{i}(W \times\{0\})$, and we set $h:=h_{1} \amalg h_{2}$ on $W^{\prime}=W_{1}^{\prime} \amalg W_{2}^{\prime}$. As already explained, the normal exponential map of $W^{\prime} \subset M$ defines a diffeomorphism
$$w_{i}: W \times B^{n-k}\left(R_{\max }\right) \rightarrow U_{i}\left(R_{\max }\right), \quad i=1,2,$$
which decomposes $U\left(R_{\text {max }}\right)=U_{1}\left(R_{\text {max }}\right) \amalg U_{2}\left(R_{\text {max }}\right)$ as a product $W^{\prime} \times$ $B^{n-k}\left(R_{\text {max }}\right)$.

In general, the Riemannian metric $g$ does not have a corresponding product structure, and we introduce an error term $T$ measuring the difference from the product metric. If $r$ denotes the distance function to $W^{\prime}$, then the metric $g$ can be written as
$$g=h+\xi^{n-k}+T=h+d r^{2}+r^{2} \sigma^{n-k-1}+T$$
on $U\left(R_{\text {max }}\right) \backslash W^{\prime} \cong W^{\prime} \times\left(0, R_{\text {max }}\right) \times S^{n-k-1}$. Here $T$ is a symmetric (2, 0)-tensor vanishing on $W^{\prime}$ (in the sense of sections of ( $T^{*} M \otimes$ $\left.T^{*} M\right)\left.\right|_{W^{\prime}}$ ). We also define the product metric
$$g^{\prime}:=h+\xi^{n-k}=h+d r^{2}+r^{2} \sigma^{n-k-1},$$
on $U\left(R_{\text {max }}\right) \backslash W^{\prime}$. Thus $g=g^{\prime}+T$. Since $T$ vanishes on $W^{\prime}$ we have for sufficiently small $r$
$$|T(X, Y)| \leq C r|X|_{g^{\prime}}|Y|_{g^{\prime}}$$
for any $X, Y \in T_{x} M$ where $x \in U\left(R_{\text {max }}\right)$. Since $T$ is smooth we have for sufficiently small $r$
$$\left|\left(\nabla_{U} T\right)(X, Y)\right| \leq C|X|_{g^{\prime}}|Y|_{g^{\prime}}|U|_{g^{\prime}},$$
and
$$\left|\left(\nabla_{U, V}^{2}\right) T(X, Y)\right| \leq C|X|_{g^{\prime}}|Y|_{g^{\prime}}|U|_{g^{\prime}}|V|_{g^{\prime}},$$
for $X, Y, U, V \in T_{x} M$. We define $T_{i}:=\left.T\right|_{M_{i}}$ for $i=1,2$.
For a fixed $R_{0} \in\left(0, R_{\text {max }}\right), R_{0}<1$, and sufficiently small in the sense of equation (40) and the following equations, we choose a smooth

Hierarchy of parameters
$$R_{\max }>R_{0}>\theta>\delta_{0}>\epsilon>0$$
We choose parameters in the order $R_{\text {max }}, R_{0}, \theta, \delta_{0}, A_{\theta}$. We then set
$$\begin{gathered}
\epsilon:=e^{-A_{\theta}} \delta_{0} . \\
\text { This implies }|t|=A_{\theta} \Leftrightarrow r_{i}=\delta_{0} .
\end{gathered}$$

\begin{figure}
\captionsetup{labelformat=empty}
\caption{Figure 2. Hierarchy of parameters}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/29267d81-b2bb-40b3-ab9a-5013c92ade0a-36.jpg?height=509&width=1026&top_left_y=822&top_left_x=577}
\end{figure}

Figure 3. The function $f$
positive function $F: M \backslash W^{\prime} \rightarrow \mathbb{R}$ such that
$$F(x)= \begin{cases}1, & \text { if } x \in M_{i} \backslash U_{i}\left(R_{\max }\right) ; \\ r_{i}(x)^{-1}, & \text { if } x \in U_{i}\left(R_{0}\right) \backslash W^{\prime} .\end{cases}$$
Next we choose small numbers $\theta, \delta_{0} \in\left(0, R_{0}\right)$ with $\theta>\delta_{0}>0$. Here "small" means that for a given small number $\theta$ we choose a number $\delta_{0}=\delta_{0}(\theta) \in(0, \theta)$ such that all arguments that need $\delta_{0}$ to be small will hold, see Figure 2. For any $\theta>0$ and sufficiently small $\delta_{0}$ there is $A_{\theta} \in\left(\theta^{-1},\left(\delta_{0}\right)^{-1}\right.$ ) and a family of smooth functions $f=f_{\theta, \delta_{0}}$ : $U\left(R_{\text {max }}\right) \rightarrow \mathbb{R}$ depending only on the coordinate $r$ such that
$$f(x)=\left\{\begin{array}{cl}
-\ln r(x), & \text { if } x \in U\left(R_{\max }\right) \backslash U(\theta) ; \\
\ln A_{\theta}, & \text { if } x \in U\left(\delta_{0}\right),
\end{array}\right.$$
and such that
$$\left|r \frac{d f}{d r}\right|=\left|\frac{d f}{d(\ln r)}\right| \leq 1, \quad \text { and } \quad\left\|r \frac{d}{d r}\left(r \frac{d f}{d r}\right)\right\|_{L^{\infty}}=\left\|\frac{d^{2} f}{d^{2}(\ln r)}\right\|_{L^{\infty}} \rightarrow 0$$
as $\theta \searrow 0$. See Figure 3.
We set $\epsilon=e^{-A_{\theta}} \delta_{0}$. We can and will assume that $\epsilon<1$.

Let $N$ be obtained from $M$ by a connected sum along $W$ with parameter $\epsilon$, as described in Section 2. In particular, $U_{\epsilon}^{N}(s)=(U(s) \backslash U(\epsilon)) / \sim$ for all $s \in\left[\epsilon, R_{\text {max }}\right]$. On the set $U_{\epsilon}^{N}\left(R_{\text {max }}\right)=\left(U\left(R_{\text {max }}\right) \backslash U(\epsilon)\right) / \sim$ we define the variable $t$ by
$$t:=\left\{\begin{aligned}
-\ln r_{1}+\ln \epsilon, & \text { on } U_{1}\left(R_{\max }\right) \backslash U_{1}(\epsilon) ; \\
\ln r_{2}-\ln \epsilon, & \text { on } U_{2}\left(R_{\max }\right) \backslash U_{2}(\epsilon) .
\end{aligned}\right.$$
Note that $t \leq 0$ on $U_{1}\left(R_{\text {max }}\right) \backslash U_{1}(\epsilon)$ and $t \geq 0$ on $U_{2}\left(R_{\text {max }}\right) \backslash U_{2}(\epsilon)$, with $t=0$ precisely on the common boundary $\partial U_{1}(\epsilon)$ identified with $\partial U_{2}(\epsilon)$ in $N$. It follows that
$$r_{i}=e^{|t|+\ln \epsilon}=\epsilon e^{|t|} .$$
We can arrange that $t: U_{\epsilon}^{N}\left(R_{\text {max }}\right) \rightarrow \mathbb{R}$ is smooth. Expressed in the variable $t$ we have
$$F(x)=\epsilon^{-1} e^{-|t|}$$
for $x \in U_{\epsilon}^{N}\left(R_{0}\right)$, or in other words if $|t|+\ln \epsilon \leq \ln R_{0}$. Then Equation (38) tells us that
$$F^{2} g=\epsilon^{-2} e^{-2|t|}(h+T)+d t^{2}+\sigma^{n-k-1}$$
on $U_{\epsilon}^{N}\left(R_{0}\right)$. If we view $f$ as a function of $t$, then
$$f(t)= \begin{cases}-|t|-\ln \epsilon, & \text { if } \ln \theta-\ln \epsilon \leq|t| \leq \ln R_{\max }-\ln \epsilon ; \\ \ln A_{\theta}, & \text { if }|t| \leq \ln \delta_{0}-\ln \epsilon ;\end{cases}$$
and $|d f / d t| \leq 1,\left\|d^{2} f / d t^{2}\right\|_{L^{\infty}} \rightarrow 0$ as $\theta$ tends to 0. We choose a cut-off function $\chi: \mathbb{R} \rightarrow[0,1]$ such that $\chi=0$ on $(-\infty,-1],|d \chi| \leq 1$, and $\chi=1$ on $[1, \infty)$. With these choices we define
$$g_{\theta}:= \begin{cases}F^{2} g_{i}, & \text { on } M_{i} \backslash U_{i}(\theta) ; \\
e^{2 f(t)}\left(h_{i}+T_{i}\right)+d t^{2}+\sigma^{n-k-1}, & \text { on } U_{i}(\theta) \backslash U_{i}\left(\delta_{0}\right) ; \\
\left.\begin{array}{l}
A_{\theta}^{2} \chi\left(t / A_{\theta}\right)\left(h_{2}+T_{2}\right) \\
+A_{\theta}^{2}\left(1-\chi\left(t / A_{\theta}\right)\right)\left(h_{1}+T_{1}\right) \\
+d t^{2}+\sigma^{n-k-1},
\end{array}\right\} & \text { on } U_{\epsilon}^{N}\left(\delta_{0}\right) .\end{cases}$$
On $U_{\epsilon}^{N}\left(R_{0}\right)$ we write $g_{\theta}$ as
$$g_{\theta}=e^{2 f(t)} \tilde{h}_{t}+d t^{2}+\sigma^{n-k-1}+\widetilde{T}_{t},$$
where the metric $\tilde{h}_{t}$ is defined by
$$\tilde{h}_{t}:=\chi\left(t / A_{\theta}\right) h_{2}+\left(1-\chi\left(t / A_{\theta}\right)\right) h_{1},$$
for $t \in \mathbb{R}$, and where the error term $\widetilde{T}_{t}$ is equal to
$$\widetilde{T}_{t}:=e^{2 f(t)}\left(\chi\left(t / A_{\theta}\right) T_{2}+\left(1-\chi\left(t / A_{\theta}\right)\right) T_{1}\right) .$$
See also Figure 4. On $U_{\epsilon}^{N}\left(R_{0}\right)$ we also define the metric without error term
$$g_{\theta}^{\prime}:=g_{\theta}-\widetilde{T}_{t}=e^{2 f(t)} \tilde{h}_{t}+d t^{2}+\sigma^{n-k-1} .$$

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/29267d81-b2bb-40b3-ab9a-5013c92ade0a-38.jpg?height=791&width=1170&top_left_y=410&top_left_x=439}
\captionsetup{labelformat=empty}
\caption{Figure 4. The metrics $g_{\theta}$. The horizontal direction in both drawings corresponds to the $t$-variable. The vertical direction in the upper drawing corresponds to the projection to $S^{n-k-1}$, and in the lower drawing it corresponds to the projection to $S^{k}$. In the lower drawing, the curved parts close to the middle part are not drawn realistically. Their curvature tends to 0 for $\theta \rightarrow 0$, and the middle becomes huge in this limit, and thus it would be too large for our picture.}
\end{figure}
An upper bound for the error term $\tilde{T}_{t}$ will be needed in the following. We claim that
$$|X|_{g^{\prime}} \leq C e^{-f(t)}|X|_{g_{\theta}^{\prime}}$$
for $X \in T_{x} N$, where $g^{\prime}$ is the metric defined by (39). To prove the claim, we decompose $X$ in a radial part, a part parallel to $W^{\prime}$, and a part parallel to $S^{n-k-1}$. This decomposition is orthogonal with respect to both $g^{\prime}$ and $g_{\theta}^{\prime}$. For $X=\frac{\partial}{\partial t}= \pm \epsilon e^{|t|} \frac{\partial}{\partial r}$ we have that $1=|X|_{g_{\theta}^{\prime}}$ and $|X|_{g^{\prime}}=\epsilon e^{|t|} \leq e^{-f(t)}$ since $f(t) \leq-|t|-\ln \epsilon$. The argument is similar if $X$ is parallel to $S^{n-k-1}$. If $X$ is tangent to $W^{\prime}$, then $|X|_{g}=|X|_{h} \leq C|X|_{\tilde{h}_{t}} \leq C e^{-f(t)}|X|_{g_{\theta}^{\prime}}$, and the claim follows.

The Relations (40) and (43) imply
$$\begin{aligned}
\left|\widetilde{T}_{t}(X, Y)\right| & \leq C e^{2 f(t)}|T(X, Y)| \\
& \leq C e^{2 f(t)} r|X|_{g^{\prime}}|Y|_{g^{\prime}} \\
& \leq C r|X|_{g_{\theta}^{\prime}}|Y|_{g_{\theta}^{\prime}}
\end{aligned}$$
for all $X, Y$. In other words this means
$$\left|\widetilde{T}_{t}\right|_{g_{\theta}^{\prime}} \leq C r=C \epsilon e^{|t|} \leq C e^{-f(t)} .$$
Further, one can calculate that
$$\left|\nabla \widetilde{T}_{t}\right|_{g_{\theta}^{\prime}} \leq C e^{-f(t)},$$
and
$$\left|\nabla^{2} \widetilde{T}_{t}\right|_{g_{\theta}^{\prime}} \leq C e^{-f(t)} .$$
Here ∇ denotes the Levi-Civita-connection with respect to $g_{\theta}^{\prime}$. In particular we see with Corollary A. 2
$$\mid \text { Scal }^{g_{\theta}}-\text { Scal }^{g_{\theta}^{\prime}} \mid \leq C e^{-f(t)} .$$
6.3. Geometric description of the new metrics. In this subsection we collect some facts about the geometry of $F^{2} g$ and $g_{\theta}^{\prime}$ introduced in the previous subsection. Most of the results are not needed for the proof of our result, but are useful to understand the underlying geometric concept of the argument. We will thus skip most of the proofs in this subsection.

The first proposition explains the special role of $\mathbb{H}^{k+1} \times \mathbb{S}^{n-k-1}$.
Proposition 6.2. Let $x_{i}$ be a sequence of points in $M \backslash W$, converging to $W$. Then the Riemann tensor of $F^{2} g$ at $x_{i}$ converges to the Riemann tensor of $\mathbb{H}^{k+1} \times \mathbb{S}^{n-k-1}$. The covariant derivative of the Riemann tensor of $F^{2} g$ converges to zero. For any fixed $R>0$ these convergences are uniform on balls (with respect to the metric $F^{2} g$ ) of radius $R$. In particular, for any fixed $R>0$ the balls $\left(B^{F^{2} g}\left(x_{i}, R\right), x_{i}, F^{2} g\right)$ converge to a ball of radius $R$ in $\mathbb{H}^{k+1} \times \mathbb{S}^{n-k-1}$ in the $C^{2, \alpha}$-topology of Riemannian manifolds with base point.

The $C^{2, \alpha}$-topology of Riemannian manifolds with base point has its origins in Cheeger's finiteness theorem [14] and in the work of Gromov [19], [20]. The article by Petersen [46, Pages 167-202] is a good introduction to the subject.

In the limit $r \searrow 0$ (or equivalently $t \rightarrow \infty$ ) the $W$-component of the metric $F^{2} g$ grows exponentially. The motivation for introducing the function $f$ into the definition of $g_{\theta}$ is to slow down this exponential growth: the diameter of the $W$-component with respect to $g_{\theta}$ is then bounded by $A_{\theta} \operatorname{diam}(W, g)$, where $\operatorname{diam}(W, g)$ is the diameter of $W$ with respect to $g$. This slowing down has to be done carefully in order to get nice limit spaces. The properties claimed for $f$ imply the following result.

Proposition 6.3. Let $\theta_{i}$ be a sequence of positive numbers tending to zero, and let $x_{i} \in U_{\epsilon}^{N}\left(R_{\text {max }}\right)$ be a sequence of points such that the limit $c:=\lim \left(\frac{\partial}{\partial t} f\right)\left(t\left(x_{i}\right)\right)$ exists. Then the Riemann tensor of $g_{\theta_{i}}$ at $x_{i}$ converges to the Riemann tensor of $\mathbb{H}_{c}^{k+1} \times \mathbb{S}^{n-k-1}$. The covariant
derivative of the Riemann tensor of $g_{\theta_{i}}$ converges to zero. For any fixed $R>0$ these convergences are uniform on balls (with respect to the metric $g_{\theta_{i}}$ ) of radius $R$. In particular, for any fixed $R>0$ the balls $\left(B^{g_{\theta_{i}}}\left(x_{i}, R\right), x_{i}, g_{\theta_{i}}\right)$ converge to a ball of radius $R$ in $\mathbb{H}_{c}^{k+1} \times \mathbb{S}^{n-k-1}$ in the $C^{2, \alpha}$-topology of Riemannian manifolds with base point.

From this proposition it follows that the balls $\left(B^{F^{2} g}\left(x_{i}, R\right), x_{i}, F^{2} g\right)$ converge to a ball of radius $R$ in $\mathbb{H}_{c}^{k+1} \times \mathbb{S}^{n-k-1}$ in the $C^{2, \alpha}$-topology of Riemannian manifolds with base point. Thus, we get an explanation why the spaces $\mathbb{H}_{c}^{k+1} \times \mathbb{S}^{n-k-1}$ appear as limit spaces.

The sectional curvature of $\mathbb{H}_{c}^{k+1}$ is $-c^{2}$. Hence the sectional curvatures of the product $\mathbb{H}_{c}^{k+1} \times \mathbb{S}^{n-k-1}$ are in the interval $\left[-c^{2}, 1\right]$. Using this fact we can prove the following Proposition.
Proposition 6.4. The scalar curvatures of $g_{\theta}$ and $g_{\theta}^{\prime}$ are bounded by a constant independent of $\theta$.
Proof. The metric $g_{\theta}^{\prime}$ is the metric of a $W S$-bundle. Hence (16) is valid. We calculate $\partial_{t} \tilde{h}_{t}=\left(1 / A_{\theta}\right) \chi^{\prime}\left(t / A_{\theta}\right)\left(h_{2}-h_{1}\right)$ and $\partial_{t}^{2} \tilde{h}_{t}=\left(1 / A_{\theta}\right)^{2} \chi^{\prime \prime}\left(t / A_{\theta}\right)\left(h_{2}-\right.$ $\left.h_{1}\right)$. This implies $\left|\operatorname{tr}^{\tilde{h}_{t}} \partial_{t} \tilde{h}_{t}\right| \leq C / A_{\theta},\left|\operatorname{tr}\left(\tilde{h}_{t}^{-1} \partial_{t} \tilde{h}_{t}\right)^{2}\right| \leq C / A_{\theta}^{2}$, and $\left|\operatorname{tr}^{\tilde{h}_{t}} \partial_{t}^{2} \tilde{h}_{t}\right| \leq C / A_{\theta}^{2}$. From (16) it follows that Scal ${ }^{g_{\theta}^{\prime}}$ is bounded. Equation (47) then implies that Scal ${ }^{g \theta}$ is bounded. \(\square\)

The geometry close to the gluing of $M_{1} \backslash U_{1}(\epsilon)$ with $M_{2} \backslash U_{2}(\epsilon)$ is described by the following simple proposition.
Proposition 6.5. Let $H$ be the metric on $W \times(-1,1)$ given by $\left(\chi(t) h_{2}+\right.$ $\left.(1-\chi(t)) h_{1}\right)+d t^{2}$. Then $\left(U_{\epsilon}^{N}\left(\delta_{0}\right), g_{\theta}^{\prime}\right)$ is isometric to $(W \times(-1,1) \times$ $\left.S^{n-k-1}, A_{\theta}^{2} H+\sigma^{n-k-1}\right)$.
6.4. Proof of Theorem 6.1. The metrics $g_{\theta}$ are defined for small $\theta>0$ as described above. In order to prove Theorem 6.1 it is sufficient to prove
$$\min \left\{\mu(M, g), \Lambda_{n, k}\right\} \leq \lim _{i \rightarrow \infty} \mu\left(N, g_{\theta_{i}}\right) \leq \mu(M, g)$$
for any sequence $\theta_{i} \searrow 0$ as $i \rightarrow \infty$ for which $\lim _{i \rightarrow \infty} \mu\left(N, g_{\theta_{i}}\right)$ exists. Recall that $(M, g)=\left(M_{1} \amalg M_{2}, g_{1} \amalg g_{2}\right)$.

The upper bound on $\lim _{i \rightarrow \infty} \mu\left(N, g_{\theta_{i}}\right)$ is easy to prove. The proof of the lower bound is more complicated, our arguments for this part are inspired by the compactness-concentration principle in analysis, see for example [17]. In the case of a concentration, we will use blow-up analysis in order to construct a non-trivial solution to the Yamabe equation on some limit space. Here we follow and generalize a similar construction of a blow-up limit in lecture notes by Schoen, see [53, Chapter V.2].

For each metric $g_{\theta}$ we have a solution of the Yamabe equation (5). We take a sequence of $\theta$ tending to 0. Following the compactness-concentration principle, this sequence of solutions can concentrate in
points or converge to a non-trivial solution or do both at the same time. The concentration in points can be used to construct a non-trivial solution on a sphere by blowing up the metrics.

In our situation we may have concentration in a fixed point (subcase I.1) or in a wandering point (subcase I.2), and we may have convergence to a non-trivial solution on the original manifold (subcase II.1.2) or in the attached part (subcases II.1.1 and II.2). In each of these cases we obtain a different lower bound for $\lim _{i \rightarrow \infty} \mu\left(N, g_{\theta_{i}}\right)$ : In the subcases I. 1 and I. 2 the lower bound is $\mu\left(\mathbb{S}^{n}\right)$, in subcase II.1.2 it is $\mu(M, g)$, and in the subcases II.1.1 and II. 2 we obtain $\Lambda_{n, k}^{(1)}$ and $\Lambda_{n, k}^{(2)}$ as lower bounds. Together these cases give the lower bound of Theorem 6.1.

The cases here are not exclusive. For example it is possible that the solutions may both concentrate in a point and converge to a non-trivial solution on the original manifold.

In our arguments we will often pass to subsequences. To avoid complicated notation we write $\theta \searrow 0$ for a sequence $\left(\theta_{i}\right)_{i \in \mathbb{N}}$ converging to zero, and we will pass successively to subsequences without changing notation. Similarly $\lim _{\theta \searrow 0} h(\theta)$ should be read as $\lim _{i \rightarrow \infty} h\left(\theta_{i}\right)$.

We set $\mu:=\mu(M, g)$ and $\mu_{\theta}:=\mu\left(N, g_{\theta}\right)$. From Theorem 1.1 we have
$$\mu, \mu_{\theta} \leq \mu\left(\mathbb{S}^{n}\right) .$$
After passing to a subsequence, the limit
$$\bar{\mu}:=\lim _{\theta \searrow 0} \mu_{\theta} \in\left[-\infty, \mu\left(\mathbb{S}^{n}\right)\right]$$
exists. Let $J:=J^{g}$ and $J_{\theta}:=J^{g_{\theta}}$ be defined as in (1).
We start with the easier part of the argument, namely with
$$\bar{\mu} \leq \mu .$$
For this let $\alpha>0$ be a small number. We choose a smooth cut-off function $\chi_{\alpha}$ on $M$ such that $\chi_{\alpha}=1$ on $M \backslash U(2 \alpha),\left|d \chi_{\alpha}\right| \leq 2 / \alpha$, and $\chi_{\alpha}=0$ on $U(\alpha)$. Let $u$ be a smooth non-zero function such that $J(u) \leq \mu+\delta$ where $\delta$ is a small positive number. On the support of $\chi_{\alpha}$ the metrics $g$ and $g_{\theta}$ are conformal since $g_{\theta}=F^{2} g$ and hence by (3) we have
$$\mu_{\theta} \leq J_{\theta}\left(\chi_{\alpha} F^{-\frac{n-2}{2}} u\right)=J\left(\chi_{\alpha} u\right)$$
for $\theta<\alpha$. It is straightforward to compute that $\lim _{\alpha \rtimes_{0}} J\left(\chi_{\alpha} u\right)=$ $J(u) \leq \mu+\delta$. From this Relation (49) follows.

Now we turn to the more difficult part of the proof, namely the inequality
$$\bar{\mu} \geq \min \left\{\mu, \Lambda_{n, k}\right\} .$$
In the case $\bar{\mu}=\mu\left(\mathbb{S}^{n}\right)$ this inequality follows trivially from (48). Hence we assume $\bar{\mu}<\mu\left(\mathbb{S}^{n}\right)$ in the following, which implies $\mu_{\theta}<\mu\left(\mathbb{S}^{n}\right)$ if $\theta$ is
sufficiently small. From Theorem 1.2 we know that there exist positive functions $u_{\theta} \in C^{2}(M)$ such that
$$L^{g_{\theta}} u_{\theta}=\mu_{\theta} u_{\theta}^{p-1},$$
and
$$\int_{N} u_{\theta}^{p} d v^{g_{\theta}}=1 .$$

We begin by proving a lemma that yields a bound of the $L^{2}$-norm of $u_{\theta}$ in terms of the $L^{\infty}$-norm. This result is non-trivial since $\operatorname{Vol}\left(N, g_{\theta}\right) \rightarrow$ $\infty$ as $\theta \searrow 0$.

Lemma 6.6. Assume that there exists $b>0$ such that
$$\mu_{\theta} \sup _{U_{\epsilon}^{N}(b)} u_{\theta}^{p-2} \leq \frac{(n-k-2)^{2}(n-1)}{8(n-2)}$$
for $\theta$ small enough. Then there exist constants $c_{1}, c_{2}>0$ independent of $\theta$ such that
$$\int_{N} u_{\theta}^{2} d v^{g_{\theta}} \leq c_{1}\left\|u_{\theta}\right\|_{L^{\infty}(N)}^{2}+c_{2}$$
for all sufficiently small $\theta$. In particular, if $\left\|u_{\theta}\right\|_{L^{\infty}(N)}$ is bounded, so is $\left\|u_{\theta}\right\|_{L^{2}(N)}$.

Proof. Let $\tilde{r} \in(0, b)$ be fixed and set $P=U(\tilde{r})$. Then $P$ is a $W S$ -bundle where, with the notation of Section 5, $I=(\alpha, \beta)$ with $\alpha=$ $-\ln \tilde{r}+\ln \epsilon$ and $\beta=\ln \tilde{r}-\ln \epsilon$. On $P$ we have two natural metrics: $g_{\theta}$ and $g_{\mathrm{WS}}=g_{\theta}^{\prime}=g_{\theta}-\widetilde{T}_{t}$. The metric $g_{\mathrm{WS}}$ has exactly the form (14) with $\varphi=f$ and $h_{t}=\tilde{h}_{t}$. Let $\theta$ be small enough and let $t \in(-\ln \tilde{r}+$ $\left.\ln \epsilon,-\ln \delta_{0}+\ln \epsilon\right) \cup\left(\ln \delta_{0}-\ln \epsilon, \ln \tilde{r}-\ln \epsilon\right)$. Then assumption $\left(A_{t}\right)$ of Theorem 5.2 is true. Now, again if $\theta$ is small enough, we have for all $t \in$ $\left(-\ln \delta_{0}+\ln \epsilon, \ln \delta_{0}-\ln \epsilon\right)$ the relation Scal ${ }^{g_{\mathrm{WS}}}=$ Scal $^{\sigma^{n-k-1}}+O\left(1 / A_{\theta}\right)$. The error term $e\left(\tilde{h}_{t}\right)$ from $\left(B_{t}\right)$ in this case satisfies
$$2(n-1)\left|e\left(\tilde{h}_{t}\right)\right| \leq\left|\operatorname{tr}^{\tilde{h}_{t}} \partial_{t} \tilde{h}_{t}\right|=\left|\operatorname{tr}^{\tilde{h}_{t}}\left(\chi^{\prime}\left(t / A_{\theta}\right) \frac{h_{2}-h_{1}}{A_{\theta}}\right)\right| \leq \frac{C}{A_{\theta}},$$
and
$$2(n-1)\left|\partial_{t} e\left(\tilde{h}_{t}\right)\right|=\left|\operatorname{tr}\left(\tilde{h}_{t}^{-1}\left(\partial_{t} \tilde{h}_{t}\right) \tilde{h}_{t}^{-1}\left(\partial_{t} \tilde{h}_{t}\right)\right)\right|+\left|\operatorname{tr}^{\tilde{h}_{t}} \partial_{t}^{2} \tilde{h}_{t}\right| \leq \frac{C}{A_{\theta}^{2}} .$$
Because of $1 / A_{\theta} \leq \theta$ condition $\left(B_{t}\right)$ is true. Equation (51) is written in the metric $g_{\theta}$. Using the expression of the Laplacian in local coordinates,
$$\Delta^{g_{\theta}} u=-\sum_{i, j}\left(\operatorname{det} g_{\theta}\right)^{-1 / 2} \partial_{i}\left(g_{\theta}^{i j}\left(\operatorname{det} g_{\theta}\right)^{1 / 2} \partial_{j} u\right),$$
one can check that if we write Equation (51) in the metric $g_{\mathrm{WS}}$ we obtain an equation of the form (17) with $\mu=\mu_{\theta}$. Together with (44), (45) and (47), one verifies that the error terms satisfy
$$|A(x)|_{g_{\mathrm{WS}}},|X(x)|_{g_{\mathrm{WS}}},|s(x)|_{g_{\mathrm{WS}}},|\epsilon(x)|_{g_{\mathrm{WS}}} \leq C e^{-f(t)},$$
where $|\cdot|_{g_{\mathrm{WS}}}$ denotes the pointwise norm at a point in $U_{\epsilon}^{N}\left(R_{0}\right)$, and where $C$ is a constant independent of $\theta$. In particular for any $c_{0}>0$, we obtain
$$|A(x)|_{g_{\mathrm{WS}}},|X(x)|_{g_{\mathrm{WS}}},|s(x)|_{g_{\mathrm{WS}}},\left|e\left(\tilde{h}_{t}\right)(x)\right|_{g_{\mathrm{WS}}},|\epsilon(x)|_{g_{\mathrm{WS}}} \leq c_{0}$$
on $U_{\epsilon}^{N}(\theta)$ for small $\theta$. These estimates allow us to apply Theorem 5.2. By the assumptions of Lemma 6.6, if $\tilde{r} \in(0, b)$ is small enough, Assumption (18) of Theorem 5.2 is true. Thus, all hypotheses of Theorem 5.2 hold for $\alpha:=-\ln \tilde{r}+\ln \epsilon, \beta:=\ln \tilde{r}-\ln \epsilon$, and hence
$$\int_{P^{\prime}} u_{\theta}^{2} d v^{g_{\mathrm{WS}}} \leq \frac{4\left\|u_{\theta}\right\|_{L^{\infty}}^{2}}{n-k-2}\left(\operatorname{Vol}^{g_{\alpha}}\left(F_{\alpha}\right)+\operatorname{Vol}^{g_{\beta}}\left(F_{\beta}\right)\right) .$$
where $P^{\prime}:=U_{\epsilon}^{N}\left(\tilde{r} e^{-\gamma}\right)$. Now observe that
$$C:=\frac{4}{n-k-2}\left(\operatorname{Vol}^{g_{\alpha}}\left(F_{\alpha}\right)+\operatorname{Vol}^{g_{\beta}}\left(F_{\beta}\right)\right)$$
does not depend on $\theta$ (since $F_{\alpha}$ and $F_{\beta}$ correspond to the hypersurface $r=\tilde{r})$. This implies that
$$\int_{P^{\prime}} u_{\theta}^{2} d v^{g_{\mathrm{WS}}} \leq C\left\|u_{\theta}\right\|_{L^{\infty}(N)}^{2}$$
where $C>0$ is independent of $\theta$. Since if $\tilde{r}$ is small enough, we clearly have
$$d v^{g_{\theta}} \leq 2 d v^{g_{\mathrm{WS}}},$$
and we obtain that
$$\int_{P^{\prime}} u_{\theta}^{2} d v^{g_{\theta}} \leq c_{1}\left\|u_{\theta}\right\|_{L^{\infty}(N)}^{2}$$
where $c_{1}:=2 C>0$ is independent of $\theta$. Now observe that $\operatorname{Vol}^{g_{\theta}}\left(N \backslash P^{\prime}\right)$ is bounded by a constant independent of $\theta$. Using the Hölder inequality we obtain
$$\begin{aligned}
\int_{N} u_{\theta}^{2} d v^{g_{\theta}} & =\int_{P^{\prime}} u_{\theta}^{2} d v^{g_{\theta}}+\int_{N \backslash P^{\prime}} u_{\theta}^{2} d v^{g_{\theta}} \\
& \leq c_{1}\left\|u_{\theta}\right\|_{L^{\infty}(N)}^{2}+\operatorname{Vol}^{g_{\theta}}\left(N \backslash P^{\prime}\right)^{\frac{2}{n}}\left(\int_{N \backslash P^{\prime}} u_{\theta}^{p} d v\right)^{\frac{n-2}{n}} .
\end{aligned}$$
Since $\left\|u_{\theta}\right\|_{L^{p}(N)}=1$, this proves Lemma 6.6 with $c_{1}$ as defined above and with $c_{2}:=\operatorname{Vol}^{g_{\theta}}\left(N \backslash P^{\prime}\right)^{\frac{2}{n}}$. For small $\theta$, the metric $\left.g_{\theta}\right|_{N \backslash P^{\prime}}$ is independent of $\theta$, and thus $c_{2}$ does not depend on $\theta$. \(\square\)

Corollary 6.7.
$$\liminf _{\theta \searrow 0}\left\|u_{\theta}\right\|_{L^{\infty}(N)}>0 .$$
Proof. We set $m_{\theta}:=\left\|u_{\theta}\right\|_{L^{\infty}(N)}$. In order to prove the corollary by contradiction we assume $\lim _{\theta \searrow 0} m_{\theta}=0$. Then since $\mu_{\theta} \leq \mu\left(\mathbb{S}^{n}\right)$ the assumption of Lemma 6.6 is satisfied for all $\theta>0$ sufficiently small, and for all $b>0$ for which $U_{\epsilon}^{N}(b)$ is defined. We get the contradiction
$$1=\int_{N} u_{\theta}^{p} d v^{g_{\theta}} \leq m_{\theta}^{p-2} \int_{N} u_{\theta}^{2} d v^{g} \leq m_{\theta}^{p-2}\left(c_{1} m_{\theta}^{2}+c_{2}\right) \rightarrow 0$$
as $\theta \searrow 0$. \(\square\)

Corollary 6.8.
$$\bar{\mu}=\lim _{\theta \searrow 0} \mu_{\theta}>-\infty .$$
Proof. Choose $x_{\theta}$ as above. We then have $\Delta^{g_{\theta}} u_{\theta}\left(x_{\theta}\right) \geq 0$, which together with (51) gives us
$$\text { Scal }^{g_{\theta}}\left(x_{\theta}\right)\left\|u_{\theta}\right\|_{L^{\infty}(N)} \leq \mu_{\theta}\left\|u_{\theta}\right\|_{L^{\infty}(N)}^{p-1} .$$
Proposition 6.4 and the previous corollary then imply that $\mu_{\theta}$ is bounded from below. \(\square\)

In addition, by Theorem 1.1, $\mu_{\theta}$ is bounded from above by $\mu\left(\mathbb{S}^{n}\right)$. It follows that $\bar{\mu} \in \mathbb{R}$. The rest of the proof is divided into cases.

Case I. $\limsup _{\theta}{ }_{\searrow^{0}}\left\|u_{\theta}\right\|_{L^{\infty}(N)}=\infty$.
As before, we set $m_{\theta}:=\left\|u_{\theta}\right\|_{L^{\infty}(N)}$ and choose $x_{\theta} \in N$ with $u_{\theta}\left(x_{\theta}\right)=$ $m_{\theta}$. After again taking a subsequence, we can assume that $\lim _{\theta \searrow 0} m_{\theta}=$ $\infty$. We consider two subcases.

Subcase I.1. There exists $b>0$ such that $x_{\theta} \in N \backslash U_{\epsilon}^{N}(b)$ for an infinite number of $\theta$.

We recall that $N_{\epsilon} \backslash U_{\epsilon}^{N}(b)=M_{1} \amalg M_{2} \backslash U(b)$. By taking a subsequence we can assume that there exists $\bar{x} \in M_{1} \amalg M_{2} \backslash U(b)$ such that $\lim _{\theta \searrow 0} x_{\theta}=\bar{x}$. We let $\tilde{g}_{\theta}:=m_{\theta}^{\frac{4}{n-2}} g_{\theta}$. In a neighborhood $U$ of $\bar{x}$ the metric $g_{\theta}=F^{2} g$ does not depend on $\theta$. We apply Lemma 4.1 with $O=U, \alpha=\theta, q_{\alpha}=x_{\theta}, q=\bar{x}, \gamma_{\alpha}=g_{\theta}=F^{2} g$, and $b_{\alpha}=m_{\theta}^{\frac{2}{n-2}}$. Let $r>0$. For $\theta$ small enough Lemma 4.1 gives us a diffeomorphism
$$\Theta_{\theta}: B^{n}(r) \rightarrow B^{g_{\theta}}\left(x_{\theta}, m_{\theta}^{-\frac{2}{n-2}} r\right)$$
such that the sequence of metrics $\left(\Theta_{\theta}^{*}\left(\tilde{g}_{\theta}\right)\right)$ tends to the flat metric $\xi^{n}$ in $C^{2}\left(B^{n}(r)\right)$. We let $\tilde{u}_{\theta}:=m_{\theta}^{-1} u_{\theta}$. By (2) we then have
$$L^{\tilde{g}_{\theta}} \tilde{u}_{\theta}=\mu_{\theta} \tilde{u}_{\theta}^{p-1}$$
on $B^{g_{\theta}}\left(x_{\theta}, m_{\theta}^{-\frac{2}{n-2}} r\right)$ and, using the fact that $d v^{\tilde{g}_{\theta}}=m_{\theta}^{p} d v^{g_{\theta}}$, we have
$$\begin{aligned}
\int_{B^{g_{\theta}}\left(x_{\theta}, m_{\theta}^{-\frac{2}{n-2}} r\right)} \tilde{u}_{\theta}^{p} d v^{\tilde{g}_{\theta}} & =\int_{B^{g_{\theta}}\left(x_{\theta}, m_{\theta}^{-\frac{2}{n-2}} r\right)} u_{\theta}^{p} d v^{g_{\theta}} \\
& \leq \int_{N} u_{\theta}^{p} d v^{g_{\theta}} \\
& =1
\end{aligned}$$
Since
$$\Theta_{\theta}:\left(B^{n}(r), \Theta_{\theta}^{*}\left(\tilde{g}_{\theta}\right)\right) \rightarrow\left(B^{g_{\theta}}\left(x_{\theta}, m_{\theta}^{-\frac{2}{n-2}} r\right), \tilde{g}_{\theta}\right)$$
is an isometry we can consider $\tilde{u}_{\theta}$ as a solution of
$$L^{\Theta_{\theta}^{*}\left(\tilde{g}_{\theta}\right)} \tilde{u}_{\theta}=\mu_{\theta} \tilde{u}_{\theta}^{p-1}$$
on $B^{n}(r)$ with $\int_{B^{n}(r)} \tilde{u}_{\theta}^{p} d v^{\Theta_{\theta}^{*}}\left(\tilde{g}_{\theta}\right) \leq 1$. Since $\left\|\tilde{u}_{\theta}\right\|_{L^{\infty}\left(B^{n}(r)\right)}=\left|\tilde{u}_{\theta}(0)\right|=1$ we can apply Lemma 4.2 with $V=\mathbb{R}^{n}, \alpha=\theta, g_{\alpha}=\Theta_{\theta}^{*}\left(\tilde{g}_{\theta}\right)$, and $u_{\alpha}=\tilde{u}_{\theta}$ (we can apply this lemma since each compact set of $\mathbb{R}^{n}$ is contained in some ball $\left.B^{n}(r)\right)$. This shows that there exists a nonnegative function $u \not \equiv 0$ (since $u(0)=1$ ) of class $C^{2}$ on ( $\mathbb{R}^{n}, \xi^{n}$ ) that satisfies
$$L^{\xi^{n}} u=a \Delta^{\xi^{n}} u=\bar{\mu} u^{p-1} .$$
By (12) we further have
$$\int_{B^{n}(r)} u^{p} d v^{\xi^{n}}=\lim _{\theta \searrow 0} \int_{B^{g_{\theta}}\left(x_{\theta}, m_{\theta}^{-\frac{2}{n-2}} r\right)} u_{\theta}^{p} d v^{g_{\theta}} \leq 1$$
for any $r>0$. In particular,
$$\int_{\mathbb{R}^{n}} u^{p} d v^{\xi^{n}} \leq 1 .$$
From Lemma 4.3, we get that $\bar{\mu} \geq \mu\left(\mathbb{S}^{n}\right) \geq \min \left\{\mu, \Lambda_{n, k}\right\}$. We have proved Inequality (50) in this subcase.

Subcase I.2. For all $b>0$ it holds that $x_{\theta} \in U_{\epsilon}^{N}(b)$ for $\theta$ sufficiently small.

The subset $U_{\epsilon}^{N}(b)$ is diffeomorphic to $W \times I \times S^{n-k-1}$ where $I$ is an interval. We identify
$$x_{\theta}=\left(y_{\theta}, t_{\theta}, z_{\theta}\right)$$
where $y_{\theta} \in W, t_{\theta} \in\left(-\ln R_{0}+\ln \epsilon,-\ln \epsilon+\ln R_{0}\right)$, and $z_{\theta} \in S^{n-k-1}$. By taking a subsequence we can assume that $y_{\theta}, \frac{t_{\theta}}{A_{\theta}}$, and $z_{\theta}$ converge respectively to $y \in W, T \in[-\infty,+\infty]$, and $z \in S^{n-k-1}$. First we apply Lemma 4.1 with $V=W, \alpha=\theta, q_{\alpha}=y_{\theta}, q=y, \gamma_{\alpha}=\tilde{h}_{t_{\theta}}, \gamma_{0}=\tilde{h}_{T}$ (we define $\tilde{h}_{-\infty}=h_{1}$ and $\tilde{h}_{+\infty}=h_{2}$ ), and $b_{\alpha}=m_{\theta}^{\frac{2}{n-2}} e^{f\left(t_{\theta}\right)}$. The lemma provides diffeomorphisms
$$\Theta_{\theta}^{y}: B^{k}(r) \rightarrow B^{\tilde{h}_{t_{\theta}}}\left(y_{\theta}, m_{\theta}^{-\frac{2}{n-2}} e^{-f\left(t_{\theta}\right)} r\right)$$
for $r>0$ such that $\left(\Theta_{\theta}^{y}\right)^{*}\left(m_{\theta}^{\frac{4}{n-2}} e^{2 f\left(t_{\theta}\right)} \tilde{h}_{t_{\theta}}\right)$ tends to the flat metric $\xi^{k}$ on $B^{k}(r)$ as $\theta \searrow 0$. Second we apply Lemma 4.1 with $V=S^{n-k-1}$, $\alpha=\theta, q_{\alpha}=z_{\theta}, \gamma_{\alpha}=\gamma_{0}=\sigma^{n-k-1}$, and $b_{\alpha}=m_{\theta}^{\frac{n}{n-2}}$. For $r^{\prime}>0$ we get diffeomorphisms
$$\Theta_{\theta}^{z}: B^{n-k-1}\left(r^{\prime}\right) \rightarrow B^{\sigma^{n-k-1}}\left(z_{\theta}, m_{\theta}^{-\frac{2}{n-2}} r^{\prime}\right)$$
such that $\left(\Theta_{\theta}^{z}\right)^{*}\left(m_{\theta}^{\frac{4}{n-2}} \sigma^{n-k-1}\right)$ converges to $\xi^{n-k-1}$ on $B^{n-k-1}\left(r^{\prime}\right)$ as $\theta \searrow 0$. For $r, r^{\prime}, r^{\prime \prime}>0$ we define
$$\begin{aligned}
U_{\theta}\left(r, r^{\prime}, r^{\prime \prime}\right):= & B^{\tilde{h}_{t_{\theta}}}\left(y_{\theta}, m_{\theta}^{-\frac{2}{n-2}} e^{-f\left(t_{\theta}\right)} r\right) \times\left[t_{\theta}-m_{\theta}^{-\frac{2}{n-2}} r^{\prime \prime}, t_{\theta}+m_{\theta}^{-\frac{2}{n-2}} r^{\prime \prime}\right] \\
& \times B^{\sigma^{n-k-1}}\left(z_{\theta}, m_{\theta}^{-\frac{2}{n-2}} r^{\prime}\right),
\end{aligned}$$
and
$$\Theta_{\theta}: B^{k}(r) \times\left[-r^{\prime \prime}, r^{\prime \prime}\right] \times B^{n-k-1}\left(r^{\prime}\right) \rightarrow U_{\theta}\left(r, r^{\prime}, r^{\prime \prime}\right)$$
by
$$\Theta_{\theta}(y, s, z):=\left(\Theta_{\theta}^{y}(y), t(s), \Theta_{\theta}^{z}(z)\right),$$
where $t(s):=t_{\theta}+m_{\theta}^{\frac{2}{n-2}} s$. By construction $\Theta_{\theta}$ is a diffeomorphism, and we see that
$$\begin{aligned}
\Theta_{\theta}^{*}\left(m_{\theta}^{\frac{4}{n-2}} g_{\theta}\right)= & \left(\Theta_{\theta}^{y}\right)^{*}\left(m_{\theta}^{\frac{4}{n-2}} e^{2 f(t)} \tilde{h}_{t}\right)+d s^{2} \\
& +\left(\Theta_{\theta}^{z}\right)^{*}\left(m_{\theta}^{\frac{4}{n-2}} \sigma^{n-k-1}\right)+\Theta_{\theta}^{*}\left(m_{\theta}^{\frac{4}{n-2}} \widetilde{T}_{t}\right) .
\end{aligned}$$
Next we study the first term on the right-hand side of (52). Note that it is here evaluated at $t$, while we have information above when evaluated at $t_{\theta}$. By construction of $f(t)$ one can verify that
$$\lim _{\theta \searrow 0}\left\|\frac{e^{f\left(t_{\theta}\right)}}{e^{f(t)}}-1\right\|_{C^{2}\left(\left[t_{\theta}-m_{\theta}^{-\frac{2}{n-2}} r^{\prime \prime}, t_{\theta}+m_{\theta}^{-\frac{2}{n-2}} r^{\prime \prime}\right]\right)}=0$$
since $\frac{d f}{d t}$ and $\frac{d^{2} f}{d t^{2}}$ are uniformly bounded. Moreover it is clear that
$$\lim _{\theta \searrow 0}\left\|\tilde{h}_{t}-\tilde{h}_{t_{\theta}}\right\|_{C^{2}\left(B^{\tilde{h}_{t_{\theta}}}\left(y_{\theta}, m_{\theta}^{-\frac{2}{n-2}} e^{-f\left(t_{\theta}\right)} r\right)\right)}=0$$
uniformly in $t \in\left[t_{\theta}-m_{\theta}^{-\frac{2}{n-2}} r^{\prime \prime}, t_{\theta}+m_{\theta}^{-\frac{2}{n-2}} r^{\prime \prime}\right]$. As a consequence
$$\lim _{\theta \searrow 0}\left\|\left(\Theta_{\theta}^{y}\right)^{*}\left(m_{\theta}^{\frac{4}{n-2}}\left(e^{2 f(t)} \tilde{h}_{t}-e^{2 f\left(t_{\theta}\right)} \tilde{h}_{t_{\theta}}\right)\right)\right\|_{C^{2}\left(B^{k}(r)\right)}=0$$
uniformly for $t \in\left[t_{\theta}-m_{\theta}^{-\frac{2}{n-2}} r^{\prime \prime}, t_{\theta}+m_{\theta}^{-\frac{2}{n-2}} r^{\prime \prime}\right]$. This implies that the sequence $\left(\Theta_{\theta}^{y}\right)^{*}\left(m_{\theta}^{\frac{4}{n-2}} e^{2 f(t)} \tilde{h}_{t}\right)$ tends to the flat metric $\xi^{k}$ in $C^{2}\left(B^{k}(r)\right)$ uniformly in $t$ as $\theta \searrow 0$. Further, we also know that the sequence
$\left(\Theta_{\theta}^{z}\right)^{*}\left(m_{\theta}^{\frac{4}{n-2}} \sigma^{n-k-1}\right)$ tends to $\xi^{n-k-1}$ in $C^{2}\left(B^{n-k-1}\left(r^{\prime}\right)\right)$ as $\theta \searrow 0$. Recalling from (42) that $g_{\theta}^{\prime}=g_{\theta}-\widetilde{T}_{t}$, we have proved that $\Theta_{\theta}^{*}\left(m_{\theta}^{\frac{4}{n-2}} g_{\theta}^{\prime}\right)$ tends to the flat metric in $C^{2}\left(B^{k}(r) \times\left[-r^{\prime \prime}, r^{\prime \prime}\right] \times B^{n-k-1}\left(r^{\prime}\right)\right)$. Finally we are going to show that the last term of (52) tends to zero in $C^{2}$. It follows from (44) that
$$\lim _{\theta \searrow 0}\left\|\Theta_{\theta}^{*}\left(m_{\theta}^{\frac{4}{n-2}} \widetilde{T}_{t}\right)\right\|_{C^{2}\left(B^{k}(r) \times\left[-r^{\prime \prime}, r^{\prime \prime}\right] \times B^{n-k-1}\left(r^{\prime}\right)\right)}=0$$
Indeed, (44) tells us that
$$\begin{aligned}
\left|\Theta_{\theta}^{*}\left(m_{\theta}^{\frac{4}{n-2}} \widetilde{T}_{t}\right)(X, Y)\right| & =m_{\theta}^{\frac{4}{n-2}}\left|\widetilde{T}_{t}\left(\Theta_{\theta *}(X), \Theta_{\theta *}(Y)\right)\right| \\
& \leq\left. C r m_{\theta}^{\frac{4}{n-2}}\left|\Theta_{\theta *}(X)\right|\right|_{g_{\theta}^{\prime}}\left|\Theta_{\theta *}(Y)\right|_{g_{\theta}^{\prime}} \\
& \leq C r|X| \Theta_{\theta}^{*}\left(m_{\theta}^{\frac{4}{n-2}} g_{\theta}^{\prime}\right)|X| \Theta_{\theta}^{*}\left(m_{\theta}^{\frac{4}{n-2}} g_{\theta}^{\prime}\right)
\end{aligned},$$
and since $\Theta_{\theta}^{*}\left(m_{\theta}^{\frac{4}{n-2}} g_{\theta}^{\prime}\right)$ tends to the flat metric we get (53). Doing the same with $\nabla \widetilde{T}_{t}$ and $\nabla^{2} \widetilde{T}_{t}$ using (45) and (46), we obtain that
$$\lim _{\theta \searrow 0} \Theta_{\theta}^{*}\left(m_{\theta}^{\frac{4}{n-2}} \widetilde{T}_{t}\right)=0$$
in $C^{2}\left(B^{k}(r) \times\left[-r^{\prime \prime}, r^{\prime \prime}\right] \times B^{n-k-1}\left(r^{\prime}\right)\right)$. Returning to (52) we see that the sequence $\Theta_{\theta}^{*}\left(m_{\theta}^{\frac{4}{n-2}} g_{\theta}\right)$ tends to $\xi^{n}=\xi^{k}+d s^{2}+\xi^{n-k-1}$ on $B^{k}(r) \times$ $\left[-r^{\prime \prime}, r^{\prime \prime}\right] \times B^{n-k-1}\left(r^{\prime}\right)$. We proceed as in Subcase I. 1 to show that $\bar{\mu} \geq \mu\left(\mathbb{S}^{n}\right) \geq \min \left\{\mu, \Lambda_{n, k}\right\}$, which proves Relation (50) in the present subcase. This ends the proof of Theorem 6.1 in Case I.

Case II. There exists a constant $C_{1}$ such that $\left\|u_{\theta}\right\|_{L^{\infty}(N)} \leq C_{1}$ for all $\theta$.

As in Case I we consider two subcases.
Subcase II.1. There exists $b>0$ such that
$$\liminf _{\theta \searrow 0}\left(\mu_{\theta} \sup _{U_{\epsilon}^{N}(b)} u_{\theta}^{p-2}\right)<\frac{(n-k-2)^{2}(n-1)}{8(n-2)} .$$

By restricting to a subsequence we can assume that
$$\mu_{\theta} \sup _{U_{\epsilon}^{N}(b)} u_{\theta}^{p-2}<\frac{(n-k-2)^{2}(n-1)}{8(n-2)}$$
for all $\theta$. Lemma 6.6 tells us that there is a constant $A_{0}>0$ such that
$$\left\|u_{\theta}\right\|_{L^{2}\left(N, g_{\theta}\right)} \leq A_{0} .$$
We split the treatment of Subcase II.1. into two subsubcases.
Subsubcase II.1.1. $\lim \sup _{b \searrow 0} \lim \sup _{\theta \searrow 0} \sup _{U_{\epsilon}^{N}(b)} u_{\theta}>0$.

We set $D_{0}:=\frac{1}{2} \limsup _{b \searrow 0} \limsup _{\theta \searrow 0} \sup _{U_{\epsilon}^{N}(b)} u_{\theta}>0$. Then there are sequences $\left(b_{i}\right)$ and $\left(\theta_{i}\right)$ of positive numbers converging to 0 such that
$$\sup _{U_{\epsilon}^{N}\left(b_{i}\right)} u_{\theta_{i}} \geq D_{0},$$
for all $i$. For brevity of notation we write $\theta$ for $\theta_{i}$ and $b_{\theta}$ for $b_{i}$. Let $x_{\theta}^{\prime} \in \overline{U_{\epsilon}^{N}\left(b_{\theta}\right)}$ be such that
$$u_{\theta}\left(x_{\theta}^{\prime}\right) \geq D_{0} .$$
As in Subcase I. 2 above we write $x_{\theta}^{\prime}=\left(y_{\theta}, t_{\theta}, z_{\theta}\right)$ where $y_{\theta} \in W$, $t_{\theta} \in\left(-\ln R_{0}+\ln \epsilon,-\ln \epsilon+\ln R_{0}\right)$, and $z_{\theta} \in S^{n-k-1}$. By restricting to a subsequence we can assume that $y_{\theta}, \frac{t_{\theta}}{A_{\theta}}$, and $z_{\theta}$ converge respectively to $y \in W, T \in[-\infty,+\infty]$, and $z \in S^{n-k-1}$. We apply Lemma 4.1 with $V=W, \alpha=\theta, q_{\alpha}=y_{\theta}, q=y, \gamma_{\alpha}=\tilde{h}_{t_{\theta}}, \gamma_{0}=\tilde{h}_{T}$, and $b_{\alpha}=e^{f\left(t_{\theta}\right)}$ and conclude that there is a diffeomorphism
$$\Theta_{\theta}^{y}: B^{k}(r) \rightarrow B^{\tilde{h}_{t_{\theta}}}\left(y_{\theta}, e^{-f\left(t_{\theta}\right)} r\right)$$
for $r>0$ such that $\left(\Theta_{\theta}^{y}\right)^{*}\left(e^{2 f\left(t_{\theta}\right)} \tilde{h}_{t_{\theta}}\right)$ converges to the flat metric $\xi^{k}$ on $B^{k}(r)$. For $r, r^{\prime}>0$ we set
$$U_{\theta}\left(r, r^{\prime}\right):=B^{\tilde{h}_{t_{\theta}}}\left(y_{\theta}, e^{-f\left(t_{\theta}\right)} r\right) \times\left[t_{\theta}-r^{\prime}, t_{\theta}+r^{\prime}\right] \times S^{n-k-1},$$
and we define
$$\Theta_{\theta}: B^{k}(r) \times\left[-r^{\prime}, r^{\prime}\right] \times S^{n-k-1} \rightarrow U_{\theta}\left(r, r^{\prime}\right)$$
by
$$\Theta_{\theta}(y, s, z):=\left(\Theta_{\theta}^{y}(y), t(s), z\right),$$
where $t(s):=t_{\theta}+s$. By construction, $\Theta_{\theta}$ is a diffeomorphism, and we see that
$$\Theta_{\theta}^{*}\left(g_{\theta}\right)=\frac{e^{2 f(t)}}{e^{2 f\left(t_{\theta}\right)}}\left(\Theta_{\theta}^{y}\right)^{*}\left(e^{2 f\left(t_{\theta}\right)} \tilde{h}_{t}\right)+d s^{2}+\sigma^{n-k-1}+\Theta_{\theta}^{*}\left(\widetilde{T}_{t}\right) .$$
We will now find the limit of $\Theta_{\theta}^{*}\left(g_{\theta}\right)$ in the $C^{2}$ topology. We define $c:=$ $\lim _{\theta \searrow 0} f^{\prime}\left(t_{\theta}\right)$, which can be assumed to exist without loss of generality.

Lemma 6.9. For fixed $r, r^{\prime}>0$ the sequence of metrics $\Theta_{\theta}^{*}\left(g_{\theta}\right)$ tends to $G_{c}=\eta_{c}^{k+1}+\sigma^{n-k-1}=e^{2 c s} \xi^{k}+d s^{2}+\sigma^{n-k-1}$ in the topological space $C^{2}\left(B^{k}(r) \times\left[-r^{\prime}, r^{\prime}\right] \times S^{n-k-1}\right)$.

As this lemma coincides with [4, Lemma 4.1] we only sketch the proof.

Proof. The intermediate value theorem tells us that
$$\left|f(t)-f\left(t_{\theta}\right)-f^{\prime}\left(t_{\theta}\right)\left(t-t_{\theta}\right)\right| \leq \frac{r^{\prime 2}}{2} \max _{s \in\left[t_{\theta}-r^{\prime}, t_{\theta}+r^{\prime}\right]}\left|f^{\prime \prime}(s)\right|$$
for all $t \in\left[t_{\theta}-r^{\prime}, t_{\theta}+r^{\prime}\right]$. Because of (41) we also have $\left\|f^{\prime \prime}\right\|_{L^{\infty}} \rightarrow 0$ for $\theta \searrow 0$, and hence
$$\lim _{\theta \searrow 0}\left\|f(t)-f\left(t_{\theta}\right)-f^{\prime}\left(t_{\theta}\right)\left(t-t_{\theta}\right)\right\|_{C^{0}\left(\left[t_{\theta}-r^{\prime}, t_{\theta}+r^{\prime}\right]\right)}=0$$
for $r^{\prime}$ fixed. Further we have
$$\begin{aligned}
\left|\frac{d}{d t}\left(f(t)-f\left(t_{\theta}\right)-f^{\prime}\left(t_{\theta}\right)\left(t-t_{\theta}\right)\right)\right| & =\left|f^{\prime}(t)-f^{\prime}\left(t_{\theta}\right)\right| \\
& =\left|\int_{t_{\theta}}^{t} f^{\prime \prime}(s) d s\right| \\
& \leq r^{\prime} \max _{s \in\left[t_{\theta}-r^{\prime}, t_{\theta}+r^{\prime}\right]}\left|f^{\prime \prime}(s)\right| \\
& \rightarrow 0
\end{aligned}$$
as $\theta \searrow 0$, and finally
$$\left|\frac{d^{2}}{d t^{2}}\left(f(t)-f\left(t_{\theta}\right)-f^{\prime}\left(t_{\theta}\right)\left(t-t_{\theta}\right)\right)\right|=\left|f^{\prime \prime}(t)\right| \rightarrow 0$$
as $\theta \searrow 0$. Together with $c=\lim _{\theta \searrow 0} f^{\prime}\left(t_{\theta}\right)$ we have shown that
$$\lim _{\theta \searrow 0}\left\|f(t)-f\left(t_{\theta}\right)-c\left(t-t_{\theta}\right)\right\|_{C^{2}\left(\left[t_{\theta}-r^{\prime}, t_{\theta}+r^{\prime}\right]\right)}=0 .$$
Hence
$$\lim _{\theta \searrow 0}\left\|e^{f(t)-f\left(t_{\theta}\right)}-e^{c\left(t-t_{\theta}\right)}\right\|_{C^{2}\left(\left[t_{\theta}-r^{\prime}, t_{\theta}+r^{\prime}\right]\right)}=0 .$$
We now write $e^{2 f(t)} \tilde{h}_{t}=e^{2 f(t)}\left(\tilde{h}_{t}-\tilde{h}_{t_{\theta}}\right)+\frac{e^{2 f(t)}}{e^{2 f\left(t_{\theta}\right)}} e^{2 f\left(t_{\theta}\right)} \tilde{h}_{t_{\theta}}$. Using the fact that
$$\lim _{\theta \searrow 0}\left\|\tilde{h}_{t}-\tilde{h}_{t_{\theta}}\right\|_{C^{2}\left(B^{\tilde{h}_{t \theta}}\left(y_{\theta}, e^{-f\left(t_{\theta}\right)} r\right)\right)}=0$$
holds uniformly for $t \in\left[t_{\theta}-r^{\prime}, t_{\theta}+r^{\prime}\right]$ we obtain that the sequence $\frac{e^{2 f(t)}}{e^{2 f\left(t_{\theta}\right)}}\left(\Theta_{\theta}^{y}\right)^{*}\left(e^{2 f\left(t_{\theta}\right)} \tilde{h}_{t}\right)$ tends to $e^{2 c s} \xi^{k}$ in the $C^{2}\left(B^{k}(r)\right)$-topology where as before $s=t-t_{\theta} \in\left[-r^{\prime}, r^{\prime}\right]$. Finally, proceeding exactly as we did to get Relation (54), we have that
$$\lim _{\theta \searrow 0} \Theta_{\theta}^{*}\left(\widetilde{T}_{t}\right)=0$$
in $C^{2}\left(B^{k}(r) \times\left[-r^{\prime}, r^{\prime}\right] \times S^{n-k-1}\right)$. Now Lemma 6.9 follows from (57). \(\square\)

We continue with the proof of Subsubcase II.1.1. As in Subcases I. 1 and I. 2 we apply Lemma 4.2 with $(V, g)=\left(\mathbb{R}^{k+1} \times S^{n-k-1}, G_{c}\right), \alpha=\theta$, and $g_{\alpha}=\Theta_{\theta}^{*}\left(g_{\theta}\right)$ (we can apply this lemma since any compact subset of $\mathbb{R}^{k+1} \times S^{n-k-1}$ is contained in some $\left.B^{k}(r) \times\left[-r^{\prime}, r^{\prime}\right] \times S^{n-k-1}\right)$. We obtain a $C^{2}$ function $u \geq 0$ that is a solution of
$$L^{G_{c}} u=\bar{\mu} u^{p-1}$$
on $\mathbb{R}^{k+1} \times S^{n-k-1}$. From (12) it follows that
$$\int_{\mathbb{R}^{k+1} \times S^{n-k-1}} u^{p} d v^{G_{c}} \leq 1 .$$
From (11) it follows that $u \in L^{\infty}\left(\mathbb{R}^{k+1} \times S^{n-k-1}\right)$. With (56), we see that $u(0) \geq D_{0}$ and thus, $u \not \equiv 0$. By (55), we also get that $u \in$ $L^{2}\left(\mathbb{R}^{k+1} \times S^{n-k-1}\right)$. By the definition of $\Lambda_{n, k}^{(1)}$ we have that $\bar{\mu} \geq \Lambda_{n, k}^{(1)} \geq$ $\Lambda_{n, k}$. This ends the proof of Theorem 6.1 in this subsubcase.
Subsubcase II.1.2. $\lim _{b \searrow 0} \limsup _{\theta \searrow 0} \sup _{U_{\epsilon}^{N}(b)} u_{\theta}=0$.
The proof in this subsubcase proceeds in several steps.
Step 1. We prove $\lim _{b \searrow 0} \limsup _{\theta \searrow 0} \int_{U_{\epsilon}^{N}(b)} u_{\theta}^{p} d v^{g_{\theta}}=0$.
Let $b>0$. Using (55) we have
$$\int_{U_{\epsilon}^{N}(b)} u_{\theta}^{p} d v^{g_{\theta}} \leq A_{0} \sup _{U_{\epsilon}^{N}(b)} u_{\theta}^{p-2}$$
where the constant $A_{0}$ is independent of $b$ and $\theta$. Step 1 follows.
Step 2. We show $\liminf _{b \searrow 0} \liminf _{\theta \searrow 0} \int_{U_{\epsilon}^{N}(2 b) \backslash U_{\epsilon}^{N}(b)} u_{\theta}^{2} d v^{g_{\theta}}=0$.
Let
$$d_{0}:=\liminf _{b \searrow 0} \liminf _{\theta \searrow 0} \int_{U_{\epsilon}^{N}(2 b) \backslash U_{\epsilon}^{N}(b)} u_{\theta}^{2} d v^{g_{\theta}} .$$
We prove this step by contradiction and assume that $d_{0}>0$. Then there exists $\delta>0$ such that for all $b \in(0, \delta]$,
$$\liminf _{\theta \searrow 0} \int_{U_{\epsilon}^{N}(2 b) \backslash U_{\epsilon}^{N}(b)} u_{\theta}^{2} d v^{g_{\theta}} \geq \frac{d_{0}}{2} .$$
For $m \in \mathbb{N}$ we set $V_{m}:=U\left(2^{-m} \delta\right) \backslash U\left(2^{-(m+1)} \delta\right)$. In particular we have
$$\liminf _{\theta \searrow 0} \int_{V_{m}} u_{\theta}^{2} d v^{g_{\theta}} \geq \frac{d_{0}}{2}$$
for all $m$. Let $N_{0} \in \mathbb{N}$. For $m \neq m^{\prime}$ the sets $V_{m}$ and $V_{m^{\prime}}$ are disjoint. Hence we can write
$$\int_{N} u_{\theta}^{2} d v^{g_{\theta}} \geq \int_{\bigcup_{m=0}^{N_{0}} V_{m}} u_{\theta}^{2} d v^{g_{\theta}} \geq \sum_{m=0}^{N_{0}} \int_{V_{m}} u_{\theta}^{2} d v^{g_{\theta}}$$
for $\theta$ small enough. This leads to
$$\begin{aligned}
\liminf _{\theta \searrow 0} \int_{N} u_{\theta}^{2} d v^{g_{\theta}} & \geq \liminf _{\theta \searrow 0} \sum_{m=0}^{N_{0}} \int_{V_{m}} u_{\theta}^{2} d v^{g_{\theta}} \\
& \geq \sum_{m=0}^{N_{0}} \liminf _{\theta \searrow 0} \int_{V_{m}} u_{\theta}^{2} d v^{g_{\theta}} \\
& \geq\left(N_{0}+1\right) \frac{d_{0}}{2} .
\end{aligned}$$

Since $N_{0}$ is arbitrary, this contradicts that $\left(u_{\theta}\right)$ is bounded in $L^{2}(N)$ and proves Step 2.

Step 3. Conclusion.
Let $d_{0}>0$. By Steps 1 and 2 we can find $b>0$ such that after passing to a subsequence, we have for all $\theta$ close to 0
$$\int_{N \backslash U_{\epsilon}^{N}(2 b)} u_{\theta}^{p} d v^{g_{\theta}} \geq 1-d_{0}$$
and
$$\int_{U_{\epsilon}^{N}(2 b) \backslash U_{\epsilon}^{N}(b)} u_{\theta}^{2} d v^{g_{\theta}} \leq d_{0} .$$
Let $\chi \in C^{\infty}(M), 0 \leq \chi \leq 1$, be a cut-off function equal to 0 on $U_{\epsilon}^{N}(b)$ and equal to 1 on $N \backslash U_{\epsilon}^{N}(2 b)$. Since the set $U_{\epsilon}^{N}(2 b) \backslash U_{\epsilon}^{N}(b)$ corresponds to $t \in\left[t_{0}-\ln 2, t_{0}\right] \cup\left[t_{1}, t_{1}+\ln 2\right]$ with $t_{0}=-\ln b+\ln \epsilon$ and $t_{1}=\ln b-\ln \epsilon$ we can assume that
$$|d \chi|_{g_{\theta}} \leq 2 \ln 2 .$$

We will use the function $\chi u_{\theta}$ to estimate $\mu$. This function is supported in $N \backslash U_{\epsilon}^{N}(b)$. If $\theta$ is smaller than $b$, then $\left(N \backslash U_{\epsilon}^{N}(b), g_{\theta}\right)$ is isometric to $\left(M \backslash U^{M}(b), F^{2} g\right)$. In other words $\left(N \backslash U_{\epsilon}^{N}(b), g_{\theta}\right)$ is conformally equivalent to $\left(M \backslash U^{M}(b), g\right)$. Relation (3) implies that
$$\mu \leq J_{\theta}\left(\chi u_{\theta}\right)=\frac{\int_{N}\left(a\left|d\left(\chi u_{\theta}\right)\right|_{g_{\theta}}^{2}+\mathrm{Scal}^{g_{\theta}}\left(\chi u_{\theta}\right)^{2}\right) d v^{g_{\theta}}}{\left(\int_{N}\left(\chi u_{\theta}\right)^{p} d v^{g_{\theta}}\right)^{\frac{n-2}{n}}} .$$
We multiply Equation (51) by $\chi^{2} u_{\theta}$ and integrate over $N$. We can re-write the result using the following form of (65),
$$\int_{N}\left|d\left(\chi u_{\theta}\right)\right|_{g_{\theta}}^{2} d v^{g_{\theta}}=\int_{N} \chi^{2} u_{\theta} \Delta^{g_{\theta}} u_{\theta} d v^{g_{\theta}}+\int_{N}|d \chi|_{g_{\theta}}^{2} u_{\theta}^{2} d v^{g_{\theta}},$$
to obtain
$$\begin{aligned}
\int_{N}\left(a\left|d\left(\chi u_{\theta}\right)\right|_{g_{\theta}}^{2}+\mathrm{Scal}^{g_{\theta}}\left(\chi u_{\theta}\right)^{2}\right) d v^{g_{\theta}}= & \mu_{\theta} \int_{N} u_{\theta}^{p} \chi^{2} d v^{g_{\theta}}+a \int_{N}|d \chi|_{g_{\theta}}^{2} u_{\theta}^{2} d v^{g_{\theta}} \\
\leq & \mu_{\theta} \int_{N} u_{\theta}^{p} d v^{g_{\theta}}+\left|\mu_{\theta}\right| \int_{U_{\epsilon}^{N}(2 b)} u_{\theta}^{p} d v^{g_{\theta}} \\
& +a \int_{N}|d \chi|_{g_{\theta}}^{2} u_{\theta}^{2} d v^{g_{\theta}} .
\end{aligned}$$
Using (59) and (60), we have
$$\int_{N}|d \chi|_{g_{\theta}}^{2} u_{\theta}^{2} d v^{g_{\theta}}=\int_{U_{\epsilon}^{N}(2 b) \backslash U_{\epsilon}^{N}(b)}|d \chi|_{g_{\theta}}^{2} u_{\theta}^{2} d v^{g_{\theta}} \leq 4(\ln 2)^{2} d_{0} .$$
Relation (58) implies $\int_{U_{\epsilon}^{N}(2 b)} u_{\theta}^{p} d v^{g_{\theta}} \leq d_{0}$. Together with $\int_{N} u_{\theta}^{p} d v^{g_{\theta}}=1$, we have
$$\int_{N}\left(a\left|d\left(\chi u_{\theta}\right)\right|_{g_{\theta}}^{2}+\operatorname{Scal}^{g_{\theta}}\left(\chi u_{\theta}\right)^{2}\right) d v^{g_{\theta}} \leq \mu_{\theta}+\left|\mu_{\theta}\right| d_{0}+4(\ln 2)^{2} a d_{0} .$$

In addition, by Relation (58),
$$\int_{N}\left(\chi u_{\theta}\right)^{p} d v^{g_{\theta}} \geq 1-d_{0} .$$
Plugging (62) and (63) in (61) we get
$$\mu \leq \frac{\mu_{\theta}+\left|\mu_{\theta}\right| d_{0}+4(\ln 2)^{2} a d_{0}}{\left(1-d_{0}\right)^{\frac{n-2}{n}}}$$
for small $\theta$. By taking the limit $\theta \searrow 0$ we can replace $\mu_{\theta}$ by $\bar{\mu}$ in this inequality. Since $d_{0}$ can be chosen arbitrarily small we finally obtain $\mu \leq \bar{\mu}$. This proves Theorem 6.1 in Subcase II.1.

Subcase II.2. For all $b>0$, we have
$$\liminf _{\theta \searrow 0}\left(\mu_{\theta} \sup _{U_{\epsilon}^{N}(b)} u_{\theta}^{p-2}\right) \geq \frac{(n-k-2)^{2}(n-1)}{8(n-2)} .$$