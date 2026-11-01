---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 2102_10856.pdf
converter: mathpix
format: mmd
---

\title{
Self-dual cosmological Bianchi IX and VIII metrics
}

\author{
A. Miković * and N. Manojlović ${ }^{\dagger}$ \\ ${ }^{* \dagger}$ Grupo de Física Matemática da Universidade de Lisboa \\ Departamento de Matemática, Faculdade de Ciências \\ Campo Grande, Edifício C6, PT-1749-016 Lisboa, Portugal \\ *Departamento de Matemática e COPELABS \\ Universidade Lusófona \\ Av. do Campo Grande, 376, 1749-024 Lisboa, Portugal \\ ${ }^{\dagger}$ Departamento de Matemática, Faculdade de Ciências e Tecnologia \\ Universidade do Algarve, Campus de Gambelas \\ PT-8005-139 Faro, Portugal
}

\begin{abstract}
We show that self-dual Bianchi IX and VIII cosmological models are described by the Nahm dynamical system for an appropriate type of matrices. We construct the general solutions in the case of the diagonal reductions of the corresponding Nahm equations and give the explicit expressions for the corresponding self-dual metrics in the Euclidean and in the Minkowski signature cases.
\end{abstract}

\footnotetext{
*E-mail address: amikovic@ulusofona.pt
${ }^{\dagger}$ E-mail address: nmanoj@ualg.pt
}

\section*{1 Introduction}

Imposing self-duality on the solutions of the Einstein equations is a way to generate new solutions, since one often ends up with an integrable system of differential equations [1, 2]. However, one can use this method only for the eucledean General Relativity (GR) or for the complex GR. Still, the eucledean or complex GR solutions are usefull, since they play a role in quantum gravity [3,4].

Self-dual Bianchi metrics have been mainly studied in the context of self-duality of the Weyl tensor and spherical symmetry, see [5-12]. Self-dual spherically symmetric Bianchi metrics were studied in the context of self-duality of the Riemann tensor in [13]. In this paper we will analyze the case of self-dual cosmological Bianchi metrics and a good framework for such a study is the Ashtekar formalism for self-dual metrics [16], as well as the Ashtekar formalism for the Bianchi cosmological spacetimes [17].

Bianchi metric reductions of the Einstein equations give dynamical systems from classical mechanics [18, 19], and imposing the Riemann tensor self-duality is expected to give integrable dynamical systems. This is reasonable to espect, because the spherically symmetric reduction of a self-dual metric leads to the Lagrange or the Halphen system of ordinary differential equations (ODE), see [13-15]. We will show that in the case of Bianchi IX and Bianchi VIII cosmological spacetimes one obtains the Nahm systems of ODE for the matrices form the Lie algebras $s o(3)$ and $s o(2,1)$, respectively. Also, in the case of the complex GR, the self-dual Bianchi IX and VIII reductions give the Nahm system for matrices from complex $\operatorname{so}(3)$ and $\operatorname{so}(2,1)$ Lie algebras. In the case of other Bianchi cosmological spacetimes, the self-dualty restriction gives linear systems of ODE, so that selfdual Bianchi IX and VIII cosmological models are the interesting cases as far as the integrability is concerned.

In section 2 we review the self-dual metrics in the Ashtekar formulation of GR. In section 3 we review the cosmological Bianchi models in the Ashtekar formulation and show that in the Bianchi IX case the dynamical equations are given by the 3-dimensional real (or 2-dimensional complex in the Minkowski case) Nahm system of differential equations. In section 4 we analyze the integrability of the real and the complex Nahm system, and solve the diagonally reduced system, which is the Lagrange dynamical system. In section 5 we study the case of self-dual Bianchi VIII model, and solve the corresponding diagonally reduced Nahm system. In section 6 we construct the Bianchi IX and VIII self-dual metrics in the diagonally reduced cases. In section 7 we present our conclussions.

\section*{2 Self-dual metrics in the Ashtekar formulation}

Let $M=\Sigma \times \mathbf{R}$ be a 4-manifold where $\Sigma$ is a 3-manifold. Let $g$ be a metric on $M$ and let $h$ be an induced metric on $\Sigma$. These two metrics are related by
$$d s^{2}=g_{\mu \nu} d x^{\mu} d x^{\nu}=\left(\xi N^{2}+h_{i j} n^{i} n^{j}\right) d t^{2}+2 d t d x^{i} h_{i j} n^{j}+h_{i j} d x^{i} d x^{j},$$
where $N$ is the laps, $n^{i}$ are the components of the shift vector and $\xi=1$ in the Euclidean case while $\xi=-1$ in the Minkowski case.

By using the metric (2.1) one can obtain the canonical formulation of the Einstein-Hilbert action, i.e. the Arnowitt-Deser-Misner formulation [20], so that
$$\sqrt{|\operatorname{det} g|} R(g) \cong \pi^{i j} \dot{h}_{i j}-n^{i} \mathcal{C}_{i}(\pi, h)-N \mathcal{C}_{0}(\pi, h),$$
where $R(g)$ is the scalar curvature, $\cong$ is up to a surface term (when $\Sigma$ is non-compact), $\pi^{i j}$ are the canonically conjugate momenta for the 3-metric components $h_{i j}$ and $\dot{X}=d X / d t$. The constraints $\mathcal{C}_{i}$ and $\mathcal{C}_{0}$ are given by
$$\begin{aligned}
\mathcal{C}_{i} & =\nabla_{j} \pi_{i}^{j} \\
\mathcal{C}_{0} & =\frac{1}{\sqrt{\operatorname{det} h}}\left(\frac{1}{2} \pi^{2}-\pi^{i j} \pi_{i j}\right)+\sqrt{\operatorname{det} h} R(h),
\end{aligned}$$
where $\pi=h_{i j} \pi^{i j}$.
One can change the canonical variables $\left(\pi_{i j}, h^{i j}\right)$ to $\left(p_{\alpha}^{i}, e_{i}^{\alpha}\right)$ canonical variables, where $e_{i}^{\alpha}$ are the triads, so that $h_{i j}=e_{i}^{\alpha} e_{j \alpha}$. Furthermore, one can pass to $\left(\tilde{p}_{i}^{\alpha}, \tilde{e}_{\alpha}^{i}\right)$ canonical variables, where $\tilde{e}_{\alpha}^{i}$ are densitized inverse triads given by
$$\tilde{e}_{\alpha}^{i}=\sqrt{\operatorname{det} h} e_{\alpha}^{i} .$$
Consequently
$$\sqrt{|\operatorname{det} g|} R(g) \cong \tilde{p}_{i}^{\alpha} \frac{d \tilde{e}_{\alpha}^{i}}{d t}-N^{\alpha} \tilde{C}_{\alpha}(\tilde{p}, \tilde{e})-n^{i} \tilde{C}_{i}(\tilde{p}, \tilde{e})-N \tilde{C}_{0}(\tilde{p}, \tilde{e}),$$
where $\tilde{C}_{\mu}(\tilde{p}, \tilde{e})=C_{\mu}(p, e)=\mathcal{C}_{\mu}(\pi, h), \mu=0$ or $\mu=i$, and
$$\tilde{C}_{\alpha}=\epsilon_{\alpha \beta \gamma} \tilde{e}^{i \beta} \tilde{p}_{i}^{\gamma} .$$
Here $\epsilon_{\alpha \beta \gamma}$ is the totally antisymmetric 3-dimensional symbol.
The Ashtekar variables are given by the canonical transformation
$$\left(\tilde{p}_{i}^{\alpha}, \tilde{e}_{\alpha}^{i}\right) \rightarrow\left(A_{i}^{\alpha}, E_{\alpha}^{i}\right)$$
such that
$$A_{i}^{\alpha}=\Gamma_{i}^{\alpha}(\tilde{e})+z \tilde{p}_{i}^{\alpha}, \quad E_{\alpha}^{i}=\tilde{e}_{\alpha}^{i},$$
where $1-\xi z^{2}=0, \Gamma_{i}^{\alpha}(\tilde{e})=\omega_{i}^{\alpha}(e)$ and $\omega_{i}^{\alpha}(e)$ is a spin connection on $\Sigma$, whose dependence on the triads is given by the vanishing torsion equations
$$T^{\alpha}=d e^{\alpha}+\epsilon^{\alpha \beta \gamma} \omega_{\beta} \wedge e_{\gamma}=0 .$$
The one-forms $A^{\alpha}$ are real in the eucledean gravity case $(z= \pm 1)$, while they are complex in the Minkowski case $(z= \pm \mathrm{i})$, and they are known as the Ashtekar connections [21].

By using (2.8), one can show that (2.6) becomes
$$\sqrt{|\operatorname{det} g|} R(g) \cong-\xi z E_{\alpha}^{i} \dot{A}_{i}^{\alpha}-N^{\alpha} G_{\alpha}-n^{i} G_{i}-\tilde{N} G_{0},$$
where $\tilde{N}=N / \sqrt{\operatorname{det} h}$,
$$G_{\alpha}=D_{i} E_{\alpha}^{i}, \quad G_{i}=F_{i j}^{\alpha} E_{\alpha}^{j}, \quad G_{0}=\epsilon_{\alpha \beta \gamma} F_{i j}^{\alpha} E^{i \beta} E^{j \gamma},$$
$D_{i} X=\partial_{i} X+\left[A_{i}, X\right]$ and $F=d A+[A, A]$ is the curvature 2-form for a real $S O(3)$ or $S U(2)$ connection $A$ in the Euclidean case, while in the Minkowski case we have a complex $S O(3)$ or $S U(2)$ connection $A$.

In the Euclidean gravity case the self-dual (SD) metrics are defined as
$$R_{a b}^{*}=R_{a b},$$
where $R^{a b}$ is the curvature 2-form for the torsion-free spin connection $\omega^{a b}$ on $M$ and
$$R_{a b}^{*}=\epsilon_{a b}{ }^{c d} R_{c d},$$
where $\epsilon_{a b c d}$ is the 4-dimensional totally antisymmetric symbol. The self-duality of the curvature is equivalent to the self-duality of the connection
$$\omega_{a b}^{*}=\omega_{a b},$$
see [22].
In the Minkowski gravity case the definition of self-duality as $X^{*}=X$ has to be modified, because $\left(X^{*}\right)^{*}=-X$. One can then define self-duality conditions as $X^{*}= \pm \mathrm{i} X$, so that
$$R_{a b}^{*}= \pm \mathrm{i} R_{a b} \Leftrightarrow \omega_{a b}^{*}= \pm \mathrm{i} \omega_{a b} .$$
The self-duality conditions (2.12) can be realized if we use complex metrics, which is also reflected by the fact that the Ashtekar connection is complex in the Minkowski signature case.

In the Euclidean case we can choose the gauge
$$N^{\alpha}=0, \quad n^{i}=0, \quad \tilde{N}=1,$$
so that the 4-metric is given by
$$d s^{2}=N^{2} d t^{2}+h_{i j} d x^{i} d x^{j} .$$
The Einstein equations are then given by
$$\begin{aligned}
& \dot{A}_{i}^{\alpha}=\epsilon_{\beta \gamma}^{\alpha} F_{i j}^{\beta} E^{j \gamma}, \\
& \dot{E}_{\alpha}^{i}=\epsilon_{\alpha \beta \gamma} E^{j \beta} D_{j} E^{i \gamma},
\end{aligned}$$
plus the Gauss and the 3-diffeomorphism constraints
$$D_{i} E_{\alpha}^{i}=0, \quad F_{i j}^{\alpha} E_{\alpha}^{j}=0 .$$

If we impose $A_{i}^{\alpha}=0$, then $F_{i j}^{\alpha}=0$, which corresponds to the vanishing of the (anti) self-dual piece of the Riemann tensor, see [23] for the Minkowski case. In the Euclidean case, $\left(\omega_{a b}^{*}\right)^{*}=\omega_{a b}$, so that
$$\omega_{a b}=\frac{1}{2}\left(\omega_{a b}+\omega_{a b}^{*}\right)+\frac{1}{2}\left(\omega_{a b}-\omega_{a b}^{*}\right)=\omega_{a b}^{+}+\omega_{a b}^{-},$$
where $\left(\omega_{a b}^{ \pm}\right)^{*}= \pm \omega_{a b}^{ \pm}$are the self-dual and the anti self-dual piece of the spin connection. Then $\omega_{a b}^{*}=\omega_{a b}$ corresponds to $R_{a b}^{*}=R_{a b}$, which corresponds to $R_{a b}^{-}=0$ or $\omega_{a b}^{-}=0$. Hence the vanishing of the anti self-dual piece of the spin connection is equivalent to vanishing of the Ashtekar connection, since
$$\omega_{\mu}^{-a b}=0 \Leftrightarrow \omega_{i}^{-\alpha \beta}=\frac{1}{2}\left(\omega_{i}^{\alpha \beta}-\left(\omega^{*}\right)_{i}^{\alpha \beta}\right)=0 \Leftrightarrow A_{i}^{\alpha}=\Gamma_{i}^{\alpha}+z \tilde{p}_{i}^{\alpha}=0 .$$

Hence the SD gravity equations are given by
$$\dot{E}_{\alpha}=\epsilon_{\alpha \beta \gamma}\left[E^{\beta}, E^{\gamma}\right], \quad \partial_{i} E_{\alpha}^{i}=0,$$
where $E_{\alpha}=E_{\alpha}^{i} \partial_{i}$, which was the main result of [16]. The SD metric is given by (2.14), where
$$N=\sqrt{\operatorname{det} h}, \quad h_{i j}=e_{i}^{\alpha} e_{j \alpha}, \quad e_{\alpha}^{i}=\frac{E_{\alpha}^{i}}{\sqrt{\operatorname{det} h}}, \quad \operatorname{det} h=\operatorname{det}\left(E_{\alpha}^{i}\right) .$$

Note that the anti self-dual (ASD) metric equations are given by
$$\dot{E}_{\alpha}=-\epsilon_{\alpha \beta \gamma}\left[E^{\beta}, E^{\gamma}\right],$$
while the other equations are the same as in the SD case.
In the Minkowski case the SD/ASD equations are given by
$$\dot{E_{\alpha}}= \pm \mathrm{i} \epsilon_{\alpha \beta \gamma}\left[E^{\beta}, E^{\gamma}\right],$$
while the other equations are the same as in the Eucledean case except the expression for the 4-metric, which is given by
$$d s^{2}=-N^{2} d t^{2}+h_{i j} d x^{i} d x^{j} .$$

\section*{3 Self-dual Bianchi cosmological models}

Bianchi cosmological spacetimes have topology $\Sigma \times \mathbf{R}$ and globally defined 1-forms $\chi^{I}$ on $\Sigma$ such that
$$d \chi^{I}+C_{J K}{ }^{I} \chi^{J} \wedge \chi^{K}=0,$$
where $C_{J K}{ }^{I}$ are the structure constants of a 3-dimensional Lie algebra [24]. Bianchi showed that
$$C_{J K}{ }^{I}=\epsilon_{J K L} S^{L I}+\delta_{[J}^{I} v_{K]},$$
where $S$ is a diagonal matrix whose values can be 0 or ±1 and $v_{K}=(v, 0,0)$ [24].
The inverse $\chi_{i}^{I}$ vector fields $L_{I}=L_{I}^{i} \partial_{i}$ satisfy the Lie algebra [24]
$$\left[L_{I}, L_{J}\right]=C_{I J}{ }^{K} L_{K} .$$

In the Ashtekar formulation for GR, one can write
$$A_{i}^{\alpha}(x, t)=\mathcal{A}_{I}^{\alpha}(t) \chi_{i}^{I}(x), \quad E_{\alpha}^{i}(x, t)=\mathcal{E}_{\alpha}^{I}(t) L_{I}^{i}(x),$$
see [17], so that the self-dual equations of motion (EOM) (2.18) become
$$\dot{\mathcal{E}}_{\alpha}^{I}=\epsilon_{\alpha}^{\beta \gamma} \mathcal{E}_{\beta}^{J} \mathcal{E}_{\gamma}^{K} C_{J K}^{I}, \quad \mathcal{E}_{\alpha}^{I} v_{I}=0,$$
and $\mathcal{A}=0$.
For the class A Bianchi models $v=0$, so that there is only one equation, while for the class $\mathrm{B}, v \neq 0$, so that a non-trivial solution $(\mathcal{E} \neq 0)$ requires $\operatorname{det} \mathcal{E}=0$.

The dynamical equation from (3.2) can be rewritten in the case of the Bianchi IX model $(S=\operatorname{diag}(1,1,1), v=0)$ as the Nahm equation
$$\dot{V}_{\alpha}=\frac{1}{2} \epsilon_{\alpha}{ }^{\beta \gamma}\left[V_{\beta}, V_{\gamma}\right],$$
where $V_{\alpha}=2 \mathcal{E}_{\alpha}=2 \mathcal{E}_{\alpha}^{I} T_{I}$ and $T_{I}$ are $n \times n$ real matricies which generate the Lie algebra (3.1).

For $C_{I J K}=\epsilon_{I J K}$ we can take $\left(T_{I}\right)_{J K}=-\epsilon_{I J K}$, so that $n=3$.
We can also take $T_{I}=-\frac{\mathrm{i}}{2} \sigma_{I}$, where $\sigma_{I}$ are Pauli matrices, so that $C_{I J K}=\epsilon_{I J K}$ and $n=2$. This choice requires complex Nahm matrices, but if we restrict the Lie algebra coefficients to real numbers, we can still get real metric components. If we consider complex metrics, we can take the same Lie algebra generators for the $n=2$ and $n=3$ case and allow the coefficients to take complex values. In this case
$$\dot{\mathcal{E}}_{\alpha}=\mathrm{i} \epsilon_{\alpha}{ }^{\beta \gamma}\left[\mathcal{E}_{\beta}, \mathcal{E}_{\gamma}\right],$$
and $V_{\alpha}=2 \mathrm{i} \mathcal{E}_{\alpha}$, then obeys the Nahm equation (3.3) for complex matricies $V_{\alpha}$.
As far as the integrability is concerned, the only non-trivial SD Bianchi models are Bianchi IX and VIII, since the other Bianchi models give linear systems of ODE.

\section*{4 Self-dual Bianchi IX model}

The Nahm equations (3.3) can be written as
$$\dot{V}_{1}=\left[V_{2}, V_{3}\right], \quad \dot{V}_{2}=\left[V_{3}, V_{1}\right], \quad \dot{V}_{3}=\left[V_{1}, V_{2}\right] .$$

The corresponding Lax pair is given by
$$L=A_{+}+\lambda A_{3}+\lambda^{2} A_{-}, \quad M=\frac{1}{2} A_{3}+\lambda A_{-},$$
where
$$A_{ \pm}=V_{1} \pm \mathrm{i} V_{2}, \quad A_{3}=2 \mathrm{i} V_{3},$$
so that the EOM (4.1) are equivalent to
$$\dot{L}=[M, L] .$$

The integrals of motion $I_{m n}(V)$ can be determined from
$$\operatorname{tr}\left(L^{n}\right)=\sum_{m} I_{m n}(V) \lambda^{m},$$
where $n=1,2,3, \ldots$. We need to find 8 independent integrals of motion from the equation (4.3) in order to construct the general solution. However, due to the identity
$$L^{3}=\frac{1}{2} \operatorname{tr}\left(L^{2}\right) L,$$
the only independent integrals of motion which are generated by $\operatorname{tr}\left(L^{n}\right)$ are the 5 integrals coming from $\operatorname{tr}\left(L^{2}\right)$, and these are
$$I_{1}=a^{2}-b^{2}, \quad I_{2}=a^{2}+b^{2}-2 c^{2}, \quad I_{3}=\vec{a} \cdot \vec{b}, \quad I_{4}=\vec{b} \cdot \vec{c}, \quad I_{5}=\vec{a} \cdot \vec{c},$$
where $\vec{a}=\left(u_{1}, v_{1}, w_{1}\right), \vec{b}=\left(u_{2}, v_{2}, w_{2}\right), \vec{c}=\left(u_{3}, v_{3}, w_{3}\right), a^{2}=(\vec{a})^{2}$ and $b^{2}=(\vec{b})^{2}$.
The components of these vectors are related to the elements of the 3-dimensional matrices $V_{\alpha}$ as
$$V_{\alpha}=\left(\begin{array}{ccc}
0 & -w_{\alpha} & v_{\alpha} \\
w_{\alpha} & 0 & -u_{\alpha} \\
-v_{\alpha} & u_{\alpha} & 0
\end{array}\right),$$
where $V_{\alpha}=u_{\alpha} T_{1}+v_{\alpha} T_{2}+w_{\alpha} T_{3}$. By choosing $u, v, w \in \mathbf{R}$ we get the Euclidean gravity case, while $u, v, w \in \mathbf{C}$ gives the Minkowski complex gravity case.

In the 2-dimensional case, we have
$$V_{\alpha}=\frac{1}{2}\left(\begin{array}{cc}
-\mathrm{i} w_{\alpha} & v_{\alpha}-\mathrm{i} u_{\alpha} \\
v_{\alpha}+\mathrm{i} u_{\alpha} & \mathrm{i} w_{\alpha}
\end{array}\right),$$
so that even when $u, v, w \in \mathbf{R}$ one obtains complex matrices. In order to avoid confusion, we will work with the 3-dimensional representation.

In terms of the vectors $\vec{a}, \vec{b}$ and $\vec{c}$ the Nahm system takes the form
$$\dot{\vec{a}}=\vec{b} \times \vec{c}, \quad \dot{\vec{b}}=\vec{c} \times \vec{a}, \quad \dot{\vec{c}}=\vec{a} \times \vec{b} .$$

Although we cannot find a general solution of the Nahm system, we can find a general solution for a reduced Nahm system given by
$$V_{1}=x T_{1}, \quad V_{2}=y T_{2}, \quad V_{3}=z T_{3} .$$
In this case we obtain the Lagrange system
$$\dot{x}=y z, \quad \dot{y}=x z, \quad \dot{z}=x y .$$

The Lagrange system has quadratic integrals of motion
$$I=\alpha x^{2}+\beta y^{2}+\gamma z^{2}, \quad \alpha+\beta+\gamma=0,$$
so that there are 2 independent quadratic integrals of motion. By taking $C_{1}=$ $x^{2}-z^{2}$ and $C_{2}=y^{2}-z^{2}$ we obtain $x_{i}= \pm \sqrt{C_{i}+z^{2}}$, so that
$$\dot{z}= \pm \sqrt{\left(C_{1}+z^{2}\right)\left(C_{2}+z^{2}\right)} .$$

Hence
$$t+C_{3}=\int \frac{d z}{\sqrt{\left(C_{1}+z^{2}\right)\left(C_{2}+z^{2}\right)}}$$
and a real solution is obtained in the following cases
$$\begin{gathered}
C_{1}>0, \quad C_{2}>0, \\
C_{1}>0, \quad C_{2}<0, \quad z^{2}>-C_{2}, \\
C_{1}<0, \quad C_{2}>0, \quad z^{2}>-C_{1}, \\
C_{1}<0, \quad C_{2}<0, \quad z^{2}>\max \left\{-C_{1},-C_{2}\right\} .
\end{gathered}$$

In all these cases the solutions can be written as Jacobi elliptic functions [25-27]. Let
$$\mathrm{pq}(u, k)=\frac{\operatorname{pn}(u, k)}{\operatorname{qn}(u, k)},$$
where
$$\operatorname{pn}(u, k) \neq \operatorname{qn}(u, k) \in\{\operatorname{sn}(u, k), \operatorname{cn}(u, k), \operatorname{dn}(u, k)\},$$
are the 3 basic Jacobi elliptic functions $\left(u \in \mathbf{R}, 0<k^{2}<1\right.$, see [27]).

Let $C_{1}=\alpha^{2}, C_{2}=\beta^{2}, \alpha<\beta$ and $u=\beta\left(t+C_{3}\right)$. Then (4.7) becomes
$$u=\int_{0}^{z / \alpha}\left(1+t^{2}\right)^{-1 / 2}\left[1+\left(k^{\prime}\right)^{2} t^{2}\right]^{-1 / 2} d t=\operatorname{arcsc}(z / \alpha, k)$$
where $k^{\prime}=\sqrt{1-k^{2}}=\alpha / \beta$. Consequently
$$z=\alpha \operatorname{sc}(u, k), \quad x=\beta \operatorname{dc}(u, k), \quad y=\alpha \operatorname{nc}(u, k) .$$

If $\alpha \geq \beta$ then $u=\alpha\left(t+t_{0}\right), k^{\prime}=\beta / \alpha$, and $x, y$ and $z$ are given by (4.12) with $(\alpha, \beta) \rightarrow(\beta, \alpha)$.

In the case $C_{1}=-\alpha^{2}, C_{2}=\beta^{2}$, we have $u=\gamma\left(t+t_{0}\right)$ and
$$u=\int_{z / \gamma}^{+\infty}\left(t^{2}-k^{\prime 2}\right)^{-1 / 2}\left(t^{2}+k^{2}\right)^{-1 / 2} d t=\operatorname{arcds}(z / \gamma, k)$$
where $\gamma=\sqrt{\alpha^{2}+\beta^{2}}$ and $k=\frac{\alpha}{\gamma}$. Then
$$z=-\gamma \operatorname{ds}(u, k), x=-\gamma \operatorname{cs}(u, k), y=-\gamma \operatorname{ns}(u, k) .$$

In the last case we have $C_{1}=-\alpha^{2}, C_{2}=-\beta^{2}$ and for $\beta<\alpha$ we obtain $u=\alpha\left(t+t_{0}\right)$ and
$$u=\int_{z / \alpha}^{+\infty}\left(t^{2}-1\right)^{-1 / 2}\left(t^{2}-k^{2}\right)^{-1 / 2} d t=\operatorname{arcdc}(z / \alpha, k)$$
where $k=\beta / \alpha$. Consequently
$$z=\alpha \operatorname{dc}(u, k), \quad x=\gamma \operatorname{sc}(u, k), \quad y=\gamma \operatorname{nc}(u, k),$$
where $\gamma=\sqrt{\alpha^{2}-\beta^{2}}$.
When $\alpha<\beta$, the solution is given by (4.14) with $(\alpha, \beta) \rightarrow(\beta, \alpha)$, so that $u=\beta\left(t+t_{0}\right)$ and $k=\alpha / \beta$.

In the complex case one can use the solution of (4.6) given in [28], which can be written as
$$x=\sqrt{I_{1}} \operatorname{sn}(u, k), \quad y=\sqrt{-I_{1}} \operatorname{cn}(u, k), \quad z=-\sqrt{-I_{2}} \operatorname{dn}(u, k),$$
where
$$k=\frac{\sqrt{I_{2}}-\sqrt{I_{2}-I_{1}}}{\sqrt{I_{1}}}, \quad u=\sqrt{I_{2}}\left(t+t_{0}\right),$$
and
$$I_{1}=x^{2}-y^{2}, \quad I_{2}=x^{2}-z^{2} .$$

Note that a complex solution can be also constructed by taking one of the real solutions (4.12), (4.13) or (4.14) and substituting $\alpha$ and $\beta$ by $\pm \sqrt{C_{1}}$ and $\pm \sqrt{C_{2}}$. For example, the real solution (4.12) gives a complex solution
$$x=\sqrt{C_{2}} \mathrm{dc}(u, k), \quad y=\sqrt{C_{1}} \mathrm{nc}(u, k), \quad z=\sqrt{C_{1}} \mathrm{sc}(u, k),$$
where
$$k=\sqrt{\frac{C_{2}-C_{1}}{C_{2}}}, \quad u=\sqrt{C_{2}}\left(t+t_{0}\right),$$
and there is no sign restriction on $C_{1}$ and $C_{2}$.

\section*{5 Self-dual Bianchi VIII model}

In the Bianchi VIII case $S=\operatorname{diag}(1,1,-1)$ and $v=0$, so that we have the system
$$\dot{\vec{a}}=\vec{b} \times \vec{c}, \quad \dot{\vec{b}}=\vec{c} \times \vec{a}, \quad \dot{\vec{c}}=-\vec{a} \times \vec{b} .$$

The Lax pair is given by (4.2), where now the matrices $V_{\alpha}$ belong to the $s o(2,1)$ Lie algebra, so that
$$V_{\alpha}=\left(\begin{array}{ccc}
0 & -w_{\alpha} & v_{\alpha} \\
w_{\alpha} & 0 & u_{\alpha} \\
v_{\alpha} & u_{\alpha} & 0
\end{array}\right) .$$
The quadratic integrals of motion are then given by
$$I_{1}=a^{2}-b^{2}, \quad I_{2}=a^{2}+b^{2}+2 c^{2}, \quad I_{3}=\vec{a} \cdot \vec{b}, \quad I_{4}=\vec{b} \cdot \vec{c}, \quad I_{5}=\vec{a} \cdot \vec{c} .$$

Note that $I_{1}$ and $I_{2}$ are two independent integrals of motion coming from a set of quadratic integrals of motion
$$I=\alpha a^{2}+\beta b^{2}+\gamma c^{2}, \quad \alpha+\beta-\gamma=0 .$$
Hence we can also chose the pair $I_{1}^{\prime}=a^{2}+c^{2}$ and $I_{2}^{\prime}=b^{2}+c^{2}$ instead of the ( $I_{1}, I_{2}$ ) pair.

As in the Bianchi IX case, the integrals (5.2) are not sufficient to solve the system (5.1), and we can make the reduction
$$\vec{a}=(x, 0,0), \quad \vec{b}=(0, y, 0), \quad \vec{c}=(0,0, z) .$$
In this case we get a modified Lagrange system
$$\dot{x}=y z, \quad \dot{y}=x z, \quad \dot{z}=-x y .$$

By using the integrals of motion $a^{2}+b^{2}$ and $b^{2}+c^{2}$, we obtain
$$C_{1}=x^{2}+z^{2}, \quad C_{2}=y^{2}+z^{2},$$
so that
$$\dot{z}=-\sqrt{\left(C_{1}-z^{2}\right)\left(C_{2}-z^{2}\right)} .$$

Hence
$$t+t_{0}=-\int \frac{d z}{\sqrt{\left(C_{1}-z^{2}\right)\left(C_{2}-z^{2}\right)}}$$
and real solutions are obtained for
$$C_{1}>0, \quad C_{2}>0, \quad z^{2}<\min \left\{C_{1}, C_{2}\right\} .$$

Let $C_{1}=\alpha^{2}, C_{2}=\beta^{2}, \alpha<\beta$ and $u=\beta\left(t+t_{0}\right)$ then (5.6) becomes
$$-u=\int_{0}^{z / \alpha}\left(1-t^{2}\right)^{-1 / 2}\left(1-k^{2} t^{2}\right)^{-1 / 2} d t=\operatorname{arcsn}(z / \alpha, k)$$
where $k=\alpha / \beta$. Hence
$$z=\alpha \operatorname{sn}(-u, k), \quad x=\alpha \operatorname{cn}(-u, k), \quad y=\beta \operatorname{dn}(-u, k) .$$

There is an alternative form of the reduced Bianchi VIII solution: if we take the integrals
$$x^{2}-y^{2}=C_{1}^{\prime}, \quad y^{2}+z^{2}=C_{2},$$
then we obtain
$$\dot{y}=\sqrt{\left(C_{1}^{\prime}+y^{2}\right)\left(C_{2}-y^{2}\right)} .$$

The real solutions are obtained for $C_{1}^{\prime}>0$ and $C_{2}>0$ or for $C_{1}^{\prime}<0$ and $C_{2}>0$. In the first case let $C_{1}^{\prime}=\alpha^{2}$ and $C_{2}=\beta^{2}$, then
$$u=\int_{y / \gamma}^{1}\left(1-t^{2}\right)^{-1 / 2}\left(k^{\prime 2}+k^{2} t^{2}\right)^{-1 / 2} d t=\operatorname{arccn}(y / \beta, k)$$
where $\gamma=\sqrt{\alpha^{2}+\beta^{2}}, u=\gamma\left(t+t_{0}\right), k=\beta / \gamma$. Consequently
$$y=\beta \operatorname{cn}(u, k), \quad x=\gamma \operatorname{dn}(u, k), \quad z=-\beta \operatorname{sn}(u, k) .$$

In the second case let $C_{1}^{\prime}=-\alpha^{2}, C_{2}=\beta^{2}$ and $\beta>\alpha$, then
$$u=\int_{1}^{y / \alpha}\left(t^{2}-1\right)^{-1 / 2}\left(1-k^{\prime 2} t^{2}\right)^{-1 / 2} d t=\operatorname{arcnd}(y / \alpha, k)$$
where $u=\beta\left(t+t_{0}\right), k^{\prime}=\alpha / \beta$. Consequently
$$y=\alpha \operatorname{nd}(u, k), \quad x=\alpha^{\prime} \operatorname{sd}(u, k), \quad z=\beta^{\prime} \operatorname{cd}(u, k),$$
where $\alpha^{\prime}=\alpha \sqrt{1-(\alpha / \beta)^{2}}$ and $\beta^{\prime}=\beta \sqrt{1-(\alpha / \beta)^{2}}$.
In the complex metric case one can take any of the real solutions (5.8), (5.9) or (5.10), and put $\alpha=\sqrt{C_{1}}$ or $\alpha= \pm \sqrt{C_{1}^{\prime}}, \beta=\sqrt{C_{2}}$ whith no restriction on the signs of the constants. For example, the real solution (5.8) gives a complex solution
$$x=\sqrt{C_{1}} \operatorname{cn}(-u, k), \quad y=\sqrt{C_{2}} \operatorname{dn}(-u, k), \quad z=\sqrt{C_{1}} \operatorname{sn}(-u, k),$$
where
$$k=\sqrt{\frac{C_{1}}{C_{2}}}, \quad u=\sqrt{C_{2}}\left(t+t_{0}\right),$$
and there is no sign restriction on $C_{1}$ and $C_{2}$.

\section*{6 Cosmological self-dual Bianchi metrics}

By using the definitions (2.14), (2.19) and (4.5) one obtains that the metric in the reduced (Lagrange) case is
$$d s^{2}=\Omega_{1} \Omega_{2} \Omega_{3}(\operatorname{det} L)\left(d t^{2}+\frac{\chi_{1}^{2}}{\Omega_{1}^{2}}+\frac{\chi_{2}^{2}}{\Omega_{2}^{2}}+\frac{\chi_{3}^{2}}{\Omega_{3}^{2}}\right),$$
where $\Omega_{i}=x_{i}(t) / 2$ and $\operatorname{det} L=\operatorname{det}\left(L_{\alpha}^{i}\right)$.
In the Bianchi IX case we have
$$\begin{aligned}
L_{1} & =\sin \psi \partial_{\theta}-\frac{\cos \psi}{\sin \theta} \partial_{\phi}+\cot \theta \cos \psi \partial_{\psi}, \\
L_{2} & =\cos \psi \partial_{\theta}+\frac{\sin \psi}{\sin \theta} \partial_{\phi}-\cot \theta \sin \psi \partial_{\psi}, \\
L_{3} & =\partial_{\psi},
\end{aligned}$$
where $\theta, \phi, \psi$ are the Euler angles ${ }^{1}$, while $x_{i}(t)$ are given by (4.12),(4.13) and (4.14).
Consequently
$$\operatorname{det}\left(L_{\alpha}^{i}\right)=\frac{1}{\sin \theta},$$

\footnotetext{
${ }^{1}$ We use the parametrization $R(\phi, \theta, \psi)=R_{3}(\psi) R_{1}(\theta) R_{3}(\phi)$ for an $S O(3)$ group element, where $R_{1}$ and $R_{3}$ are rotations around the $x$ and the $z$ axis.
}
and
$$\begin{aligned}
& \chi_{1}=\sin \psi d \theta-\cos \psi \sin \theta d \phi, \\
& \chi_{2}=\cos \psi d \theta+\sin \psi \sin \theta d \phi, \\
& \chi_{3}=\cos \theta d \phi+d \psi,
\end{aligned}$$
so that
$$d s^{2}=\frac{\Omega_{1} \Omega_{2} \Omega_{3}}{\sin \theta}\left(d t^{2}+\frac{\chi_{1}^{2}}{\Omega_{1}^{2}}+\frac{\chi_{2}^{2}}{\Omega_{2}^{2}}+\frac{\chi_{3}^{2}}{\Omega_{3}^{2}}\right) .$$

In the Bianchi VIII case we have
$$\begin{aligned}
& L_{1}=\sin \psi \partial_{\theta^{\prime}}-\frac{\cos \psi}{\sinh \theta^{\prime}} \partial_{\phi}+\operatorname{coth} \theta^{\prime} \cos \psi \partial_{\psi}, \\
& L_{2}=\cos \psi \partial_{\theta^{\prime}}+\frac{\sin \psi}{\sinh \theta^{\prime}} \partial_{\phi}-\operatorname{coth} \theta^{\prime} \sin \psi \partial_{\psi}, \\
& L_{3}=\partial_{\psi},
\end{aligned}$$
where the angles are defined by an $S O(2,1)$ group element parametrization $R(\phi, \theta, \psi)=$ $R_{3}(\psi) \tilde{R}_{1}\left(\theta^{\prime}\right) R_{3}(\phi)$ such that
$$\tilde{R}_{1}\left(\theta^{\prime}\right)=\left(\begin{array}{ccc}
1 & 0 & 0 \\
0 & \cosh \theta^{\prime} & \sinh \theta^{\prime} \\
0 & \sinh \theta^{\prime} & \cosh \theta^{\prime}
\end{array}\right),$$
and $\theta^{\prime} \in \mathbf{R}$.
Consequently
$$\operatorname{det}\left(L_{\alpha}^{i}\right)=\frac{1}{\sinh \theta^{\prime}},$$
and
$$\begin{aligned}
& \chi_{1}=\sin \psi d \theta^{\prime}-\cos \psi \sinh \theta^{\prime} d \phi, \\
& \chi_{2}=\cos \psi d \theta^{\prime}+\sin \psi \sinh \theta^{\prime} d \phi, \\
& \chi_{3}=\cosh \theta^{\prime} d \phi+d \psi,
\end{aligned}$$
while the metric is given by (6.4). The $\Omega_{i}(t)$ functions in the Bianchi VIII case are given by (5.8).

In the case of a Minkowski signature self-dual Bianchi IX complex metric, we have the same formulas for the $L$ 's and the $\chi$ 's as in the eucledean case, while $\Omega_{i}(t)$ are given by (4.15) or by (4.16) and
$$d s^{2}=\frac{\Omega_{1} \Omega_{2} \Omega_{3}}{\sinh \theta^{\prime}}\left(-d t^{2}+\frac{\chi_{1}^{2}}{\Omega_{1}^{2}}+\frac{\chi_{2}^{2}}{\Omega_{2}^{2}}+\frac{\chi_{3}^{2}}{\Omega_{3}^{2}}\right) .$$

In the case of a complex Bianchi VIII self-dual metric we have (6.7) with $\Omega_{i}(t)$ given by (5.11).

\section*{7 Conclusions}

The main results are the self-dual Bianchi IX and VII cosmological metrics given by the expression (6.4) in the Euclidean case, and by the expression (6.7) in the Minkowski case. The forms $\chi^{I}$ are given by (6.3) in the Bianchi IX case and by (6.6) in the Bianchi VIII case. The functions $2 \Omega_{i}(t)$ are given by (4.12),(4.13) and (4.14) in the Bianchi IX case, while in the Bianchi VIII case these functions are given by (5.8). In the Minkowski case, the functions $2 \Omega_{i}(t)$ are given by (4.16) for the Bianchi IX case, while in the Bianchi VII case these functions are given by (5.11).

Note that we solved the reduced Nahm's equations (4.6) and (5.3), so that a natural next step would be to solve the complete set (4.4) or (5.1). This would require the knowledge of 8 independent integrals of motion, and the Lax method gives only 5. This means that one could solve a 6-variables reduction of the Nahm's equations. However, it is not clear how to implement a 6-variables reduction such that it is preserved by the time evolution. As far as solving the complete set of Nahm's equations is concerned, one would need to find additional 3 integrals of motion, and there are indications that these conserved quantities cannot be local functions.

Note that in [13] it was considered a selfdual spherically-symmetric metric of the form
$$d s^{2}=\Omega_{1} \Omega_{2} \Omega_{3}\left(d r^{2}+\frac{\sigma_{1}^{2}}{\Omega_{1}^{2}}+\frac{\sigma_{2}^{2}}{\Omega_{2}^{2}}+\frac{\sigma_{3}^{2}}{\Omega_{3}^{2}}\right),$$
where $\Omega_{i}=f_{i}(r), r^{2}=x^{2}+y^{2}+z^{2}+t^{2}$,
$$\sigma_{i}=\frac{1}{r^{2}} \eta_{i \mu \nu} x^{\mu} d x^{\nu},$$
and $\eta_{i \mu \nu}$ are the t'Hooft coefficients.
The metric (7.1) has a similar structure as the SD Bianchi IX metric (6.1), but the variables are different. In [13] it was also showed that the self-duality of the connection associated to the metric (7.1) gives the Lagrange system
$$\Omega_{i}^{\prime}=\Omega_{j} \Omega_{k}, \quad i \neq j \neq k .$$
Hence our Lagrange system solutions (4.12),(4.13) and (4.14) can be used to construct self-dual metrics of the type (7.1), simply by replacing the variable $t$ in $x_{i}(t)$ with the variable $r$.

\section*{References}
[1] M. Dunajski, L.J. Mason and N.M.J. Woodhouse, J. Phys. A: Math. Gen. 31 (1998) 6019
\begin{itemize}
\item[] [2] Y. Nutku, M.B. Sheftel, J. Kalajci and D. Yazici, J. Phys. A: Math. Theor. 41 (2008) 395206
\item[] [3] G.W. Gibbons and C.N. Pope, Commun. Math. Phys. 66 (1979) 267
\item[] [4] J. Hartle and S. Hawking, Phys. Rev. D 28 (1983) 2960
\item[] [5] R. Maszczyk, L. J. Mason and N. M. J. Woodhouse, Class. Quant. Grav. 11 (1994) 65
\item[] [6] M. Cvetič, G. W. Gibbons, H. Lu and C. N. Pope, Class. Quant. Grav. 20 (2003) 4239
\item[] [7] H. Petersen and Y. S. Poon, Class. Quant. Grav. 7 (1990) 1707-1719.
\item[] [8] K. P. Tod, Class. Quant. Grav. 8 (1991) 1049-1051.
\item[] [9] K. P. Tod, Physics Letters A 190 (1994) 221-224.
\item[] [10] N. J. Hitchin, J. Differential Geometry Vol. 42 No. 1 (1995) 30-112.
\item[] [11] N. J. Hitchin, Integrable systems in Riemannian geometry, Surveys in Differential Geometry: Integral systems, Vol. IV (1998) 21-81.
\item[] [12] M.V. Babich and D.A. Korotkin, Lett. Math. Phys. 46 (1998) 323
\item[] [13] S. Chanda, P. Guha and R. Roychowdhury, Int. J. Geom. Methods Mod. Phys. 13 (2016) 1650042
\item[] [14] J. Harnad and J. MacKay, CRM Proc. Lecture Notes 25 (2000) 181-195.
\item[] [15] J. Harnad and J. MacKay, R. Soc. Lond. Proc. Ser. A Math. Phys. Eng. Sci. 456 (2000) 261-294.
\item[] [16] Ashtekar, Jacobson and Smolin, Commun. Math. Phys. 115 (1988) 651
\item[] [17] N. Manojlović and A. Miković, Class. Quant. Grav. 10 (1993) 559
\item[] [18] N. Manojlović and A. Miković, Adv. Theor. Math. Phys. Vol. 4 No. 1 (2000) 209-230.
\item[] [19] N. Manojlović and A. Miković, J. Math. Phys. Vol. 41 No. 7 (2000) 4777-4782.
\item[] [20] R. Arnowitt, S. Deser and C. Misner, Phys. Rev. 116 (1959) 1322
\item[] [21] A. Ashtekar, Phys. Rev. Lett. 57 (1986) 2244
\item[] [22] T. Eguchi, B. Gilkey and A.J. Hanson, Phys. Rep. 66 (1980) 213
\end{itemize}
\begin{itemize}
\item[] [23] M. Blagojević, Gravitation and Gauge Symmetries, IOP Publishing Ltd (2002) Bristol and Philadelphia
\item[] [24] L.D. Landau and E.M. Lifshitz, The Classical Theory of Fields, Course of Theoretical Physics, Volume 2, Fourth Edition, Butterworth-Heinemann 2000.
\item[] [25] E.T. Whittaker and G.N. Watson A Course of Modern Analysis, Cambridge Mathematical Library, Cambridge University Press, Reprented Fourth Edition 2000.
\item[] [26] N.I. Akhiezer, Elements of the Theory of Elliptic Functions, translations of Mathematical Monographs Vol. 79, AMS 1990.
\item[] [27] M. Abramowitz and I.A. Stegun, Handbook of Mathematical Functions, NBS (1964) Washington, D.C.
\item[] [28] L.A. Takhtajan, Teor. Mat. Fiz. 93 (1992) 330.
\end{itemize}