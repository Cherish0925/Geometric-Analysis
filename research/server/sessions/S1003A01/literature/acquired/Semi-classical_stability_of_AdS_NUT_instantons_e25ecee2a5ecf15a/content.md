---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: hep-th_0602127.pdf
converter: mathpix
format: mmd
---

\title{
Semi-classical stability of AdS NUT instantons
}

\author{
Claude Warnick \\ DAMTP, Centre for Mathematical Sciences, Cambridge University, Wilberforce Road, Cambridge CB3 OWA, UK \\ E-mail: C.M.Warnick@damtp.cam.ac.uk
}

\begin{abstract}
The semi-classical stability of several AdS NUT instantons is studied. Throughout, the notion of stability is that of stability at the one-loop level of Euclidean Quantum Gravity. Instabilities manifest themselves as negative eigenmodes of a modified Lichnerowicz Laplacian acting on the transverse traceless perturbations. An instability is found for one branch of the AdS-Taub-Bolt family of metrics and it is argued that the other branch is stable. It is also argued that the AdS-Taub-NUT family of metrics are stable. A component of the continuous spectrum of the modified Lichnerowicz operator on all three families of metrics is found.
\end{abstract}

\section*{1. Introduction}

Motivated by the AdS/CFT conjecture [1], there has recently been much interest in the two parameter AdS-Taub-NUT family ‡ of Riemannian biaxial Bianchi-IX metrics satisfying the Einstein equations with negative cosmological constant and non-trivial NUT charge [2, 3, 4, 5, 6, 7].

Upon the imposition of a regularity condition such metrics divide into two one parameter classes. The first class (AdS-Taub-Nut) have self-dual Weyl tensor and contain a nut. The second class of solutions (AdS-Taub-Bolt) contain a bolt, this class splits further into two branches. This is analogous to the case of AdS-Schwarzschild solutions at a given temperature, where the rôle of AdS is played by the AdS-Taub-Nut. The AdS-Schwarzshild solution with a smaller mass (and smaller horizon) is unstable and it's action is greater than that of both AdS and the other AdS-Schwarzshild [8, 9]. We find a similar situation for AdS-Taub-Bolt.

In [4], Hartnoll and Kumar conjectured, based on the Klebanov-Polyakov version of the $\mathrm{AdS}_{4} / \mathrm{CFT}_{3}$ correspondence, that the global minimiser of the action for the AdS-Taub-NUT class of metrics should be stable. In [10], the stability of some of these spaces against scalar perturbations and brane nucleation was discussed. By considering a one-loop correction to the bulk gravitational partition function, we shall investigate the semi-classical linear stability of such spacetimes, using techniques developed by Hu [11] and applied to the case

\footnotetext{
‡ Following [2], we refer to the full two parameter family as AdS-Taub-NUT, reserving AdS-Taub-Nut for the regular solution containing a nut
}
of Euclidean Taub-Bolt by Young [12]. These techniques have also been applied to the case of Lorentzian Taub-NUT recently by Holzegel [13]. The criterion for instability is that the modified Lichnerowicz operator
$$\widetilde{\Delta}_{L} h_{a b}=-\nabla^{e} \nabla_{e} h_{a b}-2 R_{a c b d} h^{c d}$$
acting on transverse, trace-free symmetric tensors should have no negative eigenmodes. We shall investigate the spectrum of this operator on metric perturbations of the AdS-Taub-instantons which preserve the $S U(2)$ symmetry. We find a negative mode for one of the instantons indicating instability for all values of the cosmological constant. We also find part of the positive spectrum of the modified Lichnerowicz operator for all instantons in the class under consideration.

In Section 2, we give a brief overview of the AdS-Taub-Nut and AdS-Taub-Bolt spaces, stating some results which we will later require. In Section 3, we introduce the method used to examine the stability of the spaces and we present an instability for one branch of the AdS-Taub-Bolt spaces and argue that the other spaces are linearly stable. In section 4 we present an alternative viewpoint, confirming the claims of section 3. In Section 5 we investigate the continuous spectrum of the operator $\widetilde{\Delta}_{L}$.

\section*{2. NUTs and Bolts in AdS space}

The metric for both AdS-Taub-Nut and AdS-Taub-Bolt in four dimensions can be put into the form:
$$d s^{2}=\frac{1}{A(r)} d r^{2}+4 N^{2} A(r) \sigma_{3}^{2}+B(r)\left(\sigma_{1}^{2}+\sigma_{2}^{2}\right),$$
where $\sigma_{i}$ are the left-invariant $S U(2)$ one-forms. The functions $A(r)$ and $B(r)$ are given by
$$\begin{aligned}
& A(r)=\frac{r^{2}+N^{2}-2 m r+\ell^{-2}\left(r^{4}-6 N^{2} r^{2}-3 N^{4}\right)}{r^{2}-N^{2}}, \\
& B(r)=r^{2}-N^{2},
\end{aligned}$$
where $N$ is the NUT charge and $m$ is the mass. This metric is Einstein, with $R_{\mu \nu}=-\frac{3}{\ell^{2}} g_{\mu \nu}$. The fixed point set of the $U(1)$ action is given by the solutions, $r=r_{+}$of $A(r)=0$. If $B\left(r_{+}\right)=0$, the fixed point set is of zero dimension and is known as a nut. If $B\left(r_{+}\right) \neq 0$, the fixed point set is two dimensional and is known as a bolt. As $r$ approaches $r_{+}$, we will in general have a conical singularity unless $A(r)$ satisfies the regularity condition
$$\left|A^{\prime}\left(r_{+}\right)\right|=\frac{1}{2 N} .$$
This amounts to a relation between $m$ and $N$, which can be solved and we find that the number of solutions depends on the value of $\frac{\ell}{N}$.

For all values of $N$ and $\ell$ there is a solution, called the AdS-Taub-Nut solution where
$$r_{n}=N, \quad m_{n}=\frac{N\left(\ell^{2}-4 N^{2}\right)}{\ell^{2}} .$$

Clearly we have $B(N)=0$, so we have a regular nut at $r=r_{n}$. We can also find two bolt solutions, which I shall call the AdS-Taub-Bolt ${ }^{ \pm}$solutions. They are given by:
$$\begin{aligned}
& r_{b \pm}=\frac{\ell^{2} \pm \sqrt{\ell^{4}-48 N^{2} \ell^{2}+144 N^{4}}}{12 N}, \\
& m_{b \pm}=\frac{r_{b \pm}^{4}+\left(\ell^{2}-6 N^{2}\right) r_{b \pm}^{2}+N^{2}\left(\ell^{2}-3 N^{2}\right)}{2 \ell^{2} r_{b \pm}} .
\end{aligned}$$
Clearly these equations only make sense if the quantity under the square root in the first equation is positive. This restricts $\ell / N$ to the range
$$\frac{\ell}{N} \geq 2 \sqrt{3(2+\sqrt{3})} \approx 6.69 .$$
Thus we find that requiring that the metric (2) be regular restricts the freedom quite considerably. For any given value of $\frac{\ell}{N}$, there are either 1 or 3 regular metrics in this family, excluding the critical case where $r_{\mathrm{b}+}=r_{\mathrm{b}-}$. It is possible to calculate the action for these spaces, but we shall postpone this until section 4.

It is useful to consider the limit $\ell \rightarrow \infty$, as we expect to recover the Euclidean Taub-NUT and Taub-Bolt solutions. For the AdS-Taub-Bolt ${ }^{+}$case, this limit does not exist as $r_{\mathrm{b}+} \rightarrow \infty$ as $\ell$ gets large. However, for the other two cases we can take this limit and we find for the nut case:
$$m_{n} \rightarrow N, \quad A(r) \rightarrow \frac{r-N}{r+N},$$
which gives the well known form of the metric for the self-dual Taub-NUT instanton. For the AdS-Taub-Bolt ${ }^{-}$case, we find:
$$r_{\mathrm{b}-} \rightarrow 2 N, \quad m_{b-} \rightarrow \frac{5}{4} N, \quad A(r) \rightarrow \frac{r^{2}-\frac{5}{2} N r+N^{2}}{r^{2}-N^{2}},$$
which gives the metric for Euclidean Taub-Bolt. This will provide a useful check on our stability results as for vanishing $\Lambda$, Taub-NUT has a self-dual Riemann tensor, and hence is linearly stable [14]. In [12] an unstable mode for the Taub-Bolt instanton was found.

\section*{3. Stability}
3.1. A criterion for instability

Instabilities of a physical system may make themselves known as an imaginary part of the partition function for the system [15, 16]. The partition function for Euclidean quantum gravity is given by:
$$Z=\int \mathrm{d}[g] \mathrm{e}^{-S[g]},$$
where the integral is taken over all Riemannian metrics subject to appropriate boundary behaviour and periodic in Euclidean time. The Euclidean action is given by:
$$S[g]=-\frac{1}{16 \pi G} \int_{\mathcal{M}} \mathrm{d} V \sqrt{g}(R-2 \Lambda)-\frac{1}{8 \pi G} \int_{\partial \mathcal{M}} \mathrm{d} S \sqrt{h} K .$$

Unfortunately this is not positive definite. Under a conformal transformation of the metric, $g^{\prime}=\Omega^{2} g$, where for simplicity we assume $\Omega=1$ on a neigbourhood of $\partial \mathcal{M}$ the scalar curvature transforms like:
$$R^{\prime}=\Omega^{-2} R-6 \Omega^{-3} \nabla^{a} \nabla_{a} \Omega .$$
Thus we find
$$I\left[g^{\prime}\right]=-\frac{1}{16 \pi G} \int_{\mathcal{M}} \mathrm{d} V \sqrt{g}\left(\Omega^{2} R+6 \Omega_{, a} \Omega^{, a}\right)-\frac{1}{8 \pi G} \int_{\partial \mathcal{M}} \mathrm{d} S \sqrt{h} K .$$
So by taking $\Omega$ to vary quickly, we can make $I\left[g^{\prime}\right]$ as negative as we choose. This problem can be circumvented by an appropriate choice of contour, but only in the semi-classical (one-loop) approximation [17]. For a semi-classical approximation, we expand the integral (10) about the critical points of $S[g]$, where we expect the dominant contributions to the integral. These satisfy
$$\frac{\delta S}{\delta g_{a b}}=0 \rightarrow R_{a b}=\Lambda g_{a b},$$
i.e., the classical Riemannian vacuum Einstein equations. Thus in order to find the semi-classical approximation to $Z$, one expands in small perturbations about the classical solutions:
$$\begin{aligned}
& \tilde{g}_{a b}=g_{a b}+h_{a b}, \\
& S[\tilde{g}]=S_{0}[g]+S_{2}[h]+O\left(h^{3}\right),
\end{aligned}$$
where $S_{2}[h]$ is second order in the small perturbation $h_{a b}$. We truncate the series for $I[\tilde{g}]$ and integrate over $h_{a b}$ to get
$$Z \cong Z_{1 \text { loop }}=N \mathrm{e}^{-S_{0}[g]} \int \mathrm{d}[h] \mathrm{e}^{-S_{2}[h]}$$
where the integral is to be taken over physically distinct perturbations $h_{a b}$. The action $S_{2}[h]$ is invariant under gauge transformations which correspond to infinitesimal diffeomorphisms:
$$h_{a b}^{\prime}=h_{a b}+\nabla_{a} V_{b}+\nabla_{b} V_{a} .$$
In order to deal with this, we follow [18] and use the Fadeev-Popov gauge fixing technique. The gauge fixing condition will be:
$$\nabla_{a}\left(h^{a b}-\frac{1}{\beta} g^{a b} h\right)=W^{b}$$
where $W$ is an arbitrary vector, $\beta$ is an arbitrary constant and $h=h^{a}{ }_{a}$ is the trace of the perturbation. The standard Fadeev-Popov method allows us to re-write the functional integral (15) as an integral over all fields $h_{a b}$, but with an altered integrand:
$$Z_{1 \text { loop }}=N \mathrm{e}^{-S_{0}[g]} \int \mathrm{d}[h](\operatorname{det} C) \mathrm{e}^{-I_{2 \text { eff. }}[h]} .$$
We now decompose the metric perturbation into a transverse, traceless part $\phi_{a b}$, a longitudinal traceless part generated by the vector $\tilde{n}$ and the trace $h$. Further, a Hodge-de Rham decomposition can be performed on $\tilde{n}$ so that
$$\tilde{n}_{a}=\eta_{a}+\nabla_{a} \chi, \quad \text { with } \quad \nabla_{a} \eta^{a}=0 .$$

We can then write the effective action as:
$$I_{2 \text { eff. }}=-\frac{1}{16 \pi} \int \mathrm{~d} V \mathcal{L}_{2}$$
with
$$\mathcal{L}_{2}=-\frac{1}{4} \phi^{a b} G_{a b c d} \phi^{c d}+\frac{1}{2} h F h-2 \gamma D^{a b}(\chi) D_{a b}(F \chi)-\gamma \mathfrak{D}^{a b e}\left(\eta_{e}\right) \mathfrak{D}_{a b f}\left(\left(C_{2}\right)^{f d} \eta_{d}\right)$$
where $\gamma$ is a constant related to $\beta$ by $\beta=4 \gamma /(1+\gamma)$ and we have defined operators
$$\begin{aligned}
F & =\frac{1-3 \gamma}{16 \gamma} \nabla_{e} \nabla^{e}-\frac{1}{4} \Lambda, \\
& =2 \nabla_{a} \nabla_{b}-\frac{1}{2} g_{a b} \nabla_{e} \nabla^{e}, \\
D_{a b} & \\
\mathfrak{D}_{a b e}\left(V^{e}\right) & =\frac{1}{2}\left(\nabla_{a} V_{b}+\nabla_{b} V_{a}\right), \\
\left(C_{2}\right)_{a b} V^{b} & =-\left(\nabla_{e} \nabla^{e}+\Lambda\right) V_{a}, \\
G_{a b c d} \phi^{c d} & =-\nabla_{e} \nabla^{e} \phi_{a b}-2 R_{a c b d} \phi^{c d},
\end{aligned}$$
where $V$ is a divergence free vector. It is possible to write the ( $\operatorname{det} C$ ) factor in (17) as a functional integral over anti-commuting vectors. Applying a Hodge-de Rham decomposition one finds
$$(\operatorname{det} C) \sim\left(\operatorname{det} C_{2}\right)(\operatorname{det} F) .$$
Finally, evaluating the Gaussian integrals in (17) we find
$$Z_{1 \text { loop }} \sim(\operatorname{det} G)^{-\frac{1}{2}}\left(\operatorname{det} C_{2}\right)^{\frac{1}{2}} .$$
Any zero modes of the determinants in (21) should be projected out. The determinants can be regularised by a $\zeta$-function regularisation [18]. $C_{2}$ is a positive semi-definite operator on the space of divergence free vector fields, with zero modes corresponding to Killing vectors. $G$ however is not positive definite and can in fact have a negative eigenmode. Such a negative eigenmode would introduce an imaginary part to the partition function and thus herald an instability. For example the flat Schwarzschild solution has a negative eigenmode. It is to be expected that the partition function be pathological in this case since the canonical ensemble for black holes breaks down due to the fact that they have negative specific heat.

Thus in our search for instabilities we can restrict to perturbations $h_{a b}$ which are transverse and tracefree. Our criterion for instabilities is that there exist negative eigenvalue solutions to the eigenvalue equation:
$$\left(\Delta_{L} h\right)_{a b}-2 \Lambda h_{a b}=-\nabla_{e} \nabla^{e} h_{a b}-2 R_{a c b d} h^{c d}=\lambda h_{a b},$$
where we have re-expressed $G$ in terms of the Lichnerowicz Laplacian $\Delta_{L}$ [19]. This equation is consistent with the Transverse Traceless condition.

A negative eigenmode of (22) corresponds to a direction within the space of gauge fixed metric perturbations along which the classical solution $g_{a b}$ is a local maximum. The criterion that
$$\widetilde{\Delta}_{L}=\Delta_{L}-2 \Lambda \geq 0$$
for stability may be arrived at from a more geometric perspective (see for example Besse [20]) which avoids the Fadeev-Popov procedure used above. There are some cases in which it can be shown that $\widetilde{\Delta}_{L}$ is positive definite. These include the case when $g_{a b}$ has self-dual Riemann tensor (sometimes called the half-flat condition) [14] and also the case where $g_{a b}$ is Einstein-Kähler [21]. In both these cases, the existence of a covariantly constant spinor is used to relate the eigenmodes of $\widetilde{\Delta}_{L}$ to those of scalar Laplacians acting on charged fields.

\subsection*{3.2. Hu's Technique}

Hu [11] proposed a method for separation of variables of tensor equations in a homogeneous space where the metric can be written in the form
$$d s^{2}=d r^{2}+\overline{\gamma_{i j}} \sigma^{i} \sigma^{j},$$
where $i, j=1,2,3$ and $\sigma^{i}=\sigma_{i}$ are again the left invariant one-forms on $S U(2)$. This was generalised by Young [12] to the case where $g_{00}$ is permitted to depend on $r$. The metric perturbation is expanded in terms of the Wigner functions, $\mathcal{D}_{K M}{ }^{J}(\theta, \phi, \psi)$ which are the analogue on $S^{3}$ of the spherical harmonics $Y_{l, m}(\theta, \phi)$. We concentrate on diagonal§ metric perturbations with the lowest "angular momentum", $J=M=K=0$. These are the perturbations which preserve $S U(2)$ symmetry. The resulting equations, along with the transverse and traceless conditions for the general metric form (2) are given in the Appendix.

We first consider the 11 and 22 equations. Taking the difference of (A.1) and (A.2) we find a second order differential equation for $Y=h_{11}-h_{22}$. We can put this into Schrödinger form:
$$-\frac{d^{2} \chi}{d r_{*}^{2}}+V\left(r_{*}\right) \chi=\lambda \chi, \quad 0 \leq r_{*}<\infty,$$
via the substitutions $Y=f \chi$ and $d r=g d r_{*}$, for some suitable $f$ and $g$. When we do this, we find that $V\left(r\left(r_{*}\right)\right)$ is a positive function for $r>r_{+}$, so that no normalizable solutions to (24) exist with $\lambda<0$. This means that in the search for a negative eigenmode of (22) we may set $h_{11}=h_{22}$.

We now consider the other diagonal mode. Setting $h_{11}=h_{22}$, we can use the constraint equations (A.5), (A.6) with the 00 equation (A.3) to decouple a second order differential equation in $h_{00}$ from the others. If we can solve this, we can find $h_{11}, h_{22}$ and $h_{33}$ from the constraint equations. Since (22) is consistent with the transverse traceless condition, we know that (A.5), (A.6) and (A.3) imply (A.1) and (A.4). This can be checked explicitly. The equation we decouple may be written:
$$a(r) h_{00}^{\prime \prime}+b(r) h_{00}^{\prime}+c(r) h_{00}=0,$$
where differentiation with respect to $r$ is denoted by a prime and the coefficients are given by:
$$\begin{aligned}
a(r) & =A \\
b(r) & =3 A^{\prime}+\frac{A B^{\prime}}{B}+\frac{B\left(A^{\prime 2}-2 A A^{\prime \prime}\right)}{B A^{\prime}-A B^{\prime}}-\frac{A}{B}\left(\frac{2 A B^{\prime 2}-B A^{\prime} B^{\prime}-2 A B B^{\prime \prime}}{B A^{\prime}-A B^{\prime}}\right),
\end{aligned}$$

\footnotetext{
§ The equations for off-diagonal perturbations can be put into Schrödinger form with strictly positive potential (see (24)), for all three metrics considered here and so cannot give rise to negative eigenmodes.
}
$$\begin{aligned}
c(r)=\lambda+ & \frac{A^{\prime 2}}{2 A}+\frac{A^{\prime} B^{\prime}}{B}-\frac{A B^{\prime 2}}{B^{2}}+A^{\prime \prime}+\frac{3}{2 A}\left(\frac{B A^{\prime}+A B^{\prime}}{B A^{\prime}-A B^{\prime}}\right) \\
+ & \frac{B A^{\prime} B^{\prime}+2 B A B^{\prime \prime}-2 A B^{\prime 2}}{B^{2}}\left(\frac{2 B A^{\prime}+A B^{\prime}}{B A^{\prime}-A B^{\prime}}\right),
\end{aligned}$$
the rest of this section will consist of an analysis of this equation.

\subsection*{3.3. AdS-Taub-Nut}

In the case where $A(r)$ and $B(r)$ are given by (2) with (5) we can cast equation (25) into Schrödinger form (24) where $V$ is once again found to be positive on the range $r>r_{+}$. Thus for AdS-Taub-Nut we have checked all the possible TT perturbations with $J=K=M=0$ and found that none give negative eigenvalue solutions to (22), thus there is no linear instability due to perturbations of this type. This is in agreement with the result that the $\ell \rightarrow \infty$ limit yields a (linearly) stable metric.

One would normally expect the eigenvalues of a Laplacian operator to be bounded below by the most symmetric modes. In our case that would be the $S U(2)$ invariant modes. In the case of the scalar Laplacian acting on a space with metric given by (2) this can be seen explicitly:
$$\begin{aligned}
-\nabla^{2} \phi= & -\nabla^{2}\left(\phi^{K}(r) \mathcal{D}_{K}(\theta, \phi, \psi)\right) \\
= & \left(-\nabla^{2} \phi^{K}(r)\right) \mathcal{D}_{K}(\theta, \phi, \psi)-2\left(\partial^{d} \phi^{K}(r)\right)\left(\partial_{d} \mathcal{D}_{K}(\theta, \phi, \psi)\right) \\
& \quad-\phi^{K}(r) \nabla^{2} \mathcal{D}_{K}(\theta, \phi, \psi) \\
= & \left(-\nabla^{2} \phi^{K}(r)\right) \mathcal{D}_{K}(\theta, \phi, \psi)+\phi^{K}(r)\left(-\nabla^{2} \mathcal{D}_{K}(\theta, \phi, \psi)\right) .
\end{aligned}$$
It can be shown that $\left(-\nabla^{2} \mathcal{D}_{K}\right)$ is positive for this metric form. This separation into a radial part and an angular part does not occur for the the Laplacian acting on symmetric tensors as there are extra terms introduced by the connection. It has not been possible to show explicitly that the $S U(2)$ invariant perturbations give a lower bound for $\widetilde{\Delta}_{L}$, but one would still expect this to be the case. Increasing the spin of the perturbation modes introduces a more rapidly varying angular dependence, which one would expect to increase the eigenvalues of $-\nabla^{2}$ and hence of $\widetilde{\Delta}_{L}$.

We therefore conjecture that $\widetilde{\Delta}_{L}$ is positive acting on all metric perturbations and thus that AdS-Taub-Nut is stable. This may be related to the fact that the Weyl tensor is self dual for the AdS-Taub-Nut space. In the Euclidean case, the full Riemann tensor is self-dual and this is known to imply stability [14].

\subsection*{3.4. AdS-Taub-Bolt ${ }^{-}$}

In the case of AdS-Taub-Bolt ${ }^{-}$, when one changes (25) into Schrödinger form, one encounters a divergent potential. In order to proceed, we must use numerical integration techniques. If we make the substitution $r=x N$, we find that the equations depend on $N$ only through the ratio $\frac{\ell}{N}$. We can therefore scale $N$ out of the problem and set $N=1$ without loss of generality. We must now consider the singularity structure of the differential equation (25). In the region
of interest to us, $r \geq r_{\mathrm{b}-}$, we find that the equation has 3 regular singular points, at $r_{\mathrm{b}-}, r_{\text {int }}$. and infinity, where $r_{\mathrm{b}-}<r_{\text {int. }}<\infty$. Other singular points outside of the range of interest preclude the possibility of an analytic solution.

We consider first the regular singular point at $r=r_{\mathrm{b}-}$. Near to this point, the differential equation has the asymptotic form:
$$h_{00}^{\prime \prime}+\frac{4}{r-r_{\mathrm{b}-}} h_{00}^{\prime}+\frac{2}{\left(r-r_{\mathrm{b}-}\right)^{2}} h_{00}=0 .$$
Substituting $h_{00} \sim\left(r-r_{\mathrm{b}-}\right)^{\alpha}$, we find the indicial equation
$$\alpha^{2}+3 \alpha+2=0,$$
with solutions $\alpha=-1$ and $\alpha=-2$. Thus there are two independent solutions of (25) that behave like $\left(r-r_{\mathrm{b}-}\right)^{-1}$ and $\left(r-r_{\mathrm{b}-}\right)^{-2}$ as $r \rightarrow r_{\mathrm{b}-}$. We impose a normalisation condition on the perturbation modes given by
$$\int \mathrm{d} V h_{a b} h^{a b}<\infty .$$
Using the constraint equations, we can show that the $h_{00}$ contribution dominates the integrand in a region just outside the bolt. Using the fact that $d V=\sqrt{g} d \psi d \theta d \phi d r$, where $\psi, \theta$ and $\phi$ are the usual Euler angles on $S U(2)$ and the form of the metric (2) with the constraint equations (A.5, A.6) we can show that this integral coverges at $r=r_{\mathrm{b}-}$ if and only if $h_{00} \sim\left(r-r_{\mathrm{b}-}\right)^{\beta}$ where $\beta>-3 / 2$. Thus only one of the two independent solutions at $r=r_{\mathrm{b}-}$ represents a normalisable perturbation - we must pick the solution that behaves like $h_{00} \sim\left(r-r_{\mathrm{b}-}\right)^{-1}$ near $r=r_{\mathrm{b}-}$. This provides us with a stepping off condition for our numerical integration. We can perform a Frobenius expansion of the solution about the regular singular point and then use this to calculate $h_{00}$ and $h_{00}^{\prime}$ at $r=r_{\mathrm{b}-}+\epsilon$ where $\epsilon$ is some small number, taken to be $10^{-5}$. This deals with the first regular singular point.

It can be shown, by a similar method to that used above that $h_{00}$ and $h_{00}^{\prime}$ are bounded as $r \rightarrow r_{\text {int }}$, so no special considerations are required for the numerical integration through this point.

Finally we need to take account of the regular singular point at infinity. In the limit that $r \rightarrow \infty$, the differential equation has the asymptotic form
$$h_{00}^{\prime \prime}+\frac{12}{r} h_{00}^{\prime}+\frac{28+\ell^{2} \lambda}{r^{2}} h_{00}=0 .$$
Substituting $h_{00} \sim r^{\alpha}$ we find the indicial equation:
$$\alpha^{2}+11 \alpha+\left(28+\ell^{2} \lambda\right)=0,$$
with solutions
$$\alpha_{ \pm}=\frac{-11 \pm \sqrt{9-4 \ell^{2} \lambda}}{2} .$$
Using the constraint equations, we find that the integrand of (28) is dominated by the contribution from $h_{33} \sim r^{6} h_{00}$. This translates to a requirement that $h_{00} \sim r^{\beta}$ with $\beta<-\frac{11}{2}$ in order that (28) is satisfied. So we see that only one of the two independent solutions at infinity will give a normalisable perturbation. We will need to match the normalisable solution at

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/c14ca358-7c8f-4f02-b52d-029268a80012-09.jpg?height=782&width=1281&top_left_y=301&top_left_x=381}
\captionsetup{labelformat=empty}
\caption{Figure 1. A plot showing the negative eigenvalue, $\lambda$, against $\ell$ for AdS-Taub-Bolt ${ }^{-}$Space}
\end{figure}
infinity to the normalisable solution at $r_{\mathrm{b}+}$ and this matching, if it is possible, will determine the value of $\lambda$.

In order to ascertain whether there exist negative solutions for $\lambda$, we perform a numerical integration starting at $r_{\mathrm{b}-}+\epsilon$, with initial conditions determined from the Frobenius expansion about $r_{\mathrm{b}-}$. This determines the solution, up to a arbitrary multiplicative constant as we can determine $h_{00}$ and all its derivatives here. Having chosen the normalisable solution at the bolt, we need to check that the solution is normalisable at infinity. The only parameter we still have available is $\lambda$. As $r \rightarrow \infty$ the solution must have the asymptotic form found above, but will in general be a linear combination of the two independent asymptotic forms.
$$h_{00}(r) \sim k(\lambda) r^{\alpha_{+}}+l(\lambda) r^{\alpha_{-}},$$
where $\alpha_{+}>-11 / 2$ and $\alpha_{-}<-11 / 2$ are given in equation (30) and $k(\lambda), l(\lambda)$ are constants, which we assume to depend continuously on $\lambda$. The normalisation condition requires that $\lambda=\lambda_{0}$, where $k\left(\lambda_{0}\right)=0$. Since we are only performing a numerical integration, it is not possible to find the form of $k(\lambda)$ explicitly, but we can find an interval within which $\lambda_{0}$ must lie.

If we consider $f(r)=r^{11 / 2} h_{00}(r)$, then $f(r)$ will generically tend to either positive or negative infinity, depending on the sign of $k(\lambda)$. If we can find numbers $\lambda_{1}$ and $\lambda_{2}$ such that $k\left(\lambda_{1}\right)$ has opposite sign to $k\left(\lambda_{2}\right)$, then we can deduce the existence of a root of $k(\lambda)$ in the interval $\left(\lambda_{1}, \lambda_{2}\right)$, by the Intermediate Value Theorem. This procedure was implemented using the computer package Mathematica, and negative eigenvalues have been found for values of $\ell$ on the entire range $2 \sqrt{3(2+\sqrt{3})}<\ell<\infty$. A plot of these negative eigenvalues is shown in Figure 1, together with a best fit curve.

We find that as $\ell \rightarrow \infty$, we have that $\lambda \rightarrow-0.20$ approximately. This is consistent with the findings of Roberta Young [12], who found that Euclidean Taub-Bolt had a negative
eigenmode in this sector with $\lambda \approx-0.20$. We also find that as $\ell$ approaches the critical value where the AdS-Taub-Bolt ${ }^{-}$and AdS-Taub-Bolt ${ }^{+}$spaces are the same, the negative eigenvalue tends to zero from below.

\subsection*{3.5. AdS-Taub-Bolt ${ }^{+}$}

The final case, where the bolt is located at $r=r_{\mathrm{b}+}$ is similar in many ways to the previous case. We find the same singularity structure and asymptotic forms for the perturbation. We can proceed in exactly the same way as above, but we find no negative eigenvalues. We therefore conjecture that this spacetime is stable, as it appears to have no negative eigenmodes in the lowest "angular momentum" state.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/c14ca358-7c8f-4f02-b52d-029268a80012-10.jpg?height=782&width=1281&top_left_y=938&top_left_x=381}
\captionsetup{labelformat=empty}
\caption{Figure 2. A plot showing the actions $S-S_{\text {NUT }}$ against $\ell$ for $N=1$}
\end{figure}

In Figure 2 we show a plot of the action of both AdS-Taub-Bolt spaces against $\ell$, with the action for AdS-Taub-Nut subtracted. This will be calculated in Section 4. The dotted line represents the unstable AdS-Taub-Bolt ${ }^{-}$space, the horizontal axis the Taub-NUT space and the other curve AdS-Taub-Bolt ${ }^{+}$. The thicker line denotes the global minimizer of the action. We see here two interesting features. Firstly we note that at $\ell=2 \sqrt{3(2+\sqrt{3})}$ we have a bifurcation, with the two Bolt families appearing, with one stable and the other unstable. We also note that at $\ell=2 \sqrt{7+2 \sqrt{10}}$ there is a phase transition from AdS-Taub-Nut as the global minimiser of the action to AdS-Taub-Bolt ${ }^{+}$as the global minimiser. This is the NUT charged version of the Hawking-Page transition for AdS Black Holes [8].

\section*{4. Another Perspective on Stability}

We will now present an alternative argument, which reproduces all the features of the plot in Figure 2.

In constructing the nut charged AdS instantons considered above, the usual technique (outlined in Section 2) is to consider a metric of the form (2) which satisfies the Einstein equations $R_{\mu \nu}=-\frac{3}{\ell^{2}} g_{\mu \nu}$. Then one imposes the condition of regularity to reduce the number of solutions to those given above. Here we shall consider a family of metrics which are regular everywhere, with a bolt (or possibly nut) located at $r_{b}$, which is treated as a free parameter. The AdS-Taub-Nut and Taub-Bolt(±)-AdS instantons correspond to particular choices of $r_{b}$. We can then calculate the action for this family of spacetimes as a function of $r_{b}$ and we expect it will be locally extremized at the already known values of $r_{b}$ which give solutions of the Einstein equations. This corresponds to taking a slice parameterised by $r_{b}$ through the space of metrics containing a bolt or a nut.

Our metric ansatz will be:
$$d s^{2}=\frac{1}{A(r)} d r^{2}+4 N^{2} A(r) \sigma_{3}^{2}+B(r)\left(\sigma_{1}^{2}+\sigma_{2}^{2}\right)$$
with
$$\begin{aligned}
& A(r)=\frac{\left(r-r_{b}\right)\left(\alpha r+\beta+\ell^{-2}\left(r^{3}+r^{2} r_{b}\right)\right)}{r^{2}-N^{2}}, \\
& B(r)=r^{2}-N^{2} .
\end{aligned}$$
We then impose regularity at $r=r_{b}$ and require the mass to be $m$, by considering the asymptotics. This gives us the metric functions:
$$\begin{array}{ll}
A(r) & =\frac{\left(r-r_{b}\right)\left(4 N\left(r-r_{b}\right) r_{b}\left(r+r_{b}\right)^{2}-\ell^{2}\left(4 m N\left(r_{b}-r\right)+(r+r b)\left(n^{2}-r_{b}^{2}\right)\right)\right)}{4 \ell^{2} N\left(r^{2}-N^{2}\right) r_{b}}, \\
B(r) & =r^{2}-N^{2} .
\end{array}$$
We are now ready to calculate the action. The Euclidean action is given by:
$$S=S_{\text {bulk }}+S_{\text {surf. }}=-\frac{1}{16 \pi G} \int_{\mathcal{M}} \mathrm{d} V \sqrt{g}\left(R+\frac{6}{\ell^{2}}\right)-\frac{1}{8 \pi G} \int_{\partial \mathcal{M}} \mathrm{d} S \sqrt{h} K,$$
which is the standard Einstein-Hilbert action together with the Gibbons-Hawking-York boundary term. It is well known that this integral does not converge and so some means of regularising the action is required. The method used was that of counterterm subtraction proposed by Emparan, Johnson and Myers [22]. This was also found independently by Mann [23]. The calculation proceeds much as their calculation for the action of Taub-NUT. We find that the action of the metric defined by (32) and (33) is:
$$S=\frac{4 N}{\ell^{2}}\left(r_{b}^{3}-3 N^{2} r_{b}\right)+N^{2}+4 N r_{b}-r_{b}^{2} .$$
We note that this does not depend on $m$, which is also a free parameter of this family of metrics. The variation of this reduced action alone will not determine $m$, for that we require the full Einstein equations, which force $m$ to take the NUT or Bolt values at the critical points.

Setting $r_{b}=x N$,defining $\mu=\ell / N$, and using the additive freedom to set $S=0$ for AdS-Taub-Nut we find
$$\frac{S}{N^{2}}=\frac{4}{\mu^{2}}\left(x^{3}-3 x+2\right)-3+4 x-x^{2} .$$

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/c14ca358-7c8f-4f02-b52d-029268a80012-12.jpg?height=782&width=1282&top_left_y=591&top_left_x=381}
\captionsetup{labelformat=empty}
\caption{Figure 3. A plot showing $S / N^{2}$ against $x$ for several values of $\mu=\ell / N$}
\end{figure}

So we see that as $\mu$ is varied, the graph of $S / N^{2}$ will change. A plot of $S / N^{2}$ against $x$ for various values of $\mu$ is shown in Figure 3. Also included is a dotted curve showing the locus of the extremal points of the function as $\mu$ varies. We see that the point $x=1$, which corresponds to AdS-Taub-Nut is always a minimum since we must exclude the region $x<1$ from consideration as these metrics are not regular. For small $\mu$ this is the only minimum. As we increase $\mu$, we find that a pair of extrema, one maximum and one minimum appear at $\mu=\mu_{1}$, where
$$\mu_{1}=2 \sqrt{3(2+\sqrt{3})},$$
which is precisely the value we would expect from the standard constructions for AdS-Taub-Nut and AdS-Taub-Bolt. If we think of this function $S(x) / N^{2}$ as defining the dynamics of some system by
$$\ddot{x}=-S^{\prime}(x) / N^{2},$$
then this bifurcation is of the form known as a saddle-node bifurcation, since it produces two new fixed points, one stable (a node) and one unstable (a saddle). Of course we have no formal dynamics on the space of metrics, but we still expect a local maximum to correspond to an unstable metric as it corresponds to a direction contributing an imaginary part to the partition function. Thus we shall refer to this bifurcation as a saddle-node bifurcation. We also find that the maximum occurs at precisely $x=r_{\mathrm{b}-} / N$ and the minimum at $x=r_{\mathrm{b}+} / N$,
confirming our previous result that we expect the AdS-Taub-Bolt ${ }^{-}$instanton to be unstable while the AdS-Taub-Bolt ${ }^{+}$instanton is stable.

We also note a global bifurcation when $\mu=\mu_{2}$ where
$$\mu_{2}=2 \sqrt{7+2 \sqrt{10}},$$
when the global minimum moves from $x=1$ to $x=r_{\mathrm{b}+} / N$, which corresponds to AdS-Taub-Bolt ${ }^{+}$. This again accords with what we expect from previous analysis and corresponds to the Hawking-Page type phase transition.

These observations accord nicely with the general argument given in section 6 of [24] for the production of negative modes of the Lichnerowicz operator at bifurcation points in parameter space, in particular, from figure 1 we find that the negative eigenmode tends to zero as we approach the bifurcation.

Unfortunately this analysis cannot replace that of the previous section, since we have not explicitly found a normalisable negative mode of (22) for a perturbation about the AdS-Taub-Bolt ${ }^{-}$instanton. It is possible to find the linearised perturbation of the metric at this point using our analysis, but this perturbation is not normalisable. It is however not in the Transverse, Tracefree gauge and it is possible that in the appropriate gauge this perturbation does give a normalisable mode.

\section*{5. The Continuous Spectrum of $\widetilde{\Delta}_{L}$}

We have been so far concerned with looking for eigenvalues of $\widetilde{\Delta}_{L}$ on the AdS-Taub-Nut and -Bolt instantons. In the case of an elliptic operator on a non-compact manifold, the spectrum may also include a continuum of approximate eigenvalues. As an example, the time independent Schrödinger operator for the Hydrogen atom is a Laplacian type operator acting on $\mathbb{R}^{3} /\{0\}$. As is well known, this has a countable set of negative eigenvalues corresponding to the bound states. The spectrum however includes a continuum of positive "eigenvalues" which correspond to free particles moving in the Coulomb potential. These are not true eigenvalues since they do not correspond to normalisable eigenfunctions (wavefunctions). The sense in which they may be considered part of the spectrum is given below. We shall show that the continuous spectrum of $\widetilde{\Delta}_{L}$ acting on any of the three spaces considered above includes the ray $\left\{\lambda \in \mathbb{R}: \lambda>9 / 4 l^{2}\right\}$.

\subsection*{5.1. A Little Functional Analysis}

We can think of the space of gauge fixed, finite metric perturbations as a Hilbert space, defined by:
$$\mathcal{H}=\left\{h_{a b} \in T^{*} \mathcal{M} \otimes_{S} T^{*} \mathcal{M}: \nabla^{a} h_{a b}=0, h^{a}{ }_{a}=0, \int_{\mathcal{M}} h_{a b} h^{a b} \mathrm{~d} V<\infty\right\},$$
with $L^{2}$ inner product given by
$$\langle h, k\rangle=\int_{\mathcal{M}} h_{a b} k^{a b} \mathrm{~d} V .$$
$\widetilde{\Delta}_{L}$ is then a linear operator from $\mathcal{H}_{2}$ to $\mathcal{H}_{0}$, where by $\mathcal{H}_{i}$ we mean
$$\mathcal{H}_{i}=\left\{h_{a b} \in \mathcal{H}: \partial_{c_{1}} \ldots \partial_{c_{i}} h_{a b} \text { exist and are continuous }\right\} .$$
$\mathcal{H}_{i}$ are dense subsets of $\mathcal{H}$ with respect to the norm topology, where the norm is defined as usual by:
$$\|h\|^{2}=\langle h, h\rangle=\int_{\mathcal{M}} h_{a b} h^{a b} \mathrm{~d} V .$$
A linear operator $A: \mathcal{H} \rightarrow \mathcal{H}$ is said to be bounded if $\exists k$ such that
$$\|A x\| \leq k\|x\|, \quad \forall x \in \mathcal{H},$$
an operator which is not bounded is unbounded. We define the spectrum of $A, \sigma(A)$ as follows:
$\lambda \notin \sigma(A) \Longleftrightarrow$ the following properties hold:
\begin{itemize}
\item[(i)] $(A-\lambda I)^{-1}$ exists,
\item[(ii)] $(A-\lambda I)^{-1}$ is bounded,
\item[(iii)] $(A-\lambda I)^{-1}$ is densely defined (i.e. defined on a dense subset of $\mathcal{H}$ ).
\end{itemize}

The set of $\lambda$ such that $(A-\lambda I)^{-1}$ does not exist is called the point spectrum of $A, P \sigma(A)$. the set of $\lambda$ such that $(A-\lambda I)^{-1}$ ) is unbounded is called the continuous spectrum of $A, C \sigma(A)$. We shall not discuss the third condition.

Lemma 5.1. Given $\lambda \notin P \sigma(A)$, if there exists a sequence $x_{n} \in \mathcal{H}$ such that
$$\frac{\left\|(A-\lambda I) x_{n}\right\|}{\left\|x_{n}\right\|} \rightarrow 0, \quad \text { as } \quad n \rightarrow \infty,$$
then $\lambda \in C \sigma(A)$.
Proof. Define $y_{n}=(A-\lambda I) x_{n}$, by assumption as $n \rightarrow \infty$
$$\frac{\left\|y_{n}\right\|}{\left\|(A-\lambda I)^{-1} y_{n}\right\|} \rightarrow 0 \quad \Rightarrow \quad \frac{\left\|(A-\lambda I)^{-1} y_{n}\right\|}{\left\|y_{n}\right\|} \rightarrow \infty,$$
but this clearly cannot occur if $(A-\lambda I)^{-1}$ is bounded, since if this is the case, $\exists k$ such that
$$\frac{\left\|(A-\lambda I)^{-1} y_{n}\right\|}{\left\|y_{n}\right\|} \leq k .$$
Thus $(A-\lambda I)^{-1}$ must be unbounded, hence $\lambda \in C \sigma(\lambda)$. \(\square\)

\subsection*{5.2. The $\widetilde{\Delta}_{L}$ Operator}

We now consider the continuous spectrum of $\widetilde{\Delta}_{L}$. We will restrict attention for the moment to perturbations of the form considered in section 3. These are generated by the $h_{00}$ component, which has to satisfy equation (25). We first define the functions $\rho_{n}(x)$ by:
$$\rho_{n}(x)= \begin{cases}1 & \text { if } r<n \\ 1-K \int_{n}^{r} \exp \left[-\frac{1}{(x-n)^{2}}-\frac{1}{(x-n-1)^{2}}\right] \mathrm{d} x & \text { if } n \leq r \leq n+1 \\ 0 & \text { if } r>n+1\end{cases}$$
with $K$ chosen so that $\rho_{n}(n+1)=0$. These functions are everywhere smooth on the real line. For $\lambda>9 / 4 l^{2}$ we define $f(r)$ to be the solution of (25) which gives a finite contribution to $\langle h, h\rangle$ at $r_{+}$. This generates a perturbation which satisfies
$$\left(\widetilde{\Delta}_{L}-\lambda I\right) h_{a b}=0 .$$
However this $h_{a b}$ is not an element of $\mathcal{H}$ since as $r \rightarrow \infty$ we have
$$f(r) \sim p r^{-11 / 2} \cos (\alpha \log r)+q r^{-11 / 2} \sin (\alpha \log r),$$
where $\alpha=\frac{1}{2} \sqrt{4 l^{2} \lambda-9}$ is a constant. We find that for large $r$, counting powers of $r$ gives:
$$h_{a b} h^{a b} \sqrt{g} \sim f^{2} r^{10} \sim \frac{1}{r},$$
so that $\langle h, h\rangle$ does not converge. We define $f_{n}(r)$ by
$$f_{n}(r)=\rho_{n}(\log r) f(r) .$$
Setting $h_{00}=f_{n}$ generates a perturbation which we call $h_{a b}^{n}$ via the constraint equations and we claim that
$$\frac{\left\|\left(\widetilde{\Delta}_{L}-\lambda I\right) h_{a b}^{n}\right\|}{\left\|h_{a b}^{n}\right\|} \rightarrow 0, \quad \text { as } \quad n \rightarrow \infty .$$
It is easily seen that $\left\|h_{a b}^{n}\right\| \rightarrow \infty$ since the integral in $\left\|h_{a b}^{n}\right\|$ is bounded below by the integral for $\left\|h_{a b}\right\|$ cut off at $r=\mathrm{e}^{n}$. It suffices then to show that $\left\|\left(\widetilde{\Delta}_{L}-\lambda I\right) h_{a b}^{n}\right\|$ is bounded as $n \rightarrow \infty$. Clearly $\left(\widetilde{\Delta}_{L}-\lambda I\right) h_{a b}^{n}=0$ on $\left\{r_{+} \leq r \leq \mathrm{e}^{n}\right\} \cup\left\{\mathrm{e}^{n+1} \leq r\right\}$ so we need to estimate
$$\int_{r=\mathrm{e}^{n}}^{\mathrm{e}^{n+1}}\left[\left(\widetilde{\Delta}_{L}-\lambda I\right) h^{n}\right]_{a b}\left[\left(\widetilde{\Delta}_{L}-\lambda I\right) h^{n}\right]^{a b} \mathrm{~d} V=\left\|\left(\widetilde{\Delta}_{L}-\lambda I\right) h^{n}\right\|^{2},$$
for large $n$. In this limit, we can use the large $n$ asymptotic expansions to estimate the leading order behaviour of this term. Substituting these in, we find that:
$$\left\|\left(\widetilde{\Delta}_{L}-\lambda I\right) h^{n}\right\|^{2} \sim K \int_{\mathrm{e}^{n}}^{\mathrm{e}^{n+1}}\left(L \tilde{f}_{n}\right)^{2} r^{10} \mathrm{~d} r,$$
with
$$L \tilde{f}_{n}=r^{2} \tilde{f}_{n}^{\prime \prime}+12 r \tilde{f}_{n}^{\prime}+\left(28+l^{2} \lambda\right) \tilde{f}_{n},$$
the leading order expansion of (25) and where $\tilde{f}_{n}$ is defined by:
$$\tilde{f}_{n}(r)=\left(p r^{-11 / 2} \cos (\alpha \log r)+q r^{-11 / 2} \sin (\alpha \log r)\right) \rho_{n}(\log r) .$$
Under a change of variables $x=\log r$ the integral in (48) becomes:
$$\begin{aligned}
\int_{e^{n}}^{e^{n+1}}\left(L \tilde{f}_{n}\right)^{2} r^{10} d r & =\int_{n}^{n+1}\left\{\rho_{n}^{\prime \prime}(x)(p \sin \alpha x+q \cos \alpha x)+2 \alpha \rho_{n}^{\prime}(x)(q \sin \alpha x-p \cos \alpha x)\right\}^{2} d x \\
& =\int_{0}^{1}\left\{\rho_{0}^{\prime \prime}(y)(p \sin \alpha(y+n)+q \cos \alpha(y+n))\right. \\
& \left.\quad+2 \alpha \rho_{0}^{\prime}(y)(q \sin \alpha(y+n)-p \cos \alpha(y+n))\right\}^{2} d y
\end{aligned}$$
since $\rho_{n}(x)=\rho_{0}(x-n)$. Now for all $n$ the integrand is bounded since
$$\left|\rho_{0}^{\prime}(x)\right| \leq 6,$$
thus there exist constants $C$ and $\tilde{n}$ such that
$$\left\|\left(\widetilde{\Delta}_{L}-\lambda I\right) h^{n}\right\| \leq C, \quad \forall n \geq \tilde{n} .$$
We can now apply lemma 5.1 to the operator $\widetilde{\Delta}_{L}$ and we find that for $\lambda>9 / 4 l^{2},\left(\widetilde{\Delta}_{L}-\lambda I\right)^{-1}$ is unbounded, hence $\left\{\lambda>9 / 4 l^{2}\right\} \subseteq C \sigma\left(\widetilde{\Delta}_{L}\right)$.

This result makes no use of the value of $m$ or the location of the zeroes of $A(r)$, so it holds for all three of the instantons considered here. It is also possible to perform this analysis for the other $S U(2)$ invariant modes of the perturbation and we find exactly the same condition on $\lambda$ in order that it be in the continuous spectrum.

\section*{6. Conclusions}

We have studied the semi-classical stability of the AdS-Taub-Nut instantons and the two branch family of AdS-Taub-Bolt instantons and we have found a negative mode of (22) for the AdS-Taub-Bolt ${ }^{-}$instanton, implying that this instanton is unstable. For the AdS-Taub-Nut and AdS-Taub-Bolt ${ }^{+}$instanton we have argued that they are (linearly at least) stable. We have also justified this by considering a family of regular metrics, not necessarily satisfying Einstein's equations, which contains these instantons as special cases. This gives an intuitive sense of how the saddle-node bifurcation in the $S-\mu$ plane arises, as well as the Hawking-Page type bifurcation which occurs. We have also found that for all three instantons the continuous spectrum includes the ray $\left\{\lambda>9 / 4 l^{2}\right\}$.

\section*{Acknowledgments}

I would like to thank Gary Gibbons for proposing this project and for useful discussions along the way. I am grateful to Sean Hartnoll for advice and helpful comments. Many thanks to Gustav Holzegel for much useful help and advice. I would also like to gratefully acknowledge funding from PPARC.

\section*{Appendix}

The following are a set of differential equations governing the $J=M=K=0$ piece of the tensor harmonic decomposition of the equation
$$-\nabla_{e} \nabla^{e} h_{a b}-2 R_{a c b d} h^{c d}=\lambda h_{a b},$$
for the metric
$$d s^{2}=\frac{1}{A(r)} d r^{2}+4 N^{2} A(r) \sigma_{3}^{2}+B(r)\left(\sigma_{1}^{2}+\sigma_{2}^{2}\right)$$
We suppress the $r$ dependence of $A(r)$ and $B(r)$ and use a prime to denote differentiation with respect to $r$. These are taken from [12], with some typos corrected.

11 Component
$$\bar{a}(r) h_{11}^{\prime \prime}+\bar{b}(r) h_{11}^{\prime}+\bar{c}(r) h_{00}+\bar{d}(r) h_{11}+\bar{e}(r) h_{22}+\bar{f}(r) h_{33}=-\lambda h_{11},$$
with
$$\begin{aligned}
& \bar{a}(r)=A, \\
& \bar{b}(r)=A^{\prime}-A \frac{B^{\prime}}{B}, \\
& \bar{c}(r)=-2 A\left(A^{\prime} B^{\prime}\right)+\frac{4 A^{2} B^{\prime 2}}{B}-4 A^{2} B^{\prime \prime}, \\
& \bar{d}(r)=\frac{2}{B}-\frac{A B^{\prime \prime}}{B}-\frac{A^{\prime} B^{\prime}}{B}+\frac{1}{2} A\left(\frac{B^{\prime}}{B}\right)^{2}-\frac{4 N^{2} A}{B^{2}}-\frac{1}{2 N^{2} A}, \\
& \bar{e}(r)=\frac{1}{2 N^{2} A}-\frac{4 N^{2} A}{B^{2}}-\frac{1}{2} A\left(\frac{B^{\prime}}{B}\right)^{2}, \\
& \bar{f}(r)=-\frac{A^{\prime} B^{\prime}}{8 N^{2} A}+\frac{1}{B} .
\end{aligned}$$

22 Component
$$a(r) h_{22}^{\prime \prime}+b(r) h_{22}^{\prime}+c(r) h_{00}+d(r) h_{11}+e(r) h_{22}+f(r) h_{33}=-\lambda h_{22},$$
with
$$\begin{aligned}
a(r) & =\bar{a}(r), \\
b(r) & =\bar{b}(r), \\
c(r) & =\bar{c}(r),
\end{aligned} \quad \text { and } \quad \begin{aligned}
& d(r)=\bar{e}(r), \\
& e(r) \\
& f(r) \\
& \bar{d}(r),
\end{aligned}$$
Where the overbar denotes the coefficients for (A.1).
00 Component
$$a(r) h_{00}^{\prime \prime}+b(r) h_{00}^{\prime}+c(r) h_{00}+d(r) X+f(r) h_{33}=-\lambda h_{00},$$
with
$$\begin{aligned}
& a(r)=A, \\
& b(r)=3 A^{\prime}+\frac{A B^{\prime}}{B},
\end{aligned}$$
$$\begin{aligned}
& c(r)=\frac{A^{\prime 2}}{2 A}+\frac{A^{\prime} B^{\prime}}{B}-A\left(\frac{B^{\prime}}{B}\right)^{2}+A^{\prime \prime}, \\
& d(r)=-\frac{A^{\prime} B^{\prime}}{8 A B^{2}}+\frac{B^{\prime 2}}{4 B^{3}}-\frac{B^{\prime \prime}}{4 B^{2}}, \\
& f(r)=\frac{A^{\prime 2}}{32 N^{2} A^{3}}-\frac{A^{\prime \prime}}{16 N^{2} A^{2}},
\end{aligned}$$
and $X=h_{11}+h_{22}$.
33 Component
$$a(r) h_{33}^{\prime \prime}+b(r) h_{33}^{\prime}+c(r) h_{00}+d(r) X+f(r) h_{33}=-\lambda h_{33},$$
with
$$\begin{aligned}
& a(r)=A, \\
& b(r)=-A^{\prime}+\frac{A B^{\prime}}{B}, \\
& c(r)=8 N^{2} A A^{\prime 2}-16 N^{2} A^{2} A^{\prime \prime}, \\
& d(r)=\frac{16 N^{4} A^{2}}{B^{3}}-\frac{2 N^{2} A A^{\prime} B^{\prime}}{B^{2}}, \\
& f(r)=-A^{\prime \prime}+\frac{A^{\prime 2}}{2 A}-\frac{A^{\prime} B^{\prime}}{B}-\frac{4 N^{2} A}{B^{2}},
\end{aligned}$$
and $X=h_{11}+h_{22}$.

\section*{Constraint Equations}

The above system of equations is consistent with the transverse and tracefree conditions on $h_{a b}$. This gives us the constraint equation
$$A h_{00}+\frac{1}{4 B}\left(h_{11}+h_{22}\right)+\frac{1}{16 N^{2} A} h_{33}=0,$$
coming from the traceless condition $h^{a}{ }_{a}=0$, and
$$A h_{00}^{\prime}+\left(\frac{3}{2} A^{\prime}+\frac{A B^{\prime}}{B}\right) h_{00}-\frac{B^{\prime}}{8 B^{2}}\left(h_{11}+h_{22}\right)-\frac{A^{\prime}}{32 N^{2} A^{2}} h_{33}=0,$$
which comes from the transverse condition $\nabla_{a} h^{a b}=0$.

\section*{References}
[1] J. M. Maldacena, Adv. Theor. Math. Phys. 2 (1998) 231. [arXiv:hep-th/9711200].
[2] M. M. Akbar, Nucl. Phys. B 663 (2003) 215. |arXiv:gr-qc/0301007|.
[3] M. M. Akbar and P. D. D'Eath, Nucl. Phys. B 648 (2003) 397 [arXiv:gr-qc/0202073].
[4] S. A. Hartnoll and S. P. Kumar, JHEP 0506, 012 (2005). [arXiv:hep-th/0503238].
[5] R. Clarkson, L. Fatibene and R. B. Mann, Nucl. Phys. B 652 (2003) 348. [arXiv:hep-th/0210280]
[6] A. Chamblin, R. Emparan, C. V. Johnson and R. C. Myers, Phys. Rev. D 59, 064010 (1999) [arXiv:hep-th/9808177].
[7] S. W. Hawking, C. J. Hunter and D. N. Page, Phys. Rev. D 59, 044033 (1999) [arXiv:hep-th/9809035].
[8] S. W. Hawking and D. N. Page, Commun. Math. Phys. 87 (1983) 577.
[9] T. Prestidge, Phys. Rev. D 61 (2000) 084002 [arXiv:hep-th/9907163].
[10] M. Kleban, M. Porrati and R. Rabadan, JHEP 0508, 016 (2005) |arXiv:hep-th/0409242|.
[11] B. L. Hu, J. Math. Phys. 15 (1974) 1748.
[12] R. E. Young, Phys. Rev. D 28, 2420 (1983).
[13] G. H. Holzegel, [arXiv:gr-qc/0602045].
[14] S. W. Hawking and C. N. Pope, Nucl. Phys. B 146 (1978) 381.
[15] J. S. Langer, Annals Phys. 54 (1969) 258.
[16] S. R. Coleman, in The Whys of Subnuclear Physics, Proceedings of the International School of Subnuclear Physics, Erice, 1977, edited by A. Zichichi (Plenum, New York, 1979).
[17] G. W. Gibbons, S. W. Hawking and M. J. Perry, Nucl. Phys. B 138 (1978) 141.
[18] G. W. Gibbons and M. J. Perry, Nucl. Phys. B 146 (1978) 90.
[19] A. Lichnerowicz, Instutute des Hautes Etudes Scientifiques, Publications Mathématiques, 10 (1961)
[20] A. L. Besse, Einstein Manifolds, Springer-Verlag, Berlin, 1987.
[21] C. N. Pope, J. Phys. A 15 (1982) 2455.
[22] R. Emparan, C. V. Johnson and R. C. Myers, Phys. Rev. D 60 (1999) 104001. [arXiv:hep-th/9903238].
[23] R. B. Mann, Phys. Rev. D 60, 104047 (1999) [arXiv:hep-th/9903229].
[24] G. W. Gibbons, S. A. Hartnoll and C. N. Pope, Phys. Rev. D 67 (2003) 084024 [arXiv:hep-th/0208031].