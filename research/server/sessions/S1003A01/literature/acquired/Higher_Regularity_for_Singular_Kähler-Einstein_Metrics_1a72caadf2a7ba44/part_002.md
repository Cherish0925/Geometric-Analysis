---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: Higher Regularity for Singular Kähler-Einstein Metrics]

Since $\omega_{C(Y)}$ is a cone metric, it admits the Kähler potential $\psi=\frac{1}{2} d_{C(Y)}(o, \cdot)^{2}$. At the same time, using [29, Proposition 3.1], we can find Kähler potentials $\phi_{i}$ for $\omega_{i}$ on $F_{i}\left(B_{i}\right)$, such that
$$\left|\phi_{i}-\frac{1}{2} d_{\omega_{i}}(o, \cdot)^{2}\right|<\Psi\left(i^{-1}\right) .$$
Using the estimate for the distance functions in Condition (2) we find that $\omega_{i}=$ $\omega_{C(Y)}+\sqrt{-1} \partial \bar{\partial} u_{i}$, where
$$\left|u_{i}\right|=\left|\phi_{i}-\psi\right|=\frac{1}{2}\left|d_{\omega_{i}}(o, \cdot)^{2}-d_{\omega_{C(Y)}}(o, \cdot)^{2}\right|<\Psi\left(i^{-1}\right) .$$
Since $\omega_{i}$ satisfies $\operatorname{Ric}\left(\omega_{i}\right)=c_{i} \omega_{i}$ and $\operatorname{Ric}\left(\omega_{C(Y)}\right)=0$, we have $\omega_{i}^{n}=e^{f_{i}} \omega_{C(Y)}^{n}$ for some $f_{i}$ satisfying $c_{i} \omega_{i}=-\sqrt{-1} \partial \bar{\partial} f_{i}$ on the regular part of $B$, i.e.
$$\sqrt{-1} \partial \bar{\partial}\left(f_{i}+c_{i} \phi_{i}\right)=0 .$$
By Grauert-Remmert [21] the pluriharmonic function $f_{i}+c_{i} \phi_{i}$ extends to a pluriharmonic function across the (codimension 2) singular set of $B$. By Colding's volume convergence theorem [11] we have
$$\int_{B} \omega_{i}^{n}=\int_{B} \omega_{C(Y)}^{n}+\Psi\left(i^{-1}\right),$$
and so since $c_{i} \rightarrow 0$ as $i \rightarrow \infty$ while $\phi_{i}$ is uniformly bounded, we have
$$\int_{B} e^{f_{i}+c_{i} \phi_{i}} \omega_{C(Y)}^{n}=\int_{B} \omega_{C(Y)}^{n}+\Psi\left(i^{-1}\right) .$$
In particular we have a uniform bound for the $L^{1}$ norm of the plurisubharmonic function $e^{f_{i}+c_{i} \phi_{i}}$ on $B$, with respect to $\omega_{C(Y)}^{n}$, and so by the mean value inequality on a slightly smaller ball we have a uniform upper bound $e^{f_{i}+c_{i} \phi_{i}}<1+\Psi\left(i^{-1}\right)$, or in other words $f_{i}+c_{i} \phi_{i}<\Psi\left(i^{-1}\right)$. Similarly, we have a uniform upper bound for the integral of $e^{-f_{i}-c_{i} \phi_{i}}$ with respect to $\omega_{i}^{n}$, and so we have $-f_{i}-c_{i} \phi_{i}<\Psi\left(i^{-1}\right)$ on a slightly smaller ball. This implies that $\left|f_{i}+c_{i} \phi_{i}\right|<\Psi\left(i^{-1}\right)$, and since $c_{i} \rightarrow 0$, we obtain $\left|f_{i}\right|<\Psi\left(i^{-1}\right)$. We can arrange that $f_{i}(0)=0$ by composing the $F_{i}$ by an element of $G L(N)$ close to the identity, inducing a homothetic scaling on the cone $C(Y)$. Finally, using the equation $n c_{i}=-\Delta_{\omega_{i}} f_{i}$ together with the gradient estimate for harmonic functions implies $\left|\nabla f_{i}\right|_{\omega_{i}}<\Psi\left(i^{-1}\right)$ as required in condition (3). \(\square\)

We are now ready to prove Theorem 1.1.
Proof of Theorem 1.1. By Proposition 4.2, $\omega_{Z}$ can be approximated by $\mathcal{F}$. We can set $\Lambda=1$ in Definition 3.6 because the model metric $\omega_{0}$ is a cone metric. Applying Proposition 3.7, we see that there exist a model metric $\omega_{h} \in \mathcal{F}, r_{0}>0$, and a holomorphic map $F: B_{\omega_{h}}\left(0, r_{0}\right) \rightarrow Z$ with $F(0)=p$ and constants $C, \alpha>0$, such that
$$F^{*} \omega_{Z}=\omega_{h}+\sqrt{-1} \partial \bar{\partial} u_{r}$$
for some $u_{r}$ defined on $B(0, r)$ and
$$\sup _{B_{\omega_{h}}(0, r)}\left|u_{r}\right| \leq C r^{2+\alpha}$$
for all $r<r_{0}$. By construction (see Lemma 4.1), $\omega_{h}=g^{*} \omega_{C(Y)}$. Thus (4.6) becomes
$$\left(F \circ g^{-1}\right)^{*} \omega_{Z}=\omega_{C(Y)}+\sqrt{-1} \partial \bar{\partial}\left(u_{r} \circ g^{-1}\right) .$$
Since $B(0, r / 2) \subset B_{\omega_{h}}(0, r)$, we have
$$\sup _{B(0, r / 2)}\left|u_{r} \circ g^{-1}\right| \leq C r^{2+\alpha} .$$
This completes the proof. \(\square\)

In the case of tangent cones with isolated singularities we have the following corollary, generalizing Hein-Sun [24, Theorem 1.4].

Corollary 4.3. Suppose that in the setting of Theorem 1.1 the tangent cone $C(Y)$ has an isolated singularity at the origin. Then the metric $\phi^{*} \omega_{Z}$ satisfies
$$\sup _{B(o, r) \backslash B(o, r / 2)}\left|\nabla_{\omega_{C(Y)}}^{j}\left(\phi^{*} \omega_{Z}-\omega_{C(Y)}\right)\right|_{\omega_{C(Y)}} \leq C_{j} r^{\alpha-j},$$
for all $r<r_{0}$, constants $C_{j}$, and the $\alpha$ from Theorem 1.1.
Proof. This follows from rescaling the estimate (4.7) by a factor of $r^{-1}$, and then applying Lemma 3.3. \(\square\)

\section*{5. The unstable case}

In this section we prove Theorem 1.2. Suppose that $Z$ is the Gromov-Hausdorff limit of a non-collapsing sequence of polarized Kähler-Einstein manifold. Let $p \in Z$, and suppose $C(Y)$ is the tangent cone at $p$. Unlike the previous section, we deal with an example for which the germ $(Z, p)$ is not isomorphic to the germ $(C(Y), o)$, where $o$ is the vertex of the cone. Assume that
$$C(Y)=\mathbf{C} \times\left\{f(x)=x_{1}^{2}+x_{2}^{2}+\cdots+x_{n}^{2}=0\right\} \subset \mathbf{C}^{n+1} .$$
This is equipped with the Calabi-Yau cone metric
$$\omega_{C(Y)}=\frac{1}{2} \sqrt{-1} \partial \bar{\partial}\left(|z|^{2}+r^{2}\right),$$
where $r^{2}=|x|^{2 \frac{n-2}{n-1}}$ is the distance squared of the Stenzel metric 32. Recall that the homothetic action on the coordinates $x_{i}$ has weights $w_{i}=\frac{n-1}{n-2}$, and $f$ is homogeneous with degree $d=2 \frac{n-1}{n-2}$. We assume that the germ $(Z, p)$ is isomorphic to the isolated singularity
$$X=\left\{z^{p}+x_{1}^{2}+\cdots+x_{n}^{2}=0\right\} \subset \mathbf{C}^{n+1}$$
for a fixed integer $p>d$. The effect is that the $\mathbf{C}^{*}$ action extending the homothetic action on $C(Y)$ degenerates $X$ to $C(Y)$. By [33, Theorem 2], there exists a Calabi-Yau metric $\omega$ on a neighborhood of the singular point 0, whose tangent cone at 0 is $C(Y)$.

As in the previous section, we will prove Theorem 1.2 by showing that there exists a family $\mathcal{F}$ of model metrics built from applying automorphisms and scalings to $\omega$, and that the singular Kähler-Einstein metric $\omega_{Z}$ on $Z$ can be approximated by $\mathcal{F}$ near $p$. We have the following lemma, characterizing the space $H$ of quadratic harmonic functions whose gradients generate automorphisms of $C(Y)$ that commute with scaling.

Lemma 5.1. Let $H$ be the space of quadratic harmonic functions, whose gradients generate automorphisms of $C(Y)$ that commute with scaling. Then $H$ is spanned by
$$(n-1)|z|^{2}-|x|^{2 \frac{n-2}{n-1}}$$
and
$$|x|^{-\frac{2}{n-1}} a_{j k} x_{j} \bar{x}_{k},$$
where $\left(a_{j k}\right) \in \sqrt{-1} \mathfrak{o}(n, \mathbf{R})$. For $h \in H$ there exist a holomorphic vector field $V$ on $\mathbf{C}^{n+1}$ preserving the hypersurfaces $X_{c}=\left\{c z^{p}+x_{1}^{2}+\cdots x_{n}^{2}=0\right\} \subset \mathbf{C}^{n+1}$, and a constant $\beta$ such that $L_{V} \Omega=n \beta \Omega$, where $\Omega=\left(1 / x_{1}\right) d z \wedge d x_{2} \cdots \wedge d x_{n}$ is the holomorphic volume form on $X_{c}$, and
$$V\left(\frac{|z|^{2}+r^{2}}{2}\right)-\beta\left(\frac{|z|^{2}+r^{2}}{2}\right)=h .$$
In addition we have $|\beta| \leq C\|h\|$ and
$$\sup _{B_{\omega_{c}}(0, r)}|V|_{\omega_{c}} \leq C\|h\| r,$$
i.e. $V$ has at most linear growth. Here $B(o, 1) \subset C(Y)$ is the unit ball and $\omega_{c}=$ $|s|^{-2} F_{c}^{*} \omega$ is the rescaled metric on $X_{c}$ with $F_{c}: X_{c} \rightarrow X$ given by $F_{c}(z, x)=$ $\left(s z, s^{\frac{n-1}{n-2}} x\right)$, and $s^{p-2 \frac{n-1}{n-2}}=c$.

Proof. The first part follows from [34, Lemma 2.2] using Fourier transform in the $\mathbf{C}$ direction or [9, Subsection 3.4.1] using Lemma 3.1 (3). For the holomorphic vector fields, it is very similar to the proof of [34, Lemma 2.3]. The only difference is that when $h=|z|^{2}-\frac{1}{n-1}|x|^{2 \frac{n-2}{n-1}}$, we consider the real holomorphic vector field
$$V=\operatorname{Re}\left(\frac{1}{p} z \partial_{z}+\frac{1}{2} x_{i} \partial_{x_{i}}\right) .$$
Then $V$ preserves the hypersurfaces $c z^{p}+x_{1}^{2}+\cdots x_{n}^{2}=0$, we have
$$V\left(|z|^{2}+r^{2}\right)-\left(\frac{2+n p-2 p}{2 n p}\right)\left(|z|^{2}+r^{2}\right)=\left(\frac{2 n-2-n p+2 p}{2 n p}\right) h_{a u t},$$
and we have
$$L_{V} \Omega=\left(\frac{2+n p-2 p}{2 p}\right) \Omega .$$
The estimate for $|V|_{\omega_{c}}$ is analogous to [34, Proposition 2.1 (2)], using the construction of $\omega$. \(\square\)

We now construct the family of model metrics. Let $h \in H$. Then by Lemma 5.1 there exists a vector field $V$ on $\mathbf{C}^{n+1}$ and a constant $\beta>0$ satisfying the required properties. Let $\phi(t)$ be the one-parameter group of biholomorphisms of $X$ generated by $V$. Set $g_{h}=\phi(1)$ and define $\omega_{h}=e^{-\beta} g_{h}^{*} \omega$.

Lemma 5.2. There exists a neighborhood $0 \in U \subset H$ such that $\mathcal{F}=\left\{\omega_{h} \mid h \in U\right\}$ is a family of model metrics in the sense of Definition 3.2.

Proof. This is similar to the proof of Lemma 4.1. By the construction of $\omega$, for $r_{i} \rightarrow 0,\left(r_{i} \cdot\right): B_{\omega}(0,1) \rightarrow \mathbf{C}^{n+1}$ is a holomorphic map which is a $\Psi\left(i^{-1}\right)$-Gromov-Hausdorff approximation in the sense of property (1) of Definition 3.2, where • denotes the homothetic scaling. Let $h_{i} \in H$ be a bounded sequence, and consider the corresponding model metrics $\omega_{h_{i}}=e^{-\beta_{i}} g_{i}^{*} \omega$. Since $r_{i}^{\prime}=r_{i} e^{\beta_{i} / 2} \rightarrow 0$ as $\beta_{i}$ are bounded (Lemma 5.1), it follows that $F_{i}=\left(r_{i}^{\prime} \cdot\right) \circ g_{i}: B_{r_{i}^{-2} \omega_{h_{i}}}(0,1) \rightarrow \mathbf{C}^{n+1}$ is also a $\Psi\left(i^{-1}\right)$-Gromov-Hausdorff approximation. This establishes property (1) for any bounded neighborhood $U$ of $0 \in H$.

Property (2) follows from Lemma 5.1 Property (3) is entirely similar to the proof of Lemma 4.1. For the rest, recall that $\omega=\sqrt{-1} \partial \bar{\partial} \varphi$, where we have
$$\sup _{B_{\omega}(0, r)}|\varphi| \leq C r^{2},$$
which follows from the construction in [33, Section 8]. Since $\Delta_{\omega} \varphi=n$, we can apply the gradient estimate in annuli to get
$$\sup _{B_{\omega}(0, r)}|\nabla \varphi| \leq C r$$
for all $r>0$. Differentiating $\phi(t)^{*} \varphi$ and using the bounds in Lemma 5.1, we have
$$\left|g_{h}^{*} \varphi-\varphi\right| \leq C\|h\| r^{2}$$
for all $r>0$. It follows that $\left|e^{-\beta} g_{h}^{*} \varphi-\varphi\right| \leq C\|h\| r^{2}$. Now let $k \in H$ be another quadratic harmonic function, and let $W, \gamma$ be the corresponding vector field and constant given in (5.1) of Lemma 5.1. First we note that the vector fields given by (5.1) form a Lie subalgebra. Thus by standard Lie theory, for sufficiently small $h, k, g_{\tilde{h}}=g_{h} g_{k}^{-1}$ for some $\tilde{h} \in H$, with $\tilde{h}=h-k+O(\|h-k\|\|h\|)$. Let $\tilde{V}$ and $\tilde{\beta}$ be the vector field and the constant associated to $\tilde{h}$ in (5.1). We then have
$$\begin{aligned}
\left|e^{-\gamma} g_{k}^{*} \varphi-e^{-\beta} g_{h}\right| & \leq e^{-\gamma} g_{k}^{*}\left|\varphi-e^{-(\beta-\gamma)} g_{\tilde{h}}^{*} \varphi\right| \\
& \leq e^{-\gamma} g_{k}^{*}\left(\left|\varphi-e^{-\tilde{\beta}} g_{\tilde{h}}^{*} \varphi\right|+\left|e^{-\tilde{\beta}}-e^{-(\beta-\gamma)} \| g_{\tilde{h}}^{*} \varphi\right|\right) \\
& \leq e^{-\gamma} g_{k}^{*}\left(C\|\tilde{h}\| r^{2}+C\|\tilde{h}\|\left|g_{\tilde{h}}^{*} \varphi\right|\right) \\
& \leq C\|h-k\| r^{2} .
\end{aligned}$$
This proves property (4) for some small neighborhood $U$.
Finally, let us prove (5). Let $r_{i} \rightarrow 0$ and $h_{i}, k_{i} \in H$ with $\left\|h_{i}\right\|,\left\|k_{i}\right\| \rightarrow 0$. Let $V_{i}, W_{i}$ be the corresponding vector fields for $h_{i}, k_{i}$ defined in Lemma 5.1. Let $\phi_{i}(t), \psi_{i}(t)$ be the flows of $V_{i}, W_{i}$, respectively. Set $g_{h_{i}}=\phi(1)$ and $g_{k_{i}}=\psi(1)$. Then the model metrics are given by $\omega_{h_{i}}=e^{-\beta_{i}} g_{h_{i}}^{*} \omega$ and $\omega_{k_{i}}=e^{-\gamma_{i}} g_{k_{i}}^{*} \omega$, with $\left|\beta_{i}\right| \leq$ $C\left\|h_{i}\right\|$ and $\left|\gamma_{i}\right| \leq C\left\|k_{i}\right\|$. Fix a compact set $K$ in the regular set of $B(0,1)$, and let $K_{i} \subset B_{r_{i}^{-2} \omega_{h_{i}}}(0,1)$ be compact sets converging to $K$ in the Gromov-Hausdorff sense. By (5.1) in Lemma 5.1, we have
$$V_{i}\left(r^{2} / 2\right)-\beta_{i}\left(r^{2} / 2\right)=h_{i}$$
and the analogous equation for $W_{i}, \gamma_{i}, k_{i}$. Here we denote the cone metric as $\omega_{C(Y)}=\frac{1}{2} \sqrt{-1} \partial \bar{\partial} r^{2}$. Since $\varphi_{i}=r_{i}^{-2} \varphi$ on $K_{i}$ converges to $r^{2} / 2$ in $C^{\infty}$ on $K$, it follows that under the Gromov-Hausdorff approximation,
$$\left|V_{i} \varphi_{i}-\beta_{i} \varphi_{i}-h_{i}\right| \leq \Psi\left(i^{-1}\right)\left\|h_{i}\right\| .$$
Using power series expansion as in Lemma 4.1 and the above inequality, it follows that
$$\left|e^{-\beta_{i}} g_{h_{i}}^{*} \varphi_{i}-\varphi_{i}-h_{i}\right| \leq O\left(\left\|h_{i}\right\|^{2}\right)+\Psi\left(i^{-1}\right)\left\|h_{i}\right\| \leq \Psi\left(i^{-1}\right)\left\|h_{i}\right\| .$$
Now, let $\tilde{h}_{i} \in H$ with vector field $\tilde{V}_{i}$ and constant $\tilde{\beta}_{i}$ such that $g_{\tilde{h}_{i}}=g_{h_{i}} g_{k_{i}}^{-1}$ and $\tilde{h}_{i}=h_{i}-k_{i}+O\left(\left\|h_{i}-k_{i}\right\|\left\|k_{i}\right\|\right)$. Then we have
$$\begin{aligned}
\left|e^{-\beta_{i}} g_{k_{i}}^{*} \varphi_{i}-e^{-\gamma_{i}} g_{h_{i}}^{*} \varphi_{i}-\left(k_{i}-h_{i}\right)\right| \leq & e^{-\beta_{i}} g_{k_{i}}^{*}\left|\varphi_{i}-e^{-\left(\gamma_{i}-\beta_{i}\right)} g_{\tilde{h}_{i}}^{*} \varphi_{i}+\tilde{h}_{i}\right| \\
& +\left|e^{-\beta_{i}} g_{k_{i}}^{*} \tilde{h}_{i}+\left(k_{i}-h_{i}\right)\right| \\
\leq & \Psi\left(i^{-1}\right)\left\|\tilde{h}_{i}\right\|+C\left\|h_{i}-k_{i}\right\|\left\|k_{i}\right\| \\
\leq & \Psi\left(i^{-1}\right)\left\|h_{i}-k_{i}\right\| .
\end{aligned}$$
Setting $u_{i}=e^{-\beta_{i}} g_{k_{i}}^{*} \varphi_{i}-e^{-\gamma_{i}} g_{h_{i}}^{*} \varphi_{i}$, this conclude the proof of (5). \(\square\)

Now we turn to showing that $\omega_{Z}$ can be approximated by $\mathcal{F}$. As in the previous section, let $\lambda=1 / \sqrt{2}$, and let $\left(Z_{i}, p_{i}\right)$ denote $(Z, p)$ scaled up by a factor of $\lambda^{-i}$. Let $B_{i}$ denote the unit ball centered at $p_{i}$, i.e. the ball $B\left(p, \lambda^{i}\right)$ scaled up to unit size. Let $F_{\infty}$ denote the inclusion of $C(Y)$ in $\mathbf{C}^{n+1}$. Note that the components of $F_{\infty}$ consist of $L^{2}$ orthonormal homogeneous functions $z, x_{i}$. Let $B \subset C(Y)$ be the unit ball centered at 0.

Proposition 5.3. For sufficiently large $i$ we have holomorphic maps $F_{i}: B_{i} \rightarrow$ $\mathbf{C}^{n+1}$ with the following properties, where $\Psi\left(i^{-1}\right)$ denotes a function converging to zero as $i \rightarrow \infty$.
\begin{itemize}
\item[(1)] On the ball $B_{i}$ the map $F_{i}$ gives a $\Psi\left(i^{-1}\right)$-Gromov-Hausdorff approximation to the embedding $F_{\infty}: B \rightarrow \mathbf{C}^{n+1}$. More precisely, there exist $\Psi\left(i^{-1}\right)$ -Gromov-Hausdorff approximations $g_{i}: B_{i} \rightarrow B$ such that $\left|F_{i}-F_{\infty} \circ g_{i}\right|<$ $\Psi\left(i^{-1}\right)$.
\item[(2)] The image $F_{i}\left(B_{i}\right)$ lies in $X_{i}=\left\{a_{i} z^{p}+x_{1}^{2}+\ldots x_{n}^{2}=0\right\}$ for some $a_{i}>0$ with $F_{i}\left(p_{i}\right)=0 . \quad X_{i}$ is equipped with the metric $\omega_{i}=r_{i}^{-2} G_{i}^{*} \omega$, where $r_{i}^{p-2 \frac{n-1}{n-2}}=a_{i}$ and $G_{i}: X_{i} \rightarrow X$ is given by $(z, x) \rightarrow\left(r_{i} z, r_{i}^{\frac{n-1}{n-2}} x\right)$.
\item[(3)] Let $\eta_{i}=\left(F_{i}^{-1}\right)^{*}\left(\lambda^{-2 i} \omega_{Z}\right)$ denote the metric on the image $F_{i}\left(B_{i}\right)$ induced by $\lambda^{-2 i} \omega_{Z}$. Then we have $\operatorname{Ric}\left(\eta_{i}\right)=c_{i} \eta_{i}$ for some $\left|c_{i}\right|<\Psi\left(i^{-1}\right)$, and the distance functions $d_{\eta_{i}}, d_{\omega_{i}}$ satisfy $\left|d_{\eta_{i}}-d_{\omega_{i}}\right|<\Psi\left(i^{-1}\right)$.
\item[(4)] We have $\eta_{i}^{n}=e^{f_{i}} \omega_{i}^{n}$ and $\eta_{i}=\omega_{i}+\sqrt{-1} \partial \bar{\partial} u_{i}$, with $f_{i}(0)=0$ and $\left|\nabla f_{i}\right| \eta_{i},\left|u_{i}\right|<$ $\Psi\left(i^{-1}\right)$.
\end{itemize}
In particular $\omega_{Z}$ can be approximated by $\mathcal{F}$ in the sense of Definition 3.6,
Proof. Identifying the germ of $(Z, p)$ with the germ of $(X, 0)$, we can assume that $B_{i} \subset X$. Write $R=\mathcal{O}_{X, 0}$, and let $v$ be the evaluation of $(X, 0)$ associated to $\omega$. By the construction of $\omega$, the associated graded ring $R_{v}$ is isomorphic to $R(C(Y))$, which is a Ricci-flat Kähler cone. So by Li-Xu [28, Theorem 1.3] and Li-Wang-Xu [27, Corollary A.4], we have $d_{K E}=v$, where $d_{K E}$ is the valuation given by $\omega_{Z}$.

We will focus on the case when $n=3$, as when $n>3$ it is simpler. As in Proposition 4.2, we have a subspace $P \subset \mathcal{O}_{Z, p}$ and an adapted sequence $\left\{G_{i}^{a}\right\}_{i}$ of bases for $P$, which for sufficiently large $i$ define holomorphic embeddings $F_{i}: B_{i} \rightarrow$ $\mathbf{C}^{N} . F_{i}$ converges in the Gromov-Hausdorff sense to $F_{\infty}$, which up to a unitary rotation is given by $\left(1, z, z^{2}, \mathbf{x}\right)$, the components of which form an orthonormal basis for the corresponding space in $R(C(Y))$ (we assume $n=3$ ). Here $\mathbf{x}=\left(x_{1}, x_{2}, x_{3}\right)$. From this we see that $N=6$. Note that since we have the isomorphism of germs, $\mathcal{O}_{Z, p}$ is also generated by $S=\left\{1, z, z^{2}, \mathbf{x}\right\}$. We can decompose $G_{i}^{a}$ as
$$G_{i}^{a}=g_{i}^{a}+k_{i}^{a},$$
where $g_{i}^{a}$ is a linear combination of elements in $S$ with degree equal to $d_{a}$ and $k_{i}^{a}$ has degree $>d_{a}$. As in the proof of Proposition 4.2 we have $\sup _{B_{i}}\left|G_{i}^{a}-g_{i}^{a}\right| \rightarrow 0$ as $i \rightarrow \infty$.

Define $\tilde{F}_{i}=\left(g_{i}^{a}\right)$. We can write $\tilde{F}_{i}=\left(c_{i}, z_{i}, w_{i}, \mathbf{x}_{i}\right)$, where
$$\begin{aligned}
z_{i} & =d_{i} z \\
w_{i} & =W_{i}^{T} \mathbf{x}+b_{i} z^{2}, \\
\mathbf{x}_{i} & =A_{i} \mathbf{x}+z^{2} V_{i},
\end{aligned}$$
and $b_{i}, c_{i}, d_{i}$ are scalars, $V_{i}, W_{i}$ are vectors and $A_{i}$ is a matrix. From the Gromov-Hausdorff convergence $\tilde{F}_{i} \rightarrow F_{\infty}$ we see that $\sup \left|z_{i}^{2}-w_{i}\right| \leq \Psi\left(i^{-1}\right)$, and so $\left|W_{i}\right|,\left|d_{i}^{2}-b_{i}\right| \leq \Psi\left(i^{-1}\right)$. On the other hand, writing the equation for $X$ in terms of $z_{i}, \mathbf{x}_{i}$ gives
$$\left|d_{i}\right|^{-p},\left|d_{i}^{-2} V_{i}\right|,\left|A_{i}^{T} A_{i}-I d\right| \leq \Psi\left(i^{-1}\right) .$$
Using these we can modify the embeddings $\tilde{F}_{i}$ by some $g_{i} \in G L(6)$ with $\left|g_{i}-I d\right| \leq$ $\Psi\left(i^{-1}\right)$ so that $\mathbf{x}_{i}=\left(A_{i}-b_{i}^{-1} V_{i} W_{i}^{T}\right) \mathbf{x}$. Since $A_{i}-b_{i}^{-1} V_{i} W_{i}^{T}$ converges to an orthogonal matrix, by further modifying the embeddings by linear transformations close to identity, we have $\mathbf{x}_{i}=A_{i}^{\prime} \mathbf{x}$ with $A_{i}^{\prime} \in O(3)$. We now drop the first and the third components of $\tilde{F}_{i}$ and obtain embeddings $F_{i}=\left(z_{i}, \mathbf{x}_{i}\right)$ into $\mathbf{C}^{4}$, whose image is given by $d_{i}^{-p} z^{p}+\mathbf{x}_{i}^{T} \mathbf{x}_{i}=0$. Set $a_{i}=d_{i}^{-p}$. By applying scalings $(z, \mathbf{x}) \rightarrow\left(c z, c^{\frac{n-1}{n-2}} \mathbf{x}\right)$ with some $|c|=1$, we can assume that $a_{i}>0$. So we have proved (1) and (2). The rest follows verbatim the proof of Proposition 4.2. \(\square\)

Proof Theorem 1.2. Proposition 5.3 shows that $\omega_{Z}$ can be approximated by $\mathcal{F}$ constructed in Lemma 5.2. The rest of the proof is very similar to the proof of Theorem 1.1 so we omit it. \(\square\)

\section*{6. Uniqueness of Calabi-Yau metrics under small perturbation}

In this section we prove Theorem 1.3, which says that polynomially subquadratic perturbation of a $\partial \bar{\partial}$-exact Calabi-Yau metric with maximal volume growth must be trivial. Recall that $X$ is said to have maximal volume growth if there exists $v>0$ such that for all $p \in X$ and $r>0$, we have $\operatorname{Vol}(B(p, r)) \geq v r^{2 n}$. It was proved in [30] that tangent cones at infinity of a Calabi-Yau manifold with maximal volume growth is an affine variety. It was also observed in [34, Section 3.1] that Donaldson-Sun theory extends to the $\partial \bar{\partial}$-exact case. In particular the tangent cone at infinity is unique. To prove Theorem 1.3, we need the following decay estimate. For the following, let $o \in X$ be a fixed point, and write $B(o, r)$ for the $r$-ball in $X$ with respect to the rescaled metric $c^{2} \omega$, where $0<c \ll 1$.

Lemma 6.1. For any $\alpha>0$ sufficiently small, there exists a constant $\lambda_{0}>0$ such that if $\lambda<\lambda_{0}$ and $\epsilon>0$ is sufficiently small (depending on $\lambda$ ), then we have the following. Suppose that
$$d_{G H}\left(B\left(o, \epsilon^{-1}\right), B\left(0, \epsilon^{-1}\right)\right)<\epsilon,$$
where $B\left(0, \epsilon^{-1}\right)$ is the corresponding ball in the tangent cone $C(Y)$. Suppose $u$ is a smooth function on $B(o, 1)$ with $\sup _{B(o, 1)}|u|<\epsilon$ satisfying
$$(\omega+\sqrt{-1} \partial \bar{\partial} u)^{n}=\omega^{n} .$$
Then we can find a smooth function $u^{\prime}$ on $B(o, 1 / 2)$ such that
\begin{itemize}
\item[(1)] $\partial \bar{\partial}\left(u-u^{\prime}\right)=0$,
\item[(2)] $\sup _{B(o, \lambda)}\left|u^{\prime}\right| \leq \lambda^{2-\alpha} \sup _{B(o, 1)}|u|$.
\end{itemize}

Proof. The proof is very similar to the proof of [34, Proposition 4.1], so we omit it. We note that the decay rate in (2) is slower than quadratic. Thus for this result we only need to subtract "subquadratic" harmonic functions from $u$ and automorphisms of the cone do not enter the argument. The $\partial \bar{\partial}$-exactness is required to apply Theorem 2.1 and to embed the manifold $X$ as an affine variety in $\mathbf{C}^{N}$. This in turn is required to employ the fact that subquadratic harmonic functions on the cone extend to pluriharmonic functions on the manifold. \(\square\)

Proof of Theorem 1.3. We scale down the metric. Let $\omega_{i}=2^{-2 i} \omega$, and let $u_{i}=$ $2^{-2 i} u$. Denote $B\left(o_{i}, 1\right)$ the unit ball with respect to the scaled-down metric $\omega_{i}$. Let $i_{0}$ be large enough so that
$$\sup _{B\left(o_{i}, 1\right)}\left|u_{i}\right| \leq 2^{-2 i} C\left(1+2^{-i}\right)^{2-\delta} \leq C^{\prime} 2^{-i \delta}<\epsilon,$$
and that
$$d_{G H}\left(B\left(o_{i}, \epsilon^{-1}\right), B\left(o, \epsilon^{-1}\right)\right)<\epsilon$$
for $i>i_{0}$, where $\epsilon$ is given in Lemma 6.1 Let $\alpha>0$ be sufficiently small as in Lemma 6.1 In particular we also want $\alpha<\delta$. Then we can apply Lemma 6.1 We may set $\lambda=2^{-m}$, where $m>0$ an sufficiently large integer. Let $i=i_{0}+k m$, where $k>0$ is an integer. Then by Lemma 6.1, there exists a smooth function $u^{\prime}$ on $B\left(o_{i}, 1 / 2\right)$ such that $\partial \bar{\partial}\left(u_{i}-u^{\prime}\right)=0$ and $\sup _{B\left(o_{i}, \lambda\right)}\left|u^{\prime}\right| \leq \lambda^{2-\alpha} \sup _{B(o, 1)}\left|u_{i}\right|$. Set $u_{i-1}^{\prime}=\lambda^{-2} u^{\prime}$. Note that
$$B\left(o_{i}, \lambda\right)=B\left(o_{i-m}, 1\right)=B\left(o_{i_{0}+(k-1) m}, 1\right) .$$
So we have
$$\sup _{B\left(o_{i_{0}+(k-1) m}, 1\right)}\left|u_{i-1}^{\prime}\right| \leq \lambda^{-\alpha} \sup _{B\left(o_{i}, 1\right)}\left|u_{i}\right| \leq 2^{m \alpha-k m \delta} C^{\prime} 2^{-i_{0} \delta}<\epsilon .$$
We can then iterate this process $k$ times. In the end, we have a function $u_{i_{0}}^{\prime}$ on $B\left(o_{i_{0}}, 1\right)$ with
$$\sup _{B\left(o_{i_{0}}, 1\right)}\left|u_{i_{0}}^{\prime}\right| \leq 2^{k m(\alpha-\delta)} C^{\prime} 2^{-i_{0} \delta}$$
Rescaling back, we now have a smooth function $v_{k}=2^{2 i_{0}} u_{i_{0}}^{\prime}$ satisfying
$$\left(\omega+\sqrt{-1} \partial \bar{\partial} v_{k}\right)^{n}=\omega^{n}$$
on $B\left(o, 2^{i_{0}}\right)$ such that $\partial \bar{\partial}\left(u-v_{k}\right)=0$ and
$$\sup _{B\left(o, 2^{i_{0}}\right)}\left|v_{k}\right| \leq 2^{k m(\alpha-\delta)} C^{\prime} .$$
By Lemma 3.3, up to passing to a subsequence $v_{k}$ converges uniformly in $C^{\infty}$ to 0 as $k \rightarrow \infty$. It follows that $\partial \bar{\partial} u=0$ on $B\left(o, 2^{i_{0}}\right)$. We can then increase $i_{0}$ and conclude that $\partial \bar{\partial} u=0$ on $X$. \(\square\)

We remark that the $\partial \bar{\partial}$-exactness condition is not required when the tangent cone at infinity has a smooth link (and hence is unique by Colding-Minicozzi [12]). In this case one can show Lemma 6.1 using the existence of adapted sequences of bases for harmonic functions with polynomial growth (see for example [9, 4.2.2]) and the maximum principle for the complex Monge-Ampère equation. While the setup in this case is closer to the asymptotically conical case considered in Conlon-Hein [14], this approach has the advantage that the polynomial convergence to the tangent cone at infinity is not required. It would be interesting to know if a version of the $\partial \bar{\partial}$ lemma holds in the setting of maximal volume growth, which would enable us to prove results on the level of metrics similar to [14, Theorem 3.1] as opposed to potentials.

\section*{References}
\begin{itemize}
\item[] [1] Cheeger, J., Colding, T. H. Lower bounds on Ricci curvature and the almost rigidity of warped products, Ann. of Math. (2) 144 (1996), no. 1, 189-237. (Page 7)
\item[] [2] Cheeger, J., Colding, T. H. On the structure of spaces with Ricci curvature bounded below, I., J. Differential Geom. 46 (1997), no. 3, 406-480. (Page 6)
\item[] [3] Cheeger, J., Colding, T. H., Tian, G. On the singularities of spaces with bounded Ricci curvature, Geom. Funct. Anal. 12 (2002), no. 5, 873-914. (Pages 7 and 8)
\item[] [4] Cheeger, J., Tian, G. On the cone structure at infinity of Ricci flat manifolds with Euclidean volume growth and quadratic curvature decay, Invent. Math. 118 (1994), 493-571. (Page 8)
\item[] [5] Chen, X., Donaldson, S., Sun, S. Kähler-Einstein metrics and stability, Int. Math. Res. Not. IMRN (2014), no. 8, 2119-2125. (Page 1)
\item[] [6] Chen, X. and Donaldson, S. and Sun, S. Kähler-Einstein metrics on Fano manifolds. I: Approximation of metrics with cone singularities, J. Amer. Math. Soc. 28 (2015), no. 1, 183-197. (Page 1)
\item[] [7] Chen, X. and Donaldson, S. and Sun, S. Kähler-Einstein metrics on Fano manifolds. II: Limits with cone angle less than $2 \pi$, J. Amer. Math. Soc. 28 (2015), no. 1, 199-234. (Page 1 )
\item[] [8] Chen, X. and Donaldson, S. and Sun, S. Kähler-Einstein metrics on Fano manifolds. III: Limits as cone angle approaches $2 \pi$ and completion of the main proof, J. Amer. Math. Soc. 28 (2015), no. 1, 235-278. (Page 1 )
\item[] [9] Chiu, S.-K. On Calabi-Yau manifolds with maximal volume growth, PhD Thesis, University of Notre Dame, 2021. (Pages 3822 and 27 )
\item[] [10] Chiu, S.-K. Subquadratic harmonic functions on Calabi-Yau manifolds with Euclidean volume growth, arXiv:1905.12965. (Page 8)
\item[] [11] Colding, T. H. Ricci curvature and volume convergence, Ann. of Math. (2) 145 (1997), no. 3, 477-501. (Page 20)
\item[] [12] Colding, T. H., Minicozzi, W. P. On uniqueness of tangent cones for Einstein manifolds, Invent. Math. 196.3 (2014), 515-588. (Page 27 )
\item[] [13] Colding, T. H., Naber, A. Sharp Hölder continuity of tangent cones for spaces with a lower Ricci curvature bound and applications, Ann. of Math. (2) 176 (2012), no. 2, 1173-1229. (Page 11 )
\item[] [14] Conlon, R. J., Hein, H.-J. Asymptotically conical Calabi-Yau manifolds, I, Duke Math. J. 162 (2013), no. 15, 2855-2902. (Pages 38 and 27 )
\item[] [15] Datar, V., Fu, X., Song, J. Kähler-Einstein metrics near an isolated log-canonical singularity, arXiv:2106.05486. (Page 1)
\end{itemize}
\begin{itemize}
\item[] [16] Donaldson, S. K. Stability, birational transformations and the Kahler-Einstein problem, Surv. Differ. Geom., 17, 203-228. (Page 19 )
\item[] [17] Donaldson, S. and Sun, S. Gromov-Hausdorff limits of Kähler manifolds and algebraic geometry, Acta Math. 213 (2014), no. 1, 63-106. (Pages 1 and 4 )
\item[] [18] Donaldson, S. and Sun, S. Gromov-Hausdorff limits of Kähler manifolds and algebraic geometry. II, J. Differential Geom. 107 (2017), no. 2, 327-371. (Pages 1418 and 19 )
\item[] [19] Eyssidieux, P., Guedj, V. Zeriahi, A. Singular Kähler-Einstein metrics, J. Amer. Math. Soc. 22 (2009), no. 3, 607-639. (Page 1 )
\item[] [20] Fu, X., Hein, H.-J., Jiang, X. Asymptotics of Kähler-Einstein metrics on complex hyperbolic cusps, arXiv:2108.13390. (Page 1 )
\item[] [21] Grauert, H., Remmert, R. Plurisubharmonische Funktionen in komplexen Räumen, Math. Z. 65 (1956), 175-194. (Page 20)
\item[] [22] Guenancia H., Zeriahi A. Continuity of singular Kähler-Einstein potentials, arXiv:2012.02018, to appear in IMRN. (Page 11)
\item[] [23] Hein, H.-J., Naber, A., Isolated Einstein singularities with singular tangent cones, in preparation. (Page 2)
\item[] [24] Hein, H.-J. and Sun, S. Calabi-Yau manifolds with isolated conical singularities, Publ. Math. Inst. Hautes Études Sci. 126 (2017), 73-130. (Pages 12 nd 21 )
\item[] [25] Kobayashi, R. Einstein-Kähler $V$-metrics on open Satake $V$-surfaces with isolated quotient singularities, Math. Ann. 272 (1985), 385-398. (Page 1 )
\item[] [26] Li, C.,Tian, G., Wang, F. On the Yau-Tian-Donaldson conjecture for singular Fano varieties, Comm. Pure Appl. Math. 74 (2021), no. 8, 1748-1800. (Page 1 )
\item[] [27] Li, C., Wang, X., Xu, C. Algebraicity of the metric tangent cones and equivariant $K$-stability, J. Amer. Math. Soc. 34 (2021), no. 4, 1175-1124. (Pages 12 16 18, and 24)
\item[] [28] Li, C. and Xu, C. Stability of valuations: higher rational rank, Peking Math. J. 1 (2018), no. 1, 1-79. (Pages 1218 and 24 )
\item[] [29] Liu, G., Sékelyhidi, G. Gromov-Hausdorff limits of Kähler manifolds with Ricci curvature bounded below I, arXiv:1804.08567. (Page 20 )
\item[] [30] Liu, G., Székelyhidi, G. Gromov-Hausdorff limits of Kähler manifolds with Ricci curvature bounded below II, Comm. Pure Appl. Math. 74 (2021), no. 5, 909-931. (Page 25 )
\item[] [31] Savin, O. Small perturbation solutions for elliptic equations, Comm. Partial Differential Equations 32 (2007), no. 4-6, 557-578. (Pages 9 and 10 )
\item[] [32] Stenzel, M. B. Ricci-flat metrics on the complexification of a compact rank one symmetric space, Manuscripta Math. 80 (1993), no. 2, 151-163. (Page 21 )
\item[] [33] Székelyhidi, G. Degenerations of $\mathbf{C}^{n}$ and Calabi-Yau metrics, Duke Math. J. 168 (2019), no. 14, 2651-2700. (Pages 222 and 23 )
\item[] [34] Székelyhidi, G. Uniqueness of some Calabi-Yau metrics on $\mathbf{C}^{n}$, Geom. Funct. Anal. 30 (2020), no. 4, 1152-1182. (Pages 345122225 and 26 )
\item[] [35] Yau, S. T. On the Ricci curvature of a compact Kähler manifold and the complex Monge-Ampère equation. I, Comm. Pure Appl. Math. 31 (1978), no. 3, 339-411. (Page 1 )
\end{itemize}

Mathematical Institute, University of Oxford, Oxford, UK
Email address: Shih-Kai.Chiu@maths.ox.ac.uk
Department of Mathematics, University of Notre Dame, Notre Dame, Indiana, USA
Email address: gszekely@nd.edu