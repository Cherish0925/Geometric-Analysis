---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: ALE scalar-flat Kähler metrics on non-compact weighted projective spaces]

Lemma 13. The potential function $U_{\mathbf{a}}$ of (3.38) is given by
$$U_{\mathbf{a}}=\tilde{U}^{0}\left(x_{1}, \ldots, x_{\ell}\right)+\sum_{j=1}^{\ell} \frac{1}{r_{j}}\left(\frac{a_{0} \cdots a_{\ell}}{a_{j}}\right) x_{j} U^{j}\left(x_{1}^{j}, \ldots, x_{n_{j}}^{j}\right),$$
where $\tilde{U}^{0}$ and $U^{j}$ are the potentials respectively given by (3.28) and (3.33).
Proof. Recall from the general theory [20] that $U_{\mathbf{a}}\left(x_{1}, \ldots, x_{m}\right)$ can be determined from an invariant Kähler potential $H\left(x_{1}, \ldots, x_{m}\right)$ for (3.38), via a Legendre transform. Specifically, if $H_{\mathbf{a}}$ is a function in $\left(x_{1}, \ldots, x_{m}\right)$ satisfying $d d^{c} H_{\mathbf{a}}=\omega_{\mathbf{a}}$, and $\left(d y_{1}+i d t_{1}, \ldots, d y_{m}+i d t_{m}\right)$ are holomorphic $(1,0)$-forms which form a dual basis
to the the $(1,0)$-parts of the Killing fields $\partial / \partial t_{i}$, then we can take
$$U_{\mathbf{a}}\left(x_{1}, \ldots, x_{m}\right)=\sum_{p=1}^{m} y_{p} x_{p}-H\left(x_{1}, \ldots, x_{m}\right) .$$
The functions $y_{q}$ are in turn given by $y_{q}=\frac{\partial U_{\mathbf{a}}}{\partial x_{q}}$. In our situation, a Kähler potential for (3.7) can be constructed as follows. Let
$$H^{0}\left(x_{1}, \ldots, x_{\ell}\right):=\sum_{j=1}^{\ell} x_{j} \frac{\partial \tilde{U}^{0}}{\partial x_{j}}-\tilde{U}^{0}\left(x_{1}, \ldots, x_{\ell}\right)$$
be a fibre-wise Kähler potential. Then, by using (3.27) to express the action of $J_{\mathbf{a}}$ on $d x_{i}$ and (3.2), we have
$$\begin{aligned}
d d^{c} H^{0} & =d\left(J_{\mathbf{a}} \sum_{j, i=1}^{\ell} x_{j} \frac{\partial^{2} \tilde{U}^{0}}{\partial x_{i} \partial x_{j}} d x_{i}\right) \\
& =d\left(\sum_{i, j, r=1}^{\ell} x_{j}\left(\operatorname{HessU}^{0}\right)_{i j}\left(\operatorname{Hess}\left(U^{0}\right)\right)_{i r}^{-1} \tilde{\theta}_{r}\right) \\
& =d\left(\sum_{j=1}^{\ell} x_{j} \tilde{\theta}_{j}\right)=\omega_{\mathbf{a}}
\end{aligned}$$
Thus, $U_{\mathbf{a}}$ is given by a Legendre transform of $H^{0}$ with respect to the full set of momentum coordinates $\left(x_{1}, \ldots, x_{\ell} ; \hat{x}_{k_{j}}^{j}\right)$. The set of pluriharmonic functions $\left(y_{1}, \ldots, y_{\ell} ; y_{k_{j}}^{j}\right)$ corresponding to the Killing fields $\left(X_{j}, \hat{X}_{k_{j}}^{j}\right)$ can be constructed as follows: $y_{k}^{j}:=\frac{\partial U^{j}}{\partial x_{k}^{j}}$ is the pull-back to $\stackrel{\circ}{M}$ of the pluriharmonic coordinates on each $\mathbb{C} P^{n_{j}}$, whereas
$$y_{j}:=-\frac{1}{r_{j}}\left(\frac{a_{0} \cdots a_{\ell}}{a_{j}}\right) H^{j}+\frac{\partial \tilde{U}^{0}}{\partial x_{j}},$$
with
$$H^{j}\left(x_{1}^{j}, \ldots, x_{n_{j}}^{j}\right):=\sum_{k=1}^{n_{j}} x_{k}^{j} \frac{\partial U^{j}}{\partial x_{k}^{j}}-\tilde{U}^{j}\left(x_{1}^{j}, \ldots, x_{n_{j}}^{j}\right)=-\frac{1}{2} r_{j} \log \left(1-\sum_{k=1}^{n_{j}} x_{k}^{j}\right)$$
being a Kähler potential for the normalized Fubini-Study metric $g_{\mathbb{C} P^{n_{j}}}$. (Similar calculation as in (3.40) shows that $y_{j}$ are pluriharmonic and that $\left(d y_{j}, d y_{k_{j}}^{j}\right)$ form
a dual basis for $\left(J_{\mathbf{a}} X_{j}, J_{\mathbf{a}} \hat{X}_{k_{j}}^{j}\right)$.) It then follows that
$$\begin{aligned}
U_{\mathbf{a}}^{0}= & -H^{0}+\sum_{j=1}^{\ell}\left(y_{j} x_{j}+\sum_{k_{j}=1}^{n_{j}} y_{k_{j}}^{j} \hat{x}_{k_{j}}^{j}\right) \\
= & \left(-H^{0}+\sum_{j=1}^{\ell} x_{j} \frac{\partial \tilde{U}^{0}}{\partial x_{j}}\right) \\
& +\sum_{j=1}^{\ell} \frac{x_{j}}{r_{j}}\left(\frac{a_{0} \cdots a_{\ell}}{a_{j}}\right)\left(-H^{j}+\sum_{k_{j}=1}^{n_{j}} y_{k_{j}}^{j} x_{k_{j}}^{j}\right) \\
= & \tilde{U}^{0}\left(x_{1}, \ldots, x_{\ell}\right)+\sum_{j=1}^{\ell} \frac{x_{j}}{r_{j}}\left(\frac{a_{0} \cdots a_{\ell}}{a_{j}}\right) U^{j}\left(x_{1}^{j}, \ldots, x_{n_{j}}^{j}\right) .
\end{aligned}$$ \(\square\)

We are now ready prove our main technical result
Proposition 14. Let $a_{0}, a_{1}<a_{2}<\cdots<a_{\ell}$ be any positive integer numbers, $n_{0}:=\ell$ and $n_{j}, j=1, \ldots, \ell$ non-negative integers with $\sum_{j=0}^{\ell} n_{j}=m$. Consider the unbounded simplex in $\mathbb{R}^{m}$
$$\stackrel{\circ}{\mathrm{P}}_{m}=\left\{\left(\tilde{x}_{1}^{0}, \ldots, \tilde{x}_{\ell}^{0} ; \tilde{x}_{1}^{1}, \ldots, \tilde{x}_{n_{1}}^{1} ; \ldots ; \tilde{x}_{1}^{\ell}, \ldots, \tilde{x}_{n_{\ell}}^{\ell}\right): \tilde{x}_{k_{j}}^{j}>0, \sum_{j=0}^{\ell}\left(\sum_{k_{j}=1}^{n_{j}} \tilde{x}_{k_{j}}^{j}\right)>1\right\} .$$
Then, the restriction of the scalar-flat Kähler metric (3.7) to $\stackrel{\circ}{M}_{\mathbf{a}} \cong \stackrel{\circ}{P}_{m} \times T^{m}$ can be written in the form (3.38) for a symplectic potential $\tilde{U}_{\mathbf{a}}\left(\tilde{x}_{1}, \ldots, \tilde{x}_{m}\right)$ given by Lemma 13, which satisfies the positivity and boundary conditions of [6, Prop. 1] at the faces of $\stackrel{\circ}{\mathrm{P}}_{m}$, with respect to the inward normals
$$v_{k_{j}}^{j}=\left(\frac{a_{0} \cdots a_{\ell}}{a_{j}}\right) e_{k_{j}}^{j}, \quad j=0, \ldots \ell, k_{j}=1, \ldots, n_{j}, v_{0}=\left(\frac{a_{0} \cdots a_{\ell}}{a_{0}}\right)\left(\sum_{j=0}^{\ell}\left(\sum_{k_{j}=1}^{n_{j}} e_{k_{j}}^{j}\right)\right),$$
where $e_{k_{j}}^{j}$ denotes the standard basis of $\mathbb{R}^{m}=\prod_{j=0}^{\ell} \mathbb{R}^{n_{j}+1}$.
Proof. Equivalent to (3.16) is the criterion [2, Thm. 2] (established in [1, App. A], see also [6, Lemma 2]) expressed in terms of the asymptotics of $\tilde{U}_{\mathbf{a}}$ and $\operatorname{det}\left(\operatorname{Hess}\left(\tilde{U}_{\mathbf{a}}\right)\right)^{-1}$ near the boundary of $\mathrm{P}_{m}$, which we shall now elaborate on. (This has also the advantage to deal with the boundary and positivity conditions of [6] at once.)

First of all, as $\tilde{U}^{0}$ satisfies (3.16) with the normals $v_{j}$, it follows from [2, Thm. 2] that near the boundary of $\mathrm{P}_{\ell}$,
$$\begin{aligned}
\tilde{U}^{0}= & \frac{1}{2}\left[\sum_{j=1}^{\ell}\left(\frac{a_{0} \ldots a_{\ell}}{a_{j}}\right) x_{j} \log x_{j}+\left(\frac{a_{0} \ldots a_{\ell}}{a_{0}}\right)\left(\sum_{j=1}^{\ell} x_{j}-1\right) \log \left(\sum_{j=1}^{\ell} x_{j}-1\right)\right] \\
& + \text { smooth }
\end{aligned}$$
so that
$$\begin{aligned}
U_{\mathbf{a}}= & \frac{1}{2}\left[\sum_{j=1}^{\ell}\left(\frac{a_{0} \cdots a_{\ell}}{a_{j}}\right) x_{j}\left(\left(\sum_{k_{j}=1}^{n_{j}} x_{k_{j}}^{j} \log x_{k_{j}}^{j}\right)+\left(1-\sum_{k_{j}=1}^{n_{j}} x_{k_{j}}^{j}\right) \log \left(1-\sum_{k_{j}=1}^{n_{j}} x_{k_{j}}^{j}\right)\right)\right. \\
& \left.+\sum_{j=1}^{\ell}\left(\frac{a_{0} \ldots a_{\ell}}{a_{j}}\right) x_{j} \log x_{j}+\left(\frac{a_{0} \ldots a_{\ell}}{a_{0}}\right)\left(\sum_{i=1}^{\ell} x_{i}-1\right) \log \left(\sum_{i=1}^{\ell} x_{i}-1\right)\right]+ \text { smooth } \\
= & \frac{1}{2}\left[\sum_{j=1}^{\ell}\left(\frac{a_{0} \cdots a_{\ell}}{a_{j}}\right)\left(\sum_{k_{j}=1}^{n_{j}} \tilde{x}_{k_{j}}^{j}\left(\log \tilde{x}_{k_{j}}^{j}-\log x_{j}\right)+\tilde{x}_{j}^{0}\left(\log \tilde{x}_{j}^{0}-\log x_{j}\right)\right)\right. \\
& \left.+\sum_{j=1}^{\ell}\left(\frac{a_{0} \ldots a_{\ell}}{a_{j}}\right) x_{j} \log x_{j}+\left(\frac{a_{0} \ldots a_{\ell}}{a_{0}}\right)\left(\sum_{j=0}^{\ell} \sum_{k_{j}=1}^{n_{j}} \tilde{x}_{k_{j}}^{j}-1\right) \log \left(\sum_{j=0}^{\ell} \sum_{k=1}^{n_{j}} \tilde{x}_{k_{j}}^{j}-1\right)\right] \\
& +\operatorname{smooth}=\frac{1}{2}\left[\sum_{j=1}^{\ell}\left(\frac{a_{0} \cdots a_{\ell}}{a_{j}}\right)\left(\sum_{k_{j}=1}^{n_{j}} \tilde{x}_{k_{j}}^{j} \log \tilde{x}_{k_{j}}^{j}\right)\right. \\
& \left.+\left(\frac{a_{0} \ldots a_{\ell}}{a_{0}}\right)\left(\sum_{j=0}^{\ell} \sum_{k_{j}=1}^{n_{j}} \tilde{x}_{k_{j}}^{j}-1\right) \log \left(\sum_{j=0}^{\ell} \sum_{k_{j}=1}^{n_{j}} \tilde{x}_{k_{j}}^{j}-1\right)\right]+ \text { smooth, }
\end{aligned}$$
where, we recall, we have set $n_{0}:=\ell$ in the summation in the last term.
Formula (3.38) shows that the determinant $\left.\operatorname{det}\left(\operatorname{Hess}\left(\tilde{U}_{\mathbf{a}}\right)\right)^{-1}\right)$ is, up to a positive constant, the norm with respect to $g_{\mathbf{a}}$ of the wedge product
$$\left(\bigwedge_{j=1}^{\ell} X_{j}\right) \wedge\left(\bigwedge_{j=1}^{\ell}\left(\bigwedge_{k_{j}=1}^{n_{j}} \hat{X}_{k_{j}}^{j}\right)\right)$$
of the Killing vector fields $\left(X_{1}, \cdots, X_{\ell}, \hat{X}_{k_{j}}^{j}\right)$. By (3.25), $X_{1} \wedge \cdots \wedge X_{\ell}$ is a multiple of $K_{1} \wedge \cdots \wedge K_{\ell}$, so that using (3.34), we have
$$\left(\bigwedge_{j=1}^{\ell} X_{j}\right) \wedge\left(\bigwedge_{j=1}^{\ell}\left(\bigwedge_{k_{j}=1}^{n_{j}} \hat{X}_{k_{j}}^{j}\right)\right)=\left(\bigwedge_{j=1}^{\ell} X_{j}\right) \wedge\left(\bigwedge_{j=1}^{\ell}\left(\bigwedge_{k_{j}=1}^{n_{j}}\left(X_{k_{j}}^{j}\right)^{H}\right)\right) .$$
Using the form (3.27) of the metric, one sees that with respect to $g_{\mathbf{a}}$
\begin{itemize}
\item[-] $X_{i}$ is orthogonal to $\left(X_{k}^{j}\right)^{H}$, and $\left(X_{k}^{j}\right)^{H}$ is orthogonal with $\left(X_{p}^{r}\right)^{H}$ if $j \neq r$.
\item[-] $g_{\mathbf{a}}\left(\left(X_{k}^{j}\right)^{H},\left(X_{p}^{j}\right)^{H}\right)=C_{j} x_{j} g_{\mathbb{C} P^{n_{j}}}\left(X_{k}^{j}, X_{p}^{j}\right)$,
\end{itemize}
where $C_{j}$ is a positive constant. It then follows that
$$\left.\operatorname{det}\left(\operatorname{Hess}\left(U_{\mathbf{a}}\right)\right)^{-1}\right)=C\left(\prod_{j=1}^{\ell} x_{j}^{n_{j}}\right)\left(\operatorname{det} \mathbf{H}^{0}\right)\left(\operatorname{det} \mathbf{H}^{j}\right),$$
where $\mathbf{H}^{j}=\operatorname{Hess}\left(U^{j}\right)^{-1}$ and $C$ is a positive constant. Using [2, Thm. 2] (see also [6, Rem. 4(ii)]), we get
$$\begin{aligned}
\left.\operatorname{det}\left(\operatorname{Hess}\left(U_{\mathbf{a}}\right)\right)^{-1}\right) & =\delta\left(\sum_{j=1}^{\ell} x_{j}-1\right) \prod_{j=1}^{\ell} x_{j}^{n_{j}+1}\left(\left(1-\sum_{k_{j}=1}^{n_{j}} x_{k_{j}}^{j}\right) \prod_{k_{j}=1}^{n_{j}} x_{k_{j}}^{j}\right) \\
& =\delta\left(\sum_{j=0}^{\ell} \sum_{k_{j}=1}^{n_{j}} \tilde{x}_{k_{j}}^{j}-1\right) \prod_{j=0}^{\ell} \prod_{k_{j}=1}^{n_{j}} \tilde{x}_{k_{j}}^{j},
\end{aligned}$$
where $\delta$ is a smooth positive function extended to the closure $\mathrm{P}_{m}$ of $\stackrel{\circ}{\mathrm{P}}_{m}$; by [2, Thm. 2] and [6, Rem. 4(ii)] we conclude the proof. \(\square\)

Corollary 15. The Kähler metric (3.7) gives rise to a scalar-flat Kähler metric $\left(g_{\mathbf{a}}, J_{\mathbf{a}}, \omega_{\mathbf{a}}\right)$ on the non-compact weighted projective space $M_{\mathbf{a}}=\mathbb{C} P_{-a_{0}, a_{1}, \ldots, a_{1}, \ldots, a_{\ell}, \ldots, a_{\ell}}^{m}$, where each positive integer $a_{j}$ is counted $\left(1+n_{j}\right)$-times.

Proof. Rescalling the metric (3.7) by a factor $\lambda_{\mathbf{a}}=\frac{1}{a_{0}^{n_{0}} \ldots a_{\ell}^{n_{\ell}}}$ leads to a homothety by factor $\lambda_{\mathbf{a}}$ in momenta, i.e. the Kähler metric is defined over $\lambda_{\mathbf{a}}\left(\stackrel{\circ}{\mathrm{P}}_{m}\right) \times T^{m}$ and its symplectic potential satisfies the boundary conditions of [6, Prop. 1] with respect to the inward normals $\left(v_{0}, v_{k_{j}}^{j}\right)$ of Proposition 14. Using the affine transformation $\frac{1}{\lambda_{\mathbf{a}}} \mathrm{Id}$ of $\mathbb{R}^{m}$, the labeled polytope $\lambda_{\mathbf{a}}\left(\stackrel{\circ}{\mathrm{P}}_{m}\right)$ transforms to $\stackrel{\circ}{\mathrm{P}}_{m}$ equipped with inward labelled normals
$$\tilde{v}_{k}^{j}=\left(\frac{a_{0}^{n_{0}} \cdots a_{\ell}^{n_{\ell}}}{a_{j}}\right) e_{k}^{j},$$
which are consistent with Lemma 8. By the extension criterion of [2, 6], (3.7) thus gives rise to an orbifold Kähler metric on $M_{\mathbf{a}}=\mathbb{C} P_{-a_{0}, a_{1}, \ldots, a_{1}, \ldots, a_{\ell}, \ldots, a_{\ell}}^{m}$.

Geometrically, the normals appearing in Proposition 14 give rise to an orbifold Kähler metric defined on the orbifold quotient of $M_{\mathbf{a}}$ by the cyclic group of order $\frac{1}{\lambda_{\mathrm{a}}}$. Properly rescalled, this Kähler metric pulls back to define an orbifold Kähler metric on $M_{\mathbf{a}}$, compatible with symplectic form described in Lemma 8. \(\square\)

Remark 16. (1) We note that the arguments we used to derive Proposition 14 do not require that the positive reals $a_{0}, a_{1}, \ldots, a_{\ell}$ parametrizing the construction are all integers. In fact, we have used the boundary conditions (3.16) of [6, Prop. 1], which can be formulated with respect to any inward normals $v_{j}$ to $\stackrel{\circ}{\mathrm{P}}_{m}$, belonging to a lattice or not. Thus, Proposition 14 provides solutions of the scalar-flat Abreu equation on $\stackrel{\circ}{\mathrm{P}}_{m}$, satisfying the boundary conditions corresponding to the weighted inward normals
$$\left\{\left(\frac{b_{0} \cdots b_{m}}{b_{j}}\right) e_{j}, j=1, \ldots, m ;\left(\frac{b_{0} \cdots b_{m}}{b_{0}}\right)\left(e_{1}+\cdots+e_{m}\right)\right\},$$
for any positive real numbers $b_{0}, \ldots, b_{m}$. Such solutions might be useful when applying the continuity method as in [17], or when considering Sasaki analogues of this construction, see e.g. [24]. Such metrics can also be thought of as examples of scalar-flat Kähler metrics with edge singularities along complex hyper-surfaces, in the sense of [18, 26] (see also [28] for an overview), defined on the total space of the tautological vector bundle $\mathcal{O}(-1) \rightarrow \mathbb{C} P^{m-1}$ viewed as a toric manifold with Delzant polytope $\mathrm{P}_{m}$ (e.g. via Lemma 8 with all $a_{i}=1$ ).
(2) As we mentioned along the way, one can let all $n_{j}=0$, in which case the metric (3.7) reduces to its vertical part and gives rise to an orthotoric scalar-flat Kähler metric on $\mathbb{C} P_{-a_{0}, a_{1}, \ldots, a_{\ell}}$.
(3) Up to a homothety, the symplectic form $\omega_{\mathbf{a}}$ coincides with the symplectic form $\omega^{0}$ on $M_{\mathbf{a}}$ obtained by the Delzant construction (see Lemma 8) whereas the complex structures $J_{\mathbf{a}}$ and $J^{0}$ are pointwise different. However, there is a standard way to identify equivariantly two $T^{m}$-invariant and $\omega^{0}$-compatible complex structures $J_{\mathbf{a}}$ and $J^{0}$ on any toric manifold (see e.g. [2]): to this end, one can use the potential function $\tilde{U}_{\mathbf{a}}$ on $\stackrel{\circ}{P}_{m}$ for the scalar-flat Kähler metric $\left(g_{\mathbf{a}}, J_{\mathbf{a}}\right)$, as defined in (3.38), and let $\tilde{y}_{i}:=\partial \tilde{U}_{\mathbf{a}} / \partial \tilde{x}_{i}$ as in the proof of Lemma 13; similarly, the quotient metric $g^{0}$ obtained via the Delzant quotient construction can be written in the form (3.38) with respect to a potential $\tilde{U}_{\mathbf{a}}^{0}$, and we put $\tilde{y}_{i}^{0}:=\partial \tilde{U}_{\mathbf{a}}^{0} / \partial \tilde{x}_{i}$. On thus obtains on $\stackrel{\circ}{M}_{\mathbf{a}} \subset M_{\mathbf{a}}$ holomorphic coordinate systems $\left(\tilde{y}_{i}+i \tilde{t}_{i}\right)$ and $\left(\tilde{y}_{i}^{0}+i \tilde{t}_{i}\right)$ for $J_{\mathbf{a}}$ and $J^{0}$, respectively, and thus a $T^{m}$-equivariant diffeomorphism $\Phi_{0}:\left(\tilde{y}_{i}+i \tilde{t}_{i}\right) \rightarrow\left(\tilde{y}_{i}^{0}+i \tilde{t}_{i}\right)$ which sends $J_{\mathbf{a}}$ to $J^{0}$ (on $\stackrel{\circ}{M}$ ) but which does not preserve $\omega_{\mathbf{a}}$. It then can be shown that $\Phi_{0}$ extends (equivariantly) to a biholomorphism from $\left(M_{\mathbf{a}}, J_{\mathbf{a}}\right)$ to $\left(M_{\mathbf{a}}, J^{0}\right)=$ $\mathbb{C} P_{-a_{0}, a_{1}, \ldots, a_{m}}^{m}$. \(\square\)
3.3. Behaviour of the metric at infinity. In order to complete the proof of Theorem A, we have to show that $\left(g_{\mathbf{a}}, J_{\mathbf{a}}, \omega_{\mathbf{a}}\right)$ is an ALE metric, i.e. that $\left(M_{\mathbf{a}}, J_{\mathbf{a}}\right)$ is biholomorphic to $\mathbb{C}^{m} / \Gamma_{\mathbf{a}}$ outside a compact subset, and estimate the Kähler potential of $\omega_{\mathbf{a}}$ in terms of the potential $\frac{1}{4}\|z\|^{2}$ of the standard flat metric on $\mathbb{C}^{m}$.

Proposition 17. The scalar-flat Kähler metric $g_{\mathbf{a}}$ on $\mathbb{C} P_{-a_{0}, a_{1}, \ldots, a_{m}}^{m}$ admits a chart at infinity, which is biholomorphic to the complement of a compact subset of $\mathbb{C}_{\mathbf{a}}^{m}=$ $\mathbb{C}^{m} / \Gamma_{\mathbf{a}}$, and such that a Kähler potential $H$ for the Kähler form $\omega_{\mathbf{a}}$ is written as
$$H=\frac{1}{4}\|z\|^{2}+A\|z\|^{4-2 m}+O\left(\|z\|^{3-2 m}\right)$$
when $m \geq 3$ and
$$H=\frac{1}{4}\|z\|^{2}+A \log \|z\|+O\left(\|z\|^{-2}\right)$$
when $m=2$, where $\|z\|^{2}$ is the square norm function on $\mathbb{C}^{m}$, also viewed as 4 times the Kähler potential of the standard flat metric on $\mathbb{C}^{m}$. Furthermore, the real constant $A=0$ iff $a_{0}=\sum_{j=1}^{m} a_{j}$, i.e. the metric $g_{\mathbf{a}}$ is Ricci-flat.

Proof. The proof will be done in a similar way as we proceeded in Section 2, namely by comparing the metric $g_{\mathbf{a}}$ given by (3.7) to the flat Kähler metric obtained by the same ansatz.

Given a choice of $\mathbf{a}=\left(a_{0}, \ldots, a_{\ell}\right)$ where $a_{i}$ are positive integers with $a_{1}<\ldots<$ $a_{\ell}$, we have already observed in Sect. 3.1 that letting $F_{1}(x)=\cdots=F_{\ell}(x)=p(x)$ in (3.7) and taking $\xi_{\ell} \in\left(\alpha_{\ell}, \infty\right)$, one gets a flat Kähler metric $\left(g_{\mathbf{a}}^{f}, J_{\mathbf{a}}^{f}, \omega_{\mathbf{a}}^{f}\right)$. The analysis as we just did for $\left(g_{\mathbf{a}}, J_{\mathbf{a}}, \omega_{\mathbf{a}}\right)$ yields, mutatis mutandis, that $\left(g_{\mathbf{a}}^{f}, J_{\mathbf{a}}^{f}, \omega_{\mathbf{a}}^{f}\right)$ is defined on $\stackrel{\circ}{\mathrm{C}}_{m} \times T^{m}$, where $\stackrel{\circ}{\mathrm{C}}_{m} \subset \mathbb{R}^{m}$ is the cone
$$\stackrel{\circ}{\mathrm{C}}_{m}=\left\{\left(\tilde{x}_{1}^{0}, \ldots, \tilde{x}_{\ell}^{0} ; \tilde{x}_{1}^{1}, \ldots, \tilde{x}_{n_{1}}^{1} ; \ldots ; \tilde{x}_{1}^{\ell}, \ldots, \tilde{x}_{n_{\ell}}^{\ell}\right): \tilde{x}_{k_{j}}^{j}>0, j=0, \ldots, \ell, k_{j}=1, \ldots, n_{j}\right\},$$
and satisfies the boundary conditions with respect to the normals
$$v_{k_{j}}^{j}=\left(\frac{a_{0} \cdots a_{\ell}}{a_{j}}\right) e_{k_{j}}^{j}, \quad j=0, \ldots \ell, k_{j}=1, \ldots, n_{j} .$$

The normals $\left(v_{k_{j}}^{j}\right)$ form a basis of $\mathbb{C}^{m}$, so they span a lattice $\Lambda_{\mathbf{a}}^{0}$. With respect to it, $\left(\dot{\mathrm{C}}_{m}, \Lambda_{\mathbf{a}}^{0}\right)$ is the Delzant polytope associated to the standard toric $\mathbb{C}^{m}$ and $\left(g_{\mathbf{a}}^{f}, J_{\mathbf{a}}^{f}, \omega_{\mathbf{a}}^{f}\right)$ is just the (standard) flat toric metric. It is a well-known (and easy to show) fact that the square-norm function $\|z\|^{2}$ on $\mathbb{C}^{m}$ is expressed in terms of the momenta as
$$\|z\|^{2}=2 \sum_{j=0}^{\ell} \sum_{k_{j}=1}^{n_{j}}\left(\frac{a_{0} \cdots a_{\ell}}{a_{j}}\right) \tilde{x}_{k}^{j} .$$

By Proposition 14 (see also the proof of Corollary 15), the Delzant image of the toric manifold $\left(M_{\mathbf{a}}, \omega_{\mathbf{a}}, J_{\mathbf{a}}\right)$ is $\mathrm{P}_{m} \subset \mathrm{C}_{m}$, whereas the corresponding lattice $\Lambda_{\mathbf{a}}$ is spanned by the normals $\left(v_{k_{j}}^{j}\right)$ as above plus one additional normal $v_{0}$. It follows that $\Lambda_{\mathbf{a}}^{0} \subset \Lambda_{\mathbf{a}}$. Note that $\Lambda_{\mathbf{a}} / \Lambda_{\mathbf{a}}^{0} \cong \Gamma_{\mathbf{a}}$, where $\Gamma_{\mathbf{a}}$ is the abelian group defined in Theorem A. Another look at the Delzant construction shows that the orbifold associated to $\left(\stackrel{\circ}{\mathrm{C}}_{m}, \Lambda_{\mathbf{a}}\right)$ is nothing but the orbifold quotient (see also [6, Rem. 2])
$$\mathbb{C}_{\mathbf{a}}^{m}:=\mathbb{C}^{m} / \Gamma_{\mathbf{a}}$$
so that we can think of $\left(g_{\mathbf{a}}^{f}, J_{\mathbf{a}}^{f}, \omega_{\mathbf{a}}^{f}\right)$ as the standard flat metric on $\mathbb{C}^{m} / \Gamma_{\mathbf{a}}$. We shall use the inclusion $\stackrel{\circ}{\mathrm{P}}_{m} \subset \stackrel{\circ}{\mathrm{C}}_{m}$, which in term of $\left(\xi_{1}, \ldots, \xi_{\ell}\right)$ becomes
$$\left(\alpha_{1}, \alpha_{2}\right) \times \cdots \times\left(\alpha_{\ell-1}, \alpha_{\ell}\right) \times(0, \infty) \subset\left(\alpha_{1}, \alpha_{2}\right) \times \cdots \times\left(\alpha_{\ell-1}, \alpha_{\ell}\right) \times\left(\alpha_{\ell}, \infty\right),$$
in order to compare the restrictions of $g_{\mathbf{a}}^{f}$ and $g_{\mathbf{a}}$ to the common subset
$$\left(M_{\mathbf{a}}^{0}\right)_{\lambda}:=\left(\alpha_{1}, \alpha_{2}\right) \times \cdots \times\left(\alpha_{\ell-1}, \alpha_{\ell}\right) \times(\lambda, \infty) \times P_{\mathbf{a}}$$
for some $\lambda>0$. Noting that $\xi_{\ell}$ extends as a smooth function on $\left(M_{\mathbf{a}}\right)_{\lambda}$ and $\left(\mathbb{C}_{\mathbf{a}}^{m}\right)_{\lambda}$ (as it is a simple root of the polynomial $\prod_{j=1}^{\ell}\left(t-\xi_{j}\right)=t^{\ell}-\sigma_{1} t^{\ell-1}+\cdots+$ $(-1)^{\ell} \sigma_{\ell}$ which has smooth coefficients equal to momenta), we denote respectively by $\left(\mathbb{C}_{\mathbf{a}}^{m}\right)_{\lambda} \subset \mathbb{C}_{\mathbf{a}}^{m}$ and $\left(M_{\mathbf{a}}\right)_{\lambda} \subset M_{\mathbf{a}}$ the pre-images of $(\lambda, \infty)$ by the smooth function $\xi_{\ell}$, which are complements of compact subsets in $M_{\mathbf{a}}$ and $\mathbb{C}_{\mathbf{a}}^{m}$, respectively. Our objective then will be to find a $T^{m}$-equivariant biholomorphism $\Phi:\left(\left(M_{\mathbf{a}}\right)_{\lambda}, J_{\mathbf{a}}\right) \rightarrow$ $\left(\mathbb{C}_{\mathbf{a}}^{m}\right)_{\lambda}$ and evaluate at infinity $\left(\Phi^{-1}\right)^{*}\left(\omega_{\mathbf{a}}-\omega_{\mathbf{a}}^{f}\right)$.

By [5, Thm. 1, (65) \& (70)], Kähler potentials $H^{f}(\xi), H(\xi)$ for $\left(J_{\mathbf{a}}^{f}, \omega_{\mathbf{a}}^{f}\right)$ and $\left(J_{\mathbf{a}}, \omega_{\mathbf{a}}\right)$, respectively, are given by
$$\begin{aligned}
H^{f}(\xi) & =\sum_{j=1}^{\ell}\left(\sum_{r=0}^{\ell}(-1)^{r} \alpha_{j}^{\ell-r} \sigma_{r}^{\alpha}\right) H^{j}+\sum_{j=1}^{\ell} \int_{\alpha_{j}}^{\xi_{j}} \frac{p_{c}(t) \Theta(t)}{p(t)} d t \\
& =\frac{1}{2}\left(\sum_{j=1}^{\ell} \xi_{j}-\sigma_{1}^{\alpha}\right)=\frac{1}{2}\left(\sigma_{1}-\sigma_{1}^{\alpha}\right)=\frac{1}{2} \sum_{j=1}^{\ell}\left(\frac{a_{0} \cdots a_{\ell}}{a_{j}}\right) x_{j} \\
& =\frac{1}{2} \sum_{j=0}^{\ell} \sum_{k_{j}=1}^{n_{j}}\left(\frac{a_{0} \cdots a_{\ell}}{a_{j}}\right) \tilde{x}_{k}^{j}=\frac{1}{4}\|z\|^{2}
\end{aligned}$$
$$\begin{aligned}
H(\xi) & =\frac{1}{2}\left(\sum_{j=1}^{\ell} \xi_{j}-\sigma_{1}^{\alpha}+\int_{\lambda}^{\xi_{\ell}}\left(\frac{p(x)}{F_{\ell}(x)}-1\right) d x\right) \\
& =\frac{1}{4}\|z\|^{2}-\int_{\lambda}^{\xi_{\ell}} \frac{a x+b}{F_{\ell}(x)} d x
\end{aligned}$$
where we have used the expression (3.43) for the square norm function $\|z\|^{2}$ on $\mathbb{C}^{m}$. In the above equalities, $\sigma_{r}^{\alpha}$ stands for the $r$-th elementary symmetric function of $\left(\alpha_{1}, \ldots, \alpha_{\ell}\right)$, and $H^{j}$ denotes the Kähler potential (3.41). Comparing with the notation of [5], the r.h.s of the first line of each equality is given by $\sum_{r=0}^{\ell}(-1)^{r} \sigma_{r}^{\alpha} u_{r}$ where $u_{0}$ is the Kähler potential given by [5, (65)] whereas $u_{r}(r>0)$ are the pluriharmonic functions given by [5, (70)], and we have also used that in our case $p_{c}(t)=p(t) / \Theta(t)=\prod_{j=1}^{\ell}\left(t-\alpha_{j}\right)^{n_{j}}, F_{j}(t)=p(t)$ for $j=1, \ldots, \ell-1$, and $F_{\ell}(x)=$ $p(x)+a x+b$. (Recall that, by the classification of [5], in the flat case $a=b=0$.)

An important observation, which follows from the second and third lines in (3.44) is that
$$\sum_{j=1}^{\ell} \xi_{j}=\sigma_{1}^{\alpha}+\sum_{k=1}^{\ell}\left(\frac{a_{0} \cdots a_{\ell}}{a_{k}}\right) x_{k}=\sigma_{1}^{\alpha}+\frac{1}{2}\|z\|^{2} .$$
As $\left(\xi_{1}, \ldots, \xi_{\ell-1}\right) \in\left[\alpha_{1}, \alpha_{2}\right] \times \cdots \times\left[\alpha_{\ell-1}, \alpha_{\ell}\right]$ are bounded functions on $\left(M_{\mathbf{a}}\right)_{\lambda}=$ $\left(\mathbb{C}_{\mathbf{a}}^{m}\right)_{\lambda}, \frac{1}{2}\|z\|^{2}$ goes to $\infty$ with the same rate as $\xi_{\ell}$ does (recall that $\xi_{\ell}$ is smooth on $\left(M_{\mathbf{a}}\right)_{\lambda}$ as being a simple root of the polynomial $\prod_{j=1}^{\ell}\left(t-\xi_{j}\right)=t^{\ell}-\sigma_{1} t^{\ell-1}+\cdots+$ $(-1)^{\ell} \sigma_{\ell}$ whereas t $\xi_{1}, \ldots, \xi_{\ell-1}$ are at least continuous, see [5, Prop. 14]). In other words,
$$\xi_{\ell}=\frac{1}{2}\|z\|^{2}+O(1) .$$

It is shown in $[5,(70)]$ that pluriharmonic functions $y_{j}^{f}, y_{j}$ respectively for the almost-complex structures $J_{\mathbf{a}}^{f}$ and $J_{\mathbf{a}}$ on $\left(M_{\mathbf{a}}\right)_{\lambda}$ are given by
$$\begin{aligned}
y_{j}^{f}= & -\sum_{i=1}^{\ell}(-1)^{j} \alpha_{i}^{\ell-j} H^{i}-\sum_{i=1}^{\ell} \int^{\xi_{i}} \frac{(-1)^{j} x^{\ell-j}}{\Theta(x)} d x \\
y_{j}= & -\sum_{i=1}^{\ell}(-1)^{j} \alpha_{i}^{\ell-j} H^{i}-\sum_{i=1}^{\ell} \int^{\xi_{i}} \frac{(-1)^{j} x^{\ell-j} p(x)}{\Theta(x) F_{i}(x)} d x \\
= & -\sum_{i=1}^{\ell}(-1)^{j} \alpha_{i}^{\ell-j} H^{i}-\sum_{i=1}^{\ell} \int^{\xi_{i}} \frac{(-1)^{j} x^{\ell-j}}{\Theta(x)} d x \\
& +(-1)^{j} \int^{\xi_{\ell}} \frac{x^{\ell-j}\left(F_{\ell}(x)-p(x)\right)}{\Theta(x) F_{\ell}(x)} d x \\
= & y_{j}^{f}+(-1)^{j} \int^{\xi_{\ell}} \frac{x^{\ell-j}(a x+b)}{\Theta(x) F_{\ell}(x)} d x
\end{aligned}$$

Note that in the above formulae, $y_{j}^{f}$ and $y_{j}$ are determined modulo constants of integrations, an ambiguity which we fix by letting
$$\begin{aligned}
\tilde{y}_{k}^{f} & :=\sum_{i=1}^{\ell} \int^{\xi_{i}} \frac{\prod_{j \neq k}\left(x-\alpha_{j}\right)}{\Theta(x)} d x \\
& =\sum_{i=1}^{\ell} \log \left|\xi_{i}-\alpha_{k}\right| \\
\tilde{y}_{k} & :=\sum_{i=1}^{\ell} \int^{\xi_{i}} \frac{\prod_{j \neq k}\left(x-\alpha_{j}\right) p(x)}{\Theta(x) F_{i}(x)} d x \\
& =\sum_{i=1}^{\ell} \log \left|\xi_{i}-\alpha_{k}\right|-\int_{\lambda}^{\xi_{\ell}} \frac{a x+b}{\left(x-\alpha_{k}\right) F_{\ell}(x)} d x
\end{aligned}$$
where the products are defined over indices $j, k \in\{1, \ldots, \ell\}$.
As in the proof of Lemma 13, each set $\left(y_{1}^{f}, \ldots, y_{\ell}^{f}\right)$ (resp. $\left(y_{1}, \ldots, y_{\ell}\right)$ ) of pluriharmonic functions can be completed with the pull-backs of pluriharmonic functions $\left(y_{k_{j}}^{j}\right)$ on each factor $\mathbb{C} P^{n_{j}}$ and with respective angular coordinates $\left(t_{1}^{f}, \ldots, t_{m}^{f}\right)$ (resp. $\left(t_{1}, \ldots, t_{m}\right)$, so that $\left(y_{j}^{f}, y_{k_{j}}^{j}\right)$ (resp. $\left(y_{j}, y_{k_{j}}^{j}\right)$ ) form the $T^{m}$-invariant part of an adapted $T^{m}$-equivariant holomorphic chart on $\left(\stackrel{\circ}{\mathbb{C}}_{\mathbf{a}}^{m}\right)_{\lambda}\left(\operatorname{resp} .\left(\stackrel{\circ}{M}_{\mathbf{a}}\right)_{\lambda}\right)$. We are going to construct a $T^{m}$-equivariant diffeomorphism $\Phi$ on $\left(M_{\mathbf{a}}\right)_{\lambda}$ which maps $J_{\mathbf{a}}$ to $J_{\mathbf{a}}^{f}$ and satisfies
$$y_{r} \circ \Phi=y_{r}^{f} ; \quad y_{k_{j}}^{j} \circ \Phi=y_{k_{j}}^{j} ; \quad t_{k} \circ \Phi=t_{k}^{f}$$
As $\Phi$ acts trivially on $y_{k_{j}}^{j}$, it must be fibre-wise, i.e. defined by a diffeomorphism $\left(\varphi_{1}(\xi), \ldots, \varphi_{\ell}(\xi)\right):=\left(\xi_{1}, \ldots, \xi_{\ell}\right) \circ \Phi$, which we shall denote by $\Phi(\xi)$.

Using that
$$\prod_{j \neq k}\left(x-\alpha_{j}\right)=\sum_{j=1}^{\ell}(-1)^{j-1} \sigma_{j-1}^{\alpha}\left(\hat{\alpha}_{k}\right) x^{\ell-j},$$
where we recall that $\sigma_{j-1}^{\alpha}\left(\hat{\alpha}_{k}\right)$ denotes the $(j-1)$-th elementary symmetric function of the $(\ell-1)$ elements $\left\{\alpha_{1}, \ldots, \alpha_{\ell}\right\} \backslash\left\{\alpha_{k}\right\}$, and that for each $k=1, \ldots, \ell$
$$\sum_{j=1}^{\ell}(-1)^{j-1} \sigma_{j-1}^{\alpha}\left(\hat{\alpha}_{k}\right) y_{j}^{f}=\left(\sum_{j=1}^{\ell}(-1)^{j-1} \sigma_{j-1}^{\alpha}\left(\hat{\alpha}_{k}\right) y_{j}\right) \circ \Phi,$$
(3.48) implies that $\Phi(\xi)$ sends $\tilde{y}_{k}$ to $\tilde{y}_{k}^{f}$. Exponentiating (3.49), one finds that
$$\exp \left(-\int_{\lambda}^{\varphi_{\ell}(\xi)} \frac{a x+b}{\left(x-\alpha_{k}\right) F_{\ell}(x)} d x\right)\left(x_{k} \circ \Phi\right)=x_{k}$$
see (3.17). As $\varphi_{\ell}(\xi) \in(\lambda, \infty)$ and $F_{\ell}(x)$ is a polynomial of degree $m \geq 2$, it follows that the functions $\int_{\lambda}^{\varphi_{\ell}(\xi)} \frac{a x+b}{\left(x-\alpha_{k}\right) F_{\ell}(x)} d x$ are uniformly bounded on $\left(M_{\mathbf{a}}\right)_{\lambda}=\left(\mathbb{C}_{\mathbf{a}}^{m}\right)_{\lambda}$, i.e.
$$x_{k} \circ \Phi=O\left(x_{k}\right) .$$

Using (3.3) and that $\xi_{i}$ and $\varphi_{i}(\xi)$ take values in $\left[\alpha_{i}, \alpha_{i+1}\right]$ for $i=1, \ldots, \ell-1$ (and are thus uniformly bounded) we conclude
$$\varphi_{\ell}(\xi)=M \xi_{\ell}+O(1)=\frac{M}{2}\|z\|^{2}+O(1),$$
for some positive real constant $M$. A closer look at (3.50) (using (3.3) and (3.51)) yields in fact
$$\begin{aligned}
\sum_{j=1}^{\ell}\left(\varphi_{j}(\xi)-\xi_{j}\right) & =\xi_{\ell} \int_{\lambda}^{\varphi_{\ell}(\xi)}\left(\frac{a x+b}{x F_{\ell}(x)}\right) d x+O\left(\xi_{\ell}^{1-m}\right) \\
& =-\frac{a}{2(m-1)} \xi_{\ell}^{2-m}+O\left(\xi_{\ell}^{1-m}\right)
\end{aligned}$$
Thus, using (3.44), together with (3.3)
$$\begin{aligned}
H(\Phi(\xi))-H^{f}(\xi) & =\left(H(\Phi(\xi))-H^{f}(\Phi(\xi))\right)+\left(H^{f}(\Phi(\xi))-H^{f}(\xi)\right) \\
& =-\frac{1}{2} \int_{\lambda}^{\varphi_{\ell}(\xi)}\left(\frac{a x+b}{F_{\ell}(x)}\right) d x+\frac{1}{2} \sum_{j=1}^{\ell}\left(\varphi_{j}(\xi)-\xi_{j}\right) \\
& =-\frac{a}{2} \int_{\lambda}^{\xi_{\ell}} \frac{x}{F_{\ell}(x)} d x-\frac{a}{4(m-1)} \xi_{\ell}^{2-m}+O\left(\xi_{\ell}^{1-m}\right)
\end{aligned}$$
showing that (via (3.47))
$$\begin{aligned}
H(\Phi(\xi)) & =\frac{1}{4}\|z\|^{2}+\frac{a}{4(m-2)(m-1)} \xi_{m}^{2-m}+O\left(\xi_{m}^{1-m}\right) \\
& =\frac{1}{4}\|z\|^{2}+\frac{2^{m-4} a}{(m-2)(m-1)}\|z\|^{4-2 m}+O\left(\|z\|^{3-2 m}\right)
\end{aligned}$$
when $m \geq 3$, and
$$\begin{aligned}
H(\Phi(\xi)) & =\frac{1}{4}\|z\|^{2}-\frac{a}{4} \log \xi_{2}-\frac{a}{4}+O\left(\xi_{2}^{-1}\right) \\
& =\frac{1}{4}\|z\|^{2}-\frac{a}{4} \log \|z\|^{2}+O\left(\|z\|^{-2}\right)
\end{aligned}$$
when $m=2$. \(\square\)
3.4. Proof of Theorem A. Theorem A follows from of Corollary 15 and Proposition 17. \(\square\)

\section*{4. Scalar-flat Kähler ALE surfaces}

This is the case $m=2$. There are two possibilities, depending on the number of distinct positive integers $a_{i}$ of the weigh vector $\mathbf{a}=\left(a_{0}, a_{1}, a_{2}\right)$.

Case 1. $a_{2}>a_{1}$. The metric is of the form (3.7) with all $n_{j}=0$ and $\ell=2$. This is the orthotoric construction of [5]:
$$\begin{aligned}
g_{\mathbf{a}}= & \left(\xi_{2}-\xi_{1}\right)\left(-\frac{d \xi_{1}^{2}}{\Theta_{1}\left(\xi_{1}\right)}+\frac{d \xi_{2}^{2}}{\Theta_{2}\left(\xi_{2}\right)}\right) \\
& +\frac{1}{\left(\xi_{2}-\xi_{1}\right)}\left(-\Theta_{1}\left(\xi_{1}\right)\left(d t_{1}+\xi_{2} d t_{2}\right)^{2}+\Theta_{2}\left(\xi_{2}\right)\left(d t_{1}+\xi_{1} d t_{2}\right)^{2}\right) \\
\omega_{\mathbf{a}}= & d \sigma_{1} \wedge d t_{1}+d \sigma_{2} \wedge d t_{2} \\
= & d \xi_{1} \wedge\left(d t_{1}+\xi_{2} d t_{2}\right)+d \xi_{2} \wedge\left(d t_{1}+\xi_{1} d t_{2}\right)
\end{aligned}$$
where:
\begin{itemize}
\item[-] $\xi_{1} \in\left(-a_{0} a_{2},-a_{0} a_{1}\right), \xi_{2} \in(0, \infty), \Theta_{1}(x)=2\left(x+a_{0} a_{1}\right)\left(x+a_{0} a_{2}\right), \Theta_{2}(x)=$ $2 x\left(x+a_{0}^{2}\right), b_{0}>0$;
\item[-] $\sigma_{1}=\xi_{1}+\xi_{2} ; \sigma_{2}=\xi_{1}+\xi_{2}$;
\end{itemize}

We have shown in the previous section that using suitable momentum coordinates $\left(x_{1}, x_{2}\right)$ instead of $\left(\xi_{1}, \xi_{2}\right)$, the metric is defined on $\stackrel{\circ}{M}=\stackrel{\circ}{\mathrm{P}} \times T^{2}$ where
$$\stackrel{\circ}{\mathrm{P}}=\left\{\left(x_{1}, x_{2}\right): x_{1}>0, x_{2}>0, x_{1}+x_{2}-1>0\right\} .$$
and satisfies the first-order boundary conditions (3.16) with respect to the inward normals
$$v_{1}=a_{0} a_{2}(1,0), \quad v_{2}=a_{0} a_{1}(0,1), \quad v_{0}=a_{1} a_{2}(1,1) .$$
By Corollary 15, it extends to define a scalar-flat Kähler ALE metric on $\mathbb{C} P_{-a_{0}, a_{1}, a_{2}}^{2}$ when $a_{i}$ are taken to be integers with $\operatorname{gcd}\left(a_{0}, a_{1}, a_{2}\right)=1$.
Case 2. $a_{2}=a_{1}$. This is the case $\ell=1$ and $n_{1}=1$ in (3.7), when the metric $g_{\mathbf{a}}$ becomes a particular case of (2.1) with $n=1$ (often referred to as the Calabi ansatz), see Remark 7. The toric aspects of (2.1) allow one to construct scalar-flat Kähler ALE metric on $\stackrel{\circ}{M}=\stackrel{\circ}{\mathrm{P}} \times T^{2}$ for which the corresponding matrix-valued function $\mathbf{H}$ verifies the boundary conditions (3.16) with respect to normals
$$v_{1}=a_{0} a_{1}(1,0), \quad v_{2}=a_{0} a_{1}(0,1), \quad v_{0}=a_{1}^{2}(1,1), a_{0}, a_{1}>0,$$
i.e. (4.3) in the case when $a_{1}=a_{2}$. Indeed, let $y \in[0, \ell]$ be a momentum coordinate for an $S^{1}$-isometric action on $\check{g}_{\mathbb{C} P^{1}}$ (which reflects the normalization used for $\check{g}_{\mathbb{C} P^{1}}$ ), and let
$$\sigma_{1}=z, \sigma_{2}=z y$$
be the momenta for the two commuting Killing fields of (2.1). The metric is then defined on $\stackrel{\circ}{\Sigma} \times T^{2}$ where
$$\stackrel{\circ}{\Sigma}=\left\{\left(\sigma_{1}, \sigma_{2}\right): \sigma_{1}-a>0, \sigma_{2}>0, \ell \sigma_{1}-\sigma_{2}>0\right\},$$
and verifies (3.16) with respective normals
$$u_{1}=(1,0), \quad u_{2}=(0,1), \quad u_{0}=(\ell,-1) .$$
The affine transformation
$$x_{1}=\frac{1}{a \ell}\left(\ell \sigma_{1}-\sigma_{2}\right), \quad x_{2}=\frac{1}{a \ell} \sigma_{2},$$
sends $\stackrel{\circ}{\Sigma}$ to $\stackrel{\circ}{\mathrm{P}}$, with inward normals
$$v_{1}=\ell a(1,0), \quad v_{2}=\ell a(0,1), \quad v_{0}=a(1,1) .$$

Thus, putting
$$a=a_{1}^{2}, \quad \ell=\frac{a_{0}}{a_{1}}$$
we obtain a scalar-flat Kähler solution on $\stackrel{\circ}{\mathrm{P}} \times T^{2}$, satisfying (3.16) with respect to the normals (4.4). The metric is Ricci-flat iff $a_{0}=2 a_{1}$.

We now turn to a 4-dimensional phenomenon brought to our attention by J. Viaclovsky [30]. Being of Calabi-type or orthotoric, the metric $\left(g_{\mathbf{a}}, \omega_{\mathbf{a}}, J_{\mathbf{a}}\right)$ is also ambitoric in the sense of [8]. Indeed, assuming that we are in the generic orthotoric case for instance, it has been shown in [4] that
$$\begin{aligned}
\tilde{g}_{\mathbf{a}} & =\frac{1}{\left(\xi_{1}-\xi_{2}\right)^{2}} g_{\mathbf{a}} \\
\tilde{\omega}_{\mathbf{a}} & =\frac{d \xi_{1} \wedge\left(d t_{1}+\xi_{2} d t_{2}\right)}{\left(\xi_{1}-\xi_{2}\right)^{2}}-\frac{d \xi_{2} \wedge\left(d t_{1}+\xi_{1} d t_{2}\right)}{\left(\xi_{1}-\xi_{2}\right)^{2}}
\end{aligned}$$
defines another Kähler structure on $\stackrel{\circ}{M}=\stackrel{\circ}{\Xi} \times T^{2}$ for which $\tilde{g}_{\mathbf{a}}$ is in the conformal class of $g_{\mathbf{a}}$ but the corresponding complex structure $\tilde{J}_{\mathbf{a}}$ (or, equivalently, the symplectic form $\tilde{\omega}_{\mathbf{a}}$ ) induces the opposite orientation of $\left(M, J_{\mathbf{a}}\right)$. As $\left(g_{\mathbf{a}}, \omega_{\mathbf{a}}, J_{\mathbf{a}}\right)$ is scalar-flat, it is anti-self-dual with respect to its canonical orientation. Thus, $\left(\tilde{g}_{\mathbf{a}}, \tilde{\omega}_{\mathbf{a}}, \tilde{J}_{\mathbf{a}}\right)$ becomes self-dual with respect to its canonical orientation, or equivalently Bochner-flat, see [13] for a complete local classification. Furthermore, the momenta for the Killing vector fields $K_{i}=\frac{\partial}{\partial t_{i}}$ with respect to $\tilde{\omega}_{\mathbf{a}}$ are
$$\tilde{\sigma}_{1}=-\frac{1}{\left(\xi_{1}-\xi_{2}\right)}, \quad \tilde{\sigma}_{2}=-\frac{\xi_{1}+\xi_{2}}{2\left(\xi_{1}-\xi_{2}\right)},$$
whereas the corresponding matrix-valued function $\tilde{\mathbf{H}}=\left(\tilde{g}_{\mathbf{a}}\left(K_{i}, K_{j}\right)\right)$ becomes
$$\tilde{\mathbf{H}}=\frac{1}{\left(\xi_{1}-\xi_{2}\right)^{3}}\left(\begin{array}{cc}
\Theta_{1}\left(\xi_{1}\right)-\Theta_{2}\left(\xi_{2}\right) & \xi_{2} \Theta_{1}\left(\xi_{1}\right)-\xi_{1} \Theta_{2}\left(\xi_{2}\right) \\
\xi_{2} \Theta_{1}\left(\xi_{1}\right)-\xi_{1} \Theta_{2}\left(\xi_{2}\right) & \xi_{2}^{2} \Theta_{1}\left(\xi_{1}\right)-\xi_{1}^{2} \Theta_{2}\left(\xi_{2}\right)
\end{array}\right) .$$
It is straightforward to check that
Lemma 18. $\tilde{\mathbf{H}}$ is polynomial with respect to $\left(\tilde{\sigma}_{1}, \tilde{\sigma}_{2}\right)$.
Furthermore, as the general theory in [9] predicts and as it can be checked explicitly, the change of coordinates (4.6) sends the domain $\stackrel{\circ}{\Xi}=\left(\alpha_{1}, \alpha_{2}\right) \times(0,+\infty)$ into the (bounded) simplex
$$\begin{aligned}
\stackrel{\circ}{\tilde{\Sigma}}=\left\{\left(\tilde{\sigma}_{1}, \tilde{\sigma}_{2}\right): L_{1}\right. & =\alpha_{1} \tilde{\sigma}_{1}+\tilde{\sigma}_{2}-\frac{1}{2}>0, L_{2}=-\alpha_{2} \tilde{\sigma}_{1}-\tilde{\sigma}_{2}+\frac{1}{2}>0, \\
L_{0} & \left.=\tilde{\sigma}_{2}+\frac{1}{2}>0\right\},
\end{aligned}$$
where, we recall, $\alpha_{1}=-a_{0} a_{2}, \alpha_{2}=-a_{0} a_{1}$ are the roots of $\Theta_{1}$, and $\tilde{\mathbf{H}}$ extends smoothly over $\partial \stackrel{\sim}{\tilde{\Sigma}}$, satisfying the boundary conditions (3.16) at any face of $\stackrel{\sim}{\tilde{\Sigma}}$, except possibly at the vertex $\left(0, \frac{1}{2}\right)$, with respect to the inward normals
$$\tilde{u}_{j}=\frac{-2}{\Theta_{1}^{\prime}\left(\alpha_{j}\right)}\left(\alpha_{j}, 1\right), \quad j=1,2, \quad \tilde{u}_{0}=\frac{-2}{\Theta_{2}^{\prime}(0)}(0,1)=\frac{1}{a_{0}^{2}}(0,1),$$
By Lemma 18 and continuity, the boundary conditions at the vertex $\left(0, \frac{1}{2}\right)$ must also hold. Noting that the affine transformation
$$\tilde{x}_{1}=\frac{\alpha_{2}}{\alpha_{1}-\alpha_{2}}\left(\alpha_{1} \tilde{\sigma}_{1}+\tilde{\sigma}_{2}-\frac{1}{2}\right), \quad \tilde{x}_{2}=\frac{\alpha_{1}}{\alpha_{2}-\alpha_{1}}\left(\alpha_{2} \tilde{\sigma}_{1}+\tilde{\sigma}_{2}-\frac{1}{2}\right)$$
sends $\stackrel{\circ}{\tilde{\Sigma}}$ to the standard simplex
$$\stackrel{\mathrm{S}}{\mathrm{~S}}=\left\{\left(\tilde{x}_{1}, \tilde{x}_{2}\right): \tilde{x}_{1}>0, \tilde{x}_{2}>0,1-\tilde{x}_{1}-\tilde{x}_{2}>0\right\}$$
and the normals (4.9) to
$$v_{1}=\frac{1}{a_{0} a_{1}}(1,0), \quad v_{2}=\frac{1}{a_{0} a_{2}}(0,1), \quad v_{0}=\frac{1}{a_{0}^{2}}(-1,-1) .$$
We conclude that
$$v_{1}=\lambda_{\mathbf{a}} a_{0} a_{2}(1,0), \quad v_{2}=\lambda_{\mathbf{a}} a_{0} a_{1}(0,1), \quad v_{0}=\lambda_{\mathbf{a}} a_{1} a_{2}(-1,-1),$$
where
$$\lambda_{\mathbf{a}}=a_{0}^{2} a_{1} a_{2} .$$

Similar phenomenon happens in the Calabi-type case too, i.e. when $a_{1}=a_{2}$, see [15]. In the toric setting described in this section, the negatively oriented conformal Kähler structure is
$$\tilde{g}_{\mathbf{a}}=\frac{1}{z^{2}} g_{\mathbf{a}}, \quad \tilde{\omega}_{\mathbf{a}}=\frac{1}{z}\left(\check{\omega}_{\mathbb{C} P^{1}}-\frac{1}{z} d z \wedge \theta\right),$$
which is again of Calabi type, by replacing $z$ with $\tilde{z}=1 / z$. Thus,
$$\tilde{\sigma}_{1}=\frac{1}{z}, \quad \tilde{\sigma}_{2}=\frac{y}{z}$$
are momenta with respect to $\tilde{\omega}_{\mathbf{a}}$; the Kähler metric $\left(\tilde{g}_{\mathbf{a}}, \tilde{\omega}_{\mathbf{a}}\right)$ is thus defined over $\stackrel{\circ}{\tilde{\Sigma}} \times T^{2}$, where
$$\stackrel{\circ}{\tilde{\Sigma}}=\left\{\frac{1}{a}-\tilde{\sigma}_{1}>0, \quad \tilde{\sigma}_{2}>0, \quad \ell \tilde{\sigma}_{1}-\tilde{\sigma}_{2}>0\right\} .$$
It satisfies (3.16) on the faces of $\stackrel{\circ}{\tilde{\Sigma}}$ with respect to the normals
$$\tilde{u}_{1}=(-1,0), \quad \tilde{u}_{2}=(0,1), \quad \tilde{u}_{0}=(\ell,-1),$$
except possibly at the vertex $(0,0)$. As $\left(\tilde{g}_{\mathbf{a}}, \tilde{\omega}_{\mathbf{a}}\right)$ is Bochner-flat, the matrix valued function $\tilde{\mathbf{H}}=\left(\tilde{g}_{\mathbf{a}}\left(K_{i}, K_{j}\right)\right)$ is polynomial in momenta (this follows, for example, from the local classification [13], but in our situation can also be checked directly), so that the boundary conditions at $(0,0)$ are satisfied too. The affine transformation
$$\tilde{x}_{1}=\frac{a}{\ell}\left(\ell \tilde{\sigma}_{1}-\tilde{\sigma}_{2}\right), \quad \tilde{x}_{2}=\frac{a}{\ell} \tilde{\sigma}_{2},$$
sends $\stackrel{\circ}{\Sigma}$ to $\stackrel{\circ}{S}$, with inward normals
$$v_{1}=\frac{\ell}{a}(1,0), \quad v_{2}=\frac{\ell}{a}(0,1), \quad v_{0}=\frac{1}{a}(-1,-1) .$$
As $a=a_{1}^{2}, \ell=a_{0} / a_{1}$, we get again
$$v_{1}=\lambda_{\mathbf{a}} a_{0} a_{1}(1,0), \quad v_{2}=\lambda_{\mathbf{a}} a_{0} a_{1}(0,1), \quad v_{0}=\lambda_{\mathbf{a}} a_{1}^{2}(-1,-1),$$
where
$$\lambda_{\mathbf{a}}=1 / a_{1}^{4} .$$
We summarize

Proposition 19. For any $\mathbf{a}=\left(a_{0}, a_{1}, a_{2}\right)$, with $a_{i}>0$, the Kähler metric $\left(\tilde{g}_{\mathbf{a}}, \tilde{\omega}_{\mathbf{a}}, \tilde{J}_{\mathbf{a}}\right)$ is Bochner-flat, and, on $\stackrel{ه}{\mathrm{~S}} \times T^{2}$, satisfies (3.16) with respect to the inward normals
$$v_{1}=\lambda_{\mathbf{a}} a_{0} a_{2}(1,0), \quad v_{2}=\lambda_{\mathbf{a}} a_{0} a_{1}(0,1), \quad v_{0}=\lambda_{\mathbf{a}} a_{1} a_{2}(-1,-1),$$
where $\lambda_{\mathbf{a}}>0$ is the constant given by (4.10) when $a_{1} \neq a_{2}$, and by (4.12) when $a_{1}=a_{2}$.
4.1. Proof of Theorem B. By Proposition 19 and [6, Prop. 1], the metric $\tilde{g}_{\mathbf{a}}$ compactifies on $\mathbb{C} P_{a_{0}, a_{1}, a_{2}}^{2}$ (see e.g. [2, 6] for a toric description of a compact weighted-projective space) and defines a Bochner-flat Kähler metric. However, the Bochner-flat Kähler metric on $\mathbb{C} P_{a_{0}, a_{1}, a_{2}}^{2}$ is unique, up to isometries and homotheties: this follows for instance from the fact that any Bochner-flat Kähler metric is extremal, by using the uniqueness of the extremal Kähler metrics, established in the toric case in [19].

In the Calabi case $\left(a_{1}=a_{2}\right)$, the argument is essentially done in [15]: As $g_{\mathbf{a}}=$ $\tilde{z}^{-2} \tilde{g}_{\mathbf{a}}$, the conformal factor is given by
$$\tilde{z}=\tilde{\sigma}_{1}=\frac{1}{a}\left(\tilde{x}_{1}+\tilde{x}_{2}\right) .$$
The latter is a smooth and positive function on $M=\mathbb{C} P_{a_{0}, a_{1}, a_{1}}^{2} \backslash[1,0,0]$, and therefore the metric $\frac{1}{a}\left(\tilde{x}_{1}+\tilde{x}_{2}\right)^{-2} \tilde{g}_{\mathbf{a}}$ is well-defined on that subset; it is complete because it is conformally compact, and by construction, when restricted to the pre-image $\stackrel{\circ}{M}$ of $\stackrel{\text { S }}{\text { S }}$ it coincides with $g_{\mathbf{a}}$ restricted to the pre-image of $\stackrel{\circ}{\mathrm{P}}$. These two metrics are therefore isometric, being both complete and isometric over dense subsets.

Similarly, in the orthotoric case $\left(a_{2}>a_{1}\right), g_{\mathbf{a}}=\tilde{\sigma}_{1}^{-2} \tilde{g}_{\mathbf{a}}$, with
$$\tilde{\sigma}_{1}=\frac{1}{\alpha_{1} \alpha_{2}}\left(\alpha_{1} \tilde{x}_{1}+\alpha_{2} \tilde{x}_{2}\right)=-\left(\frac{\tilde{x}_{1}}{a_{0} a_{1}}+\frac{\tilde{x}_{2}}{a_{0} a_{2}}\right)$$
is clearly strictly negative on $M=\mathbb{C} P_{a_{0}, a_{1}, a_{2}}^{2} \backslash[1,0,0]$. It follows again that
$$\left(\frac{\tilde{x}_{1}}{a_{0} a_{1}}+\frac{\tilde{x}_{2}}{a_{0} a_{2}}\right)^{-2} \tilde{g}_{\mathbf{a}}$$
is well-defined and complete on $M$, and therefore isometric to the complete scalarflat Kähler ALE metric on $\mathbb{C} P_{-a_{0}, a_{1}, a_{2}}^{2}$. \(\square\)

\section*{5. Resolution of singularities of type $\mathfrak{I}$}
5.1. Gluing weighted projective spaces and resolutions. Let $\Gamma_{\mathrm{b}}$ be a finite cyclic subgroup of $\mathrm{U}(m)$ of type $\mathfrak{I}$. By Definition B there exists a weight vector a congruent to $\mathbf{b}$ such that the weighted projective space $\mathbb{C} P_{-a_{0}, a_{1}, \ldots, a_{m}}^{m}$ is either smooth or has only singularities of type $\mathfrak{I}$. Such space comes equipped with a canonical projection
$$q: \mathbb{C} P_{-a_{0}, a_{1}, \ldots, a_{m}}^{m} \rightarrow \mathbb{C}^{m} / \Gamma_{\mathbf{a}}$$
given in homogeneous coordinates by
$$q\left(\left[z_{0}: z_{1}: \ldots: z_{m}\right]\right)=\left(\zeta^{a_{1}} z_{1}, \ldots, \zeta^{a_{m}} z_{m}\right)$$
where $\zeta$ is such that $\zeta^{a_{0}}=z_{0}$. Clearly, the above map is well-defined as a map with values in $\mathbb{C}^{m} / \Gamma_{\mathbf{a}}=\mathbb{C}^{m} / \Gamma_{\mathbf{b}}$.

If $\mathbb{C} P_{-a_{0}, a_{1}, \ldots, a_{m}}$ is smooth, i.e. $a_{1}=\ldots=a_{m}=1$ we are done, as $q$ is the resolution we were looking for. However, $\mathbb{C} P_{-a_{0}, a_{1}, \ldots, a_{m}}^{m}$ will have in general isolated
singularities of type $\mathfrak{I}$. Specifically, consider the open set $V_{1} \subset \mathbb{C} P_{-a_{0}, a_{1}, \ldots, a_{m}}^{m}$ given by the condition $\left\{z_{1} \neq 0\right\}$. As in the case of a smooth projective space, there are corresponding affine coordinates obtained by fixing $z_{1}=1$. For this, we choose $\zeta$ such that $\zeta^{a_{1}}=1 / z_{1}$. Then $\left[z_{0}: z_{1}: \ldots: z_{m}\right]=\left[\zeta^{-a_{0}} z_{0}: \zeta^{a_{1}} z_{1}: \ldots: \zeta^{a_{m}} z_{m}\right]$. Since $\zeta$ is only defined up to an $a_{1}$-th root of unity, we obtain affine coordinates chart $V_{1} \rightarrow \mathbb{C}^{m} / \Gamma_{\mathbf{b}^{\prime}}$, where $\mathbf{b}^{\prime}=\left(a_{1},-a_{0}, a_{2}, \ldots, a_{m}\right)$. If $V_{1}$ is not smooth, there is a singularity of type $\mathfrak{I}$ at a point which, without loss of generality, we can take to be $x_{1}=[0: 1: 0: \ldots: 0] \in V_{1}$ corresponding to $0 \in \mathbb{C}^{m} / \Gamma_{\mathbf{b}^{\prime}}$. Since this is a singularity of type $\mathfrak{I}$, there exists a weight vector $\mathbf{a}^{\prime}$ congruent to $\mathbf{b}^{\prime}$ such that $\mathbb{C} P_{-a_{0}^{\prime}, a_{1}^{\prime}, \ldots, a_{m}^{\prime}}$ is a weighted projective space of non-compact type with singularities of type $\mathfrak{I}$ together with a canonical projection $p: \mathbb{C} P_{-a_{0}^{\prime}, a_{1}^{\prime}, \ldots, a_{m}^{\prime}} \rightarrow V_{1}$.

We construct a new complex manifold $\mathcal{Y}^{\prime}$ out of $\mathbb{C} P_{-a_{0}, a_{1}, \ldots, a_{m}}$ and $\mathbb{C} P_{-} a_{0}^{\prime}, a_{1}^{\prime}, \ldots, a_{m}^{\prime}$ using $p$ as a gluing map. More precisely
$$\mathcal{Y}^{\prime}:=\left(\mathbb{C} P_{-a_{0}, a_{1}, \ldots, a_{m}} \backslash\left\{x_{1}\right\} \sqcup \mathbb{C} P_{-a_{0}^{\prime}, a_{1}^{\prime}, \ldots, a_{m}^{\prime}}\right) / \sim$$
where $\sim$ is the equivalence relation defined by $x \sim y$ (and $y \sim x$ ) if $x \in V_{1} \backslash\left\{x_{1}\right\}$ and $y \in \mathbb{C} P_{-a_{0}^{\prime}, a_{1}^{\prime}, \ldots, a_{m}^{\prime}} \backslash p^{-1}\left(x_{1}\right)$ with the property that $p(y)=x$. By definition $\mathcal{Y}^{\prime}$ is also endowed with a canonical projection
$$q^{\prime}: \mathcal{Y}^{\prime} \rightarrow \mathbb{C}^{m} / \Gamma_{\mathrm{b}} .$$
There may be residual singularities of type $\mathfrak{I}$ in $\mathcal{Y}^{\prime}$. By the definition of such singularities, the above construction can be iterated a finite number of times, providing a finite sequence of complex manifold
$$\mathcal{Y}=\mathcal{Y}_{n} \rightarrow \mathcal{Y}_{n-1} \rightarrow \cdots \rightarrow \mathcal{Y}_{0}=\mathbb{C}^{m} / \Gamma_{\mathbf{b}},$$
where $\mathcal{Y}$ is smooth and each $\mathcal{Y}_{i+1}$ is obtained by gluing a weighted projective space of non-compact type onto $\mathcal{Y}_{i}$ as above. The composition map
$$\pi: \mathcal{Y} \rightarrow \mathbb{C}^{m} / \Gamma_{\mathrm{b}}$$
is called a resolution of type $\mathfrak{I}$.
Let $\mathcal{X}$ be a complex orbifold with singularities of type $\mathfrak{I}$ (i.e. which has singularities modelled on neighbourhood of singularities of type $\mathfrak{I}$, see Sect. 1.2). The resolutions of type $\mathfrak{I}$ are readily extended to this setting. More precisely, we say that $\widehat{\mathcal{X}}$ is a resolution of type $\mathfrak{I}$ of $\mathcal{X}$ if there exists a finite sequence of orbifolds with singularities of type $\mathfrak{I}$
$$\widehat{\mathcal{X}}=\mathcal{X}_{n} \rightarrow \mathcal{X}_{n-1} \rightarrow \cdots \rightarrow \mathcal{X}_{0}=\mathcal{X},$$
where $\widehat{\mathcal{X}}$ is smooth, and each $\mathcal{X}_{i+1}$ is obtained by gluing a weighted projective space of non-compact type onto $\mathcal{X}_{i}$.
5.2. Resolution of extremal Kähler metrics. Let $\mathcal{X}$ be a complex orbifold with singularities of type $\mathfrak{I}$. Assume that $\mathcal{X}$ is endowed with an extremal Kähler metric with Kähler form $\omega$, which is smooth in the orbifold sense. We consider a resolution $\widehat{\mathcal{X}} \rightarrow \mathcal{X}$ of type $\mathfrak{I}$ obtained by gluing a finite number of weighted projective spaces of non-compact type as in (5.2). We want to prove that $\widehat{\mathcal{X}}$ carries smooth extremal Kähler metrics in suitable Kähler classes as well.

Using the the result of Arezzo-Lena-Mazzieri [11], which is a refinement of the Arezzo-Pacard gluing theory [12] to the extremal case, we obtain the following result:

Theorem 20. Let $\mathcal{X}$ be a complex orbifold with isolated singularities of type $\mathfrak{I}$ and $p_{1}: \mathcal{X}_{1} \rightarrow \mathcal{X}$ be the first step for constructing a resolution of type $\mathfrak{I}$.

If $\mathcal{X}$ carries an extremal Kähler metric with Kähler class $\Omega \in H^{2}(\mathcal{X}, \mathbb{R})$, then any neighbourhood of $p_{1}^{*} \Omega \in H^{2}\left(\mathcal{X}_{1}, \mathbb{R}\right)$ contains a Kähler class $\Omega_{1}$ represented by an extremal Kähler metric on $\mathcal{X}_{1}$.

Proof. The complex orbifold $\mathcal{X}$ has only singularities of type $\mathfrak{I}$. In particular they are isolated. The complex orbifold $\mathcal{X}_{1}$ is obtained by gluing a weighted projective spaces of non-compact type. This space carries a scalar-flat Kähler ALE metric by Theorem A. Furthermore, the ALE metric has a good decay at infinity, in the sense that it satisfies Proposition 17. This technical fact is important as it is required for using the Arezzo-Pacard gluing theorem.

Relying on the Arezzo-Pacard and Arezzo-Lena-Mazzieri gluing theory [12, 11], a tiny copy of the ALE metric on the weighted projective space can be glued onto the extremal Kähler metric of $\mathcal{X}$ in order to obtain a nearby extremal Kähler metric on $\mathcal{X}_{1}$. Notice that the gluing procedure provides a smooth extremal Kähler metric on $\mathcal{X}_{1}$ in a Kähler class very close to $p_{1}^{*}[\omega] \in H^{2}\left(\mathcal{X}_{1}, \mathbb{R}\right)$. \(\square\)

Using the above theorem iteratively, we obtain an extremal Kähler orbifold metric on each step $\mathcal{X}_{i}$ of the resolution (5.2). Thus we obtain the following corollary:

Corollary 21. Let $\mathcal{X}$ be a complex orbifold with isolated singularities of type $\mathfrak{I}$ and $p: \widehat{\mathcal{X}} \rightarrow \mathcal{X}$ be a resolution of type $\mathfrak{I}$.

If $\mathcal{X}$ carries an extremal Kähler metric with Kähler class $\Omega \in H^{2}(\mathcal{X}, \mathbb{R})$, then any neighbourhood of $p^{*} \Omega \in H^{2}\left(\mathcal{X}_{1}, \mathbb{R}\right)$ contains a Kähler class $\widehat{\Omega}$ represented by an extremal Kähler metric on $\widehat{\mathcal{X}}$.

Theorem C is just a consequence of the above corollary.

\section*{References}
\begin{itemize}
\item[] [1] M. Abreu, Kähler geometry of toric manifolds in symplectic coordinates, in "Symplectic and contact topology: Interactions and Perspectives", Eliashberg, Khesin, Lalonde (eds.), Fields Institute Communications, 35 (2003), 1-24.
\item[] [2] M. Abreu, Kähler metrics on toric orbifolds, J. Differential Geom. 58 (2001), no. 1, 151-187.
\item[] [3] M. Abreu, and R. Sena-Dias, Scalar-flat Kähler metrics on non-compact symplectic toric 4manifolds. Ann. Global Anal. Geom. 41 (2012) 209-239.
\item[] [4] V. Apostolov, D. M. J. Calderbank, and P. Gauduchon, The geometry of weakly self-dual Kähler surfaces. Compositio Math. 135 (2003), 279-322.
\item[] [5] V. Apostolov, D. M. J. Calderbank and P. Gauduchon, Hamiltonian 2-forms in Kähler Geometry I General Theory, J. Differential Geom. 73 (2006), 359-412.
\item[] [6] V. Apostolov, D. M. J. Calderbank, P. Gauduchon and C. Tønnesen-Friedman, Hamiltonian 2-forms in Kähler geometry II Global classification, J. Differential Geom. 68 (2004), 277-345.
\item[] [7] V. Apostolov, D. M. J. Calderbank, P. Gauduchon and C. Tønnesen-Friedman, Extremal Kähler metrics on projective bundles over a curve. Adv. Math. 227 (2011), 2385-2424.
\item[] [8] V. Apostolov, D. M. J. Calderbank, P. Gauduchon, Ambitoric geometry I: Einstein metrics and extremal ambikaehler structures, J. reine angew. Math., DOI 10.1515.
\item[] [9] V. Apostolov, D. M. J. Calderbank, P. Gauduchon, Ambitoric geometry II: Extremal toric surfaces and Einstein 4-orbifolds, Ann. Scient. Éc. Norm. Sup. (4) 48 (2015), 1075-112.
\item[] [10] C. Arezzo, and R. Lenna, Blowing up and desingularizing constant scalar-flat Kähler ALE space. Private communication.
\item[] [11] C. Arezzo, R. Lena, and L. Mazzieri, On the resolution of extremal and constant scalar curvature Kähler orbifolds, arXiv:1507.04729
\item[] [12] C. Arezzo, and F. Pacard, Blowing up and desingularizing constant scalar curvature Kähler manifolds. Acta Math. 196 (2006),179-228.
\end{itemize}
[13] R. L. Bryant, Bochner-Kähler metrics. J. Amer. Math. Soc. 14 (2001), 623-715.
[14] D. Calderbank, and M. Singer, Einstein metrics and complex singularities. Invent. Math. 156 (2004), no. 2, 405-443
[15] M. Dabkowski and M. Lock, On Kähler conformal compactifications of $U(n)$-invariant ALE spaces, Ann. Global Anal. Geom. 49 (2016), 73-85.
[16] T. Delzant, Hamiltoniens périodiques et image convexe de l'application moment, Bull. Soc. Math. France 116 (1988), 315-339.
[17] S. K. Donaldson, Extremal metrics on toric surfaces: a continuity method, J. Differential Geom. 79 (2008), 389-432.
[18] S K. Donaldson, Kähler metrics with cone singularities along a divisor, Essays in mathematics and its applications, 49-79, Springer, Heidelberg, 2012, available at arXiv:1102.1196.
[19] D. Guan, On modified Mabuchi functional and Mabuchi moduli space of Kähler metrics on toric bundles, Math. Res. Let. 6 (1999), 547-555.
[20] V. Guillemin, Kähler structures on toric varieties, J. Differential Geom. 40 (1994), 285-309.
[21] T. Eguchi, and A. J. Hanson, Self-dual solutions to Euclidean gravity, Annals of Physics 120 (1979), 82-105.
[22] A. D. Hwang and M. A. Singer, A momentum construction for circle-invariant Kähler metrics, Trans. Amer. Math. Soc. 354 (2002), 2285-2325.
[23] C. LeBrun, Counter-examples to the generalized positive action conjecture, Comm. Math. Phys. 118 (1988), 591-596.
[24] E. Legendre, Existence and non-uniqueness of constant scalar curvature toric Sasaki metrics, Composito Math. 147 (2011), 1613-1634.
[25] E. Lerman and S. Tolman, Hamiltonian torus actions on symplectic orbifolds and toric varieties, Trans. Amer. Math. Soc. 349 (1997), 4201-4230.
[26] R. Mazzeo, Kähler-Einstein metrics singular along a smooth divisor, Journées Équations aux Dérivées Partielles, Saint-Jean-de-Monts, 1999, Exp. No VI, 1-10.
[27] H. Pedersen and Y. S. Poon, Hamiltonian Constructions of Kähler-Einstein Metrics and Kähler Metrics of Constant Scalar Curvature, Commun. Math. Phys. 136 (1991), 309-326.
[28] Y. Rubinstein, Smooth and singular Kahler-Einstein metrics, in: Geometric and Spectral Analysis (P. Albin et al., Eds.), Contemp. Math. 630 (2014), AMS and Centre Recherches Mathematiques, pp. 45-138.
[29] Y. Rollin, M. Singer, Construction of Kähler surfaces with constant scalar curvature, J. Eur. Math. Soc. 11 (2009), 979-997.
[30] J. Viaclovsky, Private communication.
[31] S. R. Simanca, Kähler metrics of constant scalar curvature on bundles over $\mathbb{C P}^{n-1}$, Math. Ann. 291 (1991), 239-246.
[32] C. Tipler,Extremal Kähler metrics on blow-ups of parabolic ruled surfaces. Bull. Soc. Math. France 141 (2013), no. 3, 481-516
[33] S. M. Webster, On the pseudo-conformal geometry of Kähler manifolds, Math. Z. 157 (1977), 265-270.

Vestislav Apostolov, Département de Mathématiques, UQAM, C.P. 8888, Succursale Centre-ville, Montréal (Québec), H3C 3P8, Canada
E-mail address: apostolov.vestislav@uqam.ca
Yann Rollin, Laboratoire Jean Leray, Université de Nantes, Nantes, France
E-mail address: yann.rollin@univ-nantes.fr