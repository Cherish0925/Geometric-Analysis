# A negative-eigenvalue balance for harmonic self-dual Weyl curvature

23 September 2026.

## 1. Result

Let \((M,g)\) be a closed connected oriented smooth four-manifold with
\(\delta W^+=0\). Order the eigenvalues of the self-dual Weyl endomorphism as
\(\lambda_1<\lambda_2\le\lambda_3\). The lowest eigenvalue is assumed
simple everywhere. Set
\[
 t=-\frac34\lambda_1>0,\qquad h=\lambda_3-\lambda_2\ge0,
 \qquad z=\frac{h}{4t}<1.                                      \tag{1}
\]
The symbol \(h\) denotes a scalar splitting, not a metric. Work on the
orientation double cover of the lowest eigenline if necessary, and choose
its smooth self-dual eigenform \(\omega\) with \(|\omega|^2=2\). All
energies below descend to \(M\); using normalized integrals does not change
them under this cover.

Put
\[
 u=t^{1/3},\quad u_0=2^{-1/3},\quad \widehat g=u^2g,
 \quad\Omega=u^2\omega,
\]
\[
 Q_X=\nabla_X\omega-d\log u\wedge\iota_X\omega
                      +X^\flat\wedge\iota_{\nabla\log u}\omega,
 \qquad P=d\omega+2d\log u\wedge\omega.                       \tag{2}
\]
Thus \(\widehat\nabla\Omega=u^2Q\) and \(d\Omega=u^2P\).

**Theorem 1 (exact balance).** The following identities hold:
\[
 \boxed{\int_M\frac32\frac{1-z^2}{1+z^2}\,t^{2/3}|Q|^2
       =\frac32\int_Mt^{-1/3}h^2,}                            \tag{3}
\]
\[
 \boxed{|P|^2=\frac{z^2}{1+z^2}|Q|^2.}                       \tag{4}
\]
No derivative budget or bound on \(W^-\) is assumed.

**Theorem 2 (scalar restoring estimate).** Suppose, for fixed constants,
\[
                   t\ge m>0,\qquad z\le\theta<1.
\tag{5}
\]
Then
\[
\boxed{\begin{split}
 \fint_M\big[&|du|^2+|\nabla\omega|^2
               +u(u^3-u_0^3)(u-u_0)\big]\\
 &\le C_{m,\theta}\fint_M\big[h^2+(s+4)^2\big].
\end{split}}                                                 \tag{6}
\]
In particular, the left side controls \(\fint(u-u_0)^2\).
If additionally \(t\le M_0\), then
\[
 \boxed{\fint_M\big[|dt|^2+(t-\tfrac12)^2+|\nabla\omega|^2\big]
 \le C_{m,M_0,\theta}\fint_M\big[h^2+(s+4)^2\big].}            \tag{7}
\]
These are estimates for an eigenform supplied by the actual curvature,
not a hypothetical auxiliary form. There is no Sobolev constant,
injectivity-radius bound, scalar spectral gap, second-order input,
or full-curvature bound. Formula (6) also requires no upper bound on
\(t\). The harmonic-Weyl condition is a genuine equation hypothesis;
small Ricci error alone does not imply it.

For \(\operatorname{Ric}=-g\), the scalar term vanishes. Compared with the
previous variable-amplitude estimate
\(C(d+\sqrt{dH_2})\), (7) removes \(H_2\) and gives a linear bound in
\(d=\fint h^2/2\), in this exact harmonic-Weyl setting.

## 2. Signed conformal normalization

The derivation uses the weighted harmonic-Weyl identities underlying
Catino--Dameno, equations (2.8), (2.9), and (3.1)--(3.9), but with the
lowest negative eigenvalue rather than the largest positive one. The sign
changes the rigidity identity into an energy balance. We give the algebra
and the sign step explicitly.

In \(\widehat g\), the chosen eigenvalue is
\(\alpha=-4u/3\). Define the signed weight
\[
                 F=-\frac3{4u},\qquad F\alpha=1.
\]
Conformal covariance gives \(\delta_{\widehat g}(u^{-1}
W^+_{\widehat g})=0\). Multiplication by the constant \(-3/4\) gives
\(\delta_{\widehat g}(FW^+_{\widehat g})=0\).
Although a conformal factor must be positive, \(F\) here is a signed
tensor weight, not the conformal factor. Every equation in the next
display is linear in that weight, so its negative sign is legitimate:
\[
 0=\widehat\nabla^*\widehat\nabla(FW)
       +\frac{\widehat s}{2}FW-6FW^2+2F|W|^2I.               \tag{8}
\]
This is the standard bundle-valued Weitzenböck identity for the
divergence-free self-dual tensor \(FW\); here and in this section
\(W=W^+_{\widehat g}\).

Let
\[
 \rho=\lambda_2/\lambda_1=-\tfrac12+\tfrac32z,
 \qquad k=\frac{1-\rho}{2+\rho}=\frac{1-z}{1+z}.
\tag{9}
\]
On the open dense set where the other two eigenvalues have locally
constant multiplicities, extend \(\Omega=\Omega_1\) to an oriented
orthogonal eigenframe of \(\Lambda^+\), each of norm \(\sqrt2\), and write
\[
 \widehat\nabla\Omega_1=a\otimes\Omega_2-c\otimes\Omega_3,
 \quad\widehat\nabla\Omega_2=-a\otimes\Omega_1+b\otimes\Omega_3.
\]
The eigenvalues of \(FW\) are \(1,\rho,-1-\rho\). The first row of
its divergence equation, since the first eigenvalue is constant, gives
\[
 (1-\rho)\iota_{a^\sharp}\Omega_3
       +(2+\rho)\iota_{c^\sharp}\Omega_2=0.                  \tag{10}
\]
In a compatible orthonormal coframe this says
\(c=k(-a_2,a_1,-a_4,a_3)\). Consequently,
\[
\begin{split}
 |d\Omega|^2&=(1-k)^2|a|^2,\\
 |\widehat\nabla\Omega|^2&=2(1+k^2)|a|^2,\\
 W(\widehat\nabla_e\Omega,\widehat\nabla^e\Omega)
       &=2\alpha[\rho-(1+\rho)k^2]|a|^2.
\end{split}                                                   \tag{11}
\]
These formulas only use the signed normalized eigenvalues and (10).
In particular they do not require \(\alpha>0\).

Contract (8) with \(\Omega\otimes\Omega\), use
\(FW(\Omega)=\Omega\), \(|\Omega|^2=2\), and
\(\Delta_H\Omega=\widehat\nabla^*\widehat\nabla\Omega
-2W\Omega+\widehat s\Omega/3\). This gives
\[
\begin{split}
0={}&\tfrac12|\widehat\nabla\Omega|^2
-\tfrac2\alpha W(\widehat\nabla_e\Omega,
                         \widehat\nabla^e\Omega)\\
&+\tfrac32\langle\Omega,\Delta_H\Omega\rangle
+2\left(\frac{2|W|^2}{\alpha}-3\alpha\right).
\end{split}                                                   \tag{12}
\]
On a closed four-manifold, self-duality gives
\(\int\langle\Omega,\Delta_H\Omega\rangle=2\int|d\Omega|^2\).
Also \(|W|^2=2\alpha^2(1+\rho+\rho^2)\). Equations (11)--(12)
therefore give
\[
 \int_{\widehat g}\left[
 \frac{3(1-\rho)(2+\rho)}{2\rho^2+2\rho+5}
           |\widehat\nabla\Omega|^2
       +8\alpha(\rho+\tfrac12)^2\right]=0.                 \tag{13}
\]
The first coefficient equals \(\tfrac32(1-z^2)/(1+z^2)\).
The second term is negative, since \(\alpha=-4u/3\).
Using \(d\mu_{\widehat g}=u^4d\mu_g\), (13) is exactly (3).
Taking the ratio of the first two identities in (11) gives (4).

The calculations extend across the collision set \(\lambda_2=\lambda_3\)
by continuity: the lowest eigenline is smooth, and \(z^2\), all
coefficients in (3)--(4), and both energy densities are smooth there.
No differentiation of the possibly nonsmooth ordered splitting \(h\)
is used.

## 3. Scalar restoration with no upper amplitude bound

Write \(e=s+4\). Since the model
\[
 A=t(2I/3-\omega\otimes\omega)
\]
has the exact lowest eigenvalue and eigenline of \(W^+\), the residual
\(R=W^+-A\) satisfies \(R\omega=0\) and \(|R|^2=h^2/2\).
The conformal scalar and Weyl formulas are
\[
 \widehat s=u^{-3}(6\Delta u+su),\qquad
 \langle\widehat W^+\Omega,\Omega\rangle=-\tfrac83u,
\]
where \(\Delta=d^*d\ge0\). Testing the self-dual form Weitzenböck
formula against \(f\Omega\), with \(f=(u-u_0)/u\), gives
\[
\begin{split}
6\int|du|^2+8\int V(u)+\int e\,u(u-u_0)
={}&\int f u^2(3|P|^2-\tfrac32|Q|^2)\\
&+3u_0\int\langle du\wedge\omega,P\rangle,\qquad
 V(u)=u(u^3-u_0^3)(u-u_0).
\end{split}                                                   \tag{14}
\]
This is the arbitrary constant-norm form identity used in the previous
variable-amplitude proof; closedness or integrability is not imposed.

Here \(V(u)\ge m^{1/3}u_0^2(u-u_0)^2\). By (3) and (5),
\[
 \int u^2|Q|^2\le
       \frac{1+\theta^2}{1-\theta^2}\,m^{-1/3}\int h^2,
 \qquad
 \int |Q|^2\le
       \frac{1+\theta^2}{1-\theta^2}\,m^{-1}\int h^2.
\tag{15}
\]
Since \(|f|\le 1+u_0m^{-1/3}\) and \(|P|^2\le|Q|^2\), the first
term on the right of (14) is bounded by \(C_m\int u^2|Q|^2\).
The second is at most \(3\int|du|^2+C\int|Q|^2\).
For the scalar error observe the uniform identity and bound
\[
 \frac{u^2(u-u_0)^2}{V(u)}
 =\frac{u}{u^2+uu_0+u_0^2}\le\frac1{3u_0},
\]
with its continuous interpretation at \(u=u_0\). Young's inequality
then bounds its absolute value by \(4\int V(u)+C\int e^2\).
Absorption in (14) proves the \(du\) and \(V(u)\) parts of (6).
The conformal connection formula gives
\(|\nabla\omega|^2\le C(|Q|^2+m^{-2/3}|du|^2)\), completing (6).
If \(t\le M_0\), then
\(|dt|^2=9u^4|du|^2\) and
\((t-1/2)^2\le C_{m,M_0}V(u)\), proving (7).

## 4. What this proves about negative Einstein geometry

If \(\operatorname{Ric}=-g\), \(t\) is bounded between two positive
constants, and the upper eigenvalues approach one another in normalized
\(L^2\), (7) controls both the amplitude and the derivative of the
actual eigenform. No separate derivative estimate is needed. For example,
uniform spectral closeness to \((-2/3,1/3,1/3)\) of size \(\epsilon\)
implies all three normalized integral quantities in (7) are
\(O(\epsilon^2)\), with uniform constants for sufficiently small
\(\epsilon\).

At zero splitting and \(s=-4\), the theorem gives
\(t=1/2\) and \(\nabla\omega=0\), hence a constant-negative-scalar
Kähler metric on the double cover. It is Kähler--Einstein when
\(\operatorname{Ric}=-g\). This exact degenerate-spectrum conclusion
belongs to classical Derdziński theory; it is not claimed as a new
classification.

Small positive splitting is **not** proved to vanish. The signed balance
has two nonnegative energies on opposite sides, rather than two on the
same side of a zero identity. In particular, reversing the eigenvalue
ordering in a positive-branch rigidity theorem is not valid.
The formal reaction in the Einstein Weyl equation reinforces this
distinction. At \(W_0=\operatorname{diag}(-2/3,1/3,1/3)\),
the splitting direction \(B=\operatorname{diag}(0,b,-b)\) has
\[
 D\left[-2W-6W^2+2|W|^2I\right]_{W_0}(B)=-6B.
\]
Thus the zero-order linearization does not give a positive-mass
absorption argument for the splitting. This is a check on that proposed
proof, not a counterexample to a possible uniform exact rigidity theorem.
Neither this note nor the inspected sources decide whether every
sufficiently small two-sided spectral neighborhood is exactly Kähler.

## 5. Sources, scope, and verification

The signed algebra adapts Catino--Dameno's first-order method; the scalar
restoring test is the prior variable-amplitude argument. Their positive
largest-eigenvalue theorem does not cover this negative-lowest branch.
Kim's condition \(\lambda_2\le\lambda_3/4\) also excludes the negative
Kähler--Einstein model, whose upper eigenvalues coincide and are positive.
These distinctions are mathematical hypotheses, not novelty claims.

- A. Derdziński, *Self-dual Kähler manifolds and Einstein manifolds of
  dimension four*, Compositio Math. 49 (1983), 405--433, Proposition 5.
  [Primary paper](https://www.numdam.org/article/CM_1983__49_3_405_0.pdf).
- G. Catino and D. Dameno, *Conformal Kähler Rigidity of Einstein
  Four-Manifolds*, arXiv:2607.21538v1, Sections 2--3.
  [Primary manuscript](https://arxiv.org/html/2607.21538v1).
- I. Kim, *Pinched self-dual Weyl curvature on Einstein four-manifolds*,
  arXiv:2512.00825v1, Theorem 7.
  [Primary manuscript](https://arxiv.org/html/2512.00825v1).
- [Prior variable-amplitude scalar test](line1_variable_negative_selection.md),
  Sections 2--3; its \(H_2\)-dependent weak-Bianchi estimate is replaced
  here by (3), not silently assumed.

`check_line1_signed_harmonic_weyl.py` checks the signed normalization,
spectral coefficients, conformal powers, scalar restoring algebra, and
reaction linearization by exact symbolic arithmetic. It also rejects
three deliberate sign or normalization errors. These finite checks
support the displayed identities; the global theorem relies on the
written differential and integration argument above.
