---
retention_scope: session
part: 2
total_parts: 3
---

[Part 2/3 of: Almost-Kähler smoothings of compact complex surfaces with singularities.]

Since $A$ is defined and smooth on $M$, we see that higher order derivatives are at worst bounded. □
Remark: When performing gluing on a Kähler manifold, it is usual to work in holomorphic coordinates in which $\omega$ approaches the standard Kähler form $\omega_{0}$ on $\mathbb{C}^{m}$ to order 2. The existence of such a charts is actually a characterization of Kähler metrics. Here, we work in a Darboux chart instead, but we do retrieve an order two approximation, on the complex structure instead of the symplectic form.

Now recall that $r_{\varepsilon}=\varepsilon^{\beta}$ is our chosen gluing radius; for $\varepsilon$ small enough, $\left\{\rho \leq 4 r_{\varepsilon}\right\}$ is contained in the Darboux chart around each $p_{i}$.

Let $\chi_{1}: \mathbb{R} \rightarrow \mathbb{R}$ be a smooth cutoff function, such that
$$\chi_{1}(x)=\left\{\begin{array}{l}
0 \text { if } x \leq 2+\eta, \\
1 \text { if } x \geq 4
\end{array}\right.$$
where $\eta$ is very small; its only purpose is to provide some leeway and ensure that all derivatives will match when performing the gluing. Set
$$\chi_{r_{\varepsilon}}:=\chi_{1}\left(\frac{\rho}{r_{\varepsilon}}\right) .$$

We define an almost complex structure $J_{r_{\varepsilon}}$ on $M$ by
$$J_{r_{\varepsilon}}=\exp \left(\chi_{r_{\varepsilon}} A\right) J_{0} \exp \left(-\chi_{r_{\varepsilon}} A\right) .$$

In particular,
$$J_{r_{\varepsilon}}=\left\{\begin{array}{l}
J_{0} \text { if } \rho \leq 2 r_{\varepsilon}, \\
J_{M} \text { if } \rho \geq 4 r_{\varepsilon} .
\end{array}\right.$$

Moreover, using Lemma 19 in the "annulus" $\left\{2 r_{\varepsilon} \leq \rho \leq 4 r_{\varepsilon}\right\}$, we see that
$$\begin{aligned}
J_{r_{\varepsilon}}-J_{0} & =O\left(r_{\varepsilon}^{2}\right), \\
\partial\left(J_{r_{\varepsilon}}-J_{0}\right) & =O\left(r_{\varepsilon}\right) .
\end{aligned}$$

The first estimate results directly from the lemma. For the second, observe that
$$J_{r_{\varepsilon}}-J_{0}=\left(\exp \left(2 \chi_{r_{\varepsilon}} A\right)-I\right) J_{0}$$
thus first derivatives are of the form
$$\partial\left(J_{r_{\varepsilon}}-J_{0}\right)=2(d \exp )\left(2 \chi_{r_{\varepsilon}} A\right)\left(\partial \chi_{r_{\varepsilon}} A+\chi_{r_{\varepsilon}} \partial A\right) J_{0} .$$

To conclude, we use that in $\left\{2 r_{\varepsilon} \leq r \leq 4 r_{\varepsilon}\right\}$,
$$\partial \chi_{r_{\varepsilon}}=O\left(r_{\varepsilon}^{-1}\right) .$$

The endomorphism $J_{r_{\varepsilon}}$ on $M$ is an almost complex structure, compatible with $\omega_{M}$ by construction. It is not an integrable complex structure; however, its Nijenhuis tensor is supported in the cutoff region $\left\{2 r_{\varepsilon} \leq r \leq 4 r_{\varepsilon}\right\}$. We give an estimate of the Nijenhuis tensor $N_{J_{r_{\varepsilon}}}$, as it will appear in error terms down the road.

Lemma 20. The Nijenhuis tensor $N_{J_{r_{\varepsilon}}}$ of $J_{r_{\varepsilon}}$ verifies
$$N_{J_{r_{\varepsilon}}}=\left\{\begin{array}{l}
O\left(r_{\varepsilon}\right) \text { in }\left\{2 r_{\varepsilon} \leq r \leq 4 r_{\varepsilon}\right\}, \\
0 \text { elsewhere. }
\end{array}\right.$$
Moreover, its derivatives are bounded on $M$.
Proof. Recall that we have the following expression for the Nijenhuis tensor:
$$N_{J_{r_{\varepsilon}}}(X, Y)=\frac{1}{2} J_{r_{\varepsilon}}\left(\left(D_{r_{\varepsilon}, Y} J_{r_{\varepsilon}}\right) X-\left(D_{r_{\varepsilon}, X} J_{r_{\varepsilon}}\right) Y\right),$$
where $D_{r_{\varepsilon}}$ is the Levi-Civita connection associated to the Riemannian metric $g_{r_{\varepsilon}}:=\omega\left(\cdot, J_{r_{\varepsilon}} \cdot\right)$. Using this, we compute:
$$\begin{aligned}
N_{J_{r_{\varepsilon}}}(X, Y) & =\frac{1}{2}\left(J_{r_{\varepsilon}}-J_{0}\right)\left(\left(D_{r_{\varepsilon}, Y}\left(J_{r_{\varepsilon}}-J_{0}\right) X-\left(D_{r_{\varepsilon}, X}\left(J_{r_{\varepsilon}}-J_{0}\right) Y\right)\right.\right. \\
& +\frac{1}{2} J_{0}\left(D_{r_{\varepsilon}, Y}\left(J_{r_{\varepsilon}}-J_{0}\right) X-D_{r_{\varepsilon}, X}\left(J_{r_{\varepsilon}}-J_{0}\right) Y\right) \\
& +\frac{1}{2} J_{r_{\varepsilon}}\left(\left(D_{r_{\varepsilon}, Y} J_{0}\right) X-\left(D_{r_{\varepsilon}, X} J_{0}\right) Y\right),
\end{aligned}$$
where $D_{r_{\varepsilon}}$ is the Levi-Civita connection associated with the metric $g_{r_{\varepsilon}}=\omega_{M}\left(\cdot, J_{r_{\varepsilon}} \cdot\right)$. Using the estimate (16), we see that the first term of this sum is an $O\left(r_{\varepsilon}^{3}\right)$ and the second one is an $O\left(r_{\varepsilon}\right)$. We need estimate the third term by comparing it with the Nijenhuis tensor of $J_{0}$, which vanishes. To do this, notice that
$$D_{r_{\varepsilon}} J_{0}=\left(D_{0}+\Gamma_{r_{\varepsilon}}\right) J_{0}=\Gamma_{r_{\varepsilon}} J_{0},$$
where $\Gamma_{r_{\varepsilon}}$ is expressed with the Christoffel coefficients of the metric $g_{r_{\varepsilon}}$, thus the first derivatives of the coefficients of $g_{r_{\varepsilon}}$. As a consequence, $\Gamma_{r_{\varepsilon}} J_{0}=O\left(r_{\varepsilon}\right)$. \(\square\)

\subsection*{4.2 On the ALE space $X$.}

We proceed similarly on $X$. We work in the (family of) Darboux charts at infinity described in paragraph 3. In this chart, both $J_{X, \varepsilon}$ and $J_{0}$ are compatible with $\omega_{X, \varepsilon}$, thus there is a unique section $B_{\varepsilon}$ in $\mathcal{L}_{\omega_{X, \varepsilon}}$, anticommunting with both $J_{0}$ and $J_{X, \varepsilon}$, and such that
$$J_{X, \varepsilon}=\exp \left(B_{\varepsilon}\right) J_{0} \exp \left(-B_{\varepsilon}\right) .$$
Using our estimate (13), the same calculations that we already performed on $M$ show that
$$\begin{aligned}
B_{\varepsilon} & =O\left(r^{-4}\right) \\
\partial^{k} B_{\varepsilon} & =O\left(r^{-4-k}\right) .
\end{aligned}$$

We perform the same kind of cutoff as we did on the orbifold. Let $\chi_{2}: \mathbb{R} \rightarrow \mathbb{R}$ be a smooth cutoff function, such that
$$\chi_{2}(x)=\left\{\begin{array}{l}
1 \text { if } x \leq 1 \\
0 \text { if } x \geq 2-\eta
\end{array}\right.$$

Recall that $R_{\varepsilon}=r_{\varepsilon} / \varepsilon=\varepsilon^{\beta-1}$ is our gluing radius on the ALE space. We define a cutoff function on $X$ by
$$\chi_{R_{\varepsilon}}:=\chi_{2}\left(\frac{r}{R_{\varepsilon}}\right) .$$

If $\varepsilon$ is small enough, the region $\left\{r \geq R_{\varepsilon}\right\}$ is contained in the Darboux chart. We define an almostcomplex structure on $T^{*} S^{2}$ by
$$J_{R_{\varepsilon}}=\exp \left(\chi_{R_{\varepsilon}} B_{\varepsilon}\right) J_{0} \exp \left(-\chi_{R_{\varepsilon}} B_{\varepsilon}\right) .$$

By definition,
$$J_{R_{\varepsilon}}=\left\{\begin{array}{l}
J_{X, \varepsilon} \text { on }\left\{r \leq R_{\varepsilon}\right\} \\
J_{0} \text { on }\left\{r \geq 2 R_{\varepsilon}\right\} .
\end{array}\right.$$

As before, our estimate on $B_{\varepsilon}$ and choice of cutoff ensures that the difference between $J_{R_{\varepsilon}}$ and $J_{0}$ becomes small when $\varepsilon$ goes to zero. More precisely:
$$\begin{aligned}
J_{R_{\varepsilon}}-J_{0} & =O\left(R_{\varepsilon}^{-4}\right), \\
\partial^{k}\left(J_{R_{\varepsilon}}-J_{0}\right) & =O\left(R_{\varepsilon}^{-4-k}\right) .
\end{aligned}$$

As before, $J_{R_{\varepsilon}}$ is a compatible almost complex structure on $X$, compatible with $\omega_{X}$ in the Darboux chart. However, once again, it is not integrable. Its Nijenhuis tensor is supported in $\left\{R_{\varepsilon} \leq \rho_{x} \leq 2 R_{\varepsilon}\right\}$. The computation done on the orbifold translates directly to this case and we see that $N_{J_{R_{\varepsilon}}}$ verifies:

Lemma 21. The Nijenhuis tensor of $J_{R_{\varepsilon}}$ verifies, for any $k \geq 0$,
$$\partial^{k} N_{J_{R_{\varepsilon}}}=\left\{\begin{array}{l}
O\left(R_{\varepsilon}^{-5-k}\right) \text { on }\left\{R_{\varepsilon} \leq r \leq 2 R_{\varepsilon}\right\} \\
0 \text { elsewhere. }
\end{array}\right.$$
Proof. The proof is the same as Lemma 20, and relies on the expression (18) for the Nijenhuis tensor. We apply it this time to the Levi-Civita connection associated with the metric $g_{R_{\varepsilon}}=\omega_{X}\left(\cdot, J_{R_{\varepsilon}} \cdot\right)$. The computation then translates directly to this case, using (??) for the estimation of the Christoffel symbols. \(\square\)

\subsection*{4.3 The approximate solution}

The new almost-complex structures on $M$ and $X$ now both coincide with the standard one $J_{0}$ in suitables regions of the Darboux charts. Thus, we can glue them together to obtain an almost complex structure on the "connected sum" manifold $M_{\varepsilon}$ constructed at the end of paragraph 3.

First, we define a function on $M_{\varepsilon}$ that will encode both the function $\rho$ that extends the distance to the singularities on $M$, and the radius function $r$ on $X$. We set
$$\rho_{\varepsilon}=\left\{\begin{array}{l}
\rho \text { where } \rho \geq 2 r_{\varepsilon} ; \\
\varepsilon h_{\varepsilon^{-1}}^{*} r \text { where } \rho \leq 2 r_{\varepsilon} .
\end{array}\right.$$

We define $\hat{J}_{\varepsilon}$ as follows:
$$\hat{J}_{\varepsilon}= \begin{cases}h_{\varepsilon-1}^{*} J_{R_{\varepsilon}} & \text { where } \rho_{\varepsilon}<2 r_{\varepsilon}, \\ J_{r_{\varepsilon}} & \text { where } \rho_{\varepsilon} \geq 2 r_{\varepsilon} .\end{cases}$$

This smooth section of $\operatorname{End}\left(T M_{\varepsilon}\right)$ defines an almost complex structure on $M_{\varepsilon}$ that is compatible with $\omega_{\varepsilon}$ by construction. It is not integrable; its Nijenhuis tensor is supported in a small annulus $\left\{r_{\varepsilon} \leq \rho_{\varepsilon} \leq 4 r_{\varepsilon}\right\}$ around each singularity.

Lemma 22. The Nijenhuis tensor $N_{\hat{J}_{\varepsilon}}$ of $\hat{J}_{\varepsilon}$ verifies
$$N_{\hat{J}_{\varepsilon}}= \begin{cases}O\left(\varepsilon^{4} r_{\varepsilon}^{-5}\right) & \text { on }\left\{r_{\varepsilon} \leq \rho_{\varepsilon} \leq 2 r_{\varepsilon}\right\} \\ O\left(r_{\varepsilon}\right) & \text { on }\left\{2 r_{\varepsilon} \leq \rho_{\varepsilon} \leq 4 r_{\varepsilon}\right\} .\end{cases}$$
Moreover, its derivatives verify
$$\partial^{k} N_{\hat{J}_{\varepsilon}}= \begin{cases}O\left(\varepsilon^{4} r_{\varepsilon}^{-5-k}\right) & \text { on }\left\{r_{\varepsilon} \leq \rho_{\varepsilon} \leq 2 r_{\varepsilon}\right\} \\ O(1) & \text { on }\left\{2 r_{\varepsilon} \leq \rho_{\varepsilon} \leq 4 r_{\varepsilon}\right\} .\end{cases}$$
Proof. To deal with the rescaling, observe that
$$\begin{aligned}
N_{h_{\varepsilon-1}^{*} J_{R_{\varepsilon}}}(X, Y) & =N_{h_{\varepsilon-1}^{*} J_{R_{\varepsilon}}}\left(h_{\varepsilon-1}^{*} \tilde{X}, h_{\varepsilon^{-1}}^{*} \tilde{Y}\right) \\
& =h_{\varepsilon^{-1}}^{*} N_{J_{R_{\varepsilon}}}(\tilde{X}, \tilde{Y})
\end{aligned}$$ \(\square\)
where $\tilde{X}$ and $\tilde{Y}$ can be interpreted as vectors on $X$. Using lemma 21, we thus get the estimate on $\left\{r_{\varepsilon} \leq r \leq 2 r_{\varepsilon}\right\}$. The one on $\left\{2 r_{\varepsilon} \leq r \leq 4 r_{\varepsilon}\right\}$ comes directly from lemma 20.

Remark: Notice that for the exponent in the second line to be positive (hence for $N_{\hat{J}_{\varepsilon}}$ to decrease as $\varepsilon$ becomes small), we need $\beta<\frac{4}{5}$.

This construction endows $M_{\varepsilon}$ with an almost Kähler structure. The suitable Riemannian metric is obtained by setting $\hat{g}_{\varepsilon}:=\omega\left(\hat{J}_{\varepsilon} \cdot, \cdot\right)$. Equivalently :
$$\hat{g}_{\varepsilon}= \begin{cases}\varepsilon^{2} h_{\varepsilon^{-1}}^{*} g_{R_{\varepsilon}} & \text { where } \rho_{\varepsilon} \leq 2 r_{\varepsilon} \\ g_{r_{\varepsilon}} & \text { where } \rho_{\varepsilon} \geq 2 r_{\varepsilon}\end{cases}$$

\section*{5 The equation}

The goal now is to perturb the almost-Kähler structure on $M_{\varepsilon}$ into one with constant Hermitian scalar curvature. More precisely, we want to express the resulting equation as a partial differential equation on a function $f$ in a suitable functional space. To do this, we use the construction presented in 2.2, to associate a compatible $J_{f} \in \mathcal{A} \mathcal{C}_{\omega_{\varepsilon}}$ to any $f$. This would be analogous to the use of the $\partial \bar{\partial}$-lemma to move the Kähler form $\omega_{\varepsilon}$ in its cohomology class on a Kähler manifold.

Therefore, the differential operator we are interested in is given by $P: f \mapsto s^{\nabla}\left(J_{f}\right)$. More specifically, we want to solve the equation $P(f)=s_{g_{M}}+\lambda$ for $f$ in a suitable functional space and for some constant $\lambda$.

The strategy is the following. We want to solve this equation using a suitable version of the Inverse Function Theorem.

As a consequence, we write a Taylor development of the operator $P$ :
$$s^{\nabla}\left(J_{f}\right)=s^{\nabla}\left(\hat{J}_{\varepsilon}\right)+L_{\varepsilon} f+Q_{\varepsilon}(f),$$
where $L_{\varepsilon}$ is the linearisation of the operator at 0 and $Q_{\varepsilon}$ contains the nonlinear terms. Thus, we want to solve
$$L_{\varepsilon} f+\lambda=s_{g_{M}}-s^{\nabla}\left(\hat{J}_{\varepsilon}\right)-Q_{\varepsilon}(f) .$$

From there, if we can find a right inverse to the operator
$$\begin{aligned}
\tilde{L}_{\varepsilon}: \mathbb{R} \times E & \rightarrow F \\
(\lambda, f) & \mapsto \lambda+L_{\varepsilon} f,
\end{aligned}$$
for suitable Banach spaces $E$ and $F$, we are brought back to a fixed-point problem. To be able to use the fixed point theorem, we need to perform the following steps:
\begin{itemize}
\item[1.] Introduce weighted Hölder spaces on the connected sum $M_{\varepsilon}$;
\item[2.] Build a right inverse for $\tilde{L}_{\varepsilon}$;
\item[3.] Estimate the nonlinear operator $Q_{\varepsilon}$;
\item[4.] Estimate the difference between the Hermitian scalar curvature of the approximate solution and the scalar curvature of the orbifold metric $g_{M}$.
\end{itemize}

These steps will be the focus of the next sections.

\subsection*{5.1 Hölder spaces on $M_{\varepsilon}$.}

To make our implicit function theorem work, we will need to study elliptic linear differential operators on $M_{\varepsilon}$, as well as on its "components", namely the ALE space $X$ and punctured orbifold $M^{*}:=M \backslash\left\{p_{1} \ldots p_{k}\right\}$. However $X$ and $M^{*}$ are noncompact manifolds, and elliptic operators like the Laplacian do not have good properties in "classical" Hölder spaces $\mathcal{C}^{k, \alpha}\left(M^{*}\right)$ (resp. $\mathcal{C}^{k, \alpha}(X)$ ). As a consequence, we introduce suitable weighted Hölder spaces on $X, M^{*}$ and, from there, on $M_{\varepsilon}$. We will follow the introduction of such spaces from [8] (see also [2, 45]). For more details on analysis in weighted functional spaces, see for instance [6, 10, 27].

On the ALE model. Around each $p \in X$, we have a chart mapping the unit ball $B(0,1) \subset \mathbb{R}^{4}$ to a geodesic ball of radius $\eta r_{0}$ :
$$\phi: B(0,1) \rightarrow B\left(p, \eta r_{0}\right) .,$$
where $\eta>0$ is assumed to be very small and $r_{0}=r(p)$, where $r$ is a radius function on $X$ defined outside a compact set (for instance the radius of $\mathbb{C}^{2} / \mathbb{Z}_{2}$ in an ALE chart at infinity)..

Moreover, thanks to the ALE estimates on the fall-off of the metric, we may assume that
$$\phi^{*} g_{X}-r_{0}^{2} g_{0}=\mathcal{O}\left(r_{0}^{-4}\right),$$
and corresponding control on derivatives to order $k$.
Then, by definition, a function $f \in \mathcal{C}_{\text {loc }}^{k, \alpha}(X)$ is in $\mathcal{C}_{\delta}^{k, \alpha}(X)$ if there is a $C>0$ such that,in each such chart,
$$\|f \circ \phi\|_{\mathcal{C}^{k, \alpha}} \leq C r_{0}^{\delta} .$$

With this definition, the upshot is that if $\|f\|_{\mathcal{C}_{\delta}^{k, \alpha}(X)} \leq C$, then $f \in \mathcal{C}^{k, \alpha}(X)$ and, for $i \leq k$,
$$\left|\partial^{i} f\right| \leq c r^{\delta-i},$$
where $r$ is the radius function used above. The weight $\delta$ thus describe the behaviour at infinity of the function $f$.
Example: The function $w \mapsto|w|^{\gamma}$ belongs to $\mathcal{C}_{\delta}^{k, \alpha}(X)$ if and only if $\gamma \leq \delta$.
On the punctured orbifold. Recall that we have endowed $M$ with a function $\rho$ that is equal to the distance $p \mapsto d\left(p, p_{i}\right)$ in disjoint neighborhoods of each singularities, and smoothly extended to 1 away from the singularities. As before, around each $p \in M^{*}$, we consider maps to a small geodesic ball
$$\psi: B(0,1) \rightarrow B\left(p, \eta r_{0}\right)$$
with $r_{0}=\rho(p)$ and such that
$$\psi^{*} g_{M}-r_{0}^{2} g_{0}=\mathcal{O}_{\mathcal{C}^{k}}\left(r_{0}^{2}\right) .$$

A function $f \in \mathcal{C}_{\text {loc }}^{k, \alpha}\left(M^{*}\right)$ is in $\mathcal{C}_{\delta}^{k, \alpha}\left(M^{*}\right)$ if there is a $C>0$ such that, in each such chart,
$$\|f \circ \psi\|_{\mathcal{C}^{k, \alpha}} \leq C r_{0}^{\delta}$$
In this case, $\delta$ keeps track the worse possible behaviour for $f$ near the singularities.
Example: The function $z \mapsto|z|^{\gamma}$ belongs to $\mathcal{C}_{\delta}^{k, \alpha}\left(M^{*}\right)$ if and only if $\gamma \geq \delta$.
On the connected sum. We define the $\mathcal{C}_{\delta}^{k, \alpha}\left(M_{\varepsilon}\right)$-norm on $M_{\varepsilon}$ by gluing together the weighted spaces on the two pieces of the gluing. Namely, using a cut-off function $\chi$ that is equal to 1 outside $\rho_{\varepsilon} \geq 2 r_{\varepsilon}$ and zero in $\rho_{\varepsilon} \leq r_{\varepsilon}$, we can write any tensor field $T$ as the sum of two pieces $T_{X}:=(1-\chi) T$ and $T_{M^{*}}:=\chi T$ respectively supported in $\rho \leq 2 r_{\varepsilon}$ and $\rho \geq 2 r_{\varepsilon}$. This two pieces thus can be identified to tensor fields on $X$ and $M^{*}$ respectively. Then $\|T\|_{\mathcal{C}_{\delta}^{k, \alpha}}$ is given by
$$\varepsilon^{-\ell-\delta}\left\|\left(h_{\varepsilon^{-1}}\right)_{*} T_{X}\right\|_{\mathcal{C}_{\delta}^{k, \alpha}(X)}+\left\|T_{M^{*}}\right\|_{\mathcal{C}_{\delta}^{k, \alpha}\left(M^{*}\right)},$$
where $\ell$ is the degree of $T$. This will allow us to decompose the analysis on the ALE and orbifold parts of the gluing, which will prove very useful when constructing a right inverse for the linearised operator.
In terms of the 'radius' function $\rho_{\varepsilon}$ on $M_{\varepsilon}$, the fact that $\|f\|_{\mathcal{C}_{\delta}^{k, \alpha}\left(M_{\varepsilon}\right)} \leq c$ rewrites
$$\left|\partial^{j} f\right| \leq c \rho_{\varepsilon}^{\delta-i},$$
for any $j \leq k$; that is to say,
$$\begin{aligned}
& \left|\partial^{j} f\right| \leq c \text { where } \rho_{\varepsilon} \geq 4 r_{\varepsilon} \\
& \left|\partial^{j} f\right| \leq c \rho^{\delta-i} \text { where } 2 r_{\varepsilon} \leq \rho_{\varepsilon} \leq 4 r_{\varepsilon} \\
& \left|\partial^{j} f\right| \leq c r^{\delta-i} \text { where } \rho_{\varepsilon} \leq 2 r_{\varepsilon} .
\end{aligned}$$

We have the following relations for the norms with different weights:
$$\|f\|_{\mathcal{C}_{\delta^{\prime}}^{k, \alpha}} \leq\left\{\begin{array}{l}
\|f\|_{\mathcal{C}_{\delta}^{k, \alpha}} \text { if } \delta^{\prime} \leq \delta \\
\varepsilon^{\delta-\delta^{\prime}}\|f\|_{\mathcal{C}_{\delta^{\prime}}^{k, \alpha}} \text { if } \delta^{\prime}>\delta .
\end{array}\right.$$
Moreover, note that the multiplication
$$\begin{aligned}
& \mathcal{C}_{\delta}^{k, \alpha} \times \mathcal{C}_{\delta^{\prime}}^{k, \alpha} \rightarrow \mathcal{C}_{\delta+\delta^{\prime}}^{k, \alpha} \\
& (f, g) \mapsto f g
\end{aligned}$$
in continuous, with norm bounded independently of $\varepsilon$.
In terms of these weighted Hölder spaces, we get the following estimate from (21) and (22):
Lemma 23. The Nijenhuis tensor of $\hat{J}_{\varepsilon}$ has coefficients in $\mathcal{C}_{0}^{3, \alpha}$ for $0<\alpha<1$, and we have
$$\left\|N_{\hat{J}_{\varepsilon}}\right\|_{C_{0}^{3, \alpha}}= \begin{cases}O\left(\varepsilon^{4} r_{\varepsilon}^{-5}\right) & \text { on }\left\{r_{\varepsilon} \leq \rho_{\varepsilon} \leq 2 r_{\varepsilon}\right\} \\ O\left(r_{\varepsilon}\right) & \text { on }\left\{2 r_{\varepsilon} \leq \rho_{\varepsilon} \leq 4 r_{\varepsilon}\right\} .\end{cases}$$

\subsection*{5.2 The linearised operator $L_{\varepsilon}$.}

The next step is to understand the linearised operator $L_{\varepsilon}$. We use the computation of the linearised operator performed in Section 2.3, Proposition 10 :
$$\left.\hat{J}_{\varepsilon} \delta\left(\hat{J}_{\varepsilon} \mathcal{L}_{X_{f}} \hat{J}_{\varepsilon}\right)\right)^{b}=\Delta_{\hat{g}_{\varepsilon}} d f-2 \operatorname{Ric}\left(\operatorname{grad}_{g_{\varepsilon}} f, \cdot\right)+E_{\varepsilon} f$$
for $f \in C^{3, \alpha}\left(M_{\varepsilon}\right)$, with
$$E_{\varepsilon} f(Y)=\sum_{i} d f\left(\left(D_{e_{i}, \hat{J}_{\varepsilon} Y}^{2} \hat{J}_{\varepsilon}\right) e_{i}\right)+2 D d f\left(e_{i}, \hat{J}_{\varepsilon}\left(D_{Y} \hat{J}_{\varepsilon}\right) e_{i}\right)$$
in an orthonormal frame $\left\{e_{1}, \ldots, e_{2 m}\right\}=\frac{1}{\sqrt{2}}\left\{Z_{1}, \ldots, Z_{m}, \hat{J}_{\varepsilon} Z_{1}, \ldots, \hat{J}_{\varepsilon} Z_{m}\right\}$ on $\left(T M_{\varepsilon}, \hat{g}_{\varepsilon}\right)$.
Thus
$$L_{\varepsilon} f=\Delta_{\hat{g}_{\varepsilon}}^{2} f-2 \delta(\operatorname{Ric}(d f))+\delta E_{\varepsilon} f$$

As a consequence, the error term in supported in the gluing region $\left\{r_{\varepsilon} \leq r \leq 4 r_{\varepsilon}\right\}$, and we expect it to be small in appropriate weighted Hölder spaces.

We make this hunch precise in the next lemma.
Lemma 24 (Estimate on the error term). Let $f \in \mathcal{C}_{\delta}^{4, \alpha}\left(M_{\varepsilon}\right)$. Then we have
$$\left\|\delta E_{\varepsilon} f\right\|_{\mathcal{C}_{\delta-4}^{0, \alpha}}=o(1)\|f\|_{C_{\delta}^{4, \alpha}} .$$
Proof. Recall that for any vector fields $X, Y$ and $Z$, the following holds:
$$\hat{g}_{\varepsilon}\left(\left(D_{X} \hat{J}_{\varepsilon}\right) Y, Z\right)=2 \hat{g}_{\varepsilon}\left(\hat{J}_{\varepsilon} X, N(Y, Z) ;\right)$$
thus when computing estimates, the $C_{\delta}^{k, \alpha}\left(M_{\varepsilon}\right)$-norms of the Nijenhuis tensor and and $D \hat{J}_{\varepsilon}$ are comparable.

Applying the codifferential to the error term (27), we see that the terms that appear are of the form
$$\sum_{k=0}^{2} \partial^{k}\left(D \hat{J}_{\varepsilon}\right) \partial^{3-k} f$$
or
$$\partial^{2} f\left(D \hat{J}_{\varepsilon}\right) ; \partial^{2} f\left(D \hat{J}_{\varepsilon}\right)^{2} .$$

We need to compare these to the $C_{\delta}^{4, \alpha}$-norm of $f$. Since all these terms are supported in $\left\{r_{\varepsilon} \leq\right.$ $\left.\rho_{\varepsilon} \leq 4 r_{\varepsilon}\right\}$, by definition of the weighted norms, we have
$$\begin{aligned}
\left|\partial^{j} f\right| & \leq C r_{\varepsilon}^{\delta-j}\|f\|_{C_{\delta}^{4, \alpha}} \\
\left|\partial^{k}\left(D \hat{J}_{\varepsilon}\right)\right| & \leq C r_{\varepsilon}^{-k}\left\|N_{\hat{J}_{\varepsilon}}\right\|_{\mathcal{C}_{0}^{3, \alpha}}
\end{aligned}$$
for some positive constant $C$. Thus we obtain
$$\begin{aligned}
& \star\left|\rho_{\varepsilon}^{4-\delta}\left(D \hat{J}_{\varepsilon}\right) \partial^{3} f\right| \leq C r_{\varepsilon}\left\|N_{\hat{J}_{\varepsilon}}\right\|_{\mathcal{C}_{0}^{3, \alpha}}\|f\|_{C_{\delta}^{4, \alpha}} ; \\
& \star\left|\rho_{\varepsilon}^{4-\delta} \partial\left(D \hat{J}_{\varepsilon}\right) \partial^{2} f\right| \leq C r_{\varepsilon}\left\|N_{\hat{J}_{\varepsilon}}\right\|_{\mathcal{C}_{0}^{3, \alpha}}\|f\|_{C_{\delta}^{4, \alpha}} ; \\
& \star\left|\rho_{\varepsilon}^{4-\delta} \partial^{2}\left(D \hat{J}_{\varepsilon}\right) \partial f\right| \leq C r_{\varepsilon}\left\|N_{\hat{J}_{\varepsilon}}\right\|_{\mathcal{C}_{0}^{3, \alpha}}\|f\|_{C_{\delta}^{4, \alpha}} ; \\
& \star\left|\rho_{\varepsilon}^{4-\delta}\left(D \hat{J}_{\varepsilon}\right) \partial^{2} f\right| \leq C r_{\varepsilon}^{2}\left\|N_{\hat{J}_{\varepsilon}}\right\|_{\mathcal{C}_{0}^{3, \alpha}}\|f\|_{C_{\delta}^{4, \alpha}}
\end{aligned}$$
Using (29), we see that all the right-hand terms are $o(1)$ times $\|f\|_{C_{\delta}^{4, \alpha}}$, which is the conclusion we seeked. \(\square\)

\subsection*{5.2.1 Mapping properties of the Lichnerowicz operator.}

In this section we recall some properties of the "classical" Lichnerowicz operator on the punctured orbifold $\left(M^{*}, g_{M}, J_{M}\right)$ and on the ALE space $\left(X, g_{X}, J_{X}\right)$; those will be used as models to which we shall compare $L_{\varepsilon}$.

We are especially interested in mapping and Fredholm properties when the operator is defined between weighted spaces. We follow the exposition given in [2]. The analysis can be found in more details in Melrose's book [30] (in Sobolev spaces), as well as [38] (in Hölder spaces).

On the punctured orbifold $M^{*}$. The weight allows us to take into account the behavior of functions near the punctures, and it is to be expected that the properties of $\mathbb{L}$ will greatly depend on it. More precisely, it turns out that we will need to avoid a discrete set of "bad weights", the indicial roots. Roughly, the indicial roots describe the possible behaviors of a function in the kernel of $\mathbb{L}$ near the singularity. Using our chart near each singularity, a real, number $\delta$ is an indicial root if there is a function $v \in \mathcal{C}^{\infty}\left(B\left(p_{j}, 1\right)\right)$ such that
$$\mathbb{L}\left(\rho^{\delta} v\right)=O\left(\rho^{\delta-3}\right) .$$
Using the fact that, in this chart, the Kähler structure on $M^{*}$ differs from the Euclidean one at order 2, we see that it is equivalent to look for indicial roots of $\Lambda_{0}^{2}$, where $\Lambda_{0}$ is the Euclidean laplacian. These are known; the computation is recalled in [2] and [47] and rely on the eigenfunctions of the Laplacian on the sphere $S^{3}$, and are contained in $\mathbb{Z}$.

Choosing $\delta$ outside this critical set, we obtain that the operator
$$\begin{aligned}
\mathbb{L}_{\delta}: C_{\delta}^{4, \alpha}\left(M^{*}\right) & \rightarrow C_{\delta-4}^{0, \alpha}\left(M^{*}\right) \\
f & \mapsto \mathbb{L} f
\end{aligned}$$
is well defined, Fredholm, and has closed range. It also verifies the following duality property:
$$\operatorname{dim} \operatorname{Ker} \mathbb{L}_{\delta}=\operatorname{dim} \text { Coker } \mathbb{L}_{-\delta} .$$

To obtain good mapping properties, we need to introduce a modification of the operator. For each $i \in\{1, \ldots, k\}$, let $\xi_{i}$ be a smooth function on $M$ supported in a small ball $B\left(p_{j}, r_{0}\right)$ around $p_{j}$ and identically equal to 1 in $B\left(p_{j}, r_{0} / 2\right)$. Let $\mathcal{V}=\operatorname{span}\left(\xi_{1}, \ldots, \xi_{\ell}\right)$; we endow $\mathcal{V}$ with the norm $|f|=\sum\left|f\left(p_{i}\right)\right|$. Then we have:

Proposition 25. Assume that $\delta \in(0,1), \alpha \in(0,1)$. Then the operator
$$\begin{aligned}
\mathbb{L}_{\delta}^{\prime}:\left(\mathcal{C}_{\delta}^{4, \alpha} \oplus \mathcal{V}\right) \times \mathbb{R} & \rightarrow \mathbb{C}_{\delta-4}^{0, \alpha} \\
(f, \nu) & \mapsto \mathbb{L} f+\nu
\end{aligned}$$
is surjective and has one-dimensional kernel constituted of constant functions.
A proof of this can be found in [2] (Proposition 5.2).
The Lichnerowicz operator on $\left(M^{*}, \omega_{M}\right)$ admits a right inverse provided we add a space of functions constant near the singularities at the source. This will come at the cost of a less good norm for the right inverse of $L_{\varepsilon}$.

On the ALE space $X$. Most of the previous paragraph applies. This time, an indicial root for $\mathbb{L}_{\delta}$ is characterized by the existence of $v \in \mathcal{C}^{\infty}(\{r=1\})$ such that
$$\mathbb{L}\left(r^{\delta} v\right)=O\left(r^{\delta-5}\right),$$
and indicial roots describe asymptotic behaviors of function in $\operatorname{Ker} \mathbb{L}$. Due to the decay of the Eguchi-Hanson metric and complex structure towards the Euclidean ones, we may, as before, reduce the
problem to seeking indicial roots of $\Delta_{0}^{2}$ at infinity. This set is again contained in $\mathbb{Z}$, and, for any $\delta$ outside the critical set,the operator
$$\begin{aligned}
\mathbb{L}_{\delta}: C_{\delta}^{4, \alpha}(X) & \rightarrow C_{\delta-4}^{0, \alpha}(X) \\
f & \mapsto \mathbb{L} f
\end{aligned}$$
is well defined, Fredholm and has closed range. Moreover, the duality property (32) still holds.
Since there cannot be a holomorphic vector field on $X$ decaying at infinity, observe that for $\delta<0$, there is no nontrivial solution of $\mathbb{L} f=0$ such that $\phi \in \mathcal{C}_{\delta}^{4, \alpha}(X)$.

As a consequence, we have
Proposition 26. Assume that $\delta \in(0,1)$. Then $\mathbb{L}_{\delta}$ is surjective and its kernel is of dimension 1, generated by 1.

Again this proposition is proved in [2].

\subsection*{5.2.2 Construction of a right inverse for $L_{\varepsilon}$}

We are now able to build a right inverse for the operator $\tilde{L}_{\varepsilon}$. To do this, we will glue together right inverses of $\mathbb{L}$ on $M^{*}$ and $X$, thus obtaining an "approximate right inverse", from which we can build a proper right inverse to $L_{\varepsilon}$. This proof is the same as in [45], with the necessary adaptations due to our choice of weights as in [8], and the presence of an error term. Factoring this in, we prove

Proposition 27. For a sufficiently small gluing parameter $\varepsilon>0$, the operator
$$\begin{aligned}
\tilde{L}_{\varepsilon}: \mathcal{C}_{\delta}^{4, \alpha}\left(M_{\varepsilon}\right) \times \mathbb{R} & \rightarrow \mathcal{C}_{\delta-4}^{0, \alpha}\left(M_{\varepsilon}\right) \\
(f, \nu) & \mapsto L_{\varepsilon} f+\nu
\end{aligned}$$
admits a right inverse $G_{\varepsilon}$, with operator norm bounded by $\varepsilon^{-\delta \beta^{+}}$, where $\beta<\beta^{+}<1$.
Proof. This proof follows that of Proposition 20 in [45], which we recall in details here for the sake of completeness. The idea, explained for instance in [15], is to glue together right inverses on the model spaces, that have been obtained in section 5.2.1, to obtain an approximate right inverse to $\tilde{L}_{\varepsilon}$ on the connected sum $M_{\varepsilon}$. Then, we will modify this approximate right inverse to get a proper right inverse for $\tilde{L}_{\varepsilon}$.

We will need two sets of cutoff functions to build the approximate inverse operator. First, let $\gamma: \mathbb{R} \rightarrow[0,1]$ be a smooth function, equal to 0 on $]-\infty, 1]$ and equal to 1 in $\left[4,+\infty\left[\right.\right.$. On $M_{\epsilon}$ we define
$$\gamma_{1}: x \in M_{\varepsilon} \mapsto \gamma\left(\frac{\rho_{\varepsilon}(x)}{r_{\varepsilon}}\right) .$$
Then $\gamma_{1}$ is supported in the region $\rho_{\varepsilon} \geq r_{\varepsilon}$, which can be identified with a region of the (punctured) orbifold $M^{*}$. Its derivative $\partial \gamma_{1}$ is supported in the gluing region $r_{\varepsilon} \leq \rho_{\varepsilon} \leq 4 r_{\varepsilon}$.

We also set $\gamma_{2}:=1-\gamma_{1}$, supported in $\rho_{\varepsilon} \leq 4 r_{\varepsilon}$ which can be identified with $4 R_{\varepsilon} \geq r$ in the ALE space $X$.

Both $\gamma_{1}$ and $\gamma_{2}$ are smooth on $M_{\varepsilon}$ and are bounded in weighted Hölder norm:
$$\left\|\gamma_{i}\right\|_{\mathcal{C}_{0}^{4, \alpha}} \leq c .$$

We will need two other cutoff functions $\zeta_{1}$ and $\zeta_{2}$ with a slightly larger support, and with $\zeta_{i}=1$ in the support of $\gamma_{i}$. To do this, recall that $r_{\varepsilon}=\varepsilon^{\beta}$ with $0<\beta<1$. We choose a slightly larger exponent $\beta^{+}$and a slightly smaller exponent $\beta^{-}$so that $0<\beta^{-}<\beta<\beta^{+}<1$. Thus the region $\varepsilon<\rho_{\varepsilon}<1$ where we perform the gluing is sliced up in regions $1>4 \varepsilon^{\beta-}>4 r_{\varepsilon}>2 r_{\varepsilon}>r_{\varepsilon}>\varepsilon^{\beta^{+}}>\varepsilon$.

Let now $\zeta^{+}: \mathbb{R} \rightarrow[0,1]$ be a smooth function such that $\zeta^{+}(t)=1$ when $t \leq \beta, 0$ when $t \geq \beta^{+}$. The smooth cutoff $\zeta_{1}$, defined by
$$\zeta_{1}: x \in M_{\varepsilon} \mapsto \zeta^{+}\left(\frac{\log (\rho(x))}{\log (\varepsilon)}\right),$$
is supported in $\rho \geq \varepsilon^{\beta^{+}}$and is equal to 1 in $\operatorname{supp} \gamma_{1}$.
Similarly, let $\zeta^{-}: \mathbb{R} \rightarrow[0,1]$ be a smooth function equal to 1 on $] \beta,+\infty[$ and zero on $]-\infty, \beta^{-}[$ and define a cutoff on $M_{\varepsilon}$ by
$$\zeta_{2}: x \in M_{\varepsilon} \mapsto \zeta^{-}\left(\frac{\log (\rho(x) / 4)}{\log (\varepsilon)}\right) .$$
Then $\zeta_{2}$ is supported in $\rho \leq 4 \varepsilon^{\beta^{-}}$and is equal to 1 in $\operatorname{supp} \gamma_{2}$.
As far as estimations in Hölder norms are concerned, we see that
$$\left\|\partial \zeta_{i}\right\|_{\mathcal{C}_{-1}^{3, \alpha}} \leq \frac{c}{|\log \varepsilon|}$$

Now let $\psi \in \mathcal{C}_{\delta-4}^{0, \alpha}$. Notice that $\gamma_{1} \psi$ can be considered as a function on the punctured orbifold $M^{*}$. Moreover, using (33), we have
$$\left\|\gamma_{1} \psi\right\|_{\mathcal{C}_{\delta-4}^{0, \alpha}\left(M^{*}\right)} \leq c\|\psi\|_{\mathcal{C}_{\delta-4}^{0, \alpha}} .$$
From Proposition 25, there is a function $G_{1}\left(\gamma_{1} \psi\right)=\tilde{G}_{1}\left(\gamma_{1} \psi\right)+\sum \lambda_{i} \xi_{i} \in \mathbb{C}_{\delta-4}^{0, \alpha}\left(M^{*}\right) \oplus \mathcal{V}$ and a constant $\nu$ given by
$$\nu=\frac{1}{\operatorname{vol}\left(M^{*}\right)} \int_{M^{*}} \gamma_{1} \psi \operatorname{vol}_{g_{M}}$$
such that
$$\left\|\tilde{G}_{1}\left(\gamma_{1} \psi\right)\right\|_{\mathcal{C}_{\delta}^{4, \alpha}}+\sum\left|\lambda_{i}\right|+|\nu| \leq c\left\|\gamma_{1} \psi\right\|_{\mathcal{C}_{\delta-4}^{0, \alpha}\left(M^{*}\right)},$$
and
$$\mathbb{L}_{M}\left(G_{1}\left(\gamma_{1} \psi\right)\right)+\nu=\gamma_{1} \psi .$$

On the other hand, we may consider $\gamma_{2} \psi$ as a $\mathcal{C}_{\delta-4}^{0, \alpha}$ function on $X$. Taking into account the rescaling, we have that
$$\left\|\gamma_{2} \psi\right\|_{\mathcal{C}_{\delta-4}^{0, \alpha}(X)} \leq c \varepsilon^{\delta-4}\|\psi\|_{\mathcal{C}_{\delta-4}^{0, \alpha}} .$$

Then from Proposition 26 we see that there is a $G_{2}\left(\gamma_{2} \psi\right)$ such that
$$\left\|G_{2}\left(\gamma_{2} \psi\right)\right\|_{\mathcal{C}_{\delta}^{4, \alpha}}(X) \leq c\left\|\varepsilon^{4} \gamma_{2} \psi\right\|_{\mathcal{C}_{\delta-4}^{0, \alpha}(X)} \leq c \varepsilon^{\delta}\|\psi\|_{\mathcal{C}_{\delta-4}^{0, \alpha}},$$
thus
$$\left\|G_{2}\left(\gamma_{2} \psi\right)\right\|_{\mathcal{C}_{\delta}^{4, \alpha}} \leq c\|\psi\|_{\mathcal{C}_{\delta-4}^{0, \alpha}},$$
and such that
$$\mathbb{L}_{X} G_{2}\left(\gamma_{2} \psi\right)=\varepsilon^{4} \gamma_{2} \psi,$$
thus, after rescaling,
$$\mathbb{L}_{\varepsilon^{2} X} G_{2}\left(\gamma_{2} \psi\right)=\gamma_{2} \psi .$$

Now we glue these pieces together to get an approximate right inverse for $\tilde{L}_{\varepsilon}$. More precisely we set
$$\tilde{G} \psi=\zeta_{1} G_{1}\left(\gamma_{1} \psi\right)+\zeta_{2} G_{2}\left(\gamma_{2} \psi\right)$$
and we want to show that
$$\psi \in \mathcal{C}_{\delta-4}^{0, \alpha} \mapsto(\tilde{G} \psi, \nu)$$
is an approximate right inverse to $\tilde{L}_{\varepsilon}$, and that the operator norm of
$$\tilde{G}: \mathcal{C}_{\delta-4}^{0, \alpha} \rightarrow \mathcal{C}_{\delta}^{4, \alpha}$$
is bounded by $\varepsilon^{-\delta \beta^{+}}$.
We tackle the operator norm first. For $\psi \in \mathcal{C}_{\delta-4}^{0, \alpha}$ we want to show that
$$\left\|\zeta_{1} G_{1}\left(\gamma_{1} \psi\right)+\zeta_{2} G_{2}\left(\gamma_{2} \psi\right)\right\|_{\mathcal{C}_{\delta}^{4, \alpha}} \leq\left\|\zeta_{1} G_{1}\left(\gamma_{1} \psi\right)\right\|_{\mathcal{C}_{\delta}^{4, \alpha}}+\left\|\zeta_{2} G_{2}\left(\gamma_{2} \psi\right)\right\|_{\mathcal{C}_{\delta}^{4, \alpha}} \leq C \varepsilon^{\delta \beta^{+}}\|\psi\|_{\mathcal{C}_{\delta-4}^{0, \alpha}} .$$
The term $\zeta_{2} G_{2}\left(\gamma_{2} \psi\right)$, which can be considered on the ALE space $X$, will not be an issue. Indeed, its norm will be sum of terms of the form
$$\sum_{j=0}^{\ell} \rho^{j}\left|\partial^{j} \zeta_{2}\right| \rho^{\ell-j-\delta}\left|\partial^{\ell-j}\left(G_{2}\left(\gamma_{2} \psi\right)\right)\right|,$$
for $\ell=0, \ldots, 4$.
Using (37) and (34), in addition to the fact that $\zeta_{2}$ is a bounded function on $M_{\varepsilon}$, we see that those terms behave at worse like $\mathcal{O}\left(\|\psi\|_{\mathcal{C}_{\delta-4}^{0, \alpha}}\right)$.

The bad estimate comes from the 'orbifold' term $\zeta_{1} G_{1}\left(\gamma_{1} \psi\right)$. Indeed, $G_{1}\left(\gamma_{1} \psi\right)$ is the sum of a $\mathcal{C}_{\delta}^{4, \alpha}$ function, to which we may apply the same reasoning as the other term, and a function in $\mathcal{V}$, which behave like a constant near each puncture $p_{i}$ in $M^{*}$. Such constants are not bounded in $\mathcal{C}_{\delta}^{4, \alpha}\left(M^{*}\right)$ -norm for a positive $\delta$, as is the case here. However what we are interested in is $\zeta_{1} G_{1}\left(\gamma_{1} \psi\right)$, with $\zeta_{1}$ supported in $\left\{\rho \geq \varepsilon^{\beta^{+}}\right\}$, thus we in fact stay at a 'safe distance' from the punctures, and the norm of the constants is then comparable to
$$\sup _{\rho \geq \varepsilon^{\beta^{+}}} \lambda_{i}\left|\rho^{-\delta}\right| \leq c \varepsilon^{\delta \beta^{+}}$$

Thus, using (35), in the $\mathcal{C}_{\delta}^{4, \alpha}$-norm on $M_{\varepsilon}$ we get
$$\left\|\zeta_{1} G_{1}\left(\gamma_{1} \psi\right)\right\|_{\mathcal{C}_{\delta}^{4, \alpha}} \leq c \varepsilon^{\delta \beta^{+}}\|\psi\|_{\mathcal{C}_{\delta-4}^{0, \alpha}} .$$

To show that $\tilde{G}$ does constitute an approximate inverse to $L_{\varepsilon}$, still following the proof in [45], we prove the following claim:
$$\left\|L_{\varepsilon}(\tilde{G} \psi)+\nu-\psi\right\|_{\mathcal{C}_{\delta-4}^{0, \alpha}} \leq \frac{1}{2}\|\psi\|_{\mathcal{C}_{\delta-4}^{0, \alpha}} .$$

To do this, we will separate the study on the different "pieces" of the connected sum and compare with the model operators on $X$ and $M^{*}$. We write
$$\begin{aligned}
L_{\varepsilon}(\tilde{G} \psi)+\nu-\psi & =L_{\varepsilon}\left(\zeta_{1} G_{1}\left(\gamma_{1} \psi\right)\right)+\nu-\gamma_{1} \psi \\
& +L_{\varepsilon}\left(\zeta_{2} G_{2}\left(\gamma_{2} \psi\right)\right)-\gamma_{2} \psi
\end{aligned}$$
First we deal with the terms on the first line, which live in $\left\{\rho_{\varepsilon} \geq \varepsilon^{\beta^{+}}\right\}$. In this region, which can be considered as a subset of $M^{*}$, we want to compare $L_{\varepsilon}$ with the model operator $\mathbb{L}_{M}$. We will need the following lemma:

Lemma 28. On the region $\left\{\rho_{\varepsilon} \geq \varepsilon^{\beta^{+}}\right\}$in $M_{\varepsilon}$, the metric $\hat{g}_{\varepsilon}$ compares to the orbifold metric $g_{M}$ as follows:
$$\left\|\hat{g}_{\varepsilon}-g_{M}\right\|_{\mathcal{C}_{0}^{3, \alpha}}=\mathcal{O}\left(r_{\varepsilon}^{2}+\varepsilon^{4\left(1-\beta^{+}\right)}\right)$$

Proof. We decompose the study of $\hat{g}_{\varepsilon}-g_{M}$ in three regions of $M_{\varepsilon}$.
\begin{itemize}
\item[-] On $\left\{\rho \geq 4 r_{\varepsilon}\right\}, \hat{g}_{\varepsilon}-g_{M}=0$ by definition.
\item[-] On $\left\{2 r_{\varepsilon} \leq \rho \leq 4 r_{\varepsilon}\right\}$, we have $\hat{g}_{\varepsilon}-g_{M}=\omega_{M}\left(J_{r_{\varepsilon}}-J_{M}\right) \cdot, \cdot$ ). Using (16) we see that
$$\left\|J_{r_{\varepsilon}}-J_{M}\right\|_{\mathcal{C}_{0}^{3, \alpha}} \leq c r_{\varepsilon}^{2}$$
\item[-] Finally, on the region $\left\{\varepsilon^{\beta^{+}} \leq \rho_{\varepsilon} \leq 2 r_{\varepsilon}\right\}$, we split in $\hat{g}_{\varepsilon}-g_{M}=\hat{g}_{\varepsilon}-g_{0}+g_{0}-g_{M}$. Using (16) again, we have that $\left\|g_{0}-g_{M}\right\|_{\mathcal{C}_{0}^{3, \alpha}}=\left\|J_{0}-J_{M}\right\|_{\mathcal{C}_{0}^{3, \alpha}}=\mathcal{O}\left(r_{\varepsilon}^{2}\right)$.
To estimate $\hat{g}_{\varepsilon}-g_{0}$ we identify $\left\{\varepsilon^{\beta^{+}} \leq \rho_{\varepsilon} \leq 2 r_{\varepsilon}\right\}$ with the region $\left\{\varepsilon^{\beta^{+}-1} \leq r \leq 2 R_{\varepsilon}\right\}$ in $X$. There, $\hat{g}_{\varepsilon}=\varepsilon^{2} h_{\varepsilon^{-1}}^{*} g_{R_{\varepsilon}}$, thus our ALE estimate (13) gives $\left\|\hat{g}_{\varepsilon}-g_{0}\right\|_{\mathcal{C}_{0}^{3, \alpha}}=\mathcal{O}\left(\varepsilon^{4\left(1-\beta^{+}\right)}\right)$. \(\square\)
\end{itemize}

Now, using the same reasoning as in Proposition 18 in [45], we may estimate the operator norm of $L_{\varepsilon}-\mathbb{L}_{M}$. Recall that
$$\mathbb{L}_{M} f=-\Delta_{M}^{2} f+2 \delta\left(\operatorname{Ric}_{g_{M}}\left(\operatorname{grad}_{g_{\varepsilon}} f, \cdot\right)\right),$$
and we have obtained earlier that
$$L_{\varepsilon} f=-\Delta_{\varepsilon}^{2} f+2 \delta\left(\operatorname{Ric}_{\hat{g}_{\varepsilon}}\left(\operatorname{grad}_{g_{\varepsilon}} f, \cdot\right)\right)+E(f) .$$
Since we are not working in normal holomorphic coordinates, we have to be slightly more careful when comparing the bilaplacians $\Delta_{M}^{2}$ and $\Delta_{\varepsilon}^{2}$; indeed, the coefficients of the Laplacian $\Delta_{M}$ in our charts are comparable to $\partial\left(g_{M}^{-1} \partial f\right)$, and similarly those of $\Delta_{\varepsilon}$ are of the form $\partial\left(\hat{g}_{\varepsilon}^{-1} \partial f\right)$. In particular, notice that first derivatives of the coefficients of the metric intervene.

The coefficients of $\Delta_{M}^{2} f$ are of the form $\partial g_{M}^{-1} \partial^{2}\left(g_{M}^{-1} \partial f\right)$, and that of $\Delta_{\varepsilon}^{2} f$ are f the form $\partial \hat{g}_{\varepsilon}^{-1} \partial^{2}\left(\hat{g}_{\varepsilon}^{-1} \partial f\right)$, thus
$$\Delta_{M}^{2} f-\Delta_{\varepsilon}^{2} f=\partial\left(\left(g_{M}^{-1}-\hat{g}_{\varepsilon}^{-1}\right) \partial^{2}\left(g_{M}^{-1} \partial f\right)+\partial\left(\hat{g}_{\varepsilon}^{-1} \partial^{2}\left(\left(g_{M}^{-1}-\hat{g}_{\varepsilon}^{-1}\right) \partial f\right) .\right.\right.$$
thus
$$\begin{aligned}
\left\|\Delta_{M}^{2} f-\Delta_{\varepsilon}^{2} f\right\|_{\mathcal{C}_{\delta-4}^{0, \alpha}} & \leq\left\|\hat{g}_{\varepsilon}-g_{M}\right\|_{\mathcal{C}_{0}^{3, \alpha}}\left\|\partial^{2} f\right\|_{\mathcal{C}_{\delta-2}^{2, \alpha}} \\
& \leq\left\|\hat{g}_{\varepsilon}-g_{M}\right\|_{\mathcal{C}_{0}^{3, \alpha}}\|f\|_{\mathcal{C}_{\delta}^{4, \alpha}}
\end{aligned}$$

On the other hand, in a similar notation, the Riemannian curvature tensor is given by the derivatives of the Christoffel symbols $\Gamma=g^{-1} \partial g$, thus
$$\left\|\operatorname{Riem}\left(g_{M}\right)-\operatorname{Riem}\left(\hat{g}_{\varepsilon}\right)\right\|_{\mathcal{C}_{-2}^{0, \alpha}} \leq c\left\|\hat{g}_{\varepsilon}-g_{M}\right\|_{\mathcal{C}_{0}^{2, \alpha}} .$$
As a consequence, from Lemmas 28 and 24, we see that in operator norm, on $\left\{\rho_{\varepsilon} \geq \varepsilon^{\beta^{+}}\right\}$,
$$\left\|L_{\varepsilon}-\mathbb{L}_{M}\right\|=o(1) .$$

In a similar way, we deal with the terms on the second line of (42), which live in $\left\{\rho_{\varepsilon} \leq 4 \varepsilon^{\beta^{-}}\right\}$. This annulus can be identified with $\left\{r \leq 4 \varepsilon^{\beta^{-}-1}\right\}$ in $X$. We compare $\hat{g}_{\varepsilon}$ with the model ALE metric $g_{X}$.

Lemma 29. On the region $\left\{\rho_{\varepsilon} \leq 4 \varepsilon^{\beta^{-}}\right\}$in $M_{\varepsilon}$, the metric $\hat{g}_{\varepsilon}$ compares to the rescaled $A L E$ metric $\varepsilon^{2} h_{\varepsilon^{-1}}^{*} g_{X}$ as follows:
$$\left\|\hat{g}_{\varepsilon}-\varepsilon^{2} h_{\varepsilon^{-1}}^{*} g_{X}\right\|_{\mathcal{C}_{0}^{3, \alpha}}=\mathcal{O}\left(\varepsilon^{4} r_{\varepsilon}^{-4}+\varepsilon^{2 \beta^{-}}\right)$$
Proof. As before we split the study between the different parts of $M_{\varepsilon}$.
\begin{itemize}
\item[-] On $\left\{\rho_{\varepsilon} \leq r_{\varepsilon}\right\}, \hat{g}_{\varepsilon}$ is equal to the rescaled ALE metric.
\item[-] On $\left.\left\{r_{\varepsilon} \leq \rho_{\varepsilon} \leq 2 r_{\varepsilon}\right\}, \hat{g}_{\varepsilon}-\varepsilon^{2} h_{\varepsilon^{-1}}^{*} g_{X}=\varepsilon^{2} \omega_{X}\left(J_{R_{\varepsilon}}-J_{X}\right) \cdot, \cdot\right)$. Using the estimate (19), we see that on this annulus, $\left\|\hat{g}_{\varepsilon}-\varepsilon^{2} h_{\varepsilon^{-1}}^{*} g_{X}\right\|_{\mathcal{C}_{0}^{3, \alpha}}=\mathcal{O}\left(\varepsilon^{4} r_{\varepsilon}^{-4}\right)$.
\item[-] Finally, on $\left\{2 r_{\varepsilon} \leq \rho_{\varepsilon} \leq 4 \varepsilon^{\beta^{-}}\right\}$we write $\hat{g}_{\varepsilon}-\varepsilon^{2} h_{\varepsilon^{-1}}^{*} g_{X}=\hat{g}_{\varepsilon}-g_{0}+g_{0}-\varepsilon^{2} h_{\varepsilon^{-1}}^{*} g_{X}$. From (16) we see that on this region, $\left\|\hat{g}_{\varepsilon}-g_{0}\right\|_{\mathcal{C}_{0}^{3, \alpha}}=\mathcal{O}\left(\varepsilon^{2 \beta^{-}}\right)$, while the ALE estimate in $\left\{2 R_{\varepsilon} \leq \rho_{X} \leq 4 \varepsilon^{\beta^{-}-1}\right\}$ gives $\left\|g_{0}-\varepsilon^{2} h_{\varepsilon^{-1}}^{*} g_{X}\right\|_{\mathcal{C}_{0}^{3, \alpha}}=\mathcal{O}\left(\varepsilon^{4} r_{\varepsilon}^{-4}\right)$. \(\square\)
\end{itemize}

From there, the same proof as before shows that in operator norm
$$\left\|\mathbb{L}_{X}-L_{\varepsilon}\right\|=o(1) .$$

Thus, to prove (41), it is sufficient to show that for $\varepsilon$ small enough, we have
$$\left\|\mathbb{L}_{M}\left(\zeta_{1} G_{1}\left(\gamma_{1} \psi\right)\right)+\nu-\gamma_{1} \psi\right\|_{\mathcal{C}_{\delta-4}^{0, \alpha}} \leq \frac{1}{4}\|\psi\|_{\mathcal{C}_{\delta-4}^{0, \alpha}}$$
as well as
$$\left\|\mathbb{L}_{X}\left(\zeta_{2} G_{2}\left(\gamma_{2} \psi\right)\right)-\gamma_{2} \psi\right\|_{\mathcal{C}_{\delta-4}^{0, \alpha}} \leq \frac{1}{4}\|\psi\|_{\mathcal{C}_{\delta-4}^{0, \alpha}}$$

For the first inequality, we have
$$\begin{aligned}
\mathbb{L}_{M}\left(\zeta_{1} G_{1}\left(\gamma_{1} \psi\right)\right)+\nu-\gamma_{1} \psi & =\zeta_{1} \mathbb{L}_{M} G_{1} \gamma_{1} \psi+A\left(\operatorname{grad}_{g_{\varepsilon}} \zeta_{1} \star G_{1} \gamma_{1} \psi\right)+\nu-\gamma_{1} \psi \\
& =A\left(\operatorname{grad}_{g_{\varepsilon}} \zeta_{1} \star G_{1} \gamma_{1} \psi\right)
\end{aligned}$$
where $A$ is a third-order operator, whose coefficients are bounded in $\mathcal{C}_{\delta-4}^{0, \alpha}$, and ★ denotes a bilinear pairing. In fact, the terms contained in $A$ are similar to those appearing in (40).

Thus
$$\begin{aligned}
\left\|\mathbb{L}_{M}\left(\zeta_{1} G_{1}\left(\gamma_{1} \psi\right)\right)+\nu-\gamma_{1} \psi\right\|_{\mathcal{C}_{\delta-4}^{0, \alpha}} & =\left\|A\left(\operatorname{grad}_{g_{\varepsilon}} \zeta_{1} \star G_{1} \gamma_{1} \psi\right)\right\|_{\mathcal{C}_{\delta-4}^{0, \alpha}} \\
& \leq c\left\|\partial \zeta_{1}\right\|_{\mathcal{C}_{-1}^{3, \alpha}}\left\|G_{1} \gamma_{1} \psi\right\|_{\mathcal{C}_{\delta}^{3, \alpha}} \\
& =o(1)\|\psi\|_{\mathcal{C}_{\delta-4}^{0, \alpha}} .
\end{aligned}$$

The proof of the second inequality follows broadly the same lines. We have proven (41), i.e., we have shown that the operator norm of $\tilde{L}_{\varepsilon} \circ \tilde{G}-I$ is less than $1 / 2$. Thus, $\tilde{L}_{\varepsilon} \circ \tilde{G}$ is invertible and $\tilde{G} \circ\left(\tilde{L}_{\varepsilon} \circ \tilde{G}\right)^{-1}$ is a proper right inverse to $\tilde{L}_{\varepsilon}$. \(\square\)

\subsection*{5.3 Estimation of the Hermitian scalar curvature of $\hat{J}_{\varepsilon}$.}

We want to measure how good our approximate solution is in terms of Hermitian scalar curvature, i.e. we want to compare $s^{\nabla}\left(\hat{J}_{\varepsilon}\right)$ to the constant scalar curvature on the orbifold $M$. We obtain

Proposition 30. Denote by $s_{g_{M}}$ the constant scalar curvature of $\left(M, g_{M}\right)$. Then, for $0<\delta<1$ and $\beta<\frac{2}{3}$, we have
$$\left\|s^{\nabla}\left(\hat{J}_{\varepsilon}\right)-s_{g_{M}}\right\|_{\mathcal{C}_{\delta-4}^{0, \alpha}}=O\left(\varepsilon^{\beta(4-\delta)}\right) .$$

Proof. First recall that
$$s^{\nabla}\left(\hat{J}_{\varepsilon}\right)=s_{\hat{g}_{\varepsilon}}+\left|D \hat{J}_{\varepsilon}\right|^{2},$$
where $D$ is the Levi-Civita connection associated to $\hat{g}_{\varepsilon}$. As we already used earlier, $D \hat{J}_{\varepsilon}$ has norm comparable to the Nijenhuis tensor, hence
$$\left|D \hat{J}_{\varepsilon}\right|^{2}=\left\{\begin{array}{l}
O\left(r_{\varepsilon}^{2}\right) \text { in }\left\{2 r_{\varepsilon} \leq \rho \leq 4 r_{\varepsilon}\right\} \\
O\left(\varepsilon^{8} r_{\varepsilon}^{-10}\right) \text { in }\left\{2 r_{\varepsilon} \leq \rho \leq 4 r_{\varepsilon}\right\} .
\end{array}\right.$$

This error term will be smaller than what we want, so we only need to compare the riemannian scalar curvatures on $M_{\varepsilon}$ and $M$. The scalar curvature is a constant where $\rho \geq 4 r_{\varepsilon}$ and is bounded in $\left\{2 r_{\varepsilon} \leq \rho \leq 4 r_{\varepsilon}\right\}$, as it is given by second derivatives of the metric $g_{r_{\varepsilon}}$. On the "ALE" side, the scalar curvature is zero where $\rho \leq r_{\varepsilon}$, and is given by second derivatives of $g_{R_{\varepsilon}}$ in $\left\{r_{\varepsilon} \leq \rho \leq 2 r_{\varepsilon}\right\}$. Thus, using (19) and factoring in the rescaling, we obtain
$$s_{\hat{g}_{\varepsilon}}=O\left(\varepsilon^{4} r_{\varepsilon}^{-6}\right) \text { in }\left\{r_{\varepsilon} \leq \rho \leq 2 r_{\varepsilon}\right\} .$$
To sum up,
$$s_{\hat{g}_{\varepsilon}}=O(1)+O\left(\varepsilon^{4} r_{\varepsilon}^{-6}\right) .$$
Thus, using that $\rho=O\left(r_{\varepsilon}\right)$ in the region $\left\{r_{\varepsilon} \leq \rho \leq 4 r_{\varepsilon}\right\}$,
$$\begin{aligned}
\rho^{4-\delta}\left|s^{\nabla}\left(\hat{J}_{\varepsilon}\right)-s_{g_{M}}\right| & =\rho^{4-\delta}\left|s_{\hat{g}_{\varepsilon}}+\left|D \hat{J}_{\varepsilon}\right|^{2}-s(M)\right| \\
& =O\left(\varepsilon^{4} r_{\varepsilon}^{-2-\delta}\right)+O\left(r_{\varepsilon}^{4-\delta}\right)+O\left(r_{\varepsilon}^{6-\delta}\right)+O\left(\varepsilon^{8} r_{\varepsilon}^{-6-\delta}\right) \\
& =O\left(\varepsilon^{\beta(4-\delta)}\right),
\end{aligned}$$
as soon as $\beta<\frac{2}{3}$. \(\square\)

\subsection*{5.4 Behavior of the nonlinear part.}

Finally, we need to control the nonlinear part of the equation. Recall the expansion
$$s^{\nabla}\left(J_{f}\right)=s^{\nabla}\left(\hat{J}_{\varepsilon}\right)+L_{\varepsilon} f+Q_{\varepsilon}(f) .$$
We prove the following result, following Lemma 19 in [45].
Lemma 31. There is a constant $C$ such that
$$\left\|Q_{\varepsilon}(f)-Q_{\varepsilon}(g)\right\|_{\mathcal{C}_{\delta-4}^{0, \alpha}} \leq C\left(\|f\|_{\mathcal{C}_{2}^{4, \alpha}}+\|g\|_{\mathcal{C}_{2}^{4, \alpha}}\right)\|f-g\|_{\mathcal{C}_{\delta}^{4, \alpha}} .$$
Proof. We may rewrite
$$Q_{\varepsilon}(f)-Q_{\varepsilon}(g)=\int_{0}^{1} d_{\chi_{t}} Q_{\varepsilon}(f-g) d t$$
where $\chi_{t}:=g+t(f-g)$. Set $h=f-g$. From the Tayor development (23), we see that
$$\frac{d}{d s}{ }_{\mid s=0} Q_{\varepsilon}\left(\chi_{t}+s(f-g)\right)=d_{J_{\chi t}} s^{\nabla}\left(J_{\chi_{t}} \mathcal{L}_{X_{h}} \hat{J}_{\varepsilon}\right)-d_{\hat{J}_{\varepsilon}} s^{\nabla}\left(\hat{J}_{\varepsilon} \mathcal{L}_{X_{h}} \hat{J}_{\varepsilon}\right)$$
which we rewrite rewrites
$$d_{\chi_{t}} Q_{\varepsilon}(f-g)=\left(d_{J_{\chi_{t}}} s^{\nabla}-d_{\hat{J}_{\varepsilon}} s^{\nabla}\right)\left(J_{\chi_{t}} \mathcal{L}_{X_{h}} \hat{J}_{\varepsilon}\right)+d_{\hat{J}_{\varepsilon}} s^{\nabla}\left(\left(J_{\chi_{t}}-\hat{J}_{\varepsilon}\right) \mathcal{L}_{X_{h}} \hat{J}_{\varepsilon}\right) .$$

Observe next that
$$J_{\chi_{t}}-\hat{J}_{\varepsilon}=\left(\exp \left(\mathcal{L}_{X_{\chi_{t}}} \hat{J}_{\varepsilon}\right)-I\right) \hat{J}_{\varepsilon},$$
thus its coefficients are comparable to $\partial^{2} \chi$. Similarly, the coefficients of $\mathcal{L}_{X_{h}} \hat{J}_{\varepsilon}$ can be expressed in terms of $\partial^{2} h$.

To deal with the first term of (46), observe that due to the regularity of $J \in \mathcal{A} \mathcal{C}_{\omega_{\varepsilon}} \mapsto s^{\nabla}(J)$, the difference $d_{J_{\chi_{t}}} s^{\nabla}-d_{\hat{J}_{\varepsilon}} s^{\nabla}$ is controlled by $J_{\chi_{t}}-\hat{J}_{\varepsilon}$. Thus, the weighted norm
$$\begin{aligned}
\left\|\left(d_{J_{\chi t}} s^{\nabla}-d_{\hat{J}_{\varepsilon}} s^{\nabla}\right)\left(J_{\chi_{t}} \mathcal{L}_{X_{h}} \hat{J}_{\varepsilon}\right)\right\|_{\mathcal{C}_{\delta-4}^{0, \alpha}} & \leq c\left\|J_{\chi_{t}}-\hat{J}_{\varepsilon}\right\|_{\mathcal{C}_{0}^{2, \alpha}}\left\|J_{\chi_{t}} \mathcal{L}_{X_{h}} \hat{J}_{\varepsilon}\right\|_{\mathcal{C}_{\delta-2}^{2, \alpha}} \\
& \leq c\left\|\chi_{t}\right\|_{\mathcal{C}_{2}^{4, \alpha}}\|h\|_{\mathcal{C}_{\delta}^{4, \alpha}} \\
& \left.\leq c\|f\|_{\mathcal{C}_{2}^{4, \alpha}}+\|g\|_{\mathcal{C}_{2}^{4, \alpha}}\right)\|f-g\|_{\mathcal{C}_{\delta}^{4, \alpha}} .
\end{aligned}$$

On the other hand, our computations in section 5.2 show that the operator
$$d_{\hat{J}_{\varepsilon}} s^{\nabla}: \mathcal{C}_{\delta-2}^{2, \alpha}\left(\operatorname{End}\left(T M_{\varepsilon}\right)\right) \rightarrow \mathcal{C}_{\delta-4}^{0, \alpha}$$
is bounded. Thus,
$$\begin{aligned}
\left\|d_{\hat{J}_{\varepsilon}} s^{\nabla}\left(\left(J_{\chi_{t}}-\hat{J}_{\varepsilon}\right) \mathcal{L}_{X_{h}} \hat{J}_{\varepsilon}\right)\right\|_{\mathcal{C}_{\delta-4}^{0, \alpha}} & \left.\leq c \|\left(J_{\chi_{t}}-\hat{J}_{\varepsilon}\right) \mathcal{L}_{X_{h}} \hat{J}_{\varepsilon}\right) \|_{\mathcal{C}_{\delta-2}^{2, \alpha}} \\
& \left.\leq c\left\|\left(J_{\chi_{t}}-\hat{J}_{\varepsilon}\right)\right\|_{\mathcal{C}_{0}^{2, \alpha}} \| \mathcal{L}_{X_{h}} \hat{J}_{\varepsilon}\right) \|_{\mathcal{C}_{\delta-2}^{2, \alpha}} \\
& \leq c\left\|\chi_{t}\right\|_{\mathcal{C}_{2}^{4, \alpha}}\|h\|_{\mathcal{C}_{\delta}^{4, \alpha}} \\
& \leq c\left(\|f\|_{\mathcal{C}_{2}^{4, \alpha}}+\|g\|_{\mathcal{C}_{2}^{4, \alpha}}\right)\|f-g\|_{\mathcal{C}_{\delta}^{4, \alpha}} .
\end{aligned}$$

Summing the two final inequalities, we obtain the desired conclusion. \(\square\)

\subsection*{5.5 The nonlinear equation.}

We now have all the tools we need to solve our original equation. We follow closely the proof of Corollary 35 in [8]. Recall that we seek $f$ and $\lambda$ such that
$$L_{\varepsilon} f+\lambda=s_{g_{M}}-s^{\nabla}\left(\hat{J}_{\varepsilon}\right)-Q_{\varepsilon}(f) .$$

We look for $(f, \lambda)$ under the form $G_{\varepsilon}(\psi)$. Thus this rewrites
$$\psi=s_{g_{M}}-s^{\nabla}\left(\hat{J}_{\varepsilon}\right)-Q_{\varepsilon}\left(G_{\varepsilon}(\psi)\right):=B_{\varepsilon}(\psi) .$$
Thus our problem is reduced to a fixed point problem.
Proposition 32. There is a positive constant $C>0$ such that $B_{\varepsilon}$ maps the ball $\left\{\|\psi\|_{\mathcal{C}_{\delta-4}^{0, \alpha}} \leq C \varepsilon^{2}\right\}$ into itself and is $\frac{1}{2}$-Lipschitz on this ball.

Proof. We have
$$B_{\varepsilon}(\psi)-B_{\varepsilon}(\varphi)=Q_{\varepsilon}\left(G_{\varepsilon}(\psi)\right)-Q_{\varepsilon}\left(G_{\varepsilon}(\varphi)\right) .$$
Using Lemma 31 there is a $C_{1}>0$ such that:
$$\left\|Q_{\varepsilon}\left(G_{\varepsilon}(\psi)\right)-Q_{\varepsilon}\left(G_{\varepsilon}(\varphi)\right)\right\|_{\mathcal{C}_{\delta-4}^{0, \alpha}} \leq C_{1}\left(\left\|G_{\varepsilon}(\psi)\right\|_{\mathcal{C}_{2}^{4, \alpha}}+\left\|G_{\varepsilon}(\varphi)\right\|_{\mathcal{C}_{2}^{4, \alpha}}\right)\left\|G_{\varepsilon}(\psi-\varphi)\right\|_{\mathcal{C}_{\delta}^{4, \alpha}} .$$
Now, $\left\|G_{\varepsilon}(\psi-\varphi)\right\|_{\mathcal{C}_{\delta}^{4, \alpha}} \leq C_{2} \varepsilon^{-\delta \beta^{+}}\|\psi-\varphi\|_{\mathcal{C}_{\delta-4}^{0, \alpha}}$. On the other hand, since $\psi$ and $\phi$ are assumed to be in $\left\{\|\psi\|_{\mathcal{C}_{\delta-4}^{0, \alpha}} \leq C \varepsilon^{2}\right\}$, we get that
$$\left\|G_{\varepsilon}(\psi)\right\|_{\mathcal{C}_{\delta}^{4, \alpha}} \leq C_{2} \varepsilon^{-\delta \beta^{+}}\|\psi\|_{\mathcal{C}_{\delta-4}^{0, \alpha}} \leq C C_{2} \varepsilon^{2-\delta \beta^{+}},$$
and the same stands for $\varphi$. From this we deduce
$$\left\|G_{\varepsilon}(\psi)\right\|_{\mathcal{C}_{2}^{4, \alpha}\left(M_{\varepsilon}\right)} \leq C \varepsilon^{\delta-\delta \beta^{+}}=C C_{2} \varepsilon^{\delta\left(1-\beta^{+}\right)}$$
Thus
$$\left\|Q_{\varepsilon}\left(G_{\varepsilon}(\psi)\right)-Q_{\varepsilon}\left(G_{\varepsilon}(\varphi)\right)\right\|_{\mathcal{C}_{\delta-4}^{0, \alpha}} \leq C C_{1} C_{2} \varepsilon^{\delta\left(1-2 \beta^{+}\right)}\|\psi-\varphi\|_{\mathcal{C}_{\delta-4}^{0, \alpha}} .$$
Provided $\beta<\frac{1}{2}$, this means that for $\varepsilon$ small enough, $B_{\varepsilon}$ is $\frac{1}{2}$-contractant on $\left\{\|\psi\|_{\mathcal{C}_{\delta-4}^{0, \alpha}} \leq C \varepsilon^{2}\right\}$.

Moreover, $B_{\varepsilon}$ maps $\left\{\|\psi\|_{\mathcal{C}_{\delta-4}^{0, \alpha}} \leq C \varepsilon^{2}\right\}$ into itself. Indeed, for such a $\psi$,
$$\begin{aligned}
\left\|B_{\varepsilon}(\psi)\right\|_{\mathcal{C}_{\delta-4}^{0, \alpha}} & \leq\left\|B_{\varepsilon}(\psi)-B_{\varepsilon}(0)\right\|_{\mathcal{C}_{\delta-4}^{0, \alpha}}+\left\|B_{\varepsilon}(0)\right\|_{\mathcal{C}_{\delta-4}^{0, \alpha}} \\
& \leq \frac{1}{2}\|\psi\|_{\mathcal{C}_{\delta-4}^{0, \alpha}}+\left\|s^{\nabla}\left(\hat{J}_{\varepsilon}\right)-\lambda\right\|_{\mathcal{C}_{\delta-4}^{0, \alpha}} \\
& \leq \frac{1}{2} C \varepsilon^{2}+C_{3} \varepsilon^{\beta(4-\delta)} \\
& \leq C \varepsilon^{\prime}
\end{aligned}$$
provided we choose $\beta$ close enough to $\frac{2}{3}$ and $\delta$ close enough to 0. \(\square\)

Thus, we may prove the following result, which directly implies our Theorem 1.
Theorem 33. For $\varepsilon>0$ small enough, there is on $\left(M_{\varepsilon}, \omega_{\varepsilon}\right)$ a smooth compatible almost-Kähler structure $J_{\varepsilon}$, of constant Hermitian scalar curvature, such that
\begin{itemize}
\item[-] $J_{\varepsilon}$ converges, in $\mathcal{C}^{2, \alpha}$-norm, to $J_{M}$, on every compact set of $M^{*}$ (in the sense of Definition 13);
\item[-] $J_{\varepsilon}$ converges, in $\mathcal{C}^{2, \alpha}$-norm, to $J_{X}$, on every compact set of $X$ (in the sense of Definition 14).
\end{itemize}

Proof. According to Proposition 32, we may apply Banach's fixed point theorem to $B_{\varepsilon}$ on
$$\left\{\|\psi\|_{\mathcal{C}_{\delta-4}^{0, \alpha}} \leq C \varepsilon^{2}\right\} .$$
Therefore, there is a unique $\psi_{\varepsilon} \in \mathcal{C}_{\delta-4}^{0, \alpha}\left(M_{\varepsilon}\right)$, whose norm is comparable to $\varepsilon^{2}$, and that is solution to the main equation (47).

Then, setting $\left(f_{\varepsilon}, \lambda_{\varepsilon}\right)=G_{\varepsilon}(\psi)$, we see that $f_{\varepsilon}$ solves (24), and thus, the almost-complex structure $J_{\varepsilon}:=J_{f_{\varepsilon}}$ endows $M_{\varepsilon}$ with a constant Hermitian curvature almost-Kähler structure. Moreover, by Proposition 27, we have
$$\left\|J_{\varepsilon}-\hat{J}_{\varepsilon}\right\|_{\mathcal{C}_{\delta-2}^{2, \alpha}} \leq c\left\|f_{\varepsilon}\right\|_{\mathcal{C}_{\delta}^{4, \alpha}} \leq c \varepsilon^{2-\delta \beta^{+}} .$$
Thus, if $K_{1}$ is a compact set in $M^{*}$, then for $\varepsilon$ small enough, $K_{1} \subset M \backslash \cup_{i} B\left(p_{i}, 4 r_{\varepsilon}\right)$. By definition $\hat{J}_{\varepsilon \mid K_{1}}=J_{M \mid K_{1}}$.

Moreover, on $\subset M \backslash \cup_{i} B\left(p_{i}, 4 r_{\varepsilon}\right)$, the weighted Hölder norm $\mathcal{C}_{\delta-2}^{2, \alpha}$ coincides with the usual Hölder $\mathcal{C}^{2, \alpha}$ norm (according to the definition (26)), thus (48) implies
$$\left\|J_{\varepsilon}-J_{M}\right\|_{\mathcal{C}^{2, \alpha}\left(K_{1}\right)} \leq c \varepsilon^{2-\delta \beta^{+}} .$$
Since we have chosen $0<\delta, \beta^{+}<1$, we see that the right hand side goes to zero when $\varepsilon$ goes to zero, thus $J_{\varepsilon}$ does converge to $J_{M}$ on $K_{1}$.

Similarly, on a compact set $K_{2}$ of $X$, the pullback $h_{\varepsilon}^{*} \hat{J}_{\varepsilon}$ is equal to the ALE complex structure $J_{X \mid K_{2}}$ for $\varepsilon$ small enough.

Then, the estimate (48), and the definition of the weighted norms on $M_{\varepsilon}$ (25) imply that, on $K_{2}$, we have
$$\left\|h_{\varepsilon}^{*} J_{\varepsilon}-J_{X}\right\|_{\mathcal{C}^{2, \alpha}\left(K_{2}\right)} \leq c \varepsilon^{\delta\left(1-\beta^{+}\right)}$$
for some positive constant $c$. Since $\delta \in(0,1)$ and $\beta^{+}<1$, the right hand side goes to zero when $\varepsilon$ goes to zero.

It remains to show that the solution has the required regularity. The $\mathcal{C}^{4, \alpha}$ function $f_{\varepsilon}$ is solution of
$$s^{\nabla}\left(J_{f_{\varepsilon}}\right)=\tilde{\lambda}_{\varepsilon},$$
with $\tilde{\lambda}_{\varepsilon}$ a constant. As evidenced by the computations of Section 2.3, this equation is a 4th order elliptic equation. Moreover, the coefficients are rational functions of $x \in M_{\varepsilon}$ and derivatives of $f$ up to order 4.

Using classical results in elliptic regularity (see for instance Besse [7], Theorem 41 in the Appendix, or Morrey [34]), and a bootstrapping argument, we see that the function $f_{\varepsilon}$ is actually a smooth function on $M_{\varepsilon}$.

As a consequence, the almost-complex structure $J_{\varepsilon}=J_{f_{\varepsilon}}$ and the associated metric $g_{\varepsilon}=\omega_{\epsilon}\left(J_{\varepsilon} \cdot, \cdot\right)$ are also smooth. This concludes the proof of our main result. \(\square\)

Furthermore, we can refine the bootstrapping argument to obtain that for any $k \geq 0$, the constant hermitian scalar curvature almost-Kähler structures $\left(J_{\varepsilon}\right)$ converge, in $\mathcal{C}^{k, \alpha}$ to $J_{M}$ (resp. $J_{X}$ ) on every compact set of $M^{*}=M \backslash\left\{p_{1}, \ldots, p_{\ell}\right\}$ (resp. on every compact set of $X$ ).

To obtain this result, we need to show that $\left\|f_{\varepsilon}\right\|_{\mathcal{C}^{k, \alpha}(K)} \xrightarrow{\varepsilon \rightarrow 0} 0$ for every $k \geq 0$ and for every compact set $K \subset M^{*}$ (and the same on $X$ ). We know that $f_{\varepsilon}$ is smooth and that the previous convergence holds in $\mathcal{C}^{4, \alpha}(K)$.

We will make use of the elliptic equation verified by $f_{\varepsilon}$ : there is a constant $\lambda_{\varepsilon}$ such that
$$\lambda_{\varepsilon}=s^{\nabla}\left(J_{f_{\varepsilon}}\right)=s^{\nabla}\left(\hat{J}_{\varepsilon}\right)+L_{\varepsilon}(f)+Q_{\varepsilon}(f) .$$

First, we need the following technical lemma to better understand the non-linear part $Q_{\varepsilon}$ of the equation.

Lemma 34. The non-linear part of (50) can be decomposed as
$$Q_{\varepsilon}(u)=Q_{\varepsilon}^{(1)}(u)+Q_{\varepsilon}^{(2)}(u),$$
where
\begin{itemize}
\item[-] $Q_{\varepsilon}^{(1)}$ is a nonlinear operator or order 3 with smooth coefficients depending on $\hat{g}_{\varepsilon}$ and its derivatives;
\item[-] $Q_{\varepsilon}^{(2)}$ is a nonlinear operator of order 4, that verifies, for $u$ suitably smooth and $k \in \mathbb{N}$,
$$\left\|Q_{\varepsilon}^{(2)}(u)\right\|_{\mathcal{C}^{k, \alpha}} \leq c\|u\|_{\mathcal{C}^{k+3}}\|u\|_{\mathcal{C}^{k+4, \alpha}}$$
\end{itemize}

Proof. To better understand the nonlinearities of the equation, we turn to the computation of the connection 1-form $\alpha$ of the Chern connection. Recall a few notations: the variation of complex structure induced by a function $u$ was given by
$$a_{u}=\frac{1}{2} \mathcal{L}_{X_{u}} \hat{J}_{\varepsilon},$$
which is linear in $u$, with derivatives of order at most 2 . We set
$$J_{u}=\exp \left(-a_{u}\right) \hat{J}_{\varepsilon} \exp \left(a_{u}\right) .$$
Then in the proof of the Mohsen formula, we had obtained
$$\begin{aligned}
\alpha\left(J_{u}\right)(X)= & -\frac{1}{2} \sum_{k} \hat{g}_{\varepsilon}\left(\exp \left(a_{u}\right)\left(D_{\exp \left(-a_{u}\right) e_{k}} J_{u}\right) X, e_{k}\right) \\
& +\frac{1}{2} \sum_{k} \hat{g}_{\varepsilon}\left(\exp \left(a_{u}\right) D_{J_{u} X}\left(\exp \left(-a_{u}\right) e_{k}\right), e_{k}\right) \\
& -\frac{1}{2} \sum_{k} \hat{g}_{\varepsilon}\left(\hat{J}_{\varepsilon} \exp \left(a_{u}\right) D_{X}\left(\exp \left(-a_{u}\right) e_{k}\right), e_{k}\right) .
\end{aligned}$$

From there, we see that $\alpha_{u}$ can be written
$$\alpha\left(J_{u}\right)=\alpha_{0}+\dot{\alpha}_{u}+\tilde{Q}_{\varepsilon}^{(1)}(u)+\tilde{Q}_{\varepsilon}^{(2)}(u)$$
where $\alpha_{0}$ is the connection 1-form associated to the approximate solution $\hat{J}_{\varepsilon}, \dot{\alpha}_{u}$ is the linearization. What we are interested in are the remaining terms $\tilde{Q}_{\varepsilon}^{(1)}$ and $\tilde{Q}_{\varepsilon}^{(2)}$. The derivatives of $u$ appearing in $\tilde{Q}_{\varepsilon}^{(1)}(u)$ are of order at most 3. In fact, $\tilde{Q}_{\varepsilon}^{(1)}(u)$ is a sum of terms of the form
$$(\partial u)^{l}\left(\partial^{2} u\right)^{k}\left(D_{e_{k}} \hat{J}_{\varepsilon}\right),(\partial u)^{l}\left(\partial^{2} u\right)^{k}\left(D_{\hat{J}_{\varepsilon} X} e_{k}\right) \text { and }(\partial u)^{l}\left(\partial^{2} u\right)^{k}\left(D_{X} e_{k}\right),$$
with $k+l \geq 2$, and coefficients given by coefficients of the metric $\hat{g}_{\varepsilon}$. On the other hand, $\tilde{Q}_{\varepsilon}^{(2)}(u)$ is a sum of terms of the form
$$(\partial u)^{l}\left(\partial^{2} u\right)^{k} \partial^{3} u$$
for $k+l \geq 1$, and as before the coefficients are provided by that of the metric $\hat{g}_{\varepsilon}$.
Since
$$s^{\nabla}\left(J_{u}\right)=2 \Lambda d \alpha\left(J_{u}\right)$$
we see that
$$s^{\nabla}\left(J_{u}\right)=s^{\nabla}\left(\hat{J}_{\varepsilon}\right)+L_{\varepsilon}(u)+Q_{\varepsilon}^{(1)}(u)+Q_{\varepsilon}^{(2)}(u)$$
where the terms in $Q_{\varepsilon}^{(1)}$ are of the form $\left(\partial^{2} u\right)^{k}\left(\partial^{3} u\right)$, with $k \geq 0$, and the terms in $Q_{\varepsilon}^{(2)}(u)$ are of the form $\left(\partial^{2} u\right)^{k}\left(\partial^{4} u\right)$ for $k \geq 1$. \(\square\)

Using this, we prove
Proposition 35. For all $k \geq 1$, for every compact set $K \subset M^{*}$, we have $\left\|f_{\varepsilon}\right\|_{\mathcal{C}^{4+k, \alpha}(K)} \xrightarrow{\varepsilon \rightarrow 0} 0$
Proof. We prove the claim by induction on $k$.
For $k=1$, we want to obtain an estimate on $\left\|f_{\varepsilon}\right\|_{\mathcal{C}^{5, \alpha}(K)}$. Let $K^{\prime} \supset K$ a slightly larger compact of $M^{*}$ and let us consider $\varepsilon$ small enough so that $K^{\prime} \subset M \backslash \cup_{i}\left(B\left(p_{i}, 4 r_{\varepsilon}\right)\right.$, so that the approximate solution coincides with the orbifold structure on $K^{\prime}$. For this choice of $\varepsilon$, the smooth function $f_{\varepsilon}$ is solution of the elliptic fourth-order equation
$$\tilde{\lambda}_{\varepsilon}=L\left(f_{\varepsilon}\right)+Q^{(1)}\left(f_{\varepsilon}\right)+Q^{(2)}\left(f_{\varepsilon}\right) .$$
Here we use that there is an $\varepsilon_{K^{\prime}}$ such that for $\varepsilon<\varepsilon_{K^{\prime}}$, on the compact $K^{\prime}$, the coefficients of the equation do not depend on $\varepsilon$. Moreover, for $\varepsilon<\varepsilon_{K^{\prime}}, s^{\nabla}\left(\hat{J}_{\varepsilon}\right)$ is constant, equal to $s_{g_{M}}$ and $\tilde{\lambda}_{\varepsilon}=\lambda_{\varepsilon}-s_{g_{M}}$ goes to zero when $\varepsilon$ goes to zero. The equation (51) is quasi-linear, elliptic, of order 4 in $f_{\varepsilon}$, and its coefficients do not depend on $\varepsilon$.

As a consequence, according to the technical lemma 34, there is some positive constant $c$ such that
$$\begin{aligned}
\left\|\left(L+Q^{(2)}\right)\left(f_{\varepsilon}\right)\right\|_{\mathcal{C}^{1, \alpha}\left(K^{\prime}\right)} & \leq\left\|\lambda_{\varepsilon}\right\|_{\mathcal{C}^{1, \alpha}\left(K^{\prime}\right)}+\left\|Q^{(1)}\left(f_{\varepsilon}\right)\right\|_{\mathcal{C}^{1, \alpha}\left(K^{\prime}\right)} \\
& \leq\left\|\lambda_{\varepsilon}\right\|_{\mathcal{C}^{1, \alpha}\left(K^{\prime}\right)}+c\left\|f_{\varepsilon}\right\|_{\mathcal{C}^{4, \alpha}\left(K^{\prime}\right)} .
\end{aligned}$$
Now, according to lemma 34, $\left(L+Q^{(2)}\right) f_{\varepsilon}$ is a fourth-order elliptic operator, quasilinear, and the coefficients, which depend on $f_{\varepsilon}$, are in $\mathcal{C}^{4, \alpha}\left(K^{\prime}\right)$; since $\left\|f_{\varepsilon}\right\|_{\mathcal{C}^{4, \alpha}\left(K^{\prime}\right)} \xrightarrow{\varepsilon \rightarrow 0} 0$, this operator is really a quasilinear perturbation of the linear elliptic operator $L$.

More precisely, we can rewrite (51) under the form
$$\sum_{|\alpha|=4} a_{\alpha}\left(x, \partial f_{\varepsilon}, \partial^{2} f_{\varepsilon}, \partial^{3} f_{\varepsilon}\right) \partial_{\alpha}^{4} f_{\varepsilon}=G\left(x, \partial f_{\varepsilon}, \partial^{2} f_{\varepsilon}, \partial^{3} f_{\varepsilon}\right)$$
where the operator
$$\sum_{|\alpha|=4} a_{\alpha}(x, 0,0,0) \partial_{\alpha}^{4} u$$
is linear elliptic. Thus, for $\varepsilon$ small enough, $\left\|f_{\varepsilon}\right\|_{\mathcal{C}^{4, \alpha}\left(K^{\prime}\right)}$ is sufficiently small for the left-hand side of (52) to still be elliptic, with coefficients bounded in $\mathcal{C}^{1, \alpha}$. Thus, elliptic regularity results (see Morrey [35]) imply that
$$\left.\left\|f_{\varepsilon}\right\|\right|_{\mathcal{C}^{5, \alpha}(K)} \leq c_{2}\left(\left\|\left(L+Q^{(2)}\right)\left(f_{\varepsilon}\right)\right\|_{\mathcal{C}^{1, \alpha}\left(K^{\prime}\right)}+\left.\left\|f_{\varepsilon}\right\|\right|_{\mathcal{C}^{0}\left(K^{\prime}\right)}\right)$$

Since we know that $\left\|f_{\varepsilon}\right\|_{\mathcal{C}^{4, \alpha}\left(K^{\prime}\right)} \xrightarrow{\varepsilon \rightarrow 0} 0$, we know, in particular, that $\left.\left.\left\|f_{\varepsilon}\right\|\right|_{\mathcal{C}^{0}(K)}\right) \xrightarrow{\varepsilon \rightarrow 0} 0$. For $\varepsilon$ small enough, the above estimate rewrites
$$\left.\left\|f_{\varepsilon}\right\|\right|_{\mathcal{C}^{5}, \alpha}(K) \leq c_{3}\left(\left\|\lambda_{\varepsilon}\right\|_{\mathcal{C}^{1, \alpha}\left(K^{\prime}\right)}+\left\|f_{\varepsilon}\right\|_{\mathcal{C}^{4, \alpha}\left(K^{\prime}\right)}\right) .$$

Thus, we have obtained that on every compact set $K \subset M^{*},\left.\left\|f_{\varepsilon}\right\|\right|_{\mathcal{C}^{5, \alpha}(K)} \xrightarrow{\varepsilon \rightarrow 0} 0$.
It remains to show the induction step, which works in the exact same way. Assume, by induction hypothesis, that for every compact set $K^{\prime} \subset M^{*},\left\|f_{\varepsilon}\right\|_{\mathcal{C}^{k, \alpha}\left(K^{\prime}\right)} \xrightarrow{\varepsilon \rightarrow 0} 0$. Let $K \subset M^{*}$ a compact subset, we want to show that $\left\|f_{\varepsilon}\right\|_{\mathcal{C}^{k+1, \alpha}(K)} \xrightarrow{\varepsilon \rightarrow 0} 0$. Let $K^{\prime}$ be a slightly bigger compact subset of $M^{*}$. Choosing $\varepsilon$ small enough, we see that $f_{\varepsilon}$ is solution of (51) on $K^{\prime}$. We then go through the same steps to obtain the desired result, in a boostrap-type reasoning. The coefficients of the operator $\left(L+Q^{(2)}\right)\left(f_{\varepsilon}\right)$ are then in $\mathcal{C}^{k, \alpha}\left(K^{\prime}\right)$ by induction hypothesis, ensuring we may use the elliptic regularity theorem at each step. \(\square\)