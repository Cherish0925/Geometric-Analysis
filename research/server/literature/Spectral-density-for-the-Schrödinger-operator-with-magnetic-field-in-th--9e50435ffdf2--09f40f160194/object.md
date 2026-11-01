# Spectral density for the Schrödinger operator with magnetic field in the unit complex ball: solutions of evolutionary equations and applications to special functions

- Category: papers
- Identity: doi:10.1007/s11868-021-00401-2
- Content status: fulltext_ok

---

---
source_file: Spectral_density_for_the_Schrödinger_operator_with_magnetic_field_in_the_unit_co_46bec28cbc8b.pdf
converter: mathpix
format: mmd
---

\title{
Spectral density for the Schrödinger operator with magnetic field in the unit complex ball: Solutions of evolutionary equations and applications to special functions
}

\author{
Nour eddine Askour ${ }^{1,2, a}$, Mohamed Bouaouid ${ }^{1, b}$ and Abdelkarim Elhadouni ${ }^{1, c}$ \\ ${ }^{1}$ Department of Mathematics, Sultan Moulay Slimane University, Faculty of Sciences and Technics, Beni Mellal, BP 523, 23000, Morocco. \\ \& \\ ${ }^{2}$ Department of Mathematics, Mohammed V University, Faculty of Sciences, Rabat, P.O. Box 1014, Morocco. \\ n.askour@usms.ma, ${ }^{b}$ bouaouidfst@gmail.com and ${ }^{c}$ Karimfstgma@gmail.com
}

\begin{abstract}
The Schwartz kernel of the spectral density for the Schrödinger operator with magnetic field in the $n$-dimensional complex ball is given. As applications, we compute the heat, resolvent and the wave kernels. Moreover, the resolvent and wave kernels are used to establish two new formulas for the Gauss-hypergeometric function.
\end{abstract}

Keywords: Spectral density; Self-adjoint operator; Fourier-Helgason transform; G-invariant Laplacian; Heat kernel; Wave kernel; Gauss-hypergeometric function; Reproducing kernels.

2010 Mathematics Subject Classification: 32A70; 58C40; 49K20; 34K08.

\section*{Contents}
1 Introduction ..... 3
$2 L^{2}$-Concrete harmonic analysis of the invariant Laplacian $\Delta_{v}$ and spec- tral interpretation ..... 8
3 Spectral density ..... 16
4 Heat and resolvent kernels ..... 26
5 Wave kernel ..... 30
6 Explicit formula for some generalized integrals ..... 31

\section*{1 Introduction}

The spectral density associated with a self-adjoint operator $T$ is considered as a powerful tool for developing more general functional calculus [9]. In particular, it gives the possibility to define the operator function $f(T)$ for a more generalized function $f$. It is well known that in quantum theory that each observable is represented by a self-adjoint operator on a complex Hilbert space. Thus for the study of quantum dynamic, the spectral density becomes a very efficient tool to solve evolutionary problems associated with such observable.
Recall that the Von Neumann spectral theorem says that any self-adjoint operator $T$ densely defined on a complex Hilbert space $H$ has a Stieltjes integral representation
$$T=\int_{-\infty}^{+\infty} \lambda d E_{\lambda}, \quad I=\int_{-\infty}^{+\infty} d E_{\lambda},$$
with respect to the some unique spectral measure $\left\{E_{\lambda}\right\}_{\lambda}([15,21,17])$. The spectral density
$$e_{\lambda}=\frac{d E_{\lambda}}{d \lambda},$$
is understood as an operator-valued distribution. It is an element of the space $\mathcal{D}^{\prime}(\mathbb{R}, L(D(T), H))$, where $L(D(T), H)$ is the space of bounded operator from $D(T)$ the domain of selfadjointness for T, to the whole Hilbert space $H$. In the case where $T$ is constant-coefficients elliptic operator with symbol $P$ on the whole space $\mathbb{R}^{n}$, i.e $T=P(i \partial)$, where $i \partial=i\left(\frac{\partial}{\partial x_{1}}, \ldots, \frac{\partial}{\partial x_{n}}\right)$. Then, the Schwartz kernel of the spectral density associated with its self-adjoint extension can be written as [9]
$$e(\lambda, x, y)=\frac{1}{(2 \pi)^{n}}\left\langle e^{i(x-y) \cdot \xi}, \delta(P(\xi)-\lambda)\right\rangle,$$
where $\delta(P(\xi)-\lambda)$ is the Layer distribution associated with the function $P(\xi)-\lambda$ and the dot product $(x-y) . \xi$ means the classical scalar product in $\mathbb{R}^{n}$.
For the general case, the explicit computation of the spectral density $e_{\lambda}$ in the concrete cases depends on the spectral tools which we dispose of. For example, based on the explicit resolvent kernel of the Khon-Laplacian in [4] the authors have used the Cauchy-integral representation of the resolvent operator with respect to the spectral measure for computing the spectral density. Also the method used in [4] has been fully adapted to the case of Heisenberg quaternionic Laplacian [18]. In [3] the author has used the explicit expression of the spectral family associated with the Schrödinger operator with the magnetic field in the n-Euclidean complex space, to get by a direct computation the corresponding spectral density.

In the present work, the explicit expression of the inverse Fourier-Helgason transform helps us to compute the spectral density for a Schrödinger operator with magnetic field on the complex hyperbolic space. Precisely, we will be concerned with the following class of Schrödinger operator
$$\Delta_{v}=4\left(1-|z|^{2}\right)\left\{\sum_{1 \leq i, j \leq n}\left(\delta_{i j}-z_{i} \bar{z}_{j}\right) \frac{\partial^{2}}{\partial z_{i} \partial \bar{z}_{j}}-v \sum_{j=1}^{n} \bar{z}_{j} \frac{\partial}{\partial \bar{z}_{j}}\right\},$$
in the unit ball $\mathbb{B}_{n}$ of the $n$-dimensional complex space, where the parameter $v$ is such that $v>n$ and $v \in \mathbb{R} \backslash \mathbb{Z}$. The operator $\Delta_{v}$ will be viewed as a linear operator acting on the Hilbert space $L_{\mathcal{V}}^{2}\left(\mathbb{B}_{n}\right):=L^{2}\left(\mathbb{B}_{n}, d \mu_{\nu}(z)\right)$, where $d \mu_{\nu}=\left(1-|z|^{2}\right.$ $)^{v-n-1} d m(z)$ with $d m(z)$ is the Lebesgue measure on $\mathbb{C}^{n}=\mathbb{R}^{2 n}$. This operator has been largely considered in several equivalent forms by many authors in different contexts [23, 1, 11, 12].
In order to make the operator $\Delta_{v}$ self-adjoint on the Hilbert space $L_{v}^{2}\left(\mathbb{B}_{n}\right)$, we must consider it on its maximal domain
$$\mathcal{D}=\left\{F \in L_{v}^{2}\left(\mathbb{B}_{n}\right), \quad \Delta_{v} F \in L_{v}^{2}\left(\mathbb{B}_{n}\right)\right\} .$$
Then, the spectrum of the operator $\Delta_{v}$ decomposes as
$$\sigma\left(\Delta_{v}\right)=\sigma_{p}\left(\Delta_{v}\right) \cup \sigma_{c}\left(\Delta_{v}\right),$$
where the point spectrum $\sigma_{p}\left(\Delta_{v}\right)$ is given by
$$\sigma_{p}\left(\Delta_{v}\right)=\left\{-\left(\lambda_{\ell}^{2}+(n-v)^{2}\right), \quad \lambda_{\ell}=-i(v-n-2 \ell), \quad \ell=0, \ldots,\left[\frac{v-n}{2}\right]\right\},$$
and the continuous spectrum is given by
$$\sigma_{c}\left(\Delta_{v}\right)=\left\{-\left(\lambda^{2}+(v-n)^{2}\right), \lambda \in \mathbb{R}\right\} .$$
In view point of spectral theory, the study of the operator $\Delta_{v}$ on the domain $\mathcal{D}$ is equivalent to the study of the following operator on the same domain
$$\tilde{\Delta}_{v}=-\left(\Delta_{v}+(n-v)^{2}\right),$$
which admits the set of positive real numbers as continuous spectrum. Thus, it suffice to compute the spectral density for the operator $\tilde{\Delta}_{v}$.
Before going a head, we give a concise picture of our results. Let then consider the spectral decomposition
$$\tilde{\Delta}_{v}=\int_{-\infty}^{+\infty} s d E_{s}^{v}, I=\int_{-\infty}^{+\infty} d E_{s}^{v},$$
where $\left\{E_{s}^{v}, s \in \mathbb{R}\right\}$ is the unique corresponding spectral measure. We are precisely concerned with the Schwartz kernel of the spectral density
$$e_{s}^{v}=\frac{d E_{s}^{v}}{d s},$$
which is an operator valued distribution, element of $\mathcal{D}^{\prime}\left(\mathbb{R}, L(\mathcal{D}), \mathrm{L}_{\mathcal{V}}^{2}\left(\mathbb{B}_{n}\right)\right)$. We prove that this Schwartz kernel can be expressed as
$$\begin{aligned}
e^{v}(s, w, z) & =\frac{\Gamma(n)}{4 \pi^{n+1} 2^{2(v-n)}}(1-\langle z, w\rangle)^{-v}\left|C_{v}(\sqrt{s})\right|^{-2}(\sqrt{s})^{-1} \chi_{+}(s) \phi_{\sqrt{s}}^{(n-1,-v)}(d(z, w)) \\
& +\sum_{j=0}^{\left[\frac{v-n}{2}\right]} c_{j} \frac{j!}{(n)_{j}}(1-\langle z, w\rangle)^{-v} P_{j}^{(n-1,-v)}(\cosh (2 d(z, w))) \delta\left(s-s_{j}\right)
\end{aligned}$$
with
$$\begin{aligned}
& s_{j}=-(2 j+v-n)^{2} ; j=0, \ldots,\left[\frac{v-n}{2}\right], \\
& c_{j}=\frac{2 \Gamma(n+j)}{\pi^{n} \Gamma(n) j!} \frac{(v-n-2 j) \Gamma(v-j)}{\Gamma(v-n-j+1)},
\end{aligned}$$
$\chi_{+}(s)$ is the characteristic function of the set of positive real numbers and
$$\phi_{\lambda}^{(\alpha, \beta)}(t)={ }_{2} F_{1}\left(\frac{\alpha+\beta+1-i \lambda}{2}, \frac{\alpha+\beta+1+i \lambda}{2}, 1+\alpha ;-\sinh ^{2} t\right),$$
is the Jacobi function $([14, \mathrm{p} .5]) . P_{j}^{(\alpha, \beta)}(x)$ denote the classical Jacobi polynomial of degree $j$ [20] and $d(z, w)$ is the distance corresponding to the Bergmann metric in the unit ball $\mathbb{B}_{n}([24, \mathrm{p} .25])$
$$\cosh ^{2}(d(z, w))=\frac{|1-<z, w>|^{2}}{\left(1-|z|^{2}\right)\left(1-|w|^{2}\right)},(z, w) \in \mathbb{B}_{n} \times \mathbb{B}_{n},$$
The function
$$c_{v}(\lambda)=\frac{2^{-v+n-i \lambda} \Gamma(n) \Gamma(i \lambda)}{\Gamma\left(\frac{i \lambda+n-v}{2}\right) \Gamma\left(\frac{i \lambda+n+v}{2}\right)}$$
is the analogous of the Harish-Chandra C-function defined in [23]. For more detail, we can also see [14]. As a consequence of the spectral density, we can give for the operator $\Delta_{v}$ the heat semigroup
$$e^{t \Delta_{v}}[\varphi](z)=\int_{\mathbb{B}_{n}} K_{v}(t, z, w) \varphi(w) d \mu_{v}(w)$$
where the heat kernel $K_{v}(t, z, w)$ is given by
$$\begin{aligned}
K_{v}(t, z, w) & =(1-\langle z, w\rangle)^{-v} \sum_{j=0}^{\left[\frac{v-n}{2}\right]} \tau_{j} e^{4 j(j+n-v) t} P_{j}^{(n-1,-v)}(\cosh (2 d(z, w)) \\
& +(1-\langle z, w\rangle)^{-v} e^{-t(v-n)^{2}} \frac{\Gamma(n)}{2 \pi^{n+1} 2^{2(v-n)}} \\
& \times \int_{0}^{+\infty} e^{-t \lambda^{2}}\left|C_{v}(\lambda)\right|^{-2}{ }_{2} F_{1}\left(\frac{n-v-i \lambda}{2}, \frac{n-v+i \lambda}{2}, n ;-\sinh ^{2}(d(z, w))\right) d \lambda
\end{aligned}$$
with the constant $\tau_{j}=\frac{2(v-n-2 j) \Gamma(v-j)}{\pi^{n} \Gamma(v-n-j+1)}$. From the above heat kernel formula, we give also the resolvent kernel of the operator $\Delta_{v}$. Precisely, we have
$$\left(\xi-\Delta_{v}\right)^{-1}[F](z)=\int_{\mathbb{B}_{n}} R_{v}(\xi, z, w) F(w) d \mu_{v}(w), \operatorname{Re}(\xi)>\omega(v, n),$$
where $\omega(\nu, n)=p_{n}^{\nu}-(n-\nu)^{2}$ with $p_{n}^{\nu}=\max \left\{\left|s_{j}\right|, 0 \leq j<\frac{v-n}{2}\right\}$ and $s_{j}=-(2 j+n-\nu)^{2}$. The resolvent kernel $R(\xi, z, w)$ is given as follows
$$\begin{aligned}
R(\xi, z, w) & =(1-\langle z, w\rangle)^{-v} \sum_{j=0}^{\left[\frac{v-n}{2}\right]} \tau_{j} \frac{1}{\lambda_{j}^{2}+(v-n)^{2}+\xi} P_{j}^{(n-1,-v)}(\cosh (2 d(z, w))) \\
& +(1-\langle z, w\rangle)^{-v} \frac{\Gamma(n)}{2 \pi^{n+1} 2^{2(v-n)}} \int_{0}^{+\infty} \frac{\left|c_{v}(\lambda)\right|^{-2}}{\lambda^{2}+(v-n)^{2}+\xi} \\
& \times{ }_{2} F_{1}\left(\frac{n-v-i \lambda}{2}, \frac{n-v-i \lambda}{2}, n,-\sinh ^{2}(d(z, w))\right) d \lambda
\end{aligned}$$
where $\lambda_{j}=-i(v-n-2 j)$ for $0 \leq j<\frac{v-n}{2}$.
Also by using the spectral density, we solve for the operator $\Delta_{v}$ the following wave Cauchy problem
$$\left\{\begin{array}{l}
\frac{\partial^{2} u(t, z)}{\partial t^{2}}=\Delta_{v} u(t, z),(t, z) \in \mathbb{R} \times \mathbb{B}_{n}, \\
u(0, z)=0, \frac{\partial u(0, t)}{\partial t}=f(z) \in C_{0}^{\infty}\left(\mathbb{B}_{n}\right) .
\end{array}\right.$$
Precisely, we have
$$u(t, z)=\int_{\mathbb{B}_{n}} W_{v}(t, z, w) F(w) d \mu_{v}(w),$$
where the wave kernel is given by
$$\begin{aligned}
& W_{v}(t, z, w)=(1-<z, w>)^{-v} \sum_{j=0}^{\left[\frac{v-n}{2}\right]} \tau_{j} \frac{\sin (2 t \sqrt{j(v-n-j)}}{2 \sqrt{j(v-n-j)}} P_{j}^{(n-1,-v)}(\cosh (2 d(z, w))) \\
& \quad+(1-<z, w>)^{-v} \frac{\Gamma(n)}{2 \pi^{n+1} 2^{2(v-n)}} \\
& \quad \times \int_{0}^{+\infty} \frac{\sin \left(t \sqrt{\lambda^{2}+(n-v)^{2}}\right)}{\sqrt{\lambda^{2}+(n-v)^{2}}}\left|C_{v}(\lambda)\right|^{-2}{ }_{2} F_{1}\left(\frac{n-v-i \lambda}{2}, \frac{n-v+i \lambda}{2}, n ;-\sinh ^{2}(d(z, w))\right) d \lambda
\end{aligned}$$
We end this summary by given an application to special functions. Precisely, we obtain (up to our knowledge) two new integral formulas for the Gauss-hypergeometric function as will be stated below in the two following propositions.

Proposition 1.1. Let $v>n, v \in \mathbb{R} \backslash \mathbb{Z}$ and $0 \leq x<\sinh (|t|)$ for $t \in \mathbb{R}$, then we have the following integral formula
$$\begin{aligned}
& \int_{0}^{+\infty}\left|\frac{\Gamma\left(\frac{i \lambda+n-v}{2}\right) \Gamma\left(\frac{i \lambda+n+v}{2}\right)}{\sqrt{\lambda} \Gamma(i \lambda)}\right|^{2} \times{ }_{2} F_{1}\left(\frac{n-v-i \lambda}{2}, \frac{n-v+i \lambda}{2}, n ;-x\right) \sin (t \lambda) d \lambda \\
& =(-1)^{n-1} \pi \frac{\Gamma\left(n-\frac{1}{2}\right)}{\Gamma(n)}(1+x)^{\frac{v-n}{2}}\left(\frac{\sinh ^{2}(t)}{1+x}-1\right)_{+}^{-n+\frac{1}{2}} \\
& \times{ }_{2} F_{1}\left(1-n+v, 1-n-v, \frac{3}{2}-n, \frac{1}{2}-\frac{\cosh (t)}{2 \sqrt{1+x}}\right) \\
& -2^{2(v-n+1)} \frac{\pi}{\Gamma(n)} \sum_{j=0}^{\left[\frac{v-n}{2}\right]} \frac{(v-n-2 j) \Gamma(v-j)}{\Gamma(v-n-j+1)} P_{j}^{(n-1,-v)}(2 x+1) \frac{\sinh (t(2 j+n-v))}{2 j+n-v} .
\end{aligned}$$

Proposition 1.2. Let $v>n, v \in \mathbb{R} \backslash \mathbb{Z}$ and $\mu$ is a complex number such that $\mu \neq$ $-i(2 \ell+n \pm v)$ for $\ell=0,1,2, \ldots$ and $\operatorname{Re}\left(\mu^{2}\right)<-P_{n}^{v}$, with $p_{n}^{v}=\max \left\{\left|s_{j}\right|, 0 \leq j<\frac{v-n}{2}\right\}$ and
$s_{j}=-(2 j+n-v)^{2}$. Then, we have the following integral formula
$$\begin{aligned}
& \int_{0}^{+\infty}\left|\frac{\Gamma\left(\frac{i \lambda+n-v}{2}\right) \Gamma\left(\frac{i \lambda+n+v}{2}\right)}{\Gamma(i \lambda)}\right|^{2} \frac{1}{\lambda^{2}-\mu^{2}} \times{ }_{2} F_{1}\left(\frac{n-v-i \lambda}{2}, \frac{n-v+i \lambda}{2}, n,-x\right) d \lambda \\
& =\pi 2^{2(v-n)} \frac{\Gamma\left(\frac{n-i \mu+v}{2}\right) \Gamma\left(\frac{n-i \mu-v}{2}\right)}{\Gamma(n) \Gamma(1-i \mu)}(1+x)^{\frac{v+i \mu}{4}-\frac{n}{2}} \\
& \times{ }_{2} F_{1}\left(\frac{n-i \mu+v}{2}, \frac{n-i \mu-v}{2}, 1-i \mu, \frac{1}{1+x}\right) \\
& -\frac{4 \pi}{\Gamma(n)} 2^{2(v-n)} \sum_{j=0}^{\left[\frac{v-n}{2}\right]} \frac{(v-n-2 j) \Gamma(v-j)}{\Gamma(v-n-j+1)} \frac{1}{\lambda_{j}^{2}-\mu^{2}} P_{j}^{(n-1,-v)}(2 x+1) .
\end{aligned}$$

This paper is summarized as follows. In section 2, we review some results for the Laplacian $\Delta_{v}$ in the frame work of $L^{2}$-concrete harmonic analysis. In section 3, we give the expression of the spectral density for the operator $\tilde{\Delta}_{v}$. Section 4 is devoted to some applications as the heat semi-group, resolvent and wave kernels. In section 5, a special application of our results is reserved to establish two new integral formulas for the Gauss-hypergeometric function.

\section*{$2 L^{2}$-Concrete harmonic analysis of the invariant Laplacian $\Delta_{v}$ and spectral interpretation}

In this section we review some results on the $L^{2}$-concrete harmonic analysis of the Laplacian $\Delta_{v}$ defined in (2.12). To do so, we endow the Euclidian complex space $\mathbb{C}^{n}$ with the inner product
$$\langle z, w\rangle=z_{1} \bar{w}_{1}+z_{2} \bar{w}_{2}+\ldots+z_{n} \bar{w}_{n} .$$
The open unit ball $\mathbb{B}_{n}$ in $\mathbb{C}^{n}$ consists of $n$-tuples $z=\left(\begin{array}{c}z_{1} \\ \vdots \\ z_{n}\end{array}\right)$ for which
$$|z|^{2}=\left|z_{1}\right|^{2}+\ldots+\left|z_{n}\right|^{2}<1 .$$
The ball $\mathbb{B}_{n}$ can be identified with the unit ball of $\mathbb{R}^{2 n}$ and thus can be equipped with the Lebesgue measure $d m(z)=r^{2 n-1} d r d \sigma(w)$ where $d \sigma$ is the rotation invariant measure on the sphere $\partial \mathbb{B}_{n}=S^{2 n-1}$.
The group $G:=S U(1, n)$ consists all matrices with determinant equal one and preserve the sesquilinear form
$$\langle z, J w\rangle=z_{1} \bar{w}_{1}+z_{2} \bar{w}_{2}+\ldots+z_{n} \bar{w}_{n}-z_{n+1} \bar{w}_{n+1},$$
where
$$J=\left(\begin{array}{cc}
I_{n} & 0 \\
0 & -1
\end{array}\right) .$$
We usually write a matrix $g$ in $S U(1, n)$ in block form as
$$g=\left(\begin{array}{ll}
A & B \\
C & D
\end{array}\right) .$$
Where $A, B, C$ and $D$ are $n \times n, n \times 1,1 \times n$ and $1 \times 1$ matrixes with complex entries, respectively. Then by definition $g$ is in $S U(1, n)$ if and only if $\operatorname{det}(g)=1$ and $g^{*} J g=J$. This immediately gives that
$$g^{-1}=J g^{*} J=\left(\begin{array}{cc}
A^{*} & -C^{*} \\
-B^{*} & D^{*}
\end{array}\right) .$$
The group $S U(1, n)$ acts transitively on $\mathbb{B}_{n}$ via the fractional linear transformations
$$g \cdot z=\left(\begin{array}{ll}
A & B \\
C & D
\end{array}\right) z:=(A z+B)(C z+D)^{-1} .$$
Recall that for $g=\left(\begin{array}{ll}A & B \\ C & D\end{array}\right)$ the above action satisfy the following relation
$$1-<g . z, g . w>=\frac{1-<z, w>}{(C z+D) \overline{(C w+D)}} .$$
We denote by $U(1)$ and $U(n)$ the set of unimodular complex numbers and the set of complex unitary matrices, respectively. The origin in $\mathbb{C}^{n}$ is noted by 0. Recall that the stabilizer $K$ of $0 \in \mathbb{B}_{n}$ is given by
$$K=\left\{\left(\begin{array}{cc}
A & 0 \\
0 & B
\end{array}\right), A \in U(n), B \in U(1) \text { and } \operatorname{det}(A B)=1\right\}$$
which is the maximal compact subgroup of $S U(1, n)$. It is well known that the space $S U(1, n) / K$ is holomorphically isometric to $\mathbb{B}_{n}$ as Bargmann ball [22]. Also, the Bargmann ball $\mathbb{B}_{n}$ can be viewed as a complex hyperbolic space. Thus, we have the following identification
$$\mathbb{B}_{n}=S U(1, n) / K .$$
The group $G$ acts unitarly on the Hilbert space $L_{\nu}^{2}\left(\mathbb{B}_{n}\right):=L^{2}\left(\mathbb{B}_{n}, d \mu_{\nu}\right)$, where $d \mu_{\nu}=$ $\left(1-|z|^{2}\right)^{v-n-1} d m(z)$ with $d m(z)$ is the Lebesgue measure on $\mathbb{C}^{n}$ via
$$T^{v}(g) F(z)=J\left(g^{-1}, z\right)^{\frac{v}{n+1}} F\left(g^{-1} . z\right),$$
where $v$ is a non integer real parameter such that $v>n$ and $J\left(g^{-1}, z\right)$ is the complex Jacobian of the matrix $g^{-1}$. Then $T$ is a unitary representation of $G=S U(1, n)$ in [23]. For more detail, we refer to [7] and references therein. The corresponding $G$-invariant Laplacian was found in [23]. It is of the form
$$\Delta_{v}=4\left(1-|z|^{2}\right)\left\{\sum_{1 \leq i, j \leq n}\left(\delta_{i j}-z_{i} \bar{z}_{j}\right) \frac{\partial^{2}}{\partial z_{i} \partial \bar{z}_{j}}-v \sum_{j=1}^{n} \bar{z}_{j} \frac{\partial}{\partial \bar{z}_{j}}\right\} .$$
As mentioned in the introduction, we are precisely concerned with the G-invariant self adjoint operator
$$\tilde{\Delta}_{v}=-\left(\Delta_{v}+(v-n)^{2}\right),$$
maximally defined on the domain
$$\mathcal{D}=\left\{F \in L_{v}^{2}\left(\mathbb{B}_{n}\right), \quad \Delta_{v} F \in L_{v}^{2}\left(\mathbb{B}_{n}\right)\right\} .$$
According to [23] a fundamental family of eigenfunctions of $\Delta_{v}$ with eigenvalue $-\left((v-n)^{2}+\lambda^{2}\right)$ was given by the following family of Poisson kernels
$$P_{\lambda}^{v}(z, \omega)=\left(\frac{1-|z|^{2}}{|1-<z, \omega>|^{2}}\right)^{\frac{i \lambda+n-v}{2}}(1-<z, \omega>)^{-v}, z \in \mathbb{B}_{n}, \omega \in \partial \mathbb{B}_{n}$$
representing the function $e_{\lambda, w}(z)$ in [23]. Then the Fourier-Helgason transform (the generalized Fourier transform) is defined by
$$\tilde{F}(\lambda, \omega)=\int_{\mathbb{B}_{n}} F(z) P_{-\lambda}^{v}(z, \omega) d \mu_{v}(z),$$
for $F$ in $C_{0}^{\infty}\left(\mathbb{B}_{n}\right)$, the space of $C^{\infty}$-functions on $\mathbb{B}_{n}$ with compact support. Note that $\tilde{F}(\lambda, \omega)$ is extended to an entire function of $\lambda$.
Recall that if we take $\alpha=v-n-1$ in Theorem 2 given in [23], the condition $v>n$ and non integer lead us to write the following inversion formula for the Fourier-Helgason transform
$$\begin{aligned}
F(z) & =\frac{1}{4} \frac{\Gamma(n)}{2^{2(v-n)} \pi^{n+1}} \int_{\partial \mathbb{B}_{n}} \int_{\mathbb{R}} \tilde{F}(\lambda, \omega) P_{\lambda}^{v}(z, \omega)\left|C_{v}(\lambda)\right|^{-2} d \lambda d \sigma(\omega) \\
& +\sum_{j=0}^{\left[\frac{v-n}{2}\right]} c_{j} \int_{\partial \mathbb{B}_{n}} \tilde{F}\left(\lambda_{j}, \omega\right) P_{\lambda_{j}}^{v}(z, \omega) d \sigma(\omega)
\end{aligned}$$
with $F \in C_{0}^{\infty}\left(\mathbb{B}_{n}\right),\left[\frac{v-n}{2}\right]$ is the integral part of $\frac{v-n}{2}$ and $c_{j}$ are the constants defined by equation (1.5) in [23] as
$$c_{j}=\frac{\Gamma(n+j) \Gamma(k+1-j) \Gamma(v)(v-n-2 j)}{\pi^{n} \Gamma(n) \Gamma(v-n+1-j)(-1)^{j} \prod_{j^{\prime}=0, j^{\prime} \neq j}^{k}\left(j^{\prime}-j\right)},$$
$$\lambda_{j}=-i(v-n-2 j) \text { for } j=0, \ldots,\left[\frac{v-n}{2}\right] .$$
Moreover, the operators
$$P_{j}[F](z)=c_{j} \int_{\partial \mathbb{B}_{n}} \tilde{F}\left(\lambda_{j}, \omega\right) P_{\lambda_{j}}^{v}(z, \omega) d \sigma(\omega),$$
appearing in the discrete part of formula (2.17) can be extended to pairwise orthogonal projections on $L_{v}^{2}\left(\mathbb{B}_{n}, d \mu_{v}\right)$ ([23]). In order to give a spectral interpretation of formula (2.17), we need the following Lemma.

Lemma 2.1. [6] Let $\alpha, \beta$ be two real numbers and let $\Delta_{\alpha, \beta}$ be the following Laplacians
$$\Delta_{\alpha, \beta}=4\left(1-|z|^{2}\right)\left\{\sum_{1 \leq i, j \leq n}\left(\delta_{i, j}-z_{i} \bar{z}_{j}\right) \frac{\partial^{2}}{\partial z_{i} \partial \bar{z}_{j}}+\alpha \sum_{j=1}^{n} z_{j} \frac{\partial}{\partial z_{j}}+\beta \sum_{j=1}^{n} \bar{z}_{j} \frac{\partial}{\partial \bar{z}_{j}}-\alpha \beta\right\}$$
acting on the Hilbert space $L^{2}\left(\mathbb{B}_{n},\left(1-|z|^{2}\right)^{-(\alpha+\beta+n)-1} d m(z)\right)$. Then, for every $\gamma \in \mathbb{R}$, we have the following intertwining relation
$$\Delta_{\alpha, \beta}=M^{-1} \circ\left[\Delta_{\alpha-\gamma, \beta-\gamma}-4 \gamma(\alpha+\beta+n-\gamma)\right] \circ M,$$
where $M$ is the unitary operator defined by
$$\begin{aligned}
M: L_{\alpha, \beta}^{2}\left(\mathbb{B}_{n}\right) & \longrightarrow L_{\alpha-\gamma, \beta-\gamma}^{2}\left(\mathbb{B}_{n}\right) \\
F(z) & \longmapsto\left(1-|z|^{2}\right)^{-\gamma} F(z) .
\end{aligned}$$

Before given a spectral interpretation of the discrete part involved in formula (2.17), we will give the following remark.

Remark 2.1. The family of operators $\Delta_{\alpha, \beta}$ (with slight modifications) was considered by many authors in several contexts [6, 2, 12]. But in view point of $L^{2}$-spectral theory, the study of such operators can be reduced by means of the above lemma to the study of the operators $\Delta_{v}$ with $v=\alpha-\beta$. So, the consideration of the operators $\Delta_{v}$ is not restrictive.

With the help of the above lemma, we can state the following proposition.
Proposition 2.1. The operator $\Delta_{v}$ given in (2.12) and defined on the Hilbert space $L_{\nu}^{2}\left(\mathbb{B}_{n}\right)$ with maximal domain
$$\mathcal{D}=\left\{F \in L_{v}^{2}\left(\mathbb{B}_{n}\right), \quad \Delta_{v} F \in L_{v}^{2}\left(\mathbb{B}_{n}\right)\right\},$$
is self-adjoint and its spectrum decomposes as
$$\sigma\left(\Delta_{v}\right)=\sigma_{p}\left(\Delta_{v}\right) \cup \sigma_{c}\left(\Delta_{v}\right),$$
where the point spectrum $\sigma_{p}\left(\Delta_{\nu}\right)$ is given by
$$\sigma_{p}\left(\Delta_{v}\right)=\left\{-\left(\lambda_{l}^{2}+(n-v)^{2}\right), \lambda_{l}=-i(v-n-2 l) \text { for } l=0, \ldots,\left[\frac{v-n}{2}\right]\right\}$$
and the continuous spectrum is as follows
$$\sigma_{c}\left(\Delta_{v}\right)=\left\{-\left(\lambda^{2}+(v-n)^{2}\right), \lambda \in \mathbb{R}\right\} .$$

For the proof of this proposition we refer to the Proposition 2 in [12]. The reader can be see also the following references [8, 2]. Now, we are in position to give a spectral interpretation for the discrete part of formula (2.17). Precisely, we have.
Proposition 2.2. Let $l \in \mathbb{Z}_{+}, 0 \leq l<\frac{v-n}{2}$ and let the eigenspace
$$\mathscr{E}_{\rho_{l}}^{v}\left(\mathbb{B}_{n}\right)=\left\{F \in L_{v}^{2}\left(\mathbb{B}_{n}\right), \quad \Delta_{v} F=\rho_{l} F\right\}$$
associated with the eigenvalue $\rho_{l}=-\left(\lambda_{l}^{2}+(n-v)^{2}\right)$ with $\lambda_{l}=-i(v-n-2 l)$. Then, we have
\begin{itemize}
\item[i)] The vector space $\mathscr{E}_{\rho_{l}}^{v}\left(\mathbb{B}_{n}\right)$ is a closed subspace of $L_{v}^{2}\left(\mathbb{B}_{n}\right)$.
\item[ii)] The orthogonal projector $\Pi_{l}$ on the subspace $\mathscr{E}_{\rho_{l}}^{v}\left(\mathbb{B}_{n}\right)$ coincide with the projector $P_{l}$ defined in (2.20).
\item[iii)] The constant $c_{l}$ defined by formula (2.18) can be also written as
$$c_{l}=\frac{2 \Gamma(n+l)}{\pi^{n} \Gamma(n) l!} \frac{(v-n-2 l) \Gamma(v-l)}{\Gamma(v-n-l+1)} .$$
\end{itemize}
Proof. First, it is not difficult to see that the operator $\Delta_{v}$ is densely defined. Then, by using the well know relation between the range $R(T)$ of a densely defined operator $T$ and the kernel of its adjoint $N\left(T^{*}\right)=R(T)^{\perp}$ (see [21, p.9] for the general theory). Then, by using the self-adjointness of $\Delta_{\nu}$, we obtain the closeness of the space $\mathscr{E}_{\rho_{l}}^{v}\left(\mathbb{B}_{n}\right)=N\left(\Delta_{v}-\rho_{l}\right)$. Note that for the operator $P_{l}$ defined in (2.20) it is proved in [23] that is an integral operator with the kernel
$$K_{l}^{v}(z, w)=c_{l}(1-<z, w>)^{-v}{ }_{2} F_{1}\left(-l, l-v+n ; n ; 1-\frac{|1-<z, w>|^{2}}{\left(1-|z|^{2}\right)\left(1-|w|^{2}\right)}\right),$$
and $c_{l}$ is the constant given in equation (2.18). Then, by the general theory, the kernel $K_{l}^{v}(z, w)$ is also the reproducing kernel of the subspace
$$A_{l}^{v, 2}\left(\mathbb{B}_{n}\right):=P_{l}\left(L_{v}^{2}\left(\mathbb{B}_{n}\right)\right) .$$

In other hand, by taking $\alpha=0, \beta=-v$ and $\gamma=\frac{-v}{2}$ in formula (2.22) of Lemma (2.1), we obtain the following relation
$$\Delta_{v}=\left(1-|z|^{2}\right)^{-v / 2}\left(\Delta_{v / 2,-v / 2}+2 v\left(n-\frac{v}{2}\right) I\right)\left(1-|z|^{2}\right)^{v / 2}$$
with
$$\Delta_{v / 2,-v / 2}=4\left(1-|z|^{2}\right)\left\{\sum_{1 \leq i, j \leq n}\left(\delta_{i, j}-z_{i} \bar{z}_{j}\right) \frac{\partial^{2}}{\partial z_{i} \partial \bar{z}_{j}}+\frac{v}{2} \sum_{j=1}^{n}\left(z_{j} \frac{\partial}{\partial z_{j}}-\bar{z}_{j} \frac{\partial}{\partial \bar{z}_{j}}\right)+\frac{v^{2}}{4}\right\} .$$
Remark that the operator $\Delta_{v / 2,-v / 2}$ can be written in terms of the operator $H_{B, \rho}$, defined in [11, p.2] for $B=\frac{v}{2}$ and $\rho=1$, as follows
$$\Delta_{v / 2,-v / 2}=-H_{v / 2,1}+v^{2},$$
with
$$H_{v / 2,1}=-4\left(1-|z|^{2}\right)\left\{\sum_{1 \leq i, j \leq n}\left(\delta_{i, j}-z_{i} \bar{z}_{j}\right) \frac{\partial^{2}}{\partial z_{i} \partial \bar{z}_{j}}+\frac{v}{2} \sum_{j=1}^{n}\left(z_{j} \frac{\partial}{\partial z_{j}}-\bar{z}_{j} \frac{\partial}{\partial \bar{z}_{j}}\right)\right\}+v^{2}|z|^{2} .$$
Then, the relation (2.32) can be rewritten as
$$\Delta_{v} F=\left(1-|z|^{2}\right)^{-v / 2}\left(-H_{v / 2,1}+2 v n I\right)\left(1-|z|^{2}\right)^{v / 2} F, F \in \mathcal{D} \subset L_{v}^{2}\left(\mathbb{B}_{n}\right) .$$
Recall that from [11, p.2] the point spectrum of the operator $H_{v / 2,1}$ acting on the Hilbert space $L_{v}^{2}\left(\mathbb{B}_{n},\left(1-\mid z^{2}\right)^{-n-1} d m(z)\right)$ is given by
$$\sigma_{p}\left(H_{v / 2,1}\right)=\left\{q_{l}=2 v(2 l+n)-4 l(l+n), l \in \mathbb{Z}_{+}, 0 \leq l<\frac{v-n}{2}\right\} .$$
Also, recall that the eigenspace $\mathscr{E}_{l}^{v}\left(\mathbb{B}_{n}\right)$ corresponding to the eigenvalue $\rho_{l}=-\left(\lambda_{l}^{2}+(n-v)^{2}\right)=4 l(l+n-v)$ is a closed subspace of $L_{v}^{2}\left(\mathbb{B}_{n}\right)$. Let us denote by $H_{l}^{\nu}(z, w)$ the reproducing kernel of the space $\mathscr{E}_{l}^{\nu}\left(\mathbb{B}_{n}\right)$. Our aims in this part is to compute this reproducing kernel. To this end, we consider $F$ in $\mathscr{E}_{l}^{v}\left(\mathbb{B}_{n}\right)$, then from relation (2.36) we have the following formula
$$H_{v / 2,1}\left[\left(1-|z|^{2}\right)^{v / 2} F\right]=\left(2 v n-\rho_{l}\right)\left(1-|z|^{2}\right)^{v / 2} F .$$
Remark that $2 v n-\rho_{l}=q_{l}$ and $\left(1-|z|^{2}\right)^{v / 2} F \in L_{v}^{2}\left(\mathbb{B}_{n},\left(1-|z|^{2}\right)^{-n-1} d m(z)\right)$. Then, the function $\left(1-|z|^{2}\right)^{v / 2} F$ belongs to the eigenspace of the operator $H_{v / 2,1}$ with $q_{l}$ as the associated eigenvalue. Recall that, by (i) of Proposition 7 in [11] the reproducing
kernel of this last eigenspace is given by the formula
$$\begin{aligned}
K_{l, 1}^{v / 2}(z, w) & =A_{n, v / 2, l}(1)\left(\frac{\overline{1-\langle z, w\rangle}}{1-\langle z, w\rangle}\right)^{v / 2}\left(\frac{\left(1-|z|^{2}\right)\left(1-|w|^{2}\right)}{|1-\langle z, w\rangle|^{2}}\right)^{v / 2-l} \\
& \times{ }_{2} F_{1}\left(-l, v-l, n, 1-\frac{\left(1-|z|^{2}\right)\left(1-|w|^{2}\right)}{|1-\langle z, w\rangle|^{2}}\right),
\end{aligned}$$
with
$$A_{n, v / 2, l}(1)=\frac{1}{\pi^{n}} \frac{\Gamma(l+n)}{\Gamma(n) l!} \frac{(v-n-2 l) \Gamma(v-l)}{\Gamma(v-n-l+1)} .$$
Then for the function $\left(1-|z|^{2}\right)^{v / 2} F$, we can write the reproducing formula
$$\left(1-|z|^{2}\right)^{v / 2} F(z)=\int_{\mathbb{B}_{n}} K_{l, 1}^{v / 2}(z, w)\left(1-|w|^{2}\right)^{v / 2} F(w)\left(1-|w|^{2}\right)^{-n-1} d m(w)$$
its follows that the reproducing kernel $H_{l}^{v}(z, w)$ of the eigenspace $\mathscr{E}_{l}\left(\mathbb{B}_{n}\right)$ is given by
$$H_{l}^{v}(z, w)=\left(1-|z|^{2}\right)^{-v / 2} K_{l, 1}^{v / 2}(z, w)\left(1-|w|^{2}\right)^{-v / 2} .$$
From the expression of the kernel $K_{l, 1}^{v / 2}(z, w)$ given in (2.39), it follows that
$$\begin{aligned}
H_{l}^{v}(z, w) & =\left(1-|z|^{2}\right)^{-v / 2}\left(1-|w|^{2}\right)^{-v / 2} A_{n, v / 2, l}(1)\left(\frac{\overline{1-\langle z, w\rangle}}{1-\langle z, w\rangle}\right)^{v / 2}\left(\frac{\left(1-|z|^{2}\right)\left(1-|w|^{2}\right)}{|1-\langle z, w\rangle|^{2}}\right)^{v / 2-l} \\
& \times{ }_{2} F_{1}\left(-l, v-l ; n ; 1-\frac{\left(1-|z|^{2}\right)\left(1-|w|^{2}\right)}{|1-\langle z, w\rangle|^{2}}\right) \\
& =A_{n, v / 2, l}(1)(1-<z, w>)^{-v}\left(\frac{|1-\langle z, w\rangle|^{2}}{\left(1-|z|^{2}\right)\left(1-|w|^{2}\right)}\right)^{l} \\
& \times{ }_{2} F_{1}\left(-l, v-l ; n ; 1-\frac{\left(1-|z|^{2}\right)\left(1-|w|^{2}\right)}{|1-<z, w>|^{2}}\right)
\end{aligned}$$
By using the change of variable
$$1-\frac{\left(1-|z|^{2}\right)\left(1-|w|^{2}\right)}{|1-\langle z, w\rangle|^{2}}=\frac{x}{x-1},$$
the equation (2.43) becomes
$$H_{l}^{v}(z, w)=A_{n, v / 2, l}(1)(1-<z, w>)^{-v}(1-x)^{l}{ }_{2} F_{1}\left(-l, v-l ; n ; \frac{x}{x-1}\right) .$$

Applying the following formula [16, p.47]
$${ }_{2} F_{1}(a, b ; c ; z)=(1-z)^{-a}{ }_{2} F_{1}\left(a, c-b ; c ; \frac{z}{z-1}\right) .$$
For $a=-l, b=n+l-v$ and $c=n$, the equation (2.45) can be rewritten as
$$H_{l}^{v}(z, w)=A_{n, v / 2, l}(1)(1-<z, w>)^{-v}{ }_{2} F_{1}\left(-l, n+l-v ; n ; 1-\frac{|1-<z, w>|^{2}}{\left(1-|z|^{2}\right)\left(1-|w|^{2}\right)}\right),$$
where $A_{n, v / 2, l}(1)$ is the constant defined in (2.40). Taking into account that the function $H_{l}^{v}(z, w)$ defined in (2.43) which is the reproducing kernel of the space $\mathscr{E}_{l}^{v}\left(\mathbb{B}_{n}\right)$ can be rewritten in terms of the function $K_{l}^{v}(z, w)$ defined in (2.30) as follows
$$H_{l}^{v}(z, w)=\kappa K_{l}^{v}(z, w),$$
where the constant $\kappa$ is give by
$$\kappa=\frac{A_{n, v / 2, l}(1)}{c_{l}} .$$
Is not hard to see that $\kappa>0$, then we can consider on the space $\mathscr{E}_{l}^{v}\left(\mathbb{B}_{n}\right)$ the following new scalar product
$$<f, g>_{\kappa}=\kappa<f, g>, \text { for } f, g \in \mathscr{E}_{l}^{v}\left(\mathbb{B}_{n}\right) .$$
It is easy to see that the space $\left(\mathscr{E}_{l}^{\mathcal{V}}\left(\mathbb{B}_{n}\right),<>_{\kappa}\right)$ is a reproducing kernel Hilbert space which having the function $K_{l}^{v}(z, w)$ as reproducing kernel. Then, by using Proposition 2.3 in [19, p.18], we deduce that
$$A_{l}^{v, 2}\left(\mathbb{B}_{n}\right)=\mathscr{E}_{l}^{v}\left(\mathbb{B}_{n}\right) \text { and }\|f\|_{\kappa}=\|f\| .$$
Then, we obtain
$$\kappa\|f\|=\|f\| \text {, for all } f \in \mathscr{E}_{l}^{v}\left(\mathbb{B}_{n}\right) .$$
It follows that $\kappa=1$, so we obtain $c_{l}=A_{n, v / 2, l}(1)$ and thus the projector $P_{l}$ on $A_{l}^{v, 2}\left(\mathbb{B}_{n}\right)$ is also the projector on the eigenspace $\mathscr{E}_{l}^{v}\left(\mathbb{B}_{n}\right)$. Hence the discrete part in formula (2.5) correspond to the orthogonal projection of a function $f \in C_{0}^{\infty}\left(B_{n}\right)$ on the orthogonal direct sum
$$\bigoplus_{0 \leq l<\frac{v-n}{2}} \mathscr{E}_{l}^{v}\left(\mathbb{B}_{n}\right) .$$

Now, for a spectral interpretation of the continuous part of formula (2.17), is not hard to see that the involved integral can be written as an integral with respect to the parameter $\lambda$ over the set $\mathbb{R}$ of the following $C^{\infty}$-eigenfunctions of the operator $\Delta_{v}$,
$$G_{\lambda}(z)=\frac{1}{4} \frac{\Gamma(n)}{2^{2(\nu-n)} \pi^{n+1}}\left|C_{v}(\lambda)\right|^{-2} \int_{\partial \mathbb{B}_{n}} \tilde{F}(\lambda, \omega) P_{\lambda}^{v}(z, \omega) d \lambda d \sigma(\omega)$$
corresponding to the eigenvalues $-\left(\lambda^{2}+(n-v)^{2}\right)$. \(\square\)

Remark 2.2. Notice that the continuous spectrum $\sigma_{c}\left(\Delta_{v}\right)=\left\{-\left(\lambda^{2}+(v-n)^{2}\right), \lambda \in \mathbb{R}\right\}$ of the operator $\Delta_{v}$ is understood is the sense that $z \in \sigma_{c}\left(\Delta_{v}\right)$ if and only if the rang of the operator $\left(\Delta_{v}-z I\right)$ is not closed. Thus, is not surprising that the sets $\sigma_{c}\left(\Delta_{v}\right)$ and $\sigma_{p}\left(\Delta_{v}\right)$ are not disjoint (see [21, p.30] for more general theory).

\section*{3 Spectral density}

Our aim in this section is to compute the Schwartz kernel for the spectral density of the $G$-invariant shifted Laplacian
$$\tilde{\Delta}_{v}=-\left(\Delta_{v}+(v-n)^{2}\right),$$
with $\mathcal{D}$ its maximal domain.
Note that the spectrum of the operator $\tilde{\Delta}_{v}$ can be given easily from (2.25) by
$$\sigma\left(\tilde{\Delta}_{v}\right)=\left\{s_{j}=\lambda_{j}^{2} ; j=0, \ldots,\left[\frac{v-n}{2}\right]\right\} \cup\left\{s=\lambda^{2}, \lambda \in \mathbb{R}\right\},$$
where $\lambda_{j}=-i(v-n-2 j)$. It is easy to see that the operator $\tilde{\Delta}_{v}$ considered on the minimal domain $C_{0}^{\infty}\left(\mathbb{B}_{n}\right)$ is symmetric. Then, by using Proposition 1.14 in [21, p.20], we obtain that $\tilde{\Delta}_{v}$ is essentially self-adjoint operator, and then the self-adjoint extension of $\tilde{\Delta}_{v}$ is $-\left(\Delta_{v}+(v-n)^{2}\right)$ defined on the maximal domain $\mathcal{D}$ giving in (1.5). This extension admits a spectral decomposition [21, 15, 17]
$$I=\int_{-\infty}^{+\infty} d E_{s}^{v}, \quad \tilde{\Delta}_{v}=\int_{-\infty}^{+\infty} s d E_{s}^{v}$$
Then, in the weak sense, we have
$$(f, g)=\int_{-\infty}^{+\infty} d\left(E_{s}^{v} f, g\right),\left(\tilde{\Delta}_{v} f, g\right)=\int_{-\infty}^{+\infty} s d\left(E_{s}^{v} f, g\right), \text { for } f \in C_{0}^{\infty}\left(\mathbb{B}_{n}\right) \text { and } g \in \mathrm{~L}_{v}^{2}\left(\mathbb{B}_{n}\right) .$$

The spectral density [9]
$$e_{s}^{v}:=\frac{d E_{s}^{v}}{d s}$$
is understood as an operator-valued distribution, an element of the space $\mathcal{D}^{\prime}\left(\mathbb{R}, L\left(\mathcal{D}, \mathrm{~L}_{\mathcal{V}}^{2}\left(\mathbb{B}_{n}\right)\right)\right)$, where $L\left(\mathcal{D}, \mathrm{~L}_{\mathcal{V}}^{2}\left(\mathbb{B}_{n}\right)\right)$ is the space of bounded operators from $\mathcal{D}$ to $\mathrm{L}_{v}^{2}\left(\mathbb{B}_{n}\right)$. In terms of the spectral density $e_{s}^{v}=\frac{d E_{s}^{v}}{d s}$, the two equations given in (3.3) become as follows, respectively.
$$I=<e_{s}^{v}, 1>, \tilde{\Delta}_{v}=<e_{s}^{v}, s>,$$
where $<f(s), \phi(s)>$ is the evaluation of the distribution $f(s)$ on a test function $\phi(s)$. Since $\tilde{\Delta}_{v}$ is an elliptic operator (see [10] for the general theory), then its spectral density $e_{s}^{\nu}$ admits a distributional kernel $e(s, z, w)$ [9] an element of $\mathcal{D}^{\prime}\left(\mathbb{R}, \mathcal{D}^{\prime}\left(\mathbb{B}_{n} \times\right.\right.$ $\left.\mathbb{B}_{n}\right)$ ). Precisely, we have the following proposition.
Proposition 3.1. The Schwartz kernel $e^{v}(s, w, z)$ of the spectral density $e_{s}^{v}=\frac{d E_{s}^{v}}{d s}$ is given by
$$\begin{aligned}
e^{v}(s, w, z) & =\frac{\Gamma(n)}{4 \pi^{n+1} 2^{2(v-n)}}(1-<z, w>)^{-v}\left|C_{v}(\sqrt{s})\right|^{-2}(\sqrt{s})^{-1} \chi_{+}(s) \phi_{\sqrt{s}}^{(n-1,-v)}(d(z, w)) \\
& +\sum_{j=0}^{\left[\frac{v-n}{2}\right]} c_{j} \frac{j!}{(n)_{j}}(1-<z, w>)^{-v} P_{j}^{(n-1,-v)}(\cosh (2 d(z, w))) \delta\left(s-s_{j}\right)
\end{aligned}$$
with
$$\begin{aligned}
s_{j} & =-(2 j+v-n)^{2} ; j=0, \ldots,\left[\frac{v-n}{2}\right], \\
c_{j} & =\frac{2 \Gamma(n+j)}{\pi^{n} \Gamma(n) j!} \frac{(v-n-2 j) \Gamma(v-j)}{\Gamma(v-n-j+1)},
\end{aligned}$$
$\chi_{+}(s)$ is the characteristic function of the set of positive real numbers and
$$\phi_{\lambda}^{(\alpha, \beta)}(t)={ }_{2} F_{1}\left(\frac{\alpha+\beta+1-i \lambda}{2}, \frac{\alpha+\beta+1+i \lambda}{2}, 1+\alpha ;-\sinh ^{2} t\right),$$
is the Jacobi function $([14, p .5]) . P_{j}^{(\alpha, \beta)}(x)$ denote the classical Jacobi polynomial of degree $j$ [20] and $d(z, w)$ is the distance coresponding to the Bergmann metric in the unit ball $\mathbb{B}_{n}([24, p .25])$
$$\cosh ^{2} d(z, w)=\frac{|1-<z, w>|^{2}}{\left(1-|z|^{2}\right)\left(1-|w|^{2}\right)},(z, w) \in \mathbb{B}_{n} \times \mathbb{B}_{n},$$

The function
$$C_{v}(\lambda)=\frac{2^{-v+n-i \lambda} \Gamma(n) \Gamma(i \lambda)}{\Gamma\left(\frac{i \lambda+n-v}{2}\right) \Gamma\left(\frac{i \lambda+n+v}{2}\right)},$$
is the analogous of the Harish-Chandra C-function.
For given the proof of the above proposition, we need the following Lemma
Lemma 3.1. We have the following formula
$$\int_{\partial \mathbb{B}_{n}} P_{\lambda}^{v}(z, \omega) \overline{P_{\lambda}^{v}(w, \omega)} d \sigma(\omega)=(1-<z, w>)^{-v}{ }_{2} F_{1}\left(\frac{i \lambda+n-v}{2}, \frac{-i \lambda+n-v}{2}, n ;-\sinh ^{2}(d(z, w))\right) .$$
Proof. First, we will show that the function
$$K_{\lambda}^{v}(z, w)=\int_{\partial \mathbb{B}_{n}} P_{\lambda}^{v}(z, \omega) \overline{P_{\lambda}^{v}(w, \omega)} d \sigma(\omega)$$
satisfies the following property
$$K_{\lambda}^{v}(g . z, g . w)=(C z+D)^{v} \overline{(C w+D)}^{v} K_{\lambda}^{v}(z, w) \text {, for } g=\left(\begin{array}{cc}
A & B \\
C & D
\end{array}\right) \in S U(1, n) \text {. }$$
By using the fact that
$$1-<g z, g w>=\frac{1-<z, w>}{(C z+D) \overline{(C w+D)}},$$
we can easily see that
$$P_{\lambda}^{v}(g . z, w)=P_{\lambda}^{v}\left(z, g^{-1} w\right)(C z+D)^{v}\left|C g^{-1} w+D\right|^{i \lambda+n}\left(\frac{\left|C g^{-1} w+D\right|}{\overline{C g^{-1} w+D}}\right)^{-v} .$$
Then, we get
$$\begin{aligned}
K_{\lambda}^{v}(g . z, g . w) & =\int_{\partial \mathbb{B}_{n}} P_{\lambda}^{v}(g . z, \omega) \overline{P_{\lambda}^{v}(g . w, \omega)} d \sigma(\omega) \\
& =(C z+D)^{v} \overline{(C w+D)^{v}} \int_{\partial \mathbb{B}_{n}} P_{\lambda}^{v}\left(z, g^{-1} . \omega\right) \overline{P_{\lambda}^{v}\left(w, g^{-1} \omega\right)}\left|C g^{-1} \omega+D\right|^{2 n} d \sigma(\omega) \\
& =(C z+D)^{v} \overline{(C w+D)^{v}} \int_{\partial \mathbb{B}_{n}} P_{\lambda_{j}}^{v}(z, \xi) \overline{P_{\lambda}^{v}(w, \xi)} d \sigma(\xi)
\end{aligned}$$
where we have set $\xi=g^{-1} w$ and $d \sigma(w)=|C \xi+D|^{-2 n} d \sigma(\xi)$. Thus, we get
$$K_{\lambda}^{v}(g . z, g . w)=(C z+D)^{v} \overline{(C w+D)}^{v} K_{\lambda}^{v}(z, w) .$$
Let $g_{z}$ be the following matrix
$$g_{z}=\left(\begin{array}{ll}
A & B \\
C & D
\end{array}\right):=\left(\begin{array}{cc}
\left(I_{n}-z z^{*}\right)^{-1 / 2} & z\left(1-|z|^{2}\right)^{-1 / 2} \\
z^{*}\left(I_{n}-z z^{*}\right)^{-1 / 2} & \left(1-|z|^{2}\right)^{-1 / 2}
\end{array}\right) .$$
Is not hard to show that $g_{z}$ belongs to the group $S U(1, n)$ and then by formula (2.6), we get the inverse of $g_{z}$ as follows
$$g_{z}^{-1}=\left(\begin{array}{cc}
\left(I_{n}-z z^{*}\right)^{-1 / 2} & -\left(I_{n}-z z^{*}\right)^{-1 / 2} z \\
z^{*}\left(1-|z|^{2}\right)^{-1 / 2} & \left(1-|z|^{2}\right)^{-1 / 2}
\end{array}\right) .$$
We have that the action of the matrix $g_{z}$ satisfy $g_{z} .0=z$. So, thank to this last relation combined with formula (3.19), we can write
$$\begin{aligned}
K_{\lambda}^{v}(z, w) & =K_{\lambda}^{v}\left(g_{z} \cdot 0, w\right) \\
& =K_{\lambda}^{v}\left(g_{z} \cdot 0, g_{z} g_{z}^{-1} w\right) \\
& =D^{v} \overline{\left(C g_{z}^{-1} w+D\right)^{v}} K_{\lambda}^{v}\left(0, g_{z}^{-1} \cdot w\right) .
\end{aligned}$$
Observe that
$$\begin{aligned}
1-<z, w> & =1-<g_{z} 0, g_{z} g_{z}^{-1} w> \\
& =\frac{1}{D\left(\overline{C g_{z}^{-1} w+D}\right)},
\end{aligned}$$
where we have used formula (3.16). Thus, the formula (3.22) can be rewritten as
$$K_{\lambda}^{v}(z, w)=(1-<z, w>)^{-v} K_{\lambda}^{v}\left(0, g_{z}^{-1} w\right) .$$
By setting $\xi=g_{z}^{-1} w$, the above equation becomes
$$K_{\lambda}^{v}(z, w)=(1-<z, w>)^{-v} K_{\lambda}^{v}(0, \xi) .$$
By using the formula [23]
$$\begin{aligned}
\Phi_{\lambda}(z) & =\int_{\partial \mathbb{B}_{n}} P_{\lambda}^{v}(z, \omega) d \sigma(\omega) \\
& =\left(1-|z|^{2}\right)^{\frac{-v+n-i \lambda}{2}}{ }_{2} F_{1}\left(\frac{-i \lambda+n+v}{2}, \frac{-i \lambda+n-v}{2}, n ;|z|^{2}\right) .
\end{aligned}$$

The equation (3.25) can be also rewritten as
$$\begin{aligned}
K_{\lambda}^{v}(z, w) & =(1-\langle z, w\rangle)^{-v} \int_{\partial \mathbb{B}_{n}} \overline{P_{\lambda}^{v}(\xi, \omega)} d \sigma(\omega) \\
& =(1-\langle z, w\rangle)^{-v} \Phi_{\lambda}(\xi) \\
& =\left(1-|\xi|^{2}\right) \frac{-v+n+i \lambda}{2}(1-\langle z, w\rangle)^{-v}{ }_{2} F_{1}\left(\frac{i \lambda+n+v}{2}, \frac{i \lambda+n-v}{2}, n ;|\xi|^{2}\right) .
\end{aligned}$$
Not that
$$\begin{aligned}
1-|\xi|^{2}=1-\left|g_{z}^{-1} w\right|^{2} & =\frac{1-|w|^{2}}{\left|\left(1-|z|^{2}\right)^{-1 / 2}\left(1-z^{*} w\right)\right|^{2}} \\
& =\frac{\left(1-|w|^{2}\right)\left(1-|z|^{2}\right)}{|1-\langle z, w\rangle|^{2}} .
\end{aligned}$$
Hence, by using formula (3.28), we get
$$\begin{aligned}
K_{\lambda}^{v}(z, w) & =(1-\langle z, w\rangle)^{-v}\left[\frac{\left(1-|w|^{2}\right)(1-|z|)^{2}}{|1-\langle z, w\rangle|^{2}}\right]^{\frac{i \lambda+n-v}{2}} \\
& \times{ }_{2} F_{1}\left(\frac{i \lambda+n-v}{2}, \frac{i \lambda+n+v}{2}, n ;\left|g_{z}^{-1} w\right|^{2}\right) .
\end{aligned}$$
Then, by using (3.28) and (2.46), we get
$$\begin{aligned}
K_{\lambda}^{v}(z, w) & =(1-\langle z, w\rangle)^{-v}{ }_{2} F_{1}\left(\frac{i \lambda+n-v}{2}, \frac{-i \lambda+n-v}{2}, n ; \frac{\left|g_{z}^{-1} w\right|^{2}}{\left|g_{z}^{-1} z\right|^{2}-1}\right) \\
& =(1-\langle z, w\rangle)^{-v}{ }_{2} F_{1}\left(\frac{i \lambda+n-v}{2}, \frac{-i \lambda+n-v}{2}, n ; 1-\frac{|1-\langle z, w\rangle|^{2}}{\left(1-|z|^{2}\right)\left(1-|w|^{2}\right)}\right),
\end{aligned}$$
then by (1.16), we obtain
$$\left.K_{\lambda}^{v}(z, w)=(1-\langle z, w\rangle)^{-v}{ }_{2} F_{1}\left(\frac{i \lambda+n-v}{2}, \frac{-i \lambda+n-v}{2}, n ;-\sinh ^{2}(d(z, w))\right)\right) .$$
Hence, the above equality is the desired result. \(\square\)

\section*{Proof. (of Proposition 3.1)}

Let $F \in \mathcal{C}_{0}^{\infty}\left(\mathbb{B}_{n}\right)$, then by using formula (2.17), we have
$$\begin{aligned}
F(z) & =\frac{1}{4} \frac{\Gamma(n)}{2^{2(v-n)} \pi^{n+1}} \int_{\partial \mathbb{B}_{n}} \int_{\mathbb{R}} \tilde{F}(\lambda, \omega) P_{\lambda}^{v}(z, \omega)\left|C_{v}(\lambda)\right|^{-2} d \lambda d \sigma(\omega) \\
& +\sum_{j=0}^{k} c_{j} \int_{\mathbb{B}_{n}} \tilde{F}\left(\lambda_{j}, \omega\right) P_{\lambda_{j}}^{v}(z, \omega) d \sigma(\omega) \\
& =\frac{\Gamma(n)}{4 \pi^{n+1} 2^{2(v-n)}} \int_{-\infty}^{+\infty} d \lambda\left|C_{v}(\lambda)\right|^{-2} \int_{\mathbb{B}_{n}}\left(\int_{\partial \mathbb{B}_{n}} P_{\lambda}^{v}(z, \omega) P_{-\lambda}^{v}(w, \omega) d \sigma(\omega)\right) F(w) d \mu_{v}(w) \\
& +\sum_{0}^{\left[\frac{v-n}{2}\right]} c_{j} \int_{\mathbb{B}_{n}}\left(\int_{\partial \mathbb{B}_{n}} P_{\lambda_{j}}^{v}(z, \omega) P_{-\lambda_{j}}^{v}(w, \omega) d \sigma(\omega)\right) F(w) d \mu_{v}(w)
\end{aligned}$$
Making use of formula (3.13) in where the hypergeometric function in the right hand side was replaced by the corresponding Jacobi function defined in (3.10), then we get
$$\begin{aligned}
F(z) & =\frac{\Gamma(n)}{4 \pi^{n+1} 2^{2(v-n)}} \int_{-\infty}^{+\infty}\left[\left|C_{v}(\lambda)\right|^{-2} \int_{\mathbb{B}_{n}}(1-<z, w>)^{-v}\left(\phi_{\lambda}^{(n-1,-v)}(d(z, w))\right) F(w) d \mu_{v}(w)\right] d \lambda \\
& +\sum_{0}^{\left[\frac{v-n}{2}\right]} c_{j} \int_{\mathbb{B}_{n}}(1-<z, w>)^{-v}\left(\phi_{\lambda_{j}}^{(n-1,-v)}(d(z, w))\right) F(w) d \mu_{v}(w)
\end{aligned}$$
It is not difficult to see that the function $\lambda \longmapsto \phi_{\lambda}^{(n-1,-\nu)}(d(z, w))$ is even. Then, the equation (3.33) can be rewritten as
$$\begin{aligned}
F(z) & =\frac{\Gamma(n)}{42^{2(v-n)} \pi^{n+1}} 2 \int_{0}^{+\infty} d \lambda\left|C_{v}(\lambda)\right|^{-2} \int_{\mathbb{B}_{n}}(1-<z, w>)^{-v}\left(\phi_{\lambda}^{(n-1,-v)}(d(z, w))\right) F(w) d \mu_{v}(w) \\
& +\sum_{0}^{\left[\frac{v-n}{2}\right]} c_{j} \int_{\mathbb{B}_{n}}(1-<z, w>)^{-v}\left(\phi_{\lambda_{j}}^{(n-1,-v)}(d(z, w))\right) F(w) d \mu_{v}(w)
\end{aligned}$$
Making use of the change of variable $s=\lambda^{2}$ in the first integral of (3.34) and setting $s_{j}=\lambda_{j}^{2}=-(v-n-2 j)^{2}$ in the discreet part of (3.34), we obtain
$$\begin{aligned}
F(z) & =\frac{\Gamma(n)}{4 \pi^{n+1} 2^{2(v-n)}} \int_{0}^{+\infty}\left[\left|C_{v}(\sqrt{s})\right|^{-2} s^{\frac{-1}{2}} \int_{\mathbb{B}_{n}}(1-<z, w>)^{-v}\left(\phi_{\sqrt{s}}^{(n-1,-v)}(d(z, w))\right) F(w) d \mu_{v}(w)\right] d s \\
& +\sum_{0}^{\left[\frac{v-n}{2}\right]} c_{j} \int_{\mathbb{B}_{n}}(1-<z, w>)^{-v}\left(\phi_{\sqrt{s_{j}}}^{(n-1,-v)}(d(z, w))\right) F(w) d \mu_{v}(w)
\end{aligned}$$

Using the Dirac notation
$$\int_{-\infty}^{+\infty} \delta\left(s-s_{j}\right) d s=1$$
Then, the equation (3.35) can be written in the distributional sense as follows
$$F(z)=\int_{-\infty}^{\infty} 1\left(\int_{\mathbb{B}_{n}} e(s, w, z) F(w) d \mu_{\nu}(w)\right) d s$$
where the Schwartz kernel $e^{v}(s, w, z)$ is given by
$$\begin{aligned}
e^{v}(s, w, z) & =\frac{\Gamma(n)}{4 \pi^{n+1} 2^{2(v-n)}}(1-<z, w>)^{-v} \chi_{+}(s)\left|C_{v}(\sqrt{s})\right|^{-2}(\sqrt{s})^{-1} \phi_{\sqrt{s}}^{(n-1,-v)}(d(z, w)) \\
& +\sum_{j=0}^{\left[\frac{v-n}{2}\right]} c_{j}(1-<z, w>)^{-v} \phi_{\sqrt{s_{j}}}^{(n-1,-v)}\left(d(z, w) \delta\left(s-s_{j}\right)\right.
\end{aligned}$$
Recall that $\lambda_{j}=\sqrt{s_{i}}:=-i(v-n-2 j)$ for $j=0,1, \ldots, \frac{n-v}{2}$. Then the Jacobi function $\phi_{\sqrt{s_{j}}}^{(n-1,-v)}(d(z, w))$ involved in the discreet part of the Schwartz kernel $e^{v}(s, w, z)$ becomes
$$\phi_{\sqrt{s_{j}}}^{(n-1,-v)}(d(z, w))={ }_{2} F_{1}\left(-j, j+n-v, n ;-\sinh ^{2}(d(z, w)) .\right.$$
Next, by using the identity [16, p.39]
$$P_{k}^{(\alpha, \beta)}(y)=\frac{(1+\alpha)_{k}}{k!}{ }_{2} F_{1}\left(-k, \alpha+\beta+k+1, \alpha+1 ; \frac{1-y}{2}\right),$$
for $\alpha=n-1, \beta=-v, k=j$ and $y=1+2 \sinh ^{2}(d(z, w))=\cosh 2 d(z, w)$, the equation (3.39) becomes
$$\phi_{\sqrt{s_{j}}}^{(n-1,-v)}(d(z, w))=\frac{j!}{(n)_{j}} P_{j}^{(n-1,-v)}(\cosh 2 d(z, w)) .$$
Hence, we get
$$\begin{aligned}
e^{v}(s, w, z) & =\frac{\Gamma(n)}{4 \pi^{n+1} 2^{2(v-n)}}(1-<z, w>)^{-v} \chi_{+}(s)\left|C_{v}(\sqrt{s})\right|^{-2}(\sqrt{s})^{-1} \phi_{\sqrt{s}}^{(n-1,-v)}(d(z, w)) \\
& +\sum_{j=0}^{\left[\frac{v-n}{2}\right]} c_{j} \frac{j!}{(n)_{j}}(1-<z, w>)^{-v} P_{j}^{(n-1,-v)}(\cosh (2 d(z, w))) \delta\left(s-s_{j}\right)
\end{aligned}$$
Now, by returning back to equation (3.32) and applying the operator $\tilde{\Delta}_{v}$ to its both sides with the use of the fact that the involved function in the integral is an
eigenfunction of $\tilde{\Delta}_{v}$ associated with the eigenvalues $s=\lambda^{2}, \lambda \in \mathbb{R}$. Also, we use the fact that each function given in the discrete part is an eigenfunction of $\tilde{\Delta}_{v}$ associated with the eigenvalue $s_{j}=\lambda_{j}^{2}$ for $j=0,1, \ldots,\left[\frac{v-n}{2}\right]$. Then, by following the same method as in the above computation, we get the following equality
$$\tilde{\Delta}_{v}[F](z)=\int_{-\infty}^{+\infty} s\left[\int_{\mathbb{B}_{n}} e^{v}(s, w, z) F(w) d \mu_{v}(w)\right] d s$$
Now, considering the functional $T$ which corresponds to a test function $\varphi$ the operator $\langle T, \varphi\rangle \in \mathbf{L}\left(D, L_{v}^{2}\left(\mathbb{B}_{n}\right)\right)$ defined by:
$$\begin{aligned}
& <T, \varphi>[F](z)=\int_{-\infty}^{+\infty} \varphi(s)\left[\int_{\mathbb{B}_{n}} e^{v}(s, w, z) F(w) d \mu_{v}(w)\right] d s \\
& :=\frac{\Gamma(n)}{4 \pi^{n+1} 2^{2(v-n)}} \int_{0}^{+\infty}\left|C_{v}(\sqrt{s})\right|^{-2}(\sqrt{s})^{-1} \int_{\mathbb{B}_{n}}(1-<z, w>)^{-v} \phi_{\sqrt{s}}^{(n-1,-v)}(d(z, w)) F(w) d \mu_{v}(w) \varphi(s) d s \\
& +\sum_{j=0}^{\left[\frac{v-n}{2}\right]} \varphi\left(s_{j}\right) c_{j} \frac{j!}{(n)_{j}} \int_{\mathbb{B}_{n}}(1-<z, w>)^{-v} P_{j}^{(n-1,-v)}(\cosh (2 d(z, w))) F(w) d \mu_{v}(w)
\end{aligned}$$
Notice that from the above computation, is not hard to see that the projector $P_{j}$, defined in (2.20), can be written also in the following form
$$P_{j}[F](z)=c_{j} \frac{j!}{(n)_{j}} \int_{\mathbb{B}_{n}}(1-<z, w>)^{-v} P_{j}^{(n-1,-v)}(\cosh (2 d(z, w))) F(w) d \mu_{v}(w) .$$
We observe that the discrete part of the functional $\langle T, \varphi\rangle[F]$ can be rewritten also as
$$\sum_{j=0}^{\left[\frac{v-n}{2}\right]} \varphi\left(s_{j}\right) P_{j}[F],$$
where $P_{j}$ is the orthogonal projector on the eigenspace defined in equation (2.20). Using the fact that the norm of a projector is equal to one. The norm of the discrete part satisfy the following estimate
$$\left\|\sum_{j=0}^{\left[\frac{v-n}{2}\right]} \varphi\left(s_{j}\right) P_{j}[F]\right\|_{L_{\nu}^{2}\left(\mathbb{B}_{n}\right)} \leq\|\varphi\|_{\infty}\left(1+\frac{v-n}{2}\right)\|F\|_{L_{\nu}^{2}\left(\mathbb{B}_{n}\right)},$$
with $\|\varphi\|_{\infty}=\sup _{x \in \mathbb{R}}|\varphi(x)|<\infty$.
Then, for proving that the functional $T$ is well defined, it is remain to prove that
the following integral transform
$$A_{\varphi}[F](z):=M_{n, v} \int_{0}^{+\infty}\left|C_{v}(\sqrt{s})\right|^{-2}(\sqrt{s})^{-1} \int_{\mathbb{B}_{n}}(1-<z, w>)^{-v} \phi_{\sqrt{s}}^{(n-1,-v)}(d(z, w)) F(w) d \mu_{v}(w) \varphi(s) d s$$
define a bounded operator on $L_{v}^{2}\left(\mathbb{B}_{n}\right)$, where $M_{n, v}=\frac{\Gamma(n)}{4 \pi^{n+1} 2^{2(v-n)}}$. To do so, we first consider the case $\varphi \equiv 1$. Then, thanks to equation (3.35), the function $A_{1}[F](z)$ can be rewritten as
$$\begin{aligned}
A_{1}[F](z) & =F(z)-\sum_{j=0}^{\left[\frac{v-n}{2}\right]} c_{j} \frac{j!}{(n)_{j}} \int_{\mathbb{B}_{n}}(1-<z, w>)^{-v} P_{j}^{(n-1,-v)}(\cosh (2 d(z, w))) F(w) d \mu_{v}(w) \\
& =\left[I-\sum_{j=0}^{\left[\frac{v-n}{2}\right]} P_{j}\right][F](z)
\end{aligned}$$
where $F \in C_{0}^{\infty}\left(\mathbb{B}_{n}\right)$.
Then, we have the following estimate
$$\left\|A_{1}[F]\right\|_{L_{\gamma}^{2}\left(\mathbb{B}_{n}\right)} \leq\left(2+\frac{v-n}{2}\right)\|F\|_{L_{\gamma}^{2}\left(\mathbb{B}_{n}\right)}, F \in C_{0}^{\infty}\left(\mathbb{B}_{n}\right) .$$
Now, for a test function $\varphi$, it is easy to show that
$$\left|A_{\varphi}[F](z)\right| \leq\|\varphi\|_{\infty}\left|A_{1}[F](z)\right| .$$
This last inequality combined with estimate (3.50) implies that
$$\left\|A_{\varphi}[F](z)\right\|_{L_{\nu}^{2}\left(\mathbb{B}_{n}\right)} \leq\|\varphi\|_{\infty}\left(2+\frac{v-n}{2}\right)\|F\|_{L_{\nu}^{2}\left(\mathbb{B}_{n}\right)},$$
which prove the boundedness of the operator $A_{\varphi}$.
Finally, by (3.48) and (3.52), we get
$$\|<T, \varphi>[F]\|_{L_{v}^{2}\left(\mathbb{B}_{n}\right)} \leq\|\varphi\|_{\infty}(3+v-n)\|F\|_{L_{v}^{2}\left(\mathbb{B}_{n}\right)} .$$
Furthermore, the two equations given in (3.3) become as follows, respectively:
$$<T, 1>=I,<T, s>=\tilde{\Delta}_{v} .$$
By uniqueness of the spectral density associated to a self-adjoint operator, we conclude that the functional $T$ is nothing but the spectral density of the operator $\tilde{\Delta}_{v}$. This ends the proof. \(\square\)

Remark 3.1. Note that the operator valued function
$$\begin{aligned}
& \mathbb{R} \longrightarrow\left(L_{v}^{2}\left(\mathcal{D}, B_{n}\right),\|\cdot\|_{\mathcal{L}}\right) \\
& \lambda \longmapsto E_{\lambda}^{v}
\end{aligned}$$
is locally integrable, where $\|.\|_{\mathcal{L}}$ is the classical norm on the Banach space of bounded operators from the domain $\mathcal{D}$ onto the whole space $L_{\nu}^{2}\left(B_{n}\right)$. Then by using the fact that the point spectrum
$$\sigma_{p}\left(\tilde{\Delta}_{v}\right)=\left\{s_{j}=\lambda_{j}^{2}, \quad j=0, \ldots,\left[\frac{v-n}{2}\right]\right\}$$
is the set of the discontinuity points of the vector valued function $s \longmapsto E_{s}^{v}$. Then the derivation formula $\frac{d E_{s}^{v}}{d s}$ in the distributional sense must contain the jumps $E_{s_{j}+0}^{v}-E_{s_{j}-0}^{v}$ and the Dirac distribution $\delta\left(s-s_{j}\right)$. So, is not surprising that the discrete part in the Schwartz kernel $e^{v}(s, z, w)$ involves the above Dirac distributions.

Based on the explicit formula of the spectral density $\frac{d E_{s}^{v}}{d s}$, we use the functional calculus developed by Estrada and Fuling [9] to define, for a suitable function $f: \mathbb{R} \rightarrow \mathbb{C}$, the operator function $f\left(\tilde{\Delta}_{v}\right)$ as follows
$$f\left(\tilde{\Delta}_{\nu}\right)[\varphi](z)=\int_{\mathbb{B}_{n}} \Omega_{f}(w, z) \varphi(w) d \mu_{\nu}(w)$$
where the distributional kernel $\Omega_{f}(w, z)$ is given by
$$\begin{aligned}
\Omega_{f}(w, z) & =\int_{\sigma\left(\tilde{\Delta}_{v}\right)} e^{v}(s, w, z) f(s) d s \\
& :=\frac{\Gamma(n)}{4 \pi^{n+1} 2^{2(v-n)}}(1-\langle z, w\rangle)^{-v} \int_{0}^{+\infty}\left|C_{v}(\sqrt{s})\right|^{-2}(\sqrt{s})^{-1} \phi_{\sqrt{s}}^{(n-1,-v)}(d(z, w)) f(s) d s \\
& +\sum_{j=0}^{\left[\frac{v-n}{2}\right]} c_{j} \frac{j!}{(n)_{j}}(1-\langle z, w\rangle)^{-v} P_{j}^{(n-1,-v)}(\cosh (2 d(z, w))) f\left(s_{j}\right)
\end{aligned}$$
with $C_{\nu}$ is the Harish-Chandra function defined in (3.12), $P_{j}^{(n-1,-\nu)}($.$) are the Jacobi$ polynomials [20], $\phi_{\sqrt{s}}^{(n-1,-\nu)}($.$) is the Jacobi function defined in (3.10) and$
$$\begin{aligned}
s_{j} & =-(2 j+v-n)^{2} ; j=0, \ldots,\left[\frac{v-n}{2}\right], \\
c_{j} & =\frac{2 \Gamma(n+j)}{\pi^{n} \Gamma(n) j!} \frac{(v-n-2 j) \Gamma(v-j)}{\Gamma(v-n-j+1)} .
\end{aligned}$$

\section*{4 Heat and resolvent kernels}

In this section, we solve the heat equation and we give the resolvent kernel. First, we are interested to following Cauchy problem of heat equation associated with the operator $\Delta_{v}$ on $\mathbb{B}_{n}$ :
$$\left\{\begin{array}{l}
\frac{\partial u(t, z)}{\partial t}=\Delta_{v} u(t, z), \quad(t, z) \in \mathbb{R}^{+} \times \mathbb{B}_{n}, \\
u(0, z)=\varphi(z) \in \mathcal{C}_{0}^{\infty}\left(\mathbb{B}_{n}\right) .
\end{array}\right.$$
For the above Cauchy problem, we have the following proposition.
Proposition 4.1. The solution $u(t, z)$ of the Cauchy problem (4.1) is given by the following integral formula
$$u(t, z)=\int_{\mathbb{B}_{n}} K_{v}(t, z, w) \varphi(w) d \mu_{v}(w),$$
where $K_{\nu}(t, z, w)$ is the heat kernel given as follows
$$\begin{aligned}
K_{v}(t, z, w) & =(1-\langle z, w\rangle)^{-v} \sum_{j=0}^{\left[\frac{v-n}{2}\right]} \tau_{j} e^{4 j(j+n-v) t} P_{j}^{(n-1,-v)}(\cosh 2 d(z, w)) \\
& +(1-\langle z, w\rangle)^{-v} e^{-t(v-n)^{2}} \frac{\Gamma(n)}{2 \pi^{n+1} 2^{2(v-n)}} \\
& \times \int_{0}^{+\infty} e^{-t \lambda^{2}}\left|C_{v}(\lambda)\right|^{-2}{ }_{2} F_{1}\left(\frac{n-v-i \lambda}{2}, \frac{n-v+i \lambda}{2}, n ;-\sinh ^{2}(d(z, w))\right) d \lambda
\end{aligned}$$
where $\tau_{j}=\frac{2(v-n-2 j) \Gamma(v-j)}{\pi^{n} \Gamma(v-n-j+1)}$ and $C_{v}(\lambda)$ is the Harish-Chandra function defined in (3.12).
Proof. The solution $u(t, z)$ is given by the action of the semigroup $e^{t \Delta_{v}}$ on the initial data $\varphi(z)$ as follows
$$u(t, z)=e^{t \Delta_{v}}[\varphi](z) .$$
Note that for the operators $\Delta_{v}$ and $\tilde{\Delta}_{v}=-\left(\Delta_{v}+(n-v)^{2}\right)$, we have the following semigroup relation
$$e^{t \Delta_{v}}=e^{-t(v-n)^{2}} e^{-t \tilde{\Delta}_{v}} .$$
Then, the heat kernel $k(t, z, w)$ of $\Delta_{v}$ is given by
$$K_{v}(t, z, w)=e^{-t(v-n)^{2}} \tilde{K}_{v}(t, z, w),$$
where $\tilde{K}_{v}(t, z, w)$ is the heat kernel of the operator $\tilde{\Delta}_{v}$. By using (3.57) and (3.58), we write
$$\begin{aligned}
\tilde{K}_{v}(t, z, w) & =\int_{\sigma\left(\tilde{\Delta}_{v}\right)} e_{s}^{v}(s, w, z) e^{-t s} d s \\
& =\sum_{j=0}^{\left[\frac{v-n}{2}\right]} c_{j} \frac{j!}{(n)_{j}}(1-\langle z, w\rangle)^{-v} P_{j}^{(n-1,-v)}(\cosh 2 d(z, w)) e^{-t s_{j}} \\
& +\frac{\Gamma(n)}{4 \pi^{n+1} 2^{2(v-n)}}(1-\langle z, w\rangle)^{-v} \int_{0}^{+\infty}\left|C_{v}(\sqrt{s})\right|^{-2}(\sqrt{s})^{-1} \phi_{\sqrt{s}}^{(n-1, v)}(d(z, w)) e^{-t s} d s
\end{aligned}$$
By replacing the Jacobi function $\phi_{\sqrt{s}}^{(n-1, v)}($.$) by its expression given in terms of the$ hypergeometric function defined in (3.10) with using the change of variable $s=\lambda^{2}$ $(\lambda>0)$ in the continuous part and replacing $s_{j}$ by its value $s_{j}=-(v-n-2 j)^{2}$ in the discrete part, we obtain
$$\begin{aligned}
\tilde{K}_{v}(t, z, w) & =(1-\langle z, w\rangle)^{-v} \sum_{j=0}^{\left[\frac{v-n}{2}\right]} c_{j} \frac{j!}{(n)_{j}} e^{(v-n-2 j)^{2} t} P_{j}^{(n-1,-v)}(\cosh 2 d(z, w)) \\
& +(1-\langle z, w\rangle)^{-v} \frac{\Gamma(n)}{2 \pi^{n+1} 2^{2(v-n)}} \\
& \times \int_{0}^{+\infty} e^{-t \lambda^{2}}\left|C_{v}(\lambda)\right|^{-2}{ }_{2} F_{1}\left(\frac{n-v-i \lambda}{2}, \frac{n-v+i \lambda}{2}, n ;-\sinh ^{2}(d(z, w))\right) d \lambda
\end{aligned}$$
Next, by using the above equation and (4.6), we get
$$\begin{aligned}
K_{v}(t, z, w) & =(1-\langle z, w\rangle)^{-v} \sum_{j=0}^{\left[\frac{v-n}{2}\right]} \tau_{j} e^{4 j(j+n-v) t} P_{j}^{(n-1,-v)}(\cosh (2 d(z, w)) \\
& +(1-\langle z, w\rangle)^{-v} \frac{\Gamma(n)}{2 \pi^{n+1} 2^{2(v-n)}}
\end{aligned}$$
$$\times e^{-t(v-n)^{2}} \int_{0}^{+\infty} e^{-t \lambda^{2}}\left|C_{v}(\lambda)\right|^{-2}{ }_{2} F_{1}\left(\frac{n-v-i \lambda}{2}, \frac{n-v+i \lambda}{2}, n ;-\sinh ^{2}(d(z, w))\right) d \lambda,$$
where
$$\tau_{j}=\frac{2(v-n-2 j) \Gamma(v-j)}{\pi^{n} \Gamma(v-n-j+1)} .$$ \(\square\)

Since the operator $\Delta_{v}$ is self adjoint. Then its resolvent operator
$$R\left(\xi, \Delta_{v}\right)=\left(\xi-\Delta_{v}\right)^{-1}$$
is related to the semigroup operator by the following formula
$$R\left(\xi, \Delta_{v}\right)=\int_{0}^{+\infty} e^{-t \xi} T(t) d t$$
where $T(t)$ is the heat semigroup $e^{t \Delta_{v}}$. As a direct consequence of the above proposition, we can derive the resolvent kernel of the $G$-invariant operator $\Delta_{v}$. Precisely, we have the following proposition.

Proposition 4.2. Let $\xi \in \mathbb{C}$ such that
$$\operatorname{Re}(\xi)>\omega(v, n)=p_{n}^{v}-(n-v)^{2},$$
with
$$\begin{gathered}
p_{n}^{v}=\max \left\{\left|s_{j}\right|, \quad 0 \leq j<\frac{v-n}{2}\right\}, \\
s_{j}=-(2 j+n-v)^{2} .
\end{gathered}$$
Then the resolvent operator $R\left(\xi, \Delta_{v}\right)$ is given by
$$R\left(\xi, \Delta_{v}\right)[\varphi](z)=\int_{\mathbb{B}_{n}} R_{v}(\xi ; z, w) \varphi(w) d \mu_{v}(w),$$
where the resolvent kernel $R_{\nu}(\xi, z, w)$ is given as follows
$$\begin{aligned}
R(\xi, z, w) & =(1-\langle z, w\rangle)^{-v} \sum_{j=0}^{\left[\frac{v-n}{2}\right]} \tau_{j} \frac{1}{\lambda_{j}^{2}+(v-n)^{2}+\xi} P_{j}^{(n-1,-v)}(\cosh (2 d(z, w))) \\
& +(1-\langle z, w\rangle)^{-v} \frac{\Gamma(n)}{2 \pi^{n+1} 2^{2(v-n)}} \int_{0}^{+\infty} \frac{\left|c_{v}(\lambda)\right|^{-2}}{\lambda^{2}+(v-n)^{2}+\xi} \\
& \times{ }_{2} F_{1}\left(\frac{n-v-i \lambda}{2}, \frac{n-v-i \lambda}{2}, n,-\sinh ^{2}(d(z, w))\right) d \lambda
\end{aligned}$$
where $\lambda_{j}=-i(v-n-2 j)$ for $0 \leq j<\frac{v-n}{2}, \tau_{j}=\frac{2(v-n-2 j) \Gamma(v-j)}{\pi^{n} \Gamma(v-n-j+1)}$ and $C_{v}(\lambda)$ is the Harish-Chandra function defined in (3.12).

Proof. The equation (4.5) can be rewritten as
$$e^{t \Delta_{v}}=e^{t \omega(v, n)} e^{-t\left(\tilde{\Delta}_{v}+p_{n}^{v}\right)} .$$
where $p_{n}^{v}=\max \left\{\left|S_{j}\right|, 0 \leq j<\frac{v-n}{2}\right\}$ and $\omega(v, n)=p_{n}^{v}-(v-n)^{2}$. We can easily see that the spectrum $\sigma\left(\tilde{\Delta}_{v}+p_{n}^{v}\right)$ is included in the set of positive real numbers. Then by the self-adjointness, we show that $e^{-t\left(\tilde{\Delta}_{v}+p_{n}^{v}\right)}$ is a contraction semigroup [21, p.132] for the general theory. Then, from equation (4.18), we get the following estimate
$$\left\|e^{t \Delta_{v}}\right\| \leq e^{t \omega(v, n)} .$$
This last estimate lead us to consider the the following integral
$$\int_{0}^{+\infty} e^{-t \xi} K_{v}(t, z, w) d t$$
which takes a sense for $\operatorname{Re}(\xi)>\omega(\nu, n)$ and can reduce to the following expression
$$\begin{aligned}
\int_{0}^{+\infty} e^{-t \xi} K_{v}(t, z, w) d t & =(1-\langle z, w\rangle)^{-v} \sum_{j=0}^{\left[\frac{v-n}{2}\right]} \tau_{j} \frac{1}{\xi+4 j(v-n-j)} P_{j}^{(n-1,-v)}(\cosh (2 d(z, w))) \\
& +(1-\langle z, w\rangle)^{-v} \frac{\Gamma(n)}{2 \pi^{n+1} 2^{2(v-n)}} \int_{0}^{+\infty} \frac{\left|c_{v}(\lambda)\right|^{-2}}{\xi+(v-n)^{2}+\lambda^{2}} \\
& \times{ }_{2} F_{1}\left(\frac{n-v-i \lambda}{2}, \frac{n-v-i \lambda}{2}, n,-\sinh ^{2}(d(z, w))\right) d \lambda
\end{aligned}$$
Then, by [13, p.55], we have
$$\{\xi \in \mathbb{C}, \operatorname{Re}(\xi)>\omega(v, n)\} \subset \rho\left(\Delta_{v}\right),$$
$$\begin{aligned}
R_{v}(\xi, z, w) & =(1-\langle z, w\rangle)^{-v} \sum_{j=0}^{\left[\frac{v-n}{2}\right]} \tau_{j} \frac{1}{\xi+4 j(v-n-j)} P_{j}^{(n-1,-v)}(\cosh (2 d(z, w))) \\
& +(1-\langle z, w\rangle)^{-v} \frac{\Gamma(n)}{2 \pi^{n+1} 2^{2(v-n)}} \int_{0}^{+\infty} \frac{\left|c_{v}(\lambda)\right|^{-2}}{\xi+(v-n)^{2}+\lambda^{2}} \\
& \times{ }_{2} F_{1}\left(\frac{n-v-i \lambda}{2}, \frac{n-v-i \lambda}{2}, n,-\sinh ^{2}(d(z, w))\right) d \lambda
\end{aligned}$$
Then, the above equation can be also rewritten also as follows
$$\begin{aligned}
R(\xi, z, w) & =(1-\langle z, w\rangle)^{-v} \sum_{j=0}^{\left[\frac{v-n}{2}\right]} \tau_{j} \frac{1}{\lambda_{j}^{2}+(v-n)^{2}+\xi} P_{j}^{(n-1,-v)}(\cosh (2 d(z, w))) \\
& +(1-\langle z, w\rangle)^{-v} \frac{\Gamma(n)}{2 \pi^{n+1} 2^{2(v-n)}} \int_{0}^{+\infty} \frac{\left|c_{v}(\lambda)\right|^{-2}}{\lambda^{2}+(v-n)^{2}+\xi} \\
& \times{ }_{2} F_{1}\left(\frac{n-v-i \lambda}{2}, \frac{n-v-i \lambda}{2}, n,-\sinh ^{2}(d(z, w))\right) d \lambda
\end{aligned}$$
where $\lambda_{j}=-i(v-n-2 j)$ for $0 \leq j<\frac{v-n}{2}, \tau_{j}=\frac{2(v-n-2 j) \Gamma(v-j)}{\pi^{n} \Gamma(v-n-j+1)}$ and $C_{v}(\lambda)$ is the Harish-Chandra function defined in (3.12). \(\square\)

\section*{5 Wave kernel}

Now, we consider the following Cauchy problem of wave equation with the operator $\Delta_{v}$ on $\mathbb{B}_{n}$ :
$$\left\{\begin{array}{l}
\frac{\partial^{2} u(t, z)}{\partial t^{2}}=\Delta_{v}(t, z),(t, z) \in \mathbb{R} \times \mathbb{B}_{n}, \\
u(0, z)=0, \frac{\partial u(0, z)}{\partial t}=f(z) \in C_{0}^{\infty}\left(\mathbb{B}_{n}\right) .
\end{array}\right.$$

Proposition 5.1. The solution of the Cauchy problem (5.1) is given explicitly by the following integral formula
$$u(t, z)=\int_{\mathbb{B}_{n}} W_{v}(t, z, w) \varphi(w) d \mu_{v}(w),$$
where $W_{v}(t, z, w)$ is the wave kernel given as follows
$$\begin{aligned}
& W_{v}(t, z, w)=(1-\langle z, w\rangle)^{-v} \sum_{j=0}^{\left[\frac{v-n}{2}\right]} \tau_{j} \frac{\sin (2 t \sqrt{j(v-n-j)}}{2 \sqrt{j(v-n-j)}} P_{j}^{(n-1,-v)}(\cosh 2 d(z, w)) \\
& \quad+(1-\langle z, w\rangle)^{-v} \frac{\Gamma(n)}{2 \pi^{n+1} 2^{2(v-n)}} \\
& \quad \times \int_{0}^{+\infty} \frac{\sin \left(t \sqrt{\lambda^{2}+(n-v)^{2}}\right)}{\sqrt{\lambda^{2}+(n-v)^{2}}}\left|C_{v}(\lambda)\right|^{-2}{ }_{2} F_{1}\left(\frac{n-v-i \lambda}{2}, \frac{n-v+i \lambda}{2}, n ;-\sinh ^{2}(d(z, w))\right) d \lambda
\end{aligned}$$
where $\tau_{j}=\frac{2(v-n-2 j) \Gamma(v-j)}{\pi^{n} \Gamma(v-n-j+1)}$ and $C_{v}(\lambda)$ is the Harish-Chandra function defined in (3.12).
Proof. By using formula (3.1), the operator $\Delta_{v}$ can be also rewritten as
$$\Delta_{v}=-\left(\tilde{\Delta}_{v}+(n-v)^{2}\right) .$$
Then, the above Cauchy problem becomes
$$\left\{\begin{array}{l}
\frac{\partial^{2} u(t, z)}{\partial t^{2}}+\left(\tilde{\Delta}_{v}+(n-v)^{2}\right) u(t, z), \quad(t, z) \in \mathbb{R} \times \mathbb{B}_{n}, \\
u(0, z)=0, \quad \frac{\partial u(0, t)}{\partial t}=f(z) \in C_{0}^{\infty}\left(\mathbb{B}_{n}\right) .
\end{array}\right.$$

Now, thanks to formulas (3.57) and (3.58), the solution of the above wave Cauchy problem is given by
$$u(t, z)=\int_{\mathbb{B}_{n}} W_{v}(t, z, w) \varphi(w) d \mu_{v}(w),$$
where the wave distributional kernel is given by
$$\begin{aligned}
& W_{v}(t, z, w)=\int_{\sigma\left(\tilde{\Delta}_{v}\right)} e^{v}(s, z, w) \frac{\sin \left(\sqrt{s+(n-v)^{2}}\right)}{\sqrt{s+(n-v)^{2}}} d s \\
& :=\frac{\Gamma(n)}{4 \pi^{n+1} 2^{2(v-n)}}(1-\langle z, w\rangle)^{-v} \int_{0}^{+\infty}\left|C_{v}(\sqrt{s})\right|^{-2}(\sqrt{s})^{-1} \phi_{\sqrt{s}}^{(n-1,-v)}(d(z, w)) \frac{\sin \left(\sqrt{s+(n-v)^{2}}\right)}{\sqrt{s+(n-v)^{2}}} d s \\
& +\sum_{j=0}^{\left[\frac{v-n}{2}\right]} c_{j} \frac{j!}{(n)_{j}}(1-\langle z, w\rangle)^{-v} P_{j}^{(n-1,-v)}(\cosh (2 d(z, w))) \frac{\sin \left(\sqrt{s_{j}+(n-v)^{2}}\right)}{\sqrt{s_{j}+(n-v)^{2}}}
\end{aligned}$$
By using the fact that $s_{j}=\lambda_{j}^{2}=-(v-n-2 j)^{2}$ for $j=0,1, \ldots,\left[\frac{v-n}{2}\right]$ combined with the change of variable $s=\lambda^{2}, \lambda>0$, the above wave kernel $W_{v}(t, z, w)$ becomes
$$\begin{aligned}
& W_{v}(t, z, w)=(1-\langle z, w\rangle)^{-v} \sum_{j=0}^{\left[\frac{v-n}{2}\right]} c_{j} \frac{j!}{(n)_{j}} \frac{\sin (2 t \sqrt{j(v-n-j)}}{2 \sqrt{j(v-n-j)}} P_{j}^{(n-1,-v)}(\cosh 2 d(z, w)) \\
& \quad+(1-\langle z, w\rangle)^{-v} \frac{\Gamma(n)}{2 \pi^{n+1} 2^{2(v-n)}} \\
& \quad \times \int_{0}^{+\infty} \frac{\sin \left(t \sqrt{\lambda^{2}+(n-v)^{2}}\right)}{\sqrt{\lambda^{2}+(n-v)^{2}}}\left|C_{v}(\lambda)\right|^{-2}{ }_{2} F_{1}\left(\frac{n-v-i \lambda}{2}, \frac{n-v+i \lambda}{2}, n ;-\sinh ^{2}(d(z, w))\right) d \lambda
\end{aligned}$$
Taking into account that $\tau_{j}:=c_{j} \frac{j!}{(n)_{j}}=\frac{2(v-n-2 j) \Gamma(v-j)}{\pi^{n} \Gamma(v-n-j+1)}$, we get the desired result. \(\square\)

\section*{6 Explicit formula for some generalized integrals}

In this section, we will give some generalized integrals. The fist formula will be established by comparing the integral wave kernel obtained by the use of the spectral density with the explicit wave kernel given in [12]. The second formula will be given by comparing the integral resolvent kernel obtained from the heat kernel with the Green kernel ("resolvent kernel") obtained in [11]. Theses two formulas can be considered as an addition to the table of integral formulas for the special functions.

Proposition 6.1. Let $v>n, v \in \mathbb{R} \backslash \mathbb{Z}$ and $0 \leq x<\sinh (|t|)$ for $t \in \mathbb{R}$, then we have the following integral formula
$$\begin{aligned}
& \int_{0}^{+\infty}\left|\frac{\Gamma\left(\frac{i \lambda+n-v}{2}\right) \Gamma\left(\frac{i \lambda+n+v}{2}\right)}{\sqrt{\lambda} \Gamma(i \lambda)}\right|^{2} \times{ }_{2} F_{1}\left(\frac{n-v-i \lambda}{2}, \frac{n-v+i \lambda}{2}, n ;-x\right) \sin (t \lambda) d \lambda \\
& =(-1)^{n-1} \pi \frac{\Gamma\left(n-\frac{1}{2}\right)}{\Gamma(n)}(1+x)^{\frac{v-n}{2}}\left(\frac{\sinh ^{2}(t)}{1+x}-1\right)_{+}^{-n+\frac{1}{2}} \\
& \times{ }_{2} F_{1}\left(1-n+v, 1-n-v, \frac{3}{2}-n, \frac{1}{2}-\frac{\cosh (t)}{2 \sqrt{1+x}}\right) \\
& -2^{2(v-n+1)} \frac{\pi}{\Gamma(n)} \sum_{j=0}^{\left[\frac{v-n}{2}\right]} \frac{(v-n-2 j) \Gamma(v-j)}{\Gamma(v-n-j+1)} P_{j}^{(n-1,-v)}(2 x+1) \frac{\sinh (t(2 j+n-v))}{2 j+n-v},
\end{aligned}$$
where the notation $(x)_{+}$means the positive real part of the real number $x$.
Proof. Recall that the following wave Cauchy problem $\left(W_{n}^{\alpha \beta}\right)$
$$\left(W_{n}^{\alpha \beta}\right):\left\{\begin{array}{l}
\frac{\partial^{2} u(t, z)}{\partial t^{2}}=\Delta_{\alpha \beta} u(t, z),(t, z) \in \mathbb{R} \times \mathbb{B}_{n}, \\
u(0, z)=0, \frac{\partial u(0, z)}{\partial t}=f(z) \in C_{0}^{\infty}\left(\mathbb{B}_{n}\right),
\end{array}\right.$$
have been considered in [12], where the partial differential operator
$$\Delta_{\alpha \beta}=4\left(1-|z|^{2}\right)\left\{\sum_{1 \leq i, j \leq n}\left(\delta_{i, j}-z_{i} \bar{z}_{j}\right) \frac{\partial^{2}}{\partial z_{i} \partial \bar{z}_{j}}+\alpha \sum_{j=1}^{n} z_{j} \frac{\partial}{\partial z_{j}}+\beta \sum_{j=1}^{n} \bar{z}_{j} \frac{\partial}{\partial \bar{z}_{j}}-\alpha \beta\right\}+\sigma_{\alpha \beta}^{2}$$
acts on the Hilbert space $L^{2}\left(\mathbb{B}_{n}, d \mu_{\alpha \beta}(z)\right)$, with $d \mu_{\alpha \beta}(z)=\left(1-|z|^{2}\right)^{-(\alpha+\beta+n)-1} d m(z)$, $\alpha, \beta \in \mathbb{R}, d m(z)$ is the Lebesgue measure on $\mathbb{C}^{n}$ and $\sigma_{\alpha \beta}^{2}=(\alpha+\beta+n)^{2}$. The authors have proved that the solution of the Cauchy problem $\left(W_{n}^{\alpha \beta}\right)$ is given by
$$\begin{aligned}
u(t, z) & =(2 \pi)^{-n}\left(\frac{\partial}{\sinh (t) \partial t}\right)^{n-1} \int_{\mathbb{B}_{n}} K_{1}^{\alpha \beta}(t, z, w) f(w) d \mu_{\alpha \beta}(z) \\
& =\int_{\mathbb{B}_{n}} K_{n}^{\alpha \beta}(t, z, w) f(w) d \mu_{\alpha \beta}(z) .
\end{aligned}$$
where $K_{1}^{\alpha \beta}(t, z, w)$ is the kernel given in the equation (2.2) of the reference [12] and the distributional kernel $K_{n}^{\alpha \beta}(t, z, w)$ is given by
$$K_{n}^{\alpha \beta}(t, z, w)=c_{n}(1-\overline{<z, w>})^{\alpha}(1-<z, w>)^{\beta} I_{n}^{\alpha \beta}(t, \rho(z, w)), \rho(z, w)<|t|,$$
with $\rho(z, w)$ means the Bargmann distance $d(z, w)$ defined in (1.16) and constant $c_{n}$ is given by
$$c_{n}=(-1)^{n-1} \frac{1}{2 \pi^{n}} \Gamma\left(n-\frac{1}{2}\right) .$$
The function $I_{n}^{\alpha \beta}(\rho, t)$ is defined by
$$\begin{gathered}
I_{n}^{\alpha \beta}(\rho, t)=(\cosh (\rho))^{-(n+\alpha+\beta)}\left(\frac{\cosh ^{2}(t)}{\cosh ^{2}(d(z, w))}-1\right)_{+}^{-n+\frac{1}{2}} \\
\times{ }_{2} F_{1}\left(a, b ; \frac{a+b+1}{2}, \frac{\cosh (d(z, w))-\cosh (t)}{2 \cosh (d(z, w))}\right),
\end{gathered}$$
with $a=1-n+\alpha-\beta$ and $b=1-n+\beta-\alpha$. Note that for $\alpha=0$ and $\beta=-\nu$, the wave kernel for the Cauchy problem $W_{n}^{0,-v}$ is given by
$$\begin{aligned}
K_{n}^{0,-v}(t, z, w) & =\frac{(-1)^{n-1} \Gamma\left(n-\frac{1}{2}\right)}{2 \pi^{n}}(1-<z, w>)^{-v}(\cosh (d(z, w)))^{v-n}\left(\frac{\cosh ^{2}(t)}{\cosh ^{2}(d(z, w))}-1\right)_{+}^{-n+\frac{1}{2}} \\
& \times{ }_{2} F_{1}\left(1-n+v, 1-n-v ; \frac{3}{2}-n, \frac{\cosh (d(z, w))-\cosh (t)}{2 \cosh (d(z, w))}\right.
\end{aligned}$$
Furthermore, the Cauchy problem $W_{n}^{0,-v}$ can be also rewritten as
$$\left\{\begin{array}{l}
\frac{\partial^{2} u(t, z)}{\partial t^{2}}+\tilde{\Delta}_{v} u(t, z)=0,(t, z) \in \mathbb{R} \times \mathbb{B}_{n}, \\
u(0, z)=0, \frac{\partial u(0, z)}{\partial t}=f(z) \in C_{0}^{\infty}\left(\mathbb{B}_{n}\right),
\end{array}\right.$$
where $\tilde{\Delta}_{v}$ is the operator defined in (1.17). Then, by using formulas (3.47) and (3.48), the solution of the above wave Cauchy problem is given by
$$\begin{aligned}
u(t, z) & =\frac{\sin \left(t \sqrt{\tilde{\Delta}_{v}}\right)}{\sqrt{\tilde{\Delta}_{v}}}[f](z) \\
& =\int_{\mathbb{B}^{n}} W_{n}^{0,-v}(t, z, w) f(w) d \mu_{v}(w),
\end{aligned}$$
where the distributional wave kernel $W_{n}^{0,-v}(t, z, w)$ is given by
$$\begin{aligned}
W_{n}^{0,-v}(t, z, w) & =\int_{\sigma\left(\tilde{\Delta}_{\nu}\right)} e^{v}(s, w, z) \frac{\sin (t \sqrt{s})}{\sqrt{s}} d s \\
& :=(1-<z, w>)^{-\nu} \sum_{j=0}^{\left[\frac{v-n}{2}\right]} c_{j} \frac{j!}{(n)_{j}} P_{j}^{(n-1,-v)}(\cosh (2 d(z, w))) \frac{\sin \left(t \sqrt{s_{j}}\right)}{\sqrt{s_{j}}} \\
& +\frac{\Gamma(n)}{4 \pi^{n+1} 2^{2(v-n)}}(1-<z, w>)^{-v} \int_{0}^{+\infty}\left|C_{\nu}(\sqrt{s})\right|^{-2}(\sqrt{s})^{-1} \phi_{\sqrt{s}}^{(n-1,-v)}(d(z, w)) \frac{\sin (t \sqrt{s})}{\sqrt{s}} d s
\end{aligned}$$
Then, by using the change of variable $s=\lambda^{2},(\lambda \geq 0)$, and the fact that $\sqrt{s_{j}}=\lambda_{j}=i(2 j+n-v)$ for $j=0,1, \ldots,\left[\frac{v-n}{2}\right]$ combined the well known formula
$$\sin (i x)=i \sinh (x), x \in \mathbb{R} .$$
The equation (6.10) becomes
$$\begin{aligned}
W_{n}^{0,-v}(t, z, w) & =(1-<z, w>)^{-v} \sum_{j=0}^{\left[\frac{v-n}{2}\right]} c_{j} \frac{j!}{(n)_{j}} P_{j}^{(n-1,-v)}(\cosh ((2 d(z, w)))) \frac{\sinh (t(2 j+n-v))}{2 j+n-v} \\
& +\frac{\Gamma(n)}{2 \pi^{n+1} 2^{2(v-n)}}(1-<z, w>)^{-v} \\
& \times \int_{0}^{+\infty}\left|C_{v}(\lambda)\right|^{-2} \frac{\sin (t \lambda)}{\lambda}{ }_{2} F_{1}\left(\frac{n-v-i \lambda}{2}, \frac{n-v+i \lambda}{2}, n ;-\sinh ^{2}(d(z, w))\right) d \lambda
\end{aligned}$$
Now, by using the uniqueness of the wave kernel for the Cauchy problem $W_{n}^{0,-v}$, we get the following equality
$$W_{n}^{0,-v}(t, z, w)=K_{n}^{0,-v}(t, z, w) .$$
This last equation lead us to write
$$\begin{aligned}
& \frac{\Gamma(n)}{2 \pi^{n+1} 2^{2(v-n)}} \int_{0}^{+\infty}\left|C_{v}(\lambda)\right|^{-2} \frac{\sin (t \lambda)}{\lambda}{ }_{2} F_{1}\left(\frac{n-v-i \lambda}{2}, \frac{n-v+i \lambda}{2}, n ;-\sinh ^{2}(d(z, w))\right) d \lambda \\
& =\frac{(-1)^{n-1} \Gamma\left(n-\frac{1}{2}\right)}{2 \pi^{n}}(\cosh (d(z, w)))^{v-n}\left(\frac{\cosh ^{2}(t)}{\cosh ^{2}(d(z, w))}-1\right)_{+}^{-n+\frac{1}{2}} \\
& \times{ }_{2} F_{1}\left(1-n+v, 1-n-v ; \frac{3}{2}-n, \frac{\cosh (d(z, w))-\cosh (t)}{2 \cosh (d(z, w))}\right) \\
& -\sum_{j=0}^{\left[\frac{v-n}{2}\right]} c_{j} \frac{j!}{(n)_{j}} P_{j}^{(n-1,-v)}(\cosh ((2 d(z, w)))) \frac{\sinh (t(2 j+n-v))}{2 j+n-v} .
\end{aligned}$$

Now, setting $x=\sinh ^{2}(d(z, w))$ then $\cosh ((2 d(z, w)))=2 x+1$. The last condition in equation (6.4) require that $0 \leq x<\sinh (|t|)$. So, by replacing the Harish-Chandra function $C_{\nu}(\lambda)$ by its expression given in (3.12), we get the desired formula. \(\square\)

Proposition 6.2. Let $v>n, v \in \mathbb{R} \backslash \mathbb{Z}$ and $\mu$ is a complex number such that $\mu \neq$ $-i(2 \ell+n \pm v)$ for $\ell=0,1,2, \ldots$ and $\operatorname{Re}\left(\mu^{2}\right)<-P_{n}^{v}$, with $p_{n}^{v}=\max \left\{\left|s_{j}\right|, 0 \leq j<\frac{v-n}{2}\right\}$ and $s_{j}=-(2 j+n-v)^{2}$. Then, we have the following integral formula
$$\begin{aligned}
& \int_{0}^{+\infty}\left|\frac{\Gamma\left(\frac{i \lambda+n-v}{2}\right) \Gamma\left(\frac{i \lambda+n+v}{2}\right)}{\Gamma(i \lambda)}\right|^{2} \frac{1}{\lambda^{2}-\mu^{2}} \times{ }_{2} F_{1}\left(\frac{n-v-i \lambda}{2}, \frac{n-v+i \lambda}{2}, n,-x\right) d \lambda \\
& =\pi 2^{2(v-n)} \frac{\Gamma\left(\frac{n-i \mu+v}{2}\right) \Gamma\left(\frac{n-i \mu-v}{2}\right)}{\Gamma(n) \Gamma(1-i \mu)}(1+x)^{\frac{v+i \mu}{4}-\frac{n}{2}} \\
& \times{ }_{2} F_{1}\left(\frac{n-i \mu+v}{2}, \frac{n-i \mu-v}{2}, 1-i \mu, \frac{1}{1+x}\right) \\
& -\frac{4 \pi}{\Gamma(n)} 2^{2(v-n)} \sum_{j=0}^{\left[\frac{v-n}{2}\right]} \frac{(v-n-2 j) \Gamma(v-j)}{\Gamma(v-n-j+1)} \frac{1}{\lambda_{j}^{2}-\mu^{2}} P_{j}^{(n-1,-v)}(2 x+1) .
\end{aligned}$$
Proof. First, let us consider the following partial differential operator
$$H_{\frac{v}{2}, 1}=-4\left(1-|z|^{2}\right)\left[\sum_{1 \leq i, j \leq n}\left(\delta_{i j}-z_{i} \bar{z}_{j}\right) \frac{\partial^{2}}{\partial z_{i} \partial \bar{z}_{j}}+\frac{v}{2} \sum_{j=1}^{n}\left(z_{j} \frac{\partial}{\partial z_{j}}-\overline{z_{j}} \frac{\partial}{\partial \bar{z}_{j}}\right)\right]+v^{2}|z|^{2}$$
acting on the Hilbert space $L^{2}\left(\mathbb{B}_{n},\left(1-|z|^{2}\right)^{-n-1} d m(z)\right)$. The above operator represents the operator $H_{B, \rho}$ defined in [11], for $B=\frac{v}{2}$ and $\rho=1$. The authors in [11] have computed the Green kernel $R_{\frac{v}{2}, 1}(\mu, z, w)$, which have called abusively the resolvent kernel. They have introduce the kernel $R_{\frac{v}{2}, 1}(\mu, z, w)$ as the right inverse [5] of the operators
$$\left[H_{\frac{v}{2}, 1}-h_{\frac{v}{2}, 1}(\mu)\right], h_{\frac{v}{2}, 1}(\mu)=\mu^{2}+v^{2}+n^{2} .$$
Precisely, that is the integral operator
$$R_{\frac{v}{2}, 1}[F](z):=\int_{\mathbb{B}_{n}} R_{\frac{v}{2}, 1}(\mu, z, w) F(w)\left(1-|w|^{2}\right)^{-n-1} d m(w)$$
acting on $L^{2}\left(\mathbb{B}_{n},\left(1-|z|^{2}\right)^{-n-1} d m(z)\right)$, which solves the partial differential equations
$$\left[H_{\frac{v}{2}, 1}-h_{\frac{v}{2}, 1}(\mu)\right] g=F, \text { for } F \in L^{2}\left(\mathbb{B}_{n},\left(1-|z|^{2}\right)^{-n-1} d m(z)\right) .$$

Based on [11], the explicit expression of the kernel $R_{\frac{v}{2}, 1}(\mu, z, w)$ is given by the following formula
$$\begin{aligned}
R_{\frac{v}{2}, 1}(\mu, z, w) & =C_{\frac{v}{2}, 1}^{n}(\mu)\left(\frac{1-\overline{\langle z, w\rangle}}{1-\langle z, w\rangle}\right)^{\frac{v}{2}}\left(\frac{\left(1-|z|^{2}\right)\left(1-|w|^{2}\right)}{|1-\langle z, w\rangle|^{2}}\right)^{n-i \frac{\mu}{2}} \\
& \times{ }_{2} F_{1}\left(\frac{n-i \mu+v}{2}, \frac{n-i \mu-v}{2}, 1-i \mu, \frac{\left(1-|z|^{2}\right)\left(1-|w|^{2}\right)}{|1-\langle z, w\rangle|^{2}}\right),
\end{aligned}$$
with the constant $C_{\frac{v}{2}, 1}^{n}(\mu)$ is given by
$$C_{\frac{v}{2}, 1}^{n}(\mu)=\frac{1}{2 \pi^{n}} \frac{\Gamma\left(\frac{n-i \mu+v}{2}\right) \Gamma\left(\frac{n-i \mu-v}{2}\right)}{\Gamma(1-i \mu)},$$
and the parameter $\mu$ must satisfy the following condition
$$\mu \neq-i(2 \ell+n \pm v), \quad \ell=0,1,2, \ldots .$$
Now, by using Lemma (2.1) for $\alpha=0, \beta=-\nu$ and $\gamma=\frac{-\nu}{2}$, we obtain the following formula
$$\Delta_{v}=\left(1-|z|^{2}\right)^{\frac{-v}{2}}\left(\Delta_{\frac{v}{2}, \frac{-v}{2}}+2 v\left(n-\frac{v}{2}\right) I\right)\left(1-|z|^{2}\right)^{\frac{v}{2}} .$$
Note that the operator $H_{\frac{v}{2}, 1}$ can be also rewritten as
$$H_{\frac{v}{2}, 1}=-\Delta_{\frac{v}{2}, \frac{-v}{2}}+v^{2} I,$$
then the equation (6.23) becomes
$$\Delta_{v}=\left(1-|z|^{2}\right)^{\frac{-v}{2}}\left(-H_{\frac{v}{2}, 1}+2 n v I\right)\left(1-|z|^{2}\right)^{\frac{v}{2}}$$
which is equivalent to
$$\left(1-|z|^{2}\right)^{\frac{v}{2}}\left(-\Delta_{v}+2 n v I\right)\left(1-|z|^{2}\right)^{\frac{-v}{2}}=H_{\frac{v}{2}, 1} .$$
Using this above formula and returning back to equation (6.19), so this last equation becomes equivalent to the following equation
$$\left[\left(2 n v-h_{\frac{v}{2}, 1}(\mu)\right) I-\Delta_{v}\right]\left(1-|z|^{2}\right)^{\frac{-v}{2}} g=\left(1-|z|^{2}\right)^{\frac{-v}{2}} F .$$
Now, by setting $\xi=\xi(\mu):=2 n v-h_{\frac{v}{2}, 1}(\mu)$ in Proposition (4.1) under the condition
$$\operatorname{Re}(\xi(\mu))>\omega(v, n),$$
where $\omega(v, n)$ is the constant defined in (4.13), the equation (6.27) becomes equivalent to
$$g(z)=\int_{\mathbb{B}_{n}}\left(1-|z|^{2}\right)^{\frac{v}{2}} R(\xi(\mu), z, w)\left(1-|w|^{2}\right)^{\frac{-v}{2}} F(w)\left(1-|w|^{2}\right)^{v-n-1} d m(w),$$
where $R(\xi(\mu), z, w)$ is the resolvent kernel given by the following formula
$$\begin{aligned}
R(\xi(\mu), z, w) & =(1-\langle z, w\rangle)^{-v} \sum_{j=0}^{\left[\frac{v-n}{2}\right]} \frac{\tau_{j}}{\lambda_{j}^{2}-\mu^{2}} P_{j}^{(n-1,-v)}(\cosh (2 d(z, w))) \\
& +(1-\langle z, w\rangle)^{-v} \frac{\Gamma(n)}{2 \pi^{n+1} 2^{2(v-n)}} \\
& \times \int_{0}^{+\infty} \frac{\left|c_{v}(\lambda)\right|^{-2}}{\lambda^{2}-\mu^{2}} \times{ }_{2} F_{1}\left(\frac{n-v-i \lambda}{2}, \frac{n-v+i \lambda}{2}, n,-\sinh ^{2}(d(z, w))\right) d \lambda
\end{aligned}$$
where $\tau_{j}=\frac{2(v-n-2 j) \Gamma(v-j)}{\pi^{n} \Gamma(v-n-j+1)}$ and $\lambda_{j}^{2}=-(v-n-2 j)^{2}$.
Now, returning back to equation (6.19) and requiring that the parameter $\mu$ satisfy the both conditions
$$\mu \neq-i(2 \ell+n \pm v), \text { for } \ell=0,1,2, \ldots \text { and } \operatorname{Re}(\xi(\mu))>\omega(v, n) .$$
Then the equation (6.19) becomes equivalent to
$$g(z)=R_{\frac{v}{2}, 1}[F](z)=\int_{\mathbb{B}_{n}} R_{\frac{v}{2}}(\mu, z, w) F(w)\left(1-|w|^{2}\right)^{-n-1} d m(w) .$$
Moreover, the right inverse of the operator $\left[H_{\frac{v}{2}, 1}-h_{\frac{v}{2}, 1}(\mu)\right]$, in the sense of [5], becomes its inverse. Then by the consideration of equations (6.29) and (6.32), we get the following relation
$$R_{\frac{v}{2}, 1}=\left(1-|z|^{2}\right)^{\frac{v}{2}} R(\xi(\mu), z, w)\left(1-|w|^{2}\right)^{\frac{v}{2}},$$
for $\mu \neq-i(2 \ell+n \pm v)$ and $\operatorname{Re}(\xi(\mu))>\omega(v, n)$. Notice that this last condition is equivalent to
$$\operatorname{Re}\left(\mu^{2}\right)<-P_{n}^{v},$$
where $P_{n}^{v}$ is the parameter defined in equation (4.14). Then, the equation (6.33) is true for the parameter $\mu$ in the domain
$$D_{n, v}=\left\{\mu=u+i v, u^{2}-v^{2}<-P_{n}^{v} \text { and } \mu \neq-i(2 \ell+n \pm v) \text { for } \ell=0,1,2, \ldots\right\} .$$

By returning back to formula (6.33) and using equations (6.20) with (6.30), we obtain for $\mu \in D_{n, v}$ the following relation
$$\begin{aligned}
& (1-\langle z, w\rangle)^{-v} \sum_{j=0}^{\left[\frac{v-n}{2}\right]} \frac{\tau_{j}}{\lambda_{j}^{2}-\mu^{2}} P_{j}^{(n-1,-v)}(\cosh (2 d(z, w))) \\
& +(1-\langle z, w\rangle)^{-v} \frac{\Gamma(n)}{2 \pi^{n+1} 2^{2(v-n)}} \\
& \times \int_{0}^{+\infty} \frac{\left|c_{v}(\lambda)\right|^{-2}}{\lambda^{2}-\mu^{2}} \times{ }_{2} F_{1}\left(\frac{n-v-i \lambda}{2}, \frac{n-v+i \lambda}{2}, n,-\sinh ^{2}(d(z, w))\right) d \lambda \\
& =\left(1-|z|^{2}\right)^{\frac{-v}{2}}\left(1-|w|^{2}\right)^{\frac{-v}{2}} C_{\frac{v}{2}, 1}^{n}(\mu)\left(\frac{1-\langle z, w\rangle}{1-\langle z, w\rangle}\right)^{\frac{v}{2}}\left(\frac{\left(1-|z|^{2}\right)\left(1-|w|^{2}\right)}{|1-\langle z, w\rangle|^{2}}\right)^{n-i \frac{\mu}{2}} \\
& \times{ }_{2} F_{1}\left(\frac{n-i \mu+v}{2}, \frac{n-i \mu-v}{2}, 1-i \mu, \frac{\left(1-|z|^{2}\right)\left(1-|w|^{2}\right)}{|1-\langle z, w\rangle|^{2}}\right)
\end{aligned}$$
Is not hard to show that the right hand side of the above equation can be rewritten as
$$\begin{aligned}
& (1-\langle z, w\rangle)^{-v} C_{\frac{v}{2}, 1}^{n}(\mu)\left(\frac{\left(1-|z|^{2}\right)\left(1-|w|^{2}\right)}{|1-\langle z, w\rangle|^{2}}\right)^{n-\frac{v}{2}-i \frac{\mu}{2}} \\
& \times{ }_{2} F_{1}\left(\frac{n-i \mu+v}{2}, \frac{n-i \mu-v}{2}, 1-i \mu, \frac{\left(1-|z|^{2}\right)\left(1-|w|^{2}\right)}{|1-\langle z, w\rangle|^{2}}\right) .
\end{aligned}$$
By setting $x=\sinh ^{2}(d(z, w))$, then $\cosh (d(z, w))=(1+x)^{\frac{1}{2}}$ and $\cosh (2 d(z, w))=$ $2 x+1$. Finally, by replacing the right hand side of equation (6.36) by the last expression given in (6.37) and the Harish-Chandra $c_{\nu}(\lambda)$ by its expression given in (3.12) combined with the fact that $\cosh ^{2}(d(z, w))=\frac{\left.|1-<z, w\rangle\right|^{2}}{\left(1-|z|^{2}\right)\left(1-|w|^{2}\right)}$, the equation (6.36) becomes as follows
$$\begin{aligned}
& \int_{0}^{+\infty}\left|\frac{\Gamma\left(\frac{i \lambda+n-v}{2}\right) \Gamma\left(\frac{i \lambda+n+v}{2}\right)}{\Gamma(i \lambda)}\right|^{2} \frac{1}{\lambda^{2}-\mu^{2}} \times{ }_{2} F_{1}\left(\frac{n-v-i \lambda}{2}, \frac{n-v+i \lambda}{2}, n,-x\right) d \lambda \\
& =\pi 2^{2(v-n)} \frac{\Gamma\left(\frac{n-i \mu+v}{2}\right) \Gamma\left(\frac{n-i \mu-v}{2}\right)}{\Gamma(n) \Gamma(1-i \mu)}(1+x)^{\frac{v+i \mu}{4}-\frac{n}{2}} \\
& \times{ }_{2} F_{1}\left(\frac{n-i \mu+v}{2}, \frac{n-i \mu-v}{2}, 1-i \mu, \frac{1}{1+x}\right) \\
& -\frac{4 \pi}{\Gamma(n)} 2^{2(v-n)} \sum_{j=0}^{\left[\frac{v-n}{2}\right]} \frac{(v-n-2 j) \Gamma(v-j)}{\Gamma(v-n-j+1)} \frac{1}{\lambda_{j}^{2}-\mu^{2}} P_{j}^{(n-1,-v)}(2 x+1),
\end{aligned}$$
which is the desired formula. \(\square\)

\section*{References}
[1] J.B. Ahern, Patrick and C. Cascante, $H p$-theory for generalized m-harmonic functions in the unit ball, Indiana University Mathematics Journal, 45(1996), 103-135.
[2] P. Ahern and J. Floris, Maximal and area integral characterizations of hardysobolev spaces in the unit ball of $\mathbb{C}^{n}$, Revista matemática iberoamericana, 4(1988), 123-153.
[3] N. Askour, Phase deformed magnetic berezin transforms on $\mathbb{C}^{n}$ : A formula representing phase deformed magnetic berezin transforms as functions of the magnetic laplacian on $\mathbb{C}^{n}$, arXiv preprint arXiv:1210.7734, 2012.
[4] N. Askour and Z. Mouayn, Resolvent kernel for the kohn laplacian on heisenberg groups, Electronic Journal of Differential Equations, 2002(2002), 15.
[5] R. Beals, Exact fundamental solutions, Journées Équations aux dérivées partielles, (1998).
[6] A. Boussejra and A. Intissar, $L^{2}$-concrete spectral analysis of the invariant Laplacian $\Delta_{\alpha \beta}$ in the unit complex ball $B_{n}$, Journal of functional analysis, 160(1998), 115-140.
[7] J.G. Christensen, K. Gröchenig and G. Ólafsson, New atomic decompositons for bergman spaces on the unit ball, arXiv preprint arXiv:1504.00381, (2015).
[8] J. Elstrodt, Die Resolvente zum eigenwertproblem der automorphen formen in der hyperbolischen ebene: Teil I, Mathematische Annalen, 203(1973), 295-330.
[9] R. Estrada and S.A. Fulling, Distributional asymptotic expansions of spectral functions and of the associated Green kernels, Electronic Journal of Differential Equations, 1999(1999), 1-17.
[10] J. Folland, B. Gerald and S. Thangavelu, Lectures on partial differential equations, Berlin, 1983.
[11] A. Ghanmi and A. Intissar, Asymptotic of complex hyperbolic geometry and 12-spectral analysis of landau-like hamiltonians, Journal of Mathematical Physics, 46(2005), 032-107.
\begin{itemize}
\item[] [12] A. Intissar and M.V. Ould Moustapha, Explicit formulae for the wave kernels for the laplacians in the bergman ball, Annals of Global Analysis and Geometry, 15(1997), 221-234.
\item[] [13] R. Nagel and K.J. Engel, One-Parameter semigroups for linear evolution equations, New York, 2000.
\item[] [14] T.H. Koornwinder, Jacobi functions and analysis on noncompact semisimple Lie groups "Special functions": group theoretical aspects and applications, Dordrecht, 1984.
\item[] [15] H. Leinfelder, A geometric proof of the spectral theorem for unbounded self-adjoint operators, Mathematische Annalen, 242(1979), 85-96.
\item[] [16] W. Magnus, F. Oberhettinger and R.P. Soni, Formulas and theorems for the special functions of mathematical Physics, Springer Science and Business Media, 1966.
\item[] [17] V. Moretti, Spectral theory and quantum mechanics, London, 2013.
\item[] [18] Z. Mouhcine, Spectral density on the quaternionic Heisenberg group and a Green kernel for fractional powers of its Casimir-Laplacian, Electronic Journal of Differential Equations, 2017(2017), 1-12.
\item[] [19] M. Paulsen, Vern I.; Raghupathi, An Introduction to the theory of reproducing kernel Hilbert spaces, Cambridge University, 2016.
\item[] [20] R. Beals, Special functions and orthogonal polynomials, Cambridge University, 2016.
\item[] [21] K. Schmüdgen, Unbounded self-Adjoint operators on Hilbert space, Springer Science and Business Media, 2012.
\item[] [22] V. Volchkov, Harmonic analysis of mean periodic functions on symmetric spaces and the Heisenberg group, Springer Science and Business Media, 2009.
\item[] [23] G. Zhang, A weighted Plancherel formula II: The case of the ball, Studia Math, 102(1992), 103-120.
\item[] [24] K. Zhu, Spaces of holomorphic functions in the unit ball, Springer Science and Business Media, 2005.
\end{itemize}
