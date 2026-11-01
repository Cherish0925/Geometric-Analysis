---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 1802_04454.pdf
converter: mathpix
format: mmd
---

\title{
RIGIDITY OF EINSTEIN METRICS AS CRITICAL POINTS OF QUADRATIC CURVATURE FUNCTIONALS ON CLOSED MANIFOLDS
}

\author{
BINGQING MA, GUANGYUE HUANG, XINGXIAO LI, AND YU CHEN
}

\begin{abstract}
In this paper, we prove some rigidity results for the Einstein metrics as the critical points of a family of known quadratic curvature functionals on closed manifolds, characterized by some point-wise inequalities. Moreover, we also provide a few rigidity results that involve the Weyl curvature, the trace-less Ricci curvature and the Yamabe invariant, accordingly.
\end{abstract}

\section*{1. Introduction}

In this paper, we always assume that $M^{n}$ is a closed manifold of dimension $n \geq 3$ and $g$ a Riemannian metric on $M^{n}$ with the Riemannian curvature tensor $R_{i j k l}$, the Ricci tensor $R_{i j}$ and the scalar curvature $R$. It is well-known that any Einstein metric $g$ must be critical for the Einstein-Hilbert functional
$$\mathcal{H}=\int_{M} R$$
defined on the space $\mathscr{M}_{1}\left(M^{n}\right)$ of equivalence classes of smooth Riemannian metrics of volume one on $M^{n}$. On the other hand, Catino considered in [4] the following family of quadratic curvature functionals
$$\mathcal{F}_{t}=\int_{M}\left|R_{i j}\right|^{2}+t \int_{M} R^{2}, \quad t \in \mathbb{R}$$
which are also defined on $\mathscr{M}_{1}\left(M^{n}\right)$, and proved some related rigidity results. Furthermore, it has been observed in [2] that every Einstein metric is a critical point of $\mathcal{F}_{t}$ for all $t \in \mathbb{R}$, see (2.5) below. But the converse of this conclusion is not true in general.

Therefore it is natural to ask that under what conditions a critical metric for the functionals $\mathcal{F}_{t}$ must be a Einstein one. In fact, there have been a number of interesting conclusions to this problem, for example, under some suitable curvature conditions ( [4,15,16]), or under some integral conditions ( [9, 13]). For other development in this direction, we refer the readers to [1, 3, 10, 11] and the references therein.

\footnotetext{
2010 Mathematics Subject Classification. Primary 51H25, Secondary 53C21.
Key words and phrases. Critical metric, Yamabe invariant, Einstein, rigidity.
Research supported by NSFC (Nos. 11401179, 11371018, 11671121).
}

Recall that the Yamabe invariant $Y_{M}([g])$ is defined by
$$\begin{aligned}
Y_{M}([g]) & =\inf _{\tilde{g} \in[g]} \frac{\int_{M} \tilde{R} d v_{\tilde{g}}}{\left(\int_{M} d v_{\tilde{g}}\right)^{\frac{n-2}{n}}} \\
& =\frac{4(n-1)}{n-2} \inf _{u \in W^{1,2}\left(M^{n}\right)} \frac{\int_{M}|\nabla u|^{2} d v_{g}+\frac{n-2}{4(n-1)} \int_{M} R u^{2} d v_{g}}{\left(\int_{M}|u|^{\frac{2 n}{n-2}} d v_{g}\right)^{\frac{n-2}{n}}},
\end{aligned}$$
where $[g]$ is the conformal class of the metric $g$. It then follows that
$$\begin{aligned}
\frac{n-2}{4(n-1)} Y_{M}([g]) & \left(\int_{M}|u|^{\frac{2 n}{n-2}} d v_{g}\right)^{\frac{n-2}{n}} \\
\leq & \int_{M}|\nabla u|^{2} d v_{g}+\frac{n-2}{4(n-1)} \int_{M} R u^{2} d v_{g}
\end{aligned}$$
for all $u \in W^{1,2}\left(M^{n}\right)$. Moreover, $Y_{M}([g])$ is positive if and only if there exists a conformal metric in $[g]$ with everywhere positive scalar curvature.

In the present paper, by using some pinching conditions involving the Weyl curvature, the trace-less Ricci curvature and the Yamabe invariant, we aim to prove a number of rigidity theorems for the Einstein metrics considered as the critical points of the functional family $\mathcal{F}_{t}(t \in R)$. For convenience, we shall use Ric and $W$ throughout this paper to denote the trace-less Ricci curvature and the Weyl curvature, respectively.

Our main results are stated as follows.
Theorem 1.1. Let $\left(M^{n}, g\right)$ be a closed Riemannian manifold of dimension $n \geq 3$ with positive scalar curvature and $g$ is a critical metric for the functional family $\mathcal{F}_{t}$ over $\mathscr{M}_{1}\left(M^{n}\right)$, where
$$\begin{cases}t<-\frac{5}{12}, & \text { if } n=3 ; \\ t<-\frac{1}{3}, & \text { if } n=4 ; \\ t \leq-\frac{n}{4(n-1)}, & \text { if } n \geq 5 .\end{cases}$$
Suppose that
$$\begin{aligned}
\mid W- & \left.\frac{n-4}{\sqrt{2 n}(n-2)} \operatorname{Ric} \otimes g \right\rvert\, \\
& <-\sqrt{\frac{2}{(n-1)(n-2)}}\left(\frac{2(n-2)+2 n(n-1) t}{n}+1\right) R .
\end{aligned}$$
Then $\left(M^{n}, g\right)$ must be of Einstein.
In particular, when $n=3$, we have $W=0$ automatically. On the other hand, from (2.2) it is seen that an Einstein manifold $M^{3}$ with positive scalar curvature must be of constant positive sectional curvature. Moreover, it follows from Lemma 2.3 that $\mid$ Ric $\mathbb{O} g|=2|$ Ric $\mid$ on $M^{3}$. Consequently, the following conclusion is immediate by Theorem 1.1.

Corollary 1.2. Let $\left(M^{3}, g\right)$ be as in Theorem 1.1 with $n=3$. If
$$|\operatorname{Ric}|<-\frac{5+12 t}{\sqrt{6}} R, \quad \text { for } \quad t<-\frac{5}{12},$$
then $\left(M^{3}, g\right)$ must be of constant positive sectional curvature.
Next, for $t=-\frac{1}{2}$, we give rigidity results by using pointwise inequalities.
Theorem 1.3. Let $\left(M^{n}, g\right)$ be a closed Riemannian manifold of dimension $n \geq 3$ with positive scalar curvature and $g$ is a critical metric for the functional $\mathcal{F}_{-\frac{1}{2}}$ over $\mathscr{M}_{1}\left(M^{n}\right)$. Suppose that
$$\left|W+\frac{\sqrt{2}}{\sqrt{n}(n-2)} \operatorname{Ric} \otimes g\right| \leq \frac{n^{2}-3 n+4}{n \sqrt{2(n-1)(n-2)}} R .$$
If there exists a point where the inequality in (1.7) is strict, then $\left(M^{n}, g\right)$ must be of Einstein.

To state the next theorem, we first introduce a constant
$$C_{n}= \begin{cases}\frac{1}{\sqrt{6}}, & \text { if } n=4 ; \\ \frac{3 \sqrt{15}-6}{8 \sqrt{10}}, & \text { if } n=5 ; \\ \frac{2}{n}\left(\frac{2(n-2)}{\sqrt{n(n-1)}}+\frac{n^{2}-n-4}{\sqrt{n(n-1)(n+1)(n-2)}}\right)^{-1}, & \text { if } n \geq 6 .\end{cases}$$
Then, in terms of the Yamabe invariant, we have the following theorem:
Theorem 1.4. Let $\left(M^{n}, g\right)$ be a closed Riemannian manifold of dimension $n \geq 3$ with positive scalar curvature and $g$ is a critical metric for the functional $\mathcal{F}_{t}\left(t \leq-\frac{1}{2}\right)$ over $\mathscr{M}_{1}\left(M^{n}\right)$. Suppose that
$$\left(\int_{M}\left|W+\frac{\sqrt{2}}{\sqrt{n}(n-2)} \operatorname{Ric} \otimes g\right|^{\frac{n}{2}}\right)^{\frac{2}{n}} \leq \frac{1}{4} \sqrt{\frac{n-2}{2(n-1)}} Y_{M}([g]) .$$
Then $\left(M^{n}, g\right)$ must be of Einstein. Furthermore,
(1) if $n=3,4,5$, then (1.9) implies that $\left(M^{n}, g\right)$ is of constant positive sectional curvature;
(2) if $n \geq 6$ and (1.9) is replaced with
$$\left(\int_{M}\left|W+\frac{\sqrt{2}}{\sqrt{n}(n-2)} \operatorname{Ric} \otimes g\right|^{\frac{n}{2}}\right)^{\frac{2}{n}}<C_{n} Y_{M}([g]),$$
then $\left(M^{n}, g\right)$ must be of constant positive sectional curvature.
Corollary 1.5. Let $\left(M^{4}, g\right)$ be as in Theorem 1.4 with $n=4$. Suppose that
$$\int_{M}\left(|W|^{2}+\frac{5}{4}\left|\stackrel{\circ}{R}_{i j}\right|^{2}\right) \leq \frac{1}{48} \int_{M} R^{2} .$$
Then, $\left(M^{4}, g\right)$ must be of constant positive sectional curvature.
For a four dimensional Riemannian manifold, we also have the following rigidity theorem:

Theorem 1.6. Let $\left(M^{4}, g\right)$ be closed with positive scalar curvature and $g$ be critical for $\mathcal{F}_{t}$ over $\mathscr{M}_{1}\left(M^{4}\right)$, where
$$-\frac{1}{4} \leq t<-\frac{1}{6} .$$
Suppose that
$$\left(\int_{M}\left|W+\frac{1}{2 \sqrt{2}} \operatorname{Ric} \otimes g\right|^{2}\right)^{\frac{1}{2}}<-\frac{1+6 t}{2 \sqrt{3}} Y_{M}([g]) .$$
Then, $\left(M^{4}, g\right)$ must be of constant positive sectional curvature.
Corollary 1.7. Let $\left(M^{4}, g\right)$ be as in Theorem 1.6. If
$$\int_{M}\left(|W|^{2}+\left[1+(1+6 t)^{2}\right]\left|\stackrel{\circ}{R}_{i j}\right|^{2}\right) \leq \frac{(1+6 t)^{2}}{12} \int_{M} R^{2},$$
then $\left(M^{4}, g\right)$ must be of constant positive sectional curvature.
We remark that our rigidity results in both Corollary 1.5 and Corollary 1.7 can also be described in terms of the Euler-Poincaré characteristic. In fact, by the well-known Chern-Gauss-Bonnet formula ( [2, Equation 6.31])
$$\int_{M}\left(\left.\left|W^{2}-2\right| \stackrel{\circ}{R}_{i j}\right|^{2}+\frac{1}{6} R^{2}\right)=32 \pi^{2} \chi(M),$$
with $\chi(M)$ being the Euler-Poincaré characteristic of $M^{4}$, the pinching conditions (1.11) and (1.14) are equivalent to
$$\frac{13}{2} \int_{M}|W|^{2}+\frac{1}{3} \int_{M} R^{2} \leq 80 \pi^{2} \chi(M)$$
and
$$\frac{3+(1+6 t)^{2}}{2} \int_{M}|W|^{2}+\frac{1}{12} \int_{M} R^{2} \leq 16\left[1+(1+6 t)^{2}\right] \pi^{2} \chi(M),$$
respectively. So we have the following corollary.
Corollary 1.8. Let $\left(M^{4}, g\right)$ be closed with positive scalar curvature. If either (1) $g$ is the critical point of $\mathcal{F}_{t}$ over $\mathscr{M}_{1}\left(M^{4}\right)$ with $t \leq-\frac{1}{2}$, and $\left(M^{4}, g\right)$ satisfies (1.16), or (2) $g$ is the critical point of $\mathcal{F}_{t}$ over $\mathscr{M}_{1}\left(M^{4}\right)$ with (1.12), and $\left(M^{4}, g\right)$ satisfies (1.17), then $\left(M^{4}, g\right)$ must be of constant positive sectional curvature.

Remark 1.1. It should be emphasized that our Corollary 1.2 greatly improves a similar Theorem of Catino in [4].

In fact, combining with Remark 1.7 of Catino [4] and (i) of Theorem 1.1 in [13], the mentioned Theorem of Catino can be stated as follows:

Theorem 1.9 ( [4], Theorem 1.5). Let $\left(M^{3}, g\right)$ be a Riemannian manifold with positive scalar curvature and $g$ be a critical metric for $\mathcal{F}_{t}$ with $t \in$
$\left(-\infty,-\frac{1}{2}\right] \cup\left[-\varepsilon_{0},-\frac{1}{6}\right)$, where $\varepsilon_{0} \approx 0.3652$. Then $g$ must have constant positive sectional curvature if
$$|\operatorname{Ric}|<-\frac{1+6 t}{2 \sqrt{6}} R .$$

But it is easy to check that
$$-\frac{1+6 t}{2 \sqrt{6}}<-\frac{5+12 t}{\sqrt{6}}, \quad \text { for } t \in\left(-\infty,-\frac{1}{2}\right),$$
which shows that our pinching condition (1.6) is better than that of Catinos' in this case. Furthermore, the interval $\left(-\infty,-\frac{5}{12}\right)$ we use for $t$ is clearly larger than the interval $\left(-\infty,-\frac{1}{2}\right] \cup\left[-\varepsilon_{0},-\frac{1}{6}\right)$ used by Catinos.

We should remark that, when $n \geq 4$, our Theorem 1.1 also generalizes the conclusion (ii) of Theorem 1.1 in [13].

Acknowledgment. The second author of this paper thanks Professor Haiping Fu for sending him the recent achievements in this direction.

\section*{2. Some necessary lemmas}

Recall that the Weyl curvature $W_{i j k l}$ of a Riemannian manifold $\left(M^{n}, g\right)$ with $n \geq 3$ is related to the Riemannian curvature $R_{i j k l}$ by
$$\begin{aligned}
W_{i j k l}= & R_{i j k l}-\frac{1}{n-2}\left(R_{i k} g_{j l}-R_{i l} g_{j k}+R_{j l} g_{i k}-R_{j k} g_{i l}\right) \\
& +\frac{R}{(n-1)(n-2)}\left(g_{i k} g_{j l}-g_{i l} g_{j k}\right) .
\end{aligned}$$
Since the traceless Ricci curvature $\stackrel{\circ}{R}_{i j}=R_{i j}-\frac{R}{n} g_{i j}$, (2.1) can be written as
$$\begin{aligned}
W_{i j k l}= & R_{i j k l}-\frac{1}{n-2}\left(\stackrel{\circ}{R}_{i k} g_{j l}-\stackrel{\circ}{R}_{i l} g_{j k}+\stackrel{\circ}{R}_{j l} g_{i k}-\stackrel{\circ}{R}_{j k} g_{i l}\right) \\
& -\frac{R}{n(n-1)}\left(g_{i k} g_{j l}-g_{i l} g_{j k}\right) .
\end{aligned}$$
Furthermore, the Cotton tensor is defined by
$$\begin{aligned}
C_{i j k} & =R_{k j, i}-R_{k i, j}-\frac{1}{2(n-1)}\left(R_{, i} g_{j k}-R_{, j} g_{i k}\right) \\
& =\stackrel{\circ}{R}_{k j, i}-\stackrel{\circ}{R}_{k i, j}+\frac{n-2}{2 n(n-1)}\left(R_{, i} g_{j k}-R_{, j} g_{i k}\right),
\end{aligned}$$
where the indices after a comma denote the covariant derivatives. Then the divergence of the Weyl curvature tensor is related to the Cotton tensor by
$$-\frac{n-3}{n-2} C_{i j k}=W_{i j k l, l} .$$

It has been shown by Catino in [4, Proposition 2.1] that a metric $g$ is critical for $\mathcal{F}_{t}$ over $\mathscr{M}_{1}\left(M^{n}\right)$ if and only if it satisfies the following equations
$$\begin{aligned}
\Delta \stackrel{\circ}{\mathrm{R}}_{i j}= & (1+2 t) R_{, i j}-\frac{1+2 t}{n}(\Delta R) g_{i j}-2 R_{i k j l} \stackrel{\circ}{\mathrm{R}}_{k l} \\
& -\frac{2+2 n t}{n} R \stackrel{\circ}{\mathrm{R}}_{i j}+\frac{2}{n}\left|\stackrel{\circ}{\mathrm{R}}_{i j}\right|^{2} g_{i j} \\
{[n+4(n-1) t] \Delta R=} & (n-4)\left[\left|R_{i j}\right|^{2}+t R^{2}-\lambda\right],
\end{aligned}$$
where $\lambda=\mathcal{F}_{t}(g)$.
It is easy to see from (2.5) that
$$\begin{aligned}
\frac{1}{2} \Delta\left|\stackrel{\circ}{\mathrm{R}}_{i j}\right|^{2}= & \left|\nabla \stackrel{\circ}{\mathrm{R}}_{i j}\right|^{2}+\stackrel{\circ}{\mathrm{R}}_{i j} \Delta \stackrel{\circ}{\mathrm{R}}_{i j} \\
= & \left|\nabla \stackrel{\circ}{\mathrm{R}}_{i j}\right|^{2}+(1+2 t) \stackrel{\circ}{\mathrm{R}}_{i j} R_{, i j}-2 R_{i k j l} \stackrel{\circ}{\mathrm{R}}_{k l} \stackrel{\circ}{\mathrm{R}}_{i j}-\frac{2+2 n t}{n} R\left|\stackrel{\circ}{\mathrm{R}}_{i j}\right|^{2} \\
= & \left|\nabla \stackrel{\circ}{\mathrm{R}}_{i j}\right|^{2}+(1+2 t) \stackrel{\circ}{\mathrm{R}}_{i j} R_{, i j}-\frac{2(n-2)+2 n(n-1) t}{n(n-1)} R\left|\stackrel{\circ}{\mathrm{R}}_{i j}\right|^{2} \\
& +\frac{4}{n-2} \stackrel{\circ}{\mathrm{R}}_{i j} \stackrel{\circ}{\mathrm{R}}_{j k} \stackrel{\circ}{\mathrm{R}}_{k i}-2 W_{i k j l} \stackrel{\circ}{\mathrm{R}}_{k l} \stackrel{\circ}{\mathrm{R}}_{i j} .
\end{aligned}$$
Integrating both sides of (2.7) yields
$$\begin{aligned}
0= & \int_{M}\left|\nabla \stackrel{\circ}{\mathrm{R}}_{i j}\right|^{2}-\int_{M}\left(2 W_{i k j l} \stackrel{\circ}{\mathrm{R}}_{k l} \stackrel{\circ}{\mathrm{R}}_{i j}-\frac{4}{n-2} \stackrel{\circ}{\mathrm{R}}_{i j} \stackrel{\circ}{\mathrm{R}}_{j k} \stackrel{\circ}{\mathrm{R}}_{k i}\right. \\
& \left.+\frac{2(n-2)+2 n(n-1) t}{n(n-1)} R\left|\stackrel{\circ}{\mathrm{R}}_{i j}\right|^{2}\right)-(1+2 t) \int_{M} \stackrel{\circ}{\mathrm{R}}_{i j, j} R_{, i} \\
= & \int_{M}\left|\nabla \stackrel{\circ}{\mathrm{R}}_{i j}\right|^{2}-\int_{M}\left(2 W_{i k j l} \stackrel{\circ}{\mathrm{R}}_{k l} \stackrel{\circ}{\mathrm{R}}_{i j}-\frac{4}{n-2} \stackrel{\circ}{\mathrm{R}}_{i j} \stackrel{\circ}{\mathrm{R}}_{j k} \stackrel{\circ}{\mathrm{R}}_{k i}\right. \\
& \left.+\frac{2(n-2)+2 n(n-1) t}{n(n-1)} R\left|\stackrel{\circ}{\mathrm{R}}_{i j}\right|^{2}\right)-\frac{(n-2)(1+2 t)}{2 n} \int_{M}|\nabla R|^{2}
\end{aligned}$$
where we have used $\stackrel{\circ}{\mathrm{R}}_{i j, j}=\frac{n-2}{2 n} R_{, i}$ in the second equality. Thus, we obtain the following result:

Lemma 2.1. Let $M^{n}$ be a closed manifold and $g$ be a critical metric for $\mathcal{F}_{t}$ on $\mathscr{M}_{1}\left(M^{n}\right)$. Then
$$\begin{aligned}
& \int_{M}\left|\nabla \stackrel{\circ}{R}_{i j}\right|^{2}=\int_{M}\left(2 W_{i j k l} \stackrel{\circ}{R}_{j l} \stackrel{\circ}{R}_{i k}-\frac{4}{n-2} \stackrel{\circ}{R}_{i j} \stackrel{\circ}{R}_{j k} \stackrel{\circ}{R}_{k i}\right. \\
& \left.\quad+\frac{2(n-2)+2 n(n-1) t}{n(n-1)} R\left|\stackrel{\circ}{R}_{i j}\right|^{2}+\frac{(n-2)(1+2 t)}{2 n}|\nabla R|^{2}\right) .
\end{aligned}$$

Next, by combining the relationship
$$R_{i j k l} \stackrel{\circ}{R}_{j l} \stackrel{\circ}{R}_{i k}=W_{i j k l} \stackrel{\circ}{R}_{j l} \stackrel{\circ}{R}_{i k}-\frac{1}{n(n-1)} R\left|\stackrel{\circ}{R}_{i j}\right|^{2}-\frac{2}{n-2} \stackrel{\circ}{R}_{i j} \stackrel{\circ}{R}_{j k} \stackrel{\circ}{R}_{k i}$$
with Proposition 4.1 in [4] (for the case of dimension three, see [9, Sect. 4]), we obtain

Lemma 2.2. Let $M^{n}$ be a closed manifold. Then
$$\begin{aligned}
\int_{M}\left|\nabla \stackrel{\circ}{R}_{i j}\right|^{2}= & \int_{M}\left(W_{i j k l} \stackrel{\circ}{R}_{j l} \stackrel{\circ}{R}_{i k}-\frac{n}{n-2} \stackrel{\circ}{R}_{i j} \stackrel{\circ}{R}_{j k} \stackrel{\circ}{R}_{k i}\right. \\
& \left.-\frac{1}{n-1} R\left|\stackrel{\circ}{R}_{i j}\right|^{2}+\frac{(n-2)^{2}}{4 n(n-1)}|\nabla R|^{2}+\frac{1}{2}\left|C_{i j k}\right|^{2}\right) .
\end{aligned}$$

The next lemma comes from [8,14] (for the case of $\lambda=\frac{2}{n-2}$, see [5]):
Lemma 2.3. For every Riemannian manifold ( $M^{n}, g$ ) and any $\lambda \in \mathbb{R}$, the following estimate holds
$$\begin{aligned}
& \left|-W_{i j k l} \stackrel{\circ}{R}_{j l} \stackrel{\circ}{R}_{i k}+\lambda \stackrel{\circ}{R}_{i j} \stackrel{\circ}{R}_{j k} \stackrel{\circ}{R}_{k i}\right| \\
& \quad \leq \sqrt{\frac{n-2}{2(n-1)}}\left(|W|^{2}+\frac{2(n-2) \lambda^{2}}{n}\left|\stackrel{\circ}{R}_{i j}\right|^{2}\right)^{\frac{1}{2}}\left|\stackrel{\circ}{R}_{i j}\right|^{2} \\
& \quad=\sqrt{\frac{n-2}{2(n-1)}}\left|W+\frac{\lambda}{\sqrt{2 n}} \stackrel{\circ}{\operatorname{Ric}} @ g\right|\left|\stackrel{\circ}{R}_{i j}\right|^{2} .
\end{aligned}$$

The following lemma comes from [6], or see [7, Proposition 1.3]:
Lemma 2.4. An Einstein manifold ( $M^{n}, g$ ) with positive scalar curvature is of constant positive sectional curvature, provided
$$\left(\int_{M}|W|^{\frac{n}{2}}\right)^{\frac{2}{n}}<C_{n} Y_{M}([g]),$$
where $C_{n}$ is given by (1.8).

\section*{3. Proof of the main results}
3.1. Proof of Theorem 1.1. Using (2.9) and (2.10), it is easy to see
$$\begin{aligned}
0= & \int_{M}\left[-W_{i j k l} \stackrel{\circ}{R}_{j l} \AA_{i k}-\frac{n-4}{n-2} \AA_{i j} \AA_{j k} \AA_{k i}\right. \\
& -\frac{1}{n-1}\left(\frac{2(n-2)+2 n(n-1) t}{n}+1\right) R\left|\AA_{i j}\right|^{2} \\
& \left.-\frac{n-2}{2 n}\left((1+2 t)-\frac{n-2}{2(n-1)}\right)|\nabla R|^{2}+\frac{1}{2}\left|C_{i j k}\right|^{2}\right] .
\end{aligned}$$
Substituting the estimate (2.11) with $\lambda=-\frac{n-4}{n-2}$ into (3.1) gives
$$\begin{aligned}
0 \geq \int_{M}[ & \left(-\sqrt{\frac{n-2}{2(n-1)}}\left|W-\frac{n-4}{\sqrt{2 n}(n-2)} \operatorname{Ric} \otimes g\right|\right. \\
& \left.-\frac{1}{n-1}\left(\frac{2(n-2)+2 n(n-1) t}{n}+1\right) R\right)\left|\stackrel{\circ}{R}_{i j}\right|^{2} \\
& \left.-\frac{n-2}{2 n}\left((1+2 t)-\frac{n-2}{2(n-1)}\right)|\nabla R|^{2}+\frac{1}{2}\left|C_{i j k}\right|^{2}\right] .
\end{aligned}$$

Note that, when $t$ satisfies (1.4),
$$\frac{2(n-2)+2 n(n-1) t}{n}+1<0, \quad(1+2 t)-\frac{n-2}{2(n-1)} \leq 0 .$$
Then we can use (1.5) to find
$$\begin{aligned}
0 \geq & \int_{M}\left[\left[-\sqrt{\frac{n-2}{2(n-1)}} \left\lvert\, W-\frac{n-4}{\sqrt{2 n}(n-2)}\right. \text { Ric } \oslash g \mid\right.\right. \\
& \left.-\frac{1}{n-1}\left(\frac{2(n-2)+2 n(n-1) t}{n}+1\right) R\right]\left|\stackrel{\circ}{R}_{i j}\right|^{2} \\
& \left.-\frac{n-2}{2 n}\left((1+2 t)-\frac{n-2}{2(n-1)}\right)|\nabla R|^{2}+\frac{1}{2}\left|C_{i j k}\right|^{2}\right] \geq 0,
\end{aligned}$$
which shows that $M^{n}$ is Einstein, completing the proof of Theorem 1.1.
3.2. Proof of Theorem 1.3. When $t=-\frac{1}{2}$, we have $(1+2 t) R_{, i j}=0$. Thus by (1.7), the formula (2.7) becomes
$$\begin{aligned}
\frac{1}{2} \Delta\left|\stackrel{\circ}{\mathrm{R}}_{i j}\right|^{2}= & \left|\nabla \stackrel{\circ}{\mathrm{R}}_{i j}\right|^{2}+\frac{n^{2}-3 n+4}{n(n-1)} R\left|\stackrel{\circ}{\mathrm{R}}_{i j}\right|^{2} \\
& +\frac{4}{n-2} \stackrel{\circ}{\mathrm{R}}_{i j} \stackrel{\circ}{\mathrm{R}}_{j k} \stackrel{\circ}{\mathrm{R}}_{k i}-2 W_{i k j l} \stackrel{\circ}{\mathrm{R}}_{k l} \stackrel{\circ}{\mathrm{R}}_{i j} \\
\geq & \left|\nabla \stackrel{\circ}{\mathrm{R}}_{i j}\right|^{2}+\left[\frac{n^{2}-3 n+4}{n(n-1)} R\right. \\
& \left.-\sqrt{\frac{2(n-2)}{n-1}}\left|W+\frac{\sqrt{2}}{\sqrt{n}(n-2)} \operatorname{Ric} \otimes g\right|\right]\left|\stackrel{\circ}{R}_{i j}\right|^{2} \geq 0
\end{aligned}$$
In this case, $\left|\stackrel{\circ}{\mathrm{R}}_{i j}\right|^{2}$ is subharmonic on $M^{n}$. Using the maximum principle, we obtain that $\left|\stackrel{\circ}{R}_{i j}\right|$ is constant and $\nabla \stackrel{\circ}{R}_{i j}=0$, implying that the Ricci curvature is parallel, hence the curvature tensor is harmonic and $R$ is constant. In particular, (3.4) becomes
$$\left[\frac{n^{2}-3 n+4}{n \sqrt{2(n-1)(n-2)}} R-\left|W+\frac{\sqrt{2}}{\sqrt{n}(n-2)} \operatorname{Ric} \otimes g\right|\right]\left|\stackrel{\circ}{R}_{i j}\right|^{2}=0 .$$
If there exists a point $x_{0}$ such that the inequality (1.7) is strict, then from (3.5) we have $\left|\dot{R}_{i j}\right|\left(x_{0}\right)=0$ which with the fact that $\left|\stackrel{\circ}{R}_{i j}\right|$ constant shows that $\stackrel{\circ}{R}_{i j}=0$, that is, $M^{n}$ is Einstein, completing the proof of Theorem 1.3.
3.3. Proof of Theorem 1.4. Using the Kato inequality $\left|\nabla \stackrel{\circ}{R}_{i j}\right| \geq|\nabla| \stackrel{\circ}{R}_{i j}| |$, we have from (2.9)
$$\begin{aligned}
\int_{M}|\nabla| \stackrel{\circ}{R}_{i j}| |^{2} \leq & \int_{M}\left(2 W_{i j k l} \stackrel{\circ}{R}_{j l} \stackrel{\circ}{R}_{i k}-\frac{4}{n-2} \stackrel{\circ}{R}_{i j} \stackrel{\circ}{R}_{j k} \stackrel{\circ}{R}_{k i}\right. \\
& +\frac{2(n-2)+2 n(n-1) t}{n(n-1)} R\left|\stackrel{\circ}{R}_{i j}\right|^{2} \\
& \left.+\frac{(n-2)(1+2 t)}{2 n}|\nabla R|^{2}\right),
\end{aligned}$$
which shows
$$\begin{aligned}
\int_{M}|\nabla| \AA_{i j} \mid \|^{2} \leq & \frac{(n-2)(1+2 t)}{2 n} \int_{M}|\nabla R|^{2} \\
& +\frac{2(n-2)+2 n(n-1) t}{n(n-1)} \int_{M} R\left|\AA_{i j}\right|^{2} \\
& +\sqrt{\frac{2(n-2)}{n-1}} \int_{M}\left|W+\frac{\sqrt{2}}{\sqrt{n}(n-2)} \operatorname{Ric} \otimes g\right|\left|\stackrel{\circ}{R}_{i j}\right|^{2},
\end{aligned}$$
where we have used (2.11). This together with (1.3) gives
$$\begin{aligned}
& \frac{n-2}{4(n-1)} Y_{M}([g])\left(\int_{M}\left|\stackrel{\circ}{R}_{i j}\right|^{\frac{2 n}{n-2}} d v_{g}\right)^{\frac{n-2}{n}} \\
\leq & \frac{(n-2)(1+2 t)}{2 n} \int_{M}|\nabla R|^{2}+\frac{(n+8)(n-2)+8 n(n-1) t}{4 n(n-1)} \int_{M} R\left|\stackrel{\circ}{\mathrm{R}}_{i j}\right|^{2} \\
& +\sqrt{\frac{2(n-2)}{n-1}}\left(\int_{M}\left|W+\frac{\sqrt{2}}{\sqrt{n}(n-2)} \operatorname{Ric} \otimes g\right|^{\frac{n}{2}}\right)^{\frac{2}{n}}\left(\int_{M}\left|\stackrel{\circ}{R}_{i j}\right|^{\frac{2 n}{n-2}} d v_{g}\right)^{\frac{n-2}{n}},
\end{aligned}$$
where we have used the Hölder inequality
$$\begin{aligned}
& \int_{M}\left|W+\frac{\sqrt{2}}{\sqrt{n}(n-2)} \operatorname{Ric} \otimes g\right|\left|\AA_{i j}\right|^{2} \\
& \leq\left(\int_{M}\left|W+\frac{\sqrt{2}}{\sqrt{n}(n-2)} \operatorname{Ric} \otimes g\right|^{\frac{n}{2}}\right)^{\frac{2}{n}}\left(\int_{M}\left|\stackrel{\circ}{R}_{i j}\right|^{\frac{2 n}{n-2}} d v_{g}\right)^{\frac{n-2}{n}} .
\end{aligned}$$
In particular, (3.8) is equivalent to
$$\begin{aligned}
& {\left[\frac{n-2}{4(n-1)} Y_{M}([g])-\sqrt{\frac{2(n-2)}{n-1}}\left(\int_{M} \mid W\right.\right.} \\
& \left.\left.+\left.\frac{\sqrt{2}}{\sqrt{n}(n-2)} \operatorname{Ric} \oslash g\right|^{\frac{n}{2}}\right)^{\frac{2}{n}}\right]\left(\int_{M}\left|\stackrel{\circ}{R}_{i j}\right|^{\frac{2 n}{n-2}} d v_{g}\right)^{\frac{n-2}{n}} \\
& \leq \frac{(n-2)(1+2 t)}{2 n} \int_{M}|\nabla R|^{2}+\frac{(n+8)(n-2)+8 n(n-1) t}{4 n(n-1)} \int_{M} R\left|\stackrel{\circ}{R}_{i j}\right|^{2} .
\end{aligned}$$

It is easy to check that, for all $n$,
$$\frac{(n+8)(n-2)}{8 n(n-1)}<\frac{1}{2},$$
which shows that $1+2 t \leq 0$ implies $(n+8)(n-2)+8 n(n-1) t<0$. Hence, under the assumption (1.9), $M^{n}$ must be Einstein.

When $n=4,5$, then (1.9) becomes
$$\left(\int_{M}|W|^{\frac{n}{2}}\right)^{\frac{2}{n}} \leq \frac{1}{4} \sqrt{\frac{n-2}{2(n-1)}} Y_{M}([g])$$
since $M^{n}$ Einstein. By
$$\frac{1}{4} \sqrt{\frac{n-2}{2(n-1)}}<C_{n},$$
and with the help of Lemma 2.4, we can derive that $M^{n}$ is of constant positive sectional curvature, where $C_{n}$ is given by (1.8).

When $n \geq 6$, we can check that
$$C_{n}<\frac{1}{4} \sqrt{\frac{n-2}{2(n-1)}} .$$
Hence, if (1.10) holds, then (1.9) holds. So $M^{n}$ is of Einstein and hence, by Lemma 2.3, it is also of constant positive sectional curvature, completing the proof of Theorem 1.4.
3.4. Proof of Theorem 1.6. In order to prove Theorem 1.6, we shall need the following proposition.

Proposition 3.1. Let $M^{n}$ be a closed manifold with positive scalar curvature and $g$ be a critical metric for $\mathcal{F}_{t}$ on $\mathscr{M}_{1}\left(M^{n}\right)$ with $(1+2 t) R_{, i j}=0$. Then, for any $\alpha>\frac{1}{2}$, we have
$$\begin{aligned}
0 \geq & {\left[\left(2-\frac{1}{\alpha}\right) \frac{n-2}{4(n-1)} Y_{M}([g])\right.} \\
& \left.-\alpha \sqrt{\frac{2(n-2)}{n-1}}\left(\int_{M}\left|W+\frac{\sqrt{2}}{\sqrt{n}(n-2)} \mathrm{Ric}^{\circ} \otimes g\right|^{\frac{n}{2}}\right)^{\frac{2}{n}}\right] \\
& \times\left(\int_{M}\left|\stackrel{\circ}{R}_{i j}\right|^{\frac{2 n \alpha}{n-2}}\right)^{\frac{n-2}{n}}-\left[\frac{2 \alpha[(n-2)+n(n-1) t]}{n(n-1)}\right. \\
& \left.+\left(2-\frac{1}{\alpha}\right) \frac{n-2}{4(n-1)}\right] \int_{M} R\left|\stackrel{\circ}{\mathrm{R}}_{i j}\right|^{2 \alpha} .
\end{aligned}$$

Proof. Since $(1+2 t) R_{, i j}=0$, (2.7) becomes
$$\begin{aligned}
\left|\stackrel{\circ}{\mathrm{R}}_{i j}\right| \Delta\left|\stackrel{\circ}{\mathrm{R}}_{i j}\right| \geq & -\frac{2(n-2)+2 n(n-1) t}{n(n-1)} R\left|\stackrel{\circ}{\mathrm{R}}_{i j}\right|^{2} \\
& +\frac{4}{n-2} \stackrel{\circ}{\mathrm{R}}_{i j} \stackrel{\circ}{\mathrm{R}}_{j k} \stackrel{\circ}{\mathrm{R}}_{k i}-2 W_{i k j l} \stackrel{\circ}{\mathrm{R}}_{k l} \stackrel{\circ}{\mathrm{R}}_{i j} \\
\geq & -\sqrt{\frac{2(n-2)}{n-1}} \left\lvert\, W+\frac{\sqrt{2}}{\sqrt{n}(n-2)} \mathrm{R}^{\circ} \mathrm{ic}\right. \text { ( } \theta g\left|\left|\stackrel{\circ}{R}_{i j}\right|^{2}\right. \\
& -\frac{2(n-2)+2 n(n-1) t}{n(n-1)} R\left|\stackrel{\circ}{\mathrm{R}}_{i j}\right|^{2} .
\end{aligned}$$
Let $u=\left|\stackrel{\circ}{\mathrm{R}}_{i j}\right|$. Then for any $\alpha>0$, we have
$$\begin{aligned}
u^{\alpha} \Delta u^{\alpha}= & u^{\alpha}\left[\alpha(\alpha-1) u^{\alpha-2}|\nabla u|^{2}+\alpha u^{\alpha-1} \Delta u\right] \\
= & \left(1-\frac{1}{\alpha}\right)\left|\nabla u^{\alpha}\right|^{2}+\alpha u^{2 \alpha-2} u \Delta u \\
\geq & \left(1-\frac{1}{\alpha}\right)\left|\nabla u^{\alpha}\right|^{2}-\frac{2 \alpha[(n-2)+n(n-1) t]}{n(n-1)} R u^{2 \alpha} \\
& -\alpha \sqrt{\frac{2(n-2)}{n-1}}\left|W+\frac{\sqrt{2}}{\sqrt{n}(n-2)} \operatorname{Ric} \otimes g\right| u^{2 \alpha},
\end{aligned}$$
and hence
$$\begin{aligned}
0 \geq & \left(2-\frac{1}{\alpha}\right) \int_{M}\left|\nabla u^{\alpha}\right|^{2}-\frac{2 \alpha[(n-2)+n(n-1) t]}{n(n-1)} \int_{M} R u^{2 \alpha} \\
& -\alpha \sqrt{\frac{2(n-2)}{n-1}} \int_{M}\left|W+\frac{\sqrt{2}}{\sqrt{n}(n-2)} \operatorname{Ric} \otimes g\right| u^{2 \alpha} .
\end{aligned}$$
Therefore, by virtue of (1.3), we have for $2-\frac{1}{\alpha}>0$
$$\begin{aligned}
0 \geq & {\left[\left(2-\frac{1}{\alpha}\right) \frac{n-2}{4(n-1)} Y_{M}([g])\right.} \\
& \left.-\alpha \sqrt{\frac{2(n-2)}{n-1}}\left(\int_{M}\left|W+\frac{\sqrt{2}}{\sqrt{n}(n-2)} \operatorname{Ric} \otimes g\right|^{\frac{n}{2}}\right)^{\frac{2}{n}}\right] \\
& \times\left(\int_{M} u^{\frac{2 n \alpha}{n-2}}\right)^{\frac{n-2}{n}}-\left[\frac{2 \alpha[(n-2)+n(n-1) t]}{n(n-1)}\right. \\
& \left.+\left(2-\frac{1}{\alpha}\right) \frac{n-2}{4(n-1)}\right] \int_{M} R u^{2 \alpha},
\end{aligned}$$
where we have used the Hölder inequality
$$\begin{aligned}
\int_{M} \mid W & \left.+\frac{\sqrt{2}}{\sqrt{n}(n-2)} \operatorname{Ric} \otimes g \right\rvert\, u^{2 \alpha} \\
& \leq\left(\int_{M}\left|W+\frac{\sqrt{2}}{\sqrt{n}(n-2)} \operatorname{Ric} \otimes g\right|^{\frac{n}{2}}\right)^{\frac{2}{n}}\left(\int_{M} u^{\frac{2 n \alpha}{n-2}}\right)^{\frac{n-2}{n}}
\end{aligned}$$
So the proof of Proposition 3.1 is completed. \(\square\)

Now, we are in a position to prove Theorem 1.6.
For $n=4$, using (2.6), we obtain that the scalar curvature $R$ is harmonic and hence $R$ is constant. Therefore, (3.15) becomes
$$\begin{aligned}
0 \geq & {\left[\frac{1}{6}\left(2-\frac{1}{\alpha}\right) Y_{M}([g])-\frac{2 \alpha}{\sqrt{3}}\left(\int_{M}\left|W+\frac{1}{2 \sqrt{2}} \mathrm{Ric}^{\circ} \otimes g\right|^{2}\right)^{\frac{1}{2}}\right] } \\
& \times\left(\int_{M}\left|\stackrel{\circ}{R}_{i j}\right|^{4 \alpha}\right)^{\frac{1}{2}}-\left[\frac{\alpha(1+6 t)}{3}+\frac{1}{6}\left(2-\frac{1}{\alpha}\right)\right] \int_{M} R\left|\stackrel{\circ}{\mathrm{R}}_{i j}\right|^{2 \alpha} .
\end{aligned}$$
Since $t$ satisfies (1.12), we may take
$$\alpha=\frac{1-\sqrt{1+2(1+6 t)}}{-2(1+6 t)}$$
such that $2-\frac{1}{\alpha}>0$. In this case, we have
$$\frac{\alpha(1+6 t)}{3}+\frac{1}{6}\left(2-\frac{1}{\alpha}\right)=0 .$$
Hence (3.21) becomes
$$\begin{aligned}
0 \geq & {\left[\frac{1}{6}\left(2-\frac{1}{\alpha}\right) Y_{M}([g])-\frac{2 \alpha}{\sqrt{3}}\left(\int_{M}\left|W+\frac{1}{2 \sqrt{2}} \operatorname{Ric} \otimes g\right|^{2}\right)^{\frac{1}{2}}\right] } \\
& \times\left(\int_{M}\left|\stackrel{\circ}{R}_{i j}\right|^{4 \alpha}\right)^{\frac{1}{2}} .
\end{aligned}$$
Therefore, under the assumption (1.13), we obtain that $M^{4}$ is Einstein. Moreover, in this case, (1.13) becomes
$$\left(\int_{M}|W|^{2}\right)^{\frac{1}{2}}<-\frac{1+6 t}{2 \sqrt{3}} Y_{M}([g]) .$$
We can check that
$$-\frac{1+6 t}{2 \sqrt{3}}<\frac{1}{\sqrt{6}},$$
which, combined with Lemma 2.4, shows that $M^{4}$ is of constant positive sectional curvature, completing the proof of Theorem 1.6.

\section*{4. Proof of Corollaries 1.5 and 1.7}

In this last section, we provide the detail in proving Corollaries 1.5 and 1.7. For this, the following lemma by Catino (Lemma 4.1, [5]) is needed:
Lemma 4.1. Let $\left(M^{4}, g\right)$ be a closed manifold. Then
$$Y_{M}^{2}([g]) \geq \int_{M}\left(R^{2}-12\left|\stackrel{\circ}{R}_{i j}\right|^{2}\right),$$
and the inequality is strict unless $\left(M^{4}, g\right)$ is conformally Einstein.
When $n=4$, the pinching condition (1.9) can be written as
$$\int_{M}\left(|W|^{2}+\left|\stackrel{\circ}{R}_{i j}\right|^{2}\right)<\frac{1}{48} Y_{M}^{2}([g]) .$$
It holds by (4.1) that
$$\begin{aligned}
& \int_{M}\left(|W|^{2}+\left|\stackrel{\circ}{R}_{i j}\right|^{2}\right)-\frac{1}{48} Y_{M}^{2}([g]) \\
< & \int_{M}\left(|W|^{2}+\frac{5}{4}\left|\stackrel{\circ}{R}_{i j}\right|^{2}-\frac{1}{48} R^{2}\right),
\end{aligned}$$
from which Corollary 1.5 follows immediately.
On the other hand, (1.13) can be written as
$$\int_{M}\left(|W|^{2}+\left|\stackrel{\circ}{R}_{i j}\right|^{2}\right)<\frac{(1+6 t)^{2}}{12} Y_{M}^{2}([g])$$
which, combined with (4.1), gives
$$\begin{aligned}
& \int_{M}\left(|W|^{2}+\left|\stackrel{\circ}{R}_{i j}\right|^{2}\right)-\frac{(1+6 t)^{2}}{12} Y_{M}^{2}([g]) \\
< & \int_{M}\left(|W|^{2}+\left[1+(1+6 t)^{2}\right]\left|\stackrel{\circ}{R}_{i j}\right|^{2}-\frac{(1+6 t)^{2}}{12} R^{2}\right),
\end{aligned}$$
completing the proof of Corollary 1.7.

\section*{References}
\begin{itemize}
\item[] [1] M. Anderson, Extrema of curvature functionals on the space of metrics on 3-manifolds, Calc. Var. Partial Differential Equations, 5 (1997), 199-269.
\item[] [2] A. Besse, Einstein Manifolds, Springer-Verlag, Berlin, 2008.
\item[] [3] G. Catino, Critical metrics of the $L^{2}$-norm of the scalar curvature, Proc. Amer. Math. Soc. 142 (2014), 3981-3986.
\item[] [4] G. Catino, Some rigidity results on critical metrics for quadratic functionals, Calc. Var. Partial Differential Equations, 54 (2015), 2921-2937.
\item[] [5] G. Catino, Integral pinched shrinking Ricci solitons, Adv. Math. 303 (2016), 279-294.
\item[] [6] H. Fu, L. Xiao, Einstein manifolds with finite $L^{p}$-norm of the Weyl curvature, Differential Geom. Appl. 53 (2017), 293-305.
\item[] [7] H. Fu, L. Xiao, Rigidity theorem for integral pinched shrinking Ricci solitons, Monatsh. Math. 183 (2017), 487-494.
\item[] [8] H. Fu, J. Peng, Rigidity theorems for compact Bach-flat manifolds with positive constant scalar curvature, arXiv:1707.07236, to appear in Hokkaido Math. J.
\end{itemize}
\begin{itemize}
\item[] [9] M. Gursky, J. Viaclovsky, A new variational characterization of three-dimensional space forms, Invent. Math. 145 (2001), 251-278.
\item[] [10] M. Gursky, J. Viaclovsky, Rigidity and stability of Einstein metrics for quadratic curvature functionals, J. Reine Angew. Math. 700 (2015), 37-91.
\item[] [11] Z. Hu, H. Li, A new variational characterization of $n$-dimensional space forms, Trans. Amer. Math. Soc. 356 (2004), 3005-3023.
\item[] [12] G. Huang, B. Ma, Riemannian manifolds with harmonic curvature, Colloq. Math. 145 (2016), 251-257.
\item[] [13] G. Huang, L. Chen, Some characterizations on critical metrics for quadratic curvature functions, Proc. Amer. Math. Soc. 146 (2018), 385-395.
\item[] [14] G. Huang, Rigidity of Riemannian manifolds with positive scalar curvature, arXiv:1707.00902.
\item[] [15] F. Lamontagne, Une remarque sur la norme $L^{2}$ du tenseur de courbure, C. R. Acad. Sci. Paris Sér. I Math. 319 (1994), 237-240.
\item[] [16] S. Tanno, Deformations of Riemannian metrics on 3-dimensional manifolds, Tôhoku Math. J. 27 (1975), 437-444.
\end{itemize}

College of Physics and Materials Science, Henan Normal University, Xinxiang 453007, People's Republic of China

Department of Mathematics, Henan Normal University, Xinxiang 453007, People's Republic of China
E-mail address: bqma@henannu.edu.cn
Department of Mathematics, Henan Normal University, Xinxiang 453007, People's Republic of China
E-mail address: hgy@henannu.edu.cn
E-mail address: xxl@henannu.edu.cn
E-mail address: yuchern@126.com