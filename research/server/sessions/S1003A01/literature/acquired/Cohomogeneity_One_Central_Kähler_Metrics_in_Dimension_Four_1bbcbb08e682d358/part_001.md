---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Cohomogeneity One Central Kähler Metrics in Dimension Four]

---
source_file: 2107_14683.pdf
converter: mathpix
format: mmd
---

\title{
COHOMOGENEITY ONE CENTRAL KÄHLER METRICS IN DIMENSION FOUR
}

\author{
THALIA JEFFRES AND GIDEON MASCHLER
}

\begin{abstract}
A Kähler metric is called central if the determinant of its Ricci endomorphism is constant [M]. For the case in which this constant is zero, we study on 4-manifolds the existence of complete metrics of this type which are cohomogeneity one for three unimodular 3-dimensional Lie groups: $S U(2)$, the group of Euclidean plane motions $E(2)$ and a quotient by a discrete subgroup of the Heisenberg group nil ${ }_{3}$. We obtain a complete classification for $S U(2)$, and some existence results for the other two groups, in terms of specific solutions of an associated ODE system.
\end{abstract}

\section*{1. Introduction}

In this paper the term central Kähler metric refers to a Kähler metric for which the determinant of the Ricci endomorphism is constant. This is a special case of the metric type called central in [M]. Riemannian and hermitian metrics with constant Ricci determinant were considered earlier, see for example [K, L, BM].

On a compact Kähler manifold there exists a Futaki-type invariant for central Kähler metrics [FT]. An associated functional analogous to the K-energy appears in [CT, SW, T, R]. If a compact manifold admits a Kähler-Einstein metric, it is shown in [M] that a central Kähler metric also exists in any Kähler class, and an appropriate notion of uniqueness holds for it as well. If a compact manifold with a definite first Chern class admits a central Kähler metric, it also admits a Kähler-Einstein metric. It is, as far as we know, an open question whether in the case where the first Chern class has no sign, a similar result holds with the conclusion that the manifold admits a Kähler metric with constant Ricci eigenvalues.

On noncompact manifolds the methods for obtaining the above results are unavailable, and existence of complete central Kähler metrics does not seem to have been explored. The main purpose of this paper is to demonstrate existence of such metrics which are also invariant under certain cohomogeneity one group actions on 4-manifolds. For technical reasons our results are limited to central metrics with zero Ricci determinant, which we call centrally flat, or metrics of zero central curvature. Note that in the rough classification in [M] of compact complex surfaces admitting central Kähler metrics, the most difficult and least understood case is the centrally flat one.

It should be noted that the groups we consider are not always compact. More specifically, up to a possible quotient by a discrete subgroup, the groups are three of the six unimodular 3-dimensional Lie groups. These are (a quotient of)
the Heisenberg group nil ${ }_{3}, S U(2)$ and the group of Euclidean plane motions $E(2)$. For the first and second of these, closely related incomplete central metrics appear in [AM2, Thm. 1 and sec. 3.5].

Our methods involve ODE techniques, and are directly inspired by the papers [DS1, DS2] of Dancer and Strachan, and the recent articles [AM2, MR1]. In all of these the Kähler-Einstein case is prominent. Another less closely related work is [MR2], which examines Kähler-Ricci solitons for actions of Heisenberg groups also in higher dimensions. For all the metrics we find, completeness holds on manifolds admitting a singular orbit, and the smooth extension of the metric and Kähler form to this orbit are shown using the recent systematic approach of Verdiani and Ziller [VZ].

We remark that the need to restrict ourselves to centrally flat metrics is due to the rather unexpected fact that the Center Manifold Theorem applies only in this case to our systems of ODEs. Throughout the paper we are, of course, only interested in centrally flat metrics which are not Ricci-flat.

It is interesting to compare our results to those for Kähler-Einstein metrics in the above references. We note first that our results are restricted to metrics which are diagonal in an appropriate coframe containing left invariant 1-forms for the group. Note that cohomogeneity one Kähler-Einstein metrics under $S U(2)$ must be diagonal, but we are not aware of a similar result for central metrics.

For the action of $S U(2)$, we classify the possible cases (Theorem 3), but our methods yield only complete diagonal centrally flat metrics which are biaxial, meaning that two out of three metric coefficients are equal. In contrast, [DS1] also find complete triaxial Kähler-Einstein metrics (in which the three coefficients are all distinct). Finally, the biaxial centrally flat metrics we find, just like the corresponding Kähler-Einstein ones in [DS1], can be given in explicit form.

For $E(2)$, we obtain inexplicit triaxial metrics in analogy with the same result in [MR1] in the Kähler-Einstein case (see Theorem 4). However, in that article all cases are classified, whereas for centrally flat metrics, we have to exclude one case from consideration, as we only find for it partial information concerning solutions satisfying a certain analyticity property.

The complete centrally flat metrics under the action of the quotient of nil ${ }_{3}$ are explicitly given examples. See Theorem 2.

In sections 2 and 3 and the appendix, we recall the ansatz of [MR1], based on the notion of shear operators, and adopt it to the case of central metrics. As in the Kähler-Einstein case, this ansatz may include more than just cohomogeneity one examples. Here we include it mainly to connect with that work, and recall its specialization to the cohomogeneity one case in section 4. Our main results are given in sections 5, 6 and 7.

\section*{2. Shear and integrability}

Let $(M, g, J)$ be an almost hermitian 4-manifold. We fix a local oriented orthonormal frame denoted
$$\left\{e_{i}\right\}=\{\mathbf{k}, \mathbf{t}=J \mathbf{k}, \mathbf{x}, \mathbf{y}=J \mathbf{x}\} .$$
In the frame domain, we have an orthogonal decomposition of the tangent bundle:
$$T M=\mathcal{V} \oplus \mathcal{H}, \quad \text { with } \mathcal{V}=\operatorname{span}(\mathbf{k}, \mathbf{t}), \quad \mathcal{H}=\operatorname{span}(\mathbf{x}, \mathbf{y}) .$$
Let $\mathcal{U}$ stand for either $\mathcal{V}$ or $\mathcal{H}$, and $\pi_{\mathcal{U}^{\perp}}: T M \rightarrow \mathcal{U}^{\perp}$ denote the orthogonal projection. For a vector field $X \in \Gamma(\mathcal{U})$, consider the operator $\left.\pi_{\mathcal{U}^{\perp}} \circ \nabla X\right|_{\mathcal{U}^{\perp}}$ : $\Gamma\left(\mathcal{U}^{\perp}\right) \rightarrow \Gamma\left(\mathcal{U}^{\perp}\right)$, where ∇ is the Levi-Civita covariant derivative of $g$. Define the shear operator of $X$ by
$$S_{X}:=\text { trace-free symmetric part of }\left.\pi_{\mathcal{U} \perp} \circ \nabla X\right|_{\mathcal{U}^{\perp}} \text {. }$$

Recall the condition for integrability of $J$ in terms of shear operators given in [AM1, MR1].

Theorem 1. Given the above set-up, the almost complex structure $J$ is integrable in the frame domain if and only if
$$\begin{aligned}
\text { i) } & J S_{\mathrm{x}}=S_{\mathrm{y}} \text { on } \mathcal{V} \text {. } \\
\text { ii) } & J S_{\mathrm{k}}=S_{\mathrm{t}} \text { on } \mathcal{H} \text {. }
\end{aligned}$$

In application we will also rely on the following expression of the matrix corresponding to the shear operator in a local oriented orthonormal frame $\left\{v_{1}, v_{2}\right\}$ on $\mathcal{U}^{\perp}$.
$$\left[S_{X}\right]_{v_{1}, v_{2}}=\left[\begin{array}{cc}
-\sigma_{1} & \sigma_{2} \\
\sigma_{2} & \sigma_{1}
\end{array}\right],$$
with shear coefficients:
$$\begin{aligned}
& 2 \sigma_{1}:=g\left(\left[X, v_{1}\right], v_{1}\right)-g\left(\left[X, v_{2}\right], v_{2}\right), \\
& 2 \sigma_{2}:=-g\left(\left[X, v_{1}\right], v_{2}\right)-g\left(\left[X, v_{2}\right], v_{1}\right) .
\end{aligned}$$

One simple case in which integrability holds by Theorem 1 is when all the shears vanish: $S_{e_{i}}=0, i=1, \ldots, 4$. We refer to this as the shear-free case.

\section*{3. Shear and Kähler metrics}

We recall here an ansatz for Kähler metrics on 4-manifolds given in [MR1]. $\operatorname{Let}(M, g, J)$ be an almost hermitian 4-manifold admitting an orthonormal frame $\left\{e_{i}\right\}=\{\mathbf{k}, \mathbf{t}, \mathbf{x}, \mathbf{y}\}$, with $J \mathbf{k}=\mathbf{t}, J \mathbf{x}=\mathbf{y}$, defined over an open $U \subset M$, which satisfies the Lie bracket relations
$$\begin{array}{ll}
{[\mathbf{k}, \mathbf{t}]=L(\mathbf{k}+\mathbf{t}),} & {[\mathbf{x}, \mathbf{y}]=N(\mathbf{k}+\mathbf{t}),} \\
{[\mathbf{k}, \mathbf{x}]=A \mathbf{x}+B \mathbf{y},} & {[\mathbf{k}, \mathbf{y}]=C \mathbf{x}+D \mathbf{y},} \\
{[\mathbf{t}, \mathbf{x}]=E \mathbf{x}+F \mathbf{y},} & {[\mathbf{t}, \mathbf{y}]=G \mathbf{x}+H \mathbf{y},}
\end{array}$$
for smooth functions $A, B, C, D, E, F, G, H, L, N$ on $U$ such that
$$\begin{aligned}
& A-D=F+G, \quad B+C=H-E, \\
& N=A+D=-(E+H) .
\end{aligned}$$
Then $(g, J)$ is Kähler (see [MR1, Prop. 3.1]). Its Levi-Civita connection over $U$ can be given by setting
$$\nabla_{\mathbf{k}} \mathbf{k}=-L \mathbf{t}, \quad \nabla_{\mathbf{x}} \mathbf{x}=A \mathbf{k}+E \mathbf{t}, \quad \nabla_{\mathbf{x}} \mathbf{k}=-A \mathbf{x}+E \mathbf{y},$$
and then having all other covariant derivative expressions on frame fields determined by the requirement that ∇ be torsion-free and make $J$ parallel.

The Ricci form of the Kähler metric $g$ was shown in [MR1] to take the form
$$\begin{aligned}
\rho=L(d \hat{\mathbf{k}}+d \hat{\mathbf{t}})+(C-H) d \hat{\mathbf{k}} & +(A-F) d \hat{\mathbf{t}} \\
& +d L \wedge(\hat{\mathbf{k}}+\hat{\mathbf{t}})+d(C-H) \wedge \hat{\mathbf{k}}+d(A-F) \wedge \hat{\mathbf{t}} .
\end{aligned}$$
where the hatted quantities denote the dual coframe of $\left\{e_{\ell}\right\}$.
Using formulas (59) in the appendix for the exterior derivatives of the coframe 1-forms, as well as $d f=d_{\mathbf{k}} f \hat{\mathbf{k}}+d_{\mathbf{t}} f \hat{\mathbf{t}}+d_{\mathbf{x}} f \hat{\mathbf{x}}+d_{\mathbf{y}} f \hat{\mathbf{y}}$, valid for a smooth function $f$ on $M$, we can rewrite this formula in the form
$$\rho=\alpha \hat{\mathbf{x}} \wedge \hat{\mathbf{y}}+\beta \hat{\mathbf{k}} \wedge \hat{\mathbf{t}}+\gamma \hat{\mathbf{k}} \wedge \hat{\mathbf{x}}+\delta \hat{\mathbf{k}} \wedge \hat{\mathbf{y}}+\phi \hat{\mathbf{t}} \wedge \hat{\mathbf{x}}+\psi \hat{\mathbf{t}} \wedge \hat{\mathbf{y}},$$
where
$$\begin{aligned}
\alpha & =-N(2 L+C-H+A-F) \\
\beta & =-L(2 L+C-H+A-F)+d_{\mathbf{k}-\mathbf{t}} L-d_{\mathbf{t}}(C-H)+d_{\mathbf{k}}(A-F), \\
\gamma & =-d_{\mathbf{x}}(L+C-H), \\
\delta & =-d_{\mathbf{y}}(L+C-H), \\
\phi & =-d_{\mathbf{x}}(L+A-F), \\
\psi & =-d_{\mathbf{y}}(L+A-F) .
\end{aligned}$$

The central curvature $c$ is defined by the equation
$$\rho^{\wedge 2}=c \omega^{\wedge 2} .$$
If $c$ is constant, we write $c=\lambda$, and call the corresponding metric a central metric. In terms of the Ricci coefficients (10), we then have
$$c=\alpha \beta-\gamma \psi+\delta \phi=\lambda,$$
because $\rho^{\wedge 2}=2 c \hat{\mathbf{x}} \wedge \hat{\mathbf{y}} \wedge \hat{\mathbf{k}} \wedge \hat{\mathbf{t}}$ while $\omega^{\wedge 2}=2 \hat{\mathbf{x}} \wedge \hat{\mathbf{y}} \wedge \hat{\mathbf{k}} \wedge \hat{\mathbf{t}}$. Such a central metric will not be Einstein if either at least one of $\gamma, \delta, \phi, \psi$ is not identically zero or $\alpha$ and $\beta$ are not both equal to the same constant.

We now recall a function built in to our ansatz that gave rise in [MR1] to the independent variable in a system of ODEs used in both [MR1] and [MR2].

The Lie bracket relations (3)-(5) imply that the distribution spanned by $\mathbf{k}+\mathbf{t}$, x and y is integrable. Since this distribution is orthogonal to k - t, while the latter vector field has constant length and is easily seen to have geodesic flow,
it follows that it is locally a gradient (cf. [ON, Cor. 12.33]). Thus, there exists a smooth function $\tau$ defined in some open set $V \subset U$, such that
$$\mathbf{k}-\mathbf{t}=\nabla \tau .$$
Consider now the six functions $P, Q, R, S, L, N$, where the last two are as in (3), and the first four are given in terms of four of the functions in (4)-(5) by
$$\begin{aligned}
P & =(B-C)+(F-G), & Q & =(B-C)-(F-G), \\
R & =\sqrt{(B+C)^{2}+(F+G)^{2}}, & S & =\tan ^{-1}\left(\frac{B+C}{F+G}\right),
\end{aligned}$$
where $S$ is only defined on the set $\{F+G\} \neq 0$.
In terms of these variables, it is shown in the appendix that in case $A, B, \ldots H, L$ and $N$ are each a composition of a function of $\tau$, the ansatz equations simplify to five ODEs (89) involving those functions. In particular the ODE giving the central curvature equation takes the form
$$-N(2 L+N-P / 2)\left[-L(2 L+N-P / 2)+\left(2 L^{\prime}+N^{\prime}-P^{\prime} / 2\right)\right]=\lambda .$$

\section*{4. Cohomogeneity one examples}

It was shown in [MR1] that the ansatz of section 3 includes as a special case cohomogeneity one diagonal Kähler metrics under the action of a unimodular group in dimension three. In this section we review their construction, and derive the central metric equation for such metrics.

Assume that $(M, g)$ is a 4-dimensional Riemannian manifold admitting a proper isometric action by a three dimensional Lie group $\mathcal{G}$ with cohomogeneity one having a discrete isotropy group. Assuming also that $\mathcal{G}$ is a unimodular group, we choose a frame of left-invariant vector fields $X_{1}, X_{2}, X_{3}$, and dual coframe consisting of left-invariant 1-forms $\sigma_{1}, \sigma_{2}, \sigma_{3}$. These satisfy
$$\begin{array}{ll}
{\left[X_{1}, X_{2}\right]=-p_{3} X_{3},} & d \sigma_{1}=p_{1} \sigma_{2} \wedge \sigma_{3}, \\
{\left[X_{2}, X_{3}\right]=-p_{1} X_{1},} & d \sigma_{2}=p_{2} \sigma_{3} \wedge \sigma_{1}, \\
{\left[X_{3}, X_{1}\right]=-p_{2} X_{2} .} & d \sigma_{3}=p_{3} \sigma_{1} \wedge \sigma_{2} .
\end{array}$$
for some constants $p_{1}, p_{2}, p_{3}$. Cohomogeneity one metrics for such groups are also described as having Bianchi type A. A diagonal such metrics takes the form
$$g=(a b c)^{2} d t^{2}+a^{2} \sigma_{1}^{2}+b^{2} \sigma_{2}^{2}+c^{2} \sigma_{3}^{2},$$
for functions $a, b, c$ of $t$. We note that, of course considering the orthogonal frame $\partial_{t}, X_{1}, X_{2}, X_{3}$ dual to $d t, \sigma_{1}, \sigma_{2}, \sigma_{3}$, on $M, \partial_{t}$ commutes, of course, with all $X_{i}, i=1,2,3$.

Following Dancer and Strachan [DS1], denoting $w_{1}=b c, w_{2}=a c$, and $w_{3}=a b$, we define functions $\alpha, \beta$, and $\gamma$ so that
$$\begin{aligned}
& w_{1}^{\prime}=p_{1} w_{2} w_{3}+\alpha w_{1}, \\
& w_{2}^{\prime}=p_{2} w_{1} w_{3}+\beta w_{2}, \\
& w_{3}^{\prime}=p_{3} w_{1} w_{2}+\gamma w_{3} .
\end{aligned}$$

They show that (modulo reordering the frame vectors) the only Kähler structures $(M, g, J)$ with $g$ of the form (16) have complex structure determined by
$$J \partial_{t}=a b X_{3} \quad \text { and } \quad J X_{1}=\frac{a}{b} X_{2},$$
and $\alpha, \beta$, and $\gamma$ satisfy
$$\alpha=\beta \quad \text { and } \quad \gamma=0 .$$
The Kähler form is then given by
$$\omega=a b c^{2} d t \wedge \sigma_{3}+a b \sigma_{1} \wedge \sigma_{2}=w_{1} w_{2} d t \wedge \sigma_{3}+w_{3} \sigma_{1} \wedge \sigma_{2},$$
and $w_{1}, w_{2}, w_{3}$ satisfy
$$\begin{aligned}
& w_{1}^{\prime}=p_{1} w_{2} w_{3}+\alpha w_{1}, \\
& w_{2}^{\prime}=p_{2} w_{1} w_{3}+\alpha w_{2}, \\
& w_{3}^{\prime}=p_{3} w_{1} w_{2} .
\end{aligned}$$
This, in terms of $a, b, c$ implies
$$\begin{aligned}
2 a^{\prime} / a & =-p_{1} a^{2}+p_{2} b^{2}+p_{3} c^{2}, \\
2 b^{\prime} / b & =p_{1} a^{2}-p_{2} b^{2}+p_{3} c^{2}, \\
2 c^{\prime} / c & =p_{1} a^{2}+p_{2} b^{2}-p_{3} c^{2}+2 \alpha .
\end{aligned}$$

We recall the prescription that makes this model fit with the ansatz of Section 3. The orthonormal frame and dual coframe are given by
$$\begin{array}{ll}
\mathbf{k}=\frac{\sqrt{2}}{2}\left(\frac{1}{c} X_{3}+\frac{1}{a b c} \partial_{t}\right), & \hat{\mathbf{k}}=\frac{\sqrt{2}}{2}\left(c \sigma_{3}+a b c d t\right), \\
\mathbf{t}=\frac{\sqrt{2}}{2}\left(\frac{1}{c} X_{3}-\frac{1}{a b c} \partial_{t}\right), & \hat{\mathbf{t}}=\frac{\sqrt{2}}{2}\left(c \sigma_{3}-a b c d t\right), \\
\mathbf{x}=\frac{X_{1}}{a}, & \hat{\mathbf{x}}=a \sigma_{1}, \\
\mathbf{y}=\frac{X_{2}}{b}, & \hat{\mathbf{y}}=b \sigma_{2} .
\end{array}$$
One can easily check that relations (3)-(5) hold with these choices.
Next the functions of the ansatz are given in terms of $a, b, c$, by
$$\begin{array}{ll}
A=-E=-\frac{a^{\prime}}{\sqrt{2} a^{2} b c}=-\frac{1}{a} \frac{d a}{d \tau}, & B=F=-\frac{b p_{2}}{\sqrt{2} a c}, \\
D=-H=-\frac{b^{\prime}}{\sqrt{2} a b^{2} c}=-\frac{1}{b} \frac{d b}{d \tau}, & C=G=\frac{a p_{1}}{\sqrt{2} b c}, \\
L=-\frac{c^{\prime}}{\sqrt{2} a b c^{2}}=-\frac{1}{c} \frac{d c}{d \tau}, & N=-\frac{c p_{3}}{\sqrt{2} a b} .
\end{array}$$
Here the prime denotes differentiation with respect to $t$, while the expressions in terms of $d / d \tau$ hold due to the relation between $\tau$ and $t$ given by
$$\hat{\mathbf{k}}-\hat{\mathbf{t}}=d \tau=\sqrt{2} a b c d t, \quad \frac{d}{d \tau}=\frac{1}{\sqrt{2} a b c} \frac{d}{d t} .$$

Finally, we give the functions $P, Q, R, S$ of the change of variables (13).
$$\begin{aligned}
P & =-\sqrt{2} \frac{a^{2} p_{1}+b^{2} p_{2}}{a b c}, & Q & =0, \\
R & =\frac{a^{2} p_{1}-b^{2} p_{2}}{a b c}, & S & =\frac{\pi}{4} .
\end{aligned}$$

From the point of view of the ansatz, the four relations in (6)-(7) that imply the Kähler condition impose only two additional relations here, say $A+D=N$ and $B+C=H-E$, giving
$$\begin{aligned}
& \frac{a^{\prime}}{a}+\frac{b^{\prime}}{b}=p_{3} c^{2}, \\
& \frac{b^{\prime}}{b}-\frac{a^{\prime}}{a}=p_{1} a^{2}-p_{2} b^{2}
\end{aligned}$$
which are equivalent to (23)-(24). Our remaining task is to determine how the condition that the metric is central constrain $\alpha$ in (25).

The central metric equation (11), is given in the variables (13) by (14):
$$-N(2 L+N-P / 2)\left[-L(2 L+N-P / 2)+\frac{d}{d \tau}(2 L+N-P / 2)\right]=\lambda .$$
Calculating using the above formulas for $L, N, P$ and also (25), we have
$$\begin{aligned}
2 L+N-P / 2 & =\frac{1}{\sqrt{2} a b c}\left(-2 \frac{c^{\prime}}{c}-p_{3} c^{2}+p_{1} a^{2}+p_{2} b^{2}\right) \\
& =\frac{1}{\sqrt{2} a b c}(-2 \alpha) .
\end{aligned}$$
So that (14) takes the form
$$\frac{p_{3} c}{\sqrt{2} a b}\left(\frac{-2 \alpha}{\sqrt{2} a b c}\right)\left[\frac{c^{\prime}}{\sqrt{2} a b c^{2}} \frac{-2 \alpha}{\sqrt{2} a b c}+\frac{1}{\sqrt{2} a b c}\left(\frac{-2 \alpha}{\sqrt{2} a b c}\right)^{\prime}\right]=\lambda .$$
A relatively straightforward simplification of this which also uses (26) yields, the equivalent form
$$p_{3}\left(\alpha^{2}\right)^{\prime}=2 c^{2}\left(\lambda(a b)^{4}+p_{3}^{2} \alpha^{2}\right)$$
This equation, together with (23)-(25) constitutes the ODE system for diagonal Bianchi IX central metrics.

Note that setting $p_{3}=0$ (hence also $N=0$ ) forces $\lambda=0$ but no other constraints. On the other hand, setting $\lambda=0$ yields, for $p_{3} \neq 0$ the equation
$$\alpha^{\prime}=p_{3} c^{2} \alpha$$
which will play a major role in the following sections.
Additionally, one can check that the formula $\alpha=\mp\left(\sqrt{\lambda} / p_{3}\right)(a b)^{2}, \lambda>0$ reduces (28) to an identity, and this corresponds to the fact that this is the Kähler-Einstein condition (for $p_{3} \neq 0$, see [MR1]). On the other hand, a Kähler-Einstein metric with $p_{3}=0$ must be Ricci flat $(\lambda=0)$ and necessarily $\alpha^{\prime}=0$. But note in general from (10) that $\alpha=0$ is necessarily a Ricci flat case, so such solutions will not concern us.

\section*{5. cohomogeneity one central flat metric under a Heisenberg group quotient action.}
5.1. The equations. On the Heisenberg group, with $p_{1}=0, p_{2}=0$ and $p_{3}=1$, equations (23)-(25) and (28) take the form
$$\begin{aligned}
2 \frac{a^{\prime}}{a} & =c^{2}, \\
2 \frac{b^{\prime}}{b} & =c^{2}, \\
2 \frac{c^{\prime}}{c} & =-c^{2}+2 \alpha, \\
\alpha^{\prime} & =c^{2}\left(\alpha+\lambda(a b)^{4} / \alpha\right) .
\end{aligned}$$
Since $(a / b)^{\prime}=0$ is a first integral, $b$ is a constant multiple of $a$, so that potential metrics are so-called biaxial. From now on we assume this constant is equal to 1. Additionally, we adopt the form used in [AM2, MR2] by making the change of variables $a^{2} d t=d q$. Then, setting $\phi(q):=a^{2}$, we see from (29) that
$$\phi^{\prime}(q)=2 a \frac{d a}{d q}=2 a \frac{d a}{d t} \frac{d t}{d q}=2 a \frac{d a}{d t} \frac{1}{a^{2}}=c^{2} .$$
It follows that the metric takes the form
$$g=\phi(q)\left(\sigma_{1}^{2}+\sigma_{2}^{2}\right)+\phi^{\prime}(q)\left(\sigma_{3}^{2}+d q^{2}\right)$$
with Kähler form
$$\omega=d\left(\phi(q) \sigma_{3}\right) .$$
We now use a prime exclusively for the derivative with respect to $q$, while $\alpha$ will be considered, depending on the context, as a function of $t$ or a function of $q$. The two equations (30)-(31) then translate as follows
$$\begin{aligned}
\frac{\phi^{\prime \prime}(q)}{\phi^{\prime}(q)} & =2 c \frac{d c}{d t} \frac{d t}{d q} \frac{1}{c^{2}}=\left(-c^{2}+2 \alpha\right) \frac{1}{a^{2}}=-\frac{\phi^{\prime}(q)}{\phi(q)}+2 \frac{\alpha}{\phi(q)}, \\
\alpha^{\prime}(q) & =\frac{d \alpha}{d t} \frac{d t}{d q}=c^{2}\left(\alpha+\lambda \frac{a^{8}}{\alpha}\right) \frac{1}{a^{2}}=\frac{\phi^{\prime}(q)}{\phi(q)}\left(\alpha+\lambda \frac{\phi^{4}}{\alpha}\right) .
\end{aligned}$$
Or, simplified
$$\begin{aligned}
\frac{\left(\phi^{2}\right)^{\prime \prime}}{\left(\phi^{2}\right)^{\prime}} & =2 \frac{\alpha}{\phi} \\
\alpha^{\prime} & =\frac{\phi^{\prime}}{\phi}\left(\alpha+\lambda \frac{\phi^{4}}{\alpha}\right) .
\end{aligned}$$

We now set $\lambda=0$. Then (34) implies (if $\alpha$ is nonzero) that $\alpha / \phi$ is constant, which again we choose to be 1. Substituting this into (33) gives an equation with explicit solution
$$\phi=C \sqrt{e^{2 q}+B}, \quad C>0, B \text { constants. }$$

For simplicity we choose $C=1$ and $B=c_{1}^{2}, c_{1}>0$. Then for $q$ real valued, $\phi$ takes values in $\left(c_{1}, \infty\right)$, and
$$\phi^{\prime}=\frac{e^{2 q}}{\left(e^{2 q}+c_{1}^{2}\right)^{1 / 2}} .$$
We show that $g$ is complete, in the next few subsections. Here we point out that $g$ is not Ricci flat. In fact as $p_{3}$ is nonzero, the formula near the end of section 4 shows that for Ricci flatness we must have $\alpha=0$, but in this solution $\alpha=\phi \neq 0$.
5.2. Setup. As in [AM2], in order to avail ourselves of the methods of [VZ], we consider a cohomogeneity one action under the quotient $\mathcal{G}=\mathrm{nil}_{3} / \tilde{\mathbb{Z}}$ of the Heisenberg group by the infinite cyclic group lying in its center, and given by
$$\tilde{\mathbb{Z}}:=\left\{\left.\left[\begin{array}{ccc}
1 & 0 & 2 \pi n \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right] \right\rvert\, n \in \mathbb{Z}\right\} .$$
$\mathcal{G}$ has center $K$ isomorphic to $S O(2)$, whose transitive action on the circle $S^{1}$ extends to a linear action on $V:=\mathbb{R}^{2}$. We consider the homogeneous vector bundle $M=\mathcal{G} \times_{K} V$ (in which points of the product are identified according to $(g, v) \sim\left(g k^{-1}, k v\right)$ for $k \in K$ ). $\mathcal{G}$ acts on $M$ by left multiplication on the first factor. The action of $\mathcal{G}$ has trivial isotropy at points of a regular orbit, but isotropy $K$ at a point of the singular orbit $\mathcal{G} / K \approx \mathbb{R}^{2}$.
5.3. Length of an escaping curve. We now choose a left-invariant frame for $\mathcal{G}$ which is given in coordinates $x, y, z$ by $X_{1}=\partial_{x}, X_{2}=\partial_{y}+x \partial_{z}, X_{3}=-\partial_{z}$, to which we will add on $M$ the vector field $\partial_{q}$. Note that the domain of this coordinate system is open and dense in $M$, and $z$ is bounded due to the fact that we are considering a quotient.

The corresponding coframe consists of $d q$ and the left invariant coframe for the group given by $\sigma_{3}=x d y-d z, \sigma_{1}=d x, \sigma_{2}=d y$. Given a curve $\gamma(s): I \rightarrow$ $M$ of finite length $L(\gamma)$, with coordinate presentation $(x(s), y(s), z(s), q(s))$, we have
$$\begin{aligned}
\gamma^{\prime} & =x^{\prime} \partial_{x}+y^{\prime} \partial_{y}+z^{\prime} \partial_{z}+q^{\prime} \partial_{q} \\
& =\sigma_{1}\left(\gamma^{\prime}\right) X_{1}+\sigma_{2}\left(\gamma^{\prime}\right) X_{2}+\sigma_{3}\left(\gamma^{\prime}\right) X_{3}+d q\left(\gamma^{\prime}\right) \partial_{q}
\end{aligned}$$
so that
$$g\left(\gamma^{\prime}, \frac{X_{1}}{\left|X_{1}\right|}\right)=x^{\prime} \sqrt{\phi}, \quad g\left(\gamma^{\prime}, \frac{X_{2}}{\left|X_{2}\right|}\right)=y^{\prime} \sqrt{\phi}, \quad g\left(\gamma^{\prime}, \frac{\partial_{q}}{\left|\partial_{q}\right|}\right)=q^{\prime} \sqrt{\phi^{\prime}} .$$
It follows that the length of $\gamma$ satisfies the Cauchy-Schwarz estimates
$$\begin{aligned}
L(\gamma)=\int_{I}\left|\gamma^{\prime}(s)\right| d s & \geq \inf _{I}(\sqrt{\phi(q)})\left|\int_{I} x^{\prime} d s\right|, \\
L(\gamma) & \geq \inf _{I}(\sqrt{\phi(q)})\left|\int_{I} y^{\prime} d s\right|, \\
L(\gamma) & \geq\left|\int_{I} \sqrt{\phi^{\prime}(q)} q^{\prime} d s\right|
\end{aligned}$$

Now the right hand side of (37) equals
$$\left|\int_{q(I)} \sqrt{\phi^{\prime}(q)} d q\right| .$$
If $q(I)$ has $q=\infty$ as an endpoint, this integral is infinite, so it follows that this cannot occur if $\gamma$ has finite length. On the other hand the infima in (35)-(36) are positive since this holds for any $q \in \mathbb{R}$. It then follows from these two equations that for a finite length curve, $x$ and $y$ are bounded. Thus such a curve can only leave every compact set in $M$ if a sequence of its $q$ values approach $-\infty$. To address this problem we have to attach a "bolt" to $M$ at $q=-\infty$, that is, a singular orbit for the group action, and see that the metric and Kähler form extend smoothly to it.
5.4. Attaching a bolt. As $\phi^{\prime}(q)\left(d q^{2}+\sigma_{3}^{2}\right)=\frac{d \phi^{2}}{\phi^{\prime}(q)}+\phi^{\prime}(q) \sigma_{3}^{2}$, and $\phi^{\prime}=\left(\phi^{2}-\right.$ $\left.c_{1}^{2}\right) / \phi$, the metric $g$ can be written in the form
$$g=\frac{\phi}{\phi^{2}-c_{1}^{2}} d \phi^{2}+\frac{\phi^{2}-c_{1}^{2}}{\phi} \sigma_{3}^{2}+\phi\left(\sigma_{1}^{2}+\sigma_{2}^{2}\right)$$
defined on the domain $\phi \in\left(c_{1}, \infty\right)$.
To apply the Verdiani-Ziller smoothness conditions [VZ] for a metric at a singular orbit. We write the metric near $c_{1}$ in the for $d r^{2}+h_{r}$ where $r=0$ corresponds to $\phi=c_{1}$. Note that converting equations (29)-(31) into this form amounts to dividing their right hand side by $a b c$. From this one can see that a solution can be extended smoothly if $a, b, \alpha$ are even in $r$ and $c$ is odd in $r$. this mean that $\phi=a^{2}$ and $\phi^{\prime}=c^{2}$ are even as functions of $r$.

Computing asymptotically near $c_{1}$, we have $d r=\sqrt{\frac{\phi}{\phi^{2}-c_{1}^{2}}} d \phi \approx \sqrt{\frac{c_{1}}{\left(\phi-c_{1}\right) 2 c_{1}}} d \phi$ so that $r \approx \sqrt{2\left(\phi-c_{1}\right)}$. Thus near $c_{1}$
$$g \approx d r^{2}+\frac{r^{4} / 4+r^{2} c_{1}}{r^{2} / 2+c_{1}} \sigma_{3}^{2}+\left(r^{2} / 2+c_{1}\right)\left(\sigma_{1}^{2}+\sigma_{2}^{2}\right) .$$

We compare this with the smoothness conditions in [VZ], which in our case, for $\mathfrak{m}=\operatorname{span}\left(X_{1}, X_{2}\right), \mathfrak{p}=\operatorname{span}\left(X_{3}\right)$, are, near $r=0$,
$$\begin{aligned}
& g(\mathfrak{m}, \mathfrak{m}) \text { is even in } r, \\
& g(\mathfrak{p}, \mathfrak{m})=r^{2} \psi\left(r^{2}\right), \\
& g(X, X)=\bar{a}^{2} r^{2}+r^{4} \xi\left(r^{2}\right) \text { for } X \in \mathfrak{p} .
\end{aligned}$$
Only the last condition is not automatic in our case, and in it, $\bar{a}$ denotes the cardinality of the intersection of the (trivial) stabilizer with $\{\exp (\theta X) \mid 0 \leq$ $\theta \leq 2 \pi\}$, with $X$ normalized so that the latter set is a closed one-parameter subgroup. For the group $\mathcal{G}$ and $X=-X_{3}$ we have $\bar{a}=1$ and it is thus sufficient to check the form of $g(X, X)$ for this $X$. The coefficient of $\sigma_{3}^{2}$ is
$$\frac{r^{4} / 4+r^{2} c_{1}}{r^{2} / 2+c_{1}}=r^{2}-\frac{1}{4 c_{1}} r^{4}+O\left(r^{6}\right) .$$

Thus the conditions for smoothness of the metric are verified.
The Kähler form similarly extends smoothly to the singular fiber. In fact, it is
$$\begin{aligned}
& d \phi \wedge \sigma_{3}+\phi\left(\sigma_{1} \wedge \sigma_{2}\right)=d\left[\left(\sqrt{\phi-c_{1}}\right)^{2}\right] \wedge \sigma_{3}+\phi\left(\sigma_{1} \wedge \sigma_{2}\right) \\
& \approx 2^{-1} d\left(r^{2}\right) \wedge \sigma_{3}+\left(r^{2} / 2+c_{1}\right)(\hat{\mathbf{x}} \wedge \hat{\mathbf{y}}),
\end{aligned}$$
whereas modifying the conditions in [VZ] so that they apply to a 2-form, shows that in our case smoothness requires that near $r=0$ the coefficient of $d r \wedge \sigma_{3}$ has the form $r \psi\left(r^{2}\right)$ and the coefficient of $\sigma_{1} \wedge \sigma_{2}$ is even. The fact that $\phi$ is even and the above form conclude the proof. We thus showed

Theorem 2. For every $c_{1}>0$ the metric
$$g=\frac{e^{2 q}}{\sqrt{e^{2 q}+c_{1}^{2}}}\left(d q^{2}+\sigma_{3}^{2}\right)+\sqrt{e^{2 q}+c_{1}^{2}}\left(\sigma_{1}^{2}+\sigma_{2}^{2}\right), \quad q \in \mathbb{R}$$
defined on the $\mathcal{G} \times_{S O(2)} \mathbb{R}^{2}$, with $\mathcal{G} \simeq \operatorname{nil}_{3} / \tilde{\mathbb{Z}}$, is complete and centrally flat.
We note that it is not too difficult to classify all complete diagonal cohomogeneity one centrally flat metrics under the action of $\mathcal{G}$. We demonstrate how to carry this out in a more difficult case in the next section.

\section*{6. Centrally flat metric under the action of the compact group $S U(2)$.}
6.1. The equations. We now consider the case where the action is by the compact group $S U(2)$ for a metric with central curvature $\lambda=0$. With the choices $p_{1}=p_{2}=p_{3}=1$, the system (23)-(25),(28) becomes
$$\begin{aligned}
a^{\prime} & =\frac{a}{2}\left(-a^{2}+b^{2}+c^{2}\right) \\
b^{\prime} & =\frac{b}{2}\left(a^{2}-b^{2}+c^{2}\right) \\
c^{\prime} & =\frac{c}{2}\left(a^{2}+b^{2}-c^{2}+2 \alpha\right) \\
\alpha^{\prime} & =c^{2} \alpha .
\end{aligned}$$
Note that we must take $\lambda=0$ to ensure that the right hand side of the system is smooth, which allows us to employ the center manifold theorem.

We observe immediately that this can be reduced to a system of three equations in three unknown functions. From the first and second equations, it follows that
$$\frac{d}{d t}(a b)=a b c^{2} .$$
Combining this with the fourth equation, we have
$$\frac{d}{d t} \log \frac{a b}{\alpha}=0,$$
and so there exists a constant $A$ such that
$$\log \frac{a b}{\alpha}=A,$$
and so $\alpha=e^{-A}(a b)$. With this, the fourth equation can be eliminated, and the third equation rewritten. The system becomes
$$\begin{aligned}
& a^{\prime}=\frac{a}{2}\left(-a^{2}+b^{2}+c^{2}\right) \\
& b^{\prime}=\frac{b}{2}\left(a^{2}-b^{2}+c^{2}\right) \\
& c^{\prime}=\frac{c}{2}\left(a^{2}+b^{2}+2 e^{-A} a b-c^{2}\right) .
\end{aligned}$$

By a uniqueness argument, if an analytic solution defined on a maximal interval has an initial value in the region
$$\mathcal{R}=\left\{(a, b, c) \in \mathbb{R}^{3} \mid a, b, c>0\right\},$$
then the trajectory will remain in $\mathcal{R}$ for all values of $t$ for which the solution exists. From now on we only consider such solutions, for which the metric will defined for values of $t$ in this interval.
6.2. Linearization at equilibrium solutions and preliminary calculations. Equilibrium solutions that lie in $\overline{\mathcal{R}}$ are $(q, q, 0),(0, q, q)$, and $(q, 0, q)$, for $q \geq 0$. The coefficient matrix of the linearized system at ( $q, q, 0$ ) has eigenvalues $0,-2 q^{2}, q^{2}\left(1+e^{-A}\right)$. At $(0, q, q)$, the eigenvalues are $q^{2}, 0,-2 q^{2}$, and at $(q, 0, q)$, the eigenvalues are $0, q^{2}-2 q^{2}$. In all cases, if $q>0$ one of these eigenvalues is positive. The Center Manifold Theorem guarantees that near an equilibrium solution for which the linearized system has a positive eigenvalue with no multiplicity, the system admits an unstable curve.

Next, one verifies
Lemma 6.1. For any solution to (38), we have
$$\begin{aligned}
\frac{d}{d t}(a b) & =(a b) c^{2} \\
\frac{d}{d t}(a c) & =a c\left(b^{2}+e^{-A} a b\right) \\
\frac{d}{d t}(b c) & =b c\left(a^{2}+e^{-A} a b\right) \\
\frac{d}{d t}\left(\frac{a}{b}\right) & =\frac{a}{b}\left(-a^{2}+b^{2}\right) \\
\frac{d}{d t}\left(\frac{a}{c}\right) & =\frac{a}{c}\left(-a^{2}-e^{-A} a b+c^{2}\right) \\
\frac{d}{d t}\left(a^{2}-b^{2}\right) & =\left(a^{2}-b^{2}\right)\left(-a^{2}-b^{2}+c^{2}\right) \\
\frac{d}{d t}\left(a^{2}-c^{2}\right) & =-\left(a^{2}-c^{2}\right)\left(a^{2}-b^{2}+c^{2}\right)-2 e^{-A} a b c^{2} .
\end{aligned}$$

These are straightforward consequences of the equations of the system.
An immediate implication of these calculations is that in $\mathcal{R}$, the products $a b, a c$, and $b c$ are increasing functions. It follows that at any value of $t$, at most one of the three can be decreasing, and also that all three products have finite, non-negative limits as $t$ approaches the lower endpoint of the maximal interval on which a solution exists. As a further implication, from the equation for $d / d t(a / b)$, we see by uniqueness that either $a$ is identically equal to $b$ or never equal to $b$. Since the roles of $a$ and $b$ are interchangeable, we may therefore assume that if $a$ and $b$ do not coincide, that it is $a$ that is greater. Finally, this makes $b$ a strictly increasing function.

Now choose an initial value in the region $\mathcal{R}$. Local existence theory provides for existence to the initial value problem on a non-empty interval; let $(\xi, \eta)$ be the maximal interval of existence for a given initial value. We investigate whether there are trajectories which correspond to complete metrics.
6.3. A maximal solution interval bounded from below. We will first discover that any candidates for complete metrics correspond to trajectories for which $\xi=-\infty$. This explains the attention paid earlier to the unstable curves, for they are such trajectories. We then investigate whether any of these do in fact give rise to complete metrics.

Proposition 6.2. Trajectories for which $\xi>-\infty$ correspond to incomplete metrics.

Proof. The limit of $b$ as $t \rightarrow \xi$ is zero: If the limit of $b$ were non-zero, then both $a$ and $c$ would also have limits, and then all three functions could be extended continuously to $\xi$ itself, violating the maximality of the interval $(\xi, \eta)$. Therefore,
$$\lim _{t \rightarrow \xi} b(t)=0 .$$

We observed above that at any particular point, at most one of the functions $a, b$, or $c$ can be decreasing. However, under the assumption that $a \geq b$, the derivative of $b$ is positive, so $b$ increases throughout the entire interval of existence. Moreover, it is not possible that all three increase on all of $(\xi, \eta)$, because if they did, then all three could be extended continuously to the lower endpoint $\xi$, contradicting the maximality of the interval $(\xi, \eta)$. There remain therefore two possibilities to consider.
(i) Suppose at some point $u \in(\xi, \eta)$, that $a^{\prime}(u)<0$. Then $-a^{2}+b^{2}+c^{2}<0$ at this point. Calculating the derivative of this quantity, we find that
$$\frac{d}{d t}\left(-a^{2}+b^{2}+c^{2}\right)=a^{4}-\left(b^{2}-c^{2}\right)^{2}+2 e^{-A} a b c^{2}>0 .$$
In other words, whenever $-a^{2}+b^{2}+c^{2}$ is negative, the derivative of this quantity is positive. This implies that if $a$ decreases at any point $u$, then it decreases on all of $(\xi, u)$. A calculation also shows that where $a^{\prime}(t)<0$, that $a^{\prime \prime}(t)>0$, and this will be used later.

Since at most one of the three functions can decrease at a point or on an interval, $c$ must be increasing on all of $(\xi, u)$. Therefore, $\lim _{t \rightarrow \xi^{-}} c(t)$ exists.

We already know that $b \rightarrow 0$ as $t \searrow \xi$. If $a(t)$ approached a finite limit as $t$ approached $\xi$, then all three functions could be continuously extended to $\xi$, contradicting the maximality of the interval of existence. Therefore,
$$\lim _{t \rightarrow \xi^{-}} a(t)=\infty .$$
Since $a \rightarrow \infty$, but $a c$ approaches a finite limit, it must be that $\lim _{t \rightarrow \xi} c(t)=0$. It follows, then, that as $t \searrow \xi$, the system can be approximated by
$$\begin{aligned}
a^{\prime} & =\frac{a}{2}\left(-a^{2}\right) \\
b^{\prime} & =\frac{b}{2}\left(a^{2}\right) \\
c^{\prime} & =\frac{c}{2}\left(a^{2}+2 e^{-A} B\right),
\end{aligned}$$
where $B=\lim _{t \rightarrow \xi} a b$, a non-negative number. This system can be solved explicitly. Solving, we find that
$$\begin{aligned}
& a(t) \simeq \frac{1}{\sqrt{t-\xi}}, \\
& b(t) \simeq C \sqrt{t-\xi}, \\
& c(t) \simeq D \sqrt{t-\xi},
\end{aligned}$$
for constants $C$ and $D$ whose values do not affect the completeness question. Regarding that question, we recall that the metric is of the form
$$g=(a b c)^{2} d t^{2}+a^{2} \sigma_{1}^{2}+b^{2} \sigma_{2}^{2}+c^{2} \sigma_{3}^{2} .$$
Let $\gamma(s)$ be a curve that is constant in the orbit direction, and with $t(s)=s$. Then
$$l(\gamma)=\lim _{\varepsilon \rightarrow 0} \int_{\xi+\varepsilon}^{t_{1}}(a b c)(s) d s<\infty$$
by direct calculation. Since the length of this curve is finite, the distance to the boundary at $t=\xi$ is also finite, and the metric is incomplete.
(ii) There is a point $u \in(\xi, \eta)$ at which $c^{\prime}(u)<0$. Then $a^{2}+b^{2}+2 e^{-A} a b-c^{2}<$ 0 at that point. Similarly to above, we calculate the derivative of this quantity:
$$\frac{d}{d t}\left(a^{2}+b^{2}+2 e^{-A} a b-c^{2}\right)=c^{4}-\left(a^{2}-b^{2}\right)^{2} .$$
At $u$, we have
$$c^{2}>a^{2}+b^{2}+2 e^{-A} a b>a^{2}+b^{2},$$
and therefore,
$$c^{4}>\left(a^{2}+b^{2}\right)^{2} \geq\left(a^{2}-b^{2}\right)^{2} .$$
We therefore see that the derivative of this quantity is positive, implying that $c^{\prime}(t)<0$ on the entire interval $(\xi, u)$. We also find that $c^{\prime \prime}(t)>0$ on this interval. It must be that $c \rightarrow \infty$ and $a, b \rightarrow 0$ as $t \rightarrow \xi$. Permuting the roles of $a, b$, and $c$ in the approximated equations that appeared in Case (i), we again find that the metric is incomplete. \(\square\)
6.4. Maximal solution intervals of the form $(-\infty, \eta)$. We turn now to those trajectories for which $\xi=-\infty$. Analyzing the behavior of these solutions as $t \rightarrow-\infty$, we find which equilibrium points these approach.

Proposition 6.3. A trajectory for which $\xi=-\infty$ converges to an equilibrium solution of the form $(q, q, 0)$, with $q>0$, or $(q, 0, q)$ as $t \rightarrow-\infty$.

Proof. Since $b$ is increasing, its limit as $t \rightarrow-\infty$ exists, and so again the behavior of $b$ gives a convenient way to split into cases.
(1) Suppose first that $\lim _{t \rightarrow-\infty} b(t)>0$. In this case, and because $a b$ and $b c$ are also increasing functions, $a$ and $c$ also have finite limits as $t \rightarrow-\infty$. Comparing to the list of possible equilibrium solutions, and remembering that we have assumed without loss of generality that $a(t) \geq b(t)$, we see that $(a(t), b(t), c(t)) \rightarrow(q, q, 0)$, with $q>0$. This implies that
$$\lim _{t \rightarrow-\infty} \frac{a(t)}{b(t)}=1$$
From the earlier lemma,
$$\frac{d}{d t}\left(\frac{a}{b}\right)=\frac{a}{b}\left(-a^{2}+b^{2}\right) .$$
This is non-positive under the assumption that $a \geq b$, and it also follows that $a(t) / b(t) \geq 1$ and is either strictly decreasing or else identically equal to one. It can only be that $a(t) \equiv b(t)$ for all $t \in(-\infty, \eta)$.
(2) Now suppose that $\lim _{t \rightarrow-\infty} b(t)=0$. There are several possibilities to consider.
(i) Suppose there exists $u \in(-\infty, \eta)$ at which $a^{\prime}(u)<0$. The earlier calculation showed that at any point or on any interval where $-a^{2}+b^{2}+c^{2}<0$, that the derivative of this quantity is positive, and therefore $-a^{2}+b^{2}+c^{2}$ remains negative on all of $(-\infty, u)$. Then $a$ is decreasing on all of $(-\infty, u)$, and since at most one of the three functions can decrease on an interval, it follows that $b$ and $c$ are non-decreasing. Those same calculations also give us that $a^{\prime \prime}(t)>0$ on this interval and that
$$\lim _{t \rightarrow-\infty} a(t)=\infty .$$
Since both $\lim _{t \rightarrow-\infty} c(t)$ and $\lim _{t \rightarrow-\infty} a c$ are finite numbers, it must be that $\lim _{t \rightarrow-\infty} c(t)=0$. For large, negative values of $t$ therefore, the first equation can be approximated in the asymptotic sense by
$$a^{\prime}=\frac{a}{2}\left(-a^{2}\right) .$$
By a direct calculation, $a$ diverges at a finite value in the interval of existence, which is a contradiction.
(ii) The second possibility is that $c$ decreases at some point $u \in(-\infty, \eta)$. As calculated previously, if $c^{\prime}(u)>0$, that is, if $a^{2}+b^{2}+2 e^{-A} a b-c^{2}<$ 0 at $u \in(-\infty, \eta)$, then the derivative of this quantity is positive, and so $c$ remains a decreasing function on all of $(-\infty, u)$. Also, $c^{\prime \prime}(t)>0$ on this interval, and so $\lim _{t \rightarrow-\infty} c(t)=\infty$. Because the product $a c$ has a finite limit, we have
$\lim _{t \rightarrow-\infty} a(t)=0$. The third equation can be approximated for negative values of $t$ of large magnitude by
$$c^{\prime}=\frac{c}{2}\left(-c^{2}\right),$$
implying that $c(t) \rightarrow \infty$ at an interior point, a contradiction.
(iii) If all three of $a, b$, and $c$ are increasing on all of $(-\infty, \eta)$, then all three have finite limits as $t \rightarrow-\infty$, so $(a(t), b(t), c(t))$ converges to an equilibrium solution. Checking the list, the equilibrium solution is $(q, 0, q)$, with the possibility $q=0$ not excluded. \(\square\)
6.5. Equilibrium $(\mathbf{q}, \mathbf{q}, \mathbf{0}), \mathbf{q}>\mathbf{0}$. We now investigate the completeness of the metrics that correspond to trajectories converging to equilibrium solutions of the form $(q, q, 0)$

So assume the initial value was chosen to lie on the trajectory of an unstable curve of $(q, q, 0)$, with $q>0$.
6.5.1. The endpoint $\xi=-\infty$. For large, negative values of $t$, both $a$ and $b$ can be approximated by $q$, but for $c(t)$, we examine the equation itself, in order to determine the rate at which $c(t) \rightarrow 0$. Since $c^{2}$ is small compared to $c$, the third equation can be approximated by
$$c^{\prime} \simeq\left(1+e^{-A}\right) q^{2} c .$$
For the moment, we will write $\gamma=\left(1+e^{-A}\right) q^{2}$, a positive constant. Solving the equation gives
$$c(t) \simeq k e^{\gamma t},$$
where $k$ is a further constant. The metric can then be approximated as $t \rightarrow-\infty$ by
$$g=q^{4} k^{2} e^{2 \gamma t} d t^{2}+q^{2} \sigma_{1}^{2}+q^{2} \sigma_{2}^{2}+k^{2} e^{2 \gamma t} \sigma_{3}^{2} .$$
Making the change of variables
$$y(t)=\frac{q^{2} k}{\gamma} e^{\gamma t},$$
as in [DS1], the metric can be written as
$$g=d y^{2}+q^{2} \sigma_{1}^{2}+q^{2} \sigma_{2}^{2}+\frac{\gamma^{2}}{q^{4}} y^{2} \sigma_{3}^{2},$$
or
$$g=d y^{2}+q^{2} \sigma_{2}^{2}+q^{2} \sigma_{2}^{2}+\left(1+e^{-A}\right)^{2} y^{2} \sigma_{3}^{2},$$
where $t \rightarrow-\infty$ if and only if $y \rightarrow 0$. Thus the distance to the boundary corresponding to $\xi=-\infty$ is finite. However, in this case, under certain conditions that metric and Kähler form extend smoothly to a singular orbit (a bolt). We now show this.
6.5.2. Attaching a singular orbit at $\xi=-\infty$ for equilibrium ( $q, q, 0$ ). Denoting $r=\int_{-\infty}^{r} a(s) b(s) c(s) d s$ the metric can be transformed to the form $g=d r^{2}+$ $a^{2} \sigma_{1}^{2}+b^{2} \sigma_{2}^{2}+c^{2} \sigma_{3}^{2}$. Recall that the solutions we are examining satisfy $a=b$ with equilibrium $(q, q, 0), q \neq 0$. In that case the Lie algebra of Killing vector fields is one dimension higher, and the metric is preserved by a corresponding action of $U(2)$. The manifold then has the form $M=U(2) \times_{K} \mathbb{R}^{2} \backslash\{0\}$, with $K=U(1) \times U(1)$, and we wish to examine whether it is possible to attach smoothly a singular orbit (so-called bolt) at $r=0$, where the finite distance end of the manifold resides. As the principal orbits are 3-dimensional, the isotropy group is $H=U(1)$, and $K$ acts on $K / H \approx S^{1}$ non-effectively. However one of its factors acts, of course, effectively, and since $H$ embeds as the other factor, for the purposes of examining smooth extendibility, one can equally consider just the action of $S U(2) \subset U(2)$, which is still of cohomogeneity one, and regard the manifold as $S U(2) \times_{U(1)} \mathbb{R}^{2} \backslash\{0\}$. We will take this point of view in what follows. Note that $U(1)$ acts on $\mathbb{R}^{2}$ by a restriction of one the representations of $S U(2)$.

With this change of variables, equations (38) in that case take the form
$$\begin{aligned}
& \frac{d a}{d r}=\frac{c}{2 a}, \\
& \frac{d c}{d r}=1+e^{-A}-\frac{c^{2}}{2 a^{2}} .
\end{aligned}$$
We see from these equations that $a$ can be smoothly extended as an even function and $c$ as an odd one near $r=0$. Using the notations in [VZ], we denote
$$\mathfrak{k}=\operatorname{span}\left(X_{3}\right), \quad \mathfrak{m}=\operatorname{span}\left(X_{1}, X_{2}\right)=\ell_{1} \quad V=\operatorname{span}\left(\partial_{r}, X_{3}\right):=\ell_{-1}^{\prime},$$
where $X_{i}, i=1 \ldots 3$ respectively denote a usual the dual vectors to $\sigma_{i}$.
Consider now a solution $(a, b, c)$ approaching as $r \rightarrow 0$ the equilibrium point $(q, q, 0)$, with $a=b$. As in $S U(2)$, with our choice of normalization of the Lie algebra basis, we have $\exp \left(4 \pi X_{3}\right)=\mathrm{id}, 2 X_{3}$ generates an $U(1)$-action whose rotational isotropy action on the plane spanned by it and $d / d r$ is by $a_{1} \theta$, and on $\mathfrak{m}$ by $d_{1} \theta$, where the constants $a_{1}$ and $d_{1}$ are determined as follows. First,
$$\begin{aligned}
a_{1} & =\lim _{r \rightarrow 0} \frac{\left|2 X_{3}\right|}{r}=\lim _{r \rightarrow 0} \frac{2 c}{r}=\lim _{r \rightarrow 0} 2 \frac{d c}{d r} \\
& =2 \lim _{r \rightarrow 0}\left(1+e^{-A}-\frac{c^{2}}{2 a^{2}}\right)=2\left(1+e^{-A}-\frac{0}{2 q^{2}}\right)=2\left(1+e^{-A}\right) .
\end{aligned}$$
Since $c^{2}(r)$ is even with no constant term, following [VZ], smooth extendibility requires first of all that $2\left(1+e^{-A}\right)$ is an integer.

Second, as $\left[X_{3}, X_{1}\right]=X_{2}$ and $\left[X_{3}, X_{2}\right]=-X_{1}$, we have $d_{1}=1$. The remaining potentially nontrivial smoothness conditions for the metric in [VZ]
are
$$\begin{aligned}
& a^{2}+b^{2}=\phi_{1}\left(r^{2}\right), \\
& a^{2}-b^{2}=r^{\frac{2 d_{1}}{a_{1}}} \phi_{2}\left(r^{2}\right),
\end{aligned}$$
for some functions $\phi_{1}, \phi_{2}$. The first of these clearly holds as $a=b$ can be extended to an even function. The second is also obvious as $a=b$.

We turn to checking that the Kähler form extends across the singular orbit at $r=0$. For the isotropic action of $S O(2)$ on $T_{p} M$, we find that $\partial_{r}+\frac{i}{r} X_{3}$ is an eigenvector with eigenvalue $e^{i a_{1} \theta}$, and $X_{1}+i X_{2}$ is an eigenvector with eigenvalue $e^{i d_{1} \theta}$, and likewise for their complex conjugates. Dualizing gives eigenspaces of $T_{p}^{*} M: d r-i r \sigma_{3}$ has eigenvalue $e^{i a_{1} \theta}$, and $\sigma_{1}-i \sigma_{2}$ has eigenvalue $e^{i d_{1} \theta}$. Thus the eigenspaces of $\Lambda^{2} T_{p}^{*} M$ are
$$\begin{aligned}
E_{1} & =\operatorname{span}\left\{r d r \wedge \sigma_{3}, \sigma_{1} \wedge \sigma_{2}\right\} \\
E_{e^{i\left(a_{1}+d_{1}\right) \theta}} & =\operatorname{span}\left\{d r \wedge \sigma_{1}-r \sigma_{3} \wedge \sigma_{2}+i\left(-d r \wedge \sigma_{2}-r \sigma_{3} \wedge \sigma_{1}\right)\right\} \\
E_{e^{i\left(a_{1}-d_{1}\right) \theta}} & =\operatorname{span}\left\{d r \wedge \sigma_{1}+r \sigma_{3} \wedge \sigma_{2}+i\left(d r \wedge \sigma_{2}-r \sigma_{3} \wedge \sigma_{1}\right)\right\}
\end{aligned}$$
The smoothness condition is the equivariance condition $\omega\left(e^{a_{1} \theta} p\right)=\exp \left(\theta X_{3}\right)^{*} \omega$. This requires that the coefficient of
$$\begin{gathered}
E_{1} \text { is } \phi_{1}\left(r^{2}\right), \\
E_{e^{ \pm i\left(a_{1}-d_{1}\right) \theta}} \text { is } r^{\frac{\left|a_{1}-d_{1}\right|}{a_{1}}} \phi_{2}\left(r^{2}\right), \\
E_{e^{ \pm i\left(a_{1}+d_{1}\right) \theta}} \text { is } r^{\frac{\left|a_{1}+d_{1}\right|}{a_{1}}} \phi_{3}\left(r^{2}\right) .
\end{gathered}$$
Now we have
$$\begin{aligned}
\omega & =c d r \wedge \sigma_{3}+a b \sigma_{1} \wedge \sigma_{2} \\
& =\frac{c}{r} \cdot r d r \wedge \sigma_{3}+a^{2} \sigma_{1} \wedge \sigma_{2} .
\end{aligned}$$
Thus our only nonzero coefficients are in $E_{1}$. Thus the smoothness conditions become
$$\begin{aligned}
\frac{c}{r} & =\phi_{1}\left(r^{2}\right), \\
a^{2} & =\phi_{2}\left(r^{2}\right) .
\end{aligned}$$
Both of these hold trivially from the even/odd extendibility of $a, c$. Thus in total, the Kähler form extends smoothly across the singular orbit if and only $2 e^{-A}$ is an integer.
6.5.3. The endpoint $\eta$. Next, we consider the question of completeness as $t \rightarrow \eta$.

Recalling here that in this case that $a \equiv b$, the system reduces to
$$\begin{aligned}
a^{\prime} & =\frac{a}{2} c^{2} \\
c^{\prime} & =\frac{c}{2}\left(2\left(1+e^{-A}\right) a^{2}-c^{2}\right) .
\end{aligned}$$

Following [DS1], one can write the equations using the variables $w_{1}=b c$, $w_{2}=a c, w_{3}=a b$. In the case at hand $w_{1}=w_{2}$, and the above two equations are then equivalent to the system
$$\begin{aligned}
w_{1}^{\prime} & =\left(1+e^{-A}\right) w_{1} w_{3}, \\
w_{3}^{\prime} & =w_{1}^{2},
\end{aligned}$$
with the metric given in terms of $w_{1}$ and $w_{3}$ as
$$g=w_{1}^{2} w_{3} d t^{2}+w_{3} \sigma_{1}^{2}+w_{3} \sigma_{2}^{2}+\frac{w_{1}^{2}}{w_{3}} \sigma_{3}^{2} .$$
A curve $\gamma:\left[t_{0}, \eta\right) \rightarrow M$ which is constant in the orbit direction has length
$$l(\gamma)=\int_{t_{0}}^{\eta} w_{1} \sqrt{w_{3}} d t$$
In order to determine the behavior of $w_{1}$ and $w_{3}$ as $t \rightarrow \eta$, first eliminate $w_{1}$ to reduce to an equation in $w_{3}$ alone, which integrated once gives
$$w_{3}^{\prime}(t)=\left(1+e^{-A}\right) w_{3}^{2}(t)+\delta,$$
where $\delta$ is a constant of integration.
Lemma 6.4. $\eta$ is finite.
Proof. First observe that $w_{1}^{\prime}, w_{3}^{\prime}, w_{3}^{\prime \prime}>0$. Next, we see that $w_{1}$ and $w_{3}$ become unbounded as $t \rightarrow \eta$, whether $\eta$ is finite or not. If $\eta=\infty$, then since $w_{3}^{\prime}$ and $w_{3}^{\prime \prime}$ are both positive, $w_{3}$ must become unbounded; since $w_{3}^{\prime}=w_{1}^{2}$, then $w_{1} \rightarrow \infty$ also. If $\eta<\infty$, then at least one of $w_{1}, w_{3}$ becomes unbounded, because otherwise the maximality of the interval of existence would be contradicted. From the equations, if one becomes unbounded, so does the other.

A comparison argument now shows that in fact $\eta<\infty$. Since $w_{3} \rightarrow \infty$ as $t \rightarrow \eta$, there exists an $M$ so that for all $t \in(M, \eta)$,
$$\left(1+e^{-A}\right) w_{3}^{2}(t)+\delta>w_{3}^{2}(t) .$$
Choose $t_{1} \in(M, \eta)$, and consider the comparison equation
$$w^{\prime}=w^{2},$$
with initial value $\left(t_{1}, w_{3}\left(t_{1}\right)\right)$. The actual solution $w_{3}$ passes through the point $\left(t_{1}, w_{3}\left(t_{1}\right)\right)$ and has a steeper derivative at every point, so $w_{3}$ lies above the comparison function $w$. The comparison function becomes unbounded at a finite value $\eta_{c}$; its solution is $w=1 /\left(\eta_{c}-t\right)$. Therefore, $w_{3}$ also diverges to $\infty$ at some $\eta \leq \eta_{c}<\infty$. \(\square\)

Since $w_{3} \rightarrow \infty$ as $t \rightarrow \eta$, a multiple of that same comparison function also serves in the asymptotic sense:
$$\lim _{t \rightarrow \eta} \frac{\left(1+e^{-A}\right) w_{3}^{2}(t)+\delta}{\left(1+e^{-A}\right) w_{3}^{2}(t)}=1 .$$
The behavior of $w_{3}$ can be discerned from that of $w$, the solution to $w^{\prime}=$ $\left(1+e^{-A}\right) w^{2}$. This solution is a multiple of $1 /(\eta-t)$. Using the equation $w_{3}^{\prime}=w_{1}^{2}$, we see that
$$\int_{t_{1}}^{\eta} w_{1} \sqrt{w_{3}} d t=\infty,$$
since the integrand is asymptotically $(t-\eta)^{-3 / 2}$. Thus the metric is complete.
6.6. Equilibrium (0, 0, 0).
6.6.1. Reduction to an explicit solution. The case of equilibrium (0, 0, 0) contains many of the ideas already introduced, so we will be brief. First, in order to find the rates of convergence of $a, b, c$ as $t \rightarrow-\infty$, convert the system (38) from the variable $t$ to the variable $r=\int_{-\infty}^{t} a b c d s$. Solutions approaching this equilibrium have that $a, b, c$ can be extended smoothly as odd functions of $r$. Writing odd power series expansions of $a, b, c$ in $r$ and solving for the first order coefficients $\hat{a}, \hat{b}, \hat{c}$ respectively, yields positive solutions $\hat{a}=\hat{b}=\sqrt{\gamma} / 2, \hat{c}=\gamma / 2$ for $\gamma:=1+e^{-A}$. Hence $a / b$ tends to 1 as $r \searrow 0$ (or $t \rightarrow-\infty$ ), and as before we must have $a \equiv b$.

Thus in this case the ODE system again becomes (43) and equation (44) also holds. Now since $w_{3}^{\prime}=w_{1}^{2}, w_{3}$ is an increasing function converging to 0 as $t \rightarrow-\infty$. Therefore $w_{3}^{\prime}$ converges to 0 as $t \rightarrow-\infty$ and thus $w_{3}^{\prime}-\gamma w_{3}^{2} \rightarrow$ $0-\gamma 0=0$, so that we have $\delta=0$. The ODE system thus simplifies and its solution is just a case of the one used as comparison in the previous subsection, specifically $a(t)=\sqrt{\frac{1}{-\gamma t}}, c(t)=\sqrt{\frac{1}{-t}}$.
6.6.2. No smooth extension to a singular orbit. The distance to the endpoint $t=-\infty$ in this explicit metric is finite. Hence one needs to investigate whether the metric and Kähler form can be extended smoothly to a singular orbit. The singular orbit in this case is just a point, i.e. a "nut". But in the $r$ coordinate one easily sees that $a(r)=\sqrt{\gamma} r / 2, c(r)=\gamma r / 2$, and since we cannot have both $a^{\prime}(0)=1$ and $c^{\prime}(0)=1$ simultaneously, the metric is not complete. This can alternatively be deduced from the statement of the smoothness condition in [VZ] for the case where the isotropy subgroups of a singular fiber is $S p(1)$ and generic isotropy subgroup is trivial.
6.7. Equilibrium $(\mathbf{q}, \mathbf{0}, \mathbf{q}), \mathbf{q}>\mathbf{0}$. Suppose now that the initial value is chosen to lie on an unstable curve of $(q, 0, q)$, with $q>0$.

For large, negative values of $t$, the functions $a$ and $c$ can be approximated by $q$; to discover the rate of vanishing of $b$, we examine the equation
$$b^{\prime}=q^{2} b .$$

This is easily solved to obtain $b(t)=k e^{q^{2} t}$. After a change of variables $v(t)=$ $k e^{q^{2} t}$ (the same as in [DS]), the metric is approximated by
$$g=d v^{2}+q^{2} \sigma_{1}^{2}+v^{2} \sigma_{2}^{2}+q^{2} \sigma_{3}^{2},$$
with $t \rightarrow-\infty$ if and only if $v \rightarrow 0$. This metric is incomplete. However, in this case we cannot extend the metric smoothly to a singular orbit. Namely, upon switching to the coordinate $r$, so that the metric has the form $d r^{2}+h_{r}$, in the resulting ODE system $c$ can be extended only as an odd function near $r=0$ (whereas $a$ and $b$ can be extended either both as even, or both as odd functions). But an odd function can't have a nonzero value $q$ at $r=0$. Therefore the corresponding metric is necessarily incomplete, and we do not pursue this case further.

Collecting these investigations, we summarize the findings.
Theorem 3. Let $(M, g)$ be a Riemannian 4-manifold admitting a cohomogeneity one $S U(2)$-action by isometries. Then $g$ is a complete diagonal centrally flat Kähler metric precisely when it is of the form (16) with $(a, b, c)$ an unstable solution curve of the system (38) for an equilibrium point $(q, q, 0), q>0$, defined on a maximal interval. Such metrics satisfy $a=b$, and $M$ contains a unique singular orbit.

With regard to the explicitness of these solutions, note that one could have proceeded with the system (42) by making the change of variables as in section 5. This would give a similar explicit solution, where this time
$$\phi(q)=\frac{e^{k}}{2 \gamma} e^{2 \gamma q}+B, \text { with } \gamma=1+e^{-A} \text { and constants } k, B .$$
The case of positive $B$ corresponds to a solution converging to equilibrium $(q, q, 0), q>0$, whereas $B=0$ yields one converging to (0, 0, 0).

\section*{7. Centrally flat metrics under the Euclidean Group of plane motions}

In this section we describe a complete triaxial centrally flat metric with a cohomogeneity one action of the Euclidean group $E(2)$. The method employed is that of the recent [MR1], which in turn was inspired by [DS1].

We set $p_{2}=0, p_{1}=p_{3}=1$, and $\lambda=0$. Then the Lie algebra spanned by $X_{1}, X_{2}, X_{3}$ is the Lie algebra of the Euclidean group. The equations for zero central curvature are, from (23)-(25) and (28)
$$\begin{aligned}
a^{\prime} & =\frac{a}{2}\left(-a^{2}+c^{2}\right), \\
b^{\prime} & =\frac{b}{2}\left(a^{2}+c^{2}\right), \\
c^{\prime} & =\frac{c}{2}\left(a^{2}-c^{2}+2 \alpha\right), \\
\alpha^{\prime} & =\alpha c^{2} .
\end{aligned}$$
These can be reduced to a system of three equations as in section 6, but we will generally stick with the above version.

As in the case of $S U(2)$, the derivatives in this system are given by polynomials in the dependent variables, hence are locally Lipschitz, so that standard ODE theory applies. The symmetries of these equations include, as they are autonomous, constant shifts in $t$. Additionally, the equations possess a scaling symmetry
$$(a(t), b(t), c(t), \alpha(t)) \rightarrow\left(k a\left(k^{2} t\right), b\left(k^{2} t\right), k c\left(k^{2} t\right), k^{2} \alpha\left(k^{2} t\right)\right),$$
taking solutions to solutions.
7.1. Linearization about Equilibria. The equilibrium solutions are $(q, 0, q, 0)$ and $(0, p, 0, r)$, and we concentrate on the nonzero case. Then the system (45)-(48) has linearization about ( $q, 0, q, 0$ ) given by
$$\begin{aligned}
a^{\prime} & =-q^{2} a+q^{2} c, \\
b^{\prime} & =q^{2} b, \\
c^{\prime} & =q^{2} a-q^{2} c+q \alpha, \\
\alpha^{\prime} & =q^{2} \alpha,
\end{aligned}$$
which has one double positive, one negative and one zero eigenvalue for $q>0$. The linearization about $(0, p, 0, r)$ has three zero eigenvalues and one with the sign of $r$.

Theorem 4. A solution of (45)-(48) yields a complete centrally flat metric of the form (16) on a cohomogeneity one $E(2)$ 4-manifold if it is a solution along an unstable curve of an equilibrium point $(q, 0, q, 0), q>0$.

Proof. The proof is broken into three steps. As in the case of $S U(2)$, solutions with a maximal interval having a finite left endpoint do not yield complete metrics. See Proposition 7.2. Solutions with maximal interval $(-\infty, \eta)$ are the unstable curves of the equilibrium points $(q, 0, q, 0)$, and satisfy $0 \leq c^{2}-a^{2} \leq$ $2 \alpha$. Once again for a geodesic orthogonal to the orbits, $\eta$ is infinitely far, while $t=-\infty$ is at a finite distance. See Proposition 7.4. At $t=-\infty$ the metric nd Kähler form extend smoothly (Proposition 7.5). The proof that all finite length curves remain inside some compact set is as in [MR1]. \(\square\)

We first record in a lemma some relations, easily verifiable via (45)-(47), which will be used later in the proof.

Lemma 7.1. For the system (45)-(48),
$$\begin{aligned}
& (a b)^{\prime}=a b c^{2}, \quad(\alpha c)^{\prime}=\frac{\alpha c\left(a^{2}+c^{2}+2 \alpha\right)}{2}, \\
& (b c)^{\prime}=b c\left(a^{2}+\alpha\right), \quad\left(\frac{a}{b}\right)^{\prime}=-\frac{a^{3}}{b}, \\
& (a c)^{\prime}=a c \alpha,
\end{aligned}$$

\subsection*{7.2. Solutions.}

Proposition 7.2. There are no complete metrics corresponding to solutions of (45)-(48) with maximal interval $(\xi, \eta)$, when $\xi$ is finite. Furthermore, the unstable curves of the equilibrium points $(q, 0, q, 0)$ are non-equilibrium solutions with maximal interval $(-\infty, \eta)$ which satisfy $0 \leq c^{2}-a^{2} \leq 2 \alpha$.

Proof. For an initial time $t_{0}$, let $(\xi, \eta)$ be a maximal solution interval for the initial value problem for (45)-(48) with $a\left(t_{0}\right)=a_{0}, b\left(t_{0}\right)=b_{0}, c\left(t_{0}\right)=c_{0}$ and $\alpha\left(t_{0}\right)=\alpha_{0}$.

Uniqueness of solutions to (45)-(48) implies that if any of $a, b, c$ or $\alpha$ are zero anywhere in $(\xi, \eta)$ then they are zero everywhere. Accordingly we assume that $a, b, c$ and $\alpha$ are all positive on $(\xi, \eta)$. Then we see from Lemma 7.1 and (46) that $a b, b c, a c$, and $b$ are all increasing on $(\xi, \eta)$.

We consider the following cases:
Case 1: $c_{0}^{2}-a_{0}^{2}<0$. We first make the following claim.
Claim: In this case $a \rightarrow \infty$ as $t \rightarrow \xi^{+}$.
Proof of claim: Since
$$\left(c^{2}-a^{2}\right)^{\prime}=-\left(c^{2}-a^{2}\right)\left(c^{2}+a^{2}\right)+2 \alpha c^{2},$$
if $c^{2}-a^{2}<0$ then $\left(c^{2}-a^{2}\right)^{\prime}>0$, thus $c^{2}-a^{2}<0$ for all $\xi<t<t_{0}$. Therefore,
$$\begin{aligned}
a^{\prime} & =\frac{a}{2}\left(c^{2}-a^{2}\right), \\
a^{\prime \prime} & =\frac{a}{4}\left[\left(c^{2}-a^{2}\right)^{2}-2\left(c^{2}-a^{2}\right)\left(c^{2}+a^{2}\right)+4 \alpha c^{2}\right],
\end{aligned}$$
showing that $a$ is decreasing and concave up on $\left(\xi, t_{0}\right)$. Next, we always have $b^{\prime}>0$, while on $\left(\xi, t_{0}\right)$
$$c^{\prime}=\frac{c}{2}\left(a^{2}-c^{2}+2 \alpha\right)>0,$$
i.e. $c$ is increasing on $\left(\xi, t_{0}\right)$. Therefore $b$ and $c$ are bounded on $\left(\xi, t_{0}\right)$. Thus, as $(\xi, \eta)$ is the maximal solution interval, $a$ could be bounded as $t \rightarrow \xi^{+}$only if $\xi=-\infty$. But since $a$ is concave up, $a \rightarrow \infty$ as $t \rightarrow \xi^{+}$even when $\xi=-\infty$. \(\square\)

Since $a b$ and $a c$ are increasing, they are bounded as $t \rightarrow \xi^{+}$and $a \rightarrow \infty$, so $b \rightarrow 0, c \rightarrow 0$. Now $\alpha$ is also increasing, so $\alpha \rightarrow k$ for some constant $k$ as $t \rightarrow \xi^{+}$. Then as $t \rightarrow \xi^{+}$the first three equations will take the asymptotic form
$$\begin{aligned}
a^{\prime} & =-\frac{1}{2} a^{3} \\
b^{\prime} & =\frac{1}{2} b a^{2} \\
c^{\prime} & =\frac{1}{2} c\left(a^{2}+2 k\right)
\end{aligned}$$
the solution of which has asymptotic form
$$\begin{aligned}
& a \simeq(t-\xi)^{-\frac{1}{2}}, \\
& b \simeq b_{1}(t-\xi)^{\frac{1}{2}}, \\
& c \simeq c_{1}(t-\xi)^{\frac{1}{2}},
\end{aligned}$$
for some constants $b_{1}$ and $c_{1}$. This shows that $\xi$ is finite in this case and
$$\int_{\xi}^{t_{0}} a b c d t<\infty,$$
so the metric is not complete.
Case 2: $c_{0}^{2}-a_{0}^{2}>2 \alpha_{0}$. Here we have a similar claim.
Claim: In this case $c \rightarrow \infty$ as $t \rightarrow \xi^{+}$.
Proof of claim: Analogous to the previous claim. \(\square\)

Since $a c, b c$ and $\alpha c$ are increasing (see Lemma 7.1), they are bounded as $t \rightarrow \xi^{+}$and $c \rightarrow \infty$, so $a \rightarrow 0, b \rightarrow 0$ and $\alpha \rightarrow 0$. Then as $t \rightarrow \xi^{+}$the equations take the asymptotic form
$$\begin{aligned}
& a^{\prime}=\frac{1}{2} a c^{2} \\
& b^{\prime}=\frac{1}{2} b c^{2} \\
& c^{\prime}=-\frac{1}{2} c^{3}
\end{aligned}$$
which has solution
$$\begin{aligned}
a & \simeq a_{1}(t-\xi)^{\frac{1}{2}} \\
b & \simeq b_{1}(t-\xi)^{\frac{1}{2}} \\
c & \simeq(t-\xi)^{-\frac{1}{2}}
\end{aligned}$$
for some constants $a_{1}$ and $b_{1}$. This shows that $\xi$ is finite in this case and
$$\int_{\xi}^{t_{0}} a b c d t<\infty,$$
so the metric is not complete.
If $c^{2}-a^{2}<0$ or $c^{2}-a^{2}>2 \alpha$ at any time, then a constant shift in $t$ will give one of the previous cases. In both previous cases, $\xi$ is finite, but we know that the unstable curve of the equilibrium points $(q, 0, q, 0)$ must have $\xi=-\infty$. The existence of these curves is guaranteed by the center manifold theorem. Therefore we consider the final case:

Case 3: $0 \leq c^{2}-a^{2} \leq 2 \alpha$ for all $t \in(\xi, \eta)$. Here we have a different claim.
Claim: In this case $\xi=-\infty$.
Proof of claim: In this case $a, b$, and $c$ are all increasing, therefore they are all bounded on $\left(\xi, t_{0}\right)$. Since $(\xi, \eta)$ is the maximal solution interval $\xi=-\infty$. \(\square\)

As $a, b, c$ and $\alpha$ are all increasing, it must be that they all approach finite non-negative limits as $t \rightarrow-\infty$. Thus $(a, b, c, \alpha)$ must approach an equilibrium point. If $(a, b, c, \alpha) \rightarrow(0, p, 0, r)$ with $p>0$, then $a / b \rightarrow 0$ as $t \rightarrow-\infty$, but $a / b$ is decreasing and positive (see Lemma 7.1), so this cannot happen. On the other hand, if $r>0$ and $p=0$, note first that from (45)-(46) it easily follows that $\alpha=k a b$ for some constant $k$ which is positive for a non-equilibrium solution. Then, as $a / \alpha$ approaches 0 as $t \rightarrow-\infty$, so does $1 / b$, but $1 / b$ approaches $\infty$, which is a contradiction.

Therefore, when $t \rightarrow-\infty$ we see that $(a, b, c, \alpha) \rightarrow(q, 0, q, 0)$. \(\square\)

Note that we did not rule out the possibility that $q=0$. However, power series calculations show at least that there are no non-equilibrium trajectories approaching (0, 0, 0, 0) which are analytic, in an appropriate sense, at $t=-\infty$. From now on we will only consider the case $q>0$. The center manifold theorem guarantees that solutions exist and are defined over a maximal interval with left endpoint $-\infty$, while the above proof shows that $a$ and $c$, along with $b$ and $\alpha$ are non-decreasing on this interval.

We will need a one more property of the solutions in Case 3.
Lemma 7.3. In Case 3 above, ab is unbounded from above.
Proof. By (47) and (48)
$$(c)^{\prime}=\frac{c}{2}\left(a^{2}-c^{2}+2 \alpha\right) \leq \frac{c}{2} 2 \alpha=\frac{c}{2} \frac{2 \alpha^{\prime}}{c^{2}}=\frac{2 \alpha^{\prime}}{2 c}$$
so $\left(c^{2}\right)^{\prime} \leq 2 \alpha^{\prime}$ or $\left.c^{2}\right|_{s} ^{t} \leq\left. 2 \alpha\right|_{s} ^{t}$. Taking $s \rightarrow-\infty$ gives
$$2 \alpha \geq c^{2}-q^{2} .$$
Applying this to (47) gives
$$\left(\log c^{2}\right)^{\prime} \geq a^{2}-c^{2}+c^{2}-q^{2}=a^{2}-q^{2} .$$
As one easily checks, as we are always assuming $\alpha$ is not identically zero, there is no non-equilibrium solution with $a=q$ identically. Thus for some $t_{0}$, for any $t>t_{0}, a(t) \geq a\left(t_{0}\right)>q$, so on that domain $\left(\log c^{2}\right)^{\prime}>\epsilon>0$. Thus $c^{2}$ grows faster than exponentially, and hence so does $2 \alpha$ by (49). And $\alpha=k a b, k>0$. This proves the result if $\eta=\infty$. If $\eta$ is finite, one of $a, b, c, \alpha$ is unbounded and they are all increasing, which proves the claim if it is $a$ or $b$ that are unbounded. If it is $c, \alpha$ is also unbounded by (49) again. \(\square\)

Proposition 7.4. Let $g$ be a Riemannian metric of the form (16) on an $E(2)$ -manifold $M$, with $a, b, c$ a solution to (45)-(48) along an unstable curve of an equilibrium point $(q, 0, q, 0), q>0$, having maximal domain $I=(-\infty, \eta)$. Assume that the latter interval is also the range of the coordinate function $t$ on
$M$. For a point $p_{0} \in M$ with orbit through $p_{0}$ of principal type and a level set $M^{t}$ of $t$,
$$\lim _{t \rightarrow-\infty} d_{g}\left(p_{0}, M^{t}\right)<\infty, \quad \lim _{t \rightarrow \eta} d_{g}\left(p_{0}, M^{t}\right)=\infty,$$
where $d_{g}$ is the distance function induced by $g$.
Proof. As in [MR1] we note that the level sets of $t$ are orbits of $\mathcal{G}$ and for $t_{0}=t\left(p_{0}\right)$
$$d_{g}\left(p_{0}, M^{t_{1}}\right)=d_{g}\left(M^{t_{0}}, M^{t_{1}}\right),$$
measures the distance in the quotient manifold $\tilde{M} / \mathcal{G}$, where
$$d_{g}\left(M^{t_{0}}, M^{t_{1}}\right)=\left|\int_{t_{0}}^{t_{1}} a b c d t\right|,$$
and the metric is $(a b c)^{2} d t^{2}$.
We omit the proof that $\lim _{t \rightarrow-\infty} d_{g}\left(p_{0}, M^{t}\right)<\infty$ as it is identical to that in [MR1], and also similar to the case of $S U(2)$. To understand the behavior at the $\eta$ side of the solution interval, we adopt the change of variable $r=2(a b)^{1 / 2}$ first appearing in [PP] and [DS1], which is allowable as $a b$ is strictly increasing (Lemma 7.1). $r \rightarrow \infty$ as $t \rightarrow \eta$ since otherwise $a b$ is bounded, contradicting Lemma 7.3. Using Lemma 7.1, the metric after this change takes the form
$$g=W^{-1} d r^{2}+\frac{r^{2}}{4}\left(V \sigma_{1}^{2}+V^{-1} \sigma_{2}^{2}+W \sigma_{3}^{2}\right)$$
with $W=c^{2} /(a b)$ and $V=a / b$. Additionally,
$$\begin{aligned}
\frac{d W}{d r}=W^{\prime} / r^{\prime} & =\left(\frac{c^{2}}{a b}\right)^{\prime}(a b)^{-1 / 2} c^{-2} \\
& =-\frac{4}{r} W+\frac{2}{r} \frac{a}{b}+16 \frac{\alpha}{r^{3}} .
\end{aligned}$$
Now $a / b$ decreases to a finite nonnegative limit $L$ as $r \rightarrow \infty$, so that asymptotically
$$\frac{d W}{d r}=-\frac{4}{r} W+\frac{2}{r} L+16 \frac{\alpha}{r^{3}},$$
an equation which, using the aforementioned relation $\alpha=k a b=k \frac{r^{2}}{4}, k>0$ constant, has solution
$$W=L / 2+k+\frac{p}{r^{4}}$$
for an integration constant $p$. The metric then has the asymptotic form (51) for $W$ as above and $V=L$. If $L=0$ this asymptotic form is degenerate, but nonetheless one can still use its $d r^{2}$ component to compute the distance to $M_{r}:=M_{t(r)}$. Thus the integral of $W^{-1 / 2}$ in this asymptotic form shows that
$$\lim _{r \rightarrow \infty} d_{g}\left(p_{0}, M_{r}\right)=\infty .$$
This completes the proof. \(\square\)
7.3. Smooth extension to a singular orbit. For the case at hand, the cohomogeneity one 4-manifold with one singular orbit attached can be described as
$$E(2) \times_{S O(2)} \mathbb{R}^{2}=(0, \infty) \times E(2) \amalg\{0\} \times \mathbb{R}^{2},$$
where the right $S O(2)$-action is $(g,(T, x)) \rightarrow\left(T g, g^{-1} x\right)$.
Proposition 7.5. The metric and Kähler form corresponding to solutions of (45)-(48) along the unstable curves of the equilibrium points $(q, 0, q, 0), q>0$, defined on $(-\infty, \eta)$, can be smoothly extended to $M=E(2) \times_{S O(2)} \mathbb{R}^{2}$, with the two-dimensional singular orbit $E(2) / S O(2)$ defined over $\xi=-\infty$.