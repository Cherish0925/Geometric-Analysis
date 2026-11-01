---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: hep-th_0003071.pdf
converter: mathpix
format: mmd
---

\title{
Supersymmetry of Topological Kerr-Newman-Taub-NUT-aDS Spacetimes
}

\author{
Natxo Alonso-Alberca, ${ }^{\text {1 }}$ Patrick Meessen ${ }^{\text {® }}{ }^{\text {2 }}$ and Tomás Ortín ${ }^{\text {★★ }}{ }^{3}$ \\ - Instituto de Física Teórica, C-XVI, Universidad Autónoma de Madrid \\ E-28049-Madrid, Spain \\ ${ }$ * I.M.A.F.F., C.S.I.C., Calle de Serrano 113 bis \\ E-28006-Madrid, Spain
}

\begin{abstract}
We extend the topological Kerr-Newman- $a D S$ solutions by including NUT charge and find generalizations of the Robinson-Bertotti solution to the negative cosmological constant case with different topologies. We show how all these solutions can be obtained as limits of the general Plebanski-Demianski solution.

We study the supersymmetry properties of all these solutions in the context of gauged $N=2, d=4$ supergravity. Generically they preserve at most 1/4 of the total supersymmetry. In the Plebanski-Demianski case, although gauged $N=2, d=4$ supergravity does not have electric-magnetic duality, we find that the family of supersymmetric solutions still enjoys a sort of electric-magnetic duality in which electric and magnetic charges and mass and Taub-NUT charge are rotated simultaneously.
\end{abstract}

\footnotetext{
${ }^{1}$ E-mail: Natxo.Alonso@uam.es
${ }^{2}$ E-mail: Patrick.Meessen@uam.es
${ }^{3}$ E-mail: tomas@leonidas.imaff.csic.es
}

\section*{Introduction}

The presence of a negative cosmological constant is enough to invalidate the classical theorems [1, 2] in which it is proven that at any given time black-hole horizons are always topologically spheres: asymptotically anti-De Sitter ( $a a D S$ ) black-hole solutions are known such that the constant-time sections of their event horizons are not topologically spheres [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]. In particular, aaDS Schwarzschild black holes with horizons with the topology of Riemann surfaces of arbitrary genus (henceforth called topological black holes) were given in Ref. [13], the charged generalization in the framework of the Einstein-Maxwell theory with a negative cosmological constant (topological aaDS Reissner-Nordström (RN-aDS) black holes) was studied in Ref. [14]. The generalization to the rotating case (topological aaDS Kerr-Newman (KN-aDS) black holes) was found and studied in Ref. [15] using the general Petrov type D solution of Plebanski and Demianski (PD solution) Ref. [16] (which contains in different limits all these topological black-hole solutions) and other methods. aaDS black holes with exotic horizons with topologies are also known in higher dimensions [12], in theories with dilaton [17] and Lovelock gravity [18].

The supersymmetry properties of $a a D S$ black holes were first studied by Romans in the context of $N=2, d=4$ gauged supergravity [19] for RN- $a D S$ black holes with spherical horizons. Later on, Kostelecký and Perry studied the supersymmetry properties of KN-$a D S$ black holes [20]. Recently, Caldarelli and Klemm extended Romans' results to the case of topological RN-aDS black holes and extended and corrected Kostelecký and Perry's in the spherical KN-aDS case in Ref. [21].

The supersymmetry properties known are far from being understood. In the recent years we have learned how to interpret many supersymmetric solutions as intersections of "elementary" supersymmetric solutions preserving half of the supersymmetries. Each additional object in the intersection breaks an additional half of the remaining supersymmetry ${ }^{4}$. Thus, in $N=2, d=4$ ungauged supergravity there is essentially one kind of object which is point-like and that breaks a half of the available supersymmetry and one can either break all the supersymmetry or just one half or nothing at all.

In $N=2, d=4$ gauged supergravity, however, Romans discovered solutions that preserve just 1/4 of the supersymmetry, characterized by a magnetic charge inversely proportional to the coupling constant. The simplest of those solutions only has magnetic charge (zero mass and electric charge) equal to the minimal amount of magnetic charge allowed by Dirac's quantization condition. It is really difficult to understand this fact using the paradigm of intersection of elementary objects.

Our goal in this paper is to try to gain some insight into this problem by examining more general cases an calculating, if possible, the amount of supersymmetries preserved by the solutions. Thus, in this letter we first present topological Kerr-Newman-Taub-NUT-aDS solutions and cosmological generalizations of the Robinson-Bertotti solution and then study

\footnotetext{
${ }^{4}$ Except in Hanany-Witten-like cases in which one can add one more object to an intersection without breaking any further supersymmetry. Needless to say that here we use "object" in a loose and general way that may include gravitational instantons, certain kinds of singularities, etc.
}
their supersymmetry properties together with those of the general Plebanski-Demianski solution from which all of them can be obtained through different contractions. We will see that, generically, these solutions preserve only 1/4 of the available supersymmetries in presence of angular momentum. Our second main result will be the identification of a sort of electric-magnetic duality symmetry of the supersymmetric Plebanski-Demianski solutions that involves the mass and NUT charge.

This paper is organized as follows: in Section 1 we describe $N=2, d=4$ gauged Supergravity. In Section 2 we describe the solutions whose supersymmetry properties we are going to study. In Section 3 we study the integrability conditions of the Killing spinor equation for the topological KN-TN-aDS solutions. In Section 3.3 and Section 3.4 we perform the same analysis for RB-aDS and the general PD solutions respectively. Section 4 contains our conclusions.

\section*{1 Cosmological EM Theory and $N=2, d=4$ Gauged Supergravity}

The $N=2, d=4$ supergravity multiplet consists of the Vierbein, a couple of real gravitini and a vector field
$$\left\{e_{\mu}{ }^{a}, \psi_{\mu}=\binom{\psi_{\mu}^{1}}{\psi_{\mu}^{2}}, A_{\mu}\right\},$$
respectively. With this multiplet one can construct two different supergravity theories: "pure" $N=2, d=4$ supergravity and "gauged" $N=2, d=4$ supergravity. The former can be understood as the zero-coupling limit of the latter and the second as the theory one obtains by gauging the $S O(2)$ symmetry that rotates the gravitini. The gauged $N=$ $2, d=4$ supergravity action for these fields in the 1.5 formalism is
$$\begin{aligned}
S_{g}= & \int d^{4} x e\left\{R(e, \omega)+6 g^{2}+2 e^{-1} \epsilon^{\mu \nu \rho \sigma} \bar{\psi}_{\mu} \gamma_{5} \gamma_{\nu}\left(\hat{\mathcal{D}}_{\rho}+i g A_{\rho} \sigma^{2}\right) \psi_{\sigma}-\mathcal{F}^{2}\right. \\
& \left.+\mathcal{J}_{(m)}{ }^{\mu \nu}\left(\mathcal{J}_{(e) \mu \nu}+\mathcal{J}_{(m) \mu \nu}\right)\right\},
\end{aligned}$$
where $\hat{\mathcal{D}}$ is the $\operatorname{SO}(2,3)$ gauge covariant derivative
$$\hat{\mathcal{D}}_{\mu}=\mathcal{D}_{\mu}-\frac{i}{2} g \gamma_{\mu},$$
$F$ is the standard vector field strength, $\tilde{F}$ is the supercovariant field strength and we also define for convenience $\mathcal{F}$ by
$$\left\{\begin{array}{l}
F_{\mu \nu}=2 \partial_{[\mu} A_{\nu]}, \\
\tilde{F}_{\mu \nu}=F_{\mu \nu}+\mathcal{J}_{(e) \mu \nu}, \\
\mathcal{F}_{\mu \nu}=\tilde{F}_{\mu \nu}+\mathcal{J}_{(m) \mu \nu},
\end{array}\right.$$
where we have also defined
$$\left\{\begin{array}{l}
\mathcal{J}_{(e) \mu \nu}=i \bar{\psi}_{\mu} \sigma^{2} \psi_{\nu}, \\
\mathcal{J}_{(m) \mu \nu}=-\frac{1}{2 e} \epsilon^{\mu \nu \rho \sigma} \bar{\psi}_{\rho} \gamma_{5} \sigma^{2} \psi_{\sigma} .
\end{array}\right.$$

We see that the gauge coupling constant $g$ is related to the cosmological constant by
$$\Lambda=-3 g^{2} .$$

The equation of motion for $\omega_{\mu}{ }^{a b}$ implies that it is given by
$$\left\{\begin{aligned}
\omega_{a b c} & =-\Omega_{a b c}+\Omega_{b c a}-\Omega_{c a b}, \\
\Omega_{\mu \nu}^{a} & =\Omega_{\mu \nu}{ }^{a}(e)+\frac{1}{2} T_{\mu \nu}{ }^{a}, \\
\Omega_{a b c}(e) & =e^{\mu}{ }_{a} e^{\nu}{ }_{b} \partial_{[\mu} e_{\nu] c}, \\
T_{\mu \nu}{ }^{a} & =i \bar{\psi}_{\mu} \gamma^{a} \psi_{\nu} .
\end{aligned}\right.$$
It is assumed that this equation has been used everywhere (1.5 formalism).
The Maxwell equation and Bianchi identity are
$$\left\{\begin{array}{l}
\partial_{\mu}\left(e \mathcal{F}^{\mu \nu}\right)=\frac{i g}{2} \epsilon^{\nu \lambda \rho \sigma} \bar{\psi}_{\lambda} \gamma_{5} \gamma_{\rho} \sigma^{2} \psi_{\sigma}, \\
\partial_{\mu}\left(e^{\star} F^{\mu \nu}\right)=0 .
\end{array}\right.$$
Observe that the divergences of $\mathcal{J}_{e}$ and $\mathcal{J}_{m}$ are two topologically conserved currents that appear as electric-like and magnetic-like sources for the vector field in the Maxwell equation
$$\partial_{\mu}\left(e F^{\mu \nu}\right)=+\partial_{\mu}\left(e \mathcal{J}_{e}^{\nu \mu}\right)+\partial_{\mu}\left(e \mathcal{J}_{m}^{\nu \mu}\right)+\frac{i g}{2} \epsilon^{\nu \lambda \rho \sigma} \bar{\psi}_{\lambda} \gamma_{5} \gamma_{\rho} \sigma^{2} \psi_{\sigma} .$$
They are naturally associated to the electric and magnetic central charges of the $N=$ $2, d=4$ supersymmetry algebra. The third term in the r.h.s. of the above equation is associated to the gravitino electric charge and it is, therefore, proportional to the gauge constant. Finally, the Einstein and Rarita-Schwinger equations are
$$\left\{\begin{array}{l}
0=G_{a}{ }^{\mu}-3 g^{2} e_{a}{ }^{\mu}-2 T(\psi)_{a}{ }^{\mu}-2 \tilde{T}(A)_{a}{ }^{\mu}, \\
0=e^{-1} \epsilon^{\mu \nu \rho \sigma} \gamma_{5} \gamma_{\nu}\left(\hat{\mathcal{D}}_{\rho}+i g A_{\rho} \sigma^{2}\right) \psi_{\sigma}-i\left(\tilde{F}^{\mu \nu}+i^{\star} \tilde{F}^{\mu \nu} \gamma_{5}\right) \sigma^{2} \psi_{\nu},
\end{array}\right.$$
where the equation of motion for $\omega_{\mu}{ }^{a b}$ has been used and where
$$\left\{\begin{aligned}
T(\psi)_{a}{ }^{\mu}= & -\frac{1}{2 e} \epsilon^{\mu \nu \rho \sigma} \bar{\psi}_{\nu} \gamma_{5} \gamma_{a}\left(\hat{\mathcal{D}}_{\rho}+i g A_{\rho} \sigma^{2}\right) \psi_{\sigma} \\
& -\frac{i g}{4 e} \epsilon^{\mu \nu \rho \sigma} \bar{\psi}_{\nu} \gamma_{5} \gamma_{\rho a} \psi_{\sigma}, \\
\tilde{T}(A)_{a}{ }^{\mu}= & \tilde{F}_{a}{ }^{\rho} \tilde{F}^{\mu}{ }_{\rho}-\frac{1}{4} e_{a}{ }^{\mu} \tilde{F}^{2} .
\end{aligned}\right.$$

Apart from invariance under general coordinate and local Lorentz transformations the theory is invariant under $U(1)$ gauge transformations
$$\left\{\begin{array}{l}
A_{\mu}^{\prime}=A_{\mu}+\partial_{\mu} \chi, \\
\psi_{\mu}^{\prime}=e^{-i g \chi \sigma^{2}} \psi_{\mu},
\end{array}\right.$$
and local $N=2$ supersymmetry transformations
$$\left\{\begin{array}{l}
\delta_{\epsilon} e_{\mu}^{a}=-i \bar{\epsilon} \gamma^{a} \psi_{\mu}, \\
\delta_{\epsilon} A_{\mu}=-i \bar{\epsilon} \sigma^{2} \psi_{\mu}, \\
\delta_{\epsilon} \psi_{\mu}=\tilde{\hat{\mathcal{D}}}_{\mu} \epsilon,
\end{array}\right.$$
where the $\tilde{\hat{\mathcal{D}}}_{\mu}$ is the supercovariant derivative defined by
$$\tilde{\hat{\mathcal{D}}}_{\mu}=\hat{\mathcal{D}}_{\mu}+i g A_{\mu} \sigma^{2}+\frac{1}{4} \tilde{F} \gamma_{\mu} \sigma^{2} .$$

In the ungauged case, the theory enjoys chiral-dual invariance which interchanges the Maxwell and Bianchi equations and the topologically conserved electric and magnetic charges (and, therefore, the associated central charges). In the gauged theory, the gauge coupling breaks this invariance.

We are going to work with purely bosonic solutions of this theory. They obey the bosonic equations of motion
$$\left\{\begin{aligned}
\nabla_{\mu} F^{\mu \nu} & =0, \\
\nabla_{\mu}{ }^{\star} F^{\mu \nu} & =0, \\
R_{\mu \nu} & =2 T_{\mu \nu}(A)-3 g^{2} g_{\mu \nu},
\end{aligned}\right.$$
where $T_{\mu \nu}(A)$ is just the standard energy-momentum tensor for an Abelian gauge field:
$$T_{\mu \nu}(A)=F_{\mu}{ }^{\rho} F_{\rho \nu}-\frac{1}{4} g_{\mu \nu} F^{2} .$$

These equations of motion are duality-invariant. However, the gravitino supersymmetry rule (even with fermionic fields set to zero) is not duality-invariant and the supersymmetry properties of duality-related bosonic solutions are not, in general, the same.

\section*{2 Topological RN-TN- $a D S$, KN-TN- $a D S$ and RB- $a D S$ and PD Solutions}

In this section we display and describe the solutions whose supersymmetry properties will later be studied. For simplicity we start with the unrotating RN-TN-aDS although they are included in the general KN-TN- $a D S$ case.

\subsection*{2.1 Topological RN-TN- $a D S$ Solutions}

These solutions generalize, by including NUT charge $N$, the topological RN-aDS black hole solutions found in Ref. [14]. There are three cases labeled by the parameter $\aleph$ whose value is essentially the sign of one minus the genus of the horizon and therefore takes the values 1, 0, -1 for the sphere (genus zero), the torus (genus 1) and higher genus Riemann surfaces, respectively. In the three cases the metric can be written in this form
$$\left\{\begin{aligned}
d s^{2} & =\frac{\lambda}{R^{2}}\left(d t+\omega_{\aleph} d \varphi\right)^{2}-\frac{R^{2}}{\lambda} d r^{2}-R^{2} d \Omega_{\aleph}^{2} \\
\lambda & =\left[g^{2} R^{4}+\left(\aleph+4 g^{2} N^{2}\right)\left(r^{2}-N^{2}\right)-2 M r+|Z|^{2}\right] \\
R^{2} & =r^{2}+N^{2},
\end{aligned}\right.$$
where $d \Omega_{\aleph}^{2}$ is the metric of the unit sphere, the plane and the upper half plane respectively
$$d \Omega_{\aleph}^{2}= \begin{cases}d \theta^{2}+\sin ^{2} \theta d \varphi^{2}, & \aleph=+1 \\ d \theta^{2}+d \varphi^{2}, & \aleph=0 \\ d \theta^{2}+\sinh ^{2} \theta d \varphi^{2}, & \aleph=-1\end{cases}$$
$\omega_{\aleph}$ is the function
$$\omega_{\aleph}= \begin{cases}2 N \cos \theta, & \aleph=+1, \\ -2 N \theta, & \aleph=0, \\ -2 N \cosh \theta, & \aleph=-1,\end{cases}$$
and the vector potential is given by
$$\begin{aligned}
& A_{t}=(Q r-N P) / R^{2}, \\
& A_{\varphi}= \begin{cases}\cos \theta\left[P\left(r^{2}-N^{2}\right)+2 N Q r\right] / R^{2}, & \text { for } \aleph=+1, \\
-\theta\left[P\left(r^{2}-N^{2}\right)+2 N Q r\right] / R^{2}, & \text { for } \aleph=0, \\
-\cosh \theta\left[P\left(r^{2}-N^{2}\right)+2 N Q r\right] / R^{2}, & \text { for } \aleph=-1 .\end{cases}
\end{aligned}$$

It is understood that one has to take the equation of the last two spacetimes by a discrete group in order to get a torus or a Riemann surface of arbitrary genus.

These solutions are valid in the $g=0$ case. In that limit (with $N=0$ ) so we can speak of black holes, only the $\aleph=+1$ ones can have a regular event horizon, in agreement with [1, 2]. With $g \neq 0$ (still with $N=0$ ) and we recover the solutions of Ref. [14] in which $M$ is the mass, $Q$ the electric charge, $P$ the magnetic charge and $Z=Q+i P$ some of which are black holes with regular horizons of different topologies.

For $g=0, N \neq 0$ we recover the standard RN-TN solutions in which those parameters are still the physical parameters ${ }^{5}$ and $N$ is the NUT charge. When the product $g N \neq 0$ it is no longer clear that $M, Q, P$ are the true mass, electric and magnetic charges that appear in the superalgebra. This is similar to what happens in the rotating case [20] in which the true charges are combinations of the parameters $M, P, Q$ appearing in the solution with the product $g a$.

It is useful to have a general form of the solutions valid for the three cases $\aleph=1,0,-1$. To have such a general expression we define the coordinate $u$
$$u \equiv \begin{cases}-\cos \theta, & \aleph=+1 \\ \theta, & \aleph=0 \\ \cosh \theta, & \aleph=-1\end{cases}$$
and then

\footnotetext{
${ }^{5}$ A definition of the mass of Taub-NUT spaces cannot be given in the standard form because these solutions do not go asymptotically to any other vacuum solution. The same happens in the 5-dimensional KK monopole solution, studied in Refs. [26, 27]. However, as different from the KK monopole, the TN solution is not ultrastatic and the tricks used in those references to define and calculate the mass of the KK monopole do not seem to apply to this case. A definition inspired in the AdS/CFT correspondence, has, however, been recently given in Refs. [28, 29].
}
$$\left\{\begin{aligned}
d s^{2} & =\frac{\lambda}{R^{2}}(d t-2 N u d \varphi)^{2}-\frac{R^{2}}{\lambda} d r^{2}-\frac{R^{2}}{S(u)} d u^{2}-R^{2} S(u) d \varphi^{2}, \\
A_{t} & =(Q r-N P) / R^{2}, \\
A_{\varphi} & =-u\left[P\left(r^{2}-N^{2}\right)+2 N r Q\right] / R^{2}, \\
S(u) & =\aleph\left(1-u^{2}\right)+1-\aleph^{2},
\end{aligned}\right.$$
where $\lambda$ and $R$ are as above.

\subsection*{2.2 Topological KN-TN- $a D S$ Solutions}

These solutions generalize the topological KN- $a D S$ solutions given in Ref. [15, 21] to the non-zero NUT charge case. In the $t, r, u, \varphi$ coordinate system (which is Boyer-Lindquist-type) they can be written as follows:
$$\left\{\begin{aligned}
d s^{2}= & \frac{\lambda}{R^{2}(r, u)}\left\{d t-\left[2 N u-a\left(\aleph^{2}-u^{2}\right)\right] d \varphi\right\}^{2}-\frac{R^{2}(r, u)}{\lambda} d r^{2} \\
& -\frac{R^{2}(r, u)}{\mathcal{S}(u)} d u^{2}-\frac{\mathcal{S}(u)}{R^{2}(r, u)}\left[\left(r^{2}+N^{2}+\aleph^{2} a^{2}\right) d \varphi+a d t\right]^{2} \\
A_{t}= & {[Q r-P(N+a u)] / R^{2}(r, u) } \\
A_{\varphi}= & \frac{1}{a} \sqrt{r^{2}+N^{2}+\aleph^{2} a^{2}}[Q r-P(N+a u)] / R^{2}(r, u), \\
\lambda= & g^{2} r^{4}+\left(\aleph+\aleph^{2} a^{2} g^{2}+6 g^{2} N^{2}\right) r^{2}-2 M r+|Z|^{2} \\
& -N^{2}\left(\aleph-3 \aleph^{2} a^{2} g^{2}+3 g^{2} N^{2}\right)+a^{2}\left(1+\aleph-\aleph^{2}\right), \\
\mathcal{S}(u)= & S(u)+\left(a^{2} g^{2} u^{2}+4 a g^{2} N u\right)\left(u^{2}-\aleph^{2}\right), \\
R^{2}(r, u)= & r^{2}+(N+a u)^{2},
\end{aligned}\right.$$
with $S(u)$ as above.
In Appendix A it is explained how this metric can be obtained from the general solution of Plebanski and Demianski [16]. The above form of the potentials is valid for $a \neq 0$. The $a \rightarrow 0$ limit of the field strength is perfectly well defined.

\subsection*{2.3 Topological RB Solutions}

In ungauged $N=2, d=4$ Supergravity, the extremal RN black hole can be seen as a soliton interpolating between two supersymmetric vacua: Minkowski spacetime at infinity and RB in the near-horizon limit. The RB spacetime is the product $a D S_{2} \times S^{2}$ where both factors are maximally symmetric spaces with opposite curvatures that cancel each other. The same thing occurs with other $p$-branes in higher dimensions [25, 31] where the role of the RB spacetime is played by $a D S_{p+2} \times S^{8-p}$. Here we present a generalization of the RB spacetime to the case of gauged $N=2, d=4$ Supergravity (cosmological E-M theory) whose supersymmetry properties we will study later. They are the product of $a D S_{2}$ with a sphere $S^{2}$, a torus $T^{2}$ or a higher-genus Riemann surface $\Sigma_{g}$ in which now the curvature of the $a D S_{2}$ spacetime is not completely canceled by the other factor space but they add up to the 4-dimensional cosmological constant
$$\left\{\begin{aligned}
d s^{2} & =K^{2} r^{2} d t^{2}-\frac{1}{K^{2} r^{2}} d r^{2}-L^{-2} S(u)^{-1} d u^{2}-L^{-2} S(u) d \varphi^{2}, \\
F_{01} & =\alpha \\
F_{23} & =-\beta,
\end{aligned}\right.$$
where the constants $K, L, \alpha, \beta$ satisfy
$$\begin{aligned}
g^{2} & =\frac{1}{6}\left\{K^{2}-\aleph L^{2}\right\}, \\
\alpha^{2}+\beta^{2} & =\frac{1}{2}\left(K^{2}+\aleph L^{2}\right) .
\end{aligned}$$
The field strength is covariantly constant and in this coordinate system has constant components which correspond to the vector potential components
$$\left\{\begin{array}{l}
A_{t}=-\alpha r, \\
A_{\varphi}=-\beta / L^{2} u .
\end{array}\right.$$

The $\aleph=-1, K^{2}=2 L^{2}$ solution, which has special supersymmetry properties has been also given in [30].

\subsection*{2.4 PD Solutions}

Plebanski and Demianski found most general Petrov type $D$ solution of the cosmological E-M theory. This general solution contains as limiting cases all the known solutions, and, in particular the topological KN-TN- $a D S$ solutions presented above (which in their turn, also contain the RN-TN-aDS solutions presented at the beginning). This is shown in Appendix A.

The PD solution depends on the constants ${ }^{6} \mathrm{M}, \mathrm{N}, \mathrm{Q}, \mathrm{P}, \mathrm{E}, \alpha$ and, of course, $g$, and, in Boyer coordinates $\tau, \sigma, p, q$, reads [16]
$$\left\{\begin{aligned}
d s^{2} & =\frac{\mathcal{Q}(q)}{p^{2}+q^{2}}\left(d \tau-p^{2} d \sigma\right)^{2}-\frac{p^{2}+q^{2}}{\mathcal{Q}(q)} d q^{2}-\frac{p^{2}+q^{2}}{\mathcal{P}(p)} d p^{2}-\frac{\mathcal{P}(p)}{p^{2}+q^{2}}\left(d \tau+q^{2} d \sigma\right)^{2} \\
F_{01} & =\left(q^{2}+p^{2}\right)^{-2}\left[\mathrm{Q}\left(q^{2}-p^{2}\right)-2 \mathrm{P} p q\right], \\
F_{23} & =-\left(q^{2}+p^{2}\right)^{-2}\left[\mathrm{P}\left(q^{2}-p^{2}\right)+2 \mathrm{Q} p q\right], \\
\mathcal{Q}(q) & =g^{2} q^{4}+\mathrm{E} q^{2}-2 \mathrm{M} q+\mathrm{Q}^{2}+\alpha, \\
\mathcal{P}(p) & =g^{2} p^{4}-\mathrm{E} p^{2}+2 \mathrm{~N} p-\mathrm{P}^{2}+\alpha .
\end{aligned}\right.$$

This class of solutions has a scaling invariance given by
$$\begin{array}{lll}
q & \rightarrow \kappa q, & \mathrm{M} \rightarrow \kappa^{3} \mathrm{M}, \\
p & \rightarrow \kappa p, & \mathrm{~N} \rightarrow \kappa^{3} \mathrm{~N}, \\
\tau & \rightarrow \kappa^{2} \mathrm{Q}, & \mathrm{P} \rightarrow \kappa^{2} \mathrm{P}, \\
\sigma & \rightarrow \kappa^{-3} \sigma, & \mathrm{E} \rightarrow \kappa^{2} \mathrm{E}, \\
\alpha & \rightarrow \kappa^{4} \alpha,
\end{array}$$
which can be used to bring one of the charges to a given value. It is clear that this scaling freedom remains if one of the charges happens to be nil.

The curvature is determined by M, N, Q and P and one can see that when they are zero, the Weyl tensor vanishes. This then means that in that case, the solution is locally $a D S_{4}$.

\section*{3 Supersymmetry and Integrability Conditions}

The bosonic part of the supercovariant derivative for gauged $N=2$ supergravity is
$$\tilde{\hat{\mathcal{D}}}_{\mu}=\hat{\nabla}_{\mu}+g A_{\mu} i \sigma^{2}-\frac{i}{4} F \gamma_{\mu} i \sigma^{2},$$
where $\hat{\nabla}_{\mu}$ is the $S O(2,3)$ gauge-covariant derivative. The Killing spinor equation is
$$\tilde{\hat{D}}_{\mu} \epsilon=0,$$
and a necessary condition for it to have solutions is the integrability condition

\footnotetext{
${ }^{6}$ These constants are different from the constants $M, N, Q, P$ that appear in the previous solutions.
}
$$\left[\tilde{\hat{\mathcal{D}}}_{\mu}, \tilde{\hat{\mathcal{D}}}_{\nu}\right] \epsilon=0 .$$
One finds [19]
$$\begin{aligned}
{\left[\tilde{\hat{\mathcal{D}}}_{\mu}, \tilde{\hat{\mathcal{D}}}_{\nu}\right] \epsilon=} & -\frac{1}{4}\left\{C_{\mu \nu}{ }^{a b} \gamma_{a b}+2 i \not \nabla\left(F_{\mu \nu}+i^{\star} F_{\mu \nu} \gamma_{5}\right) i \sigma^{2}\right. \\
& \left.+\frac{g}{2} F_{a b}\left(3 \gamma^{a b} \gamma_{\mu \nu}+\gamma_{\mu \nu} \gamma^{a b}\right) i \sigma^{2}\right\} \epsilon=0 .
\end{aligned}$$

We study first the non-rotating case RN-TN- $a D S$ case.

\subsection*{3.1 Supersymmetry of Topological RN-TN-aDS Solutions}

Introducing the Vierbein 1-forms
$$\begin{array}{ll}
e^{0}=\lambda^{1 / 2} / R\left(d t+\omega_{\aleph} d \varphi\right), & e^{1}=\lambda^{-1 / 2} R d r, \\
e^{2}=R d \theta, & e^{3}=R \Omega_{\aleph} d \varphi,
\end{array}$$
we find
$$\begin{gathered}
F_{01}=\left(Q\left(r^{2}-N^{2}\right)-2 N P r\right) / R^{4}, \\
F_{23}=-\left(P\left(r^{2}-N^{2}\right)+2 N Q r\right) / R^{4}, \\
\nabla_{1} F_{01}=-2 \lambda^{1 / 2} / R^{7}\left[Q\left(r^{3}-3 r N^{2}\right)-P\left(3 r^{2} N-N^{3}\right)\right], \\
\nabla_{1}^{\star} F_{01}=-2 \lambda^{1 / 2} / R^{7}\left[P\left(r^{3}-3 r N^{2}\right)+Q\left(3 r^{2} N-N^{3}\right)\right],
\end{gathered}$$
(the remaining components of $\nabla_{a} F_{b c}$ can be found using the Bianchi identities or the Maxwell equations, which are satisfied) and
$$\begin{aligned}
-\frac{1}{2} C_{01}^{01}= & C_{02}^{02}=C_{03}^{03}=C_{12}^{12}=C_{13}^{13}=-\frac{1}{2} C_{23}^{23}=C_{1}, \\
C_{02}^{13}= & -C_{03}^{12}=C_{12}^{03}=-C_{13}^{02}=-\frac{1}{2} C_{23}^{01}=C_{2}, \\
C_{1}= & {\left[M r^{3}-\left(3 N^{2}\left(\aleph-4 g^{2} N^{2}\right)+|Z|^{2}\right) r^{2}\right.} \\
& \left.-3 N^{2} M r+N^{2}\left(N^{2}\left(\aleph-4 g^{2} N^{2}\right)+|Z|^{2}\right)\right] / R^{6}, \\
C_{2}= & -N\left[\left(\aleph-4 g^{2} N^{2}\right) r^{3}+3 M r^{2}\right. \\
& \left.-\left(3 N^{2}\left(\aleph-4 g^{2} N^{2}\right)+2|Z|^{2}\right) r-M N^{2}\right] / R^{6},
\end{aligned}$$

Plugging all this into the integrability conditions we get the following conditions on the parameters:
$$\begin{aligned}
& 0=g\left[M P+Q N\left(\aleph+4 g^{2} N^{2}\right)\right], \\
& 0=\mathcal{B}_{+} \mathcal{B}_{-},
\end{aligned}$$
where we have defined
$$\mathcal{B}_{ \pm} \equiv(M \mp g N Q)^{2}+N^{2}\left(\aleph \pm g P+4 g^{2} N^{2}\right)^{2}-\left(\aleph \pm 2 g P+5 g^{2} N^{2}\right)|Z|^{2} .$$

The first condition plays the role of a constraint which is automatically satisfied in the well-known $g=0$ case, while the second implies $\mathcal{B}_{ \pm}=0$ which should be the (saturated) Bogomol'nyi bound of gauged $N=2, d=4$ supergravity and actually it reduces to the well-known Bogomol'nyi bound of ungauged $N=2, d=4$ supergravity in asymptotically flat spaces $\left(\aleph^{\prime}=+1\right)$ generalized so as to include NUT charge (see Refs. [22, 23, 24]) $M^{2}+N^{2}=Q^{2}+P^{2}$. For $g=0$ and arbitrary $\aleph$ we get
$$M^{2}+\aleph^{2} N^{2}=\aleph\left(Q^{2}+P^{2}\right) .$$

A detailed analysis of the different cases in which the constrains is satisfied and the Bogomol'nyi bound is saturated gives as a result the four cases represented in Table 1.

The first corresponds evidently to $a D S_{4}$ itself in standard spherical coordinates, which is maximally supersymmetric and preserves all supersymmetries. The second case can be shown to describe, at least locally, $a D S_{4}$ as well (the Weyl tensor vanishes and the space is maximally symmetric). There are, thus, two different values of the parameter $N$ that correspond to the same spacetime.

In the third and fourth cases we have taken for the sake of convenience $Q$ and $N$ as independent parameters. The third case is a generalization to $g N \neq 0$ of the standard $M=|Q|$ case of ungauged $N=2, d=4$ supergravity where $Q$ is arbitrary which preserves 1/2 of the supersymmetries. Here a non-vanishing magnetic charge proportional to $N$ is induced. As a matter of fact, it admits the limits $g \rightarrow 0$ and/or $N \rightarrow 0$ with the same amount of supersymmetry preserved.

There are two particularly interesting limits: the often neglected $g=0, \aleph=0$ case which (setting $N=0$ for simplicity and rescaling the coordinates $\theta, \varphi$ which do not represent angles anymore) corresponds to the solution
$$\left\{\begin{aligned}
d s^{2} & =\frac{Q^{2}}{r^{2}} d t^{2}-\frac{r^{2}}{Q^{2}}\left(d r^{2}+d \theta^{2}+d \varphi^{2}\right), \\
A_{t} & =\frac{Q}{r} .
\end{aligned}\right.$$

This solution belongs to the Papapetrou-Majumdar class

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|}
\hline $M$ & $N$ & $Q$ & $P$ & $\aleph$ & SUSY \\
\hline 0 & 0 & 0 & 0 & +1 & 1 \\
\hline 0 & $\pm \frac{1}{2 g}$ & 0 & 0 & -1 & 1 \\
\hline $\left|Q \sqrt{\aleph+4 g^{2} N^{2}}\right|$ & any & any & $\pm N \sqrt{\aleph+4 g^{2} N^{2}}$ & any & $\frac{1}{2}$ \\
\hline $|2 g N Q|$ & any & any & $\pm \frac{\aleph+4 g^{2} N^{2}}{2 g}$ & any & $\frac{1}{4}$ \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 1: In this table we represent the different combinations of values for the parameters $M, N, Q, P, \aleph$ of the general RN-TN-aDS solution Eq. (2.1) for which there are Killing spinors and the fraction of supersymmetry preserved. The first two cases correspond locally to $a D S$. The last two cases are the two general solutions of the constraint and Bogomol'nyi bound equations and admit different limits with the same amount of supersymmetries preserved. In particular, the third case preserves the same amount of supersymmetry in the particular cases $Q=0, N=0, \aleph=+1$ (for any $Q$ ) and $N= \pm 1 / 2 g, \aleph=-1$. The fourth case preserves the same amount of supersymmetry in the cases $Q=0, N=0$ (for any $Q$ ) and $g=0$. In this last case, electric-magnetic invariance is preserved and $Q$ can be substituted by $\sqrt{Q^{2}+P^{2}}$.}
\end{table}
$$\left\{\begin{aligned}
d s^{2} & =H^{-2} d t^{2}-H^{2} d \vec{x}^{2}, \\
A_{t} & = \pm H^{-1}, \\
\partial_{\underline{i}} \partial_{\underline{i}} H & =0,
\end{aligned}\right.$$
where the harmonic function $H$ has been chosen to depend on only one coordinate $H=|Q| x$ and not on $y, z$.

The second interesting limit $Q \rightarrow 0$ also gives a supersymmetric configuration that preserves 1/2 of the supersymmetries with only magnetic and NUT charge and zero mass.

The fourth case in Table 1 preserves only 1/4 of the supersymmetries and only exists for $g \neq 0$. It is a generalization to $N \neq 0$ of Romans' global monopole solution [19]. We see that the presence of both NUT and electric charge implies that the mass parameter has to be finite. On the other hand, it admits the limits $Q \rightarrow 0$ and/or $N \rightarrow 0$ with the same amount of supersymmetry preserved.

\subsection*{3.2 Supersymmetry of KN-TN- $a D S$ Solutions}

We choose the Vierbein 1-forms
$$\begin{aligned}
e^{0} & =\frac{\lambda^{1 / 2}}{R(r, u)}\left[d t-\left(2 N u-a\left(\aleph^{2}-u^{2}\right)\right) d \varphi\right], \\
e^{1} & =\frac{R(r, u)}{\lambda^{1 / 2}} d r, \\
e^{2} & =\frac{R(r, u)}{\mathcal{S}^{1 / 2}(u)} d u, \\
e^{3} & =\frac{\mathcal{S}^{1 / 2}(u)}{R(r, u)}\left[\left(r^{2}+N^{2}+\aleph^{2} a^{2}\right) d \varphi+a d t\right],
\end{aligned}$$
on which the field strength components read
$$\begin{aligned}
& F_{01}=R(r, u)^{-4}\left[Q\left(r^{2}-(N+a u)^{2}\right)-2 \operatorname{Pr}(N+a u)\right], \\
& F_{23}=-R(r, u)^{-4}\left\{P\left(r^{2}-(N+a u)^{2}\right)+2 Q r(N+a u)\right\},
\end{aligned}$$

We only need to calculate
$$\begin{aligned}
C_{0101} & =-2 R^{-6}\left[M\left(r^{3}-3 r X^{2}\right)+N\left(\aleph-\aleph^{2} a^{2} g^{2}+4 g^{2} N^{2}\right)\left(3 r^{2} X-X^{3}\right)-Z^{2}\left(r^{2}-X^{2}\right)\right], \\
C_{0123} & =2 R^{-6}\left[M\left(3 r^{2} X-X^{3}\right)+N\left(\aleph-\aleph^{2} a^{2} g^{2}+4 g^{2} N^{2}\right)\left(3 r X^{2}-r^{3}\right)-2 Z^{2} r X\right], \\
\nabla_{1} F_{01} & =-2 R^{-7} \lambda^{1 / 2}\left[Q\left(r^{3}-3 r X^{2}\right)-P\left(3 r^{2} X-X^{3}\right)\right], \\
\nabla_{2} F_{01} & =-2 a R^{-7} \mathcal{S}^{1 / 2}\left\{P\left(r^{3}-3 r X^{2}\right)+Q\left(3 r^{2} X-X^{3}\right)\right\},
\end{aligned}$$
where we used the abbreviation $X=N+a u$. As in the RN-TN- $a D S$ case the other components of the integrability condition turn out to be proportional to the 01 component. From this one obtains the constraint and generalization of the Bogomol'nyi bound
$$\begin{aligned}
& 0=g\left[M P+N Q\left(\aleph-\aleph^{2} a^{2} g^{2}+4 g^{2} N^{2}\right)\right], \\
& 0=\mathcal{B}_{+} \mathcal{B}_{-},
\end{aligned}$$
where now
$$\begin{aligned}
\mathcal{B}_{ \pm} \equiv & M^{2}+N^{2}\left(\aleph-\aleph^{2} a^{2} g^{2}+4 g^{2} N^{2}\right)-\left[\left(\aleph+\aleph^{2} a^{2} g^{2}+6 g^{2} N^{2}\right)\right. \\
& \left. \pm 2 g \sqrt{a^{2}\left(1+\aleph-\aleph^{2}\right)-N^{2}\left(\aleph-3 \aleph^{2} a^{2} g^{2}+3 g^{2} N^{2}\right)}\right] Z^{2}
\end{aligned}$$

The fact that the bound factorizes into the product $\mathcal{B}_{+} \mathcal{B}_{-}$is difficult to see directly from the calculation but easy to deduce from the results we will find in the general PD
case. It can be checked that the (saturated) bound obtained is exactly the same, when $N=0$, as the one given by Caldarelli and Klemm in Ref. [21].

We can now try to analyze different solutions to these two equations. This is a very complex problem and it would only make sense to explain in detail a classification of the solutions if the different classes had different amounts of unbroken supersymmetry. However, in all the cases that we have been able to analyze we have not found any single supersymmetric solution with $a \neq 0$ preserving 1/2 of the supersymmetries. In fact, adding angular momentum to the RN-TN- $a D S$ solutions that do preserve 1/2 of the supersymmetries always seems to break an another half leaving only 1/4 unbroken.

For instance, the solution with $M=Q=0, P= \pm(2 g)^{-1}\left(\aleph-\aleph^{2} a^{2} g^{2}+4 g^{2} N^{2}\right), \aleph= \pm 1$ preserves 1/2 with $a=0$ and only 1/4 with $a \neq 0$. The same effect takes place in all the instances studied.

\subsection*{3.3 Supersymmetry of Topological RB Solutions}

To check supersymmetry of the topological RB solutions we only need
$$C_{0101}=\frac{1}{3}\left\{K^{2}-\aleph L^{2}\right\}=2 g^{2},$$
since the vector field strengths is covariantly constant.
The integrability condition then reads
$$g\left[g \mathbb{I}-\alpha \gamma^{01} i \sigma^{2}+\beta \gamma^{23} i \sigma^{2}\right] \epsilon=0 .$$

Obviously, for $g=0$ one finds Robinson-Bertotti which will not break any supersymmetry. When $g \neq 0$ however, one finds, just by taking the determinant of the above equation, that one has to satisfy
$$(g \pm \beta)^{2}+\alpha^{2}=0 \rightarrow\left\{\begin{array}{l}
\alpha=0 \\
\beta= \pm g
\end{array}\right.$$
which then break half of the available supersymmetry. Plugging the above equations into Eq. (2.9), one finds that
$$\aleph=-1 \quad, \quad K^{2}=2 L^{2},$$
which means that $K^{2}=4 g^{2}$ and $L^{2}=2 g^{2}$. This is the solution found in Ref. [30].
We could have found this solution also as the near-horizon limit of the $\aleph$ generalization of Romans' global monopole [19]. In that case we have $P=\frac{ \pm \aleph}{2 g}$ and with $\aleph=-1$ and all other charges vanishing we find that there is a horizon at $2 g^{2} r^{2}=1$. At this radius the solution can be approximated by
$$\begin{aligned}
d s^{2} & =4 g^{2} r^{2} d t^{2}-\frac{1}{4 g^{2} r^{2}} d r^{2}-\frac{1}{2 g^{2}}\left(d \theta^{2}+\sinh ^{2}(\theta) d \phi^{2}\right), \\
F_{23} & =-\frac{ \pm 1}{2 g} \cdot\left(\frac{1}{2 g^{2}}\right)^{-1}=\mp g .
\end{aligned}$$
which is just the supersymmetric RB-like solution discussed above. We then see that we have supersymmetry enhancement at the horizon from 1/4 to 1/2. Observe that he presence of electric charge would have meant the complete annihilation of supersymmetry at the horizon.

\subsection*{3.4 Supersymmetry of the PD General Solution}

As in the foregoing cases, one finds that all the components of the integrability condition are equivalent, so we will only write down the components of the Weyl tensor and the covariant derivative of the vector field strength to calculate the integrability condition in the 01 direction.
$$\begin{aligned}
C_{1010} & =\frac{-2(p+q)^{3}}{\left(1+p^{2} q^{2}\right)^{3}}\left[-\mathrm{M}\left(1-3 p^{2} q^{2}\right)+\mathrm{N}\left(3 p q-p^{3} q^{3}\right)+\mathrm{Z}^{2}(p-q)\left(1-p^{2} q^{2}\right)\right], \\
C_{1023} & =\frac{-2(p+q)^{3}}{\left(1+p^{2} q^{2}\right)^{3}}\left[-\mathrm{M}\left(3 p q-3 p^{3} q^{3}\right)-\mathrm{N}\left(1-3 p^{2} q^{2}\right)+\mathrm{Z}^{2} 2 p q(p-q)\right], \\
\nabla_{1} F_{01} & =\frac{2(p+q)^{2} \mathcal{Q}^{1 / 2}}{\left(1+p^{2} q^{2}\right)^{7 / 2}}\left[\mathrm{Q}\left(1-3 p^{3} q+p^{5} q^{3}-3 p^{2} q^{2}\right)+\mathrm{P}\left(3 p q-p^{3} q^{3}+p^{2}-3 p^{4} q^{2}\right)\right], \\
\nabla_{2} F_{01} & =\frac{2(p+q)^{2} \mathcal{P}^{1 / 2}}{\left(1+p^{2} q^{2}\right)^{7 / 2}}\left[\mathrm{P}\left(1-3 p^{3} q+p^{5} q^{3}-3 p^{2} q^{2}\right)-\mathrm{Q}\left(3 p q-p^{3} q^{3}+p^{2}-3 p^{4} q^{2}\right)\right],
\end{aligned}$$

Plugging these expressions into the integrability condition and calculating the determinant, one finds that the following conditions need to be satisfied in order for the solution to be supersymmetric
$$\begin{aligned}
& 0=g[\mathrm{MP}+\mathrm{NQ}], \\
& 0=\mathcal{B}_{+} \mathcal{B}_{-},
\end{aligned}$$
where, now
$$\mathcal{B}_{ \pm} \equiv \mathrm{W}^{2}-\left(\mathrm{E} \pm 2 g \alpha^{1 / 2}\right) \mathrm{Z}^{2},$$
and we have defined $\mathrm{W}^{2}=\mathrm{M}^{2}+\mathrm{N}^{2}$ and $\mathrm{Z}^{2}=\mathrm{Q}^{2}+\mathrm{P}^{2}$. One can check that these conditions are invariant under the scalings in Eq. (2.12) and they give the integrability equations of the RN-TN- $a D S$ and KN-TN- $a D S$ cases after the redefinitions (A.2).

Again we find a constraint on the charges and a generalization of the (saturated) Bogomol'nyi bound $\mathcal{B}_{ \pm}=0$. The advantage of the parameterization of the PD solution is, first of all, that the second integrability condition factorizes completely and that $\mathcal{B}_{ \pm}$is extremely simple and is almost identical to the standard bound for asymptotically flat, ungauged,
$N=2, d=4$ supergravity solutions, being electric-magnetic duality-invariant and invariant under gravito-electric-magnetic duality that rotates M into N and vice-versa. These duality invariances are broken by the constraint $g[\mathrm{MP}+\mathrm{NQ}]=0$ which is, nevertheless invariant under simultaneous rotations with the same angle
$$\left\{\begin{array} { l } 
{ \mathrm { M } ^ { \prime } = \operatorname { c o s } \theta \mathrm { M } - \operatorname { s i n } \theta \mathrm { N } , } \\
{ \mathrm { N } ^ { \prime } = \operatorname { s i n } \theta \mathrm { M } + \operatorname { c o s } \theta \mathrm { N } , }
\end{array} \quad \left\{\begin{array}{l}
\mathrm{Q}^{\prime}=\cos \theta \mathrm{Q}+\sin \theta \mathrm{P}, \\
\mathrm{P}^{\prime}=-\sin \theta \mathrm{Q}+\cos \theta \mathrm{P} .
\end{array}\right.\right.$$

Actually, assuming that $g \neq 0$ one can eliminate completely the constraint, getting a pair of equations
$$\left\{\begin{array}{l}
\mathrm{M}^{2}=\left(\mathrm{E} \pm 2 g \alpha^{1 / 2}\right) \mathrm{Q}^{2}, \\
\mathrm{~N}^{2}=\left(\mathrm{E} \pm 2 g \alpha^{1 / 2}\right) \mathrm{P}^{2},
\end{array}\right.$$
which hold even if some of these charges (but not $g$ ) vanish. These equations rotate into each other under the above duality transformations.

The rotation parameter is always bounded above:
$$\alpha^{1 / 2} \leq \pm \mathrm{E} / 2 g .$$

When this bound is saturated, then both $\mathrm{M}=0$ and $\mathrm{N}=0$, while Q and P remain arbitrary. This is always the case when $\mathrm{E}=0$.

Finally, the only supersymmetric solution with $\mathrm{Z}=0$ is a $a D S_{4}$.
A calculation of the rank of the integrability condition shows that all these configurations will generically break three-fourths of the available supersymmetries. This was to be expected from our results in the KN-TN- $a D S$ case. On the other hand we have not been able to find any combination preserving up to 1/2 of the available supersymmetry which is not the RN-TN-aDS solution.

\section*{4 Conclusions}

In this letter we have presented new solutions which generalize the already known topological black holes and the standard Robinson-Bertotti solution. We have explored their supersymmetry properties finding that generically they preserve only 1/4 of the supersymmetry. The only solutions that preserve 1/2 are non-rotating ones and the addition of angular momentum seems to break a further half of the remaining supersymmetries.

A somewhat surprising result that deserves further study is the fact that the most general family of supersymmetric solutions of this theory (i.e. the supersymmetric Plebanski-Demianski solutions) is invariant under a continuous $S O(2)$ group of electric-magnetic duality transformations. Had we not included in our study NUT charge the existence of that symmetry would have passed completely unnoticed. Its meaning is, however, obscure.

After all, the charges that undergo the duality rotation in its simplest, linear form, are not the physical charges. In terms of the physical charges, the duality transformations are very nonlinear.

\section*{Acknowledgments}

The work of N.A.-A., P.M. and T.O. have been supported in part by the European Union TMR program FMRX-CT96-0012 Integrability, Non-perturbative Effects, and Symmetry in Quantum Field Theory and by the Spanish grant AEN96-1655. P.M. would like to thank Iberdrola and the Universidad Autónoma de Madrid for their support.

\section*{A Obtaining the Topological KN-TN-aDS Metric from PD's}

Performing in Eq. (2.11) the coordinate change (see the analogous discussion in [15])
$$\begin{array}{llr}
q=r, & \tau=t+\left[a^{-1} N^{2}+a \aleph^{2}\right] \varphi, \\
p=N+a u, & \sigma=a^{-1} \phi,
\end{array}$$
and the following redefinitions of the parameters $\mathrm{M}=M, \mathrm{Q}=Q, \mathrm{P}=P$,
$$\begin{aligned}
& \mathrm{E}=\aleph+\aleph^{2} a^{2} g^{2}+6 g^{2} N^{2}, \\
& \mathrm{~N}=N\left(\aleph-\aleph^{2} a^{2} g^{2}+4 g^{2} N^{2}\right), \\
& \alpha=a^{2}\left(1+\aleph-\aleph^{2}\right)-N^{2}\left(\aleph-3 \aleph^{2} a^{2} g^{2}+3 g^{2} N^{2}\right)+P^{2},
\end{aligned}$$
we go from the PD metric to the KN-TN-aDS metric as written down in Eqs. (2.7).
Note that the choice of the redefinitions is largely dictated by the factorizability of $\mathcal{P}$.

\section*{References}
[1] S.W. Hawking, Comm. Math. Phys. 25 (1972) 152.
[2] J.L. Friedmann, K. Schleich and D.M. Witt, Phys. Rev. Lett. 69 (1992) 1849.
[3] S. Åminneborg, I. Bengtsson, S. Holst and P. Peldán, Class. Quant. Grav. 13 (1996) 2707-2714.
[4] R.B. Mann, Class. Quant. Grav. 14 (1997) L109-L114.
[5] R.B. Mann, Topological Black Holes: Outside Looking In In Haifa 1997, Internal structure of black holes and spacetime singularities 311-342.
[6] W.L. Smith and R.B. Mann, Phys. Rev. D56 (1997) 4942-4947.
[7] J.P.S. Lemos, Class. Quant. Grav. 12 (1995) 1081-1086.
[8] J.P.S. Lemos, Phys. Lett. B353 (1995) 46-51.
[9] J.P.S. Lemos and V.T. Zanchin, Phys. Rev. D54 (1996) 3840-3853.
[10] R.-G. Cai and Y.-Z. Zhang, Phys. Rev. D54 (1996) 4891-4898.
[11] C.-G. Huang and C.-B.Liang, Phys. Lett. A201 (1995) 27-32.
[12] D. Birmingham, Topological Black Holes in Anti-De Sitter Space, Report hep-th/9808032
[13] L. Vanzo, Phys. Rev. D56 (1997) 6475-6483.
[14] D. Brill, J. Louko and P. Peldán, Phys. Rev. D56 (1997) 3600.
[15] D. Klemm, V. Moretti and L. Vanzo, Phys. Rev. D57 (1998) 6127
[16] J.F. Plebanski and M. Demianski, Ann. Phys. 98 (1976) 98. J.F. Plebanski, Ann. Phys. 90 (1975) 196.
[17] Rong-Gen Cai, Jeong-Young Ji and Kwang-Sup Soh, Phys. Rev. D57 (1998) 6547-6550.
[18] Rong-Gen Cai and Kwang-Sup Soh, Phys. Rev. D59 (1999) 044013.
[19] L.J. Romans, Nucl. Phys. B383 (1992) 395-415
[20] V.A. Kostelecký and M.J. Perry, Phys. Lett. B371 (1996) 191-198
[21] M.M. Caldarelli and D. Klemm, Nucl. Phys. B545 (1999) 434
[22] R. Kallosh, D. Kastor, T. Ortín and T. Torma, Phys. Rev. D50 (1994) 6374.
[23] E. Bergshoeff, R. Kallosh and T. Ortín, Nucl. Phys. B478 (1996) 156-180.
[24] E. Álvarez, P. Meessen and T. Ortín, Nucl. Phys. B508 (1997) 181-218.
[25] G.W. Gibbons and P.K. Townsend, Phys. Rev. Lett. 71 (1993), 3754.
[26] S. Deser and M. Soldate, Gravitational Energy in Spaces with Compactified Dimensions, Nucl. Phys. B311 (1988/89) 739-750.
[27] L. Bombelli, R.K. Koul, G. Kunstatter, J. Lee and R.D. Sorkin, On Energy in 5-Dimensional Gravity and the Mass of the Kaluza-Klein Monopole, Nucl. Phys. B299 (1987) 735-756.
[28] R.B. Mann, Phys. Rev. D60 (1999) 104047.
[29] A. Chamblin, R. Emparan, C.V. Johnson and R.C. Myers, Phys. Rev. D60 (1999) 104026.
[30] S. Cacciatori, D. Klemm and D. Zanon, $w_{\infty}$ Algebras, Conformal Mechanics, and Black Holes, hep-th/9910065.
[31] H.J. Boonstra, K. Skenderis and P.K. Townsend, Journal of High Energy Physics 9901 (1999) 003.