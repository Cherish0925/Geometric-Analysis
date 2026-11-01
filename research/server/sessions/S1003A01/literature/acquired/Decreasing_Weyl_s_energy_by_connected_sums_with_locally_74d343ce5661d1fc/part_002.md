---
retention_scope: session
part: 2
total_parts: 3
---

[Part 2/3 of: Decreasing Weyl's energy by connected sums with locally ...]

Let us turn our attention to (3.35). Since the gauge terms in (3.32) are given (around $-e_{4}$ ) by polynomials of order $\leq 1$, we see that the hessian of $\bar{A}$ is equal to that of $\bar{A}_{0}$. Look at (3.30), and, for $y \sim-e_{4}$, consider a single term of the series
$$V_{i j}(y):=-\frac{1}{3} W_{\mu i j \nu} \frac{\left(t^{n} s O(y)+e_{4}\right)^{\mu}\left(t^{n} s O(y)+e_{4}\right)^{\nu}}{\left|t^{n} s O(y)+e_{4}\right|^{4}},$$
where we dropped the subscript $a$ for convenience. We have
$$\begin{aligned}
\partial_{k l}^{2} V_{i j}(y)= & -\frac{1}{3} t^{2 n} s^{2} W_{\mu i j \nu}\left[\frac{O_{k}^{\mu} O_{l}^{\nu}+O_{l}^{\mu} O_{k}^{\nu}}{\left|t^{n} s O(y)+e_{4}\right|^{4}}-4\left(t^{n} s y_{l}+O_{l}^{4}\right) \frac{O_{k}^{\mu}\left(t^{n} s O_{\beta}^{\nu} y^{\beta}+\delta_{4}^{\nu}\right)+\left(t^{n} s O_{\alpha}^{\mu} y^{\alpha}+\delta_{4}^{\mu}\right) O_{k}^{\nu}}{\left|t^{n} s O(y)+e_{4}\right|^{6}}\right. \\
-4 \delta_{k l} & \frac{\left(t^{n} s O_{\alpha}^{\mu} y^{\alpha}+\delta_{4}^{\mu}\right)\left(t^{n} s O_{\beta}^{\nu} y^{\beta}+\delta_{4}^{\nu}\right)}{\left|t^{n} s O(y)+e_{4}\right|^{6}}-4\left(t^{n} s y_{k}+O_{k}^{4}\right) \frac{O_{l}^{\mu}\left(t^{n} s O_{\beta}^{\nu} y^{\beta}+\delta_{4}^{\nu}\right)+\left(t^{n} s O_{\alpha}^{\mu} y^{\alpha}+\delta_{4}^{\mu}\right) O_{l}^{\nu}}{\left|t^{n} s O(y)+e_{4}\right|^{6}} \\
& \left.+24\left(t^{n} s y_{k}+O_{k}^{4}\right)\left(t^{n} s y_{l}+O_{l}^{4}\right) \frac{\left(t^{n} s O_{\alpha}^{\mu} y^{\alpha}+\delta_{4}^{\mu}\right)\left(t^{n} s O_{\beta}^{\nu} y^{\beta}+\delta_{4}^{\nu}\right)}{\left|t^{n} s O(y)+e_{4}\right|^{8}}\right] .
\end{aligned}$$
Let us now look at $\partial_{k l}^{2} V_{i j}\left(-e_{4}\right)$.
- Assume $O=\mathrm{Id}$ and $s=1$. Then
$$\begin{aligned}
\partial_{k l}^{2} V_{i j}\left(-e_{4}\right)=-\frac{1}{3} \frac{t^{2 n}}{\left(1-t^{n}\right)^{4}} & {\left[\left(W_{k i j l}+W_{l i j k}\right)-4 \delta_{4 k}\left(W_{l i j 4}+W_{4 i j l}\right)-4 \delta_{4 l}\left(W_{k i j 4}+W_{4 i j k}\right)\right.} \\
& \left.-4 \delta_{k l} W_{4 i j 4}+24 \delta_{4 k} \delta_{4 l} W_{4 i j 4}\right],
\end{aligned}$$
so, when summing over $n \in \mathbb{Z}, n \neq 0$, we obtain exactly the first term of (3.35), cf. (3.19).
- Assume $O \neq \mathrm{Id}$ and $t^{-1 / 2} \leq s \leq t^{1 / 2}$. Notice that, by virtue of Remark 3.7, we cannot have $s \neq 1$ and $O=\mathrm{Id}$, so all the remaining cases are included in this second one. Being $O \in \mathrm{SO}(4)$, looking at (3.37) we deduce
$$\left|\partial_{k l}^{2} V_{i j}\left(-e_{4}\right)\right| \leq C \frac{t^{2 n} s^{2}}{\left|-t^{n} s O_{4}^{\beta} e_{\beta}+e_{4}\right|^{4}}=C \frac{t^{2 n} s^{2}}{\left(t^{2 n} s^{2}-2 t^{n} s O_{4}^{4}+1\right)^{2}},$$
where $C>0$ does not depend on $n \in \mathbb{Z}$, neither on $O \in \operatorname{SO}(4)$ or $s \in\left[t^{-1 / 2}, t^{1 / 2}\right]$. Being $\operatorname{Id} \neq O \in \operatorname{SO}(4)$ with free action, then $\tau:=O_{4}^{4} \in[-1,1)$ necessarily. Consider the series over $n \in \mathbb{Z}$ of the above coefficients. Setting $\varepsilon=\log t$ we have
$$\begin{aligned}
\sum_{n \in \mathbb{Z}} \frac{t^{2 n} s^{2}}{\left(t^{2 n} s^{2}-2 t^{n} s O_{4}^{4}+1\right)^{2}} & =\frac{1}{s^{2}} \sum_{n \in \mathbb{Z}} \frac{e^{2 n \varepsilon}}{\left(e^{2 n \varepsilon}-2 \tau s^{-1} e^{n \varepsilon}+s^{-2}\right)^{2}} \\
& =\frac{1}{\varepsilon s^{2}}\left(\sum_{n \in \mathbb{Z}} \varepsilon \frac{e^{2 n \varepsilon}}{\left(e^{2 n \varepsilon}-2 \tau s^{-1} e^{n \varepsilon}+s^{-2}\right)^{2}}\right)=: \frac{1}{\varepsilon s^{2}} S(\varepsilon)
\end{aligned}$$

If $t \rightarrow 1^{+}$, then $\varepsilon \rightarrow 0^{+}$and the Riemann sum converges to
$$S(\varepsilon) \xrightarrow{\varepsilon \rightarrow 0^{+}} \int_{-\infty}^{-\infty} \frac{e^{2 x}}{\left(e^{2 x}-2 \tau s^{-1} e^{x}+s^{-2}\right)^{2}} d x=\int_{0}^{+\infty} \frac{r}{\left(r^{2}-2 \tau s^{-1} r+s^{-2}\right)^{2}} d r=: I(\tau, s),$$
where $I(\tau, s)$ is finite for any $\tau \in[-1,1)$ and $s \in[1 / 2,2]$, with $I(\tau, s) \rightarrow+\infty$ as $\tau \rightarrow 1^{-}$. Hence (recall that $\tau=O_{4}^{4}$ )
$$\sum_{n \in \mathbb{Z}}\left|\partial_{k l}^{2} V_{i j}\left(-e_{4}\right)\right| \leq \frac{C\left(O_{4}^{4}\right)}{(t-1)}, \quad \text { as } t \rightarrow 1^{+} .$$

The above considerations prove (3.35).
Finally, we prove (3.36). Letting again $\varepsilon:=\log t$, we rewrite
$$C_{2}(t)=2 \sum_{n>0} \frac{t^{2 n}}{\left(t^{n}-1\right)^{4}}=2 \sum_{n>0} \frac{e^{2 n \varepsilon}}{\left(e^{n \varepsilon}-1\right)^{4}}=: 2 \sum_{n>0}\left[\frac{1}{n^{4} \varepsilon^{4}}+f(n \varepsilon)\right],$$
where
$$f(x):=\frac{e^{2 x}}{\left(e^{x}-1\right)^{4}}-\frac{1}{x^{4}} .$$
One has
$$\sum_{n=1}^{+\infty} \frac{1}{n^{4} \varepsilon^{4}}=\frac{\pi^{4}}{90(t-1)^{4}}+O\left((t-1)^{-3}\right), \quad \text { as } t \rightarrow 1^{+} .$$
As for the other term, we notice that $f$ is continuous in $(0,+\infty), f(x)=O\left(x^{-3}\right)$ as $x \rightarrow 0^{+}$and $f(x)=O\left(x^{-4}\right)$ as $x \rightarrow+\infty$. Therefore there exists a constant $C>0$ such that $|f(x)| \leq C x^{-3} \forall x>0$, which implies
$$\sum_{n=1}^{+\infty} f(n \varepsilon) \leq \frac{C}{\varepsilon^{3}} \sum_{n=1}^{+\infty} \frac{1}{n^{3}} \leq \frac{C^{\prime}}{(t-1)^{3}}, \quad \text { as } t \rightarrow 1^{+}$$
so that (3.36) holds. \(\square\)

Finally, we have the extension of Proposition 3.4 to this setting:
Proposition 3.10. Let $(Z, g)$ and $q \in Z$ be given as in Section 3.2.1. There exists a symmetric tensor $F$, which is smooth in $Z \backslash\{q\}$, such that $\dot{B}_{g}(F)=0$ in $Z \backslash\{q\}$ and, in suitable Euclidean coordinates centered at $q$, (3.20) holds, where $A$ is smooth up to zero and satisfies
$$A(0)=0, \quad \nabla A(0)=0,$$
$$\begin{aligned}
W^{k i j l} \partial_{k l}^{2} A_{i j}(0)=- & \frac{1}{3} C_{2}(t)\left[W^{k i j l}\left(W_{k i j l}+W_{l i j k}\right)-4 W^{4 i j l}\left(W_{4 i j l}+W_{l i j 4}\right)\right. \\
& \left.-4 W^{k i j 4}\left(W_{k i j 4}+W_{4 i j k}\right)+24 W^{4 i j 4} W_{4 i j 4}\right]+O\left((t-1)^{-1}\right), \quad \text { as } t \rightarrow 1^{+},
\end{aligned}$$
where $C_{2}(t)$ is given by (3.19) and satisfies (3.36). Moreover, if we let
$$T_{k i j l}:=\frac{1}{2} \partial_{k l}^{2} A_{i j}(0),$$
then $T$ can be written as in (2.5).
The proof is identical to that of Proposition 3.4. As in Remark 3.6, we notice that $A$ will not be TT in general around 0.

\section*{4 Weyl energy of the modified metric on $Z=\left(\mathbb{R} \times \mathbb{S}^{3}\right) / G$}

We know that any locally conformally flat manifold $\left(Z, g_{Z}\right)$ is diffeomorphic to one of the models described in Theorem 3.1. Since we are only interested in the diffeomorphism class of the connected sum $Z \# M$, we might assume without loss of generality that ( $Z, g_{Z}$ ) is indeed one of the model manifolds described in Section 3. Then, by Propositions 3.4, 3.10, we know that, in the particular case in which $Z=\left(\mathbb{R} \times \mathbb{S}^{3}\right) / G$, there exists a point $q \in Z$ with $g_{Z}$ Euclidean around $q$, and there exists a tensor $F$, singular at $q$, which satisfies the properties described in the aforementioned propositions.

Let us consider the modified metric $g_{b}:=g_{Z}+b^{2} F$, where $b \ll 1$ is a small parameter. By virtue of (3.20), we have the following expansion of $g_{b}$ in Euclidean coordinates at $q$ :
$$\left(g_{b}\right)_{i j}(x)=\delta_{i j}+b^{2}\left(-\frac{1}{3} W_{k i j l}^{M} \frac{x^{k} x^{l}}{|x|^{4}}+A_{i j}(x)\right) \quad \text { in } B_{\delta}(0),$$
for $\delta>0$ small enough. Consider a small parameter $\gamma$ such that $0<a, b \ll \gamma \ll \delta / 2$; we now want to estimate
$$\mathcal{W}_{\gamma}^{Z}\left(g_{b}\right):=\int_{Z \backslash B_{\gamma}^{g}(q)}\left|W^{g_{b}}\right|^{2} d V_{g_{b}}$$
To begin, Taylor-expanding $g_{b}$ with respect to $t:=b^{2}$, we get
$$\mathcal{W}_{\gamma}^{Z}\left(g_{b}\right)=\mathcal{W}_{\gamma}^{Z}\left(g_{Z}\right)+\left.b^{2} \frac{d}{d t}\right|_{t=0} \mathcal{W}_{\gamma}^{Z}\left(g_{b}\right)+\left.\frac{b^{4}}{2} \frac{d^{2}}{d t^{2}}\right|_{t=0} \mathcal{W}_{\gamma}^{Z}\left(g_{b}\right)+O\left(b^{6}\right) .$$
Notice that the error term $O\left(b^{6}\right)$ also depends upon $\gamma$; however, since $b \ll \gamma$, the error term remains uniformly controlled by, e.g., $b^{5}$, and hence still of higher order. Being $g_{Z}$ locally conformally flat, we have $\mathcal{W}_{\gamma}^{Z}\left(g_{Z}\right)=0$ and
$$\left.\frac{d}{d t}\right|_{t=0} \mathcal{W}_{\gamma}^{Z}\left(g_{b}\right)=-4 \int_{Z \backslash B_{\gamma}^{g_{Z}}(q)}\left(W_{\alpha i j \beta}^{g_{Z}} \nabla^{\alpha} \nabla^{\beta} F^{i j}+\frac{1}{2} W_{\alpha i j \beta}^{g_{Z}} R^{\alpha \beta} F^{i j}\right) d V_{g_{Z}}=0,$$
so we are left with
$$\mathcal{W}_{\gamma}^{Z}\left(g_{b}\right)=\left.\frac{b^{4}}{2} \frac{d^{2}}{d t^{2}}\right|_{t=0} \mathcal{W}_{\gamma}^{Z}\left(g_{b}\right)+O\left(b^{6}\right) .$$
Using again the fact that $g_{Z}$ is locally conformally flat, we see from (4.2) that
$$\left.\frac{d^{2}}{d t^{2}}\right|_{t=0} \mathcal{W}_{\gamma}^{Z}\left(g_{b}\right)=-4 \int_{Z \backslash B_{\gamma}^{g}(q)}\left(\dot{W}_{\alpha i j \beta} \nabla^{\alpha} \nabla^{\beta} F^{i j}+\frac{1}{2} \dot{W}_{\alpha i j \beta} R^{\alpha \beta} F^{i j}\right) d V_{g_{Z}}$$
Integrating by parts twice, one has
$$\begin{aligned}
\int_{Z \backslash B_{\gamma}}\left(\dot{W}_{\alpha i j \beta}\right. & \left.\nabla^{\alpha} \nabla^{\beta} F^{i j}+\frac{1}{2} \dot{W}_{\alpha i j \beta} R^{\alpha \beta} F^{i j}\right) d V_{g_{Z}} \\
& =-\int_{Z \backslash B_{\gamma}}\left(\nabla^{\alpha} \dot{W}_{\alpha i j \beta} \nabla^{\beta} F^{i j}+\frac{1}{2} \dot{W}_{\alpha i j \beta} R^{\alpha \beta} F^{i j}\right) d V_{g_{Z}}-\int_{\partial B_{\gamma}} \dot{W}_{n i j \beta} \nabla^{\beta} F^{i j} d \sigma_{g_{Z}} \\
& =\int_{Z \backslash B_{\gamma}}\left(\nabla^{\beta} \nabla^{\alpha} \dot{W}_{\alpha i j \beta} F^{i j}+\frac{1}{2} \dot{W}_{\alpha i j \beta} R^{\alpha \beta} F^{i j}\right) d V_{g_{Z}}-\int_{\partial B_{\gamma}} \dot{W}_{n i j \beta} \nabla^{\beta} F^{i j} d \sigma_{g_{Z}} \\
& \quad+\int_{\partial B_{\gamma}} \nabla^{\alpha} \dot{W}_{\alpha i j n} F^{i j} d \sigma_{g_{Z}}
\end{aligned}$$
where the $n$ subscript denotes the tensor component with respect to the inward pointing unit normal (so it points towards the exterior of $B_{\gamma}$ ).

We now observe the following:

Claim. Let $\left(g_{t}\right)_{t}$ be a smooth family of metrics. If $g=g_{0}$ is locally conformally flat, then
$$\left.\frac{d}{d t}\right|_{t=0}\left(\nabla^{\alpha} \nabla^{\beta} W_{\alpha i j \beta}^{g_{t}}\right)=\nabla^{\alpha} \nabla^{\beta} \dot{W}_{\alpha i j \beta}^{g} .$$
Proof. Let $h=\left.\frac{d}{d t}\right|_{t=0} g_{t}$. Being the metric tensor and its inverse parallel at each time and using the fact that $W^{g} \equiv 0$, we have
$$\begin{aligned}
\left.\frac{d}{d t}\right|_{t=0}\left(\nabla^{\alpha} \nabla^{\beta} W_{\alpha i j \beta}\right) & =\left.\frac{d}{d t}\right|_{t=0}\left(g^{\alpha \mu} g^{\beta \nu} \nabla_{\mu} \nabla_{\nu} W_{\alpha i j \beta}\right) \\
= & \left.g^{\alpha \mu} g^{\beta \nu} \frac{d}{d t}\right|_{t=0}\left(\nabla_{\mu} \nabla_{\nu} W_{\alpha i j \beta}\right)-\left(h^{\alpha \mu} g^{\beta \nu}+g^{\alpha \mu} h^{\beta \nu}\right) \nabla_{\mu} \nabla_{\nu} W_{\alpha i j \beta} \\
= & \left.g^{\alpha \mu} g^{\beta \nu} \frac{d}{d t}\right|_{t=0}\left[\partial_{\mu}\left(\nabla_{\nu} W_{\alpha i j \beta}\right)-\Gamma_{\mu \nu}^{s} \nabla_{s} W_{\alpha i j \beta}-\Gamma_{\mu \alpha}^{s} \nabla_{\nu} W_{s i j \beta}\right. \\
& \left.\quad-\Gamma_{\mu i}^{s} \nabla_{\nu} W_{\alpha s j \beta}-\Gamma_{\mu j}^{s} \nabla_{\nu} W_{\alpha i s \beta}-\Gamma_{\mu \beta}^{s} \nabla_{\nu} W_{\alpha i j s}\right] \\
= & g^{\alpha \mu} g^{\beta \nu}\left[\nabla_{\mu}\left(\left.\frac{d}{d t}\right|_{t=0}\left(\nabla_{\nu} W_{\alpha i j \beta}\right)\right)-\dot{\Gamma}_{\mu \nu}^{s} \nabla_{s} W_{\alpha i j \beta}-\dot{\Gamma}_{\mu \alpha}^{s} \nabla_{\nu} W_{s i j \beta}\right. \\
& \left.\quad-\dot{\Gamma}_{\mu i}^{s} \nabla_{\nu} W_{\alpha s j \beta}-\dot{\Gamma}_{\mu j}^{s} \nabla_{\nu} W_{\alpha i s \beta}-\dot{\Gamma}_{\mu \beta}^{s} \nabla_{\nu} W_{\alpha i j s}\right] \\
= & g^{\alpha \mu} g^{\beta \nu} \nabla_{\mu}\left[\left.\frac{d}{d t}\right|_{t=0}\left(\partial_{\nu} W_{\alpha i j \beta}-\Gamma_{\nu \alpha}^{s} W_{s i j \beta}-\Gamma_{\nu i}^{s} W_{\alpha s j \beta}-\Gamma_{\nu j}^{s} W_{\alpha i s \beta}-\Gamma_{\nu \beta}^{s} W_{\alpha i j s}\right)\right] \\
= & g^{\alpha \mu} g^{\beta \nu} \nabla_{\mu}\left[\nabla_{\nu} \dot{W}_{\alpha i j \beta}-\dot{\Gamma}_{\nu \alpha}^{s} W_{s i j \beta}-\dot{\Gamma}_{\nu i}^{s} W_{\alpha s j \beta}-\dot{\Gamma}_{\nu j}^{s} W_{\alpha i s \beta}-\dot{\Gamma}_{\nu \beta}^{s} W_{\alpha i j s}\right] \\
= & g^{\alpha \mu} g^{\beta \nu} \nabla_{\mu} \nabla_{\nu} \dot{W}_{\alpha i j \beta}=\nabla^{\alpha} \nabla^{\beta} \dot{W}_{\alpha i j \beta},
\end{aligned}$$
thus the claim holds. \(\square\)

As a consequence of the previous claim, we see that, at our locally conformally flat metric $g_{Z}$, one has
$$\dot{B}_{i j}(F)=-4\left(\nabla^{\alpha} \nabla^{\beta} \dot{W}_{\alpha i j \beta}+\frac{1}{2} R^{\alpha \beta} \dot{W}_{\alpha i j \beta}\right) .$$
Using this identity together with (4.3), (4.4), (4.5) and the fact that $\dot{B}_{g_{Z}}(F)(p)=0$ for $p \neq q$ (see e.g. Proposition 3.4), we deduce that
$$\mathcal{W}_{\gamma}^{Z}\left(g_{b}\right)=2 b^{4}\left(\int_{\partial B_{\gamma}} \dot{W}_{n i j \beta} \nabla^{\beta} F^{i j} d \sigma_{g_{Z}}-\int_{\partial B_{\gamma}} \nabla^{\alpha} \dot{W}_{\alpha i j n} F^{i j} d \sigma_{g_{Z}}\right)+O\left(b^{6}\right) .$$
In particular, since we are assuming $g_{Z}$ to be Euclidean inside $B_{\delta}(q)$ and since $\gamma<\delta / 2$, we finally get
$$\mathcal{W}_{\gamma}^{Z}\left(g_{b}\right)=2 b^{4}\left(\int_{\partial B_{\gamma}} \dot{W}_{\eta i j \beta} \partial^{\beta} F^{i j} \nu^{\eta} d \sigma-\int_{\partial B_{\gamma}} \partial^{\alpha} \dot{W}_{\alpha i j \eta} F^{i j} \nu^{\eta} d \sigma\right)+O\left(b^{6}\right)$$
where $\nu=\left(\nu^{1}, \ldots, \nu^{4}\right)=x /|x|$ is the unit normal and $d \sigma$ is the Euclidean surface element.
We now want to expand both integrals in (4.6), starting from the second one. To begin, recall the formula for the linearized Weyl tensor at the Euclidean metric (see [MM25], equation (2.8) for the linearized of Weyl tensor in the same notation employed here; in alternative, see e.g. [CM20], which employs a different convention):
$$\begin{aligned}
\dot{W}_{\alpha i j \beta}= & \frac{1}{2}\left[\partial_{\alpha j}^{2} F_{i \beta}+\partial_{i \beta}^{2} F_{\alpha j}-\partial_{\alpha \beta}^{2} F_{i j}-\partial_{i j}^{2} F_{\alpha \beta}\right]+\frac{1}{4}\left[\delta_{\alpha \beta} \Delta F_{i j}+\delta_{i j} \Delta F_{\alpha \beta}-\delta_{i \beta} \Delta F_{\alpha j}-\delta_{\alpha j} \Delta F_{i \beta}\right] \\
& +\frac{1}{4}\left[\left(\partial_{\alpha}(\delta F)_{j}+\partial_{j}(\delta F)_{\alpha}-\partial_{\alpha j}^{2}(\operatorname{tr} F)\right) \delta_{i \beta}+\left(\partial_{i}(\delta F)_{\beta}+\partial_{\beta}(\delta F)_{i}-\partial_{i \beta}^{2}(\operatorname{tr} F)\right) \delta_{\alpha j}\right. \\
& \left.-\left(\partial_{\alpha}(\delta F)_{\beta}+\partial_{\beta}(\delta F)_{\alpha}-\partial_{\alpha \beta}^{2}(\operatorname{tr} F)\right) \delta_{i j}-\left(\partial_{i}(\delta F)_{j}+\partial_{j}(\delta F)_{i}-\partial_{i j}^{2}(\operatorname{tr} F)\right) \delta_{\alpha \beta}\right] \\
& +\frac{1}{6}\left(-\Delta(\operatorname{tr} F)+\left(\delta^{2} F\right)\right)\left(\delta_{\alpha \beta} \delta_{i j}-\delta_{\alpha j} \delta_{\beta i}\right)
\end{aligned}$$
where $\delta F$ denotes the (Euclidean) divergence of $F$. We can also compute the Euclidean divergence of (4.7), obtaining
$$\begin{aligned}
\partial^{\alpha} \dot{W}_{\alpha i j \beta}= & \frac{1}{4}\left[\partial_{j} \Delta F_{i \beta}-\partial_{\beta} \Delta F_{i j}+\partial_{i \beta}^{2}(\delta F)_{j}-\partial_{i j}^{2}(\delta F)_{\beta}\right] \\
& +\frac{1}{12}\left[\left(\partial_{j}\left(\delta^{2} F\right)-\partial_{j} \Delta(\operatorname{tr} F)\right) \delta_{i \beta}-\left(\partial_{\beta}\left(\delta^{2} F\right)-\partial_{\beta} \Delta(\operatorname{tr} F)\right) \delta_{i j}\right] .
\end{aligned}$$

Let us write (cf. (3.20))
$$F_{i j}(x)=K_{i j}(x)+A_{i j}(x), \quad K_{i j}(x):=-\frac{1}{3} W_{\mu i j \nu} \frac{x^{\mu} x^{\nu}}{|x|^{4}} .$$
While it is immediate to check that $K(x)$ is a TT tensor with respect to the Euclidean metric for any $x \neq 0$, the tensor $A$ in general has nontrivial trace and divergence near the origin, see e.g. Remark 3.6. Moreover, from the definition of $K$ we easily compute
$$\partial_{\beta} \Delta K_{i j}=\partial_{\beta}\left(\frac{8}{3} W_{k i j l} \frac{x^{k} x^{l}}{|x|^{6}}\right)=\frac{8}{3} W_{k i j l}\left(\frac{\delta_{\beta}^{k} x^{l}+x^{k} \delta_{\beta}^{l}}{|x|^{6}}-6 \frac{x_{\beta} x^{k} x^{l}}{|x|^{8}}\right),$$
while, since the singular term of $F$ is TT, we further have
$$\partial_{i \beta}^{2}(\delta F)_{j}=\partial_{i \beta}^{2}(\delta A)_{j}, \quad \partial_{j}\left(\delta^{2} F\right)=\partial_{j}\left(\delta^{2} A\right), \quad \partial_{j} \Delta(\operatorname{tr} F)=\partial_{j} \Delta(\operatorname{tr} A) .$$

Lemma 4.1. In the above setting, it holds
$$\int_{\partial B_{\gamma}} \partial^{\alpha} \dot{W}_{\alpha i j \beta} F^{i j} \nu^{\beta} d \sigma=\mathcal{C}_{1} \gamma^{-4}+\frac{\pi^{2}}{6} \partial^{k l} A^{i j}(0) W_{k i j l}+O\left(\gamma^{2}\right), \quad \text { as } \gamma \rightarrow 0^{+}$$
for a real constant $\mathcal{C}_{1}=\mathcal{C}_{1}\left(W^{M}(p)\right)$.
Proof. From (4.8) one has
$$\begin{aligned}
\int_{\partial B_{\gamma}} \partial^{\alpha} \dot{W}_{\alpha i j \beta} & F^{i j} \nu^{\beta} d \sigma=\frac{1}{4} \int_{\partial B_{\gamma}}\left[\partial_{j} \Delta F_{i \beta}-\partial_{\beta} \Delta F_{i j}+\partial_{i \beta}^{2}(\delta F)_{j}-\partial_{i j}^{2}(\delta F)_{\beta}\right] F^{i j} \nu^{\beta} d \sigma \\
+ & \frac{1}{12} \int_{\partial B_{\gamma}}\left[\left(\partial_{j}\left(\delta^{2} F\right)-\partial_{j} \Delta(\operatorname{tr} F)\right) \delta_{i \beta} F^{i j} \nu^{\beta}-\left(\partial_{\beta}\left(\delta^{2} F\right)-\partial_{\beta} \Delta(\operatorname{tr} F)\right)(\operatorname{tr} F) \nu^{\beta}\right] d \sigma
\end{aligned}$$
Using now (4.9), (4.11), the above expression becomes
$$\begin{aligned}
\int_{\partial B_{\gamma}} \partial^{\alpha} \dot{W}_{\alpha i j \beta} F^{i j} & \nu^{\beta} d \sigma=\frac{1}{4} \int_{\partial B_{\gamma}}\left[\partial_{j} \Delta K_{i \beta}-\partial_{\beta} \Delta K_{i j}\right] K^{i j} \nu^{\beta} d \sigma \\
& +\frac{1}{4} \int_{\partial B_{\gamma}}\left[\partial_{j} \Delta K_{i \beta}-\partial_{\beta} \Delta K_{i j}\right] A^{i j} \nu^{\beta} d \sigma \\
& +\frac{1}{4} \int_{\partial B_{\gamma}}\left[\partial_{j} \Delta A_{i \beta}-\partial_{\beta} \Delta A_{i j}+\partial_{i \beta}^{2}(\delta A)_{j}-\partial_{i j}^{2}(\delta A)_{\beta}\right] K^{i j} \nu^{\beta} d \sigma \\
& +\frac{1}{4} \int_{\partial B_{\gamma}}\left[\partial_{j} \Delta A_{i \beta}-\partial_{\beta} \Delta A_{i j}+\partial_{i \beta}^{2}(\delta A)_{j}-\partial_{i j}^{2}(\delta A)_{\beta}\right] A^{i j} \nu^{\beta} d \sigma \\
& +\frac{1}{12} \int_{\partial B_{\gamma}}\left(\partial^{j}\left(\delta^{2} A\right)-\partial_{j} \Delta(\operatorname{tr} A)\right) \delta_{i \beta} K^{i j} \nu^{\beta} d \sigma \\
& +\frac{1}{12} \int_{\partial B_{\gamma}}\left[\left(\partial_{j}\left(\delta^{2} A\right)-\partial_{j} \Delta(\operatorname{tr} A)\right) \delta_{i \beta} A^{i j} \nu^{\beta}-\left(\partial_{\beta}\left(\delta^{2} A\right)-\partial_{\beta} \Delta(\operatorname{tr} A)\right)(\operatorname{tr} A) \nu^{\beta}\right]
\end{aligned}$$

We now consider separately at each of the above integrals.
- By looking at (4.9), (4.10), it is easy to see (after a change of variables) that the RHS of (4.13) is of order $\gamma^{-4}$. Since we are going to show below that all the other integrals provide higher order contributions, we conclude that
$$\frac{1}{4} \int_{\partial B_{\gamma}}\left[\partial_{j} \Delta K_{i \beta}-\partial_{\beta} \Delta K_{i j}\right] K^{i j} \nu^{\beta} d \sigma=: \mathcal{C}_{1} \gamma^{-4}$$
where $\mathcal{C}_{1}=\mathcal{C}_{1}\left(W^{M}(p)\right)$ is the constant appearing in (4.12).
- Let us consider (4.14). To begin, recalling (4.10) and using the symmetries of Weyl's tensor and Bianchi's identity we got
$$\begin{aligned}
& W_{k i \beta l}\left(\frac{\delta_{j}^{k} x^{l}+x^{k} \delta_{j}^{l}}{|x|^{6}}-6 \frac{x_{j} x^{k} x^{l}}{|x|^{8}}\right)-W_{k i j l}\left(\frac{\delta_{\beta}^{k} x^{l}+x^{k} \delta_{\beta}^{l}}{|x|^{6}}-6 \frac{x_{\beta} x^{k} x^{l}}{|x|^{8}}\right) \\
= & \left(W_{j i \beta l}+W_{l i \beta j}-W_{\beta i j l}-W_{l i j \beta}\right) \frac{x^{l}}{|x|^{6}}-6 W_{k i \beta l} \frac{x_{j} x^{k} x^{l}}{|x|^{8}}+6 W_{k i j l} \frac{x_{\beta} x^{k} x^{l}}{|x|^{8}} \\
= & -3 W_{l i j \beta} \frac{x^{l}}{|x|^{6}}-6 W_{k i \beta l} \frac{x_{j} x^{k} x^{l}}{|x|^{8}}+6 W_{k i j l} \frac{x_{\beta} x^{k} x^{l}}{|x|^{8}} .
\end{aligned}$$
Substituting this formula in (4.14) and Taylor-expanding $A_{i j}$, we get
$$\begin{aligned}
\frac{2}{3} \int_{\partial B_{\gamma}}\left[-3 W_{l i j \beta}\right. & \left.\frac{x^{l}}{|x|^{6}}-6 W_{k i \beta l} \frac{x_{j} x^{k} x^{l}}{|x|^{8}}+6 W_{k i j l} \frac{x_{\beta} x^{k} x^{l}}{|x|^{8}}\right] \times \\
& \times\left(A^{i j}(0)+\partial_{s} A^{i j}(0) x^{s}+\frac{1}{2} \partial_{s t}^{2} A^{i j}(0) x^{s} x^{t}+\frac{1}{6} \partial_{s t u}^{3} A^{i j}(0) x^{s} x^{t} x^{u}+O\left(|x|^{4}\right)\right) \frac{x^{\beta}}{|x|} d \sigma .
\end{aligned}$$
Next, we notice that $W_{k i \beta l} x^{k} x^{l} x^{\beta}=0$ by skew-symmetry and that all the terms involving an odd number of derivatives of $A^{i j}$ are zero because we got an integral over a sphere of an odd number of coordinate functions (which vanishes because odd in at least one direction). Moreover, we have $A(0)=0, \nabla A(0)=0$, see (3.21), (3.38). Hence we obtain
$$(4.14)=\frac{1}{3} \int_{\partial B_{\gamma}}\left[-3 W_{l i j \beta} \frac{x^{l}}{|x|^{6}}+6 W_{k i j l} \frac{x_{\beta} x^{k} x^{l}}{|x|^{8}}\right] \partial_{s t}^{2} A^{i j}(0) \frac{x^{s} x^{t} x^{\beta}}{|x|} d \sigma+O\left(\gamma^{2}\right),$$
which, after a change of variables, can be rewritten as
$$(4.14)=W_{k i j l} \partial_{s t}^{2} A^{i j}(0) \int_{\mathbb{S}^{3}} z^{k} z^{l} z^{s} z^{t} d \sigma+O\left(\gamma^{2}\right)$$
We can now employ the identity (cf. [Bre08], Corollary 29)
$$\int_{\mathbb{S}^{3}} x^{\mu} x^{\nu} x^{k} x^{l} d \sigma_{\mathbb{S}^{3}}=\frac{\pi^{2}}{12}\left(\delta^{\mu \nu} \delta^{k l}+\delta^{\mu k} \delta^{\nu l}+\delta^{\mu l} \delta^{\nu k}\right)$$
to finally obtain that
$$(4.14)=\frac{\pi^{2}}{6} W_{k i j l} \partial^{k l} A^{i j}(0)+O\left(\gamma^{2}\right) .$$
- Consider now (4.15). Taylor-expanding the terms involving derivatives of $A$ and performing a subsequent change of variables, one gets
$$(4.15)=O\left(\gamma^{2}\right) .$$

Notice that there are no terms of order $\gamma$ because the integrals involve an odd number of coordinate functions. The same argument also shows that
$$(4.17)=O\left(\gamma^{2}\right) .$$
\begin{itemize}
\item[-] Finally, a change of variables shows that $(4.16)+(4.18)=O\left(\gamma^{3}\right)$.
\end{itemize}

Combining the last two items and (4.19), (4.21), we finally obtain (4.12), concluding our proof. \(\square\)

We now focus on the first integral in (4.6); using (4.7), (4.9) and the fact that $K$ is TT, we compute
$$\begin{aligned}
& \dot{W}_{\eta i j \beta} \partial^{\beta} F^{i j} \nu^{\eta}=\frac{1}{2}\left[\partial_{\eta j}^{2} F_{i \beta}+\partial_{i \beta}^{2} F_{\eta j}-\partial_{\eta \beta}^{2} F_{i j}-\partial_{i j}^{2} F_{\eta \beta}\right] \partial^{\beta} F^{i j} \nu^{\eta}+\frac{1}{4}\left[\Delta F_{i j} \partial^{\beta} F^{i j} \nu_{\beta}-\Delta F_{i \beta} \partial^{\beta} F^{i j} \nu_{j}\right] \\
& \quad+\frac{1}{4}\left[\Delta F_{\eta \beta} \partial^{\beta}(\operatorname{tr} A) \nu^{\eta}-\Delta F_{\eta j}(\delta A)^{j} \nu^{\eta}\right] \\
& \quad+\frac{1}{4}\left[\partial_{i}(\delta A)_{\beta}+\partial_{\beta}(\delta A)_{i}-\partial_{i \beta}^{2}(\operatorname{tr} A)\right] \partial^{\beta} F^{i j} \nu_{j}-\frac{1}{4}\left[\partial_{i}(\delta A)_{j}+\partial_{j}(\delta A)_{i}-\partial_{i j}^{2}(\operatorname{tr} A)\right] \partial^{\beta} F^{i j} \nu_{\beta} \\
& \quad+\frac{1}{4}\left[\partial_{\eta}(\Delta A)_{j}+\partial_{j}(\delta A)_{\eta}-\partial_{\eta j}^{2}(\operatorname{tr} A)\right](\delta A)^{j} \nu^{\eta}-\frac{1}{4}\left[\partial_{\eta}(\Delta A)_{\beta}+\partial_{\beta}(\delta A)_{\eta}-\partial_{\eta \beta}^{2}(\operatorname{tr} A)\right] \partial^{\beta}(\operatorname{tr} A) \nu^{\eta} \\
& \quad+\frac{1}{6}\left[-\Delta(\operatorname{tr} A)+\left(\delta^{2} A\right)\right]\left(\partial^{\beta}(\operatorname{tr} A) \nu_{\beta}-(\delta A)^{j} \nu_{j}\right)
\end{aligned}$$

To begin, we show that the integrals of all trace and divergence terms of (4.22) generate higher-order contributions.

Lemma 4.2. There holds
$$\begin{aligned}
\int_{\partial B_{\gamma}} \dot{W}_{\eta i j \beta} \partial^{\beta} F^{i j} \nu^{\eta} d \sigma & =\frac{1}{2} \int_{\partial B_{\gamma}}\left[\partial_{\eta j}^{2} F_{i \beta}+\partial_{i \beta}^{2} F_{\eta j}-\partial_{\eta \beta}^{2} F_{i j}-\partial_{i j}^{2} F_{\eta \beta}\right] \partial^{\beta} F^{i j} \nu^{\eta} d \sigma \\
& +\frac{1}{4} \int_{\partial B_{\gamma}}\left[\Delta F_{i j} \partial^{\beta} F^{i j} \nu_{\beta}-\Delta F_{i \beta} \partial^{\beta} F^{i j} \nu_{j}\right] d \sigma+O\left(\gamma^{2}\right), \quad \text { as } \gamma \rightarrow 0^{+}
\end{aligned}$$
Proof. We consider each divergence or trace term of (4.22) separately.
\begin{itemize}
\item[-] Consider the term in the second line of (4.22). Integrating and recalling (4.9), one has
\end{itemize}
$$\begin{aligned}
& \frac{1}{4} \int_{\partial B_{\gamma}}\left[\Delta F_{\eta \beta} \partial^{\beta}(\operatorname{tr} A)-\Delta F_{\eta j}(\delta A)^{j}\right] \nu^{\eta} d \sigma \\
& \quad=\frac{1}{4} \int_{\partial B_{\gamma}}\left[\left(\frac{8}{3} W_{k \eta \beta l} \frac{x^{k} x^{l}}{|x|^{6}}+\Delta A_{\eta \beta}(x)\right) \partial^{\beta}(\operatorname{tr} A)-\left(\frac{8}{3} W_{k \eta j l} \frac{x^{k} x^{l}}{|x|^{6}}+\Delta A_{\eta j}(x)\right)(\delta A)^{j}\right] \frac{x^{\eta}}{|x|} d \sigma \\
& \quad=\frac{2}{3} \int_{\partial B_{\gamma}}\left[\left(W_{k \eta \beta l} \partial^{\beta}(\operatorname{tr} A)-W_{k \eta j l}(\delta A)^{j}\right) \frac{x^{k} x^{l} x^{\eta}}{|x|^{7}} d \sigma+O\left(\gamma^{3}\right)=O\left(\gamma^{3}\right),\right.
\end{aligned}$$
due to symmetry properties of Weyl's tensor.
\begin{itemize}
\item[-] Consider the first term in the third line of (4.22), namely $\frac{1}{4}\left[\partial_{i}(\delta A)_{\beta}+\partial_{\beta}(\delta A)_{i}-\partial_{i \beta}^{2}(\operatorname{tr} A)\right] \partial^{\beta} F^{i j} \nu_{j}$.
\end{itemize} One has
$$\begin{aligned}
& \frac{1}{4} \int_{\partial B_{\gamma}}\left[\partial_{i}(\delta A)_{\beta}(x)+\partial_{\beta}(\delta A)_{i}(x)-\partial_{i \beta}^{2}(\operatorname{tr} A)(x)\right] \partial^{\beta}\left(-\frac{1}{3} W_{k}{ }^{i j} \frac{x^{k} x^{l}}{|x|^{4}}+A^{i j}(x)\right) \frac{x_{j}}{|x|} d \sigma \\
& =-\frac{1}{12} \int_{\partial B_{\gamma}}\left[\partial_{i}(\delta A)_{\beta}(x)+\partial_{\beta}(\delta A)_{i}(x)-\partial_{i \beta}^{2}(\operatorname{tr} A)(x)\right] W_{k}{ }^{i j}{ }_{l}\left(\frac{\delta^{\beta k} x^{l}+x^{k} \delta^{\beta l}}{|x|^{4}}-4 \frac{x^{\beta} x^{k} x^{l}}{|x|^{6}}\right) \frac{x_{j}}{|x|} d \sigma+O\left(\gamma^{3}\right)
\end{aligned}$$

Taylor-expanding the $A$-terms we get
$$\begin{aligned}
-\frac{1}{12} \int_{\partial B_{\gamma}}\left[\partial_{i}(\delta A)_{\beta}(0)+\partial_{\beta}(\delta A)_{i}(0)\right. & \left.-\partial_{i \beta}^{2}(\operatorname{tr} A)(0)\right]\left(\frac{W^{\beta i j}{ }_{k} x^{k}+W_{k}{ }^{i j \beta} x^{k}}{|x|^{4}}-4 W_{k}{ }^{i j}{ }_{l} \frac{x^{\beta} x^{k} x^{l}}{|x|^{6}}\right) \frac{x_{j}}{|x|} d \sigma \\
- & \frac{1}{12} \int_{\partial B_{\gamma}}\left\{\left[\partial_{i s}^{2}(\delta A)_{\beta}(0)+\partial_{\beta s}^{2}(\delta A)_{i}(0)-\partial_{i \beta s}^{3}(\operatorname{tr} A)(0)\right] x^{s} \times\right. \\
& \left.\times\left(\frac{W^{\beta i j}{ }_{k} x^{k}+W_{k}{ }^{i j \beta} x^{k}}{|x|^{4}}-4 W_{k}{ }^{i j}{ }_{l} \frac{x^{\beta} x^{k} x^{l}}{|x|^{6}}\right) \frac{x_{j}}{|x|}\right\} d \sigma+O\left(\gamma^{2}\right)
\end{aligned}$$
However, the first integral above vanishes due to the skew-symmetry and trace-free property of Weyl's tensor, while the second integral vanishes because of the odd number of coordinate functions. Hence
$$\frac{1}{4} \int_{\partial B_{\gamma}}\left[\partial_{i}(\delta A)_{\beta}(x)+\partial_{\beta}(\delta A)_{i}(x)-\partial_{i \beta}^{2}(\operatorname{tr} A)(x)\right] \partial^{\beta} F^{i j} \nu_{j} d \sigma=O\left(\gamma^{2}\right)$$
- A computation similar to the previous one also shows that the second term in the third line of (4.22) satifies
$$-\frac{1}{4} \int_{\partial B_{\gamma}}\left[\left(\partial_{i}(\delta A)_{j}+\partial_{j}(\delta A)_{i}-\partial_{i j}^{2}(\operatorname{tr} A)\right] \partial^{\beta} F^{i j} \nu_{\beta} d \sigma=O\left(\gamma^{2}\right)\right.$$

Finally, it is immediate to see that the terms in the last two lines of (4.22) are of order $O\left(\gamma^{3}\right)$. This concludes the proof. \(\square\)

We now compute the integral over $\partial B_{\gamma}$ of a generic term in the first line of (4.22); recalling (4.9) one has
$$\begin{aligned}
& \int_{\partial B_{\gamma}} \partial_{\alpha \beta}^{2} F_{i j} \partial_{\tau} F_{s t} \nu_{\eta} d \sigma=\int_{\partial B_{\gamma}} \partial_{\alpha \beta}^{2} K_{i j} \partial_{\tau} K_{s t} \nu_{\eta} d \sigma \\
&-\frac{1}{3} \int_{\partial B_{\gamma}} \partial_{\alpha \beta}^{2} A_{i j}(x) W_{\mu s t \nu}\left(\frac{\delta_{\tau}^{\mu} x^{\nu}+x^{\mu} \delta_{\tau}^{\nu}}{|x|^{4}}-4 \frac{x_{\tau} x^{\mu} x^{\nu}}{|x|^{6}}\right) \frac{x^{\eta}}{|x|} d \sigma \\
&-\frac{1}{3} \int_{\partial B_{\gamma}} W_{k i j l}\left(\frac{\delta_{\alpha}^{k} \delta_{\beta}^{l}+\delta_{\beta}^{k} \delta_{\alpha}^{l}}{|x|^{4}}-4 \frac{x_{\beta}\left(\delta_{\alpha}^{k} x^{l}+x^{k} \delta_{\alpha}^{l}\right)}{|x|^{6}}-4 \frac{\delta_{\alpha \beta} x^{k} x^{l}+x_{\alpha}\left(\delta_{\beta}^{k} x^{l}+x^{k} \delta_{\beta}^{l}\right)}{|x|^{6}}\right. \\
&\left.\quad+24 \frac{x_{\alpha} x_{\beta} x^{k} x^{l}}{|x|^{8}}\right) \partial_{\tau} A_{s t}(x) \frac{x^{\eta}}{|x|} d \sigma+\int_{\partial B_{\gamma}} \partial_{\alpha \beta}^{2} A_{i j}(x) \partial_{\tau} A_{s t}(x) \frac{x^{\eta}}{|x|} d \sigma .
\end{aligned}$$
Taylor-expanding $\partial_{\tau} A_{s t}$ and $\partial_{\alpha \beta}^{2} A_{i j}$ at 0, using the symmetry of the integrals and a change of variables, one gets
$$\begin{aligned}
& \int_{\partial B_{\gamma}} \partial_{\alpha \beta}^{2} F_{i j} \partial_{\tau} F_{s t} \nu_{\eta} d \sigma=\int_{\partial B_{\gamma}} \partial_{\alpha \beta}^{2} K_{i j} \partial_{\tau} K_{s t} \nu_{\eta} d \sigma \\
&-\frac{1}{3} \int_{\mathbb{S}^{3}} \partial_{\alpha \beta}^{2} A_{i j}(0) W_{\mu s t \nu}\left(\delta_{\tau}^{\mu} x^{\nu}+x^{\mu} \delta_{\tau}^{\nu}-4 x_{\tau} x^{\mu} x^{\nu}\right) x^{\eta} d \sigma \\
&-\frac{1}{3} \int_{\mathbb{S}^{3}} W_{k i j l}\left[\delta_{\alpha}^{k} \delta_{\beta}^{l}+\delta_{\beta}^{k} \delta_{\alpha}^{l}-4 x_{\beta}\left(\delta_{\alpha}^{k} x^{l}+x^{k} \delta_{\alpha}^{l}\right)-4\left(\delta_{\alpha \beta} x^{k} x^{l}+x_{\alpha}\left(\delta_{\beta}^{k} x^{l}+x^{k} \delta_{\beta}^{l}\right)\right)\right. \\
&\left.+24 x_{\alpha} x_{\beta} x^{k} x^{l}\right] \partial_{\tau \xi}^{2} A_{s t}(0) x^{\eta} x^{\xi} d \sigma+O\left(\gamma^{2}\right)
\end{aligned}$$

Lemma 4.3. There holds
$$\int_{\partial B_{\gamma}} \dot{W}_{\eta i j \beta} \partial^{\beta} F^{i j} \nu^{\eta} d \sigma=\mathcal{C}_{2} \gamma^{-4}+\frac{\pi^{2}}{6} \partial^{k l} A^{i j}(0) W_{k i j l}+O\left(\gamma^{2}\right), \quad \text { as } \gamma \rightarrow 0^{+}$$
for a real constant $\mathcal{C}_{2}=\mathcal{C}_{2}\left(W^{M}(p)\right)$.

Proof. By looking at (4.9), (4.10), it is easy to see (after a change of variables) that the first term on the RHS of (4.24) is of order $\gamma^{-4}$. Since from (4.24) it is clear that all the other terms are of order 1, we conclude from (4.23) and (4.24) that
$$\begin{aligned}
\frac{1}{2} \int_{\partial B_{\gamma}}\left[\partial_{\eta j}^{2} K_{i \beta}\right. & \left.+\partial_{i \beta}^{2} K_{\eta j}-\partial_{\eta \beta}^{2} K_{i j}-\partial_{i j}^{2} K_{\eta \beta}\right] \partial^{\beta} K^{i j} \nu^{\eta} d \sigma \\
+ & \frac{1}{4} \int_{\partial B_{\gamma}}\left[\Delta K_{i j} \partial^{\beta} K^{i j} \nu_{\beta}-\Delta K_{i \beta} \partial^{\beta} K^{i j} \nu_{j}\right] d \sigma=: \mathcal{C}_{2} \gamma^{-4}
\end{aligned}$$
where $\mathcal{C}_{2}=\mathcal{C}_{2}\left(W^{M}(p)\right)$ is the constant appearing in (4.25).
We now focus on the contribution of order 1; by looking again at (4.23) and (4.24), we see that it is given by the following integrals:
$$\begin{aligned}
& -\frac{1}{6} \int_{\mathbb{S}^{3}}\left(\partial^{\eta j} A^{i \beta}(0)+\partial^{i \beta} A^{\eta j}(0)-\partial^{\eta \beta} A^{i j}(0)-\partial^{i j} A^{\eta \beta}(0)\right) W_{\mu i j \nu}\left(\delta_{\beta}^{\mu} x^{\nu}+x^{\mu} \delta_{\beta}^{\nu}-4 x_{\beta} x^{\mu} x^{\nu}\right) x_{\eta} \\
& -\frac{1}{12} \int_{\mathbb{S}^{3}}\left[W_{\mu i j \nu}\left(\delta_{\beta}^{\mu} x^{\nu}+x^{\mu} \delta_{\beta}^{\nu}-4 x_{\beta} x^{\mu} x^{\nu}\right)\left(\Delta A^{i j}(0) x^{\beta}-\Delta A^{i \beta}(0) x^{j}\right)\right. \\
- & \frac{1}{6} \int_{\mathbb{S}^{3}} W_{k i \beta l}\left[\delta_{\eta}^{k} \delta_{j}^{l}+\delta_{j}^{k} \delta_{\eta}^{l}-4 x_{\eta}\left(\delta_{j}^{k} x^{l}+x^{k} \delta_{j}^{l}\right)-4\left(\delta_{j \eta} x^{k} x^{l}+x_{j}\left(\delta_{\eta}^{k} x^{l}+x^{k} \delta_{\eta}^{l}\right)\right)+24 x_{j} x_{\eta} x^{k} x^{l}\right] \partial^{\beta \xi} A^{i j}(0) x^{\eta} x_{\xi} \\
- & \frac{1}{6} \int_{\mathbb{S}^{3}} W_{k \eta j l}\left[\delta_{i}^{k} \delta_{\beta}^{l}+\delta_{\beta}^{k} \delta_{i}^{l}-4 x_{\beta}\left(\delta_{i}^{k} x^{l}+x^{k} \delta_{i}^{l}\right)-4\left(\delta_{i \beta} x^{k} x^{l}+x_{i}\left(\delta_{\beta}^{k} x^{l}+x^{k} \delta_{\beta}^{l}\right)\right)+24 x_{i} x_{\beta} x^{k} x^{l}\right] \partial^{\beta \xi} A^{i j}(0) x^{\eta} x_{\xi} \\
+ & \frac{1}{6} \int_{\mathbb{S}^{3}} W_{k i j l}\left[\delta_{\eta}^{k} \delta_{\beta}^{l}+\delta_{\beta}^{k} \delta_{\eta}^{l}-4 x_{\beta}\left(\delta_{\eta}^{k} x^{l}+x^{k} \delta_{\eta}^{l}\right)-4\left(\delta_{\eta \beta} x^{k} x^{l}+x_{\eta}\left(\delta_{\beta}^{k} x^{l}+x^{k} \delta_{\beta}^{l}\right)\right)+24 x_{\eta} x_{\beta} x^{k} x^{l}\right] \partial^{\beta \xi} A^{i j}(0) x^{\eta} x_{\xi} \\
+ & \frac{1}{6} \int_{\mathbb{S}^{3}} W_{k \eta \beta l}\left[\delta_{i}^{k} \delta_{j}^{l}+\delta_{j}^{k} \delta_{i}^{l}-4 x_{j}\left(\delta_{i}^{k} x^{l}+x^{k} \delta_{i}^{l}\right)-4\left(\delta_{i j} x^{k} x^{l}+x_{i}\left(\delta_{j}^{k} x^{l}+x^{k} \delta_{j}^{l}\right)\right)+24 x_{i} x_{j} x^{k} x^{l}\right] \partial^{\beta \xi} A^{i j}(0) x^{\eta} x_{\xi} \\
- & \frac{1}{12} \sum_{\alpha} \int_{\mathbb{S}^{3}} W_{k i j l}\left[2 \delta_{\alpha}^{k} \delta_{\alpha}^{l}-4 x_{\alpha}\left(\delta_{\alpha}^{k} x^{l}+x^{k} \delta_{\alpha}^{l}\right)-4 x^{k} x^{l}-4 x_{\alpha}\left(\delta_{\alpha}^{k} x^{l}+x^{k} \delta_{\alpha}^{l}\right)+24\left(x_{\alpha}\right)^{2} x^{k} x^{l}\right] \partial^{\beta \xi} A^{i j}(0) x_{\beta} x_{\xi} \\
+ & \frac{1}{12} \sum_{\alpha} \int_{\mathbb{S}^{3}} W_{k i \beta l}\left[2 \delta_{\alpha}^{k} \delta_{\alpha}^{l}-4 x_{\alpha}\left(\delta_{\alpha}^{k} x^{l}+x^{k} \delta_{\alpha}^{l}\right)-4 x^{k} x^{l}-4 x_{\alpha}\left(\delta_{\alpha}^{k} x^{l}+x^{k} \delta_{\alpha}^{l}\right)+24\left(x_{\alpha}\right)^{2} x^{k} x^{l}\right] \partial^{\beta \xi} A^{i j}(0) x_{j} x_{\xi}
\end{aligned}$$
We need to compute each term in (4.27). We start noticing that
$$\begin{aligned}
\int_{\mathbb{S}^{3}} W_{\mu i j \nu}\left(\delta_{\beta}^{\mu} x^{\nu}+x^{\mu} \delta_{\beta}^{\nu}-4 x_{\beta} x^{\mu} x^{\nu}\right) x_{\eta} & =\int_{\mathbb{S}^{3}}\left(W_{\beta i j \nu} x^{\nu}+W_{\mu i j \beta} x^{\mu}\right) x_{\eta}-4 W_{\mu i j \nu} \int_{\mathbb{S}^{3}} x_{\beta} x^{\mu} x^{\nu} x_{\eta} \\
& =\left(W_{\beta i j \eta}+W_{\eta i j \beta}\right) \int_{\mathbb{S}^{3}}\left(x_{\eta}\right)^{2}-4 W_{\mu i j \nu} \int_{\mathbb{S}^{3}} x_{\beta} x^{\mu} x^{\nu} x_{\eta} \\
& =\frac{\pi^{2}}{2}\left(W_{\beta i j \eta}+W_{\eta i j \beta}\right)-\frac{\pi^{2}}{3} W_{\mu i j \nu}\left(\delta_{\beta \eta} \delta^{\mu \nu}+\delta_{\beta}^{\mu} \delta_{\eta}^{\nu}+\delta_{\beta}^{\nu} \delta_{\eta}^{\mu}\right) \\
& =\frac{\pi^{2}}{6}\left(W_{\beta i j \eta}+W_{\eta i j \beta}\right),
\end{aligned}$$
where we used (cf. [Bre08, Corollary 29])
$$\int_{\mathbb{S}^{3}} x_{\eta} x_{\nu}=\frac{\pi^{2}}{2} \delta_{\eta \nu},$$
(4.20) and the trace-free property of Weyl tensor. Similar computations also show that
$$\int_{\mathbb{S}^{3}} W_{\mu i j \nu}\left(\delta_{\beta}^{\mu} x^{\nu}+x^{\mu} \delta_{\beta}^{\nu}-4 x_{\beta} x^{\mu} x^{\nu}\right) x^{\beta}=0=\int_{\mathbb{S}^{3}} W_{\mu i j \nu}\left(\delta_{\beta}^{\mu} x^{\nu}+x^{\mu} \delta_{\beta}^{\nu}-4 x_{\beta} x^{\mu} x^{\nu}\right) x^{j} .$$

Next, we got
$$\begin{aligned}
& \int_{\mathbb{S}^{3}} W_{k i \beta l} {\left[\delta_{\eta}^{k} \delta_{j}^{l}+\delta_{j}^{k} \delta_{\eta}^{l}-4 x_{\eta}\left(\delta_{j}^{k} x^{l}+x^{k} \delta_{j}^{l}\right)-4\left(\delta_{j \eta} x^{k} x^{l}+x_{j}\left(\delta_{\eta}^{k} x^{l}+x^{k} \delta_{\eta}^{l}\right)\right)+24 x_{j} x_{\eta} x^{k} x^{l}\right] \partial^{\beta \xi} A^{i j} x^{\eta} x_{\xi} } \\
&=\int\left(W_{\eta i \beta j}+W_{j i \beta \eta}\right) \partial^{\beta \xi} A^{i j} x^{\eta} x_{\xi}-4 \int\left(W_{j i \beta k}+W_{k i \beta j}\right) \partial^{\beta \xi} A^{i j} x^{k} x_{\xi} \\
&-4 \int\left[W_{k i \beta l} \partial^{\beta \xi} A^{i j} x^{k} x^{l} x_{j} x_{\xi}+\left(W_{\eta i \beta k}+W_{k i \beta \eta}\right) \partial^{\beta \xi} A^{i j} x^{k} x^{\eta} x_{j} x_{\xi}\right]+24 W_{k i \beta l} \partial^{\beta \xi} A^{i j} \int x^{k} x^{l} x_{j} x_{\xi} \\
&=-\frac{3}{2} \pi^{2} \partial^{\beta \xi} A^{i j}\left(W_{\xi i \beta j}+W_{j i \beta \xi}\right)-\frac{\pi^{2}}{3} \partial^{\beta \xi} A^{i j}\left(3 W_{j i \beta \xi}+3 W_{\xi i \beta j}\right)+2 \pi^{2}\left(W_{j i \beta \xi}+W_{\xi i \beta j}\right) \\
&=-\frac{\pi^{2}}{2} \partial^{\beta \xi} A^{i j}(0)\left(W_{j i \beta \xi}+W_{\xi i \beta j}\right) .
\end{aligned}$$
Similarly,
$$\begin{aligned}
\int_{\mathbb{S}^{3}} & W_{k \eta j l}\left[\delta_{i}^{k} \delta_{\beta}^{l}+\delta_{\beta}^{k} \delta_{i}^{l}-4 x_{\beta}\left(\delta_{i}^{k} x^{l}+x^{k} \delta_{i}^{l}\right)-4\left(\delta_{i \beta} x^{k} x^{l}+x_{i}\left(\delta_{\beta}^{k} x^{l}+x^{k} \delta_{\beta}^{l}\right)\right)+24 x_{i} x_{\beta} x^{k} x^{l}\right] \partial^{\beta \xi} A^{i j} x^{\eta} x_{\xi} \\
& =\int\left(W_{i \eta j \beta}+W_{\beta \eta j i}\right) \partial^{\beta \xi} A^{i j} x^{\eta} x_{\xi}-4 \int\left(W_{i \eta j k}+W_{k \eta j i}\right) \partial^{\beta \xi} A^{i j} x_{\beta} x^{k} x^{\eta} x_{\xi} \\
& -4 \sum_{i} W_{k \eta j l} \partial^{i \xi} A^{i j} \int x^{k} x^{l} x^{\eta} x_{\xi}-4 \int\left(W_{\beta \eta j k}+W_{k \eta j \beta}\right) \partial^{\beta \xi} A^{i j} x_{i} x^{k} x^{\eta} x_{\xi}+0 \\
& =\frac{\pi^{2}}{2} \partial^{\beta \xi} A^{i j}\left(W_{i \xi j \beta}+W_{\beta \xi j i}\right)-\frac{\pi^{2}}{3} \partial^{\beta \xi} A^{i j}\left(W_{i \xi j \beta}+W_{\beta \xi j i}+W_{i \beta j \xi}+W_{\xi \beta j i}\right) \\
& -0-\frac{\pi^{2}}{3} \partial^{\beta \xi} A^{i j}\left(W_{\beta \xi j i}+W_{i \xi j \beta}+W_{\beta i j \xi}+W_{\xi i j \beta}\right) \\
& =\frac{\pi^{2}}{6} \partial^{\beta \xi} A^{i j}\left(W_{i \xi j \beta}+W_{\beta \xi j i}\right) .
\end{aligned}$$
Also, by exchanging the indices $\beta$ and $j$ in (4.31) (except on $A$ ), we immediately see that
$$\begin{aligned}
\int_{\mathbb{S}^{3}} W_{k i j l} & {\left[\delta_{\eta}^{k} \delta_{\beta}^{l}+\delta_{\beta}^{k} \delta_{\eta}^{l}-4 x_{\beta}\left(\delta_{\eta}^{k} x^{l}+x^{k} \delta_{\eta}^{l}\right)-4\left(\delta_{\eta \beta} x^{k} x^{l}+x_{\eta}\left(\delta_{\beta}^{k} x^{l}+x^{k} \delta_{\beta}^{l}\right)\right)+24 x_{\eta} x_{\beta} x^{k} x^{l}\right] \partial^{\beta \xi} A^{i j} x^{\eta} x_{\xi} } \\
& =-\frac{\pi^{2}}{2} \partial^{\beta \xi} A^{i j}(0)\left(W_{\xi i j \beta}+W_{\beta i j \xi}\right)
\end{aligned}$$
Exchanging instead $\beta$ and $j$ in (4.32) (except on $A$ ), we got
$$\begin{aligned}
\int_{\mathbb{S}^{3}} W_{k \eta \beta l} & {\left[\delta_{i}^{k} \delta_{j}^{l}+\delta_{j}^{k} \delta_{i}^{l}-4 x_{j}\left(\delta_{i}^{k} x^{l}+x^{k} \delta_{i}^{l}\right)-4\left(\delta_{i j} x^{k} x^{l}+x_{i}\left(\delta_{j}^{k} x^{l}+x^{k} \delta_{j}^{l}\right)\right)+24 x_{i} x_{j} x^{k} x^{l}\right] \partial^{\beta \xi} A^{i j} x^{\eta} x_{\xi} } \\
& =\frac{\pi^{2}}{6} \partial^{\beta \xi} A^{i j}(0)\left(W_{i \xi \beta j}+W_{j \xi \beta i}\right)
\end{aligned}$$
Finally, we also have
$$\begin{gathered}
\sum_{\alpha} \int_{\mathbb{S}^{3}} W_{k i j l}\left[2 \delta_{\alpha}^{k} \delta_{\alpha}^{l}-4 x_{\alpha}\left(\delta_{\alpha}^{k} x^{l}+x^{k} \delta_{\alpha}^{l}\right)-4 x^{k} x^{l}-4 x_{\alpha}\left(\delta_{\alpha}^{k} x^{l}+x^{k} \delta_{\alpha}^{l}\right)+24\left(x_{\alpha}\right)^{2} x^{k} x^{l}\right] \partial^{\beta \xi} A^{i j} x_{\beta} x_{\xi} \\
=-8 \partial^{\beta \xi} A^{i j} W_{k i j l} \int x^{k} x^{l} x_{\beta} x_{\xi}=-\frac{2}{3} \pi^{2} \partial^{\beta \xi} A^{i j}\left(W_{\beta i j \xi}+W_{\xi i j \beta}\right)
\end{gathered}$$
and
$$\begin{gathered}
\sum_{\alpha} \int_{\mathbb{S}^{3}} W_{k i \beta l}\left[2 \delta_{\alpha}^{k} \delta_{\alpha}^{l}-4 x_{\alpha}\left(\delta_{\alpha}^{k} x^{l}+x^{k} \delta_{\alpha}^{l}\right)-4 x^{k} x^{l}-4 x_{\alpha}\left(\delta_{\alpha}^{k} x^{l}+x^{k} \delta_{\alpha}^{l}\right)+24\left(x_{\alpha}\right)^{2} x^{k} x^{l}\right] \partial^{\beta \xi} A^{i j} x_{j} x_{\xi} \\
=-8 \partial^{\beta \xi} A^{i j} W_{k i \beta l} \int x^{k} x^{l} x_{j} x_{\xi}=-\frac{2}{3} \pi^{2} \partial^{\beta \xi} A^{i j}\left(W_{j i \beta \xi}+W_{\xi i \beta j}\right)
\end{gathered}$$

Substituting (4.28), (4.30), (4.31), (4.32), (4.33), (4.34), (4.35) and (4.36) inside (4.27) and using the symmetries of the curvature tensor and the fact that $A$ is symmetric, we get
$$\begin{aligned}
& -\frac{1}{6}\left[\left(\partial^{\eta j} A^{i \beta}(0)+\partial^{i \beta} A^{\eta j}(0)-\partial^{\eta \beta} A^{i j}(0)-\partial^{i j} A^{\eta \beta}(0)\right) \frac{\pi^{2}}{6}\left(W_{\beta i j \eta}+W_{\eta i j \beta}\right)\right] \\
& -\frac{1}{6}\left[-\frac{\pi^{2}}{2} \partial^{\beta \xi} A^{i j}(0)\left(W_{j i \beta \xi}+W_{\xi i \beta j}\right)+\frac{\pi^{2}}{6} \partial^{\beta \xi} A^{i j}(0)\left(W_{i \xi j \beta}+W_{\beta \xi j i}\right)\right] \\
& +\frac{1}{6}\left[-\frac{\pi^{2}}{2} \partial^{\beta \xi} A^{i j}(0)\left(W_{\xi i j \beta}+W_{\beta i j \xi}\right)+\frac{\pi^{2}}{6} \partial^{\beta \xi} A^{i j}(0)\left(W_{i \xi \beta j}+W_{j \xi \beta i}\right)\right] \\
& +\frac{\pi^{2}}{18} \partial^{\beta \xi} A^{i j}(0)\left(W_{\beta i j \xi}+W_{\xi i j \beta}\right)-\frac{\pi^{2}}{18} \partial^{\beta \xi} A^{i j}(0)\left(W_{j i \beta \xi}+W_{\xi i \beta j}\right) \\
& =-\frac{1}{6}\left[\frac{\pi^{2}}{3}\left(\partial^{i \beta} A^{\eta j}(0)-\partial^{\eta \beta} A^{i j}(0)\right)\left(W_{\beta i j \eta}+W_{\eta i j \beta}\right)-\frac{\pi^{2}}{3} \partial^{\beta \xi} A^{i j}(0)\left(W_{\xi i \beta j}+W_{j i \beta \xi}\right)\right] \\
& -\frac{\pi^{2}}{18} \partial^{\beta \xi} A^{i j}(0)\left(W_{\xi i j \beta}+W_{\beta i j \xi}\right)+\frac{\pi^{2}}{18} \partial^{\beta \xi} A^{i j}(0)\left(W_{\beta i j \xi}+W_{\xi i j \beta}\right)-\frac{\pi^{2}}{18} \partial^{\beta \xi} A^{i j}(0)\left(W_{j i \beta \xi}+W_{\xi i \beta j}\right) \\
& =-\frac{\pi^{2}}{18} \partial^{i \beta} A^{\eta j}(0)\left(W_{\beta i j \eta}+W_{\eta i j \beta}\right)+\frac{\pi^{2}}{18} \partial^{\beta \xi} A^{i j}(0)\left(W_{\beta i j \xi}+W_{\xi i j \beta}\right) .
\end{aligned}$$
Finally, using again the symmetries of $W$ and $A$ together with Bianchi identity, we obtain the second term in the RHS of (4.25).

Since the remainder is $O\left(\gamma^{2}\right)$ (see (4.24)), the result follows. \(\square\)

It only remains to compute explicitly the coefficients $\mathcal{C}_{1}$ and $\mathcal{C}_{2}$ appearing in (4.12) and (4.25).
Lemma 4.4. Let $\mathcal{C}_{1}, \mathcal{C}_{2}$ be defined as in (4.19), (4.26) respectively. Then
$$\mathcal{C}_{2}-\mathcal{C}_{1}=\frac{\pi^{2}}{4}\left|W^{M}(p)\right|^{2} .$$
Proof. By definition, we got
$$\begin{aligned}
\left(\mathcal{C}_{2}-\mathcal{C}_{1}\right) \gamma^{-4}= & \frac{1}{2} \int_{\partial B_{\gamma}}\left[\partial_{\eta j}^{2} K_{i \beta}+\partial_{i \beta}^{2} K_{\eta j}-\partial_{\eta \beta}^{2} K_{i j}-\partial_{i j}^{2} K_{\eta \beta}\right] \partial^{\beta} K^{i j} \nu^{\eta} d \sigma \\
& +\frac{1}{4} \int_{\partial B_{\gamma}}\left[\Delta K_{i j} \partial^{\beta} K^{i j} \nu_{\beta}-\Delta K_{i \beta} \partial^{\beta} K^{i j} \nu_{j}\right] d \sigma . \\
& -\frac{1}{4} \int_{\partial B_{\gamma}}\left[\partial_{j} \Delta K_{i \beta}-\partial_{\beta} \Delta K_{i j}\right] K^{i j} \nu^{\beta} d \sigma
\end{aligned}$$

Consider the family of metrics $g_{t}:=g_{E}+t K$. Expanding the Weyl energy of $g_{t}$ at $t=0$ in $\mathbb{R}^{4} \backslash B_{\gamma}(0)$ (as in (4.3), (4.4)), we have
$$\int_{\mathbb{R}^{4} \backslash B_{\gamma}}\left|W^{g_{t}}\right|^{2} d V_{g_{t}}=-2 t^{2} \int_{\mathbb{R}^{4} \backslash B_{\gamma}} \dot{W}_{\alpha i j \beta} \partial^{\alpha} \partial^{\beta} K^{i j} d x+O\left(t^{3}\right), \quad \text { as } t \rightarrow 0$$
By looking at the definition of $K$ (4.9) and the formula for the linearized Weyl tensor (4.7), we notice that all the integrands on the RHS decay as $|x|^{-8}$ as $|x| \rightarrow \infty$, therefore we can integrate by parts twice as in (4.5). Recalling further that $K$ is TT and biharmonic (so in the kernel of the linearized Weyl at $g_{E}$ ), as in (4.6) we get
$$\int_{\mathbb{R}^{4} \backslash B_{\gamma}}\left|W^{g_{t}}\right|^{2} d V_{g_{t}}=2 t^{2}\left(\int_{\partial B_{\gamma}} \dot{W}_{\eta i j \beta} \partial^{\beta} K^{i j} \nu^{\eta} d \sigma-\int_{\partial B_{\gamma}} \partial^{\alpha} \dot{W}_{\alpha i j \eta} K^{i j} \nu^{\eta} d \sigma\right)+O\left(t^{3}\right),$$
where $\nu=x /|x|$ points toward the interior of $\mathbb{R}^{4} \backslash B_{\gamma}$. But now, using again (4.7) we see that indeed
$$\int_{\mathbb{R}^{4} \backslash B_{\gamma}}\left|W^{g_{t}}\right|^{2} d V_{g_{t}}=2 \frac{t^{2}}{\gamma^{4}}\left(\mathcal{C}_{2}-\mathcal{C}_{1}\right)+O\left(t^{3}\right)$$

Let us define
$$g(x)=\left(\delta_{i j}-\frac{1}{3} W_{k i j l} x^{k} x^{l}\right) d x^{i} d x^{j} .$$
If we let $y:=I(x)=x /|x|^{2}$, then
$$\tilde{g}(y):=I^{*}\left(|x|^{-4} g\right)(y)=\left(\delta_{i j}-\frac{1}{3} W_{k i j l} \frac{y^{k} y^{l}}{|y|^{4}}\right) d y^{i} d y^{j}$$
and therefore $t \tilde{g}=g_{t}$. Hence
$$\int_{\mathbb{R}^{4} \backslash B_{\gamma}}\left|W^{g_{t}}\right|^{2} d V_{g_{t}}=\int_{\mathbb{R}^{4} \backslash B_{\gamma / \sqrt{t}}}\left|W^{\tilde{g}}\right|^{2} d V_{\tilde{g}}=\int_{B_{\sqrt{t} / \gamma}}\left|W^{g}\right|^{2} d V_{g}=\frac{\pi^{2}}{2} \frac{t^{2}}{\gamma^{4}}\left|W^{M}(p)\right|^{2}+O\left(\frac{t^{3}}{\gamma^{6}}\right)$$
The result then follows from (4.37) and (4.38). \(\square\)

As a consequence of (4.6), Lemma 4.1 and Lemma 4.3 and Lemma 4.4, we obtain the expansion for the Weyl energy on $Z$ :

Corollary 4.5. Let $g_{b}$ be defined as in (4.1). Then
$$\mathcal{W}_{\gamma}^{Z}\left(g_{b}\right)=\int_{Z \backslash B_{\gamma}^{g_{Z}}(q)}\left|W^{g_{b}}\right|^{2} d V_{g_{b}}=\frac{\pi^{2}}{2} \frac{b^{4}}{\gamma^{4}}\left|W^{M}(p)\right|^{2}+O\left(b^{4} \gamma^{2}\right), \quad \text { as } 0 \ll b \ll \gamma \ll 1$$

\section*{5 Weyl energy of the perturbed non LCF metric}

On the Bach-flat manifold $\left(M, g_{M}\right)$, we want to adjust the metric in order to match its inverted and scaled counterpart to the modified metric $g_{b}$ on $Z$ (defined by (4.1)). The idea is that, since $A(0)=0$ and $\nabla A(0)=0$ (see (3.21), (3.38)), we want to add a perturbation to $g_{M}$ to match $\nabla_{k l}^{2} A_{i j}(0) x^{k} x^{l}$.

In conformal normal coordinates at $p \in M$, there exists $\varepsilon>0$ (small) such that
$$g_{M}=\left(\delta_{i j}-\frac{1}{3} W_{k i j l} z^{k} z^{l}+\zeta_{i j}(z)\right) d z^{i} d z^{j}, \quad|z|<4 \varepsilon,$$
where $\zeta_{i j}(z)=O^{(4)}(|z|)^{3}$ as $|z| \rightarrow 0$. Let us consider a smooth cutoff function $\phi$ satisfying $0 \leq \phi(r) \leq 1$ $\forall r \geq 0, \varphi(r) \equiv 0$ for $r \geq 2 \varepsilon$ and $\phi(r) \equiv 1$ for $r \leq \varepsilon$. We define a smooth tensor $H$ in $M \backslash\{p\}$ as
$$H_{i j}(z):=\frac{1}{2} \partial_{k l}^{2} A_{i j}(0) \frac{z^{k} z^{l}}{|z|^{4}} \phi(|z|)=: T_{k i j l} \frac{z^{k} z^{l}}{|z|^{4}} \phi(|z|), \quad \text { for }|z| \leq 4 \varepsilon,$$
with $H \equiv 0$ in $M \backslash B_{2 \varepsilon}^{g_{M}}(p)$. Letting $\tilde{g}_{M}:=g_{M}+a^{4} H$, one has
$$\tilde{g}_{M}=\left(\delta_{i j}-\frac{1}{3} W_{k i j l} z^{k} z^{l}+a^{4} T_{k i j l} \frac{z^{k} z^{l}}{|z|^{4}}+\zeta_{i j}(z)\right) d z^{i} d z^{j}, \quad|z|<\varepsilon$$
If we now multiply the metric $\tilde{g}_{M}$ via a positive function $f$ on $M \backslash\{p\}$, satisfying $f(z)=|z|^{-2}$ near $p$, and call $y=z /|z|^{2}$ the inverted conformal normal coordinates, by Lemma 2.2 we get
$$f^{2} \tilde{g}_{M}=: \tilde{g}_{N}=\left(\delta_{i j}-\frac{1}{3} W_{k i j l} \frac{y^{k} y^{l}}{|y|^{4}}+a^{4} T_{k i j l} y^{k} y^{l}+\tilde{\zeta}_{i j}(y)\right) d y^{i} d y^{j}, \quad|y|>\frac{1}{\varepsilon},$$
where $\tilde{\zeta}_{i j}(y)=O^{(4)}\left(|y|^{-3}\right)$ as $|y| \rightarrow+\infty$. Letting now $g_{a}:=a^{2} \tilde{g}_{N}$, then $x:=a y$ are the inverted normal coordinates for $g_{a}$ and one has
$$g_{a}=\left(\delta_{i j}-\frac{1}{3} a^{2} W_{k i j l} \frac{x^{k} x^{l}}{|x|^{4}}+a^{2} T_{k i j l} x^{k} x^{l}+\zeta_{i j}^{a}(x)\right) d x^{i} d x^{j}, \quad|x|>\frac{a}{\varepsilon},$$
where now $\zeta^{a}$ satisfies
$$\left|\nabla^{k} \zeta_{i j}^{a}(x)\right| \leq C a^{3}|x|^{-3-k}, \quad \text { for }|x|>\frac{a}{\varepsilon}, k=0, \ldots, 4 .$$

From (5.2), (4.1), (5.1) and (3.24) we see that, letting $a=b$ we can match $g_{a}^{M}$ and $g_{b}^{Z}$ in a very precise way (see Section 6.1 for the explicit construction).

We now want to compute the Weyl energy of the modified metric $g_{a}$ defined in (5.2). If we glue $\left(N=M \backslash\{p\}, g_{a}\right)$ to $\left(Z, g_{b}\right)$ at scale $\gamma$ (with $a=b \ll \gamma \ll 1$ ), then, being $\gamma=|x|=a|z|^{-1}$, we got $|z|=a \gamma^{-1}$ and therefore, using the pointwise conformal invariance of $\left|W^{g}\right|^{2} d V_{g}$, we need to compute
$$\int_{M \backslash B_{a \gamma^{-1}}^{g_{M}}(p)}\left|W^{\tilde{g}_{M}}\right|^{2} d V_{\tilde{g}_{M} .}$$
Recalling the definition of $\tilde{g}_{M}$, we let $t:=a^{4}$ and employ the notation
$$\tilde{g}_{M}=g_{t}:=g_{M}+t H, \quad V(t):=\int_{M \backslash B_{t^{1 / 4} \gamma^{-1}}^{g_{M}}(p)}\left|W^{g_{t}}\right|^{2} d V_{g_{t}} .$$
We would now like to Taylor-expand $V$ at 0 , obtaining
$$V(t)=\mathcal{W}^{M}\left(g_{M}\right)+\left.t \frac{d}{d t}\right|_{t=0} V(t)+o(t) .$$
However, it is not immediately clear whether $V$ and $V^{\prime}$ are continuous up to zero.
Lemma 5.1. $V$ is continuous up to zero and $V(0)=\mathcal{W}^{M}\left(g_{M}\right)$.
Proof. By definition of $g_{t}$, for $|z|$ close to 0 we got
$$g_{t}=g_{M}+t O\left(|z|^{-2}\right), \quad \nabla g_{t}=\nabla g_{M}+t O\left(|z|^{-3}\right), \quad \nabla^{2} g_{t}=\nabla^{2} g_{M}+t O\left(|z|^{-4}\right),$$
where ∇ denotes the Euclidean gradient (w.r.t. the coordinates $z$ ). Moreover, for $a=t^{1 / 4}<|z|<\varepsilon$, the metric $g_{t}^{-1}$ has the following expansion:
$$g_{t}^{-1}=\left(\delta_{i j}+\frac{1}{3} W_{k i j l} z^{k} z^{l}-a^{4} T_{k i j l} \frac{z^{k} z^{l}}{|z|^{4}}+O^{(3)}\left(|z|^{3}\right)\right) d z^{i} d z^{j}, \quad a=t^{1 / 4}<|z|<\varepsilon,$$
so one also has
$$g_{t}^{-1}=g_{M}^{-1}+t O\left(|z|^{-2}\right), \quad \nabla g_{t}^{-1}=\nabla g_{M}^{-1}+t O\left(|z|^{-3}\right), \quad t^{1 / 4}<|z|<\varepsilon .$$
Notice that here the error terms do not depend on $t$ (but the range of $|z|$ in which the expansion holds does). Now, the Weyl tensor contains up to second order derivatives of the metric, and, if we look closely at $\left|W^{g_{t}}\right|^{2}$, we see that it has (at worst) additional terms given by perturbations of order $\approx t^{2}|z|^{-8}+t|z|^{-4}$. In other words,
$$\left|W^{g_{t}}\right|_{g_{t}}^{2}=\left|W^{g_{M}}\right|_{g_{M}}^{2}+t^{2} O\left(|z|^{-8}\right)+t O\left(|z|^{-4}\right), \quad t^{1 / 4}<|z|<\varepsilon .$$
But now
$$\int_{B_{\varepsilon} \backslash B_{t^{1 / 4} \gamma^{-1}}}\left(t^{2}|z|^{-8}+t|z|^{-4}\right) d z \approx t \int_{t^{1 / 4} \gamma^{-1}}^{\varepsilon} r^{-1} d r=O(t(\log t)) \quad \text { as } t \rightarrow 0^{+}$$
which implies that $V(t) \rightarrow V(0)=\int_{M}\left|W^{g_{M}}\right|^{2} d V_{g_{M}}=\mathcal{W}^{M}\left(g_{M}\right)$ as $t \rightarrow 0^{+}$(the error given by the perturbation vanishes in the limit). \(\square\)

Lemma 5.2. $V$ is differentiable at 0 and one has
$$V^{\prime}(0)=-\frac{\pi^{2}}{2} \gamma^{-4}\left|W^{M}(p)\right|^{2}+\frac{4}{3} W_{k i j l}^{M} T^{k i j l}+O\left(\gamma^{4}\right) .$$
Proof. In order to compute $V^{\prime}(0)$, we first compute $V^{\prime}(s)$ for $s>0$ and then take the limit as $s \rightarrow 0^{+}$. Using the chain rule, one has
$$\left.V^{\prime}(s)=-4 \int_{M \backslash B_{s^{1 / 4} \gamma^{-1}}^{g_{M}}}\left(W_{\alpha i j \beta}^{g_{s}} \nabla^{\alpha} \nabla^{\beta} H^{i j}+\frac{1}{2} R_{g_{s}}^{\alpha \beta} W_{\alpha i j \beta}^{g_{s}} H^{i j}\right) d V_{g_{s}}-\int_{\partial B_{s^{1 / 4} \gamma^{-1}}^{g_{M}}}\left|W^{g_{s}}\right|^{2} \frac{1}{4 \gamma s^{3 / 4}} d \phi_{s_{s}} \cdot 10\right)$$
We now claim that, up to a (small) error term, it is possible to substitute $g_{s}=g_{M}+s H$ by $g_{M}$ in the above expression. Indeed, consider for instance the first term of the first integral. Then, recalling (5.6), (5.7) and the formula for Weyl's tensor in local coordinates (2.1), one sees that
$$\begin{aligned}
& \left|\int_{M \backslash B_{s^{1 / 4} \gamma^{-1}}^{g_{M}}} W_{\alpha i j \beta}^{g_{s}} \nabla^{\alpha} \nabla^{\beta} H^{i j} d V_{g_{s}}-\int_{M \backslash B_{s^{1 / 4} \gamma^{-1}}^{g_{M}}} W_{\alpha i j \beta}^{g_{M}} \nabla^{\alpha} \nabla^{\beta} H^{i j} d V_{g_{M}}\right| \\
& \quad \leq C s+C \int_{B_{\varepsilon} \backslash B_{s^{1 / 4} \gamma^{-1}}^{g_{M}}} s\left(|z|^{-2}+|z|^{-3}+|z|^{-4}\right)|z|^{-4} d V_{g_{M}} \leq C s+C \gamma^{4},
\end{aligned}$$
where we also used that $d V_{g_{s}}=d V_{g_{M}}+O\left(s^{1 / 4}\right) d x$. Arguing in the same way, we also see that the second term of the first integral generates an error of order $\sqrt{s}$. As for the last integral in (5.10), using (5.8) we only obtain
$$\int_{\partial B_{s^{1 / 4} \gamma^{-1}}^{g_{M}}}\left|W^{g_{s}}\right|^{2} \frac{1}{4 \gamma s^{3 / 4}} d \sigma_{g_{s}}=\int_{\partial B_{s^{1 / 4} \gamma^{-1}}^{g_{M}}}\left|W^{g_{M}}\right|^{2} \frac{1}{4 \gamma s^{3 / 4}} d \sigma_{g_{M}}+O(1),$$
so we actually need to be more precise. Since $d \sigma_{g_{s}}=d \sigma_{g_{M}}+O\left(s^{1 / 4}\right) d \sigma_{\mathbb{S}^{3}}$, we focus only on the squared norm of the Weyl tensor. Being $\gamma \ll 1$, we can Taylor-expand this quantity in $\partial B_{s^{1 / 4} \gamma^{-1}}^{g_{M}}$ and obtain
$$\left|W^{g_{s}}\right|^{2}=\left|W^{g_{M}}\right|^{2}+\underbrace{s\left[-4\left(W_{\alpha i j \beta}^{g_{M}} \nabla^{\alpha} \nabla^{\beta} H^{i j}+\frac{1}{2} R_{g_{M}}^{\alpha \beta} W_{\alpha i j \beta}^{g_{M}} H^{i j}\right)-\frac{1}{2}\left|W^{g_{M}}\right|^{2} g_{M}^{i j} H_{i j}\right]}_{=O\left(\gamma^{4}\right)}+O\left(\gamma^{8}\right) .$$
Then, since $\left|\nabla^{2} H_{i j}\right|=O\left(|z|^{-4}\right)$, one has
$$\int_{\partial B_{s^{1 / 4} \gamma^{-1}}^{g_{M}}}\left|W^{g_{s}}\right|^{2} d \sigma_{g_{s}}=\int_{\partial B_{s^{1 / 4} \gamma^{-1}}^{g_{M}}}\left|W^{g_{M}}\right|^{2} d \sigma_{g_{M}}-4 s \int_{\partial B_{s^{1 / 4} \gamma^{-1}}^{g_{M}}} W_{\alpha i j \beta}^{g_{M}} \nabla^{\alpha} \nabla^{\beta} H^{i j} d \sigma_{g_{M}}+O\left(\gamma^{5} s^{3 / 4}\right)$$
From this formula and a change of variables, it follows that
$$\frac{1}{4 \gamma s^{3 / 4}} \int_{\partial B_{s^{1 / 4} \gamma^{-1}}^{g_{M}}}\left|W^{g_{s}}\right|^{2} d \sigma_{g_{s}}=\frac{\pi^{2}}{2} \gamma^{-4}\left|W^{g_{M}}(p)\right|^{2}-\int_{\mathbb{S}^{3}} W_{\alpha i j \beta}^{g_{M}}(p) \partial^{\alpha} \partial^{\beta} \tilde{H}^{i j} d \sigma+O\left(\gamma^{4}\right)+O\left(s^{1 / 4} \gamma^{\left.\left(5^{1} \cdot\right) 2\right)}\right.$$
where $\tilde{H}_{i j}(x):=T_{k i j l} x^{k} x^{l}|x|^{-4}$. But now, on $\mathbb{S}^{3}$,
$$\partial_{\alpha \beta}^{2} \tilde{H}_{i j}(x)=T_{k i j l}\left[\delta_{\alpha}^{k} \delta_{\beta}^{l}+\delta_{\beta}^{k} \delta_{\alpha}^{l}-4 x_{\beta}\left(\delta_{\alpha}^{k} x^{l}+x^{k} \delta_{\alpha}^{l}\right)-4\left(\delta_{\alpha \beta} x^{k} x^{l}+x_{\alpha}\left(\delta_{\beta}^{k} x^{l}+x^{k} \delta_{\beta}^{l}\right)\right)+24 x_{\alpha} x_{\beta} x^{k} x^{l}\right],$$
so
$$\begin{aligned}
\int_{\mathbb{S}^{3}} W_{g_{M}}^{\alpha i j \beta}(p) \partial_{\alpha} \partial_{\beta} \tilde{H}_{i j} d \sigma= & -W_{g_{M}}^{\alpha i j \beta} \int_{\mathbb{S}^{3}}\left[\left(T_{\alpha i j \beta}+T_{\beta i j \alpha}\right)-4\left(T_{\alpha i j k}+T_{k i j \alpha}\right) x_{\beta} x^{k}\right. \\
& \left.-4\left(T_{\beta i j k}+T_{k i j \beta}\right) x_{\alpha} x^{k}+24 T_{k i j l} x_{\alpha} x_{\beta} x^{k} x^{l}\right] d \sigma \\
= & -W_{g_{M}}^{\alpha i j \beta}\left(2 \pi^{2}-2 \pi^{2}-2 \pi^{2}+2 \pi^{2}\right)\left(T_{\alpha i j \beta}+T_{\beta i j \alpha}\right)=0,
\end{aligned}$$
where the last identity follows from (4.29) and (4.20). Substituting (5.11), (5.12) and (5.13) into (5.10), we finally obtain
$$\begin{gathered}
V^{\prime}(s)=-4 \int_{M \backslash B_{s^{1 / 4} \gamma^{-1}}^{g_{M}}}\left(W_{\alpha i j \beta}^{g_{M}} \nabla^{\alpha} \nabla^{\beta} H^{i j}+\frac{1}{2} R_{g_{M}}^{\alpha \beta} W_{\alpha i j \beta}^{g_{M}} H^{i j}\right) d V_{g_{M}} \\
-\frac{\pi^{2}}{2} \gamma^{-4}\left|W^{M}(p)\right|^{2}+O\left(\gamma^{4}\right)+O\left(s^{1 / 4} \gamma^{-1}\right) .
\end{gathered}$$
Integrating by parts twice and using that $g_{M}$ is Bach-flat, we further have
$$\begin{gathered}
V^{\prime}(s)=4 \int_{\partial B_{s^{1 / 4} \gamma^{-1}}^{g_{M}}} W_{n i j \beta}^{g_{M}} \nabla^{\beta} H^{i j} d \sigma_{g_{M}}-4 \int_{\partial B_{s^{1 / 4} \gamma^{-1}}^{g_{M}}} \nabla^{\beta} W_{n i j \beta}^{g_{M}} H^{i j} d \sigma_{g_{M}} \\
-\frac{\pi^{2}}{2} \gamma^{-4}\left|W^{M}(p)\right|^{2}+O\left(\gamma^{4}\right)+O\left(s^{1 / 4} \gamma^{-1}\right),
\end{gathered}$$
where here $n$ denotes the normal direction pointing towards the exterior of the ball. But now the second integral is an $O\left(s^{1 / 4} \gamma^{-1}\right)$, while, after scaling, the first integral satisfies
$$\begin{aligned}
\int_{\partial B_{s^{1 / 4} \gamma^{-1}}^{g_{M}}} W_{n i j \beta}^{g_{M}} \nabla^{\beta} H^{i j} d \sigma_{g_{M}} & =W_{\alpha i j \beta}^{M}(p) T^{k i j l} \int_{\mathbb{S}^{3}}\left(\delta_{k}^{\beta} x_{l}+x_{k} \delta_{l}^{\beta}-4 x^{\beta} x_{k} x_{l}\right) x^{\alpha} d \sigma_{\mathbb{S}^{3}}+O\left(s^{1 / 4} \gamma^{-1}\right) \\
& =W_{\alpha i j \beta}^{M}(p) \int_{\mathbb{S}^{3}}\left[\left(T^{\beta i j k}+T^{k i j \beta}\right) x^{\alpha} x_{k}-4 T^{k i j l} x^{\alpha} x^{\beta} x_{k} x_{l}\right] d \sigma_{\mathbb{S}^{3}}+O\left(s^{1 / 4} \gamma^{-1}\right) \\
& =W_{\alpha i j \beta}^{M}\left(\frac{\pi^{2}}{2}-\frac{\pi^{2}}{3}\right)\left(T^{\alpha i j \beta}+T^{\beta i j \alpha}\right)+O\left(s^{1 / 4} \gamma^{-1}\right) \\
& =\frac{\pi^{2}}{3} W_{\alpha i j \beta}^{M} T^{\alpha i j \beta}+O\left(s^{1 / 4} \gamma^{-1}\right),
\end{aligned}$$
where we used (4.29), (4.20) and the symmetry of $T$ in $\alpha, \beta$. Substituting inside the formula for $V^{\prime}(s)$ and taking the limit as $s \rightarrow 0^{+}$, we finally obtain (5.9). \(\square\)

By looking at (5.4), (5.5), (5.9) and recalling that $t=a^{4}$, we obtain the following:
Corollary 5.3. Let $g_{a}$ be given by (5.2) (in particular $W=W^{M}(p)$ and $T_{\text {kijl }}=\frac{1}{2} \partial_{k l}^{2} A_{i j}(0)$ ). Then
$$\int_{M \backslash B_{a \gamma^{-1}}^{g_{M}}(p)}\left|W^{\tilde{g}_{M}}\right|^{2} d V_{\tilde{g}_{M}}=\mathcal{W}^{M}\left(g_{M}\right)-\frac{\pi^{2}}{2} \frac{a^{4}}{\gamma^{4}}\left|W^{M}(p)\right|^{2}+\frac{4}{3} a^{4} W^{k i j l} T_{k i j l}+O\left(a^{4} \gamma^{4}\right)+o\left(a^{4}\right),$$
provided $0 \ll a \ll \gamma \ll 1$.
Remark 5.4. The approach adopted here is not the only viable one. Indeed, it is also possible to directly add a quadratic correction to the (scaled and) inverted metric directly in order to obtain an expansion as in (5.2). In this way, it is no longer necessary to project the hessian on its "curvature part" using Lemma 2.1 (as done in Section 3). However, we would then get additional terms when considering the correction in normal coordinates on $M$ during the proof of Lemma 5.2, which would make the above computations significantly more involved.

\section*{6 Conclusion of the proofs}

After having constructed the metric corrections $g_{a}$ on $M$ (see (5.2)) and $g_{b}$ on $Z$ (see (4.1)) and having estimated their Weyl energies in Corollary 5.3 and Corollary 4.5 respectively, we are now in position to define a competitor metric $g_{X}$ on the connected sum $Z \# \bar{M}$ and compute its Weyl energy. As we
will see in Proposition 6.2, the difference between the Weyl energy of $g_{X}$ and that of $g_{M}$ will depend upon the interaction term (3.22), which can be shown to have the right sign (i.e. to be negative) after a proper choice of coordinates on $M$, see Lemma 6.4. This will allow us to prove Theorem 1.1 in this setting, that is, for $Z$ diffeomorphic to a finite quotient of $\mathbb{S}^{1} \times \mathbb{S}^{3}$. Then, in Proposition 6.7 we will deal with the general case in which $Z$ is a connected sum of quotients as in Theorem 3.1. Finally, we will show how to extend the result to the orbifold setting and prove Theorem 1.4.

\subsection*{6.1 Definition and expansion of the metric on the connected sum}

We start by defining the connected sum between $Z$ and $M$. Let $\left\{x^{i}\right\}$ denote normal (flat) coordinates for $g_{Z}$ at $q \in Z$, defined for $|x|<\delta$. With a slight abuse of notation, let us also denote by $\left\{x^{i}\right\}$ the inverted normal coordinates for $g_{a}$ defined at the beginning of Section 5, which are defined for $|x|>a / \varepsilon$. As in the previous section, let us consider $\gamma>0$ satisfying $0<a \ll \gamma \ll \varepsilon, \delta \ll 1$. We now glue $M$ and $Z$ along the annular regions $\{x|\gamma / 2<|x|<2 \gamma\}$ (of both $M$ and $Z$, given by their respective coordinates) via the identification map $x \rightarrow x$. We denote by $X$ the resulting smooth manifold.
Remark 6.1. By construction, $X$ is diffeomorphic to $Z \# \bar{M}$, where $\bar{M}$ denotes the manifold $M$ endowed with its opposite orientation. This is the same choice adopted in [MM25], see Remark 3.5, as well as in [GV16], see their Remark 9.1. This does not create any problem, since we can easily get a manifold diffeomorphic to $Z \# M$ by simply repeating the same procedure with $\bar{M}$ in place of $M$.

We now want to define a competitor metric $g_{X}$ on $X$. To begin, recall the expressions (4.1) for $g_{b}$ in normal (flat) coordinates at $q \in Z$ and (5.2) for $g_{a}$ in inverted conformal normal coordinates at $p \in M$. We would like to glue these metrics at $|x|=\gamma$, but in order to do so we first need to cut off some higher order error terms.

Since we got $A(0)=0, \nabla A(0)=0$ (see e.g. (3.21)), we can write
$$A_{i j}(x)=\frac{1}{2} \partial_{k l}^{2} A_{i j}(0) x^{k} x^{l}+\eta_{i j}(x), \quad \text { for }|x|<\delta,$$
where
$$\left|\nabla^{k} \eta_{i j}(x)\right| \leq C|x|^{3-k}, \quad \text { for }|x| \leq \delta, k=0, \ldots, 4 .$$
Let us define a smooth cutoff function $\chi_{\gamma}$ satisfying
$$\chi_{\gamma}(r)=\left\{\begin{array}{ll}
0 & \text { for } r \leq \frac{\gamma}{4} \\
1 & \text { for } r \geq \frac{3}{4} \gamma,
\end{array} \quad\left|\left(\chi_{\gamma}\right)^{(k)}\right| \leq C \gamma^{-k}, \quad k=0, \ldots, 4,\right.$$
where $C>0$ does not depend upon $\gamma$. We now define the modified metric $\tilde{g}_{a}$ on $M \backslash\{p\}$ by
$$\left(\tilde{g}_{a}\right)_{i j}(x):=\delta_{i j}+a^{2}\left(-\frac{1}{3} W_{k i j l} \frac{x^{k} x^{l}}{|x|^{4}}+\frac{1}{2} \partial_{k l}^{2} A_{i j}(0) x^{k} x^{l}\right)+\chi_{\gamma}(\gamma-|x|) \zeta_{i j}^{a}(x), \quad \text { for }|x|>\frac{a}{\varepsilon},$$
with $\tilde{g}_{a}=g_{a}$ elsewhere on $M \backslash\{p\}$. Similarly, we define the modified metric $\hat{g}_{b}$ on $Z$ by
$$\left(\hat{g}_{b}\right)_{i j}(x):=\delta_{i j}+b^{2}\left(-\frac{1}{3} W_{k i j l} \frac{x^{k} x^{l}}{|x|^{4}}+\frac{1}{2} \partial_{k l}^{2} A_{i j}(0) x^{k} x^{l}+\chi_{\gamma}(|x|-\gamma) \eta_{i j}(x)\right), \quad \text { for }|x|<\delta,$$
with $\hat{g}_{b}=g_{b}$ elsewhere on $Z$. We now take $a=b$ and define
$$g_{X}:= \begin{cases}g_{a} & \text { in } M \backslash\{x| | x \mid>2 a / \varepsilon\} \\ \tilde{g}_{a} & \text { in }\{x|2 a / \varepsilon<|x|<\gamma\} \\ \hat{g}_{b} & \text { in }\{x|\gamma \leq|x| \leq \delta / 2\} \\ g_{b} & \text { in } Z \backslash\{x| | x \mid \leq \delta / 2\} .\end{cases}$$
By definition, $g_{X}$ is a smooth metric on $X$.

Proposition 6.2. Let $g_{X}$ be defined as in (6.5), and assume that $0<a=b \ll \gamma \ll \varepsilon, \delta \ll 1$. Then the following expansion holds:
$$\mathcal{W}^{X}\left(g_{X}\right)-\mathcal{W}^{M}\left(g_{M}\right)=\frac{2}{3} a^{4} W^{k i j l} \partial_{k l}^{2} A_{i j}(0)+O\left(a^{4} \gamma\right)+o\left(a^{4}\right) .$$
Proof. By Corollary 4.5, Corollary 5.3 and the definition of $g_{X}$, we see that
$$\begin{aligned}
\mathcal{W}^{X}\left(g_{X}\right)-\mathcal{W}^{M}\left(g_{M}\right)= & \frac{2}{3} a^{4} W^{k i j l} \partial_{k l}^{2} A_{i j}(0)+O\left(a^{4} \gamma^{2}\right)+o\left(a^{4}\right) \\
& +\int_{B_{2 \gamma} \backslash B_{\gamma / 8}}\left|W^{g_{X}}\right|^{2} d V_{g_{X}}-\int_{B_{2 \gamma} \backslash B_{\gamma}}\left|W^{g_{b}}\right|^{2} d V_{g_{b}}-\int_{B_{\gamma} \backslash B_{\gamma / 8}}\left|W^{g_{a}}\right|^{2} d V_{g_{a}} .
\end{aligned}$$
The proposition then follows from the next lemma. \(\square\)

Lemma 6.3. Under the assumptions of Proposition 6.2 (in particular $b=a$ ), one has
$$\int_{B_{2 \gamma} \backslash B_{\gamma / 8}}\left|W^{g_{X}}\right|^{2} d V_{g_{X}}-\int_{B_{2 \gamma} \backslash B_{\gamma}}\left|W^{g_{b}}\right|^{2} d V_{g_{b}}-\int_{B_{\gamma} \backslash B_{\gamma / 8}}\left|W^{g_{a}}\right|^{2} d V_{g_{a}}=O\left(a^{4} \gamma\right) .$$
Proof. We deal separately with the integrals in $B_{2 \gamma} \backslash B_{\gamma}$ and those in $B_{\gamma} \backslash B_{\gamma / 8}$.
\begin{itemize}
\item[-] Consider
$$\int_{B_{2 \gamma} \backslash B_{\gamma}}\left|W^{g_{X}}\right|^{2} d V_{g_{X}}-\int_{B_{2 \gamma} \backslash B_{\gamma}}\left|W^{g_{b}}\right|^{2} d V_{g_{b}}=\int_{B_{2 \gamma} \backslash B_{\gamma}}\left|W^{\hat{g}_{b}}\right|^{2} d V_{\hat{g}_{b}}-\int_{B_{2 \gamma} \backslash B_{\gamma}}\left|W^{g_{b}}\right|^{2} d V_{g_{b}}$$
\end{itemize}
and let us write $g_{b}=g_{E}+b^{2} F$ and $\hat{g}_{b}=g_{E}+b^{2} \hat{F}$, where we recall that $\hat{g}_{b}$ is given by (6.4). Since $b=a \ll \gamma$, we can Taylor-expand the Weyl energies in $b$ at $g_{E}$ as in the beginning of Section 4. Recalling that $\dot{B}(F)=0$, expanding and integrating by parts we obtain
$$\begin{aligned}
\int_{B_{2 \gamma} \backslash B_{\gamma}}\left|W^{g_{b}}\right|^{2} d V_{g_{b}} & =-2 a^{4} \int_{B_{2 \gamma} \backslash B_{\gamma}} \dot{W}(F)_{\alpha i j \beta} \partial^{\alpha} \partial^{\beta} F^{i j} d x+O\left(a^{6}\right) \\
& =2 a^{4} \int_{\partial\left(B_{2 \gamma} \backslash B_{\gamma}\right)}\left(\partial^{\alpha} \dot{W}(F)_{\alpha i j \eta} F^{i j}-\dot{W}(F)_{\eta i j \beta} \partial^{\beta} F^{i j}\right) \nu^{\eta} d \sigma+O\left(a^{6}\right),
\end{aligned}$$
where this time $\nu$ is the exterior unit normal vector. Similarly,
$$\begin{aligned}
\int_{B_{2 \gamma} \backslash B_{\gamma}}\left|W^{\hat{g}_{b}}\right|^{2} d V_{\hat{g}_{b}}= & -2 a^{4} \int_{B_{2 \gamma} \backslash B_{\gamma}} \dot{B}_{i j}(\hat{F}) \hat{F}^{i j} d x \\
& +2 a^{4} \int_{\partial\left(B_{2 \gamma} \backslash B_{\gamma}\right)}\left(\partial^{\alpha} \dot{W}(\hat{F})_{\alpha i j \eta} \hat{F}^{i j}-\dot{W}(\hat{F})_{\eta i j \beta} \partial^{\beta} \hat{F}^{i j}\right) \nu^{\eta} d \sigma+O\left(a^{6}\right)
\end{aligned}$$
We now decompose
$$\hat{F}_{i j}(x)=F_{i j}(x)-\left(1-\chi_{\gamma}(|x|-\gamma)\right) \eta_{i j}(x)=: F_{i j}(x)+E_{i j}(x),$$
so that
$$\dot{B}_{i j}(\hat{F}) \hat{F}^{i j}=\dot{B}_{i j}(E) \hat{F}^{i j} .$$
Recalling that $\dot{B}$ is a linear fourth-order operator, from the definition of $E$ and $\hat{F}$ (that depend upon $\eta, \chi_{\gamma}$ defined in (6.1), (6.2)), we see that
$$\left|\hat{F}^{i j}(x)\right| \leq C|x|^{-2}, \quad\left|\dot{B}_{i j}(E)\right| \leq C \gamma^{-1}, \quad \text { for } \gamma \leq|x| \leq 2 \gamma .$$

As a consequence,
$$\left|\int_{B_{2 \gamma} \backslash B_{\gamma}} \dot{B}_{i j}(\hat{F}) \hat{F}^{i j} d x\right|=\left|\int_{B_{2 \gamma} \backslash B_{\gamma}} \dot{B}_{i j}(E) \hat{F}^{i j} d x\right| \leq C \gamma .$$
Next, we look at the boundary integrals in (6.7), (6.8). To begin, we notice that $F^{i j}=\hat{F}^{i j}$ near $\partial B_{2 \gamma}$, so the integrals in the outer boundary $\partial B_{2 \gamma}$ cancel out when taking the difference in (6.6). Thus it only remains to estimate the integrals on $\partial B_{\gamma}$.