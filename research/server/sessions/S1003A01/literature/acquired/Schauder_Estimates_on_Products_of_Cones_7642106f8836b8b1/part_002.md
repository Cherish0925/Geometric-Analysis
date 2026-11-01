---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: Schauder Estimates on Products of Cones]

Set $u_{1}=u_{0}-P_{1}$, so $\left\|u_{1}\right\|_{B(x, \lambda)}<\lambda^{2+\alpha}$. If $k=1$ is a good scale, then $B(x, \lambda)=$ $\lambda B\left(x_{1}, 1\right)$ with $\left|x_{1}\right|=\lambda^{-1}|x|<\epsilon_{0}$. Let $\tilde{u}_{1}: B\left(x_{1}, 1\right) \rightarrow \mathbf{R}$ be given by $\tilde{u}_{1}(\cdot)=$ $\lambda^{-2-\alpha} u_{1}(\lambda \cdot)$. We clearly have $\left\|\tilde{u}_{1}\right\|_{B\left(x_{1}, 1\right)}=\lambda^{-2-\alpha}\left\|u_{1}\right\|_{B(x, \lambda)}<1$. Note that $\Delta \tilde{u}_{1}=\lambda^{-\alpha} f(\lambda \cdot)$, so $\left\|\Delta \tilde{u}_{1}\right\|_{B\left(x_{1}, 1\right)}=\lambda^{-\alpha}\|f\|_{B(x, \lambda)}<\delta$. We are again in the setting of Proposition 5.1, so there is $\tilde{P}_{2} \in \mathcal{H}_{\leq 2}$-with $\left\|\tilde{P}_{2}\right\|_{B\left(x_{1}, 1\right)} \leq C$ - such that $\left\|\tilde{u}_{1}-\tilde{P}_{2}\right\|_{B\left(x_{1}, \lambda\right)}<\lambda^{2+\alpha}$. Set
$$\begin{aligned}
u_{2} & =\lambda^{2+\alpha}\left(\tilde{u}_{1}-\tilde{P}_{2}\right)\left(\lambda^{-1} \cdot\right) \\
& =u_{1}-P_{2},
\end{aligned}$$
with $P_{2}=\lambda^{2+\alpha} \tilde{P}_{2}\left(\lambda^{-1} \cdot\right)$. Clearly, $\lambda^{-1} B\left(x, \lambda^{2}\right)=B\left(x_{1}, \lambda\right)$, and we check that
$$\begin{aligned}
\left\|u_{2}\right\|_{B\left(x, \lambda^{2}\right)} & =\lambda^{2+\alpha}\left\|\tilde{u}_{1}-\tilde{P}_{2}\right\|_{B\left(x_{1}, \lambda\right)} \\
& <\lambda^{2(2+\alpha)} .
\end{aligned}$$
We proceed the same way. We obtain $P_{1}, \ldots, P_{k} \in \mathcal{H}_{\leq 2}$ such that $u_{k}=u-\left(P_{1}+\right.$ $\left.\ldots+P_{k}\right)$ satisfies $\left\|u_{k}\right\|_{B\left(x, \lambda^{k}\right)}<\lambda^{(2+\alpha) k}$ for $k=0, \ldots, a_{1}$.

Now, for $k \in I_{1}=\left[a_{1}, b_{1}\right)$ we have bad scales, and we set $P_{k}=0$, that is $u_{k+1}=$ $u k$. Clearly, $\left\|u_{k+1}\right\|_{B\left(x, \lambda^{k+1}\right)} \leq \lambda^{-m / 2}\left\|u_{k}\right\|_{B\left(x, \lambda^{k}\right)}$ whenever $u_{k+1}=u_{k}$. If we let $Q_{1}=\left(\lambda^{-m / 2} \lambda^{-(2+\alpha)}\right)^{\left|I_{1}\right|}$, we can then guarantee that $\left\|u_{k}\right\|_{B\left(x, \lambda^{k}\right)} \leq Q_{1} \lambda^{(2+\alpha) k}$ for all $k=0, \ldots, b_{1}$.

Consider now $k=b_{1}$, by the previous step, we have $\left\|u_{k}\right\|_{B\left(x, \lambda^{k}\right)}<Q_{1} \lambda^{(2+\alpha) k}$. Let
$$\tilde{u}_{k}=Q_{1}^{-1} \lambda^{-(2+\alpha) k} u_{k}\left(\lambda^{k} \cdot\right),$$
so $\|\tilde{u}\|_{B\left(x_{k}, 1\right)}=Q^{-1} \lambda^{-(2+\alpha) k}\left\|u_{k}\right\|_{B\left(x, \lambda^{k}\right)}<1$; and $\Delta \tilde{u}_{k}=Q_{1}^{-1} \lambda^{-\alpha k} f\left(\lambda^{k} \cdot\right)$, so $\left\|\Delta \tilde{u}_{k}\right\|_{B\left(x_{k}, 1\right)}<Q_{1}^{-1} \delta<\delta$. Since $k=b_{1}$ is a good scale, we can identify -after doing a cut and translating- $B\left(x_{k}, 1\right) \subset C\left(Y_{1}\right)$ with $\left|x_{k}\right|<\epsilon_{0}$. By Proposition 5.1 we have $\tilde{P}_{k+1} \in \mathcal{H}_{\leq 2}\left(C\left(Y_{1}\right)\right)$ such that $\left\|\tilde{u}_{k}-\tilde{P}_{k+1}\right\|_{B\left(x_{k}, \lambda\right)}<\lambda^{2+\alpha}$. Set
$$\begin{aligned}
u_{k+1} & =Q_{1} \lambda^{(2+\alpha) k}\left(\tilde{u}_{k}-\tilde{P}_{k+1}\right)\left(\lambda^{k} \cdot\right) \\
& =u_{k}-P_{k+1},
\end{aligned}$$
with $P_{k+1}=Q_{1} \lambda^{(2+\alpha) k} \tilde{P}_{k+1}\left(\lambda^{-k}\right)$. We check that
$$\begin{aligned}
\left\|u_{k+1}\right\|_{B\left(x, \lambda^{k+1}\right)} & =Q_{1} \lambda^{(2+\alpha) k}\left\|\tilde{u}-\tilde{P}_{k+1}\right\|_{B\left(x_{k}, \lambda\right)} \\
& <Q_{1} \lambda^{(2+\alpha)(k+1)} .
\end{aligned}$$
We proceed the same in the good range of scales $k=b_{1}, \ldots, a_{2}-1$. We have constructed $u_{k}=u-\left(P_{1}+\ldots+P_{k}\right)$ that satisfy $\left\|u_{k}\right\|_{B\left(x, \lambda^{k}\right)}<Q_{1} \lambda^{(2+\alpha) k}$ for $k=0, \ldots, a_{2}$.

When $k=a_{2}$, we hit again a range of bad scales $I_{2}=\left[a_{2}, b_{2}\right)$. Same as before, for $k=a_{2}, \ldots, b_{2}-1$, we set $u_{k+1}=u_{k}$. We let $Q_{2}=\left(\lambda^{-m / 2} \lambda^{-(2+\alpha)}\right)^{\left|I_{2}\right|}$, so $\left\|u_{k}\right\|_{B\left(x, \lambda^{k}\right)}<Q_{1} Q_{2} \lambda^{(2+\alpha) k}$ for $k=0, \ldots, b_{2}$. For the good range $k=b_{2}, \ldots, a_{3}-1$ we set
$$\tilde{u}_{k}=Q_{1}^{-1} Q_{2}^{-1} \lambda^{-(2+\alpha) k} u_{k}\left(\lambda^{k} \cdot\right) .$$
We use Proposition 5.1 to obtain $\tilde{P}_{k+1} \in \mathcal{H}_{\leq 2}\left(C\left(Y_{2}\right)\right)$ such that, if we set $P_{k+1}=$ $Q_{1} Q_{2} \lambda^{(2+\alpha) k} \tilde{P}_{k+1}\left(\lambda^{-k}\right)$ and $u_{k+1}=u_{k}-P_{k+1}$, then $\left\|u_{k}\right\|_{B\left(x, \lambda^{k}\right)}<Q_{1} Q_{2} \lambda^{(2+\alpha) k}$ for all $k=0, \ldots, a_{3}$. We proceed the same way, after $I_{n}$ there are no more bad scales, so all $k \geq b_{n}$ are good. As a result, we get a sequence $u_{k}=u-\left(P_{1}+\ldots+P_{k}\right)$ with
$$\left\|u_{k}\right\|_{B\left(x, \lambda^{k}\right)} \leq C \lambda^{(2+\alpha) k}$$
for all $k=0,1, \ldots, \infty$. Here, $C=\left(\lambda^{-m / 2} \lambda^{-(2+\alpha)}\right)^{N}$ with $\sum_{a}\left|I_{a}\right| \leq N=N\left(\epsilon_{0}, \lambda\right)$ given by Lemma 4.1.

Let $\tau_{k}=D P_{k}(x)$. Because $D$ is homogeneous of degree two, we have $D \tilde{P}\left(\lambda^{-k} \cdot\right)=$ $\lambda^{-2 k}\left(D \tilde{P}_{k}\right)\left(\lambda^{-k} \cdot\right)$. Up to a constant factor, $P_{k}$ is equal to $\lambda^{(2+\alpha) k} \tilde{P}_{k}\left(\lambda^{-k}\right)$. Therefore, $\tau_{k}=\lambda^{k \alpha} D \tilde{P}_{k}\left(x_{k}\right)$. One detail is that we have uniform bounds $\left|D^{\prime} \tilde{P}_{k}\right|\left(x_{k}\right) \leq C$ for all second order derivatives $D^{\prime}$ of the corresponding model cone, after the cut and translation identification is done. The model cones are less singular than the original, and we get estimates on more derivatives; in particular we can express $D$ as a combination of operators $D^{\prime}$ with uniformly bounded (smooth) coefficients. The Euclidean directions in $D$ will remain unchanged, but the cone directions might change into Euclidean. We are performing the cuts uniformly away from the tips of the cones. The basic fact we need is that the vector fields $\partial_{r}$ and $r^{-1} \partial_{\theta}$ on $\mathbf{R}^{2} \backslash\{0\}$ can be written as a combination of the Cartesian vector fields $\partial_{s_{1}}, \partial_{s_{2}}$ with uniformly bounded (smooth) coefficients on discs of radius 1 which are at distance $\geq 2$, say, from the origin. The outcome is that
$$\left|\tau_{k}\right| \leq C \lambda^{k \alpha},$$
so the series $\sum_{k} \tau_{k}$ converges and we set $\tau=\sum_{k=0}^{\infty} \tau_{k}$.
By Lemma 2.7 in order to prove the estimate (1.2), it is enough to show that
$$\left\|D u-\left(\tau_{1}+\ldots+\tau_{k}\right)\right\|_{B\left(x, \lambda^{k}\right)} \leq C \lambda^{k \alpha} .$$
The scaled version of Proposition 2.5 gives us
$$\begin{aligned}
\left\|D u_{k}\right\|_{B\left(x, \lambda^{k}\right)} & \leq C\left(\|f\|_{B_{k-1}}+\lambda^{-2 k}\left\|u_{k}\right\|_{B_{k-1}}\right) \\
& \leq C \lambda^{k \alpha} .
\end{aligned}$$

We rewrite $D u_{k}$ as follows
$$\begin{aligned}
D u_{k} & =D u-\left(D P_{1}+\ldots+D P_{k}\right) \\
& =D u-\left(\tau_{1}+\ldots+\tau_{k}\right)-\left(D P_{1}-D P_{1}(x)+\ldots+D P_{k}-D P_{k}(x)\right) .
\end{aligned}$$

Recall that $D^{\prime} \tilde{P}_{j}=$ constant for all second derivatives $D^{\prime} \in \mathcal{D}_{2}$ of the corresponding model cone. We use again that $D$ can be expressed as a combination of derivatives $D^{\prime}$ with uniform control on the Hölder norm of the coefficients. More precisely, the only case in which $D P_{j}$ is not constant is when $D$ contains a conical derivative, say $\partial_{r_{a}}$, and $r_{a}(x) \neq 0$. Then for all $j \geq j_{0}$, such that $\lambda^{-j_{0}} r_{a}(x)>c_{\beta}$ we introduce a cut in the $C\left(S_{2 \pi \beta_{a}}^{1}\right)$ factor. The coefficients of $\partial_{r}$ with respect to the Cartesian coordinate vector fields, in a disc of radius 1 which is at distance $R$ from the origin, are constant up to an $O(1 / R)$ error. We conclude that the Hölder semi-norm of the coefficients of $D$ in terms of $D^{\prime}$-and hence the Hölder semi-norm of $D \tilde{P}_{j}$ - is bounded by a uniform constant multiple of $\lambda^{j} r_{a}(x)$. Therefore,
$$\begin{aligned}
\sum_{j=1}^{k}\left\|D P_{j}-D P_{j}(x)\right\|_{B\left(x, \lambda^{k}\right)} & =\sum_{j} \lambda^{\alpha j}\left\|D \tilde{P}_{j}-D \tilde{P}_{j}\left(x_{j}\right)\right\|_{B\left(x_{j}, \lambda^{k-j}\right)} \\
& \leq C \lambda^{\alpha k} \sum_{j=j_{0}}^{\infty} \lambda^{j} r_{a}(x)^{-1} .
\end{aligned}$$
Now, $\sum_{j=j_{0}}^{\infty} \lambda^{j} r_{a}(x)^{-1}=\lambda^{j_{0}} r_{a}(x)^{-1} \sum_{j=0}^{\infty} \lambda^{j}$ and $\lambda^{j_{0}} r_{a}(x)^{-1}<1 / c_{\beta}$. So,
$$\sum_{j=1}^{k}\left\|D P_{j}-D P_{j}(x)\right\|_{B\left(x, \lambda^{k}\right)} \leq C \lambda^{k \alpha} .$$

The main estimate (5.1) follows from equations (5.2), (5.3) and (5.4).
Remark 5.2 (Vanishing of conical derivatives at the singular locus). Note that if $x$ lies on the singular set, say $r_{a}(x)=0$, and if $D$ is a mixed Euclidean-conical or conical-conical derivative that contains either $\partial_{r_{a}}$ or $r_{a}^{-1} \partial_{\theta_{a}}$; then $D P=0$ for all $P \in \mathcal{H}_{\leq 2}$ involved in the proof. This means that $\tau_{k}=0$ for all $k$, so $\tau=0$ and $D u(x)=0$.

Remark 5.3 (Lower order estimates). The same method of proof of Theorem 1.1, but subtracting the sub-linear harmonic parts, leads to first order estimates. Indeed, even weaker assumptions on the regularity of $f$, lead to a $C^{\alpha}$-bound of the gradient components:
$$\frac{\partial u}{\partial r_{a}}, \quad \frac{1}{r_{a}} \frac{\partial u}{\partial \theta_{a}}, \quad \frac{\partial u}{\partial s_{i}} .$$
Again, the sublinear harmonic functions only depend on the Euclidean variables, so the normal component of $\nabla u$ along $\left\{r_{a}=0\right\}$ must vanish.

The vanishing condition admits the following geometric explanation. The holonomy of $g$ along a loop that goes around $\left\{r_{a}=0\right\}$ is non-trivial on the $C\left(S_{2 \pi \beta_{a}}^{1}\right)$ factor. Take small loops around $\left\{r_{a}=0\right\}$ that shrink to a point and parallel transport $\nabla u$. If $|\nabla u|$ and $\left|\partial_{\theta_{a}} \nabla u\right|$ are uniformly bounded, then the gradient must become
invariant under parallel transport as the loops shrink. The only way this can happen is if the $C\left(S_{2 \pi \beta_{a}}^{1}\right)$-component of $\nabla u$ vanishes.
5.1. Kähler metrics. Assume $m$ is even. Introducing complex coordinates $z_{a}=$ $\left(1 / \beta_{a}\right) r_{a} e^{i \theta_{a}}$ on each cone factor, identifies $\mathbf{R}_{(\beta)}^{m}$ with $\mathbf{C}^{m / 2}$ endowed with the singular Kähler metric
$$\omega_{(\beta)}=\sum_{a}\left|z_{a}\right|^{2 \beta_{a}-2} i d z_{a} d \bar{z}_{a}+\omega_{\mathbf{C}^{m / 2-n}}$$
Theorem 1.1 provides a bound for $|\partial \bar{\partial} u|_{\alpha}$, in the sense that the components of $\partial \bar{\partial} u$ with respect to an $\omega_{(\beta)}$-orthonormal co-frame of (1, 1)-forms are $C^{\alpha}$. Given a $C^{\alpha}$ closed (1, 1)-form $\eta$ such that $\omega:=\omega_{(\beta)}+\eta>0$; it is possible to extend Theorem 1.1 to $\Delta_{\omega}$. This is done, by means of the freezing coefficients method, in GS18, Section 3.5]; see also [Don12, Section 4.2] and [Bre13, Section 2].

\section*{Appendix A. The two dimensional cone}
A.1. Geometry of balls. We recall here some basic facts on the geometry of the two-dimensional cone $C\left(S_{2 \pi \beta}^{1}\right)$. In polar coordinates on $\mathbf{R}^{2}$, the metric is
$$g=d r^{2}+\beta^{2} r^{2} d \theta^{2}$$
and $r$ measures the intrinsic distance to the apex, located at 0.
If we cut $C\left(S_{2 \pi \beta}^{1}\right)$ along a geodesic ray starting from the vertex, say $\theta=$ constant, we get a wedge in the Euclidean plane of angle $2 \pi \beta$. Given a point $p \in C\left(S_{2 \pi \beta}^{1}\right) \backslash\{o\}$, we can always cut along the 'opposite ray' to $p$. More precisely, $p$ lies on a circle of length $2 \pi \beta r$ given by the points which are at distance $r=r(p)$ from the vertex. On that circle, there is a unique antipodal point $q$ which is at maximal distance $\pi \beta r$ from $p$. We cut along the ray starting from $o$ and going through $q$, so then $p$ will lie on the 'middle of the wedge', which means equidistant from the two sides of the wedge. In coordinates, this means that we choose $\theta \in(-\pi, \pi)$ with $\theta(p)=0$ and we set $\tilde{\theta}=\beta \theta$ to get the Euclidean wedge $-\pi \beta<\tilde{\theta}<\pi \beta$.

We look at geodesic balls $B(p, \rho) \subset C\left(S_{2 \pi \beta}^{1}\right)$. The situation is pretty clear when $p$ is the vertex. All balls centered at $o$ are isometric after rescaling to unit size, that is $\rho^{-1} B(o, \rho)=B(o, 1)$. We consider $p \in C\left(S_{2 \pi \beta}^{1}\right) \backslash\{o\}$. It is clear that $\rho^{-1} B(p, \rho)$ will be isometric to the Euclidean unit disc if $\rho$ is small; and for large values of $\rho$ it will be isometric to a unit ball in $C\left(S_{2 \pi \beta}^{1}\right)$ with its center very close to the origin. We can quantify this transition as follows. First, it is enough to consider unit balls $B(\tilde{p}, 1) \subset C\left(S_{2 \pi \beta}^{1}\right)$ because $\rho^{-1} B(p, \rho)=B\left(\rho^{-1} p, 1\right)$ where $\rho^{-1}(r, \theta)=\left(\rho^{-1} r, \theta\right)$. Taking a cut, it is clear from Figure 2 that $B(\tilde{p}, 1)$ is isometric to the Euclidean unit disc if $d(\tilde{p}, o)>c_{\beta}$, where
$$c_{\beta}=\left\{\begin{array}{l}
\sin (\pi \beta) \text { if } 0<\beta \leq 1 / 2 \\
1 \text { if } \beta>1 / 2 .
\end{array}\right.$$

Given $\epsilon>0$, we say that $B(\tilde{p}, 1)$ is $\epsilon$-close to $B(o, 1)$, if $d(\tilde{p}, o)<\epsilon$. The conclusion is that, if we let $p \in C\left(S_{2 \pi \beta}^{1}\right) \backslash\{o\}$ and $r=r(p)$, then
$$\rho^{-1} B(p, \rho)=\left\{\begin{array}{l}
B_{1}^{E} \subset \mathbf{R}^{2} \text { if } \rho<c_{\beta} r \\
B(\tilde{p}, 1) \text { with } d(\tilde{p}, o)<\epsilon \text { if } \rho>\epsilon^{-1} r
\end{array}\right.$$

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/18a0a9d0-28f6-4b2a-a175-3c41e80c3b49-25.jpg?height=334&width=1280&top_left_y=417&top_left_x=453}
\captionsetup{labelformat=empty}
\caption{Figure 2. Difference between $\beta<1 / 2$, on the left, against $\beta>$ $1 / 2$, on the right. The dotted line on the left is a geodesic loop, its homotopy class in $B(p, \rho)$ is non trivial for $c_{\beta} r<\rho<r$.}
\end{figure}
We take logarithms, that is we introduce a scale parameter $s$ and write $\rho=e^{s}$. We say that a scale $s$ is good if $\rho^{-1} B(p, \rho)$ is isometric either to the Euclidean unit disc $B_{1}^{E}$ or to $B(\tilde{p}, \epsilon)$ with $d\left(\tilde{p^{\prime}, o}\right)<\epsilon$. By the above discussion, if either $s<\log c_{\beta}+\log r$ or $s>\log \left(\epsilon^{-1}\right)+\log r$ then $s$ is a good scale. In other words, the set of bad scales has size uniformly bounded above, independently of $p$, by $\log \left(\epsilon^{-1}\right)+\log \left(c_{\beta}^{-1}\right)$. The point is that, while we do not have uniform control over $p$ of which scales are good or bad, we do have a uniform bound on the set of bad scales.

Note that if $0<\beta<1 / 2$ and $c_{\beta} r<\rho<r$, then $B(p, \rho)$ is homeomorphic to an annulus. If $\epsilon<c_{\beta}$ then these values of $\rho$, for which $B(p, \rho)$ is homeomorphic to an annulus, are comprised among the bad scales.
A.2. Bounded harmonic functions. In polar coordinates, the Laplacian on the cone $C\left(S_{2 \pi \beta}^{1}\right)$ is given by
$$\Delta=\frac{\partial^{2}}{\partial r^{2}}+\frac{1}{r} \frac{\partial}{\partial r}+\frac{1}{\beta^{2} r^{2}} \frac{\partial^{2}}{\partial \theta^{2}} .$$
If we change to Cartesian coordinates $u=r \cos \theta, v=r \sin \theta$, then
$$g=\left(\cos ^{2} \theta+\beta^{2} \sin ^{2} \theta\right) d u^{2}+\left(1-\beta^{2}\right) \sin \theta \cos \theta(d u d v+d v d u)+\left(\beta^{2} \cos ^{2} \theta+\sin ^{2} \theta\right) d v^{2} .$$
The metric coefficients $g_{i j}$ are uniformly bounded but are not continuous at 0. By the much more general De Giorgi-Nash-Moser theory, we know that weak harmonic functions are automatically Hölder continuous. This is a non-trivial statement, functions in $W^{1,2}$ can be unbounded, the prototypical example is $\log |\log r|$ in a neighborhood of the origin of $\mathbf{R}^{2}$. We provide a self-contained proof of the Hölder continuity in the two-dimensional case.

Lemma A.1. Let $u \in W^{1,2}\left(B_{1}\right)$ satisfy $\Delta u=0$, then $u$ is Hölder continuous.
Proof. The following applies, more generally, to the singular metrics $\mathbf{R}_{(\beta)}^{m}$ considered in this article. We use the test function $\psi=\eta^{2} u$ as in Lemma 2.3, with $\eta=1$ on $B_{1 / 2}$ and $\operatorname{supp}(\eta) \subset B_{1}$. We get
$$\int_{B_{1}} \eta^{2}|\nabla u|^{2} \leq 4 \int_{B_{1}}|\nabla \eta|^{2} u^{2} .$$

Let $A=B_{1} \backslash B_{1 / 2}$ and let $u_{A}$ be the average of $u$ over $A$. Replacing $u$ by $u-u_{A}$ and using the Poincaré inequality, we have
$$\begin{aligned}
\int_{B_{1 / 2}}|\nabla u|^{2} & \leq C \int_{A}\left(u-u_{A}\right)^{2} \\
& \leq C \int_{A}|\nabla u|^{2} \\
& =C\left(\int_{B_{1}}|\nabla u|^{2}-\int_{B_{1 / 2}}|\nabla u|^{2}\right) .
\end{aligned}$$
We get that
$$\int_{B_{1 / 2}}|\nabla u|^{2} \leq \frac{C}{C+1} \int_{B_{1}}|\nabla u|^{2}$$
and we can iterate to obtain
$$\int_{B_{2}-k}|\nabla u|^{2} \leq\left(\frac{C}{C+1}\right)^{k} \int_{B_{1}}|\nabla u|^{2} .$$
Equivalently, $\int_{B_{r}}|\nabla u|^{2}=O\left(r^{\mu}\right)$ as $r \rightarrow 0$. Here, $\mu>0$ is given by $2^{-\mu}=(C+$ $1)^{-1} C$. We can use Poincaré again, $\int_{B_{r}}\left(u-u_{B_{r}}\right)^{2} \leq C r^{2} \int_{B_{r}}|\nabla u|^{2}$, therefore
$$\left\|u-u_{B_{r}}\right\|_{B_{r}} \leq C r^{(2+\mu-m) / 2} .$$
In particular, this shows that if $m=2$ then $u$ is Hölder continuous. \(\square\)

The eigenfunctions of the Laplace operator $\beta^{-2} \partial_{\theta}^{2}$ of $S_{2 \pi \beta}^{1}$ are $\cos (k \theta), \sin (k \theta)$, with eigenvalues $k^{2} \beta^{2}$ for $k \geq 0$. The corresponding homogeneous harmonic functions are
$$r^{k / \beta} \cos (k \theta), \quad r^{k / \beta} \sin (k \theta) .$$
Every harmonic function $u$ on $B_{1}$ admits an expansion
$$u=\sum_{k}\left(a_{k} r^{k / \beta} \cos (k \theta)+b_{k} r^{k / \beta} \sin (k \theta)\right) .$$

We introduce a complex variable, $z=(1 / \beta) r^{1 / \beta} e^{i \theta}$; note that the change of coordinates is singular at the origin. In this complex coordinate, we have
$$d r^{2}+\beta^{2} r^{2} d \theta^{2}=|z|^{2 \beta-2}|d z|^{2} .$$
and $4 \Delta=|z|^{2-2 \beta} \partial^{2} / \partial z \partial \bar{z}$. Since the weak harmonic function $u$ is continuous, by the standard removability of singularities, $u$ is a smooth harmonic function of the complex variable $z$ and the expansion (A.1) is the usual Taylor series.

\section*{References}
[ACM14] Kazuo Akutagawa, Gilles Carron, and Rafe Mazzeo, The Yamabe problem on stratified spaces, Geom. Funct. Anal. 24 (2014), no. 4, 1039-1079.
[ACM15] -, Hölder regularity of solutions for Schrödinger operators on stratified spaces, J. Funct. Anal. 269 (2015), no. 3, 815-840.
[BKMR18] Jérôme Bertrand, C Ketterer, Ilaria Mondello, and T Richard, Stratified spaces and synthetic Ricci curvature bounds, arXiv:1804.08870 (2018).
[Bre13] Simon Brendle, Ricci flat Kähler metrics with edge singularities, Int. Math. Res. Not. IMRN (2013), no. 24, 5727-5766.
[CDS15a] X.X. Chen, S. Donaldson, and S. Sun, Kähler-Einstein metrics on Fano manifolds, I: Approximation of metrics with cone singularities, J. Amer. Math. Soc. 28 (2015), no. 1, 183-197.
[CDS15b] \_\_\_\_, Kähler-Einstein metrics on Fano manifolds, II: Limits with cone andgle less than $2 \pi$, J. Amer. Math. Soc. 28 (2015), no. 1, 199-234.
[CDS15c] \_\_\_\_, Kähler-Einstein metrics on Fano manifolds, III: Limits as cone angle approaches $2 \pi$ and completion of the main proof, J. Amer. Math. Soc. 28 (2015), no. 1, 235-278.
[Din02] Yu Ding, Heat kernels and Green's functions on limit spaces, Comm. Anal. Geom. 10 (2002), no. 3, 475-514.
[Don12] Simon K. Donaldson, Kähler metrics with cone singularities along a divisor, Essays in mathematics and its applications, Springer, Heidelberg, 2012, pp. 49-79.
[GS16] Bin Guo and Jian Song, Schauder estimates for equations with cone metrics, I, arXiv: 1612.00075 (2016).
[GS18] \_\_\_\_, Schauder estimates for equations with cone metrics, II, arXiv: 1809.03116 (2018).
[GY18] Yaoting Gui and Hao Yin, Schauder estimates on smooth and singular spaces, arXiv: 1803.05081 (2018).
[HL11] Qing Han and Fanghua Lin, Elliptic partial differential equations, Second ed., Courant Lecture Notes in Mathematics, vol. 1, 2011.
[Mon17] Ilaria Mondello, The local Yamabe constant of Einstein stratified spaces, Ann. Inst. H. Poincaré Anal. Non Linéaire 34 (2017), no. 1, 249-275.
[Wan06] Xu-Jia Wang, Schauder estimates for elliptic and parabolic equations, Chinese Ann. Math. Ser. B 27 (2006), no. 6, 637-642.

LMJL, Université de Nantes
E-mail address: martin.deborbon@univ-nantes.fr
University of Notre Dame
E-mail address: gedward2@nd.edu