---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: THE FUTURE ASYMPTOTICS OF BIANCHI VIII VACUUM SOLUTIONS]

Lemma 13. Consider a Bianchi VIII solution of (5)-(7). There is a $T$ depending on the initial values such that if $\tau_{0} \geq T$ and $r\left(\tau_{0}\right) \geq\left[\left(N_{2}+N_{3}\right)\left(\tau_{0}\right)\right]^{-1 / 2}$, then $\tilde{x}$ has at least four zeros $\tau_{a}<\tau_{b} \leq \tau_{0} \leq \tau_{c}<\tau_{d}$ in
$$\left[\tau_{1}, \tau_{2}\right]=\left[\tau_{0}-\frac{\pi}{\left(N_{2}+N_{3}\right)\left(\tau_{0}\right)}, \tau_{0}+\frac{\pi}{\left(N_{2}+N_{3}\right)\left(\tau_{0}\right)}\right]$$
such that $\tilde{x}$ is non zero in $\left(\tau_{a}, \tau_{b}\right),\left(\tau_{b}, \tau_{c}\right)$ and $\left(\tau_{c}, \tau_{d}\right)$. Furthermore, for any two consecutive zeros, for example $\tau_{a}$ and $\tau_{b}$, we have
$$\left|\xi\left(\tau_{b}\right)-\xi\left(\tau_{a}\right)-\pi\right| \leq \frac{C}{\left[\left(N_{2}+N_{3}\right)\left(\tau_{a}\right)\right]^{1 / 2}}$$
where $C$ is a numerical constant.
Proof. Let $T$ be great enough that if $\tau \in\left[\tau_{1}, \tau_{2}\right]$ then
$$3\left(N_{2}+N_{3}\right)(\tau) \geq 5\left(N_{2}+N_{3}\right)\left(\tau_{0}\right) / 2 \geq 5\left(N_{2}+N_{3}\right)(\tau) / 4 .$$
This is possible by Lemma 12 and Lemma 11. Let $\mathbf{x}$ be as in (56) where $\phi_{0} \in[0,2 \pi]$ in (54) has been chosen so that $\mathbf{x}\left(\tau_{0}\right)=\tilde{\mathbf{x}}\left(\tau_{0}\right)$. If $\tau \in\left[\tau_{1}, \tau_{2}\right]$ then
$$\left|\xi(\tau)-\xi\left(\tau_{0}\right)\right|=\left|\int_{\tau_{0}}^{\tau} g(s) d s\right| \geq \frac{5}{2}\left(N_{2}+N_{3}\right)\left(\tau_{0}\right)\left|\tau-\tau_{0}\right|$$
Since $\xi$ is a monotonically growing function we conclude
$$[0,2 \pi] \subseteq\left[\phi_{0}-\frac{5}{2} \pi, \phi_{0}+\frac{5}{2} \pi\right] \subseteq\left[\xi\left(\tau_{1}\right), \xi\left(\tau_{2}\right)\right] .$$
We pick out the zeros in the interval $[0,2 \pi]$. Let $\xi\left(\tau_{\alpha}\right)=0, \xi\left(\tau_{\beta}\right)=\pi / 4, \xi\left(\tau_{\gamma}\right)=$ $3 \pi / 4, \xi\left(\tau_{\delta}\right)=5 \pi / 4 \xi\left(\tau_{\epsilon}\right)=7 \pi / 4$ and $\xi\left(\tau_{\zeta}\right)=2 \pi$, where $\tau_{\alpha}$ and so on belong to $\left[\tau_{1}, \tau_{2}\right]$. In the intervals $\left[\tau_{\alpha}, \tau_{\beta}\right],\left[\tau_{\gamma}, \tau_{\delta}\right]$ and $\left[\tau_{\epsilon}, \tau_{\zeta}\right] \tilde{x}$ cannot be zero if $T$ is great enough because of (57) and the fact that $r\left(\tau_{0}\right) \geq\left[\left(N_{2}+N_{3}\right)\left(\tau_{0}\right)\right]^{-1 / 2}$. For the same reason $\tilde{x}^{\prime}$ cannot be zero in $\left[\tau_{\beta}, \tau_{\gamma}\right]$ and $\left[\tau_{\delta}, \tau_{\epsilon}\right]$ since $\tilde{x}^{\prime}=-g \tilde{y}+\epsilon_{x}$. Thus there is exactly one zero in $\left[\tau_{\beta}, \tau_{\gamma}\right]$ and one in $\left[\tau_{\delta}, \tau_{\epsilon}\right]$ and no zeros in between. The remaining zeros are picked out in the same way. By the above it follows that for two consecutive zeros, for example $\tau_{a}$ and $\tau_{b}, \pi / 2 \leq \xi\left(\tau_{b}\right)-\xi\left(\tau_{a}\right) \leq 3 \pi / 2$. Thus
$$\begin{gathered}
\left|\xi\left(\tau_{b}\right)-\xi\left(\tau_{a}\right)-\pi\right| \leq \frac{\pi}{2}\left|\sin \left(\xi\left(\tau_{b}\right)-\xi\left(\tau_{a}\right)-\pi\right)\right| \leq \frac{\pi}{2}\left(\left|\cos \left(\xi\left(\tau_{a}\right)\right)\right|+\left|\cos \left(\xi\left(\tau_{b}\right)\right)\right|\right) \\
\leq \frac{\pi}{2 r\left(\tau_{0}\right)}\left(\left|\tilde{x}\left(\tau_{a}\right)-x\left(\tau_{a}\right)\right|+\left|\tilde{x}\left(\tau_{b}\right)-x\left(\tau_{b}\right)\right|\right) \leq \frac{9 \pi^{2}}{\left[\left(N_{2}+N_{3}\right)\left(\tau_{0}\right)\right]^{1 / 2}} \\
\leq \frac{18 \pi^{2}}{\left[\left(N_{2}+N_{3}\right)\left(\tau_{a}\right)\right]^{1 / 2}}
\end{gathered}$$
using (57) and (64). □
Lemma 14. Consider a Bianchi VIII solution of (5)-(7). There is a $T$ such that if $\tau_{a}$ and $\tau_{b}$ are two consecutive zeros of $\tilde{x}$ and $r\left(\tau_{a}\right) \geq\left[\left(N_{2}+N_{3}\right)\left(\tau_{a}\right)\right]^{-1 / 2}, \tau_{a} \geq T$, then if $z_{1}$ and $z_{2}$ are $\Sigma_{+}$evaluated in $\tau_{a}$ and $\tau_{b}$ respectively and $w_{1}$ and $w_{2}$ are $-N_{1}\left(N_{2}+N_{3}\right)$ evaluated in $\tau_{a}$ and $\tau_{b}$ respectively, we have
$$z_{2}-z_{1}=\left[-\left(1-z_{1}\right)\left(1+z_{1}\right)^{2}+\frac{3}{2} w_{1}\left(2-z_{1}\right)\right]\left(\tau_{b}-\tau_{a}\right)+\epsilon_{1}$$
and
$$w_{2}-w_{1}=\left(2 z_{1}^{2}-2 z_{1}+2-3 w_{1}\right) w_{1}\left(\tau_{b}-\tau_{a}\right)+\epsilon_{2}$$
where
$$\left|\epsilon_{i}\right| \leq \frac{C}{\left(N_{2}+N_{3}\right)^{3 / 2}\left(\tau_{a}\right)}$$
for $i=1,2$ and some numerical constant $C$.
Remark. We will prove that $\tau_{b}-\tau_{a}$ is of the order of magnitude $1 /\left(N_{2}+N_{3}\right)$. Consequently we can ignore the error terms in (65) and (66) as long as the polynomial expressions appearing in front of $\tau_{b}-\tau_{a}$ are of the order of magnitude 1.
Proof. The idea is to consider the derivatives of $\Sigma_{+}$and $-N_{1}\left(N_{2}+N_{3}\right)$ and to integrate between $\tau_{a}$ and $\tau_{b}$. We will see that $\Sigma_{+}$and $-N_{1}\left(N_{2}+N_{3}\right)$ vary slowly so that we can replace them with constants, up to an error we estimate. However, $\Sigma_{-}$and $N_{2}-N_{3}$ do not vary slowly so that we will have to use (57) and to estimate $\int_{\tau_{a}}^{\tau_{b}} \sin ^{2}(\xi(\tau)) d \tau$.
All numerical constants below will be denoted $C$. Observe that
$$\left|\tau_{b}-\tau_{a}\right| \leq \frac{C}{\left(N_{2}+N_{3}\right)\left(\tau_{a}\right)}$$
by the arguments presented in the proof of Lemma 13, assuming $T$ to be great enough. We will assume $T$ is great enough that $3\left(N_{2}+N_{3}\right)(\tau) \geq 5\left(N_{2}+N_{3}\right)\left(\tau_{0}\right) / 2 \geq$ $\left(N_{2}+N_{3}\right)(\tau)$ for all $\tau \in\left[\tau_{a}, \tau_{b}\right]$, as is possible by Lemma 12. We begin by analyzing the variation of some relevant expressions in $\left[\tau_{a}, \tau_{b}\right]$. By Lemma 12 we conclude
$$\left|\Sigma_{+}(\tau)-\Sigma_{+}\left(\tau_{a}\right)\right| \leq \frac{C}{\left(N_{2}+N_{3}\right)\left(\tau_{a}\right)}$$
for all $\tau \in\left[\tau_{a}, \tau_{b}\right]$ and similarly for $N_{1}\left(N_{2}+N_{3}\right)$. Assume $N_{2}+N_{3}$ has a max in $\tau_{\text {max }}$ in $\left[\tau_{a}, \tau_{b}\right]$ and a min in $\tau_{\text {min }}$ in the same interval. Then
$$\begin{gathered}
\left|\frac{1}{\left(N_{2}+N_{3}\right)\left(\tau_{\max }\right)}-\frac{1}{\left(N_{2}+N_{3}\right)\left(\tau_{\min }\right)}\right| \\
\leq \frac{1}{\left(N_{2}+N_{3}\right)\left(\tau_{\max }\right)}\left|1-\frac{\left(N_{2}+N_{3}\right)\left(\tau_{\max }\right)}{\left(N_{2}+N_{3}\right)\left(\tau_{\min }\right)}\right| \leq \frac{C}{\left(N_{2}+N_{3}\right)^{2}\left(\tau_{a}\right)}
\end{gathered}$$
by (60). Since $\xi$ as defined in (54) is a diffeomorphism we can consider functions of $\tau$ as functions of $\xi$. We will be interested in the following integral
$$\begin{gathered}
\int_{\tau_{a}}^{\tau_{b}} \sin ^{2} \xi(\tau) d \tau=\int_{\xi\left(\tau_{a}\right)}^{\xi\left(\tau_{b}\right)} \sin ^{2}(\xi) \frac{1}{g} d \xi=\frac{1}{g\left(\tau_{a}\right)} \int_{\xi\left(\tau_{a}\right)}^{\xi\left(\tau_{a}\right)+\pi} \sin ^{2}(\xi) d \xi \\
+\frac{1}{g\left(\tau_{a}\right)} \int_{\xi\left(\tau_{a}\right)+\pi}^{\xi\left(\tau_{b}\right)} \sin ^{2}(\xi) d \xi+\int_{\xi\left(\tau_{a}\right)}^{\xi\left(\tau_{b}\right)} \sin ^{2}(\xi)\left(\frac{1}{g}-\frac{1}{g\left(\tau_{a}\right)}\right) d \xi \\
=\frac{\pi}{2 g\left(\tau_{a}\right)}+\delta_{1}
\end{gathered}$$
where
$$\left|\delta_{1}\right| \leq \frac{C}{\left[\left(N_{2}+N_{3}\right)\left(\tau_{a}\right)\right]^{3 / 2}}$$
due to (63) and (70). Furthermore
$$\tau_{a}-\tau_{b}=\int_{\tau_{a}}^{\tau_{b}} d \tau=\int_{\xi\left(\tau_{a}\right)}^{\xi\left(\tau_{b}\right)} \frac{1}{g} d \xi=\frac{\pi}{g\left(\tau_{a}\right)}+\delta_{2}$$
by similar arguments, where $\delta_{2}$ is of the same order of magnitude as $\delta_{1}$. Consequently
$$\int_{\tau_{a}}^{\tau_{b}} \sin ^{2} \xi(\tau) d \tau=\frac{1}{2}\left(\tau_{b}-\tau_{a}\right)+\delta_{3}$$
where $\delta_{3}$ is of the same order of magnitude as $\delta_{1}$. We now have all the necessary estimates at our disposal. In $\left[\tau_{a}, \tau_{b}\right]$ we have
$$\begin{gathered}
\Sigma_{+}^{\prime}=-(2-q) \Sigma_{+}-3 S_{+}=-\left(2-2 \Sigma_{+}^{2}\right) \Sigma_{+}+2 \Sigma_{-}^{2} \Sigma_{+}-\frac{3}{2}\left(N_{2}-N_{3}\right)^{2}+3 N_{1}^{2} \\
-\frac{3}{2} N_{1}\left(N_{2}+N_{3}\right)=-\left(2-2 z_{1}^{2}\right) z_{1}+2 z_{1} r^{2}\left(\tau_{a}\right) \cos ^{2}(\xi)-2 r^{2}\left(\tau_{a}\right) \sin ^{2}(\xi)+\frac{3}{2} w_{1}+\epsilon_{3}
\end{gathered}$$
where
$$\left|\epsilon_{3}\right| \leq \frac{C}{\left(N_{2}+N_{3}\right)\left(\tau_{a}\right)}$$
due to (69), the analogous estimate for $N_{1}\left(N_{2}+N_{3}\right)$, (57) and the fact that $N_{1}$ is of the order of magnitude $\left(N_{2}+N_{3}\right)^{-1}$ (7). Integrating, using (72), we have
$$z_{2}-z_{1}=\left[-\left(2-2 z_{1}^{2}\right) z_{1}+z_{1} r^{2}\left(\tau_{a}\right)-r^{2}\left(\tau_{a}\right)+\frac{3}{2} w_{1}\right]\left(\tau_{b}-\tau_{a}\right)+\epsilon_{4}$$
where
$$\left|\epsilon_{4}\right| \leq \frac{C}{\left(N_{2}+N_{3}\right)^{3 / 2}\left(\tau_{a}\right)} .$$
Using the constraint (7) to express $r^{2}\left(\tau_{a}\right)$ in $z_{1}$ and $w_{1}$ (and $N_{1}$ ), we deduce (65) and (67), $i=1$. The argument to obtain (66) is similar. □

Lemma 15. Consider a Bianchi VIII solution of (5)-(7). For all $\epsilon>0$ there is a $T$ such that $\tau \geq T$ implies $\Sigma_{+}(\tau) \leq 1 / 2+\epsilon$.

Proof. Let $\epsilon>0$. If $\Sigma_{+}(\tau) \geq 1 / 2+\epsilon / 2$ for all $\tau \geq T$, then $-N_{1}\left(N_{2}+N_{3}\right) \rightarrow \infty$ by (5)-(7) and Lemma 11. Since this cannot occur by (7) we conclude the existence of a $t \geq T$ such that $\Sigma_{+}(t) \leq 1 / 2+\epsilon / 2$. If there is a $s \geq t$ such that $\Sigma_{+}(s) \geq 1 / 2+\epsilon$ there is an interval $\left[\tau_{1}, \tau_{2}\right]$ with $\tau_{1} \geq t, \Sigma_{+}\left(\tau_{1}\right)=1 / 2+\epsilon / 2, \Sigma_{+}\left(\tau_{2}\right)=1 / 2+\epsilon$ and $1 / 2+\epsilon / 2 \leq \Sigma_{+}(\tau) \leq 1 / 2+\epsilon$ for all $\tau \in\left[\tau_{1}, \tau_{2}\right]$. Using the constraint (7) to eliminate $N_{1}\left(N_{2}+N_{3}\right)$ in the expression for $\Sigma_{+}^{\prime}$, we conclude that
$$\frac{\epsilon}{2}=\int_{\tau_{1}}^{\tau_{2}} \Sigma_{+}^{\prime}(\tau) d \tau \leq \frac{9}{4} \int_{\tau_{1}}^{\tau_{2}} N_{1}^{2}(\tau) d \tau$$
Since $N_{1}^{\prime} \geq-2 \epsilon N_{1}$ in $\left[\tau_{1}, \tau_{2}\right]$ we conclude that
$$\frac{\epsilon}{2} \leq \frac{9 N_{1}^{2}\left(\tau_{1}\right)}{16 \epsilon} .$$
For $T$ great enough this inequality is impossible by Lemma 11. The lemma follows. \(\square\)

Lemma 16. Consider a Bianchi VIII solution of (5)-(7). $N_{1}\left(N_{2}+N_{3}\right)$ does not converge to zero.

Proof. Assume $N_{1}\left(N_{2}+N_{3}\right) \rightarrow 0$. We prove that this assumption forces $\Sigma_{+}$to become negative which, in turn, forces $-N_{1}\left(N_{2}+N_{3}\right)$ to increase, leading to a contradiction. We use Lemma 14 to achieve the decrease in $\Sigma_{+}$. To apply it we need $r$ to be big. However, the constraint yields
$$r^{2}=1-\Sigma_{+}^{2}+\frac{3}{2} N_{1}\left(N_{2}+N_{3}\right)-\frac{3}{4} N_{1}^{2} .$$
Since the last two terms converge to zero due to our assumption and Lemma 11, only $1-\Sigma_{+}^{2}$ is of relevance. From above we have control over $\Sigma_{+}$by Lemma 15 and if $\Sigma_{+} \leq-\frac{1}{2}$ we have nothing to prove as it turns out.
Let us be more precise. Let $T$ be large enough that $\Sigma_{+}(\tau) \leq \frac{3}{4}$ for all $\tau \geq T$. This is possible by Lemma 15. Assume also $T$ to be great enough that if $t \geq T$ and $-\frac{3}{4} \leq \Sigma_{+}(t)$, then
$$r^{2}(t) \geq \frac{1}{4} \geq \frac{1}{\left(N_{2}+N_{3}\right)(t)} .$$
In order to achieve this we use (73), Lemma 11 and $N_{1}\left(N_{2}+N_{3}\right) \rightarrow 0$. Finally let $T$ be great enough that Lemma 13 and Lemma 14 are applicable to all $\tau_{0} \geq T$ such that $r\left(\tau_{0}\right) \geq\left(N_{2}+N_{3}\right)^{-1 / 2}\left(\tau_{0}\right)$.
Let $t \geq T$. We prove that we can iterate $\Sigma_{+}$to become less than or equal to $-\frac{1}{2}$ using Lemma 14. If $\Sigma_{+}(t) \leq-\frac{1}{2}$ we are done. The first zero after $t$, say $t_{1}$, which exists by (74) and Lemma 13, can for the same reason be assumed to satisfy $\Sigma_{+}\left(t_{1}\right) \geq-\frac{1}{2}$. Because of (65), (67), (71) and the fact that $N_{1}\left(N_{2}+N_{3}\right) \rightarrow 0$, we conclude
$$\Sigma_{+}\left(t_{2}\right)-\Sigma_{+}\left(t_{1}\right) \leq-\frac{1}{9}\left(t_{2}-t_{1}\right)$$
if $T$ is great enough and $t_{2}$ is the first zero after $t_{1}$. If $\Sigma_{+}\left(t_{k}\right) \geq-\frac{1}{2}$, the next zero $t_{k+1}$ will satisfy a relation similar to (75). Sooner or later we will thus have $\Sigma_{+}\left(t_{k}\right) \leq-\frac{1}{2}$. Since the distance between two zeros becomes arbitrarily small as time goes on and the derivative of $\Sigma_{+}$is uniformly bounded, $\Sigma_{+}$cannot at late enough times become greater than $-\frac{1}{4}$ after having been smaller than $-\frac{1}{2}$ due to (75). Consequently there is a $T^{\prime}$ such that $\tau \geq T^{\prime}$ implies $\Sigma_{+}(\tau) \leq-\frac{1}{4}$. We conclude that $-N_{1}\left(N_{2}+N_{3}\right) \rightarrow \infty$ by considering the derivative of $N_{1}\left(N_{2}+N_{3}\right)$ and using Lemma 11. □

Lemma 17. Consider a Bianchi VIII solution to (5)-(1). For all $\epsilon>0$ there is a $T$ such that $\tau \geq T$ implies $-N_{1}\left(N_{2}+N_{3}\right) \geq 1 / 2-\epsilon$.

Proof. Assuming $-N_{1}\left(N_{2}+N_{3}\right) \leq 1 / 2-\epsilon / 2$, we prove that the expression grows at late enough times. Under certain conditions on $\Sigma_{+}$this will be seen by considering the derivative of $-N_{1}\left(N_{2}+N_{3}\right)$, but under other other circumstances we apply Lemma 14. In order for the iteration to work, we will have to have a good upper bound on $\Sigma_{+}$, c.f. (76). We will also need Lemma 16 in order to get a starting point greater than or equal to some fixed positive number, irrespective of at how late a time we start.

Let $\frac{1}{10}>\epsilon>0$ and $S$ be such that
$$\Sigma_{+}(\tau) \leq \frac{1}{2}+\epsilon^{2}$$
for all $\tau \geq S$. Define $w=-N_{1}\left(N_{2}+N_{3}\right)$. Since $w$ does not converge to zero there is an $\eta>0$ such that for all $S^{\prime}$ there is a $t \geq S^{\prime}$ satisfying $w(t) \geq \eta$. Let $t \geq S$ be such. We prove that there is a $t^{\prime} \geq t$ with the property that
$$w\left(t^{\prime}\right) \geq \frac{1}{2}-\frac{\epsilon}{2} .$$
Assume
$$w(t) \leq \frac{1}{2}-\frac{\epsilon}{2} .$$
There are two possibilities. Either $\Sigma_{+} \leq-\frac{1}{4}$, in which case we will be able to see that $w$ increases by considering its derivative. If $\Sigma_{+} \geq-\frac{1}{2}$ we will be able to apply Lemma 14.
1. There is a $T^{\prime}$ such that if $\left[t_{1}, t_{2}\right]$ is an interval in which $\Sigma_{+} \leq-\frac{1}{4}$ and $t_{1} \geq T^{\prime}$, then
$$w\left(t_{2}\right)-w\left(t_{1}\right) \geq \frac{1}{2} w\left(t_{1}\right)\left(t_{2}-t_{1}\right) .$$
This can be seen by applying Lemma 11, (5) and (7).
2. There is a $T^{\prime \prime}$ such that if $t_{1}<t_{2}$ are two consecutive zeros of $\Sigma_{-}$with $T^{\prime \prime} \leq t_{1}$, $\Sigma_{+}\left(t_{1}\right) \geq-\frac{1}{2}$ and $1 / 2-\epsilon / 2 \geq w\left(t_{1}\right) \geq \eta / 2$, then
$$w\left(t_{2}\right)-w\left(t_{1}\right) \geq \epsilon w\left(t_{1}\right)\left(t_{2}-t_{1}\right) .$$
We get, in $t_{1}$
$$r^{2}=1-\Sigma_{+}^{2}-\frac{3}{4} N_{1}^{2}+\frac{3}{2} N_{1}\left(N_{2}+N_{3}\right) \geq \frac{3}{4} \epsilon-3 \epsilon^{2}$$
if $T^{\prime \prime}$ is great enough. If $T^{\prime \prime}$ is great enough we can apply Lemma 14. Consider (66) with $\tau_{a}$ replaced with $t_{1}$ and $\tau_{b}$ replaced with $t_{2}$. Since $2 z_{1}^{2}-2 z_{1}+2 \geq 3 / 2 \forall z_{1} \in \mathbb{R}$ and $1 / 2-\epsilon / 2 \geq w\left(t_{1}\right)$ we get
$$w\left(t_{2}\right)-w\left(t_{1}\right) \geq \frac{3 \epsilon}{2} w\left(t_{1}\right)\left(t_{2}-t_{1}\right)+\epsilon_{2} .$$
Since $w\left(t_{1}\right) \geq \eta / 2$ we can use (67) and (71) to prove that (80) holds if $T^{\prime \prime}$ is big enough. This is where we need Lemma 16.
Assume $t$ to be greater than $T^{\prime}$ and $T^{\prime \prime}$ and that $w(\tau) \leq 1 / 2-\epsilon / 2$ for $\tau \in[t, s]$. We can divide $[t, s]$ into $t=s_{0}<s_{1}<s_{2}<\ldots<s_{k}<s_{k+1}=s$ where $\Sigma_{+}\left(s_{i}\right)=-\frac{1}{3}$, $i=1, \ldots, k$ and $\Sigma_{+}$is either $\geq-\frac{1}{2}$ or $\leq-\frac{1}{4}$ in each $\left[s_{i}, s_{i+1}\right]$. If $1 \leq i \leq k$ then we can change $s_{i}$ so that it becomes a zero of $\Sigma_{-}$without changing the earlier conditions of the construction except that the new $\Sigma_{+}\left(s_{i}\right)$ need not necessarily equal $-\frac{1}{3}$, c.f. (81). This is due to the fact that we can apply Lemma 13 if $t$ is great enough, that $\left|\Sigma_{+}^{\prime}\right|$ is uniformly bounded and the fact that the distance to the next zero goes to zero as $t$ goes to infinity.
Since $w(t) \leq 1 / 2-\epsilon / 2$ we can apply Lemma 13 to get a zero $s_{1 / 2}$ with $t \leq s_{1 / 2}$ assuming $t$ is great enough and $\Sigma_{+}(t) \geq-\frac{1}{2}$, c.f. (81). Since $s_{1 / 2}-t$ is of the order of magnitude $1 /\left(N_{2}+N_{3}\right)$ and $w^{\prime}$ is uniformly bounded we can assume $w\left(s_{1 / 2}\right) \geq \eta / 2$. If $\Sigma_{+} \leq-\frac{1}{4}$ in $\left[s_{0}, s_{1}\right]$, we let $s_{1 / 2}=t$. Observe that the condition $w(v) \geq \eta / 2$ will be satisfied for a zero $v$ of $\Sigma_{-}$with $s \geq v \geq s_{1 / 2}$ by 1 and 2. If $\Sigma_{+} \geq-\frac{1}{2}$ in $\left[s_{k}, s\right]$ we have to take into account the possibility that $s$ need not be a zero of $\Sigma_{-}$. Let
in that case $s_{k+1 / 2}$ be the last zero of $\Sigma_{-}$before $s$. If $\Sigma_{+} \leq-\frac{1}{4}$ in $\left[s_{k}, s\right]$ we let $s_{k+1 / 2}=s$. We have, applying (80) or (79) in the intervals $\left[s_{i}, s_{i+1}\right]$
$$w\left(s_{k+1 / 2}\right)-w\left(s_{1 / 2}\right) \geq \frac{1}{2} \epsilon \eta\left(s_{k+1 / 2}-s_{1 / 2}\right) .$$
Using the fact that $\left|w^{\prime}\right|$ is uniformly bounded and the estimates of $s_{1 / 2}-t$ and $s-s_{k+1 / 2}$ we conclude that
$$w(s)-w(t) \geq \frac{1}{2} \epsilon \eta(s-t)-\frac{C}{\left(N_{2}+N_{3}\right)(t)}-\frac{C}{\left(N_{2}+N_{3}\right)(s)}$$
for some constant $C>0$. We conclude the existence of a $t^{\prime} \geq t$ as in (77). Finally, $w$ cannot become smaller than $1 / 2-\epsilon$ once it has become greater than $1 / 2-\epsilon / 2$ given $t$ great enough. We only have to apply the above and observe that $\left|w^{\prime}\right|$ is uniformly bounded and the distance between two zeros of $\Sigma_{-}$becomes arbitrarily small as $t \rightarrow \infty$. □

Theorem 1. Let $\left(\Sigma_{+}, \Sigma_{-}, N_{1}, N_{2}, N_{3}\right)$ be a Bianchi VIII solution to (5)-(7) with $N_{1}<0$ and $N_{2}, N_{3}>0$. Then
$$\lim _{\tau \rightarrow \infty} N_{1}=0, \lim _{\tau \rightarrow \infty} N_{2}=\infty, \lim _{\tau \rightarrow \infty} N_{3}=\infty .$$
Furthermore
$$\lim _{\tau \rightarrow \infty} \Sigma_{+}=\frac{1}{2}, \lim _{\tau \rightarrow \infty} \Sigma_{-}=0$$
and
$$\lim _{\tau \rightarrow \infty} N_{1}\left(N_{2}+N_{3}\right)=-\frac{1}{2}, \quad \lim _{\tau \rightarrow \infty}\left(N_{2}-N_{3}\right)=0 .$$
Proof. We begin by proving that for every $\epsilon>0$ there is a $T$ such that $\tau \geq T$ implies $\Sigma_{+}(\tau) \geq 1 / 2-\epsilon$. We will then be able to draw the conclusions of the theorem. Use the constraint (7) to obtain
$$\Sigma_{+}^{\prime}=-\frac{3}{2}\left(N_{2}-N_{3}\right)^{2}\left(\Sigma_{+}+1\right)+\frac{3}{2} N_{1}\left(N_{2}+N_{3}\right)\left(2 \Sigma_{+}-1\right)+\frac{3}{2} N_{1}^{2}\left(2-\Sigma_{+}\right) .$$
Observe that by Lemma 17 we can assume $-N_{1}\left(N_{2}+N_{3}\right)$ to be big. By Lemma 11 we can disregard the term involving $N_{1}$. If $\Sigma_{+}$is smaller than, say, $1 / 2-\epsilon / 2$, we want $\Sigma_{+}$to increase. Considering (82) two things can happen. Either $r$ is small, in which case the first term is negligible and then the second term which is positive will dominate. Thus $\Sigma_{+}$increases. If $r$ is big, we have to use Lemma 14. We make these observations more precise in the following two statements.
1. There is a $T^{\prime}$ such that if $r^{2}(\tau) \leq \epsilon / 36$ and $\Sigma_{+}(\tau) \leq 1 / 2-\epsilon / 2$ for $\tau \in[t, s]$ where $t \geq T^{\prime}$, then
$$\Sigma_{+}(s)-\Sigma_{+}(t) \geq \frac{\epsilon}{3}(s-t) .$$
The proof is as follows. If $T^{\prime}$ is great enough then $-\left[N_{1}\left(N_{2}+N_{3}\right)\right](\tau) \geq \frac{1}{3}$ for $\tau \geq T^{\prime}$ so that if $\Sigma_{+}(\tau) \leq 1 / 2-\epsilon / 2$ then
$$\frac{3}{2} N_{1}\left(N_{2}+N_{3}\right)\left(2 \Sigma_{+}-1\right) \geq \frac{\epsilon}{2}$$
in $\tau$. Assume $T^{\prime}$ to be great enough that we also have
$$\frac{3}{2}\left[N_{1}^{2}\left(2-\Sigma_{+}\right)\right](\tau) \leq \frac{\epsilon}{12}$$
for $\tau \geq T^{\prime}$. If $\tau \in[t, s]$ we thus conclude that
$$\Sigma_{+}^{\prime}(\tau) \geq \frac{\epsilon}{3}$$
using (82). The statement follows.
2. There is a $T^{\prime \prime}$ such that if $r^{2}(\tau) \geq \epsilon / 100$ and $\Sigma_{+}(\tau) \leq 1 / 2-\epsilon / 2$ for $\tau \in\left[\tau_{1}, \tau_{2}\right]$ where $\tau_{1} \geq T^{\prime \prime}$ and $\tau_{1}$ and $\tau_{2}$ are consecutive zeros of $\Sigma_{-}$then
$$\Sigma_{+}\left(\tau_{2}\right)-\Sigma_{+}\left(\tau_{1}\right) \geq \frac{\epsilon^{2}}{10}\left(\tau_{2}-\tau_{1}\right)$$
The proof is as follows. We have
$$r^{2}(\tau) \geq \frac{1}{\left(N_{2}+N_{3}\right)(\tau)}$$
for $\tau \in\left[\tau_{1}, \tau_{2}\right]$ if $T^{\prime \prime}$ is large enough. If $T^{\prime \prime}$ is large enough, we can apply Lemma 14. Consider (65). The relevant polynomial expression is
$$\begin{aligned}
& -\left(1-z_{1}\right)\left(1+z_{1}\right)^{2}+\frac{3}{2} w_{1}\left(2-z_{1}\right)=-\left(1-z_{1}\right)\left(1+z_{1}\right)^{2}+\frac{3}{4}\left(2-z_{1}\right) \\
& \quad+\frac{3}{2}\left(w_{1}-\frac{1}{2}\right)\left(2-z_{1}\right)=\left(z_{1}+2\right)\left(z_{1}-\frac{1}{2}\right)^{2}+\frac{3}{2}\left(w_{1}-\frac{1}{2}\right)\left(2-z_{1}\right)
\end{aligned}$$
Since $-1 \leq z_{1} \leq 1 / 2-\epsilon / 2$ in our situation, and since we can assume $T^{\prime \prime}$ to be great enough that $w_{1} \geq 1 / 2-\epsilon^{2} / 36$ by Lemma 17, we conclude
$$-\left(1-z_{1}\right)\left(1+z_{1}\right)^{2}+\frac{3}{2} w_{1}\left(2-z_{1}\right) \geq \frac{\epsilon^{2}}{4}-\frac{\epsilon^{2}}{8}=\frac{\epsilon^{2}}{8} .$$
Thus (84) follows, in which we have absorbed the error term in (65) using (67) and (71).
Let $S$ be greater than $T^{\prime}$ and $T^{\prime \prime}$. We start by proving the existence of a $t \geq S$ such that $\Sigma_{+}(t) \geq 1 / 2-\epsilon / 2$. Assume $\Sigma_{+}(\tau) \leq 1 / 2-\epsilon / 2$ in $[S, s]$. We can divide the interval by $S=s_{0}<s_{1}<\ldots<s_{k}<s_{n}=s$ where $r^{2}$ is either $\geq \epsilon / 100$ or $\leq \epsilon / 36$ in each $\left[s_{i}, s_{i+1}\right]$ and $r^{2}\left(s_{i}\right)=\epsilon / 50$ for all $s_{i} i=1, \ldots, k$. If $S$ is large enough we can assume the $s_{i} i=1, \ldots, k$ to be zeros of $\Sigma_{-}$without changing the earlier conditions of the construction other than $r^{2}\left(s_{i}\right)=\epsilon / 50, i=1, \ldots, k$. The reason is that we can apply Lemma 13 to $s_{i}, i=1, \ldots, k$, if $S$ is large enough, to get a zero within a distance of the order of magnitude $1 /\left(N_{2}+N_{3}\right)$. Using the estimate (57) and the fact that $r^{2}=\tilde{x}^{2}+\tilde{y}^{2}, r^{2}$ can be made to vary an arbitrarily small amount from the original $s_{i}$ to the first zero after it by choosing $S$ large enough. If $r^{2}(\tau) \geq \epsilon / 100$ in $\left[s_{0}, s_{1}\right]$, we let $s_{1 / 2}$ be the first zero after $s_{0}$. Otherwise, we let $s_{1 / 2}=s$. We define $s_{k+1 / 2}$ analogously. Using (83) and (84) we conclude
$$\Sigma_{+}\left(s_{k+1 / 2}\right)-\Sigma_{+}\left(s_{1 / 2}\right) \geq \frac{\epsilon^{2}}{10}\left(s_{k+1 / 2}-s_{1 / 2}\right)$$
assuming $\epsilon<10 / 3$. If we use our estimates of $s_{1 / 2}-S$ and $s-s_{k+1 / 2}$ we get
$$\Sigma_{+}(s)-\Sigma_{+}(S) \geq \frac{\epsilon^{2}}{10}(s-S)-\frac{C}{\left(N_{2}+N_{3}\right)(S)}-\frac{C}{\left(N_{2}+N_{3}\right)(s)}$$
If $S$ and $s-S$ are large enough this is not possible and there must thus be a $t$ such that $\Sigma_{+}(t) \geq 1 / 2-\epsilon / 2$.

If $S$ big is enough, $\Sigma_{+}$cannot become smaller than $1 / 2-\epsilon$ once it has been larger than $1 / 2-\epsilon / 2$ due to (84), (83), the fact that $\left|\Sigma_{+}^{\prime}\right|$ is uniformly bounded and the fact that the distance between two zeros of $\Sigma_{-}$goes to zero as $\tau \rightarrow \infty$.

Combining this observation with Lemma 15 we conclude that
$$\lim _{\tau \rightarrow \infty} \Sigma_{+}(\tau)=\frac{1}{2} .$$
The constraint (7) then yields
$$-N_{1}\left(N_{2}+N_{3}\right) \leq \frac{2}{3}\left(1-\Sigma_{+}^{2}-\Sigma_{-}^{2}-\frac{3}{4}\left(N_{2}-N_{3}\right)^{2}-\frac{3}{4} N_{1}^{2}\right) \leq \frac{2}{3}\left(1-\Sigma_{+}^{2}\right) .$$
Since the right hand side converges to $\frac{1}{2}$ we can use Lemma 17 to conclude that
$$\lim _{\tau \rightarrow \infty} N_{1}\left(N_{2}+N_{3}\right)=-\frac{1}{2} .$$
By the constraint we can then conclude that
$$\lim _{\tau \rightarrow \infty}\left(N_{2}-N_{3}\right)=0$$
and
$$\lim _{\tau \rightarrow \infty} \Sigma_{-}=0 .$$ \(\square\)

\section*{9. Conclusions}

For all class A spacetimes except IX, $q$ converges to a non-zero value as $\tau \rightarrow \infty$. Thus, by (27), the following theorem follows.

Theorem 2. For all Bianchi class A vacuum spacetimes except those of type IX, the asymptotic behaviour of the reduced Hamiltonian in the expanding direction is given by
$$\lim _{\tau \rightarrow \infty} H_{\text {reduced }}(\tau)=0 .$$
Consider the metric $\tilde{g}$. By (22) we have
$$\tilde{g}(\tau)=\sum_{i=1}^{3} \lambda_{i}(\tau) \xi^{i} \otimes \xi^{i}$$
where
$$\lambda_{i}(\tau)=\exp \left(\int_{0}^{\tau} 6 \Sigma_{i} d \tau^{\prime}\right)$$
by (24). Note that $\Sigma_{i}$ is a vector determined by $\Sigma_{+}$and $\Sigma_{-}$and that the sum of its components is zero. Let us introduce some terminology.

Definition 4. If two $\lambda_{i}$ converge to zero and one to infinity, we say that the evolution exhibits a cigar degeneracy. If one $\lambda_{i}$ converges to zero and two to infinity, we call it a pancake degeneracy.
9.1. Bianchi I. In this case the $\Sigma_{i}$ are constants satisfying
$$\sum_{i=1}^{3} \Sigma_{i}^{2}=\frac{2}{3} .$$
Thus $\lambda_{i}$ converges to $0, \infty$ or 1 depending on the solution. We get both pancakes and cigars. Concerning the $a_{i}$ in (25), we observe that if the Bianchi I solution corresponds to a special point on the Kasner circle, then two $a_{i}$ are constant and one goes to zero. For all other Bianchi I solutions, one $a_{i}$ goes to infinity and the other two to zero.
9.2. Bianchi II. The $\Sigma_{i}$ converge to $s_{i}$ where the $s_{i}$ satisfy
$$\sum_{i=1}^{3} s_{i}^{2}=\frac{2}{3} .$$
The points $\left(s_{1}, s_{2}, s_{3}\right)=\left(\frac{2}{3},-\frac{1}{3},-\frac{1}{3}\right)$ and the ones obtained by permutating its coordinates are however not allowed as limit points (they correspond to the flat Kasner vacuum solutions). Again we get pancakes or cigars depending on the solution. As far as the $a_{i}$ :s are concerned, one goes to infinity and two go to zero.
9.3. Bianchi $\mathbf{V I}_{0}$. In this case the $\Sigma_{i}$ converge to $\left(\frac{2}{3},-\frac{1}{3},-\frac{1}{3}\right)$ or one of the points obtained by permuting its coordinates. We get a cigar degeneracy.
Considering the $a_{i}$, (25) shows that one of the $a_{i}$ goes to zero, but what happens to the other two is unclear.

Proposition 8. Consider a Bianchi $V I_{0}$ solution to (5)-(7). Then all the $a_{i}$ converge to zero as $\tau \rightarrow \infty$.

Proof. Considering (25) and (26), we are interested in the integrals
$$\int_{0}^{\tau}\left(1+\Sigma_{+} \pm \sqrt{3} \Sigma_{-}\right) d s=\frac{1}{2} \int_{0}^{\tau}\left(2+2 \Sigma_{+} \pm 2 \sqrt{3} \Sigma_{-}\right) d s .$$
Observe however that
$$\left(1+\Sigma_{+}\right)^{\prime}=-(2-q)\left(1+\Sigma_{+}\right)$$
whence
$$1+\Sigma_{+}(\tau)=\exp \left[-\int_{0}^{\tau}(2-q) d s\right]\left[1+\Sigma_{+}(0)\right]$$
so that, using the expressions for $N_{2}^{\prime}$ and $N_{3}^{\prime}$ in (5), we get
$$a_{2}^{-2}=c_{2} \frac{N_{2}}{1+\Sigma_{+}}$$
and
$$a_{3}^{-2}=c_{3} \frac{-N_{3}}{1+\Sigma_{+}}$$
where $c_{2}$ and $c_{3}$ are positive constants. Consider now the function
$$Z_{1}=\frac{\frac{4}{3} \Sigma_{-}^{2}+\left(N_{2}-N_{3}\right)^{2}}{-N_{2} N_{3}} .$$

This function is monotone decreasing to the future, and bounded from below by 2 , since
$$\left(N_{2}-N_{3}\right)^{2} \geq-2 N_{2} N_{3} .$$
Thus it converges to a positive real number, and in consequence, the same is true of $1 / Z_{1}$. Thus, using the constraint,
$$\frac{-N_{2} N_{3}}{1+\Sigma_{+}}=\frac{4}{3}\left(1-\Sigma_{+}\right) \frac{-N_{2} N_{3}}{\frac{4}{3}\left(1-\Sigma_{+}^{2}\right)}=\frac{4}{3}\left(1-\Sigma_{+}\right) \frac{1}{Z_{1}} \rightarrow \alpha$$
where $\alpha$ is a positive real number. Since $N_{2}$ and $N_{3}$ converge to zero as $\tau \rightarrow \infty$ by Proposition 2, we conclude that $a_{2}$ and $a_{3}$ converge to zero. □
9.4. Bianchi VII ${ }_{0}$. There are two possibilities. Either the $\Sigma_{i}$ are constants equal to $\left(-\frac{2}{3}, \frac{1}{3}, \frac{1}{3}\right)$, to $\left(\frac{2}{3},-\frac{1}{3},-\frac{1}{3}\right)$ or one of the vectors obtained by permuting the coordinates or they converge to $\left(\frac{2}{3},-\frac{1}{3},-\frac{1}{3}\right)$ (or a permuted vector). The first possibility yields a pancake or cigar degeneracy. The second possibility yields a cigar degeneracy.
Considering the $a_{i}$ we have the following proposition.
Proposition 9. Consider a Bianchi VII ${ }_{0}$ solution to (5)-(7). Then all the $a_{i}$ converge to zero as $\tau \rightarrow \infty$.

Proof. The argument is similar to the Bianchi $\mathrm{VI}_{0}$ case, but easier. We just need to observe that $N_{2}, N_{3}$ are bounded away from zero, and $1+\Sigma_{+} \rightarrow 0$ by Lemma 6 and Proposition 5. □
9.5. Bianchi VIII. In this case the $\Sigma_{i}$ converge to $\left(-\frac{1}{3}, \frac{1}{6}, \frac{1}{6}\right)$ up to permutations. We have a pancake singularity.
Let us also consider what happens to the $a_{i}$ appearing in (19). Considering (25), two of the $a_{i}$ converge to zero, but what happens to the third one is more difficult to say, since the integrand tends to zero. Here we wish to prove that it is bounded away from infinity.

Proposition 10. Consider a Bianchi VIII solution to (5)-(7). The $a_{i}$ in (19) are bounded as $\tau \rightarrow \infty$.

Proof. As already mentioned two of the $a_{i}$ converge to zero. Let us consider the third one. Since $\Sigma_{1}=-2 \Sigma_{+} / 3$, we have
$$a_{1}(\tau)=\exp \left(\int_{0}^{\tau}\left(2 \Sigma_{+}-1\right) d s\right),$$
and in consequence our goal is to prove that $\Sigma_{+}$does not get that much bigger than $\frac{1}{2}$. By Theorem 1, we conclude that $q-4 \Sigma_{+} \rightarrow-\frac{3}{2}$, so that there is a $T_{1}$ such that
$$N_{1}(\tau) \leq e^{-\tau}$$
for all $\tau \geq T_{1}$. Using the constraint (7) to eliminate $N_{1}\left(N_{2}+N_{3}\right)$, we deduce
$$\Sigma_{+}^{\prime}=-\left(1-\Sigma_{+}^{2}-\Sigma_{-}^{2}\right)\left(2 \Sigma_{+}-1\right)-\frac{9}{4}\left(N_{2}-N_{3}\right)^{2}+\frac{9}{4} N_{1}^{2} .$$

Observe that in the first term, $1-\Sigma_{+}^{2}-\Sigma_{-}^{2} \rightarrow \frac{3}{4}$. The term involving $N_{1}^{2}$ is undesireable, but it can be handled in the following way. Let
$$f=\Sigma_{+}-\frac{1}{2}+N_{1} .$$
Then
$$f^{\prime}=-\left(1-\Sigma_{+}^{2}-\Sigma_{-}^{2}\right)\left(2 \Sigma_{+}-1\right)-\frac{9}{4}\left(N_{2}-N_{3}\right)^{2}+\frac{9}{4} N_{1}^{2}+\left(q-4 \Sigma_{+}\right) N_{1} .$$
If $\Sigma_{+}(\tau)>\frac{1}{2}$, and if $\tau$ is greater than some $T_{2}$, then we can absorb the term involving $N_{1}^{2}$ in the term arising from the derivative of $N_{1}$, and conclude that
$$f^{\prime}(\tau) \leq-\alpha f(\tau),$$
where $1>\alpha>0$ is a suitable constant. If there is a $T$ such that $\Sigma_{+}(\tau) \leq \frac{1}{2}$ for all $\tau \geq T$, we are done, so assume not. Let us divide the problem into two subcases. Either there is a $T \geq T_{1}, T_{2}$ such that $\Sigma_{+}(\tau)>\frac{1}{2}$ for all $\tau \geq T$, or there is a time sequence $\tau_{k} \rightarrow \infty$ such that $\Sigma_{+}\left(\tau_{k}\right)=\frac{1}{2}$. It is convenient to assume $\tau_{1} \geq T_{1}, T_{2}$ in this case. In the first case, we have
$$f(\tau) \leq f(T) \exp [-\alpha(\tau-T)]$$
by integrating (86), and in particular
$$0 \leq \Sigma_{+}(\tau)-\frac{1}{2} \leq f(T) \exp [-\alpha(\tau-T)]$$
so that the integral appearing in (85) is finite. Consider now the second subcase. Assume $\Sigma_{+}(\tau)>1 / 2$ with $\tau>\tau_{1}$. Let $t<\tau$ be the first point before $\tau$ at which $\Sigma_{+}(t)=\frac{1}{2}$. Then
$$f(\tau) \leq f(t) \exp [-\alpha(\tau-t)] \leq \exp [-t-\alpha(\tau-t)] \leq \exp [-\alpha \tau]$$
since $\alpha<1$ and $f(t)=N_{1}(t) \leq e^{-t}$. Thus the integral appearing in (85) cannot diverge to infinity. □

\section*{Acknowledgements}

This research was supported in part by the National Science Foundation under Grant No. PHY94-07194. Part of this work was carried out while the author was enjoying the hospitality of the Institute for Theoretical Physics, Santa Barbara. The author also wishes to acknowledge the support of Royal Swedish Academy of Sciences. The main motivation for writing this article originated in the work of Fischer and Moncrief, and the author is grateful to Lars Andersson for suggesting the problem and Alan Rendall for suggesting improvements.

\section*{References}
\begin{itemize}
\item[] [1] Ellis G and MacCallum M 1969 A class of homogenous cosmological models Commun. Math. Phys. 12 108-41
\item[] [2] Wainwright J and Hsu L 1989 A dynamical systems approach to Bianchi cosmologies: orthogonal models of class A Class. Quantum Grav. 6 1409-31
\item[] [3] Wainwright J, Hancock M J and Uggla C 1999 Asymptotic self-similarity breaking at late times in cosmology Class. Quantum Grav. 16 2577-98
\item[] [4] Ringström H 2000 The Bianchi IX attractor Preprint gr-qc/0006035
\item[] [5] Fischer A and Moncrief V 1999 The Einstein flow, the $\sigma$-constant and the geometrization of 3-manifolds Class. Quantum Grav. 16 L79-L87
\item[] [6] Barrow J and Gaspar Y 2001 Bianchi VIII empty futures Preprint gr-qc/0102004
\end{itemize}
[7] Irwin M C 1980 Smooth dynamical systems, Academic Press

Max-Planck-Institut für Gravitationsphysik, Am Mühlenberg 1, D-14476 Golm, GerMANY