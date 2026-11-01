---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 2003_03234.pdf
converter: mathpix
format: mmd
---

\title{
One-sided type-D Ricci-flat metrics
}

\author{
Paul Tod* \\ Mathematical Institute, Oxford University
}

October 28, 2021

\begin{abstract}
We consider four-dimensional, Riemannian, Ricci-flat metrics for which one or other of the self-dual or anti-self-dual Weyl tensors is type-D. Such metrics always have a valence-2 Killing spinor, and therefore a Hermitian structure and at least one Killing vector. We rederive the results of Przanowski and collaborators, that these metrics can all be given in terms of a solution of the $S U(\infty)$-Toda field equation, and show that, when there is a second Killing vector commuting with the first, the method of Ward can be applied to show that the metrics can also be given in terms of an axisymmetric solution of the flat three-dimensional Laplacian. Thus in particular the field equations linearise.

As a corollary, we show that the same technique linearises the field equations for a four-dimensional Einstein metric with anti-self-dual Weyl tensor and two commuting symmetries.

We reduce the Einstein equations with non-zero scalar curvature and one-sided type-D Weyl tensor, excluding the Kähler-Einstein case, to a modified but not integrable Toda equation.
\end{abstract}

Some examples of the constructions are given.

\section*{1 Introduction}

In this note we consider four-dimensional, Riemannian, Ricci-flat metrics for which one or other of the self-dual or anti-self-dual Weyl tensors is type-D in the Petrov-Pirani-Penrose classification (for which see e.g. [9]). We'll call these metrics one-sided type- D, a term in use at least since 1984 (see [13]). Our motivation comes indirectly from the Chen-Teo metric [4]. This has two commuting Killing vectors and is Riemannian and Ricci-flat and was obtained by inverse-scattering methods, which are available since the Einstein equations in this case are known to be completely integrable, (see e.g. [3]). It was discovered by Aksteiner [2] that the Chen-Teo metric is one-sided type-D, and therefore, as we shall see,

\footnotetext{
*email: tod@maths.ox.ac.uk
}

Hermitian. In this note we ask: can one do more with it, in the light of the general solution of one-sided type-D vacuum metrics in [13, 14]?

In [13, 14] the Einstein vacuum equations, subject to these restrictions, are reduced to the $S U(\infty)$-Toda equation (we'll omit the term " $S U(\infty)$ " henceforth). It's known that the Toda equation linearises if the solution has an extra symmetry, [18], which suggests that the field equations for one-sided type-D Ricci-flat metrics with a second symmetry commuting with the first linearise, and we shall see here that they do.

Our method is to start in Section 2 with the assumption of a 4-dimensional Riemannian, Ricci-flat metric which is one-sided type-D, or equivalently (as we show) is Hermitian. Then we use the two-component spinor formalism to rederive the expressions of [14] for the metric in terms of a solution $u$ of the Toda field equation (18). The metric automatically has a Killing vector which arises from a valence- 2 Killing spinor, which in turn is a consequence of the type-D-ness (by [10]), and our rederivation serves to explain the occurence of this Killing vector. Then in Section 3 we add the assumption that there is a second Killing vector and deduce that, after possible redefinitions of coordinates and $u$ preserving the Toda field equation, the second Killing vector must be a symmetry of $u$ corresponding to an ignorable coordinate which can be taken to be $y$ in (18). Then in Section 4 we exploit the observation in [18] that solutions of the Toda field equation independent of $y$ correspond to axisymmetric solutions of the flat 3-dimensional Laplacian. We arrive at our main result: that Riemannian, Ricci-flat, one-sided type-D 4-metrics with two commuting Killing vectors are in one-to-one correspondence with axisymmetric solutions of the flat three-dimensional Laplacian. The field equations, known to be completely integrable in this case, in fact linearise. We also give a corollary: by [11] (see also [15], [17]) the general ASD Einstein metric with a symmetry and non-zero Ricci scalar can be found in terms of a solution of the Toda field equation; consequently if there is a second Killing vector commuting with the first then again by [18] the solution can be given in terms of a solution of the axisymmetric Laplace equation - in this case too the Einstein equations linearise. In Section 5 we show that the field equations for one-sided type-D Einstein metrics reduce to a modified Toda field equation which is not integrable ([6]), in Section 6 we deal with a puzzling feature of the constructions, and in Section 7 we give some examples of all the reductions.

Acknowledgements: I am grateful to Dr Steffen Aksteiner of the AEI, Golm, for discussions about the Chen-Teo metric, and for telling me that it was one-sided type-D, and to the Institut Mittag-Leffler in Djursholm, Sweden for hospitality as part of the programme 'General Relativity, Geometry and Analysis' during September 2019, supported by the Swedish Research Council under grant no. 2016-06596. I am grateful to Dr Maciej Dunajski of DAMTP Cambridge for references [11, 12, 13, 14] and useful discussions, in the course of which we realised that the construction given here must be possible, and I am grateful to Profs Jenya Ferapontov and Boris Kruglikov for information about integrability of the modified Toda equation (40).

\section*{2 One-sided type-D}

In this section, we rederive the results of [14] in the style of [15, 17]. The virtue of this rederivation is that one sees how it follows from the algebraic assumption on the Weyl spinor, and one also sees the origin of the first Killing vector in this assumption. For background on the 2-component spinor formalism see [8] or [9].

Start then with a Riemannian, Ricci-flat and one-sided type-D metric. The unprimed Weyl spinor (as a matter of convenience, call this the SD Weyl spinor - it would more properly be the ASD Weyl spinor but this makes very little difference for us) can be taken to be
$$\psi_{A B C D}=\psi o_{(A} o_{B} o_{C}^{\dagger} o_{D)}^{\dagger}$$
with real $\psi=6 \Psi_{2}$ in NP conventions, and the spinor normalisation
$$o_{A} o^{\dagger A}=1 .$$
We'll assume the metric is non-trivially type-D, in the sense that the SD Weyl spinor is not zero, so that $\psi$ is not the zero function. The argument of [10] still goes through to show that the spinor field $\omega_{A B}$ defined as
$$\omega_{A B}=i \psi^{-1 / 3} o_{(A} o_{B)}^{\dagger}$$
is a (real) Killing spinor, or equivalently
$$\nabla_{A^{\prime}(A} \omega_{B C)}=0 .$$
Therefore
$$\nabla_{A^{\prime} A} \omega_{B C}=\epsilon_{A(B} K_{C) A^{\prime}}$$
for some real vector $K_{A A^{\prime}}$, which is then necessarily a Killing vector. To see this necessity, calculate commutators as follows (conventions following [9]): by Ricci-flat-ness
$$0=\Delta_{A^{\prime} B^{\prime}} \omega^{C D}=\nabla_{\left(A^{\prime}\right.}^{(C)} K_{\left.B^{\prime}\right)}^{D)},$$
and with zero Ricci scalar
$$\Delta_{A B} \omega_{C D}=\psi_{E A B C} \omega_{D}^{E}+\psi_{E A B D} \omega_{C}^{E},$$
whence
$$\psi_{E(A B C} \omega_{D)}^{E}=0,$$
as we know (this follows from (1), (2)), and the trace of (5) on $B C$ gives
$$\nabla_{A A^{\prime}} K_{D}{ }^{A^{\prime}}=\psi_{A B D E} \omega^{B E}=-\frac{1}{3} \psi \omega_{A D} .$$

From the trace of this we deduce $\nabla_{a} K^{a}=0$, so with (4) we see that $K^{a}$ is a Killing vector, as claimed, and furthermore we may write
$$\nabla_{A A^{\prime}} K_{B B^{\prime}}=-\frac{1}{6} \psi \omega_{A B} \epsilon_{A^{\prime} B^{\prime}}+\chi_{A^{\prime} B^{\prime}} \epsilon_{A B},$$
for symmetric $\chi_{A^{\prime} B^{\prime}}$ (which we use in Section 6). The identity
$$\nabla_{a} \nabla_{b} K_{c}=R_{b c a d} K^{d},$$
which holds for any Killing vector, now gives
$$\nabla_{A A^{\prime}}\left(-\frac{1}{6} \psi \omega_{B C}\right)=-\psi_{A B C D} K_{A^{\prime}}^{D},$$
which is equivalent to
$$\omega_{A C} K_{A^{\prime}}^{C}=-\frac{1}{6} \psi^{-5 / 3} \nabla_{a} \psi,$$
and which also follows by contracting (3) with $\omega^{B C}$, so this is an identity, and
$$\nabla_{A A^{\prime}} \chi_{B^{\prime} C^{\prime}}=-\psi_{A^{\prime} B^{\prime} C^{\prime} D^{\prime}} K_{A}{ }^{D^{\prime}} .$$
We find, introducing $\phi_{A B}$ as
$$\phi_{A B}=2 i o_{(A} o_{B)}^{\dagger}=2 \psi^{1 / 3} \omega_{A B},$$
that there is an almost complex structure determined by
$$J_{a}^{b}:=\phi_{A}^{B} \delta_{A^{\prime}}^{B^{\prime}},$$
which is then easily seen to be integrable - thus the metric is Hermitian by virtue of being type-D and Ricci-flat. Conversely, if there is an integrable complex structure of the form of (10) (i.e. with this duality) then necessarily $o^{A}$ is geodesic and shear-free and therefore, by the Goldberg-Sachs Theorem (see e.g. [9]), is a repeated PND of the Weyl spinor. Then $o^{\dagger A}$ is another and so the Weyl spinor is type-D. Therefore the properties of being Hermitian and being one-sided type-D are here equivalent.

With (9) we obtain
$$\phi_{A B} K_{A^{\prime}}^{B}=2 \psi^{1 / 3} \omega_{A B} K_{A^{\prime}}^{B}=\nabla_{a}\left(\psi^{-1 / 3}\right) .$$
(By a general argument, this must be a gradient as it defines the Hamiltonian for $K$ ).
We can proceed to find a metric ansatz as follows: set $W^{-1}:=K^{b} K_{b}$ and start an orthonormal basis of one-forms with
$$\theta^{0}=W^{1 / 2} K=W^{-1 / 2}(d t+\omega),$$
where $K^{a} \partial_{a}=\partial_{t}$ and we've introduced a presently unknown one form $\omega$. Introduce $\theta^{1}$ as
$$\theta^{1}=J \theta^{0}=W^{1 / 2} J K=W^{1 / 2} \phi_{A}^{B} K_{B A^{\prime}}=-W^{1 / 2} d\left(\psi^{-1 / 3}\right),$$
using (11), and so $\theta^{1}=W^{1 / 2} d z$ with $z=-\psi^{-1 / 3}$. Next we can choose $\theta^{2}, \theta^{3}$ orthogonal to $\theta^{0}, \theta^{1}$ and such that $J \theta^{2}=\theta^{3}$. There will be a complex coordinate $\zeta$ such that
$$\theta^{2}+i \theta^{3}=W^{1 / 2} e^{u / 2} d \zeta,$$
for some real $u$, and the metric is
$$g=W^{-1}(d t+\omega)^{2}+W\left(d z^{2}+e^{u} d \zeta d \bar{\zeta}\right),$$
in terms of functions $u, W$ and the one-form $\omega$, all to be determined.
We haven't exhausted the information in integrability of the complex structure. The holomorphic one-forms are
$$e^{1}:=\theta^{0}+i \theta^{1}=W^{-1 / 2}(d t+\omega)+i W^{1 / 2} d z, \quad e^{2}=\theta^{2}+i \theta^{3}=W^{1 / 2} e^{u / 2} d \zeta,$$
and at once
$$e^{1} \wedge e^{2} \wedge d e^{2}=0,$$
but the vanishing of $e^{1} \wedge e^{2} \wedge d e^{1}$ leads to
$$d \zeta \wedge(d \omega-i d z \wedge d W)=0$$
which we leave for the moment (this will be part of the 'monopole' equation).
From (6) we have, written as forms
$$d K=-\frac{1}{6} \psi^{2 / 3} J+\mathrm{ASD} \text { terms },$$
with $J$ the complex structure as a 2-form:
$$J=2\left(\theta^{0} \wedge \theta^{1}+\theta^{2} \wedge \theta^{3}\right) .$$
However, with
$$d \omega=\alpha d y \wedge d z+\beta d z \wedge d x+\gamma d x \wedge d y,$$
we obtain
$$\begin{gathered}
d K=d\left(W^{-1}(d t+\omega)\right)=(d t+\omega) \wedge W^{-2} d W+W^{-1} d \omega \\
=c_{1} z^{-2}\left(\theta^{0} \wedge \theta^{1}+\theta^{2} \wedge \theta^{3}\right)+f_{1}\left(\theta^{0} \wedge \theta^{1}-\theta^{2} \wedge \theta^{3}\right)+f_{2}\left(\theta^{0} \wedge \theta^{2}-\theta^{3} \wedge \theta^{1}\right)+f_{3}\left(\theta^{0} \wedge \theta^{3}-\theta^{1} \wedge \theta^{2}\right)
\end{gathered}$$
where the $f_{i}$ are the coefficients of the ASD terms in (14). From this we read off
$$\alpha=-W_{x}, \beta=-W_{y}, \gamma=-e^{u}\left(W_{z}-2 c_{1} \frac{W^{2}}{z^{2}}\right),$$
and $c_{1}$ is a constant fixed by earlier choices (in fact $c_{1}=-1 / 3$ but it is convenient to leave it in the formulae). Note (13) is a consequence of these, but there is a stronger integrability condition to check for (15), namely
$$0=d^{2} \omega=\left(\alpha_{x}+\beta_{y}+\gamma_{z}\right) d x \wedge d y \wedge d z .$$
We'll come back to this when we have an expression for $W$.
We next calculate the SD curvature with this choice for $d \omega$ by Cartan calculus based on a normalised triad of SD 2-forms: with an orthonormal basis of one-forms chosen as
$$\theta^{0}=W^{-1 / 2}(d t+\omega), \theta^{1}=W^{1 / 2} d z, \theta^{2}=W^{1 / 2} e^{u / 2} d x, \theta^{3}=W^{1 / 2} e^{u / 2} d y$$
define an orthonormal basis of SD 2-forms as
$$\phi^{1}=\theta^{0} \wedge \theta^{1}+\theta^{2} \wedge \theta^{3}, \phi^{2}=\theta^{0} \wedge \theta^{2}+\theta^{3} \wedge \theta^{1}, \phi^{3}=\theta^{0} \wedge \theta^{3}+\theta^{1} \wedge \theta^{2},$$
solve
$$d \phi^{i}=-\alpha^{i}{ }_{j} \wedge \phi^{j}$$
for $\alpha^{i}{ }_{j}$ to find
$$\alpha_{2}^{1}=C \theta^{2}, \alpha_{1}^{3}=-C \theta^{3}, \alpha_{3}^{2}=E \theta^{0}+G \theta^{2}+H \theta^{3},$$
with
$$E=-c_{1} z^{-2} W^{1 / 2}, G=\frac{1}{2} W^{-1 / 2} e^{-u / 2} u_{y}, H=-\frac{1}{2} W^{-1 / 2} e^{-u / 2} u_{x}$$
and
$$C=-\frac{1}{2} W^{-1 / 2} u_{z}-c_{1} z^{-2} W^{1 / 2}$$
Now obtain the curvature components subject to Ricci flatness from
$$\Omega_{j}^{i}=d \alpha_{j}^{i}+\alpha_{k}^{i} \wedge \alpha_{j}^{k}=\Omega_{j \cdot k}^{i} \phi^{k},$$
with $\epsilon^{i j k} \Omega_{i j \cdot k}=0$ (which encodes vanishing Ricci scalar; these indices are raised and lowered by $\delta_{i j}, \delta^{i j}$ ), to find from $\Omega_{2}^{1}+i \Omega^{1}$ that necessarily
$$W=-\frac{z^{2} u_{z}}{2 c_{1}}+f(z),$$
with
$$f^{\prime}-2 \frac{f}{z}+c_{1} \frac{f^{2}}{z^{2}}=0$$
so that
$$f=\frac{z^{2}}{c_{1} z+c_{2}},$$
for a constant $c_{2}$. Then from $\Omega_{3}^{2}$ we find that $u$ satisfies the Toda field equation:
$$u_{x x}+u_{y y}+\left(e^{u}\right)_{z z}=0$$
and $c_{1} f=z$ so that $c_{2}=0$ and
$$W=\frac{1}{c_{1}} z\left(1-\frac{1}{2} z u_{z}\right) .$$
Now we can check the integrability condition (17). In fact $G=W / z$ satisfies a familiar monopole equation:
$$G_{x x}+G_{y y}+\left(e^{u} G\right)_{z z}=0 .$$
The SD curvature components are now
$$\Omega_{2}^{1}=c_{1} z^{-3} \phi^{3}, \Omega_{1}^{3}=c_{1} z^{-3} \phi^{2}, \Omega_{3}^{2}=-2 c_{1} z^{-3} \phi^{1},$$
which is recognisably type-D, as expected (in this setting, type-D is the condition that the SD Weyl tensor, which is here represented by the real trace-free symmetric matrix $E_{i j}:=\epsilon_{i}{ }^{m n} \Omega_{m n \cdot j}$, should be degenerate, in having a repeated eigen-value).

We have recovered the expressions in [13] as deductions from the assumption of Riemannian, Ricci-flat and either Hermitian or one-sided type-D, and we see why there is always a Killing vector preserving the complex structure.

Note that
\begin{itemize}
\item[-] The holomorphic one-forms are now
$$e^{1}=W^{-1 / 2}(d t+\omega)+i W^{1 / 2} d z, \quad e^{2}=W^{1 / 2} e^{u / 2}(d x+i d y) .$$
\item[-] We can always set $c_{1}=1$ by a constant rescaling of the metric and redefinition of some coordinates, and this is the value arrived at in [14]: we've recovered their expressions exactly.
\item[-] The 2-form $z^{-2} \phi^{1}$ is closed: this is the rescaling that makes the metric Kähler (for the fact that there must be one, see e.g. [5]).
\end{itemize}

\section*{3 A second Killing vector}

Suppose there is a second Killing vector, then we may write it as
$$L=A \partial_{t}+B \partial_{x}+C \partial_{y}+D \partial_{z},$$
(with $C$ not as in the previous section). We start by showing it must have a restricted form, which then allows the Toda field equation to be linearised.

Write L for the Lie derivative along $L$, and assume $L$ commutes with $K=\partial_{t}$ so that
$$\mathrm{L}(K)=0,$$
which forces $A, B, C, D$ to be independent of $t$. Also
$$0=\mathrm{L}(g(K, K))=\mathrm{L}\left(W^{-1}\right) \text { so that } \mathrm{L}(W)=0 .$$
The curvature is constant along $L$ so that $\mathrm{L} \psi_{A B C D}$ is zero, therefore $\mathrm{L} \psi=0$ (with $\psi$ the scalar in (1)) and then by the previous section $\mathrm{L} z=0$ and so $D=0$. Also the Lie derivative of $\phi_{A B}$ must be zero (since $-4 \psi_{A B C D}=\psi \phi_{(A B} \phi_{C D)}$ ), and so the complex structure is preserved. From the vanishing of $\mathrm{L}(W)$ we now deduce
$$\mathrm{L}\left(u_{z}\right)=0 .$$

Since $K, W$ and $J$ are preserved by $L$, we deduce
$$\mathcal{L}_{L}\left(e^{1}\right)=0,$$
when, by raising the index, we'll also have
$$0=\mathrm{L}\left(W^{1 / 2} \partial_{t}+i W^{-1 / 2} \partial_{z}\right)=i W^{-1 / 2} \mathrm{~L}\left(\partial_{z}\right),$$
so that $\mathrm{L}\left(\partial_{z}\right)=0$ and $A, B, C$ are independent of $z$.
What can we say about $\mathcal{L}_{L}\left(e^{2}\right)$ ? The complex structure is preserved so
$$\mathcal{L}_{L}\left(e^{2}\right)=\alpha e^{1}+\beta e^{2}$$
for some $\alpha, \beta$. Already
$$\mathcal{L}_{L}\left(e^{1}\right)=0 \text { so also } \mathcal{L}_{L}\left(\bar{e}^{1}\right)=0$$
and
$$\mathcal{L}_{L}\left(g\left(\bar{e}^{1}, e^{2}\right)\right)=0 \text { whence } g\left(\bar{e}^{1}, \mathcal{L}_{L}\left(e^{2}\right)\right)=0 \text {, }$$
so $\alpha=0$, and by considering $\mathcal{L}_{L}\left(g\left(\bar{e}^{2}, e^{2}\right)\right)$ we find $\beta$ pure imaginary: $L$ rotates the o.n. basis in the $\left(\theta^{2}, \theta^{3}\right)$-plane.

From (12) we have the freedom
$$t \rightarrow t+f(x, y), \omega \rightarrow \omega-d f,$$
and under this
$$L=A \partial_{t}+B \partial_{x}+C \partial_{y} \rightarrow A \partial_{t}+B\left(\partial_{x}+f_{x} \partial_{t}\right)+C\left(\partial_{y}+f_{y} \partial_{t}\right),$$
and in particular
$$A \rightarrow A+B f_{x}+C f_{y},$$
which we can exploit to set $A=0$. From
$$0=\mathrm{L}(K)=\mathrm{L}\left(W^{-1}(d t+\omega)\right) \text { we deduce } \mathrm{L}(\omega)=0 .$$
Now all that remains of the Killing equation for $L$ is
$$\mathrm{L}\left(e^{u}\left(d x^{2}+d y^{2}\right)\right)=0,$$
i.e. $L=B(x, y) \partial_{x}+C(x, y) \partial_{y}$ is a Killing vector of the 2-metric $h=e^{u}\left(d x^{2}+d y^{2}\right)$. We consider this problem in a subsection.

\subsection*{3.1 Solving (22) for $L$}

We are considering the 2-metric
$$h:=e^{u}\left(d x^{2}+d y^{2}\right),$$
with $u(x, y, z)$ which for our problem we can assume analytic (as solutions of the Toda equation must be). We perform the following calculation at a fixed but arbitrary $z$, which we can take to be $z=0$. First calculate the Ricci scalar of $h$ :
$$R=-e^{-u}\left(u_{x x}+u_{y y}\right) .$$
We are requiring the existence of a Killing vector
$$L=B(x, y) \partial_{x}+C(x, y) \partial_{y},$$
which must preserve $R$ and so must be orthogonal to $d R$, so for some $\Omega(x, y)$ we have
$$B=-\Omega R_{y}, \quad C=\Omega R_{x} .$$
The Killing equations are
$$0=\mathcal{L}_{L} h_{a b}=L^{c} \partial_{c} h_{a b}+h_{a c} \partial_{b} L^{c}+h_{c b} \partial_{a} L^{c} .$$
With $a b=12$ this gives
$$B_{y}+C_{x}=0,$$
while with $a b=11$ or 22
$$B_{x}=C_{y}=-\frac{1}{2} L(u) .$$
Substitute from (23) into (24) and (25) to obtain the following system for $d \Omega$ :
$$\begin{gathered}
\Omega_{x} R_{x}-\Omega_{y} R_{y}=\Omega\left(R_{y y}-R_{x x}\right) \\
\Omega_{x} R_{y}+\Omega_{y} R_{x}=-2 \Omega R_{x y}
\end{gathered}$$
which algebraically solves to give
$$\begin{aligned}
\frac{\Omega_{x}}{\Omega} & =D^{-1}\left(R_{x}\left(R_{y y}-R_{x x}\right)-2 R_{y} R_{x y}\right), \\
\frac{\Omega_{y}}{\Omega} & =D^{-1}\left(-R_{y}\left(R_{x x}-R_{y y}\right)-2 R_{x} R_{x y}\right),
\end{aligned}$$
with $D=\left(R_{x}\right)^{2}+\left(R_{y}\right)^{2}=|d R|^{2}$ (note this is not $h(d R, d R)$ ). This can be simplified by moving some terms to the left since
$$D_{x}=2 R_{x} R_{x x}+2 R_{y} R_{x y}, D_{y}=2 R_{x} R_{x y}+2 R_{y} R_{y y}$$
so that
$$\begin{aligned}
& (\log (\Omega D))_{x}=D^{-1} R_{x}\left(R_{x x}+R_{y y}\right), \\
& (\log (\Omega D))_{y}=D^{-1} R_{y}\left(R_{x x}+R_{y y}\right),
\end{aligned}$$
or
$$d(\log (\Omega D))=D^{-1} \Delta_{0} R d R$$
with $\Delta_{0} R:=R_{x x}+R_{y y}$ (which again is not $\Delta_{h}$ ). Integrability for (26) is then
$$d\left(D^{-1} \Delta_{0} R\right) \wedge d R=0$$
which is solved by
$$D^{-1} \Delta_{0} R=F(R)$$
for some (analytic) $F$. This says
$$\Delta_{0} R+F(R)|\nabla R|^{2}=0$$
so solve $G^{\prime \prime} / G^{\prime}=F$ for $G$ to deduce
$$\nabla \cdot\left(G^{\prime} \nabla R\right)=0,$$
and
$$\Delta(G(R))=0,$$
with $\Delta_{0}$ or $\Delta_{h}$.
We have a necessary condition: some function of $R$ is harmonic. Next we exploit the coordinate freedom: with $\zeta=x+i y$ we can make the change
$$\zeta \rightarrow \hat{\zeta}=f(\zeta), \hat{x}=\phi(x, y), \hat{y}=\psi(x, y),$$
where $\phi, \psi$ are conjugate harmonic functions, if we accompany this by
$$u \rightarrow \hat{u}=u-\log f^{\prime}-\log \left(\bar{f}^{\prime}\right)$$
and then $R$ is unchanged (this is also of course a symmetry of the Toda field equation (18)). Now if $G(R)$ is harmonic then there is a new coordinate system in which it is $\hat{x}$. Drop the hats then w.l.o.g. $R=R(x)$ and the candidate Killing vector is $\partial_{y}$. (If preferred we could choose new coordinates so that $R=R(r)$ i.e. radially symmetric at least in some neighbourhood, possibly not including either the origin or a complete circle.)

We have
$$L=\partial_{y} \text { and } u_{y}=0 \text { at } z=0 .$$
By (21) we shall also have
$$0=\mathrm{L}\left(u_{z}\right)=u_{z y}$$
at $z=0$. Now by uniqueness of solution for the Toda field equation (18) we shall have $u_{y}=0$ for all $z$, and the second Killing vector is, without loss of generality, $L=\partial_{y}$ everywhere.

\section*{4 Ward's linearisation of the Toda field equation}

In this section, we follow [18] to relate the $y$-independent Toda field equation:
$$u_{x x}+\left(e^{u}\right)_{z z}=0,$$
to the axisymmetric Laplace equation in cylindrical polars:
$$V_{Z Z}+R^{-1}\left(R V_{R}\right)_{R}=0 .$$
This will lead to a solution of the Ricci-flat equations for the general one-sided type-D metric with an extra symmetry in terms of a solution of the axisymmetric Laplace equation in three dimensions.

To see how $u$ and $V$ are related, and following [18], set
$$x=V_{Z}, z=\frac{1}{2} R V_{R}, u=\log \left(R^{2} / 4\right),$$
(so we need to suppose that $V_{R}, V_{Z}$ are not constant). We calculate the Jacobian matrix
$$\frac{\partial(x, z)}{\partial(R, Z)}=\left(\begin{array}{cc}
V_{Z R} & -\frac{1}{2} R V_{Z Z} \\
V_{Z Z} & \frac{1}{2} R V_{R Z}
\end{array}\right)$$
with the aid of (29), and the inverse is
$$\frac{\partial(R, Z)}{\partial(x, z)}=\Delta^{-1}\left(\begin{array}{cc}
\frac{1}{2} R V_{Z R} & \frac{1}{2} R V_{Z Z} \\
-V_{Z Z} & V_{R Z}
\end{array}\right)$$
with $\Delta=\frac{1}{2} R\left(\left(V_{R Z}\right)^{2}+\left(V_{Z Z}\right)^{2}\right)$ (since $V_{R}, V_{Z}$ are not constant, $\Delta$ is nonzero). In particular therefore
$$R_{x}=\frac{1}{2} \Delta^{-1} R V_{R Z}, \quad R_{z}=-\Delta^{-1} V_{Z Z},$$
so with $u=\log \left(R^{2} / 4\right)$ as in (30) we deduce
$$u_{x}=\frac{2}{R} R_{x}=\Delta^{-1} V_{R Z}=Z_{z}, e^{u} u_{z}=-\frac{R}{2} \Delta^{-1} V_{Z Z}=-Z_{x},$$
and by cross-differentiating, we see that $u$ satisfies (28).
With $u_{y}=0, d \omega$ as in (15) subject to (16) becomes
$$d \omega=-W_{x} d y \wedge d z-e^{u}\left(W_{z}-2 c_{1} \frac{W^{2}}{z^{2}}\right) d x \wedge d y=d(F d y)$$
with
$$F_{z}=W_{x}=-\frac{z^{2} u_{x z}}{2 c_{1}}, \quad F_{x}=-e^{u}\left(W_{z}-2 c_{1} \frac{W^{2}}{z^{2}}\right)=\frac{1}{2 c_{1}} e^{u}\left(-z^{2}\left(u_{z z}+\left(u_{z}\right)^{2}\right)+2 z u_{z}-2\right) .$$
To integrate for $F$ we need the function $H$ conjugate to $V$. From (29) this satisfies
$$H_{R}=R V_{Z}, \quad H_{Z}=-R V_{R},$$
and then one verifies that
$$F=\frac{1}{2 c_{1}}\left(z^{2} u_{x}-\frac{1}{2} x R^{2}+H\right) .$$
Now transform the metric. First note that
$$\begin{gathered}
d z^{2}+e^{u} d x^{2}=\left(\frac{1}{2}\left(R V_{R}\right)_{R} d R+\frac{1}{2} R V_{R Z} d Z\right)^{2}+\frac{R^{2}}{4}\left(V_{R Z} d R+V_{Z Z} d Z\right)^{2} \\
=\frac{R^{2}}{4}\left(\left(-V_{Z Z} d R+V_{R Z} d Z\right)^{2}+\left(V_{R Z} d R+V_{Z Z} d Z\right)^{2}\right) \\
=\frac{1}{2} R \Delta\left(d R^{2}+d Z^{2}\right)
\end{gathered}$$
with the aid of (29) and the definition of $\Delta$. Now the metric is
$$\begin{gathered}
g=W^{-1}(d t+\omega)^{2}+W\left(d z^{2}+e^{u}\left(d x^{2}+d y^{2}\right)\right) \\
=W^{-1}(d t+F d y)^{2}+W e^{u} d y^{2}+\frac{1}{2} W R \Delta\left(d R^{2}+d Z^{2}\right) \\
=\quad\left(\begin{array}{ll}
d t & d y
\end{array}\right)\left(\begin{array}{cc}
W^{-1} & F W^{-1} \\
F W^{-1} & F^{2} W^{-1}+W e^{u}
\end{array}\right)\binom{d t}{d y}+\Omega^{2}\left(d R^{2}+d Z^{2}\right)
\end{gathered}$$
which is the canonical form for a Ricci-flat metric with two commuting Killing vectors. Note that the determinant of the matrix of Killing vector contractions is $e^{u}=R^{2} / 4$ so that
$R$ (up to a constant factor) is the standard radial coordinate, and then $Z$ is its harmonic conjugate. The metric components can be given explicitly in terms of $V, R, Z$ by noting
$$\begin{gathered}
W=\frac{V_{R}}{2 c_{1}}\left(\frac{R\left(\left(V_{R Z}\right)^{2}+\left(V_{Z Z}\right)^{2}\right)+V_{R} V_{Z Z}}{\left(\left(V_{R Z}\right)^{2}+\left(V_{Z Z}\right)^{2}\right)}\right), \\
F=\frac{1}{2 c_{1}}\left(H+\frac{R\left(V_{R}\right)^{2} V_{R Z}-R^{2} V_{Z}\left(\left(V_{R Z}\right)^{2}+\left(V_{Z Z}\right)^{2}\right)}{2\left(\left(V_{R Z}\right)^{2}+\left(V_{Z Z}\right)^{2}\right)}\right), \\
\Omega^{2}=\frac{1}{8 c_{1}} R^{2} V_{R}\left(R\left(\left(V_{R Z}\right)^{2}+\left(V_{Z Z}\right)^{2}\right)+V_{R} V_{Z Z}\right) .
\end{gathered}$$
Note that:
\begin{itemize}
\item[-] We have linearised the field equations for a Ricci-flat metric with two commuting symmetries. These field equations are already known to be linear if one of the symmetries is hypersurface orthogonal. We can be sure that we haven't inadvertently reduced to this case by looking at the examples which follow, specifically the Riemannian Kerr solution which does not in general admit a hypersurface orthogonal Killing vector.
\item[-] We have an expression for the metric given harmonic $V(R, Z)$. We could think about getting back to $V$ starting from $g$. One route is to set $Q=R V_{R}$ when
$$8 c_{1} \Omega^{2}=Q\left(\left(Q_{Z}\right)^{2}+\left(Q_{R}\right)^{2}-R^{-1} Q Q_{R}\right)$$
which needs to be solved for $Q$ given $\Omega$, with $Q$ also subject to
$$Q_{R R}-R^{-1} Q_{R}+Q_{Z Z}=0 .$$
\end{itemize}

\subsection*{4.1 A Corollary: linearising the SD Einstein equations with two commuting symmetries}

As a corollary to the previous section, we recall that the general solution to the (fourdimensional) SD (or ASD) Einstein equations with a symmetry was given in [11] (see also [15], [17]) and it also depends on a solution to the Toda field equation. Thus with a second symmetry, the Ward transformation can be applied again to give the general solution in this case in terms of an axisymmetric solution of the Laplace equation.

Recall, from [15], the metric in this case is
$$g=\frac{1}{P z^{2}}(d t+\omega)^{2}+\frac{P}{z^{2}}\left(d z^{2}+e^{u}\left(d x^{2}+d y^{2}\right)\right),$$
with
$$\begin{gathered}
u_{x x}+u_{y y}+\left(e^{u}\right)_{z z}=0 \\
2 \Lambda P=z u_{z}-2
\end{gathered}$$
where $\Lambda$ is proportional to the (constant) Ricci scalar, and
$$d \omega=-P_{x} d y \wedge d z-P_{y} d z \wedge d x-\left(P e^{u}\right)_{z} d x \wedge d y .$$
If we add a second symmetry then the argument goes through as before, and without loss of generality we can suppose $u_{y}=0$ and the second symmetry is $L=\partial_{y}$. We can solve for $\omega$ :
$$\omega=F d y, \quad F=\frac{1}{2 \Lambda}\left(z u_{x}-Q\right),$$
with $Q$ conjugate to $u$ in the sense
$$u_{x}=Q_{z}, \quad\left(e^{u}\right)_{z}=-Q_{x} .$$
We follow the Ward transformation as before, set:
$$x=V_{Z}, z=\frac{1}{2} R V_{R}, \quad u=\log \left(R^{2} / 4\right),$$
then as before
$$d z^{2}+e^{u} d x^{2}=\frac{1}{2} R \Delta\left(d R^{2}+d Z^{2}\right),$$
with
$$\Delta=\frac{1}{2} R\left(\left(V_{R Z}\right)^{2}+\left(V_{Z Z}\right)^{2}\right) .$$
The metric becomes
$$g=\frac{8 \Lambda \Delta}{R^{2} V_{R}^{2}\left(2 \Delta+V_{R} V_{Z Z}\right)}(d t+F d y)^{2}+\frac{\left(2 \Delta+V_{R} V_{Z Z}\right)}{2 \Lambda \Delta V_{R}^{2}} d y^{2}+\frac{\left(2 \Delta+V_{R} V_{Z Z}\right)}{R V_{R}^{2}}\left(d R^{2}+d Z^{2}\right) .$$
For $F$ we note from (32) that $Q=Z$ and from the Jacobian matrix (31)
$$z u_{x}=\frac{1}{2 \Delta} R V_{R} V_{Z Z},$$
so that
$$F=\frac{1}{2 \Lambda}\left(\frac{1}{2 \Delta} R V_{R} V_{Z Z}-Z\right) .$$
This then is the general SD Einstein metric with $\Lambda \neq 0$ and two commuting symmetries, written in terms of a solution $V$ of the axisymmetric Laplace equation (29). We'll give an example in Section 7.

\section*{5 One-sided type-D Einstein metrics}

It's natural to ask whether the addition of a non-zero scalar curvature interferes with the integrability of the field equations: for ASD vacuum with a symmetry it does not while for vacuum with two commuting Killing vectors it does. In the case considered in this section it does - we can reduce the field equations to a modified Toda field equation but not an integrable one. ${ }^{1}$

To see this, suppose we still have (1) but with a nonzero $\Lambda$, in NP conventions. Then (2) still defines a Killing spinor (the argument in [10] for its existence uses the contracted Bianchi identity, which is unchanged in this case). We need to assume that $\psi$ is not constant as we shall want to use it as a coordinate. By making this assumption we are eliminating some cases: if $\psi$ is constant then $K^{a}$ is zero and $\omega_{A B}$ defines a Kähler form, thus we are excluding Einstein-Kähler metrics. Equation (3) still defines a Killing vector $K^{a}$, but (6) is changed to
$$\nabla_{A A^{\prime}} K_{B B^{\prime}}=-\frac{1}{6}(\psi+12 \Lambda) \omega_{A B} \epsilon_{A^{\prime} B^{\prime}}+\chi_{A^{\prime} B^{\prime}} \epsilon_{A B},$$
with a corresponding change in (14). With $d \omega$ as in (15) we find $\alpha$ and $\beta$ as in (16) unchanged but
$$\gamma=-e^{u}\left(W_{z}+\frac{2}{3}(\psi+12 \Lambda) \psi^{-1 / 3}\right) .$$
We may introduce $z=-\psi^{-1 / 3}$ as before and then it is convenient to introduce
$$g(z)=\frac{1}{3} \psi^{-1 / 3}(\psi+12 \Lambda)=\frac{12 \Lambda z^{3}-1}{3 z^{2}} .$$
The connection coefficients $\alpha^{i}{ }_{j}$ take the same form with $G$ and $H$ unchanged but with
$$C=W^{1 / 2} g-\frac{1}{2} W^{-1 / 2} u_{z},$$
and
$$E=g W^{1 / 2} .$$
We calculate the curvature forms $\Omega^{i}{ }_{j}$ but this time with $\epsilon_{i j k} \Omega_{i j . k}=24 \Lambda$. From $\Omega^{1}{ }_{2}+i \Omega^{1}{ }_{3}$ we find
$$g W=-\frac{1}{2} u_{z}+h(z)$$
with $h^{\prime}=h^{2}$ so that $h=-(z-c)^{-1}$ for some $c$. Then $\Omega_{3}^{2}$ leads to $c=0$ and the modified Toda equation
$$u_{x x}+u_{y y}+\left(e^{u}\right)_{z z}+e^{u}\left(A(z) u_{z}+B(z)\right)=0,$$
for $u$, with
$$A=\frac{72 \Lambda z^{2}}{1-12 \Lambda z^{3}}, \quad B=-\frac{144 \Lambda z}{1-12 \Lambda z^{3}}$$

\footnotetext{
${ }^{1}$ This class of metrics was considered in [12] but it is not straightforward to compare results obtained.
}

One can now verify that the expression for $d \omega$ is consistent (i.e. that $d(d \omega)=0$ ). One can also check that (40) cannot just be transformed back into the Toda equation by the simple change of variable:
$$z \rightarrow Z=f(z), \quad u \rightarrow U=u+F(z) .$$
This in fact shows that (40) is not integrable: it is known ([6]) that the only modifications of Toda of the form of (40) which are integrable are those obtained by the transformation (41). We can check the expressions for $A(z)$ and $B(z)$ by obtaining the known one-sided type D Einstein space which is the Schwarzschild-de Sitter metric. We do this in the final section, with other examples. In the next section we dispose of an apparent puzzle concerning the one-sided type-D vacuum and Einstein metrics.

\section*{6 An apparent puzzle}

From the assumption of one-sided type-D-ness and either vacuum or Einstein, we have been able to reduce the Einstein equations to one of two PDEs for a single function $u$. It is striking that at no stage do we consider the ASD Weyl spinor, only ever the SD Weyl spinor, but the ASD Weyl spinor is evidently uniquely defined from the metric. This could be contrasted with linear (gravity) theory in which there are degrees of freedom and therefore free data to be specified for both SD and ASD linearised Weyl spinors. One way to explain this apparent puzzle is to point to the Killing vector arising from the Killing spinor, which necessarily satisfies the identity
$$\nabla_{a} \nabla_{b} K_{c}=R_{b c a d} K^{d},$$
a relation that one doesn't have in linear theory but which, in the full theory, clearly connects the ASD and SD Weyl spinors. Dealing first with one-sided type-D vacuum solutions, we have the Killing spinor $\omega_{A B}$ from (2), defining the Killing vector $K^{a}$ via (3), which in turn satisfies (6). If we contract (6) with $K^{b}$ we obtain
$$\frac{1}{2} \nabla_{a} W^{-1}=K^{b} \nabla_{a} K_{b}=-\frac{1}{6} \psi \omega_{A B} K_{A^{\prime}}^{B}-\chi_{A^{\prime} B^{\prime}} K_{A}^{B^{\prime}}$$
which we may rearrange as
$$\chi_{A^{\prime} B^{\prime}} K_{A}^{B^{\prime}}=\frac{1}{36} \psi^{-2 / 3} \nabla_{a} \psi-\frac{1}{2} \nabla_{a} W^{-1}=\nabla_{a} Q$$
where we introduce $Q=-\frac{1}{2} W^{-1}-\frac{1}{12} z^{-1}$. Multiplying by $K_{A^{\prime}}^{A}$ gives an expression for $\chi_{A^{\prime} B^{\prime}}$ as
$$\chi_{A^{\prime} B^{\prime}}=W K_{A^{\prime}}^{B} \nabla_{B B^{\prime}} Q$$
which is therefore known explicitly when we know $u$. This in turn is a potential for the SD Weyl spinor via (8) so that, as must be the case, knowledge of $u$ fixes both the ASD and the SD Weyl spinor - there is no more free data.

\section*{7 Examples}
\begin{itemize}
\item[-] Starting with one-sided type-D vacua, flat space is not an example of the construction, as we're assuming the SD Weyl spinor isn't zero. However, we could have chosen the zero solution of the Toda equation, when, taking $c_{1}=1$ for simplicity,
$$u=0, \quad W=z, \quad \omega=x d y,$$
and the metric is
$$g=\frac{1}{z}(d t+x d y)^{2}+z\left(d z^{2}+d x^{2}+d y^{2}\right),$$
which is recognisably the Gibbons-Hawking metric with potential $z$ (see e.g. [7]). In particular, this metric is hyper-Kähler with the other orientation so that the primed Weyl spinor is zero. With $T=\frac{2}{3} z^{3 / 2}$, it can be written
$$g=d T^{2}+\left(\frac{3 T}{2}\right)^{3 / 2}\left(d x^{2}+d y^{2}\right)+\left(\frac{2}{3 T}\right)^{3 / 2}(d t+x d y)^{2}$$
which makes the isometry group manifest: this is LRS Bianchi-type II. Because $u=0$, this doesn't have a Ward form.
\item[-] There are separable solutions of the Toda equation (18) in the sense $u=f(x, y)+g(z)$ (see e.g. [16]) some of which can be written
$$u=-2 \log \left(1+x^{2}+y^{2}\right)+\log \left(4\left(z^{2}+2 m z+a\right)\right),$$
for real constants $a, m$, when
$$W=\frac{z(a+m z)}{z^{2}+2 m z+a}, \quad \omega=-a \cos \theta d \phi,$$
and we've introduced polar coordinates by $\zeta=\tan (\theta / 2) e^{i \phi}$. The metric can be written
$$g=\frac{\left(z^{2}+2 m z+a\right)}{z(a+m z)}(d t-a \cos \theta d \phi)^{2}+\frac{z(a+m z)}{z^{2}+2 m z+a} d z^{2}+z(a+m z)\left(d \theta^{2}+\sin ^{2} \theta d \phi^{2}\right),$$
which has LRS Bianchi-type-IX form. When $a=0$ it is the Riemannian Schwarzschild solution; with $a=m^{2}, n=-m^{3 / 2} / 2$ it is the self-dual Taub-NUT metric as given in equation (3.9) of [7]; with $m=0$ it is the Eguchi-Hanson metric as in (3.20) of [7] but with $a^{4}$ there replaced by $-16 a^{3}$ from here (in particular it isn't the Riemannian Kerr solution).
There will be more, probably unfamiliar, one-sided type-D metrics determined by the 'quadric ansatz' [16] for solutions of the Toda equation.
\end{itemize}
\begin{itemize}
\item[-] To illustrate the Ward transformation on a one-sided type-D vacuum with an extra symmetry, we consider the particular separable solution of the Toda equation given by
$$u=2 \log \operatorname{sech} x+\log \left(z^{2}+2 m z+a\right),$$
when
$$W=\frac{z(m z+a)}{z^{2}+2 m z+a}, \omega=a \tanh x d y$$
and with $\cos \theta=\tanh x, \phi=-y$ we arrive at the metric in (43) again, but this time with $u$ such that $u_{y}=0$. For simplicity put $a=m^{2}$, and then
$$R=2(z+m) \operatorname{sech} x, Z=-2(z+m) \tanh x,$$
and
$$V=-2 m \log R+\left(R^{2}+Z^{2}\right)^{1 / 2}-Z \tanh ^{-1}\left(\frac{Z}{\left(R^{2}+Z^{2}\right)^{1 / 2}}\right)$$
which one verifies is harmonic. (In spherical polars the terms independent of $m$ are
$$V=r(1-\cos \theta \log \cot (\theta / 2) .)$$
\item[-] For the transformation (30) to be nontrivial, we need $V_{R}$ and $V_{Z}$ to be nonconstant, so for an example with a simple $V$ consider
$$V=R^{2}-2 Z^{2} .$$
Then
$$x=V_{Z}=-4 Z, \quad z=\frac{1}{2} R V_{R}=R^{2}, \quad u=\log \left(R^{2} / 4\right),$$
and we have the simple solution $u=\log (z / 4)$ of (28). After a change of variable, the metric (12) becomes the LRS Riemannian Kasner solution:
$$g=d T^{2}+T^{-2 / 3} d U^{2}+T^{4 / 3}\left(d X^{2}+d Y^{2}\right) .$$
\item[-] Riemannian Kerr: We start with the NP tetrad (of vectors) tied to the Principal Null Directions for Lorentzian Kerr as given in [1], (24)-(26), lower to one-forms and transform to Boyer-Lindquist coordinates via (35) of [1] to obtain
$$\begin{gathered}
\ell=d t-\frac{\Sigma^{2}}{\tilde{\Delta}} d r-a \sin ^{2} \theta d \phi, n=\frac{\tilde{\Delta}}{2 \Sigma^{2}}\left(d t-a \sin ^{2} \theta d \phi\right)+\frac{1}{2} d r \\
m=\frac{1}{\sqrt{2} \Gamma}\left(i a \sin \theta d t-\Sigma^{2} d \theta-i\left(r^{2}+a^{2}\right) \sin \theta d \phi\right)
\end{gathered}$$
where
$$\Sigma^{2}=r^{2}+a^{2} \cos ^{2} \theta, \quad \tilde{\Delta}=r^{2}-2 m r+a^{2}, \quad \Gamma=r+i a \cos \theta .$$
\end{itemize}

In this form we can analytically continue to Riemannian signature by changing $(t, a)$ to $(i t, i a)$. It's convenient to boost and rotate the basis a little to arrive at
$$L=(-i \tilde{\Theta}) \ell=\tilde{\Theta}\left(d t-a \sin ^{2} \theta d \phi\right)+\frac{i}{2 \tilde{\Theta}} d r, \quad N=\bar{L}$$
and
$$M=\frac{1}{\sqrt{2} \Sigma}\left(-\Sigma^{2} d \theta+i \sin \theta\left(a d t+\left(r^{2}-a^{2}\right) d \phi\right)\right)$$
where now
$$\tilde{\Theta}=\frac{\sqrt{\tilde{\Delta}}}{\Sigma \sqrt{2}}, \quad \tilde{\Delta}=r^{2}-2 m r-a^{2}, \quad \Sigma^{2}=r^{2}-a^{2} \cos ^{2} \theta .$$
Since both Weyl spinors are type-D we have a choice of complex structures, both of them integrable: one, say $J_{1}$, has $L, M$ as holomorphic one-forms and the other, $J_{2}$, has $L, \bar{M}$. We lower the Killing vector $K=\partial_{t}$ and take its exterior derivative to obtain
$$d K=i X(L \wedge \bar{L}+M \wedge \bar{M})+i Y(L \wedge \bar{L}-M \wedge \bar{M})$$
with
$$X=-m(r-a \cos \theta)^{-2}, \quad Y=-m(r+a \cos \theta)^{-2},$$
so if we stick with $J_{1}$ then $i(L \wedge \bar{L}+M \wedge \bar{M})$ is the 2-form corresponding to the Killing spinor under consideration, the scalar $\psi$ is a multiple of $(r-a \cos \theta)^{-3}$ and the coordinate $z$ is a multiple of $r-a \cos \theta$. Comparing the Riemannian Kerr metric, which is now
$$g=2 \tilde{\Theta}^{2}\left(d t-a \sin ^{2} \theta d \phi\right)^{2}+\frac{d r^{2}}{2 \tilde{\Theta}^{2}}+\Sigma^{2} d \theta^{2}+\frac{\sin ^{2} \theta}{\Sigma^{2}}\left(a d t+\left(r^{2}-a^{2}\right) d \phi\right)^{2}$$
with the metric form (12) and using $z=r-a \cos \theta$, we are led to
$$e^{u} d \zeta d \bar{\zeta}=\tilde{\Delta} \sin ^{2} \theta\left(\left(a \tilde{\Delta}^{-1} d r-\csc \theta d \theta\right)^{2}+d \phi^{2}\right)$$
when a choice for $\zeta$ is
$$\zeta=x+i y=\log \left(\left(\frac{r-m-b}{r-m+b}\right)^{-a / 2 b} \tan (\theta / 2) e^{i \phi}\right),$$
where $b^{2}=a^{2}+m^{2}$, so in particular $y=\phi$, and then $u$ is given by
$$e^{u}=\left(r^{2}-2 m r-a^{2}\right) \sin ^{2} \theta,$$
in agreement with (30) (as this is the determinant of the $(\phi, t)$-part of the metric). It is straightforward to verify that
$$u_{x}=Z_{z}, \quad e^{u} u_{z}=-Z_{x},$$
with $Z=2(r-m) \cos \theta$, so that $u$ does satisfy (28) but we can't obtain $u(x, z)$ explicitly. From (30) we have
$$R^{2}=4 e^{u}=4\left(r^{2}-2 m r-a^{2}\right) \sin ^{2} \theta,$$
together with
$$Z=2(r-m) \cos \theta,$$
so that $(r, \theta)$ are ellipsoidal coordinates in the $(R, Z)$ plane. It is straightforward to obtain $V(r, \theta)$ : we find
$$\begin{gathered}
V=2(r-a \cos \theta)+2((r-m) \cos \theta-a) \log \tan (\theta / 2)+2 m \log \sin \theta \\
+\left((m+b)-\frac{a}{b}(r-m) \cos \theta\right) \log (r-m-b)+\left((m-b)+\frac{a}{b}(r-m) \cos \theta\right) \log (r-m+b) .
\end{gathered}$$
This isn't simple for $V$ in terms of $R, Z$ (or $x, z$ ).
\begin{itemize}
\item[-] We can give a simple example of the construction described in the Corollary (Section 4.1) by again taking $V=R^{2}-2 Z^{2}$. With $\Lambda=2$ for convenience (which leads to Ricci scalar equal to -24), and $Y=y / 4$, the metric turns out to be
$$g=\frac{4}{R^{4}}(d t-Z d Y)^{2}+\frac{1}{R^{2}}\left(d R^{2}+d Y^{2}+d Z^{2}\right) .$$
This is easily to be seen to be ASD Einstein-Kähler with constant holomorphic sectional curvature and negative Ricci scalar, so it must be the Bergman metric.
\item[-] As an example of one-sided type-D Einstein from Section 5, we note that (40) has solutions of the form
$$u=-2 \log \left(1+k\left(x^{2}+y^{2}\right)\right)+F(z),$$
with $e^{F}$ a 2-parameter family of quartic polynomials in $z$ :
$$e^{F}=c_{2}\left(1+24 \Lambda z^{3}\right)+c_{3} z\left(1+6 \Lambda z^{3}\right)+4 k z^{2},$$
and these include the Schwarzschild-de Sitter metric if $k=1, c_{2}=0$, and $c_{3}$ is negative and related to the mass parameter. This calculation also confirms the expressions for $A$ and $B$ in (40).
\end{itemize}

\section*{References}
\begin{itemize}
\item[] [1] T Adamo and E T Newman, The Kerr-Newman metric, Scholarpedia, 9(10):31791.
\item[] [2] S Aksteiner, private communication to the author (2019).
\end{itemize}
\begin{itemize}
\item[] [3] V Belinski and E Verdaguer, Gravitational solitons, Cambridge Monographs on Mathematical Physics. Cambridge University Press, Cambridge, 2001.
\item[] [4] Y Chen and E Teo A new AF gravitational instanton, Phys.Lett. B703 359-362 (2011) arXiv:1107.0763
\item[] [5] M Dunajski and P Tod, Four-Dimensional Metrics Conformal to Kähler, Math.Proc.Camb.Phil.Soc. doi 10.1017/S030500410999048X arXiv:0901.2261
\item[] [6] Private communication from Jenya Ferapontov, but see also S Berjawi, E Ferapontov, B Kruglikov and V Novikov, Second-order PDEs in 3D with Einstein-Weyl conformal structure arXiv: 2104.02716
\item[] [7] G W Gibbons and S W Hawking, Classification of gravitational instanton symmetries. Comm. Math. Phys. 66 291-310 (1979)
\item[] [8] S A Huggett and K P Tod, An Introduction to Twistor Theory, LMS Student Text 4, Cambridge: CUP 1985
\item[] [9] R Penrose and W Rindler, Spinors and Spacetime vols I and II, Cambridge: CUP 1984 and 1986
\item[] [10] R Penrose and M Walker, On quadratic first integrals of the geodesic equations for type \{22\} spacetimes, Comm. Math. Phys. 18 265-274 (1970)
\item[] [11] M Przanowski, Killing vector fields in self-dual, Euclidean Einstein spaces with $\Lambda \neq 0$ Jour.Math.Phys. 32 1004-1010 (1991)
\item[] [12] M Przanowski, Notes on the Einstein equations for locally Hermite-Einstein spaces, Acta Physica Polonica 22 357-365 (1991)
\item[] [13] M Przanowski and B Baka, One-sided type D gravitational instantons, Gen.Rel.Grav. 16 797-803 (1984)
\item[] [14] M Przanowski and S Bialecki, Lie-Bäcklund transformations and gravitational instantons, Acta Physica Polonica B18 879-889 (1987)
\item[] [15] K P Tod, The $S U(\infty)$ Toda field equation and special four-dimensional metrics inLecture Notes in pure and applied mathematics 184 Geometry and Physics, eds. J E Andersen, J Dupont, H Pedersen and A Swann Marcel Dekker Inc. New York (1997)
\item[] [16] K P Tod, Scalar-flat Kähler and hyper-Kähler metrics from Painlevé-III. Classical Quantum Gravity 12, 1535-1547 (1995)
\item[] [17] P Tod, A Note on Riemannian Anti-self-dual Einstein metrics with Symmetry, arXiv:hep-th/0609071
\end{itemize}
[18] R S Ward, Einstein-Weyl spaces and $S U(\infty)$ Toda fields, Class.Quant.Grav. 7 L95-98 (1990)