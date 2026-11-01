---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Bianchi IX self-dual Einstein metrics and singular
                    <i>G</i>
                    <sub>2</sub>
                    manifolds]

---
source_file: hep-th_0206151.pdf
converter: mathpix
format: mmd
---

\title{
Bianchi IX Self-dual Einstein Metrics and Singular $G_{2}$ Manifolds
}

\author{
M. Cvetič ${ }^{\dagger b}$, G.W. Gibbons ${ }^{\sharp}$, H. Lü ${ }^{\star}$ and C.N. Pope ${ }^{\ddagger b}$ \\ ${ }^{\dagger}$ Department of Physics and Astronomy, University of Pennsylvania Philadelphia, PA 19104, USA \\ ${ }^{\sharp}$ DAMTP, Centre for Mathematical Sciences, Cambridge University Wilberforce Road, Cambridge CB3 OWA, UK \\ *Michigan Center for Theoretical Physics, University of Michigan Ann Arbor, MI 48109, USA \\ ${ }^{\ddagger}$ Center for Theoretical Physics, Texas A\&M University, College Station, TX 77843, USA \\ ${ }^{\mathrm{b}}$ Isaac Newton Institute for Mathematical Sciences, 20 Clarkson Road, University of Cambridge, Cambridge CB3 0EH, UK
}

\begin{abstract}
We construct explicit cohomogeneity two metrics of $G_{2}$ holonomy, which are foliated by twistor spaces. The twistor spaces are $S^{2}$ bundles over four-dimensional Bianchi IX Einstein metrics with self-dual (or anti-self-dual) Weyl tensor. Generically the 4-metric is of triaxial Bianchi IX type, with $S U(2)$ isometry. We derive the first-order differential equations for the metric coefficients, and obtain the corresponding superpotential governing the equations of motion, in the general triaxial Bianchi IX case. In general our metrics have singularities, which are of orbifold or cosmic-string type. For the special case of biaxial Bianchi IX metrics, we give a complete analysis their local and global properties, and the singularities. In the triaxial case we find that a system of equations written down by Tod and Hitchin satisfies our first-order equations. The converse is not always true. A discussion is given of the possible implications of the singularity structure of these spaces for M-theory dynamics.
\end{abstract}

\section*{Contents}
1 Introduction ..... 2
2 Asymptotically-conical $G_{2}$ metrics ..... 3
$2.1 G_{2}$ holonomy of $R^{3}$ bundles over self-dual Einstein 4-metrics ..... 3
2.2 Nearly-Kähler geometry and $G_{2}$ holonomy ..... 5
$3 G_{2}$ holonomy equations for Bianchi IX base ..... 7
4 Biaxial anti-self-dual Bianchi IX metrics ..... 9
4.1 Self-dual Taub-NUT-de Sitter metrics ..... 10
4.2 Biaxial first-order equations, and self-dual Eguchi-Hanson-de Sitter ..... 12
4.3 Phase-plane analysis for the biaxial system ..... 15
4.4 Global structure of the biaxial solutions ..... 17
4.5 Phase plane and global structure for negative $\Lambda$ ..... 18
4.6 Superpotential for the biaxial system ..... 20
5 Triaxial anti-self-dual Bianchi IX metrics ..... 20
5.1 Phase-plane and superpotential for triaxial system ..... 20
5.2 The Tod-Hitchin first-order system ..... 22
5.3 Explicit examples ..... 24
5.4 Global structure of the metrics ..... 26
6 Singularity structure and M-theory ..... 28
A Bianchi IX Einstein-Kähler metrics ..... 32
B Iwai's construction, Dragt coordinates and the Guichardet connection ..... 33
C Killing spinors ..... 35

\section*{1 Introduction}

Concrete non-singular examples of seven-dimensional metrics with $G_{2}$ holonomy have been known only since about 1989. The original construction involved making an ansatz for metrics of cohomogeneity one, where the six-dimensional principal orbits were $S^{3} \times S^{3}$, or else the twistor spaces of $S^{4}$ or $\mathbb{C P}^{2}$ [1, 2]. The twistor space is a 2-sphere bundle over the $S^{4}$ or $\mathbb{C P}^{2}$ base, with an $S U(2)$ or $S O(3)$ structure group associated to the chiral spin (or spin ${ }^{c}$ ) bundle of the base. The local construction can be carried out for any base space $M_{4}$ equipped with an Einstein metric and for which the Weyl tensor is self-dual or anti-self-dual [1, 2]. ${ }^{1}$ By a theorem of Hitchin, the only nonsingular such examples with positive Ricci tensor (which implies $M_{4}$ is compact) occur when $M_{4}$ is $S^{4}$ or $\mathbb{C P}^{2}$ [3].

The current interest in $G_{2}$ manifolds in M-theory has been motivated in part by the role that they can play in compactifying to four dimensions, analogous to the compactification of ten-dimensional string theory on Calabi-Yau 6-manifolds. Unlike the latter, where non-singular Calabi-Yau manifolds can naturally give rise to chiral $\mathcal{N}=1$ theories in four dimensions starting from the heterotic string in $D=10$, non-singular $G_{2}$ compactifications of M-theory would necessarily give abelian non-chiral $\mathcal{N}=1$ theories in four dimensions. To get non-abelian chiral theories from M-theory, one needs to consider compactifications on singular $G_{2}$ manifolds. One explicit realisation of such an M-theory compactification has an interpretation as an $S^{1}$ lift of Type IIA theory (compactified on an orientifold) with intersecting D6-branes and O6 orientifold planes [4]. Non-Abelian gauge fields arise at the locations of coincident branes, and chiral matter arises at the intersections of D6-branes. The $S^{1}$ lift of such configurations results in singular $G_{2}$ holonomy metrics in M-theory. Codimension four ADE-type singularities are associated with the location of the coincident D6-branes, and co-dimension seven singularities are associated with the location of the intersection of two D6-branes in Type IIA theory [4, 5, 6, 7, 8].

Further analyses of co-dimension seven singularities of the $G_{2}$ holonomy spaces, leading to chiral matter, were given in [6, 7, 8] and the subsequent work [9, 10, 11, 12]. It is expected that there exist wide classes of 7-manifolds with $G_{2}$ holonomy and the singularity structure that again would yield non-Abelian $\mathcal{N}=1$ supersymmetric four-dimensional theories with chiral matter, and in particular the explicit construction of such metrics would provide a starting point for further studies of chiral M-theory dynamics.

\footnotetext{
${ }^{1}$ Such metrics are generally referred to as "self-dual Einstein," and unless the context makes it necessary in order to avoid confusion, we shall often use this term regardless of whether the Weyl tensor is actually self-dual or anti-self-dual.
}

Much research on finding new non-singular $G_{2}$ manifolds has been carried out in recent times (see, for example, [13, 14, 15, 16, 17, 18, 19] and references therein). In view of their potential phenomenological interest, it is appropriate also to investigate examples of singular $G_{2}$ manifolds. Typically, these singularities should be of co-dimension seven, and they should be of the relatively mild orbifold type [5, 6], where the curvature is bounded everywhere except for delta-function contributions.

One way to obtain singular $G_{2}$ holonomy spaces is by returning to the original $G_{2}$ construction in [1, 2], with principal orbits that are $S^{2}$ bundles over self-dual Einstein four-dimensional manifolds $M_{4}$ (forming the base of the twistor space), but with $M_{4}$ now chosen to be neither the $S^{4}$ nor the $\mathbb{C P}^{2}$ non-singular examples. Instead, one can choose $M_{4}$ to be a self-dual Einstein space with orbifold-type singularities. Some investigations of the $G_{2}$ metrics that result from such a construction have already been carried out [10]. In this paper we pursue the analysis further, by considering more general possibilities for the base space $M_{4}$. Since the procedure for obtaining the $G_{2}$ metric from a given self-dual Einstein base space $M_{4}$ is well established [1, 2], much of the paper will concentrate on the details of the self-dual Einstein metrics themselves.

There exists a large mathematical literature on self-dual Einstein metrics (sometimes called quaternionic Kähler). The focus of our study in this paper will be on self-dual Einstein metrics of the triaxial Bianchi IX type, where there is an $S U(2)$ isometry that acts transitively on 3-dimensional orbits that are (locally) $S^{3}$. Quite a lot is known about this case [20, 22, 23], but we believe that our results go beyond what is in the existing literature, and that our viewpoint, derived as it is from the associated $G_{2}$ metric, is novel. In particular, we shall derive the general first-order equations for these metrics and analyse their local and global structure. For the special case of biaxial Bianchi IX metrics, we provide a complete analysis. In the triaxial case, we compare our analysis with that of Tod [21] and Hitchin [22, 23], and analyse some of the explicitly-known solutions. Some implications for M-theory of these $G_{2}$ holonomy metrics are also discussed.

\section*{2 Asymptotically-conical $G_{2}$ metrics}
$2.1 G_{2}$ holonomy of $R^{3}$ bundles over self-dual Einstein 4 -metrics
The metrics of $G_{2}$ holonomy that have twistor-space orbits take the form [1, 2]
$$d s_{7}^{2}=4\left(1-\frac{1}{r^{4}}\right)^{-1} d r^{2}+r^{2}\left(1-\frac{1}{r^{4}}\right)\left(D \mu_{i}\right)^{2}+2 r^{2} d s_{4}^{2},$$
where $\mu_{i} \mu_{i}=1$. The covariant exterior derivative is defined by $D \mu_{i} \equiv d \mu_{i}+\epsilon_{i j k} A^{j} \mu_{k}$, and the metric $d s_{4}^{2}$ is required to be Einstein, with $R_{a b}=\Lambda g_{a b}$ (with $\Lambda$ taken to be normalised to $\Lambda=3$ in (1). The Yang-Mills fields have the defining property that $D J^{i}=0$, where the quaternionic Kähler forms $J^{i}$ on the base space $\mathrm{M}_{4}$ have a definite duality, and satisfy
$$J_{a b}^{i} J_{b c}^{j}=-\delta_{a c} \delta^{i j}+\epsilon_{i j k} J_{a c}^{k},$$
where the gauge-covariant exterior derivative is defined by
$$D J_{a b}^{i} \equiv \nabla J_{a b}^{i}+\epsilon_{i j k} A^{j} J_{a b}^{k},$$
with
$$\nabla J_{a b}^{i} \equiv d J_{a b}^{i}+\omega_{a c} J_{c b}^{i}+\omega_{b c} J_{a c}^{i} .$$
The integrability condition $D^{2} J_{a b}^{i}=0$ has, as a particular consequence,
$$F_{a b}^{i}=\frac{1}{2} J_{c d}^{i} R_{a b c d},$$
where $F^{i} \equiv d A^{i}+\frac{1}{2} \epsilon_{i j k} A^{j} \wedge A^{k}$. We furthermore require that the Yang-Mills fields $F^{i}$ be proportional to the quaternionic Kähler forms. We shall take $J_{a b}^{i}$ to be self-dual, in which case we have the identity
$$J_{a b}^{i} J_{c d}^{i}=\delta_{a c} \delta_{b d}-\delta_{a d} \delta_{b d}+\epsilon_{a b c d} .$$
From this and equation (5), it can be seen that if the Weyl tensor
$$C_{a b c d} \equiv R_{a b c d}-\frac{1}{3} \Lambda\left(\delta_{a c} \delta_{b d}-\delta_{a d} \delta_{b c}\right)$$
of the Einstein metric $d s_{4}^{2}$ is anti-self-dual, then we shall have
$$F^{i}=\frac{1}{3} \Lambda J^{i} .$$

We can change variables to a set of coordinates $u_{i}$ on $\mathbb{R}^{3}$, which are unconstrained, by taking $u_{i}=\rho \mu_{i}$, and letting $\frac{1}{3} \Lambda \rho^{2}=r^{4}-1$, leading to the expression
$$d s_{7}^{2}=\frac{\left(D u_{i}\right)^{2}}{\sqrt{1+\frac{1}{3} \Lambda \rho^{2}}}+2 \sqrt{1+\frac{1}{3} \Lambda \rho^{2}} d s_{4}^{2}$$
where $\rho$ means $\sqrt{u_{i} u_{i}}, D u_{i}=d u_{i}+\epsilon_{i j k} A^{j} u_{k}$, and we have rescaled so that $d s_{4}^{2}$ has cosmological constant $\Lambda$.

The $G_{2}$ holonomy is easily established by noting that we may take the associative 3-form to be, reverting to $\Lambda=3$ for convenience,
$$\Phi_{(3)}=\frac{1}{6}\left(1+\rho^{2}\right)^{-3 / 4} \epsilon_{i j k} D u_{i} D u_{j} D u_{k}+2\left(1+\rho^{2}\right)^{1 / 4} D u_{i} \wedge J^{i} .$$

The dual of $\Phi_{(3)}$ in the metric (9) is therefore
$$* \Phi_{(3)}=4\left(1+\rho^{2}\right) \Omega_{(4)}+\epsilon_{i j k} D u_{i} \wedge D u_{j} \wedge J^{k},$$
where $\Omega_{(4)}$ is the volume form of $d s_{4}^{2}$, which can also be written as $\Omega_{(4)}=\frac{1}{2} J^{1} \wedge J^{1}=$ $\frac{1}{2} J^{2} \wedge J^{2}=\frac{1}{2} J^{3} \wedge J^{3}$. From the identity $D^{2} u_{i}=\epsilon_{i j k} F^{j} u_{k}$, one easily sees that $\Phi_{(3)}$ is closed and co-closed.

\subsection*{2.2 Nearly-Kähler geometry and $G_{2}$ holonomy}

If we go to the asymptotic region, where $\rho \longrightarrow \infty$, we get the metric on the cone over the twistor space of $\mathrm{M}_{4}$,
$$d s_{7}^{2}=\frac{1}{\rho}\left(D u_{i}\right)^{2}+2 \rho d s_{4}^{2} .$$
Defining $\rho=\frac{1}{4} r^{2}$, this becomes
$$d s_{7}^{2}=d r^{2}+r^{2} d s_{6}^{2},$$
and so if $d s_{7}^{2}$ has $G_{2}$ holonomy then
$$d s_{6}^{2}=\frac{1}{4}\left(D \mu_{i}\right)^{2}+\frac{1}{2} d s_{4}^{2}$$
is the nearly-Kähler metric on the twistor space of $\mathrm{M}_{4}$. The associative 3-form becomes
$$\Phi_{(3)}=\frac{1}{6} \rho^{-3 / 2} \epsilon_{i j k} D u_{i} D u_{j} D u_{k}+2 \rho^{1 / 2} D u_{i} \wedge J^{i},$$
and its Hodge dual is
$$* \Phi_{(3)}=4 \rho^{2} \Omega_{(4)}+\epsilon_{i j k} D u_{i} \wedge D u_{j} \wedge J^{k} .$$
The conditions of closure and co-closure of $\Phi_{(3)}$ therefore imply that $d s_{6}^{2}$ in (14) is nearly-Kähler.

The definition of a nearly-Kähler metric $d s_{6}^{2}$ is that the cone over $d s_{6}^{2}$, namely
$$d \hat{s}_{7}^{2}=d r^{2}+r^{2} d s_{6}^{2}$$
has $G_{2}$ holonomy. A more suggestive, but equivalent, terminology for $d s_{6}^{2}$ is therefore that it has weak $S U(3)$ holonomy; we discuss this briefly below.

If the cone metric $d \hat{s}_{7}^{2}$ has $G_{2}$ holonomy, it follows that the associative 3-form $\Phi_{(3)}$, which may be written as
$$\Phi_{(3)}=r^{2} d r \wedge J_{(2)}+r^{3} \rho_{(3)},$$
must be closed and co-closed. This has the consequences
$$d J_{(2)}=3 \rho_{(3)}, \quad d \tilde{\rho}_{(3)}+2 J_{(2)} \wedge J_{(2)}=0,$$
where $\tilde{\rho}_{(3)} \equiv *_{6} \rho_{(3)}$. Immediate further consequences of these equations are $J_{(2)} \wedge \rho_{(3)}=0$ and $d \rho_{(3)}=0$. The associativity relation
$$\Phi_{A B E} \Phi_{C D E}=\delta_{A C} \delta_{B D}-\delta_{A D} \delta_{B C}+\frac{1}{6} \epsilon_{A B C D E F G} \Phi_{E F G}$$
for the 3-form $\Phi_{(3)}$ has the consequences that
$$J_{a b} J_{b c}=-\delta_{a c}, \quad J_{a d} \rho_{a b d}=\tilde{\rho}_{a b c} .$$
This means that $J$ defines an almost complex structure in $d s_{6}^{2}$, and that with respect to $J$, $\psi_{(3)} \equiv \rho+\mathrm{i} \hat{\rho}$ is a holomorphic 3-form of type (3,0).

The relation to weak $S U(3)$ holonomy can be made more explicit by considering the covariantly-constant spinor $\hat{\eta}$ that exists in the $G_{2}$ metric (17). In the natural orthonormal basis $\hat{e}^{0}=d r, \hat{e}^{a}=r e^{a}$, one finds that the covariant exterior derivative $\hat{\nabla}=d+\frac{1}{4} \hat{\omega}_{A B} \Gamma^{A B}$ is given by $\hat{\nabla}=\nabla-\frac{1}{2} \Gamma_{0 a} e^{a}+d r \frac{\partial}{\partial r}$. If $d s_{6}^{2}$ has weak SU (3) holonomy then it admits Killing spinors $\eta_{ \pm}$satisfying $D_{a}^{ \pm} \eta_{ \pm} \equiv\left(\nabla_{a} \pm \frac{1}{2} \Gamma_{0 a}\right) \eta_{ \pm}=0$, for which the integrability condition is $\left[D_{a}^{ \pm}, D_{b}^{ \pm}\right]=\frac{1}{4} C_{a b c d} \Gamma^{c d}$. This admits solutions $\eta_{ \pm}$if $C_{a b c d} \Gamma^{c d}$ generates the $S U(3)$ subgroup of the tangent-space group $S O(6) \sim S U(4)$. The two spinors are related by $\eta_{ \pm}^{*}=\eta_{\mp}$, and $\Gamma_{0} \eta_{ \pm}=-\eta_{\mp}$. The covariantly constant spinor in the $G_{2}$ metric $d \hat{s}_{7}^{2}$ is given by $\hat{\eta}=\eta_{-}$.

In terms of the Killing spinors $\eta_{ \pm}$in $d s_{6}^{2}$, the almost complex structure $J_{(2)}$ and the 3-form $\rho_{(3)}$ are given by
$$J_{a b}=\mathrm{i} \eta_{+}^{\dagger} \Gamma_{a b} \eta_{-}, \quad \rho_{a b c}=\mathrm{i} \eta_{+}^{\dagger} \Gamma_{0 a b c} \eta_{-}$$
From the Killing spinor equations $D_{a}^{ \pm} \eta_{ \pm}=0$ one can now easily derive the equations
$$\nabla_{a} J_{b c}=\rho_{a b c}, \quad \nabla_{a} \tilde{\rho}_{b c d}=-3 J_{[a b} J_{c d]} .$$
These equations, which in particular imply (19), characterise nearly-Kähler metrics. Note that by symmetrising the first equation on $a$ and $b$, we obtain the equation for a Yano Killing tensor, $\nabla_{(a} J_{b) c}=0$ [24]. Thus the nearly Kähler 6-manifolds constructed in this paper provide new examples of a supersymmetric quantum mechanical systems with hidden symmetries [25, 26]. In fact, because $J_{a b}$ is an almost complex structure, the associated symmetric Staeckel Killing tensor is given by $J_{a b} J^{b}{ }_{c}=-g_{a c}$, and hence is trivial in this case.

\section*{$3 G_{2}$ holonomy equations for Bianchi IX base}

We now apply the formalism of section 2.1, with the four-dimensional base metric taken to be of the triaxial Bianchi IX form:
$$d s_{4}^{2}=d t^{2}+a_{i}^{2} \sigma_{i}^{2} .$$
The self-dual $S U(2)$ Yang-Mills connection is
$$A^{i}=-\omega_{0 i}-\frac{1}{2} \epsilon_{i j k} \omega_{j k},$$
where the spin connection of $d s_{4}^{2}$, in the vielbein basis $e^{0}=d t, e^{i}=a_{i} \sigma_{i}$, is given by
$$\omega_{01}=\beta_{1} e^{1}, \quad \omega_{23}=\gamma_{1} e^{1},$$
and cyclically, with
$$\beta_{1} \equiv-\frac{\dot{a}_{1}}{a_{1}}, \quad \gamma_{1} \equiv \frac{a_{1}^{2}-a_{2}^{2}-a_{3}^{2}}{2 a_{1} a_{2} a_{3}},$$
and cyclically. Since the Yang-Mills potentials are expressed in terms of the left-invariant 1-forms $\sigma_{i}$,
$$A^{i}=-a_{i}\left(\beta_{i}+\gamma_{i}\right) \sigma_{i},$$
the field strengths are necessarily $S U(2)$ invariant, and are given by
$$F^{i}=-\Theta_{0 i}-\epsilon_{i j k} \Theta_{j k} .$$

By imposing the closure and co-closure of $\Phi_{(3)}$ given by (10) (or equivalently, and more simply, (15)), we find that the first-order equations for $a_{i}$ such that the 7-manifold has $G_{2}$ holonomy are then given by
$$\begin{aligned}
\dot{a}_{1}-\dot{a}_{2} \dot{a}_{3}+ & \left(\frac{a_{3}^{2}-a_{1}^{2}-a_{2}^{2}}{2 a_{1} a_{2}}\right) \dot{a}_{2}+\left(\frac{a_{2}^{2}-a_{1}^{2}-a_{3}^{2}}{2 a_{1} a_{3}}\right) \dot{a}_{3} \\
& \quad+\frac{a_{2}^{4}+a_{3}^{4}-3 a_{1}^{4}+2\left(a_{1}^{2} a_{2}^{2}+a_{1}^{2} a_{3}^{2}-a_{2}^{2} a_{3}^{2}-\frac{2}{3} \Lambda a_{1}^{2} a_{2}^{2} a_{3}^{2}\right)}{4 a_{1}^{2} a_{2} a_{3}}=0,
\end{aligned}$$
together with the two equations obtained by cyclic permutation of the subscripts 1, 2 and 3. Note that we have restored the cosmological constant $\Lambda$, so that $d s_{4}^{2}$ satisfies $R_{a b}=\Lambda g_{a b}$. It is straightforward to see that after using the first-order equations, (29) becomes
$$F^{i}=-\frac{1}{3} \Lambda\left(e^{0} \wedge e^{i}+\frac{1}{2} \epsilon_{i j k} e^{j} \wedge e^{k}\right)=\frac{1}{3} \Lambda J^{i} .$$

We saw in in section 2 that the conditions for $d s_{7}^{2}$ in (9) to have $G_{2}$ holonomy should be equivalent to the conditions for $d s_{4}^{2}$ to have (anti)-self-dual Weyl tensor. In fact another way to derive the first-order equations (30) is as follows. We define the family of tensors
$$X_{a b c d} \equiv R_{a b c d}-\kappa\left(g_{a c} g_{b d}-g_{a d} g_{b c},\right.$$
where $\kappa$ is an as-yet unspecified constant parameter. If we now require that $X_{a b c d}$ be anti-self-dual, we obtain the equation
$${ }^{*} R_{a b c d}+R_{a b c d}-\kappa \epsilon_{a b c d}-\kappa\left(g_{a c} g_{b d}-g_{a d} g_{b d}\right)=0 .$$
Contraction with $g^{b d}$ gives $R_{a c}=3 \kappa g_{a c}$. It then follows that $X_{a b c d}$ is the Weyl-tensor of an Einstein metric with scalar curvature $12 \kappa$, and moreover that the Einstein manifold has anti-self-dual Weyl tensor. We find that the equations
$$X_{0123}=-X_{2323}, \quad X_{0231}=-X_{3131}, \quad X_{0312}=-X_{1212}$$
give precisely (30), and that the remaining anti-self-duality equations for $X_{a b c d}$, i.e.
$$X_{0101}=-X_{0123}, \quad X_{0202}=-X_{0231}, \quad X_{0303}=-X_{0312},$$
give second-order equations that are nothing but the derivatives of (30).
One could in principle solve (30) for the $\dot{a}_{i}$ themselves, but this involves finding the roots of a quintic equation. It is, nevertheless, useful to present the first-order equations in a factorised form. Solving two of the equations (30) for $\dot{a}_{2}$ and $\dot{a}_{3}$, and substituting into the third, we get
$$\begin{aligned}
& \left(\dot{a}_{1}-\frac{a_{1}^{2}-\left(a_{2}+a_{3}\right)^{2}}{2 a_{2} a_{3}}\right)^{2}\left(\dot{a}_{1}-\frac{a_{1}^{2}-\left(a_{2}-a_{3}\right)^{2}}{2 a_{2} a_{3}}\right)^{2}\left(\dot{a}_{1}-\frac{a_{1}^{2}-a_{2}^{2}-a_{3}^{2}}{2 a_{2} a_{3}}-\frac{1}{3} \Lambda a_{2} a_{3}\right) \\
& -\frac{1}{9} \Lambda^{2} a_{1}^{2} a_{2} a_{3}\left(2 a_{2} a_{3} \dot{a}_{1}+3 a_{2}^{2}+a_{3}^{2}-a_{1}^{2}\right)\left(2 a_{2} a_{3} \dot{a}_{1}+a_{2}^{2}+3 a_{3}^{2}-a_{1}^{2}\right)=0 .
\end{aligned}$$
Of course the two equations following by cyclic permutation hold too, but it would be misleading to think of these three as the equations for the $a_{i}$, since one should not solve them independently. Rather, we can view (36) itself as the equation for $\dot{a}_{1}$, and then substitute this solution back into the cyclic set defined by (30) in order to obtain the equations for $\dot{a}_{2}$ and $\dot{a}_{3}$.

It is interesting to observe that in the limit when $\Lambda \longrightarrow 0$, then from (36) and (30) we can see that we get either the "Atiyah-Hitchin" [27] first-order system ${ }^{2}$
$$\dot{a}_{1}=\frac{a_{1}^{2}-\left(a_{2}+a_{3}\right)^{2}}{2 a_{2} a_{3}}, \quad \text { and cyclic, }$$
or the "BGPP" [28] system
$$\dot{a}_{1}=\frac{a_{1}^{2}-a_{2}^{2}-a_{3}^{2}}{2 a_{2} a_{3}}, \quad \text { and cyclic } .$$

\footnotetext{
${ }^{2}$ Or an equivalent one with sign reversals of certain of the $a_{i}$ functions
}

The equations (37) admit the Atiyah-Hitchin [27] and self-dual Taub-NUT [29] metrics as particular solutions, whilst the equations (38) admit the BGPP [28] and Eguchi-Hanson [30] metrics as solutions.

It is often more convenient to recast first-order equations such as (30) into a form where the metric functions $\alpha_{i} \equiv a_{i}^{2}$ themselves appear without square roots. This can be achieved by introducing a new radial variable $\rho$, defined by $d t=a_{1} a_{2} a_{3} d \rho$. We then find that (30) becomes
$$\begin{aligned}
& 2 \frac{d \alpha_{1}}{d \rho}-\frac{1}{\alpha_{2} \alpha_{3}} \frac{d \alpha_{2}}{d \rho} \frac{d \alpha_{3}}{d \rho}+\frac{\left(\alpha_{3}-\alpha_{1}-\alpha_{2}\right)}{\alpha_{2}} \frac{d \alpha_{2}}{d \rho}+\frac{\left(\alpha_{2}-\alpha_{3}-\alpha_{1}\right)}{\alpha_{3}} \frac{d \alpha_{3}}{d \rho} \\
& +\alpha_{2}^{2}+\alpha_{3}^{2}-3 \alpha_{1}^{2}+2 \alpha_{1}\left(\alpha_{2}+\alpha_{3}\right)-2 \alpha_{2} \alpha_{3}-\frac{4}{3} \Lambda \alpha_{1} \alpha_{2} \alpha_{3}=0
\end{aligned}$$
and cyclically. Note also that in terms of the $\beta_{i}$ and $\gamma_{i}$ coefficients defined in (26) and (27), the first-order equations (30) can be written as
$$\left(\beta_{1}+\gamma_{1}\right)\left(\gamma_{2}+\gamma_{3}\right)=\left(\beta_{2}+\gamma_{2}\right)\left(\beta_{3}+\gamma_{3}\right)+\frac{1}{3} \Lambda,$$
and cyclically.
If we consider the specialisation where all three metric functions $a_{i}$ are set equal, $a_{i}=a$, the first-order system (30) reduces to
$$\dot{a}^{2}+\frac{1}{3} \Lambda a^{2}=\frac{1}{4} .$$
This gives
$$d s_{4}^{2}=d t^{2}+\frac{3}{4 \Lambda} \sin ^{2}\left(\sqrt{\frac{1}{3} \Lambda} t\right) \sigma_{i}^{2} .$$
The metric extends to a complete non-singular metric on $S^{4}$ if $\Lambda>0$, and to the hyperbolic space $H^{4}$ if $\Lambda<0$.

The specialisation to biaxial metrics, where two of the metric functions are set equal, is considerably more complicated. We shall study this in detail in the next section.

\section*{4 Biaxial anti-self-dual Bianchi IX metrics}

In this section we shall specialise to the biaxial case, setting $a_{2}=a_{1}$. The first-order equations (30) reduce to
$$\begin{aligned}
\dot{a}_{3} & =\dot{a}_{1}^{2}+\frac{\dot{a}_{1} a_{3}}{a_{1}}-1+\frac{3 a_{3}^{2}}{4 a_{1}^{2}}+\frac{1}{3} \Lambda a_{1}^{2}, \\
0 & =\left(2 a_{1} \dot{a}_{1}+a_{3}\right)\left(2 a_{1} \dot{a}_{1}+a_{3}-2 a_{1}\right)\left(2 a_{1} \dot{a}_{1}+a_{3}+2 a_{1}\right)+\frac{1}{6} \Lambda a_{1}\left(2 a_{1} \dot{a}_{1}+3 a_{3}\right) .
\end{aligned}$$

It is easy to see that if we take the limit where $\Lambda$ goes to zero, the cubic equation for $\dot{a}_{1}$ has roots giving
$$\dot{a}_{1}=-\frac{a_{3}}{2 a_{1}}+1, \quad \text { or } \quad \dot{a}_{1}=-\frac{a_{3}}{2 a_{1}}-1, \quad \text { or } \quad \dot{a}_{1}=-\frac{a_{3}}{2 a_{1}} .$$
The first two possibilities are associated with the first-order equations that yield the self-dual Ricci-flat Taub-NUT metrics, whilst the third yields the Eguchi-Hanson metric (which is also self-dual and Ricci-flat). In the self-dual Taub-NUT case, the $S O(3) \subset U(2)$ rotates the three hyper-Kähler forms as a triplet, while in the case of the Eguchi-Hanson metrics, they are singlets under $\operatorname{SO}(3)$.

For future reference, we note that the equations (43) imply that the Weyl tensor of $d s_{4}^{2}$ satisfies the relation
$$Y^{2}=X^{3},$$
where
$$X \equiv \frac{1}{24} C_{a b c d} C^{a b c d}, \quad Y \equiv \frac{1}{48} C_{a b c d} C^{c d e f} C_{e f}{ }^{a b}$$

\subsection*{4.1 Self-dual Taub-NUT-de Sitter metrics}

The general biaxial Bianchi IX Einstein metrics have long been known; these are the Taub-NUT-de Sitter solutions. Their local form can straightforwardly be derived by directly solving the Einstein equations in a suitable coordinate gauge. Writing (24) as
$$d s_{4}^{2}=\frac{d r^{2}}{a_{3}^{2}}+a_{1}^{2}\left(\sigma_{1}^{2}+\sigma_{2}^{2}\right)+a_{3}^{2} \sigma_{3}^{2}$$
the Ricci tensor is given (in the natural orthonormal frame) by
$$\begin{aligned}
& R_{00}=-a_{3} a_{3}^{\prime \prime}-a_{3}^{\prime 2}-\frac{2\left(a_{1}^{\prime} a_{3}^{\prime} a_{3}+a_{1}^{\prime \prime} a_{3}^{2}\right)}{a_{1}}, \\
& R_{11}=R_{22}=-\frac{a_{1}^{\prime \prime} a_{3}^{2}}{a_{1}}-\frac{a_{1}^{\prime 2} a_{3}^{2}}{a_{1}^{2}}-\frac{2 a_{1}^{\prime} a_{3}^{\prime} a_{3}}{a_{1}}-\frac{a_{3}^{2}}{2 a_{1}^{4}}+\frac{1}{a_{1}^{2}}, \\
& R_{33}=-a_{3} a_{3}^{\prime \prime}-a_{3}^{\prime 2}-\frac{2 a_{1}^{\prime} a_{3}^{\prime} a_{3}}{a_{1}}+\frac{a_{3}^{2}}{2 a_{1}^{4}} .
\end{aligned}$$
From this we see that $R_{00}-R_{33}=-a_{3}^{2}\left(a_{1}^{-4}+4 a_{1}^{\prime \prime} a_{1}^{-1}\right) / 2$, and since this must vanish by the Einstein condition, it is easy to solve for $a_{1}$, and hence, using the remaining Einstein equations, for $a_{3}$. Any Einstein solution to (48) is by definition a Taub-NUT-de Sitter metric. Apart from special limiting cases, the general solution has three parameters that we can think of as the mass $m$, the NUT charge $n$, and the cosmological constant $\Lambda$. This
general metric is given by ${ }^{3}$
$$d s_{4}^{2}=\frac{r^{2}-n^{2}}{\Delta} d r^{2}+\frac{4 n^{2} \Delta}{r^{2}-n^{2}} \sigma_{3}^{2}+\left(r^{2}-n^{2}\right)\left(\sigma_{1}^{2}+\sigma_{2}^{2}\right),$$
where
$$\Delta \equiv r^{2}-2 m r+n^{2}+\Lambda\left(n^{4}+2 n^{2} r^{2}-\frac{1}{3} r^{4}\right) .$$

The metric (49) has a self-dual or anti-self-dual Weyl tensor if [35]
$$m= \pm n\left(1+\frac{4}{3} \Lambda n^{2}\right),$$
in which case we find
$$\Delta=(r \mp n)^{2}\left(1-\frac{1}{3} \Lambda(r \mp n)(r \pm n)\right) .$$

Making the specific choice of the upper sign, we obtain the self-dual Taub-NUT-de Sitter metric
$$d s_{4}^{2}=\frac{d r^{2}}{F}+4 n^{2} F \sigma_{3}^{2}+\left(r^{2}-n^{2}\right)\left(\sigma_{1}^{2}+\sigma_{2}^{2}\right),$$
where
$$\begin{aligned}
F & =\left(\frac{r-n}{r+n}\right)\left(1-\frac{1}{3} \Lambda(r-n)(r+3 n)\right), \\
& =\frac{\Lambda}{3}\left(\frac{r-n}{r+n}\right)\left(r_{+}-r\right)\left(r-r_{-}\right), \quad r_{ \pm} \equiv-n \pm \sqrt{4 n^{2}+\frac{3}{\Lambda}} .
\end{aligned}$$
The Weyl tensor is given by
$$\begin{aligned}
& C_{0101}=C_{2323}=-C_{0123}=-\frac{n\left(1+\frac{1}{3} \Lambda n^{2}\right)}{(r+n)^{3}}, \\
& C_{0303}=C_{1212}=-C_{0312}=\frac{2 n\left(1+\frac{1}{3} \Lambda n^{2}\right)}{(r+n)^{3}} .
\end{aligned}$$

It can easily be verified that this metric satisfies the first-order equations (30). Note that because it is biaxial, and thus satisfies our reduced first-order system (43), it follows that the Weyl tensor of the self-dual Taub-NUT-de Sitter metrics obeys the relation (45). It is evident that if we send $\Lambda$ to zero in (53), we obtain the self-dual Taub-NUT metric first written down as a Euclidean-signature metric in [29]:
$$d s_{4}^{2}=\left(\frac{r+n}{r-n}\right) d r^{2}+4 n^{2}\left(\frac{r-n}{r+n}\right) \sigma_{3}^{2}+\left(r^{2}-n^{2}\right)\left(\sigma_{1}^{2}+\sigma_{2}^{2}\right) .$$

\footnotetext{
${ }^{3}$ The metric (49), parameterised by $m, n$ and $\Lambda$, covers an open dense set in the modulus space of solutions of (48). However, for special choices of relation between the parameters, it may be necessary to change the radial coordinate $r$ because (49) degenerates unless a limit is taken.
}

We saw, however, that the first-order equations (43) have three branches, and in the limit where $\Lambda$ goes to zero two of these should lead to the self-dual Taub-NUT metric, whilst the third should lead instead to the Eguchi-Hanson metric. As noted above, the metric form (49) with parameters $m, n$ and $\Lambda$, and radial coordinate $r$, does not necessarily cover all regions of the modulus space, and in the present case the existence of three branches suggests that there should exist a different parameterisation of biaxial self-dual Einstein metrics whose limiting form when $\Lambda$ goes to zero is the Eguchi-Hanson metric.

The required metrics cannot be the ones found in [35], which are referred to as the Eguchi-Hanson-de Sitter metrics,
$$d s_{4}^{2}=\frac{d r^{2}}{F}+\frac{1}{4} r^{2} F \sigma_{3}^{2}+\frac{1}{4} r^{2}\left(\sigma_{1}^{2}+\sigma_{2}^{2}\right),$$
where $F=1-\ell^{4} r^{-4}-\frac{1}{6} \Lambda r^{2}$, because these metrics have neither self-dual nor anti-self-dual Weyl tensor, when $\Lambda$ and $\ell$ are both non-zero, and thus they do not satisfy (30). They are in fact Einstein-Kähler, and the Weyl tensor has a definite duality only if $\ell=0$ (giving the Fubini-Study metric on $\mathbb{C P}^{2}$ if $\Lambda>0$, and the Bergmann metric on the open ball in $\mathbb{C}^{2}$ if $\Lambda<0$ ), or if $\Lambda=0$, in which case the Weyl tensor has the opposite duality and the metric is Eguchi-Hanson. ${ }^{4}$ In order to find the "missing" metrics, which we shall distinguish from (57) by giving them the name "self-dual Eguchi-Hanson-de Sitter," it is helpful to study the first-order equations (43) in greater detail. This forms the topic of the next subsection.

\subsection*{4.2 Biaxial first-order equations, and self-dual Eguchi-Hanson-de Sitter}

To proceed with studying the biaxial first-order equations (43), we define
$$u \equiv \dot{a}_{1}+\frac{a_{3}}{2 a_{1}} .$$
The cubic equation for $\dot{a}_{1}$ now becomes
$$3 u^{3}+\left(\Lambda a_{1}^{2}-3\right) u-\Lambda a_{1} a_{3}=0 .$$
One approach is to follow Cardano's procedure for solving the cubic equation, but other than establishing the principle that there will be two roots whose $\Lambda \longrightarrow 0$ limit yields the self-dual Taub-NUT first-order equation $u= \pm 1$, with the third yielding the Eguchi-Hanson first-order equation $u=0$ (see (44)), the direct solution of the cubic equation is not very enlightening.

\footnotetext{
${ }^{4}$ We shall discuss Bianchi IX Einstein-Kähler metrics briefly in appendix A.
}

A more profitable route is to view (59) as an equation expressing $a_{3}$ in terms of $u$,
$$a_{3}=-\frac{u\left(u^{2}+\lambda a_{1}^{2}-1\right)}{\lambda a_{1}} .$$
Note that we are defining
$$\lambda \equiv \frac{1}{3} \Lambda$$
for convenience. In view of (60), we can now choose to regard $\left(a_{1}, u\right)$ as our two metric functions, rather than $\left(a_{1}, a_{3}\right)$. From the first-order equations (43) we can now deduce that $a_{1}$ and $u$ satisfy the first-order equations
$$\dot{u}=-\lambda a_{1}, \quad \dot{a}_{1}=\frac{u\left(u^{2}+3 \lambda a_{1}^{2}-1\right)}{2 \lambda a_{1}^{2}} .$$

In order to find the solution that gives rise to Eguchi-Hanson in the $\lambda \equiv \frac{1}{3} \Lambda \longrightarrow 0$ limit, is useful to make a redefinition that casts the equations (62) and (60) into a form where this limit can be taken smoothly, and such that $u$ tends to zero in the limit. This is easily done, by letting $u=\lambda w$. The first-order equations (62) become
$$\dot{w}=-a_{1}, \quad \dot{a}_{1}=\frac{w\left(\lambda^{2} w^{2}+3 \lambda a_{1}^{2}-1\right)}{2 a_{1}^{2}},$$
and (60) gives
$$a_{3}=-\frac{w\left(\lambda^{2} w+3 \lambda a_{1}^{2}-1\right)}{a_{1}} .$$
It follows that the solution to (63) for general non-vanishing $\lambda$ will give the required self-dual Eguchi-Hanson-de Sitter metrics. By defining a new radial variable $x$ such that $d x=-a_{1} d t$, the equation for $w$ can be solved to give $w=x$, and hence the solution for $a_{1}$ can be found. After a further simple coordinate redefinition, the solution can be expressed as
$$d s_{4}^{2}=\frac{d \rho^{2}}{U V}+\frac{1}{4} \rho^{2} \frac{V}{1-2 \mu \ell^{2}}\left(\sigma_{1}^{2}+\sigma_{2}^{2}\right)+\frac{1}{4} \rho^{2}\left(\frac{1-\mu \ell^{2}}{1-2 \mu \ell^{2}}\right)^{2} U V \sigma_{3}^{2},$$
where
$$U \equiv 1-\frac{\ell^{4}}{\rho^{4}}, \quad V \equiv 1-\mu\left(\ell^{2}+\rho^{2}\right) .$$
The metric is Einstein, with cosmological constant $\Lambda=12 \mu$, and its Weyl tensor is anti-self-dual. In fact, we find that the tangent-frame components of the Weyl tensor are given by
$$\begin{aligned}
& C_{0101}=C_{2323}=-C_{0123}=-\frac{2 \ell^{4}\left(1-\mu \ell^{2}\right)}{\rho^{6}}, \\
& C_{0303}=C_{1212}=-C_{0312}=\frac{4 \ell^{4}\left(1-\mu \ell^{2}\right)}{\rho^{6}} .
\end{aligned}$$

Since (65) is Einstein and of biaxial Bianchi IX type, it must be contained within the general Taub-NUT-de Sitter class of solutions (49). Furthermore, since its Weyl tensor is anti-self-dual, it can be expected to lie within the subclass of (49) that satisfy (51). After simple algebra we find that there is indeed a transformation that maps (49) with the anti-self-dual specialisation given by (51) into (65), namely
$$r^{2}=-\frac{\left(12-\Lambda \ell^{2}-2 \Lambda \rho^{2}\right)^{2}}{32 \Lambda\left(6-\Lambda \ell^{2}\right)}, \quad n^{2}=-\frac{\left(12-\Lambda \ell^{2}\right)^{2}}{32 \Lambda\left(6-\Lambda \ell^{2}\right)} .$$
Substituting these redefinitions into (49) with (52), we recover (63). It should be noted that when $\Lambda \ell^{2}<6$, the self-dual Eguchi-Hanson-de Sitter metric corresponds to a section of the self-dual Taub-NUT-de Sitter metric in which the NUT parameter and radial coordinate are imaginary. Thus from the point of view of the real geometry, the self-dual Taub-NUT-de Sitter and self-dual Eguchi-Hanson-de Sitter metrics should be viewed as inequivalent.

In order to clarify the relations between the self-dual Taub-NUT-de Sitter and self-dual Eguchi-Hanson-de Sitter metrics, and more generally to investigate the full solution space of the self-dual biaxial metrics, it is useful to study the phase-plane for the first-order system (62). Before doing so, we shall close this subsection by showing where two well-known self-dual Einstein metrics that are contained within the biaxial Bianchi IX class fit in, namely $S^{4}$ and $\mathbb{C P}^{2}$.

Setting $\ell=0$ in (65) gives $S^{4}$, as can be seen by changing to the radial coordinate $t$ defined by $\sqrt{\mu} \rho=\sin \frac{1}{2} t$. This gives
$$d s_{4}^{2}=\frac{3}{\Lambda}\left(d t^{2}+\frac{1}{4} \sin ^{2} t \sigma_{i}^{2}\right) .$$
From (68), this corresponds to $n^{2}=-3 /(4 \Lambda)$ in the self-dual Taub-NUT-de Sitter parameterisation.

Another special case of (65), which arises when $\Lambda \ell^{2}=12$, also gives rise to $S^{4}$. This is a singular limit, for which we must first rescale the Euler angle $\psi$ that appears in $\sigma_{3}=$ $d \psi+\cos \theta d \phi$ according to $\psi=\left(1-\frac{1}{12} \Lambda \ell^{2}\right)^{-1} \tau$. Substituting into (65), and then sending $\ell^{2} \longrightarrow 12 / \Lambda$, we obtain
$$d s_{4}^{2}=\frac{3}{\Lambda}\left[d \chi^{2}+\sin ^{2} \chi\left(\sigma_{1}^{2}+\sigma_{2}^{2}\right)+\cos ^{2} \chi d \tau^{2}\right],$$
where we have also set $\Lambda \rho^{2}=12 \sin \chi$. We can recognise (70) as the metric on $S^{4}$, written as a foliation by $S^{2} \times S^{1}$ surfaces. The fact that (65) describes $S^{4}$ both for $\ell^{2}=0$ and $\ell^{2}=12 / \Lambda$ is not unexpected in view of the expressions (67), since the Weyl tensor can be seen to vanish for these two values of $\ell^{2}$. Note that from (68) the value of NUT parameter
in the self-dual Taub-NUT-de Sitter parameterisation corresponding to the $S^{4}$ limit with $\Lambda \ell^{2}=12$ is $n=0$.

A further special case of (65) is when $\Lambda \ell^{2}=6$. This gives $\mathbb{C P}^{2}$. One must first define a new radial coordinate, for example by setting $\rho^{2}=(2 \mu)^{-1}\left[1+\left(1-2 \mu \ell^{2}\right) \cos 2 \chi\right]$, before taking the limit. We then obtain the metric
$$d s_{4}^{2}=\frac{6}{\Lambda}\left[d \chi^{2}+\frac{1}{4} \sin ^{2} \chi\left(\sigma_{1}^{2}+\sigma_{2}^{2}\right)+\frac{1}{4} \sin ^{2} \chi \cos ^{2} \chi \sigma_{3}^{2}\right],$$
which can be recognised as the Fubini-Study metric on $\mathbb{C P}^{2}$ [35]. From (68), it corresponds, in the self-dual Taub-NUT-de Sitter parameterisation, to sending the NUT parameter $n$ to infinity. Note that with the conventions of this paper, the Weyl tensor is anti-self-dual, as is the (covariantly constant) Kähler form $J=e^{0} \wedge e^{3}-e^{1} \wedge e^{2}$. Of course none of the self-dual quaternionic Kähler forms $J^{i}$ is covariantly constant, since the right-handed $S U(2)$ part of the spin connection is non-vanishing.

\subsection*{4.3 Phase-plane analysis for the biaxial system}

As we have seen above, finding a uniform parameterisation of the space of solutions, even in the biaxial case, is non-trivial. The approach taken in this section will be to classify all the possible orbits in the phase space of the first-order equations (62). We shall find that not all solutions can be parameterised by giving real and finite values of $\ell$, or $n$.

We begin by making the definition $v=3 a_{1}$, choosing the scale size $\lambda=3$ for convenience, and sending $t \longrightarrow-t$ for inconvenience. The first-order equations (62) become
$$\dot{u}=v, \quad \dot{v}=\frac{9 u\left(1-u^{2}-v^{2}\right)}{2 v^{2}},$$
and so the solutions can be represented as flows in the $(u, v)$ plane. We can divide the two equations to get
$$\frac{d v}{d u}=\frac{9 u\left(1-u^{2}-v^{2}\right)}{2 v^{3}} .$$

In general, equation (73) can be integrated to give the flows for any biaxial self-dual solution. The constant of integration is related to the NUT parameter $n$, or, equivalently, the scale parameter $\ell$ in the self-dual Eguchi-Hanson-de Sitter formulation. In terms of $n$, the integral of (73) is given by
$$\left(u^{2}+\frac{1}{3} v^{2}-1\right)^{2}=12 n^{2}\left(u^{2}+\frac{2}{3} v^{2}-1\right) .$$
Since this is symmetrical under reflections in the $u$ and $v$ axes, it suffices to consider flows within the positive quadrant.

It follows from (73) that flow lines inside the unit circle have positive gradient, whilst those outside the unit circle have negative gradient. The $v$ axis corresponds to $a_{3}=0$, signifying an endpoint of the metric at which the 3-dimensional orbits degenerate to an $S^{2}$ bolt. The $u$ axis, on the other hand, corresponds to $a_{1}=0$, and the metric will be singular here unless it happens that $u= \pm 1$ or $u=0$, in which case the orbits degenerate to a point, implying a NUT endpoint in the metric. By a theorem of Hitchin's, the only complete and non-singular metrics with positive $\Lambda$ are $S^{4}$ and $\mathbb{C P}^{2}$.

It is straightforward to establish that the $\mathbb{C P}^{2}$ solution (71) corresponds to the ellipse $u^{2}+\frac{2}{3} v^{2}=1$. The flow starts on the $v$ axis at $v^{2}=\frac{3}{2}$ at a bolt, and runs along the ellipse to a NUT on the $u$ axis at $u=1$. Since we have chosen the normalisation $\mu=\frac{1}{12} \Lambda=\frac{1}{4} \lambda=\frac{3}{4}$ in this subsection, it follows that this occurs for $\ell^{2}=\frac{2}{3}$.

The $S^{4}$ solution (69) with $\ell^{2}=0$ corresponds to the ellipse $\left(u-\frac{1}{2}\right)^{2}+\frac{1}{3} v^{2}=\frac{1}{4}$. This runs from the NUT at $u=0, v=0$ to the NUT at $u=1, v=0$. The other $S^{4}$ solution (70), with $\ell^{2}=12 / \Lambda=4 / 3$, corresponds to the ellipse $u^{2}+\frac{1}{3} v^{2}=1$. Although this appears to be singular since, from (60), we have $a_{3}=0$, we saw that to obtain (70) it was necessary to rescale the $\psi$ coordinate and this has the effect of compensating for the vanishing of $a_{3}$.

The phase-plane plot, with the various ellipses and unit circle mentioned above displayed, is given in Figure 1.

From (74), we see that solutions starting from a bolt on the $v$ axis are specified at $u=0$ by
$$\begin{array}{llc}
\text { Region A : } & -\infty<n^{2}<-\frac{1}{12}: & \frac{3}{2}>v^{2}>0, \\
\text { Region B : } & -\infty<n<0: & \frac{3}{2}<v^{2}<3, \\
\text { Region C : } & 0<n<\infty: & 3<v^{2}<\infty .
\end{array}$$
We also have solutions starting from the singular curvature singularity along the $u$ axis, specified at $v=0$ by:
$$\text { Region D: } \quad-\frac{1}{12}<n^{2}<0: \quad 0<u<1 .$$
In terms of the parameter $\ell^{2}$ of the self-dual Eguchi-Hanson-de Sitter formulation of the metrics, we see from (68) that Region A, where $n$ is imaginary, is covered by real values of $\ell$, and so the self-dual Eguchi-Hanson-de Sitter form of the metrics is better adapted to describing this region of the phase plane. On the other hand, in Region D, where $n$ is again imaginary, $\ell$ is complex, and so neither the self-dual Taub-NUT-de Sitter nor self-dual

Eguchi-Hanson-de Sitter formulation is well adapted to describing this region of the phase plane. It is straightforward to find an adapted parameterisation where the analogue of the NUT parameter, and the radial coordinate, is real in Region D, but since the metrics there have power-law curvature singularities there is not much value in writing them down.

It is instructive to express the Weyl tensor for the biaxial self-dual metrics in terms of $u$ and $v$. We find that it is given by
$$C_{0101}=-C_{0123}=C_{2323}=-2 C_{0303}=2 C_{0312}=-2 C_{1212}=f,$$
where
$$f=-\frac{81}{2} v^{-6}\left(u^{2}+\frac{1}{3} v^{2}-1\right)\left(\left(u-\frac{1}{2}\right)^{2}+\frac{1}{3} v^{2}-\frac{1}{4}\right)\left(\left(u+\frac{1}{2}\right)^{2}+\frac{1}{3} v^{2}-\frac{1}{4}\right) .$$
As expected, this vanishes only on the $S^{4}$ ellipses, and it diverges everywhere on the $u$ axis except at the points $u=0, \pm 1$, provided they are approached along the $S^{4}$ flows.

\subsection*{4.4 Global structure of the biaxial solutions}

As we have already remarked, a theorem of Hitchin's implies that when the cosmological constant $\Lambda$ is positive, only the $S^{4}$ and $\mathbb{C P}^{2}$ self-dual Einstein metrics can be non-singular. In particular, therefore, this means that the self-dual Taub-NUT-de Sitter and self-dual Eguchi-Hanson-de Sitter metrics will be singular except for the special values of $n$ or $\ell^{2}$ for which they reduce to $S^{4}$ or $\mathbb{C P}^{2}$.

We shall analyse the self-dual Taub-NUT-de Sitter metrics first, described by (53) and (54). The coordinate $r$ is taken to lie in the interval $n \leq r \leq r_{+}$. For convenience, we shall again set $\Lambda=9$ here. Near $r=n$, letting $r-n=\rho^{2}$, the metric becomes
$$d s_{4}^{2} \sim 8 n\left[d \rho^{2}+\frac{1}{4} \rho^{2}\left(\sigma_{1}^{2}+\sigma_{2}^{2}+\sigma_{3}^{2}\right)\right],$$
which describes a NUT. The metric smoothly approaches the origin of $\mathbb{R}^{4}$, provided that the Euler angle $\psi$ appearing in $\sigma_{3}=d \psi+\cos \theta d \phi$ has its canonical period $4 \pi$.

Near $r=r_{+}$, by letting $r_{+}-r=\rho^{2}$ we see that the metric becomes
$$d s_{4}^{2} \sim \frac{2}{\left(\sqrt{3} \sqrt{12 n^{2}+1}-6 n\right)}\left(d \rho^{2}+4 n^{2}\left(\sqrt{3} \sqrt{12 n^{2}+1}-6 n\right)^{2} \rho^{2} \sigma_{3}^{2}\right)+\left(r_{+}^{2}-n^{2}\right)\left(\sigma_{1}^{2}+\sigma_{2}^{2}\right) .$$
This approaches $\mathbb{R}^{2} \times S^{2}$ locally, but in general there will be a conical singularity. If $\psi$ has period $\Delta \psi=4 \pi / N$, then regularity at $r=r_{+}$is achieved if
$$N=4 n\left(-6 n+\sqrt{3} \sqrt{12 n^{2}+1}\right) .$$

Regularity at $r=n$ required $N=1$. This is compatible with (80) if $n=\infty$, which is the limit where the self-dual Taub-NUT-de Sitter metric becomes $\mathbb{C P}^{2}$ [35]. (Another case where the singularity can be avoided is by taking a limit where $n^{2} \longrightarrow-3 /(4 \Lambda)=-\frac{1}{12}$, in which case one must first rescale coordinates in the metric. This case is $S^{4}$.) For all other values of $n$, there will be a deficit angle at the origin, and a hence a conical singularity.

The $G_{2}$ metrics (9) obtained by taking $d s_{4}^{2}$ to be self-dual Taub-NUT-de Sitter were discussed recently in [10]. They have cohomogeneity 2, since there are two "radial" coordinates $\rho$ and $t$. The conical singularities in the Taub-NUT-de Sitter metrics imply, of course, that the corresponding $G_{2}$ metrics will have conical singularities too.

A further class of geometries within the biaxial Bianchi IX class is obtained by considering instead the self-dual Eguchi-Hanson-de Sitter form of the metrics, given by (65). If $2 \mu \ell^{2}<1$, meaning that $\Lambda \ell^{2}<6$, the radial coordinate $\rho$ can be chosen to lie in the interval $\ell \leq \rho \leq \rho_{0}$, where $\rho_{0}^{2}=1 / \mu-\ell^{2}$. Near $\rho=\ell$, setting $\rho=\ell+x^{2}$, we find
$$d s_{4}^{2} \sim \frac{\ell}{1-2 \mu \ell^{2}}\left[d x^{2}+\left(1-\mu \ell^{2}\right)^{2} x^{2} \sigma_{3}^{2}\right]+\frac{1}{4} \ell^{2}\left(\sigma_{1}^{2}+\sigma_{2}^{2}\right),$$
whilst near $\rho=\rho_{0}$, we have, setting $\rho=\rho_{0}-x^{2}$,
$$d s_{4}^{2} \sim \frac{1-\mu \ell^{2}}{1-2 \mu \ell^{2}}\left(d x^{2}+\frac{1}{4} x^{2} \sigma_{i}^{2}\right) .$$
Thus regularity at the NUT at $\rho=\rho_{0}$ requires that $\psi$ have period $4 \pi$, which implies that there is a conical singularity on the bolt at $\rho=\ell$.

\subsection*{4.5 Phase plane and global structure for negative $\Lambda$}

The phase-plane analysis of section 4.3 can be repeated for the case where the cosmological constant $\Lambda$ is taken to be negative. Starting from (62) and (60), and fixing the scale by choosing $\lambda \equiv \frac{1}{3} \Lambda=-3$, we now have
$$\begin{aligned}
& \dot{u}=v, \quad \dot{v}=\frac{9 u\left(1-u^{2}+v^{2}\right)}{2 v^{2}}, \\
& \frac{d v}{d u}=\frac{9 u\left(1-u^{2}+v^{2}\right)}{2 v^{3}}, \\
& a_{3}=-\frac{u}{v}\left(1-u^{2}+\frac{1}{3} v^{2}\right) .
\end{aligned}$$

The flow can be integrated, giving
$$\left(u^{2}-\frac{1}{3} v^{2}-1\right)^{2}+12 n^{2}\left(u^{2}-\frac{2}{3} v^{2}-1\right)=0 .$$
As in the case when $\Lambda>0$, this is symmetric under reflections in the $u$ and $v$ axes. The hyperbola $u^{2}-\frac{2}{3} v^{2}=1$, which arises when $n=\infty$, corresponds to the Bergmann
metric on the open ball in $\mathbb{C}^{2}$ (i.e. the Fubini-Study metric with negative $\Lambda$, which is the coset $S U(2,1) / U(2)$ ). The hyperbolic 4-space $H^{4}$ arises if $n=0$, giving the hyperbola $u^{2}-\frac{1}{3} v^{2}=1$. It also arises if $n^{2}=\frac{1}{12}$, giving the hyperbolae $\left(u \pm \frac{1}{2}\right)^{2}-\frac{1}{3} v^{2}=\frac{1}{4}$.

The Weyl tensor is given by (76), where $f$ is now given by
$$f=\frac{81}{2} v^{-6}\left(u^{2}-\frac{1}{3} v^{2}-1\right)\left(\left(u-\frac{1}{2}\right)^{2}-\frac{1}{3} v^{2}-\frac{1}{4}\right)\left(\left(u+\frac{1}{2}\right)^{2}-\frac{1}{3} v^{2}-\frac{1}{4}\right) .$$
The Weyl tensor therefore vanishes on the $H^{4}$ hyperbolae, and has a power-law divergence at all points on the $u$ axis except if one approaches $u=0, \pm 1$ along the $H^{4}$ flows.

Writing the metric in the self-dual Eguchi-Hanson-de Sitter form (65), where now $\mu \equiv$ $\frac{1}{12} \Lambda$ is taken to be negative, say $-\mu \equiv \nu>0$, we see that the radial variable can be taken in the range $\rho \geq \ell$. Near $\rho=\ell$ we set $\rho=\ell+x^{2}$, giving
$$d s_{4}^{2} \sim \frac{\ell}{1+2 \nu \ell^{2}}\left[d x^{2}+\left(1+\nu \ell^{2}\right)^{2} x^{2} \sigma_{3}^{2}\right]+\frac{1}{4} \ell^{2}\left(\sigma_{1}^{2}+\sigma_{2}^{2}\right) .$$
Thus we have a regular $S^{2}$ bolt, provided that the period $\Delta \psi$ of $\psi$ is chosen to be
$$\Delta \psi=\frac{2 \pi}{1+\nu \ell^{2}} .$$
Provided that $\ell$ is such that this period is $4 N$, for $N$ an integer, we shall have a regular metric, with $S^{3} / Z_{N}$ orbits.

Now consider instead writing the metric in the self-dual Taub-NUT-de Sitter form (53). Taking $\Lambda=-9$ for simplicity, the roots $r_{ \pm}$are given by $r_{ \pm}=-n \pm \frac{1}{\sqrt{3}} \sqrt{12 n^{2}-1}$. Assuming $n^{2}>\frac{1}{12}$, this means that the roots $r_{ \pm}$are both less than $n$ (assumed positive), and so we can take $r \geq n$. Near $r=n$ we set $r=n+x^{2}$, finding
$$d s_{4}^{2} \sim 8 n\left(d x^{2}+\frac{1}{4} x^{2} \sigma_{i}^{2}\right) .$$
Thus $r=n$ is a regular NUT, provided $\psi$ has period $4 \pi$.
The regular solutions with a bolt, which we described in the self-dual Eguchi-Hanson-de Sitter form (65) above, can also be expressed in the self-dual Taub-NUT-de Sitter form. They correspond to running the radial coordinate $r$ from $r=r_{-}$to $r=-\infty$ (note that $r_{-}<-n$, so the curvature singularity at $r=-n$ is avoided).

All the other solutions represented in Figure 2 have flows that intersect the $u$ axis at points other than $u=0$ or ±1, and thus they have power-law curvature singularities.

\subsection*{4.6 Superpotential for the biaxial system}

Although the $D=4$ self-dual Einstein spaces do not themselves have special holonomy, the existence of the first-order system implies that it might be possible to derive it from a superpotential. To obtain such a superpotential, we first notice that the Hamiltonian of the cohomogeneity one Einstein space is given by $H=T+U$, where
$$\begin{aligned}
T & =\frac{2 a_{1}^{\prime} a_{2}^{\prime}}{a_{1} a_{2}}+\frac{2 a_{1}^{\prime} a_{3}^{\prime}}{a_{1} a_{3}}+\frac{2 a_{2}^{\prime} a_{3}^{\prime}}{a_{2} a_{3}} \\
U & =\frac{1}{2}\left(a_{1}^{4}+a_{2}^{4}+a_{3}^{4}-2 a_{1}^{2} a_{2}^{2}-2 a_{1}^{2} a_{3}^{2}-2 a_{2}^{2} a_{3}^{2}+12 \lambda a_{1}^{2} a_{2}^{2} a_{3}^{2}\right),
\end{aligned}$$
and a prime denotes a derivative with respect to $\eta$ defined by $d t=a_{1} a_{2} a_{3} d \eta$.
Here, we shall consider the biaxial system with $a_{2}=a_{1}$, and use the $u$ and $a_{1}$ variables defined in section 4.2. We can write $T=\frac{1}{2} g_{i j}\left(d \alpha^{i} / d \eta\right)\left(d \alpha^{j} / d \eta\right)$, with $\alpha_{i}=\left(a_{1}, u\right)$, which implies that $g_{i j}$ is given by
$$\begin{aligned}
g_{i j} & =\left(\begin{array}{cc}
\frac{4 x}{a_{1}^{2} y} & \frac{4 z}{a_{1} u y} \\
\frac{4 z}{a_{1} u y} & 0
\end{array}\right), \\
x & \equiv 1+3 \lambda a_{1}^{2}-u^{2}, \quad y \equiv-1+\lambda a_{1}^{2}+u^{2}, \quad z \equiv-1+\lambda a_{1}^{2}+3 u^{2} .
\end{aligned}$$
We find that the potential $U$ can then expressed as $U=-\frac{1}{2} g^{i j}\left(\partial W / \partial \alpha_{i}\right)\left(\partial W / \partial \alpha_{j}\right)$, with the superpotential $W$ given by
$$W=-\frac{u^{2}\left(u^{2}-1\right)^{2}}{\lambda^{2} a_{1}^{2}}-\frac{u^{2}\left(5 u^{2}-4\right)}{\lambda}-a_{1}^{2}\left(3 u^{2}+2\right)+\lambda a_{1}^{4} .$$
It is straightforward to derive the first order equations from this superpotential.

\section*{5 Triaxial anti-self-dual Bianchi IX metrics}

In this section we discuss the full triaxial system of equations, which are considerably more complicated than the biaxial case.

\subsection*{5.1 Phase-plane and superpotential for triaxial system}

We begin with an outline of a phase-plane analysis for the triaxial system, using methods similar to those that we used for the biaxial case.

Starting from the first-order equation for $\dot{a}_{1}$ obtained in (36), it is natural to define the auxiliary variable $w$, by
$$w \equiv \dot{a}_{1}-\frac{a_{1}^{2}-a_{2}^{2}-a_{3}^{2}}{2 a_{2} a_{3}} .$$

In terms of $w$, equation (36) becomes
$$\left(w^{2}-1\right)^{2}\left(w-\lambda a_{2} a_{3}\right)-\lambda^{2} a_{1}^{2}\left(a_{2} w+a_{3}\right)\left(a_{3} w+a_{2}\right)=0 .$$
The remaining first-order equations in (30), namely those for $\dot{a}_{2}$ and $\dot{a}_{3}$, then become
$$\begin{aligned}
& \dot{a}_{2}=\frac{a_{2}^{2}-a_{1}^{2}-a_{3}^{2}}{2 a_{1} a_{3}}-\frac{\lambda a_{1}\left(a_{2} w+a_{3}\right)}{w^{2}-1}, \\
& \dot{a}_{3}=\frac{a_{3}^{2}-a_{1}^{2}-a_{2}^{2}}{2 a_{1} a_{2}}-\frac{\lambda a_{1}\left(a_{3} w+a_{2}\right)}{w^{2}-1} .
\end{aligned}$$

We can now try following the strategy of treating $\left(w, a_{2}, a_{3}\right)$ as the independent variables, instead of $\left(a_{1}, a_{2}, a_{3}\right)$. This is similar to the strategy used in the biaxial case, although not exactly parallel. Differentiating (93), using (94) and (92), and then using (93) itself to substitute for $a_{1}^{2}$, we get
$$\begin{aligned}
\left(\dot{w}+\lambda a_{1}\right)\left(w^{2}\right. & -1)^{2}\left[a_{2} a_{3}\left(3 w^{4}+6 w^{2}-1\right)-4\left(a_{2}^{2}+a_{3}^{2}\right) w^{3}\right. \\
& \left.-\lambda a_{2} a_{3}\left(\left(a_{2}^{2}+a_{3}^{2}\right)\left(1+3 w^{2}\right)+2 a_{2} a_{3} w\left(w^{2}+3\right)\right)\right]=0 .
\end{aligned}$$
Unless the algebraic expression contained in square brackets vanishes, we therefore have the first-order equation
$$\dot{w}=-\lambda a_{1} .$$
We should think of $a_{1}$ as being solved for here, using (93). Since this would involve the use of square roots, it seems preferable to introduce a new radial variable $\rho$, defined by $d \rho=-a_{1} d t$. We then have
$$w^{\prime}=\lambda .$$
The remaining first-order equations (94) will also involve $a_{1}$ only through $a_{1}^{2}$, and so we shall have the system
$$\begin{aligned}
w^{\prime} & =\lambda, \\
a_{2}^{\prime} & =-\frac{a_{2}^{2}-a_{1}^{2}-a_{3}^{2}}{2 a_{1}^{2} a_{3}}+\frac{\lambda\left(a_{2} w+a_{3}\right)}{w^{2}-1}, \\
a_{3}^{\prime} & =-\frac{a_{3}^{2}-a_{1}^{2}-a_{2}^{2}}{2 a_{1}^{2} a_{2}}+\frac{\lambda\left(a_{3} w+a_{2}\right)}{w^{2}-1},
\end{aligned}$$
where from (93), $a_{1}^{2}$ is given by
$$a_{1}^{2}=\frac{\left(w^{2}-1\right)^{2}\left(w-\lambda a_{2} a_{3}\right)}{\lambda^{2}\left(a_{2} w+a_{3}\right)\left(a_{3} w+a_{2}\right)} .$$

Analogously to the biaxial case, we see from (93) that when $\lambda=0$ we have $w=0$ corresponding to the "BGPP" first-order equations, and $w= \pm 1$ corresponding to the "Atiyah-Hitchin" first-order equations.

The problem of solving the general triaxial first-order equations can be reduced to a second-order equation in a single variable. Defining $y \equiv a_{2} / a_{3}$ and $z \equiv a_{2} a_{3}$, we find, after normalising so that $\lambda=1$, that $y$ satisfies the equation
$$y^{\prime \prime}-\frac{3 y^{2}-2 \rho y+1}{y\left(y^{2}-1\right)} y^{\prime 2}-\frac{2 \rho y^{2}-3 \rho^{2} y-y+2 \rho}{\rho\left(\rho^{2}-1\right) y} y^{\prime}+\frac{2\left(y^{2}-1\right)}{\rho\left(\rho^{2}-1\right)^{2}}=0,$$
and that $z$ is given by
$$z=\frac{\rho\left(\rho^{2}-1\right) y\left[\left(\rho^{2}-1\right) y^{\prime}+1-y^{2}\right]}{\left(\rho^{2}-1\right)^{2} y y^{\prime}+\rho\left(y^{4}-1\right)+2 y^{2}\left(y^{2}-1\right)} .$$

We find that it is possible to derive the triaxial first-order system from a superpotential also. We use $\alpha_{i}=\left(u, a_{2}, a_{3}\right)$ as variables, as discussed above. The kinetic energy $T$ given in (89) can be straightforwardly rewritten in terms of derivatives of $\left(u, a_{2}, a_{3}\right)$, and hence we can read off the components of the sigma-model metric $g_{i j}$ in $T=\frac{1}{2} g_{i j}\left(d \alpha^{i} / d \eta\right)\left(d \alpha^{j} / d \eta\right)$, where as before $d t=a_{1} a_{2} a_{3} d \eta$. Since the expression for $g_{i j}$ is quite complicated, we shall not present it here. Then, we find after some calculation that the potential $U$ given in (89) can be written in terms of a superpotential $W$ as $U=-\frac{1}{2} g^{i j}\left(\partial W / \partial \alpha^{i}\right)\left(\partial W / \partial \alpha^{j}\right)$, with
$$W=-a_{2}^{2}-a_{3}^{2}-2 \lambda^{-1} w^{2}+\frac{a_{2} a_{3}\left(3 w^{2}-1\right)}{w}+\frac{\left(\lambda^{2} a_{2}^{2} a_{3}^{2}-w^{2}\right)\left(w^{2}-1\right)^{2}}{\lambda^{2} w\left(a_{2} w+a_{3}\right)\left(a_{3} w+a_{2}\right)} .$$

It is easily verified that if one sets $a_{2}=a_{1}$, then $w$ reduces to the function $u$ of the biaxial system, and, after using (60) to replace $a_{3}$ by $u$, then $W+\lambda^{-1}$ becomes the biaxial superpotential given in (91), where $W$ denotes the triaxial superpotential (102) after the biaxial specialisations.

\subsection*{5.2 The Tod-Hitchin first-order system}

In this section we shall follow Tod [21] and Hitchin [22, 23], who use a different approach to study the general triaxial system (30). The metric is written as
$$d s_{4}^{2}=F\left(\frac{d x^{2}}{x(1-x)}+\frac{\sigma_{1}^{2}}{\Omega_{1}^{2}}+\frac{(1-x) \sigma_{2}^{2}}{\Omega_{2}^{2}}+\frac{x \sigma_{3}^{2}}{\Omega_{3}^{2}}\right) .$$
Tod [21] shows that $d s_{4}^{2}$ is Einstein with anti-self-dual Weyl tensor if the functions $\Omega_{i}$ satisfy
$$\Omega_{1}^{\prime}=-\frac{\Omega_{2} \Omega_{3}}{x(1-x)}, \quad \Omega_{2}^{\prime}=-\frac{\Omega_{3} \Omega_{1}}{x}, \quad \Omega_{3}^{\prime}=-\frac{\Omega_{1} \Omega_{2}}{1-x},$$
where a prime denotes a derivative with respect to $x$, and $F$ is given by
$$F=-\frac{8 x \Omega_{1}^{2} \Omega_{2}^{2} \Omega_{3}^{2}+2 \Omega_{1} \Omega_{2} \Omega_{3}\left[x\left(\Omega_{1}^{2}+\Omega_{2}^{2}\right)-\left(1-4 \Omega_{3}^{2}\right)\left(\Omega_{2}^{2}-(1-x) \Omega_{1}^{2}\right)\right]}{4\left(x \Omega_{1} \Omega_{2}+2 \Omega_{3}\left(\Omega_{2}^{2}-(1-x) \Omega_{1}^{2}\right)\right)^{2}} .$$
(We have normalised the Einstein constant so that $R_{a b}=3 g_{a b}$.)
This first-order system can be reduced to the problem of solving the Painlevé VI equation [21]. One introduces a function $y(x)$, in terms of which the $\Omega_{i}^{2}$ are written as
$$\begin{aligned}
\Omega_{1}^{2} & =\frac{(y-x)^{2} y(y-1)}{x(1-x)}\left(z-\frac{1}{2(y-1)}\right)\left(z-\frac{1}{2 y}\right), \\
\Omega_{2}^{2} & =\frac{y^{2}(y-1)(y-x)}{x}\left(z-\frac{1}{2(y-x)}\right)\left(z-\frac{1}{2(y-1)}\right), \\
\Omega_{3}^{2} & =\frac{(y-1)^{2} y(y-x)}{(1-x)}\left(z-\frac{1}{2 y}\right)\left(z-\frac{1}{2(y-x)}\right),
\end{aligned}$$
where
$$z=\frac{x-2 x y+y^{2}-2 x(1-x) y^{\prime}}{4 y(y-1)(y-x)} .$$
(Note that $\Omega_{1}^{2}-\Omega_{2}^{2}-\Omega_{3}^{2}$, which is conserved, must take the value $-\frac{1}{4}$ in order that $d s_{4}^{2}$ be Einstein.) The claim then is that the first-order equations are satisfied if $y$ satisfies the Painlevé VI equation
$$\begin{aligned}
y^{\prime \prime}= & \frac{1}{2}\left(\frac{1}{y}+\frac{1}{y-1}+\frac{1}{y-x}\right) y^{\prime 2}-\left(\frac{1}{x}+\frac{1}{x-1}+\frac{1}{y-x}\right) y^{\prime} \\
& +\frac{y(y-1)(y-x)}{x^{2}(x-1)^{2}}\left(\alpha+\beta \frac{x}{y^{2}}+\gamma \frac{x-1}{(y-1)^{2}}+\delta \frac{x(x-1)}{(y-x)^{2}}\right),
\end{aligned}$$
with $(\alpha, \beta, \gamma, \delta)=\left(\frac{1}{8},-\frac{1}{8}, \frac{1}{8}, \frac{3}{8}\right)$. Note that the expression (105) for $F$ is actually quite simple, expressed in terms of $y$ :
$$\begin{aligned}
F & =\frac{y(1-y)(y-x) z}{2 x(1-x)} \\
& =\frac{x-2 x y+y^{2}-2 x(1-x) y^{\prime}}{8 x(1-x)} .
\end{aligned}$$

It is a straightforward, although somewhat involved, exercise to show that if the first-order equations (104) are satisfied, then the metric functions $a_{i}$ indeed satisfy our first-order equations (30). Note, however, that the converse is not true; not every solution of the general first-order equations (30) for anti-self-dual Einstein metrics gives a solution of (104). For example, the uniaxial solutions certainly do not satisfy the equations (104); setting the $a_{i}^{2}$ equal implies that $\Omega_{2}^{2}=(1-x) \Omega_{1}^{2}$ and $\Omega_{3}^{2}=x \Omega_{1}^{2}$, and one can easily see that substituting into (104) leads to a contradiction. Likewise, one can show that setting any two of the metric functions equal leads to a degeneration in (104). This can be understood from the fact that the radial coordinate used in [21, 22] becomes a constant if any two of the metric functions are set equal.

The first-order equations (104) were obtained in [21, 22, 23] by first solving the conditions for metrics with anti-self-dual Weyl tensor and vanishing Ricci scalar, and then performing
a conformal rescaling of the metric to arrive at one that was Einstein. We have shown that every solution of the Tod-Hitchin system provides a solution of our system of first-order equations. Our equations are valid not only for the triaxial case but also for the biaxial and uniaxial cases, and yield all possible Bianchi IX self-dual Einstein metrics. The method of Tod and Hitchin breaks down in the biaxial and uniaxial cases. The arguments from twistor theory presented in [23] show that the Tod-Hitchin method gives the general triaxial metric, but the explicit correspondence to our first-order equations remains unclear.

\subsection*{5.3 Explicit examples}

Hitchin gives explicit solutions to (108) characterised by an integer $k$, with $k=3,4,6,8$ [22, 23]. The case $k=3$ corresponds to the round metric on $S^{4}$, written in triaxial form [32], whilst $k=4$ corresponds to the Fubini-Study metric on $\mathbb{C P}^{2}$, again written in triaxial form [38]. ${ }^{5}$ For $k \geq 5$ the metrics will necessarily have orbifold-type singularities.

In general it is easiest to give these solutions $y(x)$ by introducing a "parametric variable" $r$, with $y$ and $x$ both expressed in terms of $r$. Thus one has:
$$\begin{array}{ll}
k=3: & y=\frac{r^{2}\left(2 r^{2}+5 r+2\right)}{(2 r+1)\left(r^{2}+r+1\right)}, \quad x=\frac{r^{3}(r+2)}{2 r+1}, \\
k=4: & y=r, \quad x=r^{2}, \\
k=6: & y=\frac{r\left(r^{2}+r+1\right)}{(2 r+1)}, \quad x=\frac{r^{3}(r+2)}{(2 r+1)}, \\
k=8: & \frac{4 r\left(3 r^{2}-2 r+1\right)}{(r+1)(1-r)^{3}\left(r^{2}+2 r+3\right)}, \quad x=\left(\frac{2 r}{1-r^{2}}\right)^{4} .
\end{array}$$
It is straightforward to verify that these expressions all satisfy the Painlevé equation (108).
For $k=3$, after normalising so that $R_{a b}=3 g_{a b}$, the metric (103) becomes [22]
$$h^{2}=\frac{3}{\left(1+r+r^{2}\right)^{2}}, \quad a_{1}^{2}=(1+2 r)^{2} h^{2}, \quad a_{2}^{2}=\left(1-r^{2}\right)^{2} h^{2}, \quad a_{3}^{2}=r^{2}(2+r)^{2} h^{2} .$$
Note that the radial variable $r$ being used here is precisely the parametric variable in (110). Defining a new radial variable $t$ by $r=-\frac{1}{2}+\frac{\sqrt{3}}{2} \tan \left(\frac{1}{2} \sqrt{3} t\right)$, the $k=3$ metric becomes
$$d s_{4}^{2}=d t^{2}+4 \sin ^{2} t \sigma_{1}^{2}+4 \sin ^{2}\left(t-\frac{2}{3} \pi\right) \sigma_{2}^{2}+4 \sin ^{2}\left(t+\frac{2}{3} \pi\right) \sigma_{3}^{2},$$
which can be recognised as the triaxial form of the Einstein metric on $S^{4}$, discussed in [32].
For $k=4$, and normalising for convenience so that $R_{a b}=6 g_{a b}$, the metric in [22] has
$$h^{2}=\frac{1}{4 r(1+r)^{2}}, \quad a_{1}^{2}=\frac{1}{1+r}, \quad a_{2}^{2}=\frac{(1-r)^{2}}{(1+r)^{2}}, \quad a_{3}^{2}=\frac{r}{1+r} .$$

\footnotetext{
${ }^{5}$ The triaxial form of the Fubini-Study metric is derived in appendix B.
}

Defining a new radial variable by $r=\tan ^{2} t$, the $k=4$ metric becomes
$$d s_{4}^{2}=d t^{2}+\cos ^{2} t \sigma_{1}^{2}+\cos ^{2} 2 t \sigma_{2}^{2}+\sin ^{2} t \sigma_{3}^{2},$$
which can be recognised as the triaxial $\mathbb{C P}^{2}$ metric [38], discussed in appendix B.
For $k=6$, the metric functions are given by
$$\begin{aligned}
& h^{2}=\frac{3\left(1+r+r^{2}\right)}{r(r+2)^{2}(2 r+1)^{2}}, \quad a_{1}^{2}=\frac{3\left(1+r+r^{2}\right)}{(r+2)(2 r+1)^{2}}, \\
& a_{2}^{2}=\frac{3\left(r^{2}-1\right)^{2}}{\left(1+r+r^{2}\right)(r+2)(2 r+1)}, \quad a_{3}^{2}=\frac{3 r\left(1+r+r^{2}\right)}{(r+2)^{2}(2 r+1)} .
\end{aligned}$$
The radial coordinate runs from $r=1$ to $r=\infty$, and we have normalised the metric so that $R_{a b}=3 g_{a b}$.

For $k=8$, after rederiving the metric using the construction given in [22], we find that the metric functions are given by
$$\begin{aligned}
h^{2} & =\frac{4(1+r)\left(3-2 r+r^{2}\right)\left(1-2 r+3 r^{2}\right)\left(1+2 r+3 r^{2}\right)}{(1-r) r\left(1+r^{2}\right)\left(1+2 r-r^{2}\right)^{2}\left(3+2 r+r^{2}\right)^{2}}, \\
a_{1}^{2} & =\frac{4(1-r)(1+r)^{3}\left(3-2 r+r^{2}\right)\left(1-2 r+3 r^{2}\right)}{\left(1+2 r-r^{2}\right)\left(3+2 r+r^{2}\right)^{2}\left(1+2 r+3 r^{2}\right)}, \\
a_{2}^{2} & =\frac{4\left(1+r^{2}\right)\left(3-2 r+r^{2}\right)\left(1-2 r-r^{2}\right)^{2}\left(1+2 r+3 r^{2}\right)}{\left(1+2 r-r^{2}\right)^{2}\left(3+2 r+r^{2}\right)^{2}\left(1-2 r+3 r^{2}\right)}, \\
a_{3}^{2} & =\frac{16 r\left(1-2 r+3 r^{2}\right)\left(1+2 r+3 r^{2}\right)}{\left(1+2 r-r^{2}\right)\left(3-2 r+r^{2}\right)\left(3+2 r+r^{2}\right)^{2}},
\end{aligned}$$
where we have again chosen the normalisation so that $R_{a b}=3 g_{a b}$. (This corrects a typographical error in [22], where there is an extra factor $(1+r)^{2}$ in the coefficient of $\sigma_{3}^{2}$ that should not be there.) The radial coordinate lies in the interval $\sqrt{2}-1<r<1$.

The $k=3$ and $k=4$ Tod-Hitchin metrics are $S^{4}$ and $\mathbb{C P}^{2}$ respectively, albeit in their less common triaxial forms. The existence of more than one Bianchi IX form is a consequence of the homogeneity of these metrics. The isometry algebra contains more than one $S U(2)$ subalgebra, and the orbits are different. The full set of homogeneous Einstein 4-manifolds is known, and from that list we deduce that this can only happen for self-dual Einstein metrics in the case of $S^{4}$ and $\mathbb{C P}^{2}$. Thus for higher values of $k$, the Tod-Hitchin metrics and the biaxial Bianchi IX self-dual Einstein metrics form disjoint classes. An explicit demonstration of this for the $k=6$ and $k=8$ metrics can be given by computing the quantity $X^{3} / Y^{2}$, where $X$ and $Y$ are the quadratic and cubic Weyl tensor invariants defined in (46). We showed that any biaxial self-dual Einstein metric must satisfy $X^{3} / Y^{2}=1$ (see (45)), and an elementary calculation shows that whilst this is true for the $k=3$ and $k=4$ metrics, it does not hold for the $k=6$ and $k=8$ metrics.

\subsection*{5.4 Global structure of the metrics}

The global structure of the Tod-Hitchin metrics is described in detail in [22, 23]. Here, we summarise the conclusions, presenting them in a way that is perhaps more readily accessible to physicists.

The key to understanding the global structure is to understand the nature of the degenerate orbits where metric coefficients vanish. An important feature of the metrics, for all $k$ including $k=3$ and $k=4$, is that at one end of the radial coordinate range the coefficient of $\sigma_{1}$ vanishes, while at the other end it is the coefficient of $\sigma_{2}$ that vanishes instead. This "slumping" is reminiscent of the metric behaviour in the Atiyah-Hitchin metric, where the coefficient of one of the $\sigma_{i}$ vanishes at short distance, while the coefficient of another of them stablises in the asymptotic region. In fact, as shown in [22], the Atiyah-Hitchin metric itself arises as the $k \longrightarrow \infty$ limit of the Tod-Hitchin metrics.

Because of the slumping, it is useful to introduce two different Euler-angle parameterisations of the left-invariant 1-forms, one adapted to the region where $\sigma_{1}$ collapses, and the other adapted to the region where $\sigma_{2}$ collapses. The procedure was described in [33], and elaborated somewhat in [34]. Here we shall present a brief summary of the description in [34], with labelling adapted to our present conventions.

Let us introduce Euler angles $(\theta, \phi, \psi)$ and $(\tilde{\theta}, \tilde{\phi}, \widetilde{\psi})$, such that
$$\begin{array}{ll}
\sigma_{1}=d \psi+\cos \theta d \phi, & \sigma_{2}+\mathrm{i} \sigma_{3}=e^{\mathrm{i} \psi}(d \theta+\mathrm{i} \sin \theta d \phi), \\
\sigma_{2}=d \widetilde{\psi}+\cos \tilde{\theta} d \tilde{\phi}, & \sigma_{3}+\mathrm{i} \sigma_{1}=e^{\mathrm{i} \tilde{\psi}}(d \tilde{\theta}+\mathrm{i} \sin \tilde{\theta} d \tilde{\phi}) .
\end{array}$$
We begin by taking $\psi$ and $\widetilde{\psi}$ both to have period $2 \pi$, so that the orbits are $\mathbb{R P}^{3}$. Clearly one could, in principle, solve for the transformation that relates the tilded and untilded coordinates, but we shall not need this.

We now consider the operation, which we shall denote by $I_{1}$, which implements the identification $\psi \approx \psi+\pi$. It is easily seen that in terms of the tilded coordinates, this corresponds to $\tilde{\theta} \longrightarrow \pi-\tilde{\theta}, \tilde{\phi} \longrightarrow \tilde{\phi}+\pi, \tilde{\psi} \longrightarrow-\tilde{\psi}$. Likewise we define $\widetilde{I}_{2}$ which implements $\widetilde{\psi} \approx \widetilde{\psi}+\pi$. Since the tilded basis is related to the untilded by a cyclic permutation of $\left(\sigma_{1}, \sigma_{2}, \sigma_{3}\right)$, we can see that in our notation we shall have $I_{i}=\widetilde{I}_{i}$, and so we can deduce that the effect of the $I_{i}$ on the untilded coordinates is
$$\begin{array}{ll}
I_{1}: & \theta \longrightarrow \theta, \quad \phi \longrightarrow \phi, \quad \psi \longrightarrow \psi+\pi, \\
I_{2}: & \theta \longrightarrow \pi-\theta, \quad \phi \longrightarrow \phi+\pi, \quad \psi \longrightarrow-\psi, \\
I_{3}: & \theta \longrightarrow \pi-\theta, \quad \phi \longrightarrow \phi+\pi, \quad \psi \longrightarrow \pi-\psi,
\end{array}$$
while on the tilded coordinates we have
$$\begin{aligned}
& I_{1}: \quad \tilde{\theta} \longrightarrow \pi-\tilde{\theta}, \quad \tilde{\phi} \longrightarrow \tilde{\phi}+\pi, \quad \widetilde{\psi} \longrightarrow \pi-\tilde{\psi}, \\
& I_{2}: \quad \tilde{\theta} \longrightarrow \tilde{\theta}, \quad \tilde{\phi} \longrightarrow \tilde{\phi}, \quad \widetilde{\psi} \longrightarrow \widetilde{\psi}+\pi, \\
& I_{3}: \quad \tilde{\theta} \longrightarrow \pi-\tilde{\theta}, \quad \tilde{\phi} \longrightarrow \tilde{\phi}+\pi, \quad \widetilde{\psi} \longrightarrow-\widetilde{\psi},
\end{aligned}$$

Consider first the case $k=3$, which gives the triaxial metric (112) on $S^{4}$. Near $t=0$ we have
$$d s_{4}^{2} \sim d t^{2}+4 t^{2} \sigma_{1}^{2}+\sigma_{2}^{2}+\sigma_{3}^{2} .$$
From the expression (117) we see that regularity at $t=0$ requires that $\psi$ have period $\pi$, and so from (119) we should impose the identification $I_{1}$. Near the other endpoint $t=\frac{2}{3} \pi$, we set $t=\frac{2}{3} \pi-\tau$, and so the metric takes the form
$$d s_{4}^{2} \sim d \tau^{2}+4 \tau^{2} \sigma_{2}^{2}+\sigma_{1}^{2}+\sigma_{3}^{2} .$$
From (118) we see that regularity requires that $\widetilde{\psi}$ have period $\pi$, and so from (120) we should in addition impose the identification $I_{2}$. Thus the principal orbits are $S O(3) /\left(\mathbb{Z}_{2} \times \mathbb{Z}_{2}\right)$. We also see that the 2-dimensional bolt described by $\sigma_{2}^{2}+\sigma_{3}^{2}=d \theta^{2}+\sin ^{2} \theta d \phi^{2}$ at $t=0$, and the 2-dimensional bolt described by $\sigma_{1}^{2}+\sigma_{3}^{2}=d \tilde{\theta}^{2}+\sin ^{2} \tilde{\theta} d \tilde{\phi}^{2}$ at $t=\frac{2}{3} \pi$ each has the topology of $\mathbb{R P}^{2}$, since there is an antipodal identification on the former implied by $I_{2}$ in (119), and in the latter implied by $I_{1}$ in (120). The metric therefore extends smoothly on the Veronese surfaces $\mathbb{R P}^{2}$ at each endpoint [22].