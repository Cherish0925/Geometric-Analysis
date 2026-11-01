---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: Eguchi-Hanson harmonic spinors revisited]

Clearly $\bar{\partial} \beta=0$ so $\beta$ is a Dirac zero mode provided that
$$0=D \beta=-\bar{\partial}^{*} \beta=-\bar{\partial}^{*} \bar{\partial} \phi=g^{\mu \bar{\nu}} \partial_{\mu} \partial_{\bar{\nu}} \phi=\bar{\partial} \partial \phi=\triangle \phi .$$
Take $\phi$ to be a real function of $s$ and set $\chi=\mathrm{d} \phi / \mathrm{d} s$, so that
$$\beta=\chi(s) \bar{\partial} s .$$
We have $\partial \beta=\chi^{\prime} \partial s \wedge \bar{\partial} s+\chi \partial \bar{\partial} s$ so contracting with the inverse metric we get
$$-\bar{\partial}^{*} \beta=g^{\nu \bar{\mu}}\left(\chi^{\prime} \bar{z}_{\mu} z_{\nu}+\chi \delta_{\nu \mu}\right) .$$
Using (4.37) we calculate
$$\operatorname{Tr}\left(g^{-1}\right)=\frac{1}{F}\left(n+1+\frac{\kappa}{s^{n+1}}\right)=\frac{n}{F}+F^{n}, \quad \bar{z}_{\mu} z_{\nu} g^{\nu \bar{\mu}}=\frac{1}{F}\left[s+\frac{\kappa}{s^{n}}\right]=s F^{n} .$$
Therefore, $\beta$ is a zero mode if
$$\chi^{\prime}\left[s+\frac{\kappa}{s^{n}}\right]+\chi\left(n+1+\frac{\kappa}{s^{n+1}}\right)=0,$$
which integrates to
$$\chi=\frac{1}{s^{n+1}\left(1+\frac{\kappa}{s^{n+1}}\right)^{\frac{n}{n+1}}}=\frac{1}{s^{n+1} F^{n}} .$$
Thus
$$\begin{aligned}
& \beta=\chi(s) z \mathrm{~d} \bar{z}=\frac{z \mathrm{~d} \bar{z}}{s^{n+1} F^{n}} \\
& \tilde{\omega}=2 i \mathrm{~d}\left(\frac{z \mathrm{~d} \bar{z}}{s^{n+1} F^{n}}\right)
\end{aligned}$$
Note that for $n=1$ we recover (2.42).
The 2-form $\tilde{\omega}=2 i \mathrm{~d} \beta$ has components
$$\tilde{\omega}_{\mu \bar{\mu}}=-2 i \frac{n}{s^{n+1} F^{2 n+1}}, \quad \tilde{\omega}_{\mu \bar{\nu}}=-2 i\left(1+\frac{n}{F^{n+1}}\right) \frac{z_{\mu} \bar{z}_{\nu}}{s^{n+2} F^{2 n+1}}, \mu \neq \nu .$$
One can see that while $\beta$ is not defined for $s=0, \tilde{\omega}$ is a globally defined 2-form. To check the $L^{2}$ condition we need to integrate $|\tilde{\omega}|^{2}$ with respect to the volume element $r^{2 n+1} \mathrm{~d} r$ where $r=\sqrt{s}$. For large $r$ we have $F \sim 1, g^{\rho \bar{\nu}} \sim \delta^{\rho \nu},|\tilde{\omega}|^{2} \sim r^{4(n+1)}$ hence $|\tilde{\omega}|^{2}$ is integrable. On the other hand $\beta$ is not $L^{2}$. In fact since
$$\partial_{z_{\mu}}^{b}=F^{\prime} \bar{z}_{\mu} z_{\nu} \mathrm{d} z^{\bar{\nu}}+F \mathrm{~d} z^{\bar{\nu}} \quad \Rightarrow \quad z^{\mu} \partial_{z_{\mu}}^{b}=\frac{z_{\nu} \mathrm{d} \bar{z}^{\nu}}{F^{n}},$$
the metric dual $\beta^{\sharp}$ of $\beta$ is
$$\beta^{\sharp}=\beta^{\nu} \partial_{z_{\nu}}, \quad \beta^{\nu}=g^{\bar{\mu} \nu} \beta_{\bar{\mu}}=\chi z^{\nu} F^{n}=\frac{z^{\nu}}{s^{n+1}} .$$
Thus, the squared norm of $\beta$ is
$$|\beta|^{2}=\beta^{\nu} \bar{\beta}_{\nu}=\frac{1}{s^{2 n+1} F^{n}},$$
which is not $L^{2}$ due to the logarithmic divergence near $r=0$.
Finally, we want to normalise $\tilde{\omega}$ so that it is the curvature of a connection $\mathcal{A}$. To do so, we need to impose the quantisation condition
$$\frac{i}{2 \pi} \int_{\Sigma} \mathrm{d} \mathcal{A}=\ell \in \mathbb{Z}$$
where $\Sigma$ is any generator of $H^{2}(K, \mathbb{Z})=\mathbb{Z}$. We can take $\Sigma$ to be the $\mathbb{C} P^{1}$ obtained setting $\zeta=0=w_{2}=\cdots=w_{n}$. To compute the flux of $\tilde{\omega}$ over $\Sigma$ we switch to $\left(w_{i}, \zeta\right)$ coordinates. Using (4.21) we find
$$\tilde{\omega}=\frac{2 i}{n+1}\left(\frac{\mathrm{~d} \log \zeta+\alpha}{\left(\kappa+|\zeta|^{2}\right)^{\frac{n}{n+1}}}\right),$$
for $\alpha$ given by (4.12). It follows that
$$\left.\tilde{\omega}\right|_{\Sigma}=\frac{\left.2 i \mathrm{~d} \alpha\right|_{\Sigma}}{(n+1) \kappa^{\frac{n}{n+1}}} .$$
Since $\frac{i}{2 \pi} \frac{\left.\mathrm{~d} \alpha\right|_{\Sigma}}{(n+1)}$ has unit flux over $\Sigma$, the required normalisation is
$$\mathcal{A}=\ell(A-\bar{A}), \quad A=\kappa^{\frac{n}{n+1}} \frac{z \mathrm{~d} \bar{z}}{2 s^{n+1} F^{n}}$$
which for $n=1$ gives back (2.49).
The analogue of the $n=1$ Killing vector field $X_{3}$ generating translation along the circles $|\zeta|=$ const of the fibres is
$$\xi=\frac{i}{2}\left(z^{\nu} \partial_{\nu}-\bar{z}^{\nu} \partial_{\bar{\nu}}\right)$$
Using (4.53) we see that
$$\xi^{b}=\frac{i}{2}\left(\frac{z \mathrm{~d} \bar{z}-\bar{z} \mathrm{~d} z}{F^{n}}\right) \quad \Rightarrow \quad 2 \mathrm{~d} \xi^{b}=2 i \mathrm{~d}\left(\frac{z \mathrm{~d} \bar{z}}{F^{n}}\right) .$$
Since $F$ satisfies the identity
$$F-\frac{\kappa}{F^{n} s^{n+1}}=\frac{1}{F^{n}},$$
it follows that
$$\omega-\kappa \tilde{\omega}=2 i \mathrm{~d}\left(\frac{z \mathrm{~d} \bar{z}}{F^{n}}\right)=2 \mathrm{~d} \xi^{b}$$
4.4. Zero modes of the twisted Dirac operator on $\mathcal{O}(-n-1)$. As already mentioned, by the same argument used for EH, the canonical spin- $c$ structure on $K=\mathcal{O}(-n-1)$ admits no non-trivial $L^{2}$ harmonic spinor. In this section we consider the problem of normalisable zero modes with respect to the Dirac operator twisted by the connection (4.59). We will limit ourselves to the study of zero modes in $\Lambda^{0,1}(K)$.

Take the ansatz
$$\sigma=P\left(z_{i}\right) h(s) \bar{\partial} s,$$
where $P$ is a function of $z_{1}, \ldots, z_{n+1}$ only, so that the equation $\bar{\partial} \sigma=0$ is automatically satisfied. The remaining equation is the projection onto $\Lambda^{0}(K)$ of
$$\partial \sigma=-\ell \bar{A} \wedge \sigma .$$
One has
$$\partial \sigma=h \partial_{i} P \mathrm{~d} z^{i} \wedge \bar{\partial} s+P h^{\prime} \partial s \wedge \bar{\partial} s+P h \partial \bar{\partial} s .$$
The projections of $\partial \bar{\partial} s, \partial s \wedge \bar{\partial} s$ onto $\Lambda^{0}(K)$ are given by (4.47), and
$$h z_{\mu} \partial_{\nu} P g^{\mu \bar{\nu}}=h z_{\mu} \partial_{\nu} f\left(\frac{\delta^{\nu \mu}}{F}+\frac{\kappa}{s^{n+2} F} \bar{z}^{\mu} z^{\nu}\right)=h F^{n} z_{\mu} \partial_{\mu} P .$$
Now take $P$ to be a homogeneous polynomial in $\left(z_{1}, \ldots, z_{n+1}\right)$ of degree $\delta$, so that $z_{\mu} \partial_{\mu} P=\delta P$. Then
$$-\bar{\partial}^{*} \sigma=\frac{P}{F}\left(F^{n+1}\left(\delta h+h^{\prime} s+h\right)+n h\right) .$$

We also need to compute the $\Lambda^{0}(K)$ projection of $\mathcal{A} \wedge \sigma=\bar{A} \wedge \sigma$. Since
$$\bar{A}=\kappa^{\frac{n}{n+1}} \frac{\partial s}{2 s^{n+1} F^{n}},$$
we obtain
$$-\bar{A}_{\mu} \sigma_{\nu} g^{\mu \bar{\nu}}=-\kappa^{\frac{n}{n+1}} \frac{P h z_{\nu} \bar{z}_{\mu} g^{\nu \bar{\mu}}}{2 s^{n+1} F^{n}}=-\kappa^{\frac{n}{n+1}} \frac{P h}{2 s^{n}} .$$
Therefore, the twisted Dirac equation becomes the following ODE for $h$,
$$F^{n+1}\left((\delta+1) h+h^{\prime} s\right)+n h=\kappa^{\frac{n}{n+1}} \ell \frac{h F}{2 s^{n}} .$$

Equivalently
$$(\log h)^{\prime}=\frac{\ell \kappa^{\frac{n}{n+1}}}{2 F^{n} s^{n+1}}-\frac{\delta+1}{s}-\frac{n}{s F^{n+1}},$$
which has solution
$$h=h_{0} f, \quad h_{0}=\frac{1}{F^{n} s^{\delta+n+1}} .$$
Here $h_{0}$ solves (4.72) for $\ell=0$, and $f$ satisfies
$$(\log f)^{\prime}=\frac{\ell \kappa^{\frac{n}{n+1}}}{2 F^{n} s^{n+1}}$$

To discuss normalisability we only need the behaviour of $f$ for small and large $s$, which is
$$f \sim \begin{cases}s^{\ell / 2} & \text { for } s \ll 1, \\ \exp \left(-\frac{\ell \kappa^{\frac{n}{n+1}}}{2 n} \frac{1}{s^{n}}\right) & \text { for } s \gg 1 .\end{cases}$$
Since $|P|^{2}=s^{\delta},|\bar{\partial} s|^{2}=F^{n} s$, the squared norm of $\sigma$ is
$$|\sigma|^{2}=|P|^{2} h^{2}|\bar{\partial} s|^{2}=\frac{f^{2}}{F^{n} s^{\delta+2 n+1}},$$
which is to be integrated with respect to the volume element $r^{2 n+1}$ for $r=\sqrt{s}$. For large $r$ we have $F \sim 1$ so $|\sigma|^{2} r^{2 n+1} \mathrm{~d} r \sim r^{-(2 \delta+2 n+1)} \mathrm{d} r$ which always gives a finite contribution. For small $r$ we have $f \sim r^{\ell}, F \sim \kappa^{\frac{1}{n+1}} r^{-2}$, hence $|\sigma|^{2} r^{2 n+1} \mathrm{~d} r \sim r^{2 \ell-2 \delta-1} \mathrm{~d} r$ and square-integrability requires
$$\ell>\delta .$$
Note the similarity with the condition (3.46) obtained for $n=1$, where we took $\delta=2 N$. Note also how the (untwisted, not $L^{2}$ ) spinor $h_{0} \bar{\partial} s$ obtained for $\ell=0, \delta=0$ is, up to scale, equal to the connection (4.59) with harmonic $L^{2}$ curvature, again in complete analogy with the $n=1$ case.

\section*{5. Discussion}

The main result of this work is the explicit description of the $L^{2}$ zero modes of the (twisted) Dirac operator on both the Eguchi-Hanson metric, see (3.41), and its higher dimensional generalisation given by the Calabi metric on $\mathcal{O}(-n-1)$. As expected, for $n=1$ the EH zero modes organise themselves into multiplets of the EH isometry group $S U(2)$. The dimension of the space of zero modes is controlled by the integer $\ell$, see (2.49), that controls the twist. The Dirac operator index analysis in [4] confirms that the zero modes obtained are all the zero modes, and so for the EH space the problem of finding the harmonic spinors is completely solved.

Far from arbitrary, the $U(1)$ connection used for the twist is preferred geometrically for multiple reasons. First, its curvature is the unique (up to scale) harmonic $L^{2}$ 2-form on EH. Second, it is a connection on the total space of the $S^{1}$ bundle over EH arising as a level set in the process of the hyperkähler reduction from $\mathbb{H}^{2}$. In passing, this suggests that the twisted Dirac operator may also be understood as an appropriate dimensional reduction of the untwisted Dirac operator on $\mathbb{H}^{2}$. It would be very interesting to see whether this is the case, and whether the harmonic spinors (3.41) can also be understood as arising from the dimensional reduction of some very simple spinors on $\mathbb{C}^{4}$. We leave this to further work. Third, the $U(1)$ connection with $L^{2}$ curvature agrees with the lowest lying (untwisted, not $L^{2}$ ) Dirac zero mode.

The EH metric is the $n=1$ case of Calabi's family of Ricci-flat Kähler metrics on $\mathcal{O}(-n-1)$, $n \in \mathbb{N}$. As we have shown, many of the EH results generalise to higher $n$. First, the description (4.31) of the metric in terms of "symmetrical" coordinates completely parallels the case of EH. Second, for all values of $n$ there is a unique $L^{2}$ harmonic 2-form $\tilde{\omega}$, see (4.51), which also arises as the curvature of the lowest lying zero mode of the untwisted Dirac operator, and whose connection can be used to twist the Dirac operator. Moreover, $\tilde{\omega}$ differs from the Kähler form $\omega$ by a constant multiple of $\mathrm{d} \xi^{b}$, see (4.63), for $\xi$ a Killing vector field generating the isometric U(1) action on the fibre. Interestingly, the forms $\omega, \tilde{\omega}, \mathrm{d} \xi^{b}$ are all harmonic although only $\tilde{\omega}$
is $L^{2}$. Third, the EH zero modes (3.41) of the Dirac operator twisted by this preferred $U(1)$ connection have analogues (4.64) in the general case. These general zero modes again fall into irreducible representations of the $U(n+1)$ isometry group, and the number of allowed zero modes is controlled by the integer $\ell$ that determines the curvature flux.

The cases $n=1$ and $n>1$ also present an important difference: the EH metric is hyperkähler while for $n>1$ Calabi's metric is Calabi-Yau but not hyperkähler. For this reason, for $n>1$ there can be no analogue of the hyperkähler quotient derivation of the EH metric reviewed in section 2.5, but one may still wonder if the metric could be obtained as the Kähler reduction of some simpler higher-dimensional metric.

In the general case, we cannot claim that the Dirac zero modes that we have found exhaust all $L^{2}$ harmonic spinors. For EH it is possible to come to this conclusion thanks to the fact that, since the curvature of the twisting connection is self-dual, there are no zero modes in $W^{+}$and the index of the Dirac operator is equal to the number of $L^{2}$ zero modes in $W^{-}$. This self-duality argument does not extend to higher $n$, and we have no alternative argument showing that there are no $L^{2}$ zero modes in $W^{+}$. In fact, we have only analysed zero modes belonging to $\Lambda^{0,1}$ and we also do not know if there are additional zero modes in the spaces $\Lambda^{0,2 k+1}, 2 k \leq n$. A complete answer to these questions is left for future work, along with the interesting problem of studying zero modes of the Dirac operator twisted by $L^{2}$ harmonic forms of degree other than two.

Another outcome of this work is the development of a set of rules for computing the spin- $c$ Dirac operator on a Kähler manifold. Indeed, we have shown that the computation of the action of this Dirac operator on spinors is no more complicated than the computation of the exterior derivative of differential forms. The only additional operation needed is the application of the metric contraction to the result of the exterior derivative, to map the latter into the space $\Lambda^{0, \bullet}$ where spinors live. This gives extremely simple computational rules and makes the formalism of spinors as differential forms extremely convenient for explicit calculations involving the Dirac operator. We hope this work will lead to a better familiarity of the community with the very efficient computational tool that spin- $c$ spinors provide.

We close with some remarks on what motivated us to embark on the present investigation. The Calabi construction can be applied to an arbitrary Kähler manifold $M$ with non-zero scalar curvature, and gives a Ricci-flat Kähler metric on the total space of the canonical bundle of $M$. Applying this construction to $\mathbb{C P}^{1} \times \mathbb{C P}^{2}$ is particularly interesting because the resulting Ricciflat metric has the Standard Model gauge group as its isometry group. The resulting space is Calabi-Yau with holonomy group $S U(4)$. Its metric is asymptotically conical, with the metric on the base of the cone being the nearly parallel $G_{2}$ metric $M(3,2)$ discussed in particular in [7]. We are interested in determining the $L^{2}$ harmonic spinors of (the appropriately twisted) Dirac operator on this space. The present work can be considered as setting the stage for this more involved computation.

Acknowledgements. The authors are grateful to Bernd Schroers for introducing them to each other, and for participating in the early stages of this collaboration. GF thanks the Simons Foundation for its support under the Simons Collaboration on Special Holonomy in Geometry, Analysis and Physics [grant number 488631].

\section*{Appendix A. The geometry of $\mathbb{C}^{2}$}

In this appendix we want to relate the descriptions of Euclidean $\mathbb{R}^{4}=\mathbb{C}^{2}$ as a cohomogeneityone space with respect to the action of $S U(2)$, as a complex manifold and as a complex line bundle. To that end it is convenient to first review the geometry of $S U(2)$.
A.1. The geometry of $S U(2)$. As it is well known, $S^{3} \simeq S U(2)$. A possible parametrisation of left-invariant 1-forms on $S U(2)$ is
$$\begin{aligned}
& \eta_{1}=+\sin \psi \mathrm{d} \theta-\cos \psi \sin \theta \mathrm{d} \phi \\
& \eta_{2}=-\cos \psi \mathrm{d} \theta-\sin \psi \sin \theta \mathrm{d} \phi \\
& \eta_{3}=\mathrm{d} \psi+\cos \theta \mathrm{d} \phi
\end{aligned}$$
where $\theta \in[0, \pi], \phi \in[0,2 \pi), \psi \in[0,4 \pi)$. Taking the same range for $\theta, \phi$ with $\psi \in[0,2 \pi)$ gives instead a parametrisation of $S U(2) / \mathbb{Z}_{2}=S O(3)$. Note that the forms (A.1) satisfy
$$\mathrm{d} \eta_{i}=+\frac{1}{2} \epsilon_{i j k} \eta_{j} \wedge \eta_{k} .$$

The left-invariant vector fields on $S U(2)$ satisfying $\eta_{i}\left(X_{j}\right)=\delta_{i j}$ are
$$\begin{aligned}
& X_{1}=+\sin \psi \frac{\partial}{\partial \theta}+\frac{\cos \psi}{\sin \theta}\left(\cos \theta \frac{\partial}{\partial \psi}-\frac{\partial}{\partial \phi}\right) \\
& X_{2}=-\cos \psi \frac{\partial}{\partial \theta}+\frac{\sin \psi}{\sin \theta}\left(\cos \theta \frac{\partial}{\partial \psi}-\frac{\partial}{\partial \phi}\right) \\
& X_{3}=+\frac{\partial}{\partial \psi} .
\end{aligned}$$
They satisfy the $\mathfrak{s u}(2)$ Lie algebra relation
$$\left[X_{i}, X_{j}\right]=-\epsilon_{i j k} X_{k} .$$
In fact it can be checked that $X_{i}$ is the left-invariant vector field associated to $\frac{i}{2} \sigma_{i}$, for $\left(\sigma_{i}\right)$ the Pauli matrices.

We can also introduce right-invariant 1-forms $\left(\zeta_{i}\right)$ and vector fields $\left(Y_{i}\right)$,
$$\begin{aligned}
& \zeta_{1}=-\cos \phi \sin \theta \mathrm{d} \psi+\sin \phi \mathrm{d} \theta \\
& \zeta_{2}=+\sin \phi \sin \theta \mathrm{d} \psi+\cos \phi \mathrm{d} \theta \\
& \zeta_{3}=\mathrm{d} \phi+\cos \theta \mathrm{d} \psi \\
Y_{1}= & \sin \phi \frac{\partial}{\partial \theta}+\frac{\cos \phi}{\sin \theta}\left(\cos \theta \frac{\partial}{\partial \phi}-\frac{\partial}{\partial \psi}\right) \\
Y_{2}= & \cos \phi \frac{\partial}{\partial \theta}-\frac{\sin \phi}{\sin \theta}\left(\cos \theta \frac{\partial}{\partial \phi}-\frac{\partial}{\partial \psi}\right) \\
Y_{3}= & \frac{\partial}{\partial \phi}
\end{aligned}$$
satisfying $\zeta_{i}\left(Y_{j}\right)=\delta_{i j}$,
$$\left[Y_{i}, Y_{j}\right]=+\epsilon_{i j k} Y_{k}, \quad \mathrm{~d} \zeta_{i}=-\frac{1}{2} \epsilon_{i j k} \zeta_{k}, \quad\left[X_{i}, Y_{j}\right]=0$$

The metric
$$g_{S^{3}}=\frac{1}{4}\left(\eta_{1}^{2}+\eta_{2}^{2}+\eta_{3}^{2}\right)=\frac{1}{4}\left(\zeta_{1}^{2}+\zeta_{2}^{2}+\zeta_{3}^{2}\right)$$
is the round metric on the 3-sphere of unit radius, or equivalently the bi-invariant metric on $S U(2)$. In terms of the latter description it is clear that the metric is invariant under both a left and right $S U(2)$ action. The left action is generated by the right-invariant vector fields (A.6). Such vector fields satisfy $L_{Y_{i}} \eta_{j}=0$. The right $S U(2)$ action is generated by the left-invariant vector fields (A.3). We have
$$\begin{aligned}
L_{X_{i}} \zeta_{j} & =L_{Y_{i}} \eta_{j}=0 \\
L_{X_{i}} \eta_{j} & =-\epsilon_{i j k} \eta_{k}, \quad L_{Y_{i}} \zeta_{j}=+\epsilon_{i j k} \zeta_{k}
\end{aligned}$$
A.2. The geometry of $\mathbb{C}^{2}$. The orbit structure of $\mathbb{C}^{2} \simeq \mathbb{R}^{4}$ with respect to the $S U(2)$ action is obtained by writing $\mathbb{R}^{4}=\{0\} \cup\left((0, \infty) \times S^{3}\right)$. Introducing a radial coordinate $r \in[0, \infty)$ transverse to the $S U(2)$ orbits we can write the Euclidean metric on $\mathbb{C}^{2}$ as
$$g_{\mathbb{C}^{2}}=\mathrm{d} r^{2}+\frac{r^{2}}{4}\left(\eta_{1}^{2}+\eta_{2}^{2}+\eta_{3}^{2}\right)$$
The quantities $\left(\eta_{i}\right),\left(\zeta_{i}\right),\left(X_{i}\right),\left(Y_{i}\right)$ extend to well-defined 1-forms and vector fields on $\mathbb{R}^{4} \backslash\{0\}$.

As a real manifold $\mathbb{R}^{4}$ has isometry group $O(4)$. We can identify a point $\left(z_{1}, z_{2}\right) \in \mathbb{C}^{2} \backslash\{0\}$ with a pair $(r, x)$ where $x$ is the $\operatorname{SU}(2)$ element given by
$$\frac{1}{\left|z_{1}\right|^{2}+\left|z_{2}\right|^{2}}\left(\begin{array}{cc}
z_{1} & -\bar{z}_{2} \\
z_{2} & \bar{z}_{1}
\end{array}\right)$$
and $r=\sqrt{\left|z_{1}\right|^{2}+\left|z_{2}\right|^{2}}$. Left and right matrix multiplication of (A.11) by an $S U(2)$ element give raise to isometries, with the left action generated by the right-invariant vector fields $\left(Y_{i}\right)$ and the right action by the left-invariant vector fields $\left(X_{i}\right)$. Explicitly is $h \in S U(2)$ is given by
$$h=\left(\begin{array}{cc}
a & -\bar{b} \\
b & \bar{a}
\end{array}\right)$$
the left and right $S U(2)$ action are given by (A.13), (A.14) respectively,
$$\begin{array}{cc}
z_{1} \mapsto a z_{1}-\bar{b} z_{2}, & z_{2} \mapsto b z_{1}+\bar{a} z_{2}, \\
z_{1} \mapsto a z_{1}-b \bar{z}_{2}, & z_{2} \mapsto a z_{2}+b \bar{z}_{1} .
\end{array}$$
Since $(S U(2) \times S U(2)) / \mathbb{Z}_{2}=S O(4)$, the left and right $S U(2)$ action give the (connected component of the) full isometry group of $\mathbb{R}^{4}$. The $\mathbb{Z}_{2}$ quotient corresponds to the fact that for $a=\bar{a}$, $b=0$, which in $S U(2)$ implies $a= \pm 1$, left and right action result in the same transformation.

The map (A.14) is not complex linear. In fact $\mathbb{C}^{2}$ as a complex manifold has metric
$$g_{\mathbb{C}^{2}}=\left|\mathrm{d} z_{1}\right|^{2}+\left|\mathrm{d} z_{2}\right|^{2},$$
complex structure
$$J\left(\partial / \partial z_{i}\right)=+i \partial / \partial z_{i}, \quad J\left(\mathrm{~d} z_{i}\right)=-i \mathrm{~d} z_{i},$$
and the smaller isometry group $U(2) \subset S O(4)$. There is a group isomorphism $U(2)=(S U(2) \times$ $U(1)) / \mathbb{Z}_{2},(h, u) \mapsto h u$. The (left) $S U(2)$ action is (A.13) and the $U(1)$ action is diagonal,
$$\left(z_{1}, z_{2}\right) \cdot \mathrm{e}^{i t}=\left(z_{1}, z_{2}\right) \mathrm{e}^{i t} .$$
Looking at (A.14) we see that (A.17) is the $U(1)$ action obtained restricting the right $S U(2)$ action to the $U(1)$ subgroup obtained by setting $b=0$.

We now define an orthonormal frame $\left(X_{1}, X_{2}, X_{3}, X_{4}\right)$ consisting of real vector fields adapted to the action (A.17) and the complex structure $J$,
$$\begin{aligned}
& X_{1}=-\frac{i}{2}\left(\bar{z}_{2} \frac{\partial}{\partial z_{1}}-\bar{z}_{1} \frac{\partial}{\partial z_{2}}-z_{2} \frac{\partial}{\partial \bar{z}_{1}}+z_{1} \frac{\partial}{\partial \bar{z}_{2}}\right) \\
& X_{2}=-\frac{1}{2}\left(\bar{z}_{1} \frac{\partial}{\partial z_{2}}-\bar{z}_{2} \frac{\partial}{\partial z_{1}}+z_{1} \frac{\partial}{\partial \bar{z}_{2}}-z_{2} \frac{\partial}{\partial \bar{z}_{1}}\right) \\
& X_{3}=+\frac{i}{2}\left(z_{1} \frac{\partial}{\partial z_{1}}+z_{2} \frac{\partial}{\partial z_{2}}-\bar{z}_{1} \frac{\partial}{\partial \bar{z}_{1}}-\bar{z}_{2} \frac{\partial}{\partial \bar{z}_{2}}\right) \\
& X_{4}=-\frac{1}{2}\left(z_{1} \frac{\partial}{\partial z_{1}}+z_{2} \frac{\partial}{\partial z_{2}}+\bar{z}_{1} \frac{\partial}{\partial \bar{z}_{1}}+\bar{z}_{2} \frac{\partial}{\partial \bar{z}_{2}}\right) .
\end{aligned}$$
The frame $\left(X_{i}\right)$ is adapted in the sense that $X_{3}$ is the infinitesimal generator of the action (A.17), $X_{4}=J X_{3}, X_{2}=J X_{1}$ and $\left(X_{1}, J X_{1}\right)$ is the $g_{\mathbb{C}^{2}}$-orthogonal complement of $\left(X_{3}, J X_{3}\right)$. More precisely,
$$X_{3}-i J X_{3}=i\left(z_{1} \frac{\partial}{\partial z_{1}}+z_{2} \frac{\partial}{\partial z_{2}}\right)$$
generates (A.17) and $X_{3}$ is the corresponding real holomorphic vector field. We have
$$\left|X_{1}\right|^{2}=\left|X_{2}\right|^{2}=\left|X_{3}\right|^{2}=\left|X_{4}\right|^{2}=\frac{1}{4}\left(\left|z_{1}\right|^{2}+\left|z_{2}\right|^{2}\right),$$
where $\left|X_{i}\right|^{2}=g_{\mathbb{C}^{2}}\left(X_{i}, X_{i}\right)$. As we will show, the vector fields $\left(X_{1}, X_{2}, X_{3}\right)$ in (A.18) are the left-invariant vector fields (A.3) expressed in terms of complex coordinates.

Denoting by $X^{b}$ the $g_{\mathbb{C}^{2}}$-metric dual of $X$ we have
$$\begin{aligned}
\theta_{1} & =X_{1}^{b}=-\frac{i}{4}\left(z_{1} \mathrm{~d} z_{2}-z_{2} \mathrm{~d} z_{1}-\bar{z}_{1} \mathrm{~d} \bar{z}_{2}+\bar{z}_{2} \mathrm{~d} \bar{z}_{1}\right)=-\frac{1}{2} \operatorname{Im}\left(z_{1} \mathrm{~d} z_{2}-z_{2} \mathrm{~d} z_{1}\right) \\
\theta_{2} & =X_{2}^{b}=-\frac{1}{4}\left(z_{1} \mathrm{~d} z_{2}-z_{2} \mathrm{~d} z_{1}+\bar{z}_{1} \mathrm{~d} \bar{z}_{2}-\bar{z}_{2} \mathrm{~d} \bar{z}_{1}\right)=+\frac{1}{2} \operatorname{Re}\left(z_{1} \mathrm{~d} z_{2}-z_{2} \mathrm{~d} z_{1}\right) \\
\theta_{3} & =X_{3}^{b}=+\frac{i}{4}\left(z_{1} \mathrm{~d} \bar{z}_{1}+z_{2} \mathrm{~d} \bar{z}_{2}-\bar{z}_{1} \mathrm{~d} z_{1}-\bar{z}_{2} \mathrm{~d} z_{2}\right)=+\frac{1}{2} \operatorname{Im}\left(\bar{z}_{1} \mathrm{~d} z_{1}+\bar{z}_{2} \mathrm{~d}_{2}\right) \\
\theta_{4} & =X_{4}^{b}=-\frac{1}{4}\left(z_{1} \mathrm{~d} \bar{z}_{1}+z_{2} \mathrm{~d} \bar{z}_{2}+\bar{z}_{1} \mathrm{~d} z_{1}+\bar{z}_{2} \mathrm{~d} z_{2}\right)=-\frac{1}{2} \operatorname{Re}\left(\bar{z}_{1} \mathrm{~d} z_{1}+\bar{z}_{2} \mathrm{~d}_{2}\right)
\end{aligned}$$
Thus
$$g_{\mathbb{C}^{2}}=\sum_{i=1}^{4} \frac{\theta_{i}^{2}}{\left|X_{i}\right|^{2}}=\frac{\left|\bar{z}_{1} \mathrm{~d} z_{1}+\bar{z}_{2} \mathrm{~d} z_{2}\right|^{2}}{\left|z_{1}\right|^{2}+\left|z_{2}\right|^{2}}+\frac{\left|z_{1} \mathrm{~d} z_{2}-z_{2} \mathrm{~d} z_{1}\right|^{2}}{\left|z_{1}\right|^{2}+\left|z_{2}\right|^{2}},$$
where the first and second addend correspond to the metric restricted to $\operatorname{Span}\left(X_{3}, J X_{3}\right)$, $\operatorname{Span}\left(X_{1}, J X_{1}\right)$ respectively.

The metrics (A.15), (A.10) are related by the diffeomorphism
$$z_{1}=r \cos \left(\frac{\theta}{2}\right) \mathrm{e}^{\frac{i}{2}(\psi+\phi)}, \quad z_{2}=r \sin \left(\frac{\theta}{2}\right) \mathrm{e}^{\frac{i}{2}(\psi-\phi)} .$$
It can be checked the pulling back by (A.23) the vector fields $\left(X_{1}, X_{2}, X_{3}\right)$ in (A.18) map to (A.3), and
$$X_{4}=-\frac{r}{2} \frac{\partial}{\partial r}, \quad \theta_{4}=-\frac{r}{2} \mathrm{~d} r .$$
Note how $\left(X_{3}, X_{4}\right)$ span the $(r, \psi)$ plane. The forms $\eta_{i}, \theta_{i}$ are the metric dual of $X_{i}$ with respect to, respectively, $g_{S^{3}}$ and $g_{\mathbb{C}^{2}}$. For vector fields $X, Y$ tangent to $S^{3}$ we have $g_{S^{3}}(X, Y)=$ $\frac{4}{\left|z_{1}\right|^{2}+\left|z_{2}\right|^{2}} g_{\mathbb{C}^{2}}(X, Y)$, hence
$$\eta_{i}=\left(\frac{4}{\left|z_{1}\right|^{2}+\left|z_{2}\right|^{2}}\right) \theta_{i} .$$

The space $\mathbb{C}^{2} \backslash\{0\}$ can be viewed as a line bundle over $\mathbb{C} P^{1}$. We introduce complex coordinates $(w, \zeta) \in \mathbb{C}^{2}$ on the base and fibre via
$$\left(z_{1}, z_{2}\right)=\frac{\zeta}{\sqrt{1+|w|^{2}}}(w, 1), \quad(w, \zeta)=\left(\frac{z_{1}}{z_{2}}, \sqrt{\left|z_{1}\right|^{2}+\left|z_{2}\right|^{2}} \frac{z_{2}}{\left|z_{2}\right|}\right) .$$
Since
$$\begin{aligned}
\left|z_{1}\right|^{2}+\left|z_{2}\right|^{2} & =|\zeta|^{2} \\
z_{1} \mathrm{~d} z_{2}-z_{2} \mathrm{~d} z_{1} & =-\frac{\zeta^{2} \mathrm{~d} w}{1+|w|^{2}} \\
\bar{z}_{1} \mathrm{~d} z_{1}+\bar{z}_{2} \mathrm{~d} z_{2} & =\bar{\zeta} \mathrm{d} \zeta+\frac{|\zeta|^{2}}{2}\left(\frac{\bar{w} \mathrm{~d} w-w \mathrm{~d} \bar{w}}{1+|w|^{2}}\right)=\bar{\zeta}(\mathrm{d} \zeta+i a \zeta)
\end{aligned}$$
where
$$a=\frac{1}{2 i} \frac{\bar{w} \mathrm{~d} w-w \mathrm{~d} \bar{w}}{1+|w|^{2}}=\frac{\operatorname{Im}(\bar{w} \mathrm{~d} w)}{1+|w|^{2}},$$
we get
$$g_{\mathbb{C}^{2}}=|\mathrm{d} \zeta+i a \zeta|^{2}+\frac{|\zeta|^{2}|\mathrm{~d} w|^{2}}{\left(1+|w|^{2}\right)^{2}} .$$

Thinking of $S^{3}$ as the Hopf fibration $U(1) \hookrightarrow S^{3} \rightarrow \mathbb{C} P^{1}$ we recognise $z$ as an inhomogeneous coordinate on the base $\mathbb{C} P^{1}$ and $\zeta$, for $|\zeta|=|R|$, as the angle parametrising the $U(1)$ fibres. If the value of $|\zeta|$ is allowed to vary in ( $0, \infty$ ) we obtain a parametrisation of ( $0, \infty) \times S^{3}$ viewed as the line bundle $\mathbb{C}^{2} \backslash\{0\} \rightarrow \mathbb{C} P^{1}$. Since
$$\zeta \frac{\partial}{\partial \zeta}=z_{1} \frac{\partial}{\partial z_{1}}+z_{1} \frac{\partial}{\partial z_{2}}$$
the vector field $X_{3}$ translating along the fibres becomes
$$X_{3}=\frac{i}{2}\left(\zeta \frac{\partial}{\partial \zeta}-\bar{\zeta} \frac{\partial}{\partial \bar{\zeta}}\right) .$$

Further parametrising
$$\zeta=r e^{i \chi}, \quad \Leftrightarrow \quad r=|\zeta|=\sqrt{\left|z_{1}\right|^{2}+\left|z_{2}\right|^{2}}, \mathrm{e}^{i \chi}=\frac{z_{2}}{\left|z_{2}\right|},$$
we obtain
$$g_{\mathbb{C}^{2}}=\mathrm{d} r^{2}+r^{2}\left[(\mathrm{~d} \chi+a)^{2}+\frac{|\mathrm{d} w|^{2}}{\left(1+|w|^{2}\right)^{2}}\right],$$
where the term in brackets is the round metric on $S^{3}$. Introducing the usual coordinates $(\theta, \phi)$, $\psi \in[0,4 \pi)$ parametrising the base and fibre of the Hopf fibration as in (A.23) we get
$$\begin{aligned}
& w=\frac{z_{1}}{z_{2}}=\cot \frac{\theta}{2} \mathrm{e}^{i \phi} \\
& \chi=\frac{\psi-\phi}{2}
\end{aligned}$$
so that
$$\begin{aligned}
\frac{|\mathrm{d} w|^{2}}{\left(1+|w|^{2}\right)^{2}} & =\frac{1}{4}\left(\mathrm{~d} \theta^{2}+\sin ^{2} \theta \mathrm{~d} \phi^{2}\right)=\frac{1}{4}\left(\eta_{1}^{2}+\eta_{2}^{2}\right) \\
\mathrm{d} \chi+a & =\frac{\mathrm{d} \psi+\cos \theta \mathrm{d} \phi}{2}=\frac{\eta_{3}}{2}, \quad a=\left(\frac{1+\cos \theta}{2}\right) \mathrm{d} \phi
\end{aligned}$$
recovering (A.10).
The line bundle $\mathbb{C}^{2} \backslash\{0\} \rightarrow \mathbb{C} P^{1}$ is homotopy equivalent to the Hopf fibration. The latter has first Chern number one. In fact
$$\beta=\left.\left[\bar{z}_{1} \mathrm{~d} z_{1}+\bar{z}_{2} \mathrm{~d} z_{2}\right]\right|_{S^{3}}=\left.i \operatorname{Im}\left(\bar{z}_{1} \mathrm{~d} z_{1}+\bar{z}_{2} \mathrm{~d} z_{2}\right)\right|_{S^{3}}=i(\mathrm{~d} \chi+a)=\frac{i}{2} \eta_{3}$$
evaluates to 1 on the generator (A.19) of the $U(1)$ action and so defines a connection on the total space of the Hopf bundle. By Chern-Weyl the first Chern number of the Hopf fibration is
$$\frac{i}{2 \pi} \int_{\mathbb{C} P^{1}} \mathrm{~d} \beta=1$$

The splitting (A.22) can be understood as a special case of a Kähler reduction. Let $M$ be a Kähler manifold with metric $g$ and Kähler form $\omega$. Assume that there is a free Hamiltonian and isometric action of $U(1)$ on $M$ generated by the vector field $\xi$. Let $\mu$ be the associated Hamiltonian, $i_{\xi} \omega=-\mathrm{d} \mu$. Denote by $\Sigma_{c}$ the level set $\mu^{-1}(c)$. It is well known that if $c$ is a regular value of $\mu$ then the quotient $\Sigma_{c} / U(1)$ equipped with the metric and Kähler form induced by $g$ and $\omega$ is a smooth Kähler manifold of complex dimension $\operatorname{dim}_{\mathbb{C}} M-1$. The vector fields $\xi, J \xi$ are respectively tangent and orthogonal to $\Sigma_{c}$. In particular $J \xi$ spans the $g$-orthogonal complement of $T \Sigma_{c}$. Therefore the quotient metric $\bar{g}$ can be identified with the $g$-orthogonal complement of $(\xi, J \xi)$ in $M$,
$$g=\bar{g}+g^{\perp}$$
where $g^{\perp}=\left.g\right|_{\operatorname{Span}(\xi, J \xi)}$. Writing $\theta=g(\xi, \cdot), \theta_{J}=g(J \xi, \cdot)$ we have
$$g=\bar{g}+\frac{\theta^{2}+\theta_{J}^{2}}{g(\xi, \xi)} .$$

Take now $M=\mathbb{C}^{2}$ and consider the $U(1)$ action is generated by the nowhere vanishing vector field $\xi=X_{3}$, which preserves both $g_{\mathbb{C}^{2}}$ and $\omega_{\mathbb{C}^{2}}$. The action is Hamiltonian with
$$\mu=\frac{1}{2}\left(\left|z_{1}\right|^{2}+\left|z_{2}\right|^{2}\right) .$$

Taking a basis $\left(X_{1}, X_{2}=J X_{1}\right)$ for the orthogonal complement of $\left(X_{3}, X_{4}=J X_{3}\right)$ as in (A.18), gives back (A.22),
$$g_{\mathbb{C}^{2}}=\bar{g}+g^{\perp}=\frac{\theta_{1}^{2}+\theta_{2}^{2}}{\left|X_{1}\right|^{2}}+\frac{\theta_{3}^{2}+\theta_{4}^{2}}{\left|X_{3}\right|^{2}}=\frac{\left|z_{1} \mathrm{~d} z_{2}-z_{2} \mathrm{~d} z_{1}\right|^{2}}{\left|z_{1}\right|^{2}+\left|z_{2}\right|^{2}}+\frac{\left|\bar{z}_{1} \mathrm{~d} z_{1}+\bar{z}_{2} \mathrm{~d} z_{2}\right|^{2}}{\left|z_{1}\right|^{2}+\left|z_{2}\right|^{2}} .$$
For $R \neq 0$ the $\mu$ level sets $\left|z_{1}\right|^{2}+\left|z_{2}\right|^{2}=R^{2}$ are 3 -spheres and the induced metric is
$$g_{S_{R}^{3}}=\frac{\theta_{1}^{2}+\theta_{2}^{2}}{\left|X_{1}\right|^{2}}+\frac{\theta_{3}^{2}}{\left|X_{3}\right|^{2}}=\frac{R^{2}}{4}\left[\frac{4|\mathrm{~d} w|^{2}}{\left(1+|w|^{2}\right)^{2}}+4\left(\frac{\operatorname{Im}(\bar{\zeta} \mathrm{~d} \zeta)}{R^{2}}+a\right)^{2}\right]=\frac{R^{2}}{4}\left(\eta_{1}^{2}+\eta_{2}^{2}+\eta_{3}^{2}\right),$$
having used (A.36).

\section*{Appendix B. Calabi's construction}

For reference, we summarise here Calabi's construction [2] of a Ricci-flat Kähler manifold on the canonical bundle of a Kähler-Einstein manifold with scalar curvature $s \neq 0$. We partially follow the presentation given in [17].
B.1. The Chern connection. We recall, see e.g. [14], that a holomorphic vector bundle $E \rightarrow$ $M$ equipped with a Hermitian product $\langle\cdot, \cdot\rangle$ carries a preferred connection ∇ known as the Chern connection. It is characterised by compatibility with the Hermitian product: $\nabla_{X}\left\langle\sigma_{1}, \sigma_{2}\right\rangle=$ $\left\langle X\left(\sigma_{1}\right), \sigma_{2}\right\rangle+\left\langle\sigma_{1}, X\left(\sigma_{2}\right)\right\rangle$ and compatibility with the complex structure on the total space. If $E$ is a line bundle, $\sigma$ a section of $E$ then for some connection form $\alpha$
$$\nabla \sigma=\alpha \otimes \sigma .$$
Compatibility with the Hermitian product implies
$$\mathrm{d} \log \|\sigma\|^{2}=\alpha+\bar{\alpha} .$$
For a holomorphic section (B.2) implies $\alpha=\partial \log \|\sigma\|^{2}$. If instead $\sigma=e$ is unitary, that is $\|e\|^{2}=1$, then the connection is purely imaginary, $\alpha=-\bar{\alpha}$. We recall that if $\alpha$ is the Chern connection on a line bundle $E$ then the $-\alpha$ is the Chern connection on $E^{*}$.

Assume now that $M$ is Kähler and $E=T M \otimes \mathbb{C}$ is the complexified tangent bundle. Denote by $K=\Lambda^{n, 0}(M)$ the canonical bundle of $M$, by $K^{*}$ its dual and let $\alpha$ be the Chern connection on $K, \mathrm{~d} \alpha$ the corresponding curvature. Since $M$ is Kähler, the Chern connection on $E$ is just the Levi-Civita connection on $T M$ extended by complex linearity. The dual $K^{*}$ of the canonical bundle $K=\Lambda^{n, 0}(M)$ of $M$ is the determinant bundle of $E$, so the Chern connection on $K^{*}$ is the trace of the Levi-Civita connection on $T M$, and the Chern connection $\alpha$ on $K$ its opposite. Therefore
$$\mathrm{d} \alpha=i \rho_{M}$$
where $\rho_{M}$ is the Ricci form on $M$. If $M$ is Kähler-Einstein of complex dimension $n$ and scalar curvature $s$ then $\rho_{M}=\frac{s}{2 n} \omega_{M}$, where $\omega_{M}$ is the Kähler form on $M$, hence
$$-i \mathrm{~d} \alpha=\rho_{M}=\frac{s}{2 n} \omega_{M} .$$
B.2. Calabi's construction. In this section $M$ is a Kähler-Einstein manifold of complex dimension $n$ with Riemannian metric $g_{M}$, Kähler form $\omega_{M}$, Riemannian volume element
$$\operatorname{vol}_{M}=\frac{\omega^{n}}{n!}$$
and scalar curvature $s$. The bundle $K$ is the canonical bundle of $M, \alpha$ the connection form of the Chern connection ∇ on $K$. Compatibility of ∇ with the complex structure is equivalent to $\nabla^{0,1}=\bar{\partial}$.

Let $\sigma$ be a unitary section of $K$. Since $\sigma$ is a form of degree $(n, 0), \partial \sigma=0=\nabla^{1,0} \sigma$ and so
$$\mathrm{d} \sigma=\bar{\partial} \sigma=\nabla \sigma=\alpha \wedge \sigma .$$
The Riemannian metric on $M$ induces a Hermitian product $\langle\cdot, \cdot\rangle$ on $K$ given by
$$\sigma \wedge * \bar{\sigma}=\|\sigma\|^{2} \mathrm{vol}_{M} .$$

Since $*: \Lambda^{p, q}(M) \rightarrow \Lambda^{n-q, n-p}(M)$ and $*^{2}=(-1)^{(p+q)^{2}}$, $*$ acts on $\Lambda^{0, n}(M)$ by multiplication by $i^{n^{2}}$. Hence (B.7) is equivalent to
$$\sigma \wedge \bar{\sigma}=(-i)^{n^{2}}\|\sigma\|^{2} \frac{\omega_{M}^{n}}{n!} .$$

Let $\zeta$ be a coordinate on the fibres of $K$, set
$$\theta=\mathrm{d} \zeta+\zeta \alpha .$$
and define
$$\begin{aligned}
\omega & =\lambda\left[u \omega_{M}+\frac{2 i n}{s} u^{\prime} \theta \wedge \bar{\theta}\right], \\
\Omega & =\theta \wedge e,
\end{aligned}$$
where $u$ is a function of $|\zeta|^{2}$ and $\lambda$ is some non-zero constant. We are now going to show that $(\omega, \Lambda)$ satisfy
$$\begin{aligned}
\mathrm{d} \omega & =0 \\
\mathrm{~d} \Omega & =0 \\
\Omega \wedge \omega & =0 \\
\Omega \wedge \bar{\Omega} & =C \omega^{n+1}
\end{aligned}$$
Closure of $\Omega$ means that the complex structure defined by declaring $\theta$ to be a $(1,0)$ form on $K$ is integrable, while (B.14) implies that $\omega$ is a $(1,1)$ form in the complex structure defined by $\Omega$. Equation (B.12) and non-degeneracy of $\omega$ then imply that $\omega$ is a Kähler form on $K$. Finally the normalisation condition (B.15), where $C$ is some constant, implies that the Kähler metric on $K$ is Ricci-flat.

Since (B.15) is equivalent to
$$\|\Omega\|^{2}=i^{(n+1)^{2}} C,$$
the value of the constant $C$ depends on the value $\|\Omega\|$. Here we follow [10] by taking
$$C=(-i)^{(n+1)^{2}}= \begin{cases}1 & \text { if } n \text { is odd } \\ -i & \text { if } n \text { is even }\end{cases}$$
corresponding to $\|\Omega\|^{2}=1$.
We now show the properties (B.12)-(B.15) hold for $\omega, \Omega$ defined by (B.10), (B.11) and $u$ given below by (B.26). One calculates
$$\begin{aligned}
\mathrm{d}|\zeta|^{2} & =\zeta \bar{\theta}+\bar{\zeta} \theta \\
\mathrm{d} \theta & =\zeta \mathrm{d} \alpha+\mathrm{d} \zeta \wedge \alpha=i \frac{s}{2 n} \zeta \omega_{M}+\mathrm{d} \zeta \wedge \alpha=i \frac{s}{2 n} \zeta \omega_{M}+\theta \wedge \alpha
\end{aligned}$$
from which $\mathrm{d} \omega=0$ easily follows. Since, using (B.6),
$$\Omega=(\mathrm{d} \zeta+\zeta \alpha) \wedge e=\mathrm{d}(\zeta e)$$
$\Omega$ is closed. Since $\Omega$ is of type ( $n+1,0$ ) one has $\omega_{M} \wedge \Omega=0$ and $\omega \wedge \Omega=0$ follows. Using (B.8) applied to the Kähler metric determined by $\omega$ one has
$$\Omega \wedge \bar{\Omega}=(-i)^{(n+1)^{2}}\|\Omega\|^{2} \frac{\omega^{n+1}}{(n+1)!},$$
and from (B.10)
$$\omega^{n+1}=\frac{2 i n}{s} \lambda^{n+1} u^{n} u^{\prime} \omega_{M}^{n} \wedge \theta \wedge \bar{\theta}$$
giving
$$\Omega \wedge \bar{\Omega}=(-1)^{n}(-i)^{n^{2}} \frac{2 n}{s(n+1)} \lambda^{n+1}\|\Omega\|^{2} u^{n} u^{\prime} \operatorname{vol}_{M} \wedge \theta \wedge \bar{\theta}$$

We can also compute directly
$$\begin{aligned}
\Omega \wedge \bar{\Omega} & =(-1)^{n} \theta \wedge \bar{\theta} \wedge e \wedge \bar{e}=(-1)^{n}(-i)^{n^{2}} \theta \wedge \bar{\theta} \wedge e \wedge * \bar{e} \\
& =(-1)^{n}(-i)^{n^{2}} \operatorname{vol}_{M} \wedge \theta \wedge \bar{\theta}
\end{aligned}$$
Thus
$$\frac{2 n}{s(n+1)} \lambda^{n+1}\|\Omega\|^{2} u^{n} u^{\prime}=1$$
and in order to satisfy the normalisation condition $\|\Omega\|^{2}=1$ we need to impose
$$\frac{2 n}{s(n+1)} \lambda^{n+1} u^{n} u^{\prime}=1,$$
which has solution
$$u=\left(c|\zeta|^{2}+\kappa\right)^{\frac{1}{n+1}}$$
where $\kappa$ is an integration constant and
$$c=\frac{s(n+1)^{2}}{2 n \lambda^{n+1}} .$$

In conclusion the Kähler form $\omega$ and metric $g$ on $K$ are
$$\begin{aligned}
\omega & =\lambda u \omega_{M}+i(n+1)(\lambda u)^{-n} \theta \wedge \bar{\theta} \\
g & =\lambda u g_{M}+2(n+1)(\lambda u)^{-n}|\theta|^{2}
\end{aligned}$$
If $s>0, \kappa>0$ and $g_{M}$ is complete then $g$ is globally defined on the total space of $K$ and complete.

\section*{References}
\begin{itemize}
\item[1.] M. Atiyah, N. S. Manton and B. J. Schroers, Geometric Models of Matter, Proc. Roy. Soc. Lond. A 468 (2012), 1252-1279 doi:10.1098/rspa.2011.0616 [arXiv:1108.5151 [hep-th]]. 2
\item[2.] E. Calabi, Métriques kählériennes et fibrés holomorphes, Annales scientifiques de l'École Normale Supérieure 12 (1979), 169-294. 3 4- 26
\item[3.] T. Eguchi and A. J. Hanson, Asymptotically flat self-dual solutions to Euclidean gravity, Phys. Lett. B 74 (1978), 249-251. 23
\item[4.] G. Franchetti, Harmonic spinors on a family of Einstein manifolds, Nonlinearity 31 (2018), 2419. 2.10 .20
\item[5.] T. Hausel and E. Hunsicker and R. Mazzeo Hodge cohomology of gravitational instantons, Duke Math. J. 122 (2004), 485-548. 17
\item[6.] T. Friedrich, Dirac operators in Riemannian Geometry, Graduate Studies in Mathematics, 25, AMS (2000). 2, 10
\item[7.] T. Friedrich, I. Kath, A. Moroianu, U. Semmelmann, On nearly parallel G2-structures, Journal of Geometry and Physics 23 (1997) 259-286. 21
\item[8.] G. W. Gibbons and S. W. Hawking, Classification of gravitational instanton symmetries, Commun. Math. Phys. 66 (1979), 291-310. 3
\item[9.] N. J. Hitchin, $L^{2}$-cohomology of hyperkähler quotients, Commun. Math. Phys. 211 (2000), 153-165. 7
\item[10.] N. J. Hitchin, The moduli space of special lagrangian submanifolds, arXiv: Differential Geometry (1997). 27
\item[11.] N. J. Hitchin, Hyperkähler manifolds, Astérisque, tome 206 (1992), Séminaire Bourbaki, exp. no 748, p. 137-166. 8
\item[12.] N. J. Hitchin, Harmonic Spinors, Advances in Mathematics, 14 (1974) 1-55. 2
\item[13.] R. Jante and B. J. Schroers, Dirac operators on the Taub-NUT space, monopoles and SU(2) representations, JHEP 01 (2014), 114 doi:10.1007/JHEP01(2014)114 [arXiv:1312.4879 [hep-th]]. 2
\item[14.] A. Moroianu, Lectures on Kähler geometry, Cambridge University Press, 2007. 26
\item[15.] L. I. Nicolaescu, Lectures on the geometry of manifolds, second ed., World Scientific, 2007. 10
\item[16.] C. N. Pope, Axial Vector Anomalies and the Index Theorem in Charged Schwarzschild and Taub - Nut Spaces, Nucl. Phys. B 141 (1978), 432-444 doi:10.1016/0550-3213(78)90038-X. 2
\item[17.] S. M. Salamon, Riemannian geometry and holonomy groups, Acta Applicandae Mathematica 20 (1990), 309-311. 426
\item[18.] E. Witten, Search for a realistic Kaluza-Klein theory, Nuclear Physics B186 (1981), 412-428. 2
\item[19.] E. Witten, Physics and Geometry, Proceedings of the International Congress of Mathematicians Berkeley, California, USA, 1986. 2
\end{itemize}
(GF) Department of Mathematical Sciences, University of Bath, Claverton Down, Bath BA2
7AY, England, United Kingdom
Email address: gf424 [at] bath.ac.uk, ORCID: 0000-0002-1511-6204
(KK) School of Mathematical Sciences, University of Nottingham, Nottingham, NG7 2RD, UK Email address: kirill.krasnov[at]nottingham.ac.uk, ORCID: 0000-0003-2800-3767