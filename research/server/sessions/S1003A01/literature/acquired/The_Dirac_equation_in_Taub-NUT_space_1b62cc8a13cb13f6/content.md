---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: The_Dirac_equation_in_Taub-NUT_space_674f6d72152c.pdf
converter: mathpix
format: mmd
---

\title{
The Dirac equation \\ in Taub-NUT space
}

\author{
A. COMTET ( ${ }^{1}$ ) and P. A. HORVÁTHY ( ${ }^{2}$ )
}

\begin{abstract}
Using chiral supersymmetry, we show that the massless Dirac equation in the Taub-NUT gravitational instanton field is exactly soluble and explain the arisal and the use of the dynamical (super) symmetry.
\end{abstract}

Physics Letters B 349, p. 49-56 (1995)

\section*{1. Introduction}

The Dirac equation $\not D \psi=0$ in the Kaluza-Klein (KK) monopole field - obtained by imbedding the Taub-NUT solution into five-dimensional gravity with trivial time dependence [1] - was studied in the mid eighties [2]. It was found in particular that there were no zero modes and therefore the Rubakov effect was absent. It was later realized, that the motion of a spin 0 particle in the KK monopole field is exactly soluble, and that it has a Kepler-type dynamical symmetry [3], [4]. Recently [5], a Runge-Lenz vector was constructed also in the spinning case. Even more recently van Holten found, by applying the geometric technique of Ref. [6], that the Taub-NUT gravitational instanton has an $N=4$ supersymmetry [7]. In this Letter, we point out that the fermion problem is also exactly soluble, rederive the above symmetries following an entirely different approach, and use them to find the spectrum and the S-matrix. The clue is chiral supersymmetry (SUSY): the Dirac operator, $\not l=\left(\begin{array}{ll} & T^{\dagger} \\ T & \end{array}\right)$ is supersymmetric in 4 dimensions: Its square,
$$\not D^{2}=\left(\begin{array}{cc}
T^{\dagger} T & \\
& T T^{\dagger}
\end{array}\right) \equiv\left(\begin{array}{cc}
H_{1} & \\
& H_{0}
\end{array}\right) \equiv H,$$
is in fact the Hamiltonian of a supersymmetric quantum mechanical system, with 'fermion operator' $\gamma^{5}=$ $\left(\begin{array}{ll}1 & \\ & -1\end{array}\right)$ and intertwining transformations
$$U=\frac{1}{\sqrt{H_{0}}} T \quad \text { and } \quad U^{-1} \equiv U^{\dagger}=T^{\dagger} \frac{1}{\sqrt{H_{0}}} .$$
Indeed, $U^{\dagger} H_{0} U=H_{1}$.

\footnotetext{
( ${ }^{1}$ ) Division de Physique Théorique, IPN, Université Paris-Sud, F-91405 ORSAY, Cedex (France) and LPTPE, Université de Paris VI.
( ${ }^{2}$ ) Laboratoire de Mathématiques et Applications, Faculté des Sciences, Parc de Grandmont, Université, F-37200 TOURS (France). e-mail: horvathy@univ-tours.fr
}

If $\psi$ is an $H_{0}$-eigenfunction with eigenvalue $E^{2}>0$, then $\Psi=T^{\dagger} \psi$ is an $H_{1}$-eigenfunction with the same eigenvalue. $H_{1}$ has therefore the same spectrum as $H_{0}$ up to zero-energy ground states which arise as solutions of $T \Psi=0$. If $H_{0} \psi=E^{2} \psi$, then $\not D\binom{U^{\dagger} \psi}{ \pm \psi}= \pm E\binom{U^{\dagger} \psi}{ \pm \psi}$, so the eigenfunctions of the Dirac operator can be found from those of $\not D^{2}$.

Let us assume that one of the partner hamiltonians, say $H_{0}$, is simple so that its spectrum and symmetries are known. Then the corresponding quantities for $H_{1}$ are readily obtained by SUSY. In the same spirit, if some operator $A_{0}$ is conserved for $H_{0}$ i.e. $\left[H_{0}, A_{0}\right]=0$, then
$$A_{1}=U^{\dagger} A_{0} U$$
is conserved for $H_{1},\left[H_{1}, A_{1}\right]=0$, and the diagonal operator $A=\operatorname{diag}\left(A_{1}, A_{0}\right)$ is conserved for the Dirac operator, $[\not D, A]=0$. (With a slight abuse of notations, $A_{1}$ will be identified with $\operatorname{diag}\left(A_{1}, 0\right)$, etc.). The bosonic symmetries of $\not D$ can hence also be obtained from those of $H_{1}$ and have plainly the same algebraic structure as those of $H_{0}$. They can be, in principle, calculated using Eq. (1.3). Their explicit forms are, however, rather complicated as well as useless, since all their properties follow from those of $A_{0}$. They will therefore be omitted.

The supersymmetries of $H$ are easily identified and contain $Q_{1}=\not D$. Those which commute with $Q_{1}$ form the supersymmetry algebra of the Dirac operator. This is precisely what happens for the Taub-NUT metric: due to self-duality, one of the partner Hamiltonians reduces to the spin 0 Hamiltonian, and can be hence exactly solved. The other partner hamiltonian is complicated, but SUSY dispenses us from solving it.

\section*{2. The Dirac operator in the Taub-NUT background}

The Taub-NUT gravitational instanton is described by the 4-metric
$$V\left\{d r^{2}+r^{2}\left(d \theta^{2}+\sin ^{2} \theta d \phi^{2}\right)\right\}+\frac{1}{V}\{d \psi-4 m \vec{A} \cdot d \vec{r}\}^{2},$$
where
$$V=1+\frac{4 m}{r} \quad \text { and } \quad \vec{A} \cdot d \vec{r}=\cos \theta d \phi$$
In the usual context, the Taub-NUT parameter, $m$ is positive; $m<0$ arises, e.g. in the long-range scattering of self-dual $S U(2)$ monopoles [3], [4]. The curved-space gamma matrices, $\hat{\gamma}^{\mu}$, and the spin connection, $\Gamma^{\mu}$, are expressed as [8]
$$\hat{\gamma}^{j}=\left(\begin{array}{cc}
0 & -\frac{i}{\sqrt{V}} \sigma^{j} \\
\frac{i}{\sqrt{V}} \sigma^{j} & 0
\end{array}\right), \quad \hat{\gamma}^{4}=\left(\begin{array}{cc}
0 & \sqrt{V}-\frac{4 i m}{\sqrt{V}} \vec{\sigma} \cdot \vec{A} \\
\sqrt{V}+\frac{4 i m}{\sqrt{V}} \vec{\sigma} \cdot \vec{A} & 0
\end{array}\right),$$
and
$$\vec{\Gamma}=\left(\begin{array}{cc}
\frac{4 m}{2 V^{2}}(\vec{\nabla} V \cdot \vec{\sigma}) \vec{A}+\frac{1}{2 V} \vec{\nabla} V \times \vec{\sigma} & 0 \\
0 & 0
\end{array}\right), \quad \Gamma_{4}=\left(\begin{array}{cc}
-\frac{1}{2 V^{2}} \vec{\nabla} V \cdot \vec{\sigma} & 0 \\
0 & 0
\end{array}\right),$$
respectively. The operator $\partial_{\psi}$ commutes with the Dirac operator $\not D=\hat{\gamma}^{\mu}\left(\partial_{\mu}+i \Gamma_{\mu}\right)$, since nothing depends on $\psi$. Therefore, we can restrict ourselves to a fixed eigensector of $\partial_{\psi}$. Requiring $\psi$ to be periodic with period $16 \pi m$, the eigenvalues of $-4 m i \partial_{\psi}$, denoted by $q$ and identified with the electric charge, are half-integers. For a fixed $q$ (assumed positive for definiteness), the Dirac operator $\not D$ becomes
$$\not D=\left(\begin{array}{cc}
0 & T^{\dagger} \\
T & 0
\end{array}\right)=\left(\begin{array}{cc}
0 & -\frac{i}{\sqrt{V}} \vec{\sigma} \cdot \vec{\pi}+\frac{q}{4 m} \sqrt{V} \\
\frac{i}{V} \vec{\sigma} \cdot \vec{\pi} \sqrt{V}+\frac{q}{4 m} \sqrt{V} & 0
\end{array}\right),$$
where $\vec{\pi}=-i \vec{\nabla}+q \vec{A}$. It is easy to check that $T$ and $T^{\dagger}$ are each other's adjoint with respect to the Taub-NUT volume element $V d^{4} x$, as they have to be. Using the (anti)self-duality property $\vec{\nabla} V=-4 m \vec{B}$, the square of $\not D$ is found to be (1.1) with
$$\left\{\begin{array}{l}
H_{1}=H_{0}+\frac{1}{V}\left[\frac{q}{r^{2} V} \vec{\sigma} \cdot \hat{\mathbf{r}}+\frac{4 m}{r^{2} V} \vec{\sigma} \cdot \vec{r} \times \vec{L}_{0}+\frac{12 m^{2}}{r^{4} V^{2}}\right], \\
H_{0}=\frac{1}{V}\left[\vec{\pi}^{2}+\left(\frac{q}{4 m}\right)^{2} V^{2}\right],
\end{array}\right.$$
where $\vec{L}_{0}=\vec{r} \times \vec{\pi}+q \hat{\mathbf{r}}$ is the orbital angular momentum [conserved for $H_{0}$ but not for $H_{1}$ ]. The partner hamiltonians $H_{1}$ and $H_{0}$ differ hence in a complicated expression, and it is not at all obvious that they have the same spectra. SUSY implies however that this is nevertheless true.

The 'lower' (i.e. $\gamma^{5}=-1$ ) sector is simple: all spin dependence dropped out. $H_{0}$ is in fact the the Hamiltonian for a spin 0 particle in the KK field [3], [4] (times the unit matrix). Decomposing into radial and transverse components, $H_{0} \Psi_{0}=E^{2} \Psi_{0}$ leads to the non-relativistic Coulomb-type equation
$$\left[-\frac{1}{r^{2}} \frac{d}{d r}\left(r^{2} \frac{d}{d r}\right)+\frac{\vec{L}_{0}^{2}}{r^{2}}+\left(\frac{q^{2}}{2 m}-4 m E^{2}\right) \frac{1}{r}+\left(\left(\frac{q}{4 m}\right)^{2}-E^{2}\right)\right] \Psi_{0}=0 .$$
Inserting $\vec{L}_{0}^{2}=L(L+1), L=q, q+1, \ldots$ and setting
$$\Psi_{0}^{+}=u_{+}(r) Y_{L}^{\mu}(\theta, \phi)\binom{1}{0} \quad \text { and } \quad \Psi_{0}^{-}=u_{-}(r) Y_{L}^{\mu}(\theta, \phi)\binom{0}{1},$$
where the $Y_{L}^{\mu}$ 's are the 'Wu-Yang' monopole harmonics, we find that both radial functions $u_{ \pm}$become
$$u(r)=r^{L} e^{i k r} F(i \lambda+L+1,2 L+2,-2 i k r),$$
where $F$ is the confluent hypergeometric function and
$$k^{2}=E^{2}-(q / 4 m)^{2} \quad \text { and } \quad \lambda=-4 m\left[\left(E^{2} / 2\right)-(q / 4 m)^{2}\right] / k .$$
By Eq. (2.9), the wave function vanishes at the origin. No hermiticity problem arises therefore. Bound states only arise for $E^{2}>(q / 4 m)^{2}$ which requires $m<0$. Square integrability requires $\lambda^{2}=-(p+L+1)^{2}=-n^{2}$, $p=0,1, \ldots$, yielding the spectrum
$$E_{n}^{2}=\frac{1}{8 m^{2}} \sqrt{n^{2}-q^{2}}\left(n-\sqrt{n^{2}-q^{2}}\right), \quad n=q+1, q+2, \ldots$$
Such a state is labelled by the quantum numbers
$$\left\{\begin{array}{cc}
E & \text { energy } \\
L=q, q+1, \ldots & \text { total orbital angular momentum } \\
\mu=-L, \ldots, L & \text { third component of } \vec{L}_{0} \\
s= \pm \frac{1}{2} & \text { eigenvalue of } \sigma_{3}
\end{array}\right.$$
The $n^{\text {th }}$ energy level is therefore $2\left(n^{2}-q^{2}\right)$-fold degenerate. By supersymmetry, the positive spectrum of the superpartner $H_{1}$ is again (2.11) with the same multiplicities; the eigenstates carry the same labels (2.12). Zero modes only arise in the 'upper' sector. Setting
$$\psi_{1}=\binom{\frac{e^{i(q / 4 m) \psi}}{\sqrt{V}} \chi}{0},$$
where $\chi$ is a two-component Pauli spinor, the equation $\not \partial_{\psi}=0$ reduces to
$$\left[\vec{\sigma} \cdot \vec{\pi}-i\left(\frac{q}{4 m}\right) V\right] \chi=0 .$$
Applying the flat-space adjoint operator, $\vec{\sigma} \cdot \vec{\pi}+i(q / 4 m) V$, yields
$$\left[\vec{\pi}^{2}+2 q \frac{\vec{\sigma} \cdot \hat{\mathbf{r}}}{r^{2}}+\left(\frac{q}{4 m}\right)^{2}\left(1+\frac{4 m}{r}\right)^{2}\right] \chi=0,$$
which is precisely the zero-mode equation of the D'Hoker-Vinet 'dyon' [9]. For $m>0$, there are no zero modes. This is consistent with the known results [2]. For $m<0$, Eq. (2.15) admits $2 q$ normalizable solutions, described, e.g. in Ref. [10]. They have the lowest possible angular momentum, $j=q-\frac{1}{2}$, and are expressed as
$$\chi=r^{q-1} e^{-q r}\left(\sqrt{\frac{q+\frac{1}{2}-\mu}{2 q+1}} Y_{q}^{\mu-1 / 2}\binom{1}{0}-\sqrt{\frac{q+\frac{1}{2}+\mu}{2 q+1}} Y_{q}^{\mu+1 / 2}\binom{0}{1}\right),$$
$\mu=-\left(q-\frac{1}{2}\right), \ldots,\left(q-\frac{1}{2}\right)$. Scattering states arise for $E^{2}>(q / m)^{2}$. For a scalar particle, an incoming/outgoing state is characterized by its momentum $\vec{k}_{i n} \equiv \vec{k}$ and $\vec{k}_{\text {out }} \equiv \vec{k}^{\prime}$ respectively. The scalar $S$-matrix reads [3]
$$S_{0}\left(\vec{k}^{\prime} \mid \vec{k}\right)=\sum_{L \geq q}(2 L+1) \frac{(L-i \lambda)!}{(L+i \lambda)!} \mathcal{D}_{-q, q}^{L}\left(R^{-1}\left(\vec{k}^{\prime}\right) R(\vec{k})\right),$$
where $\lambda$ is as in Eq. (2.10), $\mathcal{D}_{m, n}^{L}$ is the rotation matrix and $R(\vec{k})$ denotes the rotation which takes the $z$-axis to the $\vec{k}$-direction. In the spinning case [11], for the $H_{0}$ dynamics, incoming/outgoing states get an extra label, namely the third component of the spin, $s$ and $s^{\prime}$, respectively. Since $s=\vec{k} \cdot \vec{\sigma} / 2$, the $S$-matrix of $H_{0}$ is simply
$$S\left(\vec{k}^{\prime}, s^{\prime} \mid \vec{k}, s\right)=S_{0}\left(\vec{k}^{\prime} \mid \vec{k}\right) \mathcal{D}_{s^{\prime}, s}^{1 / 2}\left(R^{-1}\left(\vec{k}^{\prime}\right) R(\vec{k})\right) .$$
Now if $\psi_{0}^{\text {in/out }}$ is any incoming/outgoing wave for the $H_{0}$, then $\psi_{1}=U\left(\psi_{0}^{\text {in/out }}\right)$ is one for $H_{1}$ with the same labels. Therefore, the $S$-matrix for $H_{1}$ is again Eq. (2.18), just like for $H_{0}$.

\section*{3. Bosonic symmetries}
$H_{0}$ is conveniently viewed as the Hamiltonian of a spin $\frac{1}{2}$ particle - but one with gyromagnetic ratio $g=0$. Being uncoupled, the spin vector,
$$\overrightarrow{\mathrm{S}}_{0}=\frac{1}{2} \vec{\sigma},$$
is conserved. SUSY carries this over to $H_{1}$ :
$$\overrightarrow{\mathrm{S}}_{1}=U^{\dagger} \overrightarrow{\mathrm{S}}_{0} U$$
is conserved conserved for $H_{1}$. (The explicit expression is not illuminating). The diagonal vector $\overrightarrow{\mathrm{S}}=$ $\operatorname{diag}\left(\overrightarrow{\mathrm{S}}_{1}, \overrightarrow{\mathrm{~S}}_{0}\right)$ is therefore conserved for $\not D$. Note that $\overrightarrow{\mathrm{S}}_{1}$ and $\overrightarrow{\mathrm{S}}_{0}$ are separately conserved for $H=\operatorname{diag}\left(H_{1}, H_{0}\right)$.

The Taub-NUT metric is radially symmetric. Therefore, the orbital angular momentum, $\vec{L}_{0}$, arises naturally when $H_{0}$ is viewed as describing two, uncoupled, spinless particles. But the total angular momentum,
$$\vec{J}=\vec{L}_{0}+\overrightarrow{\mathrm{S}}_{0},$$
is also natural, when $H_{0}$ is viewed as describing a $\operatorname{spin} \frac{1}{2}$ particle. $H_{0}$ admits therefore two independent conserved 'angular momentum' operators. The operators $\overrightarrow{\mathrm{S}}_{0}$ and $\vec{L}_{0}$ plainly commute, so we get an $\mathrm{o}(3) \oplus \mathrm{o}(3)$ symmetry. Again by supersymmetry, the superpartner, $H_{1}$, admits the same symmetries, namely $\overrightarrow{\mathrm{S}}_{1}$ in Eq. (3.2) and
$$\vec{L}_{1}=U^{\dagger} \vec{L}_{0} U .$$
Since the total angular momentum, $\vec{J}$, is invariant, $U^{\dagger} \vec{J} U=\vec{J}$, the partner of $\vec{L}_{0}=\vec{J}-\overrightarrow{\mathrm{S}}_{0}$ is also written as $\vec{L}_{1}=\vec{J}-\overrightarrow{\mathrm{S}}_{1}=\vec{L}_{0}+\overrightarrow{\mathrm{S}}_{0}-\overrightarrow{\mathrm{S}}_{1}$. The Dirac operator $\not D$ admits therefore the bosonic $\mathrm{o}(3) \oplus \mathrm{o}(3)$ symmetry, generated by
$$\overrightarrow{\mathrm{S}}=\operatorname{diag}\left(\overrightarrow{\mathrm{S}}_{1}, \overrightarrow{\mathrm{~S}}_{0}\right) \quad \text { and } \quad \vec{L}=\operatorname{diag}\left(\vec{L}_{1}, \vec{L}_{0}\right) .$$
These operators were found by van Holten using a quite different method. For example, $\vec{L}$ is his 'improved angular momentum'.
$H_{0}$ actually admits further symmetries [3], namely a Runge-Lenz vector,
$$\vec{K}_{0}=\frac{1}{2}\left\{\vec{\pi} \times \vec{L}_{0}-\vec{L}_{0} \times \vec{\pi}\right\}-4 m \hat{\mathbf{r}}\left(H_{0}-\left(\frac{q}{4 m}\right)^{2}\right) .$$
The vector operators $\vec{L}_{0}$ and $\vec{K}_{0}$ generate an $\mathrm{o}(3,1)$ dynamical symmetry for scattered motions and $\mathrm{o}(4)$ for bound motions, to which $\overrightarrow{\mathrm{S}}_{0}$ adds an extra o(3).

SUSY transports the Runge-Lenz vector to $H_{1}$ :
$$\vec{K}_{1}=U^{\dagger} \vec{K}_{0} U,$$
and then to $\not D$ to yield $\vec{K}=\operatorname{diag}\left(\vec{K}_{1}, \vec{K}_{0}\right)$. (The explicit form of $\vec{K}_{1}$ - presented in Ref. [5] - is very complicated). The dynamical symmetry can be used to derive the bound-state spectrum and the S-matrix: for fixed energy $H=E^{2}$, the Casimirs of the full system satisfy, by construction, the same relations as those of $H_{0}$, namely
$$\left\{\begin{array}{l}
\frac{\vec{K}}{\sqrt{E^{2}-(q / 4 m)^{2}}} \cdot \vec{L}=-4 m q \frac{E^{2} / 2-(q / 4 m)^{2}}{\sqrt{E^{2}-(q / 4 m)^{2}}}, \\
\left(\frac{\vec{K}}{\sqrt{E^{2}-(q / 4 m)^{2}}}\right)^{2}-\vec{L}^{2}=1-q^{2}+\left(4 m \frac{E^{2} / 2-(q / 4 m)^{2}}{\sqrt{E^{2}-(q / 4 m)^{2}}}\right)^{2}, \\
(\overrightarrow{\mathrm{~S}})^{2}=\frac{3}{4},
\end{array}\right.$$
confirming that the spin is indeed decoupled. From the representation theory of o(4) we infer that
$$4 m \frac{(q / 4 m)^{2}-E^{2} / 2}{\sqrt{(q / 4 m)^{2}-E^{2}}}=n, \quad n=q+1, \ldots$$
yielding the spectrum (2.11) once again. The scattering can be described using the spinning extension of Zwanziger's approach [11]; one finds Eq. (2.18) once again. It is worth stressing that the only effect of spin is to double the multiplicity for bound states, and to multiply the $S$ matrix by the spin factor, respectively.
4. Supersymmetry [12]

Consider first the supersymmetries of $H=\not D^{2}$, restricted to positive-energy states. Firstly, the two odd scalar charges
$$Q_{1}=\left(\begin{array}{cc}
0 & T^{\dagger} \\
T & 0
\end{array}\right), \quad Q_{2}=-i \gamma^{5} Q_{1}=\left(\begin{array}{cc}
0 & -i T^{\dagger} \\
i T & 0
\end{array}\right)$$
are both square-roots of $H$,
$$\left\{Q_{\alpha}, Q_{\beta}\right\}=2 \delta_{\alpha \beta} H .$$

Now the components of the two 'spins', $\overrightarrow{\mathrm{S}}_{0}$ and $\overrightarrow{\mathrm{S}}_{1}$, span two independent $\mathrm{o}(3) \simeq \operatorname{su}(2)$ 's,
$$\left[\mathrm{S}_{a}^{i}, \mathrm{~S}_{b}^{j}\right]=i \epsilon_{k}^{i j} \delta_{a b} \mathrm{~S}_{a}^{k},$$
$(a, b=0,1)$ as well as commute with $\gamma^{5}$,
$$\left[\gamma^{5}, \overrightarrow{\mathrm{~S}}_{a}\right]=0 .$$
But they also satisfy the anticommutation relation $\left\{\mathrm{S}_{a}^{i}, \mathrm{~S}_{b}^{j}\right\}=(1 / 2) \delta^{i j} \delta_{a b}$; therefore, the following two vector odd charges
$$\vec{Q}_{\alpha}=2 i\left[\overrightarrow{\mathrm{~S}}_{0}, Q_{\alpha}\right] \quad(\alpha=1,2)$$
also commute with $H=\not D^{2}$. The commutation relations are (4.3)-(4.4), augmented with
$$\begin{array}{ll}
{\left[\gamma^{5}, Q_{\alpha}\right]=2 i \epsilon_{\alpha \beta} Q_{\beta},} & {\left[\gamma^{5}, Q_{\alpha}^{k}\right]=2 i \epsilon_{\alpha \beta} Q_{\beta}^{k},} \\
{\left[S_{0}^{i}, Q_{\alpha}^{j}\right]=\frac{1}{2} i\left(\delta_{i j} Q_{\alpha}+\epsilon_{i j k} Q_{\alpha}^{k}\right),} & {\left[S_{1}^{i}, Q_{\alpha}^{j}\right]=-\frac{1}{2} i\left(\delta_{i j} Q_{\alpha}-\epsilon_{i j k} Q_{\alpha}^{k}\right),} \\
{\left[\overrightarrow{\mathrm{S}}_{0}, Q_{\alpha}\right]=-\frac{1}{2} i \vec{Q}_{\alpha},} & {\left[\overrightarrow{\mathrm{S}}_{1}, Q_{\alpha}\right]=\frac{1}{2} i \vec{Q}_{\alpha} .}
\end{array}$$
The anticommutation relations read in turn (4.2) and
$$\begin{aligned}
& \left\{Q_{\alpha}, \vec{Q}_{\beta}\right\}=-4 H \epsilon_{\alpha \beta}\left(\overrightarrow{\mathrm{S}}_{1}+\overrightarrow{\mathrm{S}}_{0}\right) \\
& \left\{Q_{\alpha}^{i}, Q_{\beta}^{j}\right\}=2 H \delta_{\alpha \beta} \delta_{i j}-4 H \epsilon_{\alpha \beta} \epsilon_{i j k}\left(S_{1}^{k}-S_{0}^{k}\right) .
\end{aligned}$$
Since all odd operators anticommute with $\gamma^{5}$, we conclude that $H=\not D^{2}$ admits the superalgebra $\mathrm{u}(2 / 2)$ as symmetry. It is easy to read off the symmetries of $\not D_{1} \equiv Q_{1}$ from these relations: $Q_{1}$ itself and
$$\vec{Q}_{2}=\left(\begin{array}{cc}
0 & \frac{i}{\sqrt{V}}(\vec{\pi}+i \vec{\sigma} \times \vec{\pi})-\left(\frac{q}{4 m}\right) \sqrt{V} \vec{\sigma} \\
-\frac{i}{V}(\vec{\pi}-i \vec{\sigma} \times \vec{\pi}) \sqrt{V}-\left(\frac{q}{4 m}\right) \sqrt{V} \vec{\sigma} & 0
\end{array}\right)$$
generate, with $\overrightarrow{\mathrm{S}}=\operatorname{diag}\left(\overrightarrow{\mathrm{S}}_{1}, \overrightarrow{\mathrm{~S}}_{2}\right)$, an $N=4$ sub-superalgebra:
$$\begin{array}{ll}
{\left[S^{i}, Q_{2}^{j}\right]=i \epsilon_{i j k} Q_{2}^{k},} & {\left[\overrightarrow{\mathrm{~S}}, Q_{1}\right]=0,} \\
\left\{Q_{1}, Q_{1}\right\}=2 H, & \left\{Q_{2}^{i}, Q_{2}^{j}\right\}=2 H \delta_{i j}, \quad\left\{Q_{1}, \vec{Q}_{2}\right\}=-4 H \overrightarrow{\mathrm{~S}} .
\end{array}$$
In Ref. [7], these supercharges are associated to Killing-Yano tensors.

\section*{5. Discussion}

Some of the results above can be generalized. The multi-Taub-NUT metric is given, for example, again by (2.1), but (2.2) replaced rather by
$$V=1+\sum_{i} \frac{4 m}{\left|\vec{r}-\vec{r}_{i}\right|} .$$
Requiring (anti) self-duality, $\vec{\nabla} V=-4 m \vec{B}$, we still obtain a solution of the vacuum Einstein equations. The square of $\not D$ is (1.1) with $H_{0}$ as in Eq. (2.6) (while $H_{1}$ is a complicated expression similar to the one before). The spin drops out again in the 'lower' sector, giving rise to the same supersymmetry algebra as above (while the o(4)/o(3, 1) Kepler symmetry is in general broken). Similar statements should hold for other self-dual metrics like the Eguchi-Hanson or Atiyah-Hitchin metric, etc.

Unlike in Ref. [5], our conserved electric charge $q$ contains no spin contribution. The explanation may well be the following one. Taub-NUT space has the geometry of $S^{3} \times \mathbf{R}^{+}$; the four-dimensional rotation group, SO(4), acts on the $S^{3}$ part by isometries. The $\partial_{\psi}=$ const. condition breaks SO(4) to SO(3) × SO(2); the conserved quantities associated to the SO(3) (respectively to SO(2)) are the total angular momentum, $\vec{J}$, and the electric charge, $q$, respectively. The conserved quantities can, however, be 'improved' [7]. For the SO(3), this yields the 'orbital' expressions $\vec{L}=\vec{J}-\vec{S}$. It is likely that the spin part of the 'charge' of Ref. [5] can be removed by a similar 'improvement', leaving us with the spin-independent $-i \partial_{\psi}$.

In the 'dyon' case, an additional conserved quantity is provided by the analog of Dirac's operator [10],
$$\mathcal{K}=\left(\begin{array}{cc}
0 & \vec{\sigma} \cdot \vec{\ell}+1 \\
-(\vec{\sigma} \cdot \vec{\ell}+1) & 0
\end{array}\right), \quad \vec{\ell}=\vec{r} \times \vec{\pi} .$$
$\mathcal{K}$ commutes with the Dirac operator and is associated to a Penrose-Floyd tensor [13]. It has the remarkable property, that its anticommutator with the vector supercharge $\vec{Q}_{2}$ reproduces the Runge-Lenz vector. More precisely,
$$\frac{1}{2}\left\{\vec{Q}_{2}, \mathcal{K}\right\}=\vec{K}-q(\vec{J}+\overrightarrow{\mathrm{S}}) .$$

The results of van Holten indicate, that a similar statement holds in the Taub-NUT case also. We have, however, not yet found the curved-space version of the $\mathcal{K}$ in Eq. (5.2); the obvious guess $\sqrt{V} \mathcal{K}$ neither commutes with $\not D$ nor agrees with Eq. (5.3) completely.

Another intriguing problem is to extend the bosonic o(4, 2) symmetry [3, 4] to the spinning case.

Acknowledgement. We are indebted to L. Fehér for enlightening discussions and for allowing us to use his unpublished notes. We thank also J. W. van Holten for correspondence.

\section*{References}
[1] D. Gross and M. J. Perry, Nucl. Phys. B226, 29 (1983); R. Sorkin, Phys. Rev. Lett. 51, 87 (1983).
[2] Z. F. Ezawa and A. Iwazaki, Phys. Lett. 138B, 81 (1984); M. Kobayashi and A. Sugamoto, Prog. Theor. Phys. 72, 122 (1984); A. Bais and P. Batenburg Nucl. Phys. B245, 469 (1984).
[3] G. W. Gibbons and N. Manton, Nucl. Phys. B274, 183 (1986); G. W. Gibbons and P. Ruback, Phys. Lett. 188B, 226 (1987); Comm. Math. Phys. 115, 267 (1988).
[4] L. Fehér and P. A. Horváthy, Phys. Lett. 183B, 182 (1987); B. Cordani, L. Fehér and P. A. Horváthy, Phys. Lett. 201B, 481 (1988) T. Iwai and Katayama, Journ. Geom. Phys. 12, 55 (1993).
[5] M. Visinescu, Phys. Lett. B339, 28 (1994); Class. Quant. Grav. 11, 1867 (1994).
[6] G. W. Gibbons, R. H. Rietdijk and J. W. van Holten, Nucl. Phys. B404, 42 (1993).
[7] J. W. van Holten, Phys. Lett. B342, 47 (1995).
[8] H. Boutaleb Joutei, A. Chakrabarti and A. Comtet, Phys. Rev. D21, 2280 (1980)
[9] E. D'Hoker and L. Vinet, Phys. Rev. Lett. 55, 1043 (1986).
[10] F. Bloore and P. A. Horváthy, Journ. Math. Phys. 33, 1869 (1992); M. Berrondo and H. V. McIntosh, Journ. Math. Phys. 11, 125 (1970).
[11] D. Zwanziger, Phys. Rev. 176, 1480 (1968); L. Gy. Fehér and P. A. Horváthy, Mod. Phys. Lett A3, 1451 (1988).
[12] L. Gy. Fehér, unpublished notes (1988); L. Gy. Fehér, P. A. Horváthy and L. O'Raifeartaigh, Int. Journ. Mod. Phys. A4, 5277 (1989).
[13] S. Durand, J.-M. Lina and L. Vinet, Lett. Math. Phys. 17, 289 (1989).