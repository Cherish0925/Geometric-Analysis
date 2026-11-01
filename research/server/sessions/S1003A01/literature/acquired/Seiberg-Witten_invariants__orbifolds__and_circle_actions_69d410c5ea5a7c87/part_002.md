---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: Seiberg-Witten invariants, orbifolds, and circle actions]

Two of the cross terms in equation (28) are zero as follows. First, since $\nabla_{\mathrm{T}} \eta=0$ we have
$$\begin{aligned}
2 \int_{X} \operatorname{Re}\left\langle\sigma(\eta) \boldsymbol{\nabla}_{\mathrm{T}} \psi, D^{+} \psi\right\rangle & =\int_{X}\left\langle\sigma(\eta) \boldsymbol{\nabla}_{\mathrm{T}} \psi, D^{+} \psi\right\rangle+\left\langle D^{+} \psi, \sigma(\eta) \boldsymbol{\nabla}_{\mathrm{T}} \psi\right\rangle \\
& =\int_{X}\left\langle\psi, \sigma(\eta) \boldsymbol{\nabla}_{\mathrm{T}}\left(D^{+} \psi\right)\right\rangle+\left\langle\psi, D^{-}\left(\sigma(\eta) \boldsymbol{\nabla}_{\mathrm{T}} \psi\right)\right\rangle \\
& =\int_{X}\left\langle\psi,\left\{\sigma(\eta) \boldsymbol{\nabla}_{\mathrm{T}}, D\right\} \psi\right\rangle
\end{aligned}$$
But by equations (16), (17), and (25),
$$\left\{\sigma(\eta) \boldsymbol{\nabla}_{\mathrm{T}}, D\right\}=\frac{1}{2} \eta \wedge \iota_{\mathrm{T}} F_{A}=0 .$$
Similarly, we can use the fact that $f \eta$ and $c$ are both self-adjoint to show
$$\begin{aligned}
2 \int_{X} \operatorname{Re}\langle\sigma(f \eta) \Psi, \sigma(c) \Psi\rangle & =\int_{X}\langle(\sigma(c) \sigma(f \eta)+\sigma(f \eta) \sigma(c) \Psi, \Psi\rangle \\
& =-2 \int_{X}\langle c, f \eta\rangle|\Psi|^{2}=0 .
\end{aligned}$$

The remaining two cross terms in equation (28) are analyzed in the following lemma.
Lemma 22. In the situation above,
$$\int_{X} \operatorname{Re}\left\langle\sigma(\eta) \boldsymbol{\nabla}_{\mathrm{T}} \psi, \sigma(c) \Psi\right\rangle+\operatorname{Re}\left\langle f \sigma(\eta) \Psi, D^{+} \psi\right\rangle=\int_{X}\left|\iota_{\mathrm{T}} d a\right|^{2} .$$
Proof. Let $\left\{\eta=e^{0}, e^{1}, e^{2}, e^{3}\right\}$ be a local coframe where $e^{1}, e^{2}, e^{3}$ are pulled back from the base. First we take the adjoints of both terms on the left hand side of equation (29).

Applying the adjoint of $\sigma(\eta) \boldsymbol{\nabla}_{\mathrm{T}}$ in the first term of equation (29) gives
$$\begin{aligned}
\sigma(\eta) \nabla_{\mathrm{T}}(\sigma(c) \Psi) & =\sum_{i=1}^{3} \sigma(\eta) \sigma\left(\nabla_{\mathrm{T}}\left(c_{i} e^{i}\right)\right) \Psi+\sigma(\eta) \sigma(c)\left(\nabla_{\mathrm{T}} \Psi\right) \\
& =\sum_{i=1}^{3} \sigma(\eta) \sigma\left(\nabla_{\mathrm{T}}\left(c_{i} e^{i}\right)\right) \Psi \\
& =\sum_{i=1}^{3} \sigma\left(\left(\mathrm{~T} c_{i}\right) \eta \wedge e^{i}\right) \Psi+\sigma(\eta) \sigma\left(c_{i} \nabla_{\mathrm{T}}\left(e^{i}\right)\right) \Psi \\
& =\sum_{i=1}^{3} \sigma\left(\left(\mathrm{~T} c_{i}\right) \eta \wedge e^{i}\right) \Psi
\end{aligned}$$
We used equation (1) in the first line, and (23) in the second. We also used the definition of ∇ from equation (3).

Similarly, we take the adjoint of $D$ in the second term of equation (29) to find
$$D(f \sigma(\eta) \Psi)=\sigma(d f \wedge \eta) \Psi+\sigma(f \eta) D \Psi=\sigma(d f \wedge \eta) \Psi .$$

Next we show that the sum of the right hand sides of equations (30) and (31) is equal to
$$\sigma\left(\eta \wedge \iota_{\mathrm{T}}(d a)\right) \Psi .$$
First, note that for $i=0,1,2,3$,
$$\iota_{T} d \eta=0 \quad \text { and } \quad \iota_{\mathrm{T}} d e^{i}=0 .$$
This holds for $e^{0}=\eta$ since $d \eta$ is the curvature of a principal orbifold circle bundle so is pulled back from $Y$; it holds for the remaining $i$ since $e^{1}, e^{2}, e^{3}$ are pulled back from $Y$. Hence,
$$\begin{aligned}
\eta \wedge \iota_{\mathrm{T}}(d a) & =\eta \wedge \iota_{\mathrm{T}}(d(f \eta+c)) \\
& =\eta \wedge \iota_{\mathrm{T}}\left((d f \wedge \eta+f d \eta)+\sum_{i=1}^{3}\left(d c_{i} \wedge e^{i}+c_{i} \wedge d e^{i}\right)\right) \\
& =d f \wedge \eta+\sum_{i=1}^{3}\left(\mathrm{~T} c_{i}\right) \eta \wedge e^{i}
\end{aligned}$$

Combining equations (30), (31), and (33) and projecting onto the self-dual 2-forms we get:
$$\int_{X} \operatorname{Re}\left\langle\sigma(\eta) \nabla_{\mathrm{T}} \psi, \sigma(c) \Psi\right\rangle+\operatorname{Re}\left\langle f \sigma(\eta) \Psi, D^{+} \psi\right\rangle=\int_{X} \operatorname{Re}\left\langle\psi,\left(\eta \wedge \iota_{\mathrm{T}} d a\right)^{+} \Psi\right\rangle$$
Using equation (26), we can reduce further
$$\begin{aligned}
\int_{X} \operatorname{Re}\left\langle\psi,\left(\eta \wedge \iota_{\mathrm{T}} d a\right)^{+} \Psi\right\rangle & =\int_{X} \frac{1}{2}\left\langle\psi,\left(\eta \wedge \iota_{\mathrm{T}} d a\right)^{+} \Psi\right\rangle+\frac{1}{2}\left\langle\left(\eta \wedge \iota_{\mathrm{T}} d a\right)^{+} \Psi, \psi\right\rangle \\
& =\int_{X} 2\left\langle\left(\eta \wedge \iota_{\mathrm{T}} d a\right)^{+}, q(\Psi, \psi)+q(\psi, \Psi)\right\rangle \\
& =\int_{X} 2\left\langle\left(\eta \wedge \iota_{\mathrm{T}} d a\right), d^{+} a\right\rangle \\
& =\int_{X}\left|\iota_{\mathrm{T}} d a\right|^{2}+\frac{1}{2} \int_{X} \mathbf{i} d a \wedge \mathbf{i} d a .
\end{aligned}$$
The last equality is the same calculation as in equation (19). \(\square\)

Combining equations (28-29), gives the sum of non-negative terms. Hence we conclude that the following terms are identically zero:
$$\begin{aligned}
\nabla_{\mathrm{T}} \psi+\frac{1}{2} f \Psi & =0, \\
D^{+} \psi+\frac{1}{2} \sigma(c) \Psi & =0, \\
\iota_{\mathrm{T}} d a & =0 .
\end{aligned}$$

Notice that equation (36) is equivalent to
$$\nabla_{T} a=d f .$$

We investigate equation (34) more carefully in the next lemma.
Lemma 23.
$$\int_{X}\left|\nabla_{\mathrm{T}} \psi+\frac{1}{2} f \Psi\right|^{2}=\int_{X}\left|\nabla_{\mathrm{T}} \psi\right|^{2}+\frac{1}{4} f^{2}|\Psi|^{2}+2|d f|^{2} .$$

Since $f=\iota_{\mathrm{T}} a$ and $\Psi \neq 0$ almost everywhere, we conclude from this lemma that
$$\begin{aligned}
\nabla_{\mathrm{T}} \psi & =0, \\
\iota_{\mathrm{T}} a & =0 .
\end{aligned}$$

Equation (38) implies that the spinor is circle invariant while equations (36) and (39) imply that $a$ is pulled back from $Y$. These two facts together imply that $(a, \psi)$ is pulled back from some $\left(a_{0}, \psi_{0}\right)$ on $Y$. Equation (35) shows that $\left(a_{0}, \psi_{0}\right)$ satisfies the last equation of $\mathcal{T}_{\mathrm{S}_{0}}$. It is easy to verify that $\left(a_{0}, \psi_{0}\right)$ satisfies the other two equations of $\mathcal{T}_{\mathrm{S}_{0}}$. Hence $(a, \psi)$ is in $\pi^{*}\left(\operatorname{ker} \mathcal{T}_{\mathrm{S}_{0}}\right)$ and this completes the proof of Theorem B.

Proof of Lemma 23: We must show that the cross term satisfies
$$\int_{X} \operatorname{Re}\left\langle\boldsymbol{\nabla}_{\mathrm{T}} \psi, f \Psi\right\rangle=\int_{X} 2|d f|^{2} .$$

Integrating by parts and noting that $\boldsymbol{\nabla}_{\mathrm{T}} \Psi=0$,
$$\int_{X} \operatorname{Re}\left\langle\boldsymbol{\nabla}_{\mathrm{T}} \psi, f \Psi\right\rangle=\int_{X} \operatorname{Re}\left\langle\psi,\left(-\nabla_{\mathrm{T}} f\right) \Psi\right\rangle .$$
Pulling out the imaginary valued function $\nabla_{\mathrm{T}} f$, using equation (26), and integrating by parts again,
$$\begin{aligned}
\int_{X} \operatorname{Re}\left\langle\psi,\left(-\nabla_{\mathrm{T}} f\right) \Psi\right\rangle & =-2 \int_{X}\left\langle\nabla_{\mathrm{T}} f, d^{*} a\right\rangle \\
& =2 \int_{X}\left\langle f, \nabla_{\mathrm{T}} d^{*} a\right\rangle .
\end{aligned}$$

The results follows once we show $\nabla_{\mathrm{T}} d^{*} a=\Delta f$. We first calculate $d^{*} a$ at a point $p \in X$. Then
$$d^{*} a=-\sum_{i=0}^{3} \iota_{e_{i}} \nabla^{L . C .} a=-\sum_{i=0}^{3}\left\langle\nabla_{e_{i}}^{L . C .} a, e^{i}\right\rangle .$$

Differentiating this with respect to $\nabla_{\mathrm{T}}$,
$$\begin{aligned}
\nabla_{\mathrm{T}} d^{*} a & =-\sum_{i=0}^{3} \nabla_{\mathrm{T}}\left\langle\nabla_{e_{i}}^{L . C .} a, e^{i}\right\rangle \\
& =-\sum_{i=0}^{3}\left\langle\nabla_{\mathrm{T}} \nabla_{e_{i}}^{L . C .} a, e^{i}\right\rangle .
\end{aligned}$$

Next we will show using the connection matrices (11) and (12), and equation (14) that
$$\sum_{i=0}^{3}\left\langle\left[\nabla_{\mathrm{T}}, \nabla_{e_{i}}^{L . C .}\right] a, e^{i}\right\rangle=0 .$$
By setting $a=\sum a_{k} e^{k}$ and using the fact that $\nabla_{\mathrm{T}} e^{i}=0$,
$$\begin{aligned}
\sum_{i=0}^{3}\left\langle\left[\nabla_{\mathrm{T}}, \nabla_{e_{i}}^{L . C .}\right] a, e^{i}\right\rangle= & \sum_{i=0}^{3}\left\langle\nabla_{\mathrm{T}}\left(\left(e_{i} \cdot a_{k}\right) e^{k}+a_{k} \nabla_{e_{i}}^{L . C .} e^{k}\right)-\nabla_{e_{i}}^{L . C .}\left(\left(\mathrm{T} \cdot a_{k}\right) e^{k}\right), e^{i}\right\rangle \\
= & \sum_{i=0}^{3} \mathrm{~T} \cdot e_{i} \cdot a_{i}+\left(\mathrm{T} \cdot a_{k}\right)\left\langle\nabla_{e_{i}}^{L . C .} e^{k}, e^{i}\right\rangle+a_{k}\left\langle\nabla_{\mathrm{T}} \nabla_{e_{i}}^{L . C .} e^{k}, e^{i}\right\rangle \\
& -e_{i} \cdot \mathrm{~T} \cdot a_{i}-\left(\mathrm{T} \cdot a_{k}\right)\left\langle\nabla_{e_{i}}^{L . C .} e^{k}, e^{i}\right\rangle .
\end{aligned}$$
The first and fourth term cancel because $\left[\mathrm{T}, e_{i}\right]=0$ by equation (14). The second and last term also cancel. The third term is equal to
$$a_{k} \mathrm{~T} \cdot\left\langle\nabla_{e_{i}}^{L . C .} e^{k}, e^{i}\right\rangle$$
because $\nabla_{T}$ is compatible with the metric and $\nabla_{\mathrm{T}} e^{i}=0$. But
$$\sum_{i=0}^{3}\left\langle\nabla_{e_{i}}^{\text {L.C. }} e^{k}, e^{i}\right\rangle=-\sum_{i=0}^{3}\left\langle e^{k}, \nabla_{e_{i}}^{\text {L.C. }} e^{i}\right\rangle .$$
By inspecting the connection matrix (11), we can see that $\nabla_{e_{i}}^{L . C .} e^{i}$ contains only the terms $\omega_{j}^{i}$ which are pulled back from $Y$. Since these terms are invariant under the circle action, equation (43) vanishes giving equation (42).

Therefore we can commute $\nabla_{\mathrm{T}}$ with $\nabla_{e_{i}}^{L . C .}$ in equation (41), and apply equation (37) to get:
$$\nabla_{\mathrm{T}} d^{*} a=-\sum_{i=0}^{3}\left\langle\nabla_{e_{i}}^{L . C .} d f, e^{i}\right\rangle=\Delta f .$$
This statement is independent of frame, so we can substitute it into equation (40). The lemma now follows by integration by parts.

\section*{6. Results}

We are now ready to prove the formula for calculating the Seiberg-Witten invariants of a 4-manifold with a fixed point free circle action and state some immediate corollaries.

Theorem C. Let $X$ be a closed smooth 4-manifold with $b_{+}>1$ and a fixed point free circle action. Let $Y^{3}$ be the orbifold quotient space and suppose that $\chi \in \operatorname{Pic}^{t}(Y)$ is the orbifold Euler class of the circle action. If $\xi$ is a $\operatorname{Spin}^{c}$ structure over $X$ with $S W_{X}^{4}(\xi) \neq 0$, then $\xi=\pi^{*}\left(\xi_{0}\right)$ for some $\operatorname{Spin}^{c}$ structure on $Y$ and
$$S W_{X}^{4}(\xi)=\sum_{\substack{\xi^{\prime} \equiv \xi_{0} \\ \bmod 22}} S W_{Y}^{3}\left(\xi^{\prime}\right),$$
where $\xi^{\prime}-\xi_{0}$ is a well-defined element of $\operatorname{Pic}^{t}(Y)$. When $b_{+}=1$, the formula holds for all $\operatorname{Spin}^{c}$ structures which are pulled back from $Y$.

Remark 24. In the $b_{+}(X)=1$ case, the numerical invariant may still depend on the chamber structure of $Y$ if $b_{1}(Y)=1$. A nice example to check that Theorem A together with Theorem C gives the correct invariants in the $b_{+}(X)=1$ case is the manifold $T^{2} \times S^{2}$.

Proof. Recall that for a generic choice of metric and perturbation $\left(g_{Y}, \delta\right)$ the moduli space satisfies $\mathcal{H}_{\mathrm{S}_{0}}^{0}=\mathcal{H}_{\mathrm{S}_{0}}^{1}=\mathcal{H}_{\mathrm{S}_{0}}^{2}=0$ for all solutions $\mathrm{S}_{0}=\left(A_{0}, \Psi_{0}\right)$ to the 3-dimensional Seiberg-Witten equations (see subsection 5.3 for more details). For this good pair the moduli space $\mathcal{M}\left(Y, g_{Y}, \delta\right)$ is a smooth manifold with no reducible solutions. Since we can choose a perturbation generically such that the projection of $F_{A_{0}}+\delta$ onto the harmonic 2-forms is not a multiple of the harmonic representative of $\chi$ for all solutions in $\mathcal{M}\left(Y, g_{Y}, \delta\right)$, we have that
$$\left(\pi^{*}\left(F_{A_{0}}\right)+\pi^{*}(\delta)\right)^{+} \neq 0$$
on $X$ as well, hence $\mathcal{N}\left(X, g_{X}, \pi^{*}(\delta)^{+}\right)$does not contain reducible solutions either. By Theorem B, $\mathcal{N}\left(X, g_{X}, \pi^{*}(\delta)^{+}\right)$is diffeomorphic to a smooth manifold without reducible solutions. We have in effect shown that $\left(g_{X}, \pi^{*}(\delta)^{+}\right)$is a good pair and that this moduli space can be used to calculate the SW invariant.

Choose a specific Spin ${ }^{c}$ structure $\xi$ on $X$ such that $c_{1}(\xi)$ is pulled back and $S W_{X}(\xi) \neq 0$. There exists a $\operatorname{Spin}^{c}$ structure $\xi_{0}$ on $Y$ such that $\xi=\pi^{*}\left(\xi_{0}\right)$ by Theorem B, and
$$\mathcal{N}\left(X, \xi, g_{X}, \pi^{*}(\delta)^{+}\right)=\coprod_{\xi^{\prime} \cong \xi_{0}} \coprod_{\bmod \chi} \mathcal{M}\left(Y, \xi^{\prime}, g_{Y}, \delta\right) .$$
From this the formula follows. \(\square\)

When the action is free, the theorem above reduces to the formula worked out in a previous paper.

Corollary 25. Let $X$ be a closed smooth 4-manifold with $b_{+}>1$ and a free circle action. Then the orbit space $Y^{3}$ is a smooth 3-manifold and suppose that $\chi \in H^{2}(Y ; \mathbb{Z})$ is the first Chern class of the circle action on $X$. If $\xi$ is a $\operatorname{Spin}^{c}$ structure over $X$ with $S W_{X}^{4}(\xi) \neq 0$, then $\xi=\pi^{*}\left(\xi_{0}\right)$ for some Spin ${ }^{c}$ structure on $Y$ and
$$S W_{X}^{4}(\xi)=\sum_{\xi^{\prime} \equiv \xi_{0} \bmod \chi} S W_{Y}^{3}\left(\xi^{\prime}\right),$$
where $\xi^{\prime}-\xi_{0}$ is a well-defined element of $H^{2}(Y ; \mathbb{Z})$.
Because of this formula, it is particularly easy to calculate the Seiberg-Witten invariants for manifolds with free circle actions. The proof of this theorem in [B] is completely different than the proof of Theorem C. It used a gluing theorem and the next corollary, which now is just a consequence of Theorem C:

Corollary 26 (c.f. Donaldson [D]). Let $X \cong Y^{3} \times S^{1}$ with $b_{+}(X)>1$. If a Spin ${ }^{c}$ structure $\xi$ has $S W_{X}(\xi) \neq 0$, then there is one $\operatorname{Spin}^{c}$ structure $\xi_{0}$ on $Y$ such that $\xi=\pi^{*}\left(\xi_{0}\right)$ and
$$S W_{X}^{4}(\xi)=S W_{Y}^{3}\left(\xi_{0}\right) .$$

The usual route used to explain the corollary above is to consider the cyclic covering of $X$ by $Y^{3} \times \mathbb{R}$. There is a natural way to pullback solutions of (4) to solutions on $Y^{3} \times \mathbb{R}$ for Spin ${ }^{c}$ structures pulled up from $Y^{3}$. After putting the solution in temporal gauge it satisfies
the 3-dimensional Seiberg-Witten equations because it is a constant gradient-flow of the Chern-Simons-Dirac functional [CM]. Thus for each $\xi$ on $X$ such that $S W_{X}(\xi) \neq 0$ there is a Spin ${ }^{c}$ structure on $Y$ whose moduli space is nonempty for all generic metrics and perturbations. This corollary shows that this moduli space can actually be identified with the moduli space of $X$ and can be used to calculate the Seiberg-Witten invariant.

\section*{7. Examples}

In this subsection we construct a $b_{+}(X)=1$ 4-manifold with free circle actions whose Seiberg-Witten invariants are still diffeomorphism invariants. In this situation we can use Theorem C to calculate its Seiberg-Witten polynomial. We then use Theorem B to study the moduli spaces of $X$ and its quotient $Y$ and explain why the invariants do not change when crossing a "wall."

Recall the construction from [B]. Take the Whitehead link in $S^{3}$ and compose each component with the knots $K_{1}$ and $K_{2}$ (see Figure 1). Then the 3 -manifold $Y_{K_{1} K_{2}}$ is the result of surgery on this new link with each surgery coefficient equal to 0. Because the Whitehead link is fibered, when and $K_{1}$ and $K_{2}$ are fibered knots, the resulting 3-manifold fibers over the circle.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/393dcbc9-6054-4dbd-8d6d-fcd127ef622c-24.jpg?height=409&width=524&top_left_y=947&top_left_x=781}
\captionsetup{labelformat=empty}
\caption{Figure 1. $Y_{K_{1} K_{2}}$ before surgery.}
\end{figure}

Define the $X_{K_{1} K_{2}}(L)$ to be the unit circle bundle of a line bundle $L$ over $Y_{K_{1} K_{2}}$. When $c_{1}(L)$ is nontorsion, we get the following facts:
\begin{itemize}
\item[1.] $b_{1}\left(Y_{K_{1} K_{2}}\right)=2, b_{1}\left(X_{K_{1} K_{2}}(L)\right)=2$, and $b_{+}\left(X_{K_{1} K_{2}}(L)\right)=1$.
\item[2.] The cup product pairing
$$\cup: H^{1}\left(X_{K_{1} K_{2}}(L) ; \mathbb{Z}\right) \otimes H^{1}\left(X_{K_{1} K_{2}}(L) ; \mathbb{Z}\right) \rightarrow H^{2}\left(X_{K_{1} K_{2}}(L) ; \mathbb{Z}\right)$$
is trivial. This can be computed from the cup product on $Y_{K_{1} K_{2}}$ using the isomorphism $\pi^{*}: H^{1}\left(Y_{K_{1} K_{2}} ; \mathbb{Z}\right) \rightarrow H^{1}\left(X_{K_{1} K_{2}}(L) ; \mathbb{Z}\right)$.
\end{itemize}

The two facts above are exactly the conditions needed to show that the wall crossing number is zero for all Spin ${ }^{c}$ structures [LL]. Hence Seiberg-Witten invariants are still diffeomorphism invariants for these manifolds. In fact, any unit circle bundle over a three manifold which satisfies the conditions above will be such an example. The manifolds constructed above are also particularly easy for calculating the Seiberg-Witten polynomial using Theorem C. We give one example.

Let $Y=Y_{K_{1} K_{2}}$ be the manifold where $K_{1}$ and $K_{2}$ are the fibered $6_{3}$ knot in [R] (see Figure 2). Then the Seiberg-Witten polynomial
$$\mathcal{S} \mathcal{W}_{Y}^{3}(x, y)=\left(x^{-4}-3 x^{-2}+5-3 x^{2}+x^{4}\right)\left(y^{-4}-3 y^{-2}+5-3 y^{2}+y^{4}\right)$$
is calculated using Milnor torsion and Meng-Taubes' theorem [MT]. In this setup $x=\exp \left(P D\left(m_{1}\right)\right)$ and $y=\exp \left(P D\left(m_{2}\right)\right)$ are formal variables where $m_{1}, m_{2} \in H_{1}(Y ; \mathbb{Z})$ represent the meridian loops of each component of the Whitehead link. Thus the term $9 x^{2} y^{2}$ in the polynomial above
means that the Seiberg-Witten invariant for the Spin ${ }^{c}$ structure identified with $P D\left(2 m_{1}+2 m_{2}\right)$ is 9 .

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/393dcbc9-6054-4dbd-8d6d-fcd127ef622c-25.jpg?height=408&width=567&top_left_y=355&top_left_x=758}
\captionsetup{labelformat=empty}
\caption{Figure 2. $Y$ constructed out of $6_{3}$ knots.}
\end{figure}

Let $X=X_{K_{1} K_{2}}(L)$ be the unit circle bundle of a line bundle $L$ which satisfies $c_{1}(L)=$ $4 P D\left(m_{1}\right)$. By Theorem A and the fact that Seiberg-Witten invariants for $X$ are independent of the wall crossing, $c_{1}(\xi)$ is pulled back from $Y$. Thus $d(\xi)=0$ and condition (20) holds for Spin ${ }^{c}$ structures with nontrivial SW invariants. We can apply Theorem C to get
$$\mathcal{S} \mathcal{W}_{X}^{4}(x, y)=7 y^{-4}-6 x^{2} y^{-4}-21 y^{-2}+18 x^{2} y^{-2}+35-30 x^{2}-21 y^{2}+18 x^{2} y^{2}+7 y^{4}-6 x^{2} y^{4}$$
where the formal variables are defined by $x=\exp \left(\pi^{*}\left(P D\left(m_{1}\right)\right)\right)$ and $y=\exp \left(\pi^{*}\left(P D\left(m_{2}\right)\right)\right)$ and represent the pullback of $\operatorname{Spin}^{c}$ structures on $Y$. Note that $X$ is an example of a nonsymplectic 4-manifold with a circle action whose quotient fibers over the circle.

Theorem C gives insight into why the Seiberg-Witten invariant does not change when crossing a wall. Let $G_{X}$ be the product space of metrics and $\Gamma\left(\Lambda_{+}\right)$and recall that $\left(g_{X}, \delta\right) \in G_{X}$ is called a good pair if the moduli space $\mathcal{M}\left(X, \xi, g_{X}, \delta\right)$ is a smooth manifold without reducible solutions. When $b_{+}>1$ the wall of bad pairs is at least codimension 2 and a cobordism can be constructed between the two moduli spaces of good pairs. However, when $b_{+}(X)=1$ it is possible that two good pairs cannot be connected through a generic smooth path in $G_{X}$ without crossing a wall of bad pairs where reducible solutions occur. Passing through a bad pair could cause a singularity to occur in the cobordism. For a general $b_{+}=1$ manifold, this will often break the invariance of the Seiberg-Witten invariant.

Suppose that we had two good pairs that can not be connected without going through a bad pair. Connect the two good pairs with smooth generic paths to good pairs of the form $\left(g_{X}=\eta^{2}+g_{Y}, \pi^{*}(-F \pm \eta)^{+}\right)$. Here $g_{X}$ is fixed, $\|\eta\|$ is sufficiently small, and $F$ is the harmonic curvature form which represents $2 \pi \mathbf{i} c_{1}\left(\xi_{0}\right)$ for some $\operatorname{Spin}^{c}$ structure on $Y$. Suppose for the sake of argument that $\left\{\gamma(t)=\left(g_{X}, \pi^{*}(-F+t \eta)^{+}\right) \mid-1 \leq t \leq 1\right\}$ is a smooth generic path in $G_{X}$ connecting the good pairs. Then a bad pair occurs in both $G_{X}$ and $G_{Y}$ precisely when $t=0$. While the wall has codimension $b_{+}(X)=1$ in $G_{X}$ and hence unavoidable, the wall in $G_{Y}$ has codimension $b_{1}(Y)=2$. Thus it is possible to perturb the path in $G_{Y}$ to a smooth generic path which avoids any bad pairs. The moduli spaces $\mathcal{M}\left(Y, \xi_{0}, g_{Y},-F \pm \eta\right)$ are then cobordant, and
$$S W_{Y}\left(\xi_{0}, g_{Y},-F-\eta\right)=S W_{Y}\left(\xi_{0}, g_{Y},-F+\eta\right) .$$
This can be done for each $\operatorname{Spin}^{c}$ structure $\xi^{\prime}$ on $Y$ such that $\xi=\pi^{*}\left(\xi^{\prime}\right)$, so by Theorem C
$$S W_{X}\left(\xi, g_{X}, \pi^{*}(-F-\eta)^{+}\right)=S W_{X}\left(\xi, g_{X}, \pi^{*}(-F+\eta)^{+}\right),$$
i.e., the Seiberg-Witten invariant is independent of metric and perturbation.

Note that the perturbed path in $G_{Y}$ will correspond to a perturbed path in $G_{X}$ which will still go through a bad pair. The moduli space for $X$ will have reducible solutions at the bad pair, but they do not change the value of the Seiberg-Witten invariant.

The same analysis holds for any $b_{+}=14$-manifold with a fixed point free circle action and $b_{1}(Y)=2$. Therefore we get the following corollary to Theorem C.

Corollary 27. Let $X$ be a $b_{+}=1$ 4-manifold with a fixed point free circle action whose quotient $Y$ satisfies $b_{1}(Y)=2$. If $\xi=\pi^{*}\left(\xi_{0}\right)$ is a $\operatorname{Spin}^{c}$ structure which is pulled back from a $\operatorname{Spin}^{c}$ structure $\xi_{0}$ on $Y$, then
$$S W_{X}^{4}(\xi)=\sum_{\xi^{\prime} \equiv \xi_{0} \bmod \chi} S W_{Y}^{3}\left(\xi^{\prime}\right)$$
and the numerical invariant does not depend on the chamber in which it was calculated.

\section*{8. Final remarks}

Theorem C together with an affirmative answer to the following conjecture would establish a way to calculate Seiberg-Witten invariants for any $b_{+}>14$-manifold with a circle action.

Conjecture 28. If $X$ is a $b_{+}>1$ smooth closed 4-manifold with a circle action that has fixed points, then $\mathcal{S W}_{X} \equiv 0$.

There is already considerable evidence which suggest that this is true. For simply connected 4-manifolds carrying a circle action, we can apply the classification result of R. Fintushel [F1, F2].

Theorem 29 (Fintushel). Modulo the 3-dimensional Poincaré conjecture, a simply connected 4-manifold carrying a smooth $S^{1}$-action must be a connected sum of copies of $S^{4}, \mathbb{C P}^{2}, \overline{\mathbb{C P}}^{2}$, and $S^{2} \times S^{2}$.

This classification result is enough to show that in the $b_{+}>1$ case, $X$ is the connected sum of two $b_{+}>0$ pieces, and hence $\mathcal{S} \mathcal{W}_{X} \equiv 0$.

The conjecture also follows from Proposition 4 of [B] for 4-manifolds with smooth semi-free actions whose orbit space $Y$ has a nonempty boundary and the rank $H_{1}(Y, \partial Y ; \mathbb{Z})>1$.

A counter example to the conjecture above would be just as interesting as the proof.

\section*{References}
\begin{itemize}
\item[] [B] S. Baldridge, Seiberg-Witten invariants of 4-manifolds with free circle actions, Communications in Contemporary Mathematics, accepted for publication, to appear. E-print GT-9911051.
\item[] [CM] W. Chen and R. Matveyev, Symplectic Lefschetz fibrations on $S^{1} \times M^{3}$, Geom. Topol. 4 (2000), 517-535.
\item[] [D] S. Donaldson, The Seiberg-Witten equations and 4-manifold topology, Bull. A.M.S. 33 (1996), 45-70.
\item[] [F1] R. Fintushel, Circle actions on simply connected 4-manifolds, Trans. A.M.S. 230 (1977), 147-171.
\item[] [F2] R. Fintushel, Classification of circle actions on 4-manifolds, Trans. A.M.S. 242 (1978), 377-390.
\item[] [FS2] R. Fintushel and R. Stern, Knots, links, and 4-manifolds, Invent. Math., 134 (1998), 363-400.
\item[] [FM1] R. Friedman and J. Morgan, Algebraic surfaces and Seiberg-Witten invariants, J. Algebraic Geom., 6 (1997), 445-479.
\item[] [FM2] R. Friedman and J. Morgan, Obstruction bundles, semiregularity, and Seiberg-Witten invariants, Comm. Anal. and Geom., 7 (1999), 451-496.
\item[] [FuS] M. Furuta and B. Steer, Seifert fibred homology 3-spheres and the Yang-Mills equations on Riemann surfaces with marked points, Adv. in Math., 96 (1992), 38-102.
\item[] [HP] W. Huck and V. Puppe, Circle actions on 4-manifolds II, Arch. Math. 71 (1998), 493-500.
\item[] [LL] T.J. Li and A. Liu, General wall crossing formula, Math.l Res. Letters 2 (1995), 797-810.
\item[] [M] J. Morgan, 'The Seiberg-Witten Equations and Applications to the Topology of Smooth Four manifolds', Princeton University Press, Princeton, New Jersey, 1996.
\item[] [MT] G. Meng and C. Taubes, $\underline{S W}=$ Milnor Torsion, Math. Research Letters 3 (1996), 661-674.
\item[] [MOY] T. Mrowka, P. Ozsváth, and B. Yu, Seiberg-Witten monopoles on Seifert fibered spaces, Comm. Anal. Geom. 5 (1997), 685-791.
\end{itemize}
\begin{itemize}
\item[] [N] L. Nicolaescu, 'Notes on Seiberg-Witten Theory', Graduate Studies in Mathematics 28, American Mathematical Society, Providence, Rhode Island, 2000.
\item[] [OS1] P. Ozsváth and Z. Szabó, Higher type adjunction inequalities in Seiberg-Witten theory, preprint.
\item[] [OS2] P. Ozsváth and Z. Szabó, The symplectic Thom conjecture, Ann. of Math. 151 (2000), 93-124.
\item[] [R] D. Rolfsen, 'Knots and Links', Publish or Perish, Inc., Houston, TX, 1989.
\item[] [S] I. Satake, The Gauss-Bonnet theorem for V-manifolds, J. Math. Soc. Japan 4 (1957), 464-491.
\item[] [T] C. Taubes, The Seiberg-Witten invariants and symplectic forms, Math. Res. Letters 1 (1994), 809-822.
\item[] [W] E. Witten, Monopoles and four-manifolds, Math. Res. Letters 1 (1994), 769-796.
\end{itemize}

Department of Mathematics, Michigan State University
East Lansing, Michigan 48824
E-mail address: baldridg@math.msu.edu