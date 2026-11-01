---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: Scalar and tensor eigenvalue bounds for conformally Kähler Einstein four-manifolds]

Induction gives $r_{j}=\sum_{k=j}^{10} p_{k} 231^{k-j} 118^{10-k}$, so $r_{0}=118^{10} \mathfrak{p}(231 / 118)$. Uniqueness and (6.13) prove (6.10). The denominator $D_{a}=D(a-1)$ is positive for $a>1$ by (4.21); hence the Calabi derivative has no pole on this interval. \(\square\)
6.2. The antisymmetric affine potential. Henceforth $a=a_{*}$ and $s=s_{a_{*}}$. Put
$$q=x_{1}-x_{2}, \quad F=q / s .$$
The moment components are global smooth functions, and $s$ is strictly positive. Thus $F \in C^{\infty}(M)$. The polygon and $s$ are invariant under $\left(x_{1}, x_{2}\right) \mapsto\left(x_{2}, x_{1}\right)$, whereas $q$ changes sign. Therefore
$$\int_{M} F d v_{g}=4 \pi^{2} \int_{P_{a}}\left(x_{1}-x_{2}\right) s^{-5} d x=0$$
It is nonzero since $P_{a}$ has nonempty interior. Define
$$V=\int_{P_{a}} s^{-4} d x, \quad I=\int_{P_{a}} q^{2} s^{-6} d x, \quad J=\int_{\partial P_{a}} q^{2} s^{-4} d \sigma, \quad K=\int_{\partial P_{a}} s^{-2} d \sigma$$
All four numbers are positive. Since $\operatorname{Scal}_{g}=4 \Lambda$, Proposition 5.1 and Corollary 5.3 give
$$\Lambda=\frac{K}{2 V}, \quad \frac{\mathcal{R}_{g}(F)}{\Lambda}=\frac{2 J V}{I K}-2, \quad \lambda_{1}^{\mathrm{sc}}(g) \leq \mathcal{R}_{g}(F) .$$
Here $\mathcal{R}_{g}(F)=\int_{M}|d F|_{g}^{2} d v_{g} / \int_{M} F^{2} d v_{g}$. The identities involving $\Lambda$ are asserted only at the CLW parameter, where (6.1) holds.

For any function $f$ of $t=x_{1}+x_{2}$, change variables from $\left(x_{1}, x_{2}\right)$ to $\left(x_{1}, t\right)$; the Jacobian is one. The slice intervals are $0 \leq x_{1} \leq t$ for $0 \leq t \leq a$ and $t-a \leq x_{1} \leq a$ for $a \leq t \leq a+1$. Consequently
$$\begin{aligned}
\int_{P_{a}} f(t) d x & =\int_{0}^{a} t f(t) d t+\int_{a}^{a+1}(2 a-t) f(t) d t, \\
\int_{\text {slice at } t}\left(x_{1}-x_{2}\right)^{2} d x_{1} & = \begin{cases}t^{3} / 3, & 0 \leq t \leq a \\
(2 a-t)^{3} / 3, & a \leq t \leq a+1 .\end{cases}
\end{aligned}$$
The second line follows by integrating $\left(2 x_{1}-t\right)^{2}$ on the stated intervals. On the diagonal facet $t=a+1$, lattice measure is $d x_{1}$ for $1 \leq x_{1} \leq a$, and
$$\int_{1}^{a}\left(2 x_{1}-a-1\right)^{2} d x_{1}=\frac{(a-1)^{3}}{3} .$$
The other four facets occur in two exchange-symmetric pairs. Equations (6.19)-(6.20) give
$$\begin{aligned}
& V=\int_{0}^{a} \frac{t}{s(t)^{4}} d t+\int_{a}^{a+1} \frac{2 a-t}{s(t)^{4}} d t \\
& I=\frac{1}{3}\left(\int_{0}^{a} \frac{t^{3}}{s(t)^{6}} d t+\int_{a}^{a+1} \frac{(2 a-t)^{3}}{s(t)^{6}} d t\right) \\
& J=2 \int_{0}^{a} \frac{t^{2}}{s(t)^{4}} d t+2 \int_{a}^{a+1} \frac{(2 a-t)^{2}}{s(t)^{4}} d t+\frac{(a-1)^{3}}{3 s(a+1)^{4}} \\
& K=2 \int_{0}^{a+1} s(t)^{-2} d t+\frac{a-1}{s(a+1)^{2}}
\end{aligned}$$
The measure on the diagonal facet is $d x_{1}$, not $\sqrt{2} d x_{1}$.
6.3. The rational inequality. The four integrals above are rational functions of $a$. For integers $j \geq 0$ and $p>j+1$, put
$$\mathcal{I}_{j, p}(l, r ; b, c)=c^{-j-1} \sum_{v=0}^{j}\binom{j}{v}(-b)^{j-v} \frac{(b+c r)^{v-p+1}-(b+c l)^{v-p+1}}{v-p+1} .$$

If $c \neq 0$ and $b+c t>0$ on $[l, r]$, the substitution $z=b+c t$ gives
$$\int_{l}^{r} t^{j}(b+c t)^{-p} d t=\mathcal{I}_{j, p}(l, r ; b, c) .$$
Indeed, $t^{j} d t=c^{-j-1}(z-b)^{j} d z$; expand $(z-b)^{j}$ and integrate $z^{v-p}$. The assumption $p>j+1$ excludes the exponent -1.

Lemma 6.2. At $a=a_{*}$, the moments in (6.17) satisfy
$$3951 \mathrm{IK}-2000 \mathrm{JV}>0 .$$
Consequently
$$\mathcal{R}_{g}(F)<\frac{1951}{1000} \Lambda .$$
Proof. Proposition A. 2 proves (6.27) from $\mathfrak{p}\left(a_{*}\right)=0$ and $a_{*}>231 / 118$. Since $I, K>0$, division by 1000IK gives
$$\frac{2 J V}{I K}<\frac{3951}{1000} .$$
Subtracting 2 in (6.18) proves (6.28). \(\square\)

Remark 6.3. The function $F$ is a test function, not an asserted eigenfunction. The proof gives an upper bound for $\lambda_{1}^{\mathrm{sc}}(g)$; it does not identify its value or multiplicity. Nor is the space of affine quotients asserted to be preserved by $\Delta_{g}$. Hall-Murphy's numerical value in the anti-invariant subspace [17, Section 5] is obtained from an approximate metric and is not used here.

\section*{7. Conformal instability and the entropy index}
7.1. The scalar lower bound and its equality case. For a nonconstant eigenfunction on a closed Einstein four-manifold, $\Delta \psi=\lambda \psi$, integration by parts and (2.3) give
$$\left\|\nabla^{2} \psi\right\|_{L^{2}}^{2}=\lambda(\lambda-\Lambda)\|\psi\|_{L^{2}}^{2}, \quad\left\|\nabla^{2} \psi+\frac{\lambda}{4} \psi g\right\|_{L^{2}}^{2}=\lambda\left(\frac{3}{4} \lambda-\Lambda\right)\|\psi\|_{L^{2}}^{2} .$$
In particular $\lambda \geq 4 \Lambda / 3$ when $\Lambda>0$. Equality gives $\nabla^{2} \psi=-(\Lambda / 3) \psi g$ pointwise, because a smooth tensor with zero squared integral is zero. Obata's theorem [26] then makes the manifold isometric to a round sphere. The CLW manifold has $b_{2}=3$, whereas $S^{4}$ has $b_{2}=0$, so equality is excluded. Combining this with (6.18) and Lemma 6.2 proves the eigenvalue inequalities in Theorem B.
7.2. The entropy Hessian. For a closed $n$-manifold, put
$$\begin{aligned}
\mathcal{W}(g, v, \tau) & =(4 \pi \tau)^{-n / 2} \int_{M}\left[\tau\left(\operatorname{Scal}_{g}+|d v|^{2}\right)+v-n\right] e^{-v} d v_{g} \\
v(g) & =\inf \left\{\mathcal{W}(g, v, \tau): \tau>0, v \in C^{\infty}(M),(4 \pi \tau)^{-n / 2} \int_{M} e^{-v} d v_{g}=1\right\}
\end{aligned}$$
At a positive Einstein metric $\operatorname{Ric}_{g}=\Lambda g, v$ is critical. We use its Hessian on the space
$$S_{g}=\left\{H \in C^{\infty}\left(S^{2} T^{*} M\right): \delta H=0, \int_{M} \operatorname{tr}_{g} H d v_{g}=0\right\} .$$
The Cao-Hamilton-Ilmanen formula, with the proof and normalization in Cao-Zhu [6, Theorem 1.2], states that
$$D^{2} v_{g}(H, H)=\frac{1}{4 \Lambda \operatorname{Vol}_{g}(M)}\left\langle\left(2 \Lambda-L_{g}\right) H, H\right\rangle_{L^{2}} \quad\left(H \in S_{g}\right) .$$
To match conventions, their shrinking parameter is $\tau=1 /(2 \Lambda)$ and their rough Laplacian is $-\nabla^{*} \nabla$. On (7.3), the divergence and integrated-trace terms of their operator vanish. Its auxiliary potential solves $(\Lambda-\Delta) v=0$ with zero mean. The lower bound $\lambda_{1}^{\mathrm{sc}} \geq n \Lambda /(n-1)>\Lambda$, obtained by the $n$-dimensional version of (7.1), gives $v=0$. The remaining operator is $-\frac{1}{2} \nabla^{*} \nabla+\stackrel{\circ}{R}=\frac{1}{2}\left(2 \Lambda-L_{g}\right)$,
which gives the coefficient in (7.4). We retain the prefactor of [6, Theorem 1.2] in all the formulas below.

Both diffeomorphism and scaling directions lie in the radical of this Hessian. Indeed, $D v_{g^{\prime}}\left(\mathcal{L}_{X} g^{\prime}\right)=$ 0 for every nearby metric $g^{\prime}$, by diffeomorphism invariance. Differentiating in a direction $H$ at the critical metric gives
$$D^{2} v_{g}\left(H, \mathcal{L}_{X} g\right)+D v_{g}\left(\mathcal{L}_{X} H\right)=0, \quad D^{2} v_{g}\left(H, \mathcal{L}_{X} g\right)=0 .$$
Differentiating $D v_{g^{\prime}}\left(g^{\prime}\right)=0$ gives $D^{2} v_{g}(H, g)+D v_{g}(H)=0$, hence $D^{2} v_{g}(H, g)=0$. These invariances follow from (7.2): pullback of $g, v$ changes the integrals by the change-of-variables formula; replacing $(g, \tau)$ by $(c g, c \tau)$ leaves both the normalized measure and $\tau\left(\right.$ Scal $\left._{g}+|d v|_{g}^{2}\right)$ unchanged.

Proposition 7.1 (Conformal eigendirections). Let $\left(M^{4}, g\right)$ be closed and connected, with $\operatorname{Ric}_{g}=\Lambda g$, $\Lambda>0$. Suppose $\Delta_{g} \psi=\lambda \psi, \psi \neq 0$, and $4 \Lambda / 3<\lambda<2 \Lambda$. Then
$$D^{2} v_{g}(\psi g, \psi g)=\frac{(2 \Lambda-\lambda)(3 \lambda-4 \Lambda)}{4 \Lambda(\lambda-\Lambda) \operatorname{Vol}_{g}(M)}\|\psi\|_{L^{2}}^{2}>0 .$$
The metrics $g_{t}=(1+t \psi) g$ are positive definite for $|t|<\|\psi\|_{\infty}^{-1}$. There exists $\epsilon \in\left(0,\|\psi\|_{\infty}^{-1}\right)$ such that $v\left(g_{t}\right)>v(g)$ whenever $0<|t|<\epsilon$.

Proof. Integration of the eigenfunction equation gives $\int_{M} \psi d v_{g}=0$. Define
$$H=\nabla^{2} \psi+(\lambda-\Lambda) \psi g .$$
This tensor equals $-S(\psi)$ for the operator defined in [15, Definition 5.2 and Theorem 5.4], where it is attributed to Cao-Hamilton-Ilmanen. The commutation identities of Lemma 2.1 give, explicitly,
$$\begin{aligned}
\delta H & =(\lambda-\Lambda) d \psi-(\lambda-\Lambda) d \psi=0, \\
L_{g} H & =\lambda \nabla^{2} \psi+\lambda(\lambda-\Lambda) \psi g=\lambda H, \\
\operatorname{tr}_{g} H & =-\lambda \psi+4(\lambda-\Lambda) \psi=(3 \lambda-4 \Lambda) \psi .
\end{aligned}$$
Thus $H \in S_{g}$. Expanding its norm and using (7.1) yields
$$\begin{aligned}
\|H\|_{L^{2}}^{2} & =\left[\lambda(\lambda-\Lambda)-2 \lambda(\lambda-\Lambda)+4(\lambda-\Lambda)^{2}\right]\|\psi\|_{L^{2}}^{2} \\
& =(\lambda-\Lambda)(3 \lambda-4 \Lambda)\|\psi\|_{L^{2}}^{2}>0 .
\end{aligned}$$
Equations (7.4) and (7.8) give
$$D^{2} v_{g}(H, H)=\frac{2 \Lambda-\lambda}{4 \Lambda \operatorname{Vol}_{g}(M)}\|H\|_{L^{2}}^{2}>0 .$$
Since $\nabla^{2} \psi=\frac{1}{2} \mathcal{L}_{\nabla \psi} g$, (7.5) implies
$$D^{2} v_{g}(H, H)=(\lambda-\Lambda)^{2} D^{2} v_{g}(\psi g, \psi g) .$$
Substitution of (7.9) proves (7.6). For $|t|<\|\psi\|_{\infty}^{-1}, 1+t \psi \geq 1-|t|\|\psi\|_{\infty}>0$. If $c$ denotes the positive quantity in (7.6), the second variation at this critical metric gives
$$v((1+t \psi) g)=v(g)+\frac{1}{2} c t^{2}+o\left(t^{2}\right) \quad(t \rightarrow 0) .$$
Choose $\epsilon>0$ so that the absolute value of the remainder is at most $c t^{2} / 4$ for $|t|<\epsilon$. The entropy then exceeds $v(g)$ for $0<|t|<\min \left(\epsilon,\|\psi\|_{\infty}^{-1}\right)$. In particular the conformal second variation is positive. \(\square\)

Completion of Theorem B. The first eigenfunction satisfies the hypotheses of Proposition 7.1, by (7.1) and (6.28). That proposition supplies a pure conformal destabilizing variation. \(\square\)

Corollary 7.2. For the CLW Einstein metric, the positive index of $D^{2} v_{g}$ modulo infinitesimal diffeomorphisms and scaling is at least three.

Proof. Constant rescaling of Theorem C gives two $L^{2}$-orthonormal TT eigentensors $T_{1}, T_{2}$ with eigenvalues $\mu_{i}<7 \Lambda / 6<2 \Lambda$. Let $H$ be (7.7) for a first positive scalar eigenfunction. For every smooth TT tensor $T$,
$$\langle T, H\rangle_{L^{2}}=\langle\delta T, d \psi\rangle_{L^{2}}+(\lambda-\Lambda) \int_{M} \psi \operatorname{tr}_{g} T d v_{g}=0$$
The three tensors belong to $S_{g}$ and are linearly independent. The polarized formula (7.4), together with $L_{g} T_{i}=\mu_{i} T_{i}$ and $L_{g} H=\lambda H$, gives
$$D^{2} v_{g}\left(a_{1} T_{1}+a_{2} T_{2}+b H, a_{1} T_{1}+a_{2} T_{2}+b H\right)=\frac{\left(2 \Lambda-\mu_{1}\right) a_{1}^{2}+\left(2 \Lambda-\mu_{2}\right) a_{2}^{2}+(2 \Lambda-\lambda) b^{2}\|H\|_{L^{2}}^{2}}{4 \Lambda \operatorname{Vol}_{g}(M)} .$$
It is positive for every nonzero $\left(a_{1}, a_{2}, b\right)$. By (7.5), a positive-definite subspace intersects the dif-feomorphism and scaling directions only at zero. It therefore remains three-dimensional in the quotient. \(\square\)

\section*{8. Compactly supported variations on the cone}

Let $\left(M^{4}, g\right)$ be closed, with $\operatorname{Ric}_{g}=3 g$, and let $G=d r^{2}+r^{2} g$. If $X, Y$ are vector fields on $M$ lifted independently of $r$, the connection is
$$\begin{aligned}
\nabla_{\partial_{r}}^{G} \partial_{r} & =0, \quad \nabla_{\partial_{r}}^{G} X=\nabla_{X}^{G} \partial_{r}=r^{-1} X, \\
\nabla_{X}^{G} Y & =\nabla_{X}^{g} Y-r g(X, Y) \partial_{r} .
\end{aligned}$$
These equations follow by substituting $G_{r r}=1, G_{r i}=0$ and $G_{i j}=r^{2} g_{i j}$ in the connection formula. They give
$$R_{G}\left(\partial_{r}, \cdot\right)=0, \quad R_{G}(X, Y) Z=R_{g}(X, Y) Z-g(Y, Z) X+g(X, Z) Y .$$
For lifted vectors $X, Y$,
$$\operatorname{Ric}_{G}\left(\partial_{r}, \partial_{r}\right)=0, \quad \operatorname{Ric}_{G}\left(\partial_{r}, X\right)=0, \quad \operatorname{Ric}_{G}(X, Y)=\operatorname{Ric}_{g}(X, Y)-3 g(X, Y)=0 .$$
Thus $G$ is Ricci-flat.
Proposition 8.1. Let $k$ be a nonzero smooth $T T$ eigentensor with $L_{g} k=\lambda k$. For $\varphi \in C_{c}^{\infty}((0, \infty))$, set
$$H=r^{2} \varphi(r) k, \quad H\left(\partial_{r}, \cdot\right)=0 .$$
Then $H$ is TT and
$$Q_{C}(H)=\|k\|_{L^{2}(g)}^{2} \int_{0}^{\infty}\left[r^{4}\left(\varphi^{\prime}\right)^{2}+(\lambda-6) r^{2} \varphi^{2}\right] d r$$
If $\lambda<15 / 4$, then $Q_{C}(H)<0$ for some $\varphi$. In that case the cone has infinite negative index on smooth compactly supported TT tensors.

Proof. Let $\left(\widetilde{e}_{a}\right)_{a=1}^{4}$ be a local $g$-orthonormal frame and put $e_{0}=\partial_{r}, e_{a}=r^{-1} \widetilde{e}_{a}$. At a point where $\nabla^{g} \widetilde{e}_{a}=0$, the components of $H$ and its derivatives are
$$\begin{aligned}
H_{a b} & =\varphi k_{a b}, & H_{0 a} & =H_{00}=0, \\
\left(\nabla_{0}^{G} H\right)_{a b} & =\varphi^{\prime} k_{a b}, & \left(\nabla_{c}^{G} H\right)_{a b} & =r^{-1} \varphi\left(\nabla_{c}^{g} k\right)_{a b}, \\
\left(\nabla_{c}^{G} H\right)_{0 b} & =-r^{-1} \varphi k_{c b}, & \left(\nabla_{c}^{G} H\right)_{00} & =0 .
\end{aligned}$$
The components with slots $b 0$ equal those with slots $0 b$. Consequently
$$\operatorname{tr}_{G} H=\varphi \operatorname{tr}_{g} k=0, \quad\left(\delta_{G} H\right)_{0}=r^{-1} \varphi \operatorname{tr}_{g} k=0, \quad\left(\delta_{G} H\right)_{b}=r^{-1} \varphi\left(\delta_{g} k\right)_{b}=0 .$$
Squaring all components in (8.6) gives
$$\left|\nabla^{G} H\right|_{G}^{2}=\left(\varphi^{\prime}\right)^{2}|k|_{g}^{2}+r^{-2} \varphi^{2}\left(\left|\nabla^{g} k\right|_{g}^{2}+2|k|_{g}^{2}\right) .$$
The constant-curvature-one operator satisfies
$$\sum_{i} k\left(R_{1}\left(e_{i}, X\right) Y, e_{i}\right)=g(X, Y) \operatorname{tr}_{g} k-k(X, Y)=-k(X, Y),$$
where $R_{1}(X, Y) Z=g(Y, Z) X-g(X, Z) Y$. Substitution in (8.2) gives
$$\left\langle\stackrel{\circ}{R}_{G} H, H\right\rangle_{G}=r^{-2} \varphi^{2}\left(\left\langle\stackrel{ْ}{R}_{g} k, k\right\rangle_{g}+|k|_{g}^{2}\right) .$$
The two additional squared-norm terms cancel in (1.12). Since $d v_{G}=r^{4} d r d v_{g}$ and
$$\int_{M}\left(|\nabla k|^{2}-2\left\langle\stackrel{\circ}{R}_{g} k, k\right\rangle\right) d v_{g}=(\lambda-6)\|k\|_{L^{2}}^{2}$$
we obtain (8.5).
For $\chi \in C_{c}^{\infty}(\mathbb{R})$, set
$$t=\log r, \quad \varphi(r)=r^{-3 / 2} \chi(\log r) .$$
Then $\varphi^{\prime}=r^{-5 / 2}\left(\chi^{\prime}-\frac{3}{2} \chi\right)$, so
$$\begin{aligned}
\int_{0}^{\infty} r^{4}\left(\varphi^{\prime}\right)^{2} d r & =\int_{\mathbb{R}}\left(\left(\chi^{\prime}\right)^{2}+\frac{9}{4} \chi^{2}\right) d t \\
\int_{0}^{\infty} r^{2} \varphi^{2} d r & =\int_{\mathbb{R}} \chi^{2} d t
\end{aligned}$$
The cross term integrates to zero because $\chi$ is compactly supported. Hence
$$Q_{C}(H)=\|k\|_{L^{2}}^{2} \int_{\mathbb{R}}\left[\left(\chi^{\prime}\right)^{2}+\left(\lambda-\frac{15}{4}\right) \chi^{2}\right] d t .$$
Define
$$\eta(t)= \begin{cases}\exp \left(-1 /\left(1-t^{2}\right)\right), & |t|<1, \\ 0, & |t| \geq 1 .\end{cases}$$
For $|t|<1$, every derivative of $\eta$ is a finite sum of terms $t^{a}\left(1-t^{2}\right)^{-b} \exp \left(-1 /\left(1-t^{2}\right)\right)$ with nonnegative integers $a, b$. This follows by induction and the product rule. Since $\lim _{s \rightarrow \infty} s^{b} e^{-s}=0$ for every $b$, all one-sided derivatives tend to zero at $t= \pm 1$. The zero extension is therefore smooth. Also $\eta(0)=e^{-1}>0$ and $\operatorname{supp} \eta=[-1,1]$. Set $\chi_{L}(t)=\eta(t / L)$. Then
$$\frac{\int_{\mathbb{R}}\left(\chi_{L}^{\prime}\right)^{2} d t}{\int_{\mathbb{R}} \chi_{L}^{2} d t}=L^{-2} \frac{\int_{\mathbb{R}}\left(\eta^{\prime}\right)^{2} d t}{\int_{\mathbb{R}} \eta^{2} d t} .$$
If $\lambda<15 / 4$, it suffices to choose
$$L^{2}>\frac{\int_{\mathbb{R}}\left(\eta^{\prime}\right)^{2} d t}{(15 / 4-\lambda) \int_{\mathbb{R}} \eta^{2} d t} .$$
Equations (8.13)-(8.14) then give $Q_{C}(H)<0$. For $j \geq 1$, set $\chi_{j}(t)=\chi_{L}(t-3 L j)$ and let $H_{j}$ be the associated tensor. Its support is contained in the compact annulus $e^{3 L j-L} \leq r \leq e^{3 L j+L}$. These annuli are disjoint. For every finite family of real numbers ( $a_{j}$ ),
$$Q_{C}\left(\sum_{j} a_{j} H_{j}\right)=\sum_{j} a_{j}^{2} Q_{C}\left(H_{j}\right)<0 \quad \text { if }\left(a_{j}\right) \neq 0 .$$
Disjoint support and $H_{j} \neq 0$ also give linear independence. Thus negative subspaces exist in every finite dimension. \(\square\)

Completion of Theorem C. The two bounds in (1.11) lie below 15/4. Apply Proposition 8.1 to either metric. \(\square\)

\section*{9. Quotients and the half-Weyl classification}

The quotient argument uses harmonic two-forms on a finite Riemannian covering. The classification theorems are applied after this construction.

\subsection*{9.1. Harmonic forms on positive Kähler-Einstein surfaces.}

Lemma 9.1. Let $\left(Y^{4}, g, J\right)$ be a closed connected Kähler-Einstein surface with $\operatorname{Ric}_{g}=3 g$. Then $b_{1}(Y)=0$ and $b_{2}^{+}(Y)=1$. Moreover
$$\operatorname{dim} \operatorname{ker}\left(\left.L_{g}\right|_{\mathrm{TT}}\right) \geq b_{2}^{-}(Y)=b_{2}(Y)-1 .$$
Proof. For a harmonic one-form $\alpha$,
$$0=\left\langle\Delta_{H} \alpha, \alpha\right\rangle_{L^{2}}=\|\nabla \alpha\|_{L^{2}}^{2}+3\|\alpha\|_{L^{2}}^{2} .$$
Thus $\alpha=0$, giving $b_{1}=0$ by Hodge theory. On self-dual two-forms, the Weitzenböck formula of [11, Section 2] is
$$\Delta_{2}=\nabla^{*} \nabla+\frac{\text { Scal }}{3} I-2 W^{+} .$$
For a Kähler surface, $W^{+}$has eigenvalue Scal /6 on $\mathbb{R} \Omega$ and - Scal / 12 on its orthogonal complement. These are the Kähler curvature identities of [11, Section 2]. Since $\Omega$ is parallel, the splitting $\Lambda^{+}=$ $\mathbb{R} \Omega \oplus \Omega^{\perp}$ is parallel. A harmonic self-dual form therefore has a harmonic scalar coefficient on $\mathbb{R} \Omega$, and its component $\psi$ in $\Omega^{\perp}$ satisfies
$$0=\|\nabla \psi\|_{L^{2}}^{2}+\frac{\mathrm{Scal}}{2}\|\psi\|_{L^{2}}^{2}=\|\nabla \psi\|_{L^{2}}^{2}+6\|\psi\|_{L^{2}}^{2} .$$
The scalar coefficient is constant and $\psi=0$. Hence $\mathcal{H}^{+}=\mathbb{R} \Omega$ and $b_{2}^{+}=1$. For every $\omega \in \mathcal{H}^{-}$, Proposition 3.1 and Scal = 12 give
$$\delta_{g}\left(\omega \circ_{g} \Omega\right)=0, \quad \mathcal{P}_{g}\left(\omega \circ_{g} \Omega\right)=-2\left(\omega \circ_{g} \Omega\right) .$$
Equation (3.19) then gives $L_{g}\left(\omega \circ_{g} \Omega\right)=0$. Injectivity in (3.4) proves (9.1). \(\square\)

Proposition 9.2. Let $\left(\widetilde{M}^{4}, \widetilde{g}, J\right)$ be a closed connected Kähler-Einstein surface, $\operatorname{Ric}_{\widetilde{g}}=3 \widetilde{g}$. Suppose $\sigma$ is a fixed-point-free anti-holomorphic isometric involution. Give $M=\widetilde{M} /\langle\sigma\rangle$ the quotient metric and the orientation induced by the complex orientation. Then
$$\operatorname{dim} \operatorname{ker}\left(\left.L_{g}\right|_{\mathrm{TT}}\right) \geq b_{2}(M)+1 .$$
Proof. An anti-complex linear isomorphism in complex dimension two preserves real orientation: complex conjugation has real determinant $(-1)^{2}=1$, and a complex-linear isomorphism has positive real determinant. Thus $\sigma$ preserves orientation and commutes with the Hodge star. Being an isometry, it also commutes with the Hodge Laplacian.

Let $\widetilde{\Omega}$ be the Kähler form. Anti-holomorphicity and isometry give
$$\sigma^{*} \widetilde{\Omega}=-\widetilde{\Omega} .$$
If $\omega$ is harmonic, anti-self-dual and anti-invariant, then
$$\sigma^{*}\left(\omega \circ{ }_{\tilde{g}} \widetilde{\Omega}\right)=(-\omega) \circ{ }_{\tilde{g}}(-\widetilde{\Omega})=\omega \circ{ }_{\tilde{g}} \widetilde{\Omega} .$$
It descends to a smooth tensor on $M$. The covering map is a local isometry, so trace, divergence and $L$ commute with pullback. Lemma 9.1 makes the descended tensor TT and a zero mode.

Put $b=b_{2}(M)$. We compute the dimension of the anti-invariant anti-self-dual harmonic space. By (9.2), $b_{1}=0$ on both spaces; Poincaré duality gives $b_{3}=0$ as well. Euler characteristic is multiplicative under the degree-two covering, since a finite triangulation of $M$ lifts to twice as many simplices in each degree. Thus
$$2+b_{2}(\widetilde{M})=2(2+b), \quad b_{2}(\widetilde{M})=2 b+2 .$$
By Lemma 9.1, $b_{2}^{+}(\widetilde{M})=1$, so $b_{2}^{-}(\widetilde{M})=2 b+1$. Let $\pi: \widetilde{M} \rightarrow M$ be the covering. A differential form on $M$ pulls back to an invariant form. Conversely, on an evenly covered open set, an invariant form has the same expression on both sheets; these expressions define a smooth form on $M$. Since $\pi$ is an orientation-preserving local isometry, $\pi^{*} \Delta_{g}=\Delta_{\widetilde{g}} \pi^{*}$ and $\pi^{*}\left(*_{g}\right)={ }^{*} \widetilde{g} \pi^{*}$. Pullback is injective, so these statements give an isomorphism between harmonic forms on $M$ and invariant harmonic forms on $\widetilde{M}$. Their degree-two dimension is $b$. By (9.7), the invariant self-dual harmonic space is zero. The
invariant anti-self-dual space therefore has dimension $b$. Since an involution has only eigenvalues 1 and -1, its anti-invariant anti-self-dual space has dimension
$$(2 b+1)-b=b+1 .$$
Let $\omega_{1}, \ldots, \omega_{b+1}$ be a basis of that space, and let $S_{i}$ be the descended tensors. If $\sum_{i} a_{i} S_{i}=0$, pullback gives $\left(\sum_{i} a_{i} \omega_{i}\right) \circ \widetilde{\Omega}=0$. Equation (3.4) gives $\sum_{i} a_{i} \omega_{i}=0$, so every $a_{i}=0$. This proves (9.6). \(\square\)
9.2. Application of the classification theorems. We use the following three precise classification statements. First, a simply connected closed Einstein four-manifold of positive scalar curvature and $\operatorname{det} W^{+} \geq 0$ is either anti-self-dual or globally conformally Kähler [29, Theorem 1.3]. Second, a closed Einstein metric Hermitian with respect to a complex structure is Kähler-Einstein or is homothetic to the Page or Chen-LeBrun-Weber metric [23, Theorem A]. Third, a closed oriented Einstein four-manifold with det $W^{+}>0$ is either simply connected, or has fundamental group $\mathbb{Z} / 2$ and a del Pezzo double cover with an anti-holomorphic deck involution; the conformally rescaled metric on the cover is Kähler [24, Proposition 1]. The cover need not initially be assumed Kähler-Einstein.

The positive anti-self-dual Einstein classification states that a closed simply connected Einstein four-manifold with positive scalar curvature and $W^{+}=0$ is, up to homothety and isometry, $S^{4}$ or $\mathbb{C P}^{2}$ with its Fubini-Study metric and reversed complex orientation [2, Theorem 13.30]. The statement with $W^{-}=0$ is obtained by reversing orientation.

Lemma 9.3. A closed simply connected Kähler-Einstein surface with $\mathrm{Ric}=3 g$ and $b_{2}=1$ is isometric to the normalized Fubini-Study projective plane.

Proof. By Lemma 9.1, $b_{2}^{+}=1$ and $b_{2}^{-}=0$. Thus $\chi=3$ and the signature is $\varsigma=1$. Use the endomorphism norm for $W^{ \pm}: \Lambda^{ \pm} \rightarrow \Lambda^{ \pm}$. The Chern-Gauss-Bonnet and Hirzebruch signature formulas, in the Einstein case and the curvature normalization of [2, Chapter 13], are
$$\begin{aligned}
8 \pi^{2} \chi & =\int_{M}\left(\left|W^{+}\right|^{2}+\left|W^{-}\right|^{2}+\frac{\text { Scal }^{2}}{24}\right) d v_{g} \\
12 \pi^{2} \varsigma & =\int_{M}\left(\left|W^{+}\right|^{2}-\left|W^{-}\right|^{2}\right) d v_{g}
\end{aligned}$$
Since the Kähler eigenvalues of $W^{+}$are $2,-1,-1,\left|W^{+}\right|^{2}=6=$ Scal $^{2} / 24$. Subtract twice the second identity in (9.11) from the first. This gives
$$0=8 \pi^{2} \cdot 3-24 \pi^{2} \cdot 1=\int_{M}\left(-\left|W^{+}\right|^{2}+3\left|W^{-}\right|^{2}+\frac{\mathrm{Scal}^{2}}{24}\right) d v_{g}=3 \int_{M}\left|W^{-}\right|^{2} d v_{g}$$
The integrand is continuous and nonnegative. If it were positive at one point, it would have positive integral on an open neighborhood. Therefore $W^{-}=0$. Apply the half-conformally-flat classification just stated, with reversed orientation. The sphere is excluded by $b_{2}=1$; the Einstein normalization fixes the homothety. \(\square\)

Proof of Theorem D. Let ( $\widetilde{M}, \widetilde{g}$ ) be the universal Riemannian cover. A geodesic projects to a geodesic of the complete closed manifold $M$; its lift extends for all time. The cover is therefore complete. Since $\operatorname{Ric}_{\widetilde{g}}=3 \widetilde{g}$, Myers' theorem gives $\operatorname{diam}(\widetilde{M}) \leq \pi$. Hopf-Rinow implies compactness. Each fibre of the covering is closed and discrete in $\widetilde{M}$, hence finite. Thus the cover has finite degree. The lifted orientation and the local-isometry property preserve the condition $\operatorname{det} W^{+} \geq 0$. The cover is simply connected, so Wu's theorem applies.

Suppose first that $W_{\tilde{g}}^{+}=0$. The half-conformally-flat classification gives the round sphere or the Fubini-Study projective plane as the cover. There is no nontrivial oriented quotient in either case. Indeed, $b_{1}(M)=0$ by (9.2), so $\chi(M)=2+b_{2}(M) \geq 2$. A cover of degree $d \geq 2$ by $S^{4}$ would instead give $\chi(M)=2 / d \leq 1$. A cover by $\mathbb{C P}^{2}$ would give $\chi(M)=3 / d \leq 3 / 2$. Thus the cover has degree one. The round cone is Euclidean away from the origin and $Q_{C}(H)=\int|\nabla H|^{2} \geq 0$. For the Fubini-Study cone, stability is [14, Theorem 1.3, proved in Section 5]; that theorem uses exactly the transverse compact-support condition in (1.12).

Suppose next that the universal cover is conformally Kähler. Its Kähler representative has positive scalar curvature by [23, Proposition 1]. The eigenvalues of $W_{k}^{+}$for that representative are $s_{k} / 6,-s_{k} / 12,-s_{k} / 12$, so $\operatorname{det} W_{k}^{+}=s_{k}^{3} / 864>0$. If $\widetilde{g}=f^{2} k$, then $W_{\widetilde{g}}^{+}=f^{-2} W_{k}^{+}$as endomorphisms of two-forms. Consequently
$$\operatorname{det} W_{\widetilde{g}}^{+}=f^{-6} \frac{s_{k}^{3}}{864}>0 .$$
The covering is a local orientation-preserving isometry, so this inequality descends to $M$. LeBrun's double-cover theorem now gives $\pi_{1}(M)=1$ or $\mathbb{Z} / 2$.

If $\pi_{1}(M)=1$, LeBrun's Einstein-Hermitian classification gives three cases. In the Kähler-Einstein case, Lemma 9.1 supplies $b_{2}(M)-1$ TT zero eigentensors. If $b_{2}(M)=1$, Lemma 9.3 gives Fubini-Study, already treated. Otherwise $b_{2}(M)-1 \geq 1$, and the zero eigentensors give (1.15). In the Page and Chen-LeBrun-Weber cases, $b_{2}(M)-1$ is respectively 1 and 2, and Theorem C gives the same assertion.

If $\pi_{1}(M)=\mathbb{Z} / 2$, apply the Einstein-Hermitian classification on the double cover. The cover cannot be Chen-LeBrun-Weber, since its Euler characteristic is 5, which cannot be twice an integer. Nor can it be the Page manifold: [24, Lemma 1] states that no nonsimply connected smooth oriented four-manifold has a covering space homeomorphic to $\mathbb{C P}^{2} \# \overline{\mathbb{C P}}^{2}$. All of its hypotheses hold here. The cover is consequently Kähler-Einstein for the complex structure supplied by LeBrun's double-cover theorem. If its other Kähler representative is $\widehat{k}=u^{2} \widetilde{g}$, its Kähler form is $u^{2} \widetilde{\Omega}$. Therefore
$$0=d\left(u^{2} \widetilde{\Omega}\right)=2 u d u \wedge \widetilde{\Omega}$$
In a unitary orthonormal coframe, $\widetilde{\Omega}=e^{12}+e^{34}$. For $\alpha=\sum_{i} a_{i} e^{i}$,
$$\alpha \wedge \widetilde{\Omega}=a_{1} e^{134}+a_{2} e^{234}+a_{3} e^{123}+a_{4} e^{124} .$$
The four three-forms are independent. Thus $d u=0$ and $u$ is constant. The deck involution is therefore anti-holomorphic and isometric for the Kähler-Einstein metric itself. Proposition 9.2 proves (1.16), with $b_{2}(M)+1 \geq 1$. It also gives (1.15).

Every case other than round or Fubini-Study has a TT eigenvalue below $7 / 2<15 / 4$. Proposition 8.1 gives instability and infinite compactly supported TT index. This proves both implications of the classification. \(\square\)

\section*{Appendix A. An algebraic proof of the scalar estimate}

The notation $\mathfrak{p}, D_{a}, I, J, V, K$ is that of Section 6. We prove the required strict inequality by polynomial identities at the root $a_{*}$. All polynomials and coefficients used in the proof are specified below.
A.1. Rational moment formulas. For $a>1$, put
$$\begin{aligned}
\ell & =a+1, & & B_{0}=a^{5}+7 a^{4}+6 a^{3}+2 a^{2}-5 a-3, \\
C & =4\left(1-a^{3}\right), & & B_{1}=B_{0}+a C, \quad B_{2}=B_{0}+\ell C .
\end{aligned}$$
Thus $s_{a}(t)=\left(12 / D_{a}\right)\left(B_{0}+C t\right)$. In particular $B_{0}, B_{1}, B_{2}>0$, since $D_{a}>0$ and $s_{a}>0$ on $[0, a+1]$. Set
$$\mathrm{V}=\left(12 / D_{a}\right)^{4} V, \quad \mathrm{I}=\left(12 / D_{a}\right)^{6} I, \quad \mathrm{~J}=\left(12 / D_{a}\right)^{4} J, \quad \mathrm{~K}=\left(12 / D_{a}\right)^{2} K .$$
For every $a>1$, define $V(a), I(a), J(a), K(a)$ by (6.21)-(6.24) with $s=s_{a}$. These positive rational integrals are defined independently of the existence of an Einstein metric at that parameter. The normalized moments in (A.2) replace $s_{a}(t)$ by $B_{0}+C t$. Their homogeneity degrees are respectively -4, -6, -4, -2; hence $2 J V /(I K)=2 \mathrm{JV} /(\mathrm{IK})$. Only at $a=a_{*}$ is this quotient related to the Einstein constant by (6.18).

For $L>0, b>0$ and $b+c L>0$, define $F_{j, p}(L ; b, c)=\int_{0}^{L} t^{j}(b+c t)^{-p} d t$. For the five pairs used below one has
$$\begin{array}{ll}
F_{0,2}=\frac{L}{b(b+c L)}, & F_{2,4}=\frac{L^{3}}{3 b(b+c L)^{3}}, \\
F_{1,4}=\frac{L^{2}(3 b+c L)}{6 b^{2}(b+c L)^{3}}, & F_{3,6}=\frac{L^{4}(5 b+c L)}{20 b^{2}(b+c L)^{5}}, \\
F_{1,6}=\frac{L^{2}\left(10 b^{3}+10 b^{2} c L+5 b c^{2} L^{2}+c^{3} L^{3}\right)}{20 b^{4}(b+c L)^{5}} . &
\end{array}$$
All arguments on the right are $(L ; b, c)$. To prove these formulas, put $y=t /(b+c t)$ and $Y=L /(b+c L)$. The derivative is $d y / d t=b /(b+c t)^{2}>0$, so the substitution is one-to-one on $[0, L]$. Also $1-c y=b /(b+c t)>0$. Consequently
$$t=\frac{b y}{1-c y}, \quad d t=\frac{b d y}{(1-c y)^{2}}, \quad F_{j, p}(L ; b, c)=b^{j-p+1} \int_{0}^{Y} y^{j}(1-c y)^{p-j-2} d y .$$
The exponents $p-j-2$ are respectively 0, 0, 1, 1, 3. For the last formula the integral is $b^{-4}\left(Y^{2} / 2-\right.$ $\left.c Y^{3}+3 c^{2} Y^{4} / 4-c^{3} Y^{5} / 5\right)$. Substitution of $Y$ proves (A.3); the other four formulas follow by integrating $y^{j}$ or $y^{j}(1-c y)$.

Let $T_{L}=\left\{x_{1}, x_{2} \geq 0: x_{1}+x_{2} \leq L\right\}$. Except for boundaries of measure zero, $P_{a}$ is obtained from $T_{a+1}$ by deleting the two translates $(a, 0)+T_{1}$ and $(0, a)+T_{1}$. They are disjoint because $a>1$. On either deleted triangle, with translated coordinates $u, v$ and $z=u+v$, the integral of $\left(x_{1}-x_{2}\right)^{2}$ along the slice is
$$\int_{0}^{z}(a+2 u-z)^{2} d u=a^{2} z+\frac{z^{3}}{3}$$
The sign of $a$ is reversed on the other triangle, with the same squared integral. Thus
$$\begin{aligned}
& \mathrm{V}=F_{1,4}\left(\ell ; B_{0}, C\right)-2 F_{1,4}\left(1 ; B_{1}, C\right) \\
& \mathrm{I}=\frac{1}{3} F_{3,6}\left(\ell ; B_{0}, C\right)-2 a^{2} F_{1,6}\left(1 ; B_{1}, C\right)-\frac{2}{3} F_{3,6}\left(1 ; B_{1}, C\right), \\
& \mathrm{J}=2 F_{2,4}\left(\ell ; B_{0}, C\right)-8 a F_{1,4}\left(1 ; B_{1}, C\right)+\frac{(a-1)^{3}}{3 B_{2}^{4}}, \\
& \mathrm{~K}=2 F_{0,2}\left(\ell ; B_{0}, C\right)+\frac{a-1}{B_{2}^{2}} .
\end{aligned}$$
For the third line, subtract the integrands on the two changed pairs of coordinate facets: $t^{2}-(2 a-t)^{2}=$ $4 a(t-a)$ for $a \leq t \leq a+1$. The remaining facet is the diagonal, whose moment is (6.20). The fourth line is the sum of the four coordinate facets and the diagonal facet.

Define four polynomials in $a$ by
$$\begin{aligned}
v=\ell^{2}( & \left.3 B_{0}+C \ell\right) B_{1}^{2}-2\left(3 B_{1}+C\right) B_{0}^{2}, \\
i= & \ell^{4}\left(5 B_{0}+C \ell\right) B_{1}^{4}-6 a^{2} B_{0}^{2}\left(10 B_{1}^{3}+10 B_{1}^{2} C+5 B_{1} C^{2}+C^{3}\right) \\
& \quad-2 B_{0}^{2} B_{1}^{2}\left(5 B_{1}+C\right), \\
j= & 2 \ell^{3} B_{1}^{2} B_{2}-4 a B_{0}\left(3 B_{1}+C\right) B_{2}+(a-1)^{3} B_{0} B_{1}^{2}, \\
k= & 2 \ell B_{2}+(a-1) B_{0} .
\end{aligned}$$
Substitution of (A.3) into (A.6), over a common denominator in each line, gives
$$\mathrm{V}=\frac{v}{6 B_{0}^{2} B_{1}^{2} B_{2}^{3}}, \quad \mathrm{I}=\frac{i}{60 B_{0}^{2} B_{1}^{4} B_{2}^{5}}, \quad \mathrm{~J}=\frac{j}{3 B_{0} B_{1}^{2} B_{2}^{4}}, \quad \mathrm{~K}=\frac{k}{B_{0} B_{2}^{2}} .$$
The integrand defining I is positive on an open subset of the polygon, and the integrand defining K is positive on every open facet. Hence $\mathrm{I}, \mathrm{K}>0$. All factors in their displayed denominators are positive, so $i, k>0$. Define
$$\mathfrak{F}(a)=11853 i(a) k(a)-20000 v(a) j(a) .$$

Equations (A.2) and (A.8) give the exact identity
$$3951 I K-2000 J V=\left(\frac{D_{a}}{12}\right)^{8} \frac{\mathfrak{F}(a)}{180 B_{0}^{3} B_{1}^{4} B_{2}^{7}} .$$
Its prefactor is positive for every $a>1$.

\section*{A.2. Polynomial division and positive translate.}

Lemma A.1. Let $\mathfrak{p}$ be (6.9). There are polynomials $Q, R \in \mathbb{Z}[a]$, of degrees 25 and 9, such that
$$\mathfrak{F}=\mathfrak{p} Q+R .$$
Write $Q=\sum_{j=0}^{25} q_{j} a^{j}$ and $R=\sum_{j=0}^{9} r_{j} a^{j}$. Their coefficients are given in Table 1. Moreover
$$118^{9} R\left(\frac{231+z}{118}\right)=\sum_{j=0}^{9} c_{j} z^{j}, \quad c_{j}>0,$$
with the coefficients in Table 2.
Proof. For an integer polynomial $A$, denote the coefficient of $a^{j}$ by $\left[a^{j}\right] A$, and extend every coefficient sequence by zero outside its stated range. Products are evaluated by
$$\left[a^{j}\right](A B)=\sum_{r=0}^{j}\left(\left[a^{r}\right] A\right)\left(\left[a^{j-r}\right] B\right) .$$
Using (A.1) and (A.7) in this formula gives, for $0 \leq j \leq 35$,
$$\left[a^{j}\right] \mathfrak{F}=r_{j}+\sum_{r=0}^{10} p_{r} q_{j-r}, \quad\left(p_{0}, \ldots, p_{10}\right)=(-6,-7,21,20,0,-42,-34,-12,6,5,1) .$$
Here $q_{j}, r_{j}$ are the integers displayed in Table 1. To compute them successively from the stated factors, put $f_{j}=\left[a^{j}\right] \mathfrak{F}$ and set
$$\begin{aligned}
q_{j} & =f_{j+10}-\sum_{r=0}^{9} p_{r} q_{j+10-r} \quad(j=25,24, \ldots, 0), \\
r_{j} & =f_{j}-\sum_{r=0}^{10} p_{r} q_{j-r} \quad(0 \leq j \leq 9) .
\end{aligned}$$
Thus (A.14) is a coefficient identity in $\mathbb{Z}[a]$, proving (A.11). For instance, the coefficients in degrees 35 and 34 are -2205 $=q_{25}$ and $276759=q_{24}+5 q_{25}=287784-11025$.

The binomial theorem gives, for each $0 \leq j \leq 9$,
$$c_{j}=\sum_{k=j}^{9}\binom{k}{j} r_{k} 231^{k-j} 118^{9-k} .$$
This sum yields the ten integers of Table 2. Every displayed integer is positive. Formula (A.16) proves (A.12) and its sign assertion. \(\square\)

Proposition A.2. At the root $a_{*}$ in Lemma 6.1,
$$3951 I\left(a_{*}\right) K\left(a_{*}\right)-2000 J\left(a_{*}\right) V\left(a_{*}\right)>0 .$$
Proof. Put $z_{*}=118 a_{*}-231$. By (6.10), $z_{*}>0$. Since $\mathfrak{p}\left(a_{*}\right)=0$, Lemma A. 1 gives
$$\mathfrak{F}\left(a_{*}\right)=R\left(a_{*}\right)=118^{-9} \sum_{j=0}^{9} c_{j} z_{*}^{j} \geq 118^{-9} c_{0}>0 .$$
Every other factor on the right of (A.10) is positive. That identity proves (A.17). \(\square\)

\begin{table}
\captionsetup{labelformat=empty}
\caption{Table 1. Coefficients for $\mathfrak{F}=\mathfrak{p Q}+R$. The remainder coefficients with index greater than 9 are zero.}
\begin{tabular}[t]{|l|l|l|l|l|}
\hline $j$ & $q_{j}$ & $r_{j}$ & $j$ & $q_{j}$ \\
\hline 0 & -1588589253209596 & -9531535506952461 & 13 & 476232516 \\
\hline 1 & 740732446020673 & -6675730081712563 & 14 & -148476658 \\
\hline 2 & -277859321196300 & 36878345425165852 & 15 & -50976437 \\
\hline 3 & 86595295758476 & 14790960069851972 & 16 & -655340412 \\
\hline 4 & -21232530012668 & -8500831174448830 & 17 & -315842653 \\
\hline 5 & 2961425110884 & -63112921934493674 & 18 & -1962508 \\
\hline 6 & 707881307862 & -24162316927159204 & 19 & 223569796 \\
\hline 7 & -810603807347 & -5 185708498471564 & 20 & 208601668 \\
\hline 8 & 430796582928 & 12532924481239783 & 21 & 107349204 \\
\hline 9 & -175037545095 & 2221544641356161 & 22 & 32506234 \\
\hline 10 & 58852065720 & 0 & 23 & 5004455 \\
\hline 11 & -16306269728 & 0 & 24 & 287784 \\
\hline 12 & 3391655536 & 0 & 25 & -2205 \\
\hline
\end{tabular}
\end{table}

\begin{table}
\captionsetup{labelformat=empty}
\caption{Table 2. Positive coefficients of $118^{9} R((231+z) / 118)$.}
\begin{tabular}[t]{|l|l|}
\hline $j$ & $c_{j}$ \\
\hline 0 & 1453244795845348307811581388481233 \\
\hline 1 & 171655433886954619973704509793399625 \\
\hline 2 & 4874552333819787686694611996698660 \\
\hline 3 & 59174508513273196527776438138516 \\
\hline 4 & 401626856903820450846877488926 \\
\hline 5 & 1669697462701839922689345982 \\
\hline 6 & 4353382536789351507350996 \\
\hline 7 & 6928352208810973839332 \\
\hline 8 & 6097476398165753113 \\
\hline 9 & 2221544641356161 \\
\hline
\end{tabular}
\end{table}

\section*{Appendix B. Operator normalizations}

The following identities relate the conventions used in the proof. For Ric $_{g}=3 g$ on a four-manifold,
$$\begin{aligned}
L_{g} & =\nabla^{*} \nabla+6 I-2 \stackrel{\circ}{R}_{g}, \\
\mathcal{E}_{g} & =L_{g}-6 I, \\
L_{\mathrm{BO}} & =\frac{1}{2} \mathcal{E}_{g}, \\
\mathcal{P}_{g} & =\frac{1}{2} L_{g}-2 I-\frac{2}{3} \mathcal{K}_{g} \delta_{g}, \\
\mathcal{J}_{g}(T) & =\left\langle L_{g} T, T\right\rangle_{L^{2}}-\frac{4}{3}\left\|\delta_{g} T\right\|_{L^{2}}^{2} .
\end{aligned}$$
On TT tensors, $\mathcal{P}_{g}=\frac{1}{2} L_{g}-2 I$. The three full-Lichnerowicz thresholds used in this paper are

\begin{tabular}[t]{|l|l|}
\hline property or variational range & threshold for $L_{g}$ \\
\hline negative Einstein-operator mode & $\lambda<6$ \\
\hline shifted divergence-penalty identity & $\tau \leq 4$ \\
\hline negative separated cone variation & $\lambda<15 / 4$. \\
\hline
\end{tabular}
The value $7 / 2$ is a bound obtained from $\rho<2$, not one of the operator thresholds. The proof of Theorem C does not compute an eigenvalue exactly, and does not require negativity of $L_{g}$ itself.

The scalar and tensor conclusions use different eigenvalue notation. For Ric $_{g}=\Lambda g$, the bounds for the CLW metric are
$$\lambda_{1}^{\mathrm{sc}}(g)<\frac{1951}{1000} \Lambda<2 \Lambda, \quad \lambda_{2}^{\mathrm{TT}}(g)<\frac{7}{6} \Lambda<\frac{5}{4} \Lambda .$$
The final tensor threshold is the five-dimensional cone threshold under the constant rescaling to Einstein constant 3. The divergence-free conformal tensor in (7.7) is not TT: its trace is $(3 \lambda-4 \Lambda) \psi \neq 0$.

\section*{References}
\begin{itemize}
\item[] [1] V. Apostolov and G. Maschler, Conformally Kähler, Einstein-Maxwell geometry, J. Eur. Math. Soc. 21 (2019), no. 5, 1319-1360. arXiv:1512.06391v1. Equation numbers cited here refer to the preprint.
\item[] [2] A. L. Besse, Einstein manifolds, Ergebnisse der Mathematik und ihrer Grenzgebiete (3), vol. 10, Springer-Verlag, Berlin, 1987.
\item[] [3] O. Biquard and T. Ozuch, Instability of conformally Kähler, Einstein metrics, J. Differential Geom. 133 (2026), no. 3, 335-346; arXiv:2310.10109v3. Numbered citations refer to version 3.
\item[] [4] O. Biquard and Y. Rollin, Wormholes in ACH Einstein manifolds, Trans. Amer. Math. Soc. 361 (2009), no. 4, 2021-2046; arXiv:math/0609558v4.
\item[] [5] H.-D. Cao, R. S. Hamilton and T. Ilmanen, Gaussian densities and stability for some Ricci solitons, arXiv:math/0404165, 2004.
\item[] [6] H.-D. Cao and M. Zhu, On second variation of Perelman's Ricci shrinker entropy, Math. Ann. 353 (2012), no. 3, 747-763; arXiv:1008.0842v5.
\item[] [7] G. Catino and D. Dameno, Conformal Kähler rigidity of Einstein four-manifolds, arXiv:2607.21538v1, 23 July 2026.
\item[] [8] X. Chen, C. LeBrun and B. Weber, On conformally Kähler, Einstein manifolds, J. Amer. Math. Soc. 21 (2008), no. 4, 1137-1168; arXiv:0705.0710v2. Numbered citations refer to version 2.
\item[] [9] E. Delay, Conformal Laplacian on symmetric 2-tensors, Manuscripta Math. 174 (2024), no. 1-2, 73-86.
\item[] [10] E. Delay, Two remarkable differential operators acting on symmetric 2-tensors, lecture slides, Lichnerowicz conference, Institut Henri Poincaré, 13 June 2025, 69 pp.; author's conference slides.
\item[] [11] A. Derdziński, Self-dual Kähler manifolds and Einstein manifolds of dimension four, Compositio Math. 49 (1983), no. 3, 405-433; NUMDAM.
\item[] [12] S. K. Donaldson, Interior estimates for solutions of Abreu's equation, Collect. Math. 56 (2005), no. 2, 103-142; arXiv:math/0407486.
\item[] [13] P. B. Gilkey, Invariance theory, the heat equation, and the Atiyah-Singer index theorem, Mathematics Lecture Series, vol. 11, Publish or Perish, Wilmington, DE, 1984; Sections 1.3 and 1.6. Electronic edition.
\item[] [14] S. Hall, R. Haslhofer and M. Siepmann, The stability inequality for Ricci-flat cones, J. Geom. Anal. 24 (2014), no. 1, 472-494. arXiv:1111.4981v1, 21 November 2011.
\item[] [15] S. J. Hall and T. Murphy, On the spectrum of the Page and the Chen-LeBrun-Weber metrics, Ann. Global Anal. Geom. 46 (2014), 87-101.
\item[] [16] S. J. Hall and T. Murphy, Erratum to: On the spectrum of the Page and the Chen-LeBrun-Weber metrics, Ann. Global Anal. Geom. 47 (2015), 223.
\item[] [17] S. J. Hall and T. Murphy, Numerical approximations to extremal toric Kähler metrics with arbitrary Kähler class, Proc. Edinb. Math. Soc. (2) 60 (2017), no. 4, 893-910; arXiv:1407.1272v2. Numbered citations, including Conjecture 5.3, refer to version 2.
\item[] [18] S. J. Hall and T. Murphy, Bounding the first invariant eigenvalue of toric Kähler manifolds, Math. Res. Lett. 24 (2017), no. 1, 67-81; arXiv:1505.01075.
\item[] [19] R. A. Hennigar, H. K. Kunduri, K. T. B. Sievers and Y. Wang, Spectrum of the Laplacian on the Page metric, J. Phys. A: Math. Theor. 58 (2025), no. 40, 405204; arXiv:2412.19879v1.
\item[] [20] N. Koiso, A decomposition of the space $\mathcal{M}$ of Riemannian metrics on a manifold, Osaka J. Math. 16 (1979), no. 2, 423-429.
\item[] [21] K. Kröncke, Stable and unstable Einstein warped products, Trans. Amer. Math. Soc. 369 (2017), no. 9, 6537-6563. arXiv:1507.01782v2.
\item[] [22] K. Kröncke and Á. Szabó, Optimal coordinates for Ricci-flat conifolds, Calc. Var. Partial Differential Equations 63 (2024), no. 7, Paper No. 188, 41 pp.; arXiv:2203.01711v1.
\item[] [23] C. LeBrun, On Einstein, Hermitian 4-manifolds, J. Differential Geom. 90 (2012), no. 2, 277-302. arXiv:1010.0238.
\item[] [24] C. LeBrun, Einstein metrics, conformal curvature, and anti-holomorphic involutions, Ann. Math. Québec 45 (2021), 391-405. arXiv:2007.01180.
\item[] [25] A. Nifa, Negative Lichnerowicz modes on Einstein warped products and spheres, preprint, 2026, 21 pp. DOI: 10.5281/zenodo.22681023.
\item[] [26] M. Obata, Certain conditions for a Riemannian manifold to be isometric with a sphere, J. Math. Soc. Japan 14 (1962), 333-340.
\item[] [27] D. N. Page, A compact rotating gravitational instanton, Phys. Lett. B 79 (1978), no. 3, 235-238.
\item[] [28] P. Schwahn and U. Semmelmann, Einstein metrics, their moduli spaces and stability, arXiv:2507.18463v3, 2026.
\item[] [29] P. Wu, Einstein four-manifolds with self-dual Weyl curvature of nonnegative determinant, Int. Math. Res. Not. IMRN 2021 (2021), no. 2, 1043-1054. arXiv:1903.11818v2.
\end{itemize}

Toulouse, France
Email address: nifa.anass@gmail.com