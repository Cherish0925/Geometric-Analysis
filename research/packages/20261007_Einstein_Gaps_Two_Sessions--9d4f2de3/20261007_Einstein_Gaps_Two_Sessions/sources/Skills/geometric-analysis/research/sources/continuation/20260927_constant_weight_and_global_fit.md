# Constant-weight calibration and the cost of extending actual cores

27 September 2026. Continuation of `e58b867` under the
[unified research directive](../guidance/source/20260927_unified_research_directive.zh.md).
The actual supply, curvature norms and orientations are those of
[I07](../mathematics/current/line1_functional_pencil.md),
[I40](20260927_mixed_current_and_signed_cores.md), and
[I41](20260927_conformal_separation_and_zero_end.md).

The first result replaces the variable-weight endpoint field by **any**
constant-weight actual solution after a controlled conformal reduction.
An exact nonnegative identity controls its amplitude, harmonic-curvature
remainder and Maxwell residual, uniformly in the parameter. Keeping its
two error scales separate improves the all-metric compactified gap from
cubic to quadratic at the zero-Weyl end, and strengthens the upper energy
wall on the same actual topological inputs. The subsequent
calculations test the actual high-index cores against the missing global
matching, and retain the curvature-action cancellation in the balanced
first-order problem. Neither O10 nor the balanced optimal coefficient is
settled here.

## 1. The weak endpoint can be studied at constant scalar curvature

Let the fixed Spin-c structure be solvable for every metric in the conformal
class of a closed oriented four-metric \(g\), with
\(p=(a_g^+)^2>0\). As in I07, put

\[
 S_2=\int s^2,\quad P=\int|\operatorname{Ric}^{\circ}|^2,
 \quad w=\sqrt6|W^+|,\quad
 D_\beta=(1+\beta^{-1})S_2+(\beta+1)\int w^2-72\pi^2p,
\]
\[
 r=V^{-1}\int|\operatorname{Ric}+g|^2,\qquad
 \kappa=r+D_\beta/V,\qquad \beta\ge2.
 \tag{1.1}
\]

The conformal class has negative Yamabe constant: a nonnegative constant
scalar representative would contradict the positive actual monopole
projection by the spinor Weitzenbock formula. Let \(\widehat g\) be its
scalar-minus-four representative. Hodge star on two-forms, \(p\), and the
integrated Weyl energies are conformally invariant. The exact identities
proved in I41 Section 1 give

\[
 \delta=S_2-\widehat S_2\ge0,\qquad
 \widehat P=P-\delta/12,\qquad
 \widehat D_\beta=D_\beta-(1+\beta^{-1})\delta\ge0.
 \tag{1.2}
\]

Thus \(0\le\delta\le D_\beta\). If \(e=s+4\), then
\(\int e^2\le4rV\) and
\(S_2=16V-8\int e+\int e^2\). Since
\(\widehat S_2=16\widehat V\),

\[
 1-\sqrt r-\kappa/16
 \le\frac{\widehat V}{V}
 \le1+\sqrt r+r/4.
 \tag{1.3}
\]

In particular, when the left denominator is positive,

\[
 \boxed{\widehat\kappa
 =\frac{\widehat P+\widehat D_\beta}{\widehat V}
 \le\frac{\kappa}{1-\sqrt\kappa-\kappa/16}.}
 \tag{1.4}
\]

An actual sequence with \(\beta\to\infty\), \(\kappa\to0\) therefore
exists if and only if such a sequence exists with \(s=-4\). The same
class, its square condition, and \(\chi/A\) are retained;
\(\widehat V/V\to1\). There is no pointwise Ricci or conformal-factor
regularity claim. This is an endpoint consequence of the inherited exact
conformal identities, not a new Yamabe existence theorem.

We will also need a comparison independent of \(D_\beta\). Write
\(g=u^2\widehat g\), with \(\Delta=d^*d\) on \(\widehat g\).
The scalar transformation gives
\(e u^2=6u^{-1}\Delta u+4(u^2-1)\). Expand its square and integrate.
The cross term is \(48\int(u-u^{-1})\Delta u
=48\int(1+u^{-2})|du|^2\). Subtract the exact formula for \(\delta\)
in I41 Section 1 to obtain

\[
 \boxed{\int_g(s_g+4)^2=\delta
 +16\int_{\widehat g}(u^2-1)^2+48\int_{\widehat g}|du|^2.}
 \tag{1.5}
\]

In particular \(\delta\le4rV\). Moreover,

\[
16\widehat V=16V-8\int_g e+\left(\int_g e^2-\delta\right)
\ge16V(1-\sqrt r),\qquad e=s_g+4.
\tag{1.6}
\]

Thus \(\widehat V/V\ge1-\sqrt r\), whether or not
\(D_\beta/V\) is small. This is an energy comparison, not a bound
on the Hessian of the conformal factor in a uniformly controlled chart.

## 2. An exact constant-weight calibration for every finite parameter

Work now with \(s=-4\). Take **any** actual solution

\[
 D_A\Phi=0,\qquad F_A^+=2i\sigma(\Phi).
 \tag{2.1}
\]

It exists by scaling an ordinary unperturbed solution: if its spinor is
\(\Psi\), take \(\Phi=\Psi/\sqrt2\). No continuity, uniqueness, or
comparison with the earlier variable-weight solutions is used. The maximum
principle gives \(0\le\rho=|\Phi|^2\le2\). Set

\[
 \psi=2\sqrt2\sigma(\Phi),\qquad
 \zeta=\langle\Phi,\nabla_A\Phi\rangle,
 \quad J=\|F_A^+-(F_A^+)_H\|_2^2\ge0,
\]
\[
 E_\lambda=\langle W^+\psi,\psi\rangle+w\rho^2/3\ge0,
\]
\[
 D_0=2\int|d\rho|^2+
 \int(4\rho|\nabla_A\Phi|^2-|\nabla\psi|^2)
       +2\int|d\psi|^2+2\int E_\lambda\ge0.
 \tag{2.2}
\]

For \(\beta\ge2\), define

\[
 c=\frac{4(\beta+1)}{3\beta}\in[4/3,2],\qquad
 z=w-4/\beta,\qquad
 C_\beta(\rho)=\rho+c/2-\frac{(\rho+c)^2}{2c(\beta+1)}.
 \tag{2.3}
\]

**Theorem (same-solution constant-weight identity).**

\[
\boxed{\begin{aligned}
 \frac{c}{18}D_\beta={}&\frac12D_0+cJ
       +\int(\rho-c)^2 C_\beta(\rho)\\
 &+\frac{c(\beta+1)}{18}
       \int\left[z-\frac{3(\rho^2-c^2)}{c(\beta+1)}\right]^2.
\end{aligned}}
 \tag{2.4}
\]

Every term on the right is nonnegative. In particular,

\[
 \boxed{D_0\le\frac29D_\beta,\quad
 J\le\frac1{18}D_\beta,\quad
 \int(\rho-c)^2\le\frac16D_\beta.}
 \tag{2.5}
\]

**Proof.** The actual spinor/form identities in I07, with weight exactly
two, read

\[
 D_0=\frac23\int(4+w)\rho^2-2\int\rho^3.
 \tag{2.6}
\]

Since \(|F_A^+|^2=\rho^2/2\), Hodge projection gives

\[
 9\int\rho^2
 =16(1+\beta^{-1})V+(\beta+1)\int w^2-D_\beta+18J.
 \tag{2.7}
\]

Insert (2.7) into (2.6), use (2.3), and expand the cubic around \(c\).
Before completing the last square, the result is

\[
 \frac12D_0+cJ+\int(\rho-c)^2(\rho+c/2)
  +\frac{c(\beta+1)}{18}\int z^2
 =\frac c{18}D_\beta+\frac13\int z(\rho-c)(\rho+c).
 \tag{2.8}
\]

Completing the \(z\) square gives (2.4). Further,
\(C_\beta(0)=2/3\), and

\[
 C_\beta'(\rho)
 =\frac{\beta(4\beta+4-3\rho)}{4(\beta+1)^2}>0
 \quad (0\le\rho\le2).
\]

Thus \(C_\beta\ge2/3\). Dropping terms gives (2.5), using \(c\le2\).
This proof never changes the actual solution. QED.

There is an equivalent full Weyl-square identity. Define the globally
smooth polynomial model

\[
 \alpha=\frac{9\beta}{8(\beta+1)^2},\qquad
 W_0=\alpha(\rho^2 I/3-\psi\otimes\psi).
\]

Its two repeated eigenvalues are \(\alpha\rho^2/3\). Direct expansion
in the three-dimensional self-dual bundle gives

\[
 |W^+-W_0|^2=(w-2\alpha\rho^2)^2/6+2\alpha E_\lambda.
\]

The square in (2.4) is exactly \((w-2\alpha\rho^2)^2\).
Using (2.9) below cancels the \(E_\lambda\) term and yields

\[
 \boxed{\frac{D_\beta}{18}=J+\frac4c\int|\zeta|^2
 +\frac{\beta+1}{3}\int|W^+-W_0|^2
 +\frac1c\int C_\beta(\rho)(\rho-c)^2.}
 \tag{2.9a}
\]

At \(\beta=2\), rescaling back to the ordinary spinor gives precisely
the four-term identity in I47 Section 4.1. The extension here is the
same-solution identity for the whole finite parameter range, not a new
claim about the already established beta-two case. It requires only
the actual solution (2.1) on the scalar-minus-four metric; conformal
solvability was used to reach and supply that representative in Section 1.

### 2.1. A first-order Maxwell estimate without a spectral gap

The exact Hopf/Dirac identities used in I47 Section 4.1 are

\[
 d\rho=2\operatorname{Re}\zeta,\quad
 |\nabla\psi|^2=4\rho|\nabla_A\Phi|^2
                       -4|\operatorname{Im}\zeta|^2,
 \quad |d\psi|^2=2|\operatorname{Im}\zeta|^2.
\]

Consequently

\[
 D_0=8\int|\zeta|^2+2\int E_\lambda.
 \tag{2.9}
\]

The determinant Bianchi identity is \(dF_A=0\), and
\(F_A^+=i\psi/\sqrt2\). In the project's Clifford convention,
\(\delta F_A=-2i\operatorname{Im}\zeta\). Its norm, independently of
the sign convention, therefore obeys

\[
 \boxed{\|\delta F_A\|_2^2
 =4\|\operatorname{Im}\zeta\|_2^2
 \le D_0/2\le D_\beta/9.}
 \tag{2.10}
\]

Let \(H_A\) be the harmonic representative of the same imaginary curvature
class. The exact form \(F_A-H_A\) has zero square integral, so its two
chiral squared norms are equal. Hence

\[
 \boxed{\|F_A-H_A\|_2^2=2J\le D_\beta/9,\qquad
 d(F_A-H_A)=0,\qquad
 \|\delta(F_A-H_A)\|_2^2\le D_\beta/9.}
 \tag{2.11}
\]

In fact the sum is bounded by the same constant:
\(\|F_A-H_A\|_2^2+\|\delta(F_A-H_A)\|_2^2\le D_\beta/9\).
Indeed (2.4) gives
\(\|\delta F_A\|_2^2+(c/2)\|F_A-H_A\|_2^2\le cD_\beta/18\),
and \(c/2\le1\).

This is a Hodge graph-norm bound. It is not a rough covariant
\(W^{1,2}\) bound on two-forms: the latter introduces the uncontrolled
opposite Weyl curvature in the Weitzenbock formula. Nor does (2.11)
bound \(d\delta F_A\) in \(L^2\). Spectrally, coefficients of size
\(\lambda^{-1}\) at eigenvalue \(\lambda\to\infty\) have vanishing
graph norm but a nonvanishing Laplacian. Such a spectral illustration is
not an actual counterexample to the coupled equations.

By (2.5), \(\rho\to4/3\) in normalized \(L^2\) at squared error
\(O(D_\beta/V+\beta^{-2})\). With
\(\omega=(3\sqrt2/4)\psi\),

\[
 \|\omega\|_\infty\le3\sqrt2/2,\qquad
 \fint\left[(|\omega|^2-2)^2+|d\omega|^2\right]
       \le C(D_\beta/V+\beta^{-2}).
 \tag{2.12}
\]

Thus the unrestricted actual endpoint can be attacked using a scalar-minus-four
metric and a constant-weight solution with small Maxwell residual. All
original supplier quantifiers remain in force; only the analytic field
chosen for the proof has changed. No bound on \(\nabla w\) or derivative
of an auxiliary weight is needed.

### 2.2. Continuing the Maxwell equation to the critical source

The current has \(\operatorname{Re}\zeta=d\rho/2\). Hence, in the
same convention as (2.10),
\(d\zeta=-d\delta F_A/2\). Since \(dF_A=0\), the actual torsion
curvature relation of I40 Section 3 becomes the global polynomial identity

\[
 \boxed{\rho^2\Delta_H F_A^-+\rho^3F_A^-
                  =-2q_-(t)+\mathcal R,}
 \tag{2.13}
\]
\[
 |\mathcal R|\le C\left(\rho^3|\operatorname{Ric}^{\circ}|
                 +\rho^{3/2}|\zeta||\nabla_A\Phi|\right).
\]

Hodge Laplacian commutes with chirality. On \(\{\rho>0\}\) this is
\((\Delta_H+\rho)F_A^-=-2q_-(t)/\rho^2+\mathcal R/\rho^2\).
The source has no singular norm bound there: the exact pointwise
\(|t|^2\le2\rho^2|\nabla_A\Phi|^2\) and
\(|\zeta|\le\sqrt\rho|\nabla_A\Phi|\) bound its magnitude by
\(C(\rho|\operatorname{Ric}^{\circ}|+|\nabla_A\Phi|^2)\).
But its squared norm involves the critical fourth-power gradient energy.
The available budget bounds that quantity, not its concentration by a
small multiple of \(V\). Division by \(\rho\) across the zero set is
not needed or asserted in (2.13).

There is also a precise remaining term in a covariant-regularity attempt.
For the real ASD form \(a_-=-iF_A^-\),

\[
 \|\nabla a_-\|_2^2=2\|da_-\|_2^2+
       \frac43\|a_-\|_2^2+2\int\langle W^-a_-,a_-\rangle.
 \tag{2.14}
\]

Even if \(a_-=K+E\), with a bounded fitted model \(K\),
\(\|E\|_2^2=o(V)\), and \(\|W^-\|_2^2\le C(B)V\), only the
\(K,K\) and \(K,E\) terms are controlled by these norms. The remaining
\(\int\langle W^-E,E\rangle\) requires information not supplied by
two separate \(L^2\) bounds. Thus (2.13) is a concrete new way to use
the full equations, not a regularity or zero-end-gap conclusion.

The natural signed pairing can be taken further. Along a hypothetical
zero-end sequence assume \(a^2\ge T_+\), put
\(\eta=r+D_\beta/V+\beta^{-2}\le1\), and use normalized norms below.
Set \(\rho_*=4/3\), \(U_*=-4/3\), \(m_*=128/81\),
\(\Pi=\nabla_A\Phi\), \(\tau=t_\Phi\), \(m=|\tau|^2\), and
\(S=m_*+2\rho^2|\Pi|^2\). The constant-weight identities give

\[
\Delta\rho=-2|\Pi|^2-(-4+2\rho)\rho/2,\qquad
0\le\nu:=2\rho^2|\Pi|^2-m\le4\rho|\zeta|^2.
\]

The estimates above and the inherited Hessian estimate imply
\(\|\rho-\rho_*\|_2+\|\zeta\|_2+\|d\rho\|_2
+\|\operatorname{Ric}^{\circ}\|_2\le C\sqrt\eta\), with
\(\Pi,\tau\) bounded in normalized \(L^4\) and
\(\nabla_A\Pi,\nabla\tau\) bounded in normalized \(L^2\).
Thus \(\fint S=2m_*+O(\sqrt\eta)\), \(\fint S^2\le C\),
and \(\fint\nu=O(\eta)\). The scalar test \(2\rho^2/S\) has derivative

\[
d(2\rho^2/S)=\frac{4m_*\rho}{S^2}d\rho
 -\frac{8\rho^4}{S^2}\operatorname{Re}\langle\Pi,\nabla_A\Pi\rangle.
\]

It is bounded in normalized \(L^2\), so this test gives
\(\fint S^{-1}=(2m_*)^{-1}+O(\sqrt\eta)\). The same nonnegative
reciprocal defect as in [I40, Section 8](20260927_mixed_current_and_signed_cores.md)
then yields \(\fint m^2/S=m_*/2+O(\sqrt\eta)\) and
\(\fint(m/S)^2=1/4+O(\sqrt\eta)\).

Write real ASD forms \(f=-iF_A^-\), \(Q=-iq_-(\tau)\),
\(R=-i\mathcal R\), and \(B=\rho^3Q/S\). Pairing the actual curvature
equation with \(Q/S\), whose weighted derivative test is bounded by
I40 (8.10), gives
\(\fint\langle f,B\rangle=-m_*/8+O(\sqrt\eta)\) and
\(\fint|B|^2=\rho_*^6/32+O(\sqrt\eta)\).
Chern--Weil supplies

\[
 \fint|f|^2+\frac{4\pi^2(a^2-T_+)}V
 =\fint\rho^2/2-2\fint|W^+|^2-2/3+r/2
 =2/9+O(\sqrt\eta).
\]

Completing the square, exactly as in I41 Section 6, proves

\[
 K=-\frac{4m_*}{\rho_*^6}B,\qquad \|K\|_\infty\le C,\qquad
 \|f-K\|_2^2+\frac{4\pi^2(a^2-T_+)}V\le C\sqrt\eta.
 \tag{2.14a}
\]

All denominators are bounded below by \(m_*\); this transfers the
bounded ASD fit to this same constant-weight solution without identifying
it with an earlier weighted solution.

Let \(\gamma=\operatorname{Im}\zeta\). Since
\(\delta f=-\gamma\), \(df=*\gamma\), integration by parts in
(2.13) gives the exact identity

\[
\begin{aligned}
 \int\rho^3|f|^2+2\int\langle Q,f\rangle+2\int\rho^2|\gamma|^2
 ={}&\int\langle R,f\rangle\\
 &-4\int\rho\langle\gamma,\iota_{\nabla\rho}f\rangle.
\end{aligned}
 \tag{2.14b}
\]

The right side is \(O(\eta^{1/4}V)\). Indeed R is bounded in normalized
\(L^2\) and has \(L^1\) norm \(O(\sqrt\eta)\); the ASD form
\(\rho(d\rho\wedge\gamma)^-\) is similarly \(L^2\)-bounded and
\(L^1\)-small. Pair their bounded-model parts with K and their remaining
parts with \(f-K\) using (2.14a). Testing instead against the harmonic
\(h=-i(H_A)^-\) gives the same formula with the test factor f replaced
everywhere by h, without the nonnegative \(\gamma^2\) term. Its error
is also small by (2.11).

This closes the error in these signed tests, but their principal terms
balance: \(\fint\rho^3|f|^2\to128/243\), whereas
\(2\fint\langle Q,f\rangle\to-128/243\). It is not a contradiction.
Testing instead with \(\Delta_H f\) leaves
\(4\int\langle\gamma,\delta Q\rangle\) and
\(\int\langle R,\Delta_H f\rangle\).
The estimate \(|\delta Q|\le C|\tau||\nabla\tau|\) gives only a
critical bounded contribution, not a vanishing one. This identifies the
unpaid derivative coupling rather than assigning a false positive sign
to (2.14b).

### 2.3. An anisotropic all-metric gap

The improved Weyl-fit coefficient in (2.9a) changes the parameter estimate;
it should not be discarded by replacing every error with \(r+D_\beta/V\).

**Theorem.** Under the actual conformal supplier of Section 1, with
\(b_a=(-a^2)_+/V\), there is a universal \(c_0>0\) such that

\[
 \boxed{(1+b_a)\left(r+\frac{D_\beta}{\beta V}\right)
       \ge c_0\frac{(\beta-2)^2}{\beta^4},\qquad \beta\ge2.}
 \tag{2.15}
\]

If \(a^2\ge T_+=2\chi+3\tau\), the factor \(1+b_a\) can be
removed. No pointwise curvature, Euler-density, diameter, noncollapse,
Sobolev, or stationarity bound is assumed.

**Proof on a scalar-minus-four metric.** Put
\(t=1/\beta\), \(d=D_\beta/V\), \(\varepsilon=r+td\), and
\(\omega=\sqrt2\psi/c\), \(v=|\omega|^2\). Then

\[
 W_0=t(vI/3-\omega\otimes\omega),\quad
 \fint|W^+-W_0|^2\le Ctd,
\]
\[
 \|\omega\|_\infty\le C,\qquad
 \fint\bigl((v-2)^2+|dv|^2+|d\omega|^2\bigr)\le Cd.
 \tag{2.16}
\]

Here the endomorphism model has coefficient \(t\), not \(t/2\).
All bounds follow from the same solution in (2.9a). Its coarse Hessian
budget is \(C(1+r+d+b_a)V\): the positive-spinor curvature uses only
\(W^+\), scalar curvature, Ricci and the determinant curvature;
\(\int|F_A^-|^2\le2V+4\pi^2(-a^2)_+\), while the scalar equation
bounds \(\int|\nabla_A\Phi|^2\le CV\). More precisely,
\(\nabla_A^*\nabla_A\Phi=(1-\rho/2)\Phi\), and
\(\int|\nabla_A^*\nabla_A\Phi|^2\le8V/27\).
Apply the bounded-section Hessian identity and interpolation exactly as
in I07 Section 5; no derivative estimate for \(F_A\) is needed.
No opposite Weyl or derivative-of-weight term enters this estimate.

Let \(J_t=\operatorname{div}W(W_0)\), where \(W(\cdot)\) is the
usual passage from the self-dual endomorphism to its curvature tensor,
and \(X=\fint|J_t|^2\). The derivative of this polynomial has its
explicit factor \(t\), so
\(\fint|\nabla J_t|^2\le Ct^2(1+r+d+b_a)\).
The weak Bianchi self-test therefore gives

\[
 X\le Ct\sqrt{(r+td)(1+r+d+b_a)}.
 \tag{2.17}
\]

For completeness, the exact polynomial/Hodge contraction from
[round 21, Section 6, equation (17)](../mathematics/current/round21_analytic.md)
on this form is

\[
\begin{split}
 X=t^2\fint\bigl[&\tfrac43v^2-\tfrac43t v^3
 +2v\langle(W^+-W_0)\omega,\omega\rangle
 +4v|d\omega|^2-\tfrac56|dv|^2\\
 &+4\langle\iota_{\nabla v}\omega,*d\omega\rangle\bigr].
\end{split}
 \tag{2.18}
\]

Its constant-amplitude part is \((16/3)t^2(1-2t)\).
The amplitude, Weyl, and derivative errors in (2.18) are bounded,
respectively, by \(Ct^2\sqrt d\), \(Ct^2\sqrt{td}\), and
\(Ct^2d\). Thus

\[
 t^2(1-2t)\le CX+Ct^2(\sqrt d+d+\sqrt{td}).
 \tag{2.19}
\]

If \(r,d\le1\), divide by \(t>0\), insert (2.17), and use
\(t\sqrt d\le\sqrt{td}\), \(td\le\sqrt{td}\), and
\(t\sqrt{td}\le\sqrt{td}\). This proves
\(t(1-2t)\le C\sqrt{(1+b_a)(r+td)}\).
If \(r>1\) or \(d>1\), its squared conclusion follows directly from
\(r+td\ge\min(1,t)\). This proves (2.15) on the representative.

**Transfer to every input metric.** For \(r\le1/16\), (1.5) implies
\(\widehat V/V\ge1-\sqrt r\ge3/4\), and

\[
 \widehat r+t\widehat d
 =\frac{P+tD_\beta-(1/12+t+t^2)\delta}{\widehat V}
 \le2(r+td),\qquad
 1+\widehat b_a\le2(1+b_a).
\]

Apply the just-proved estimate to \(\widehat g\). For \(r>1/16\)
the desired bound is immediate after reducing \(c_0\). Finally,
\(a^2\ge T_+\) and Chern--Weil imply
\(b_a\le r/(8\pi^2)\); the small/large \(r\) split removes the
factor. QED.

This proves a stronger estimate than the inherited compactified transfer,
although its right side still tends to zero. For an exact normalized
negative Einstein metric it gives
\(D_\beta/V\ge c_0(\beta-2)^2/\beta^3\) after square-cost removal.
It does not give a positive lower bound independent of \(\beta\).

### 2.4. The upper energy wall now has a quadratic endpoint margin

Use the compactified functional \(P_t=tD_{1/t}\), extended at zero by
\(P_0=6\int|W^+|^2\). Equation (2.15) says

\[
 \boxed{(1+b_a)(r+P_t/V)\ge c_0t^2(1-2t)^2,
                    \qquad 0\le t\le1/2.}
 \tag{2.20}
\]

The prior exponent was three. This improvement is for integral Ricci
error, not only the bounded-pointwise-Ricci setting of I45.

Suppose, as in the inherited upper-wall application, that every metric
admits the specified actual selection with
\(p\ge A>0\), \(a^2\ge T_+\), and
\(T_+=A(1-h)\), \(1/4<h<1/3\). Define

\[
 e=\frac{\int|\operatorname{Ric}|^2}{8\pi^2A},\quad
 G(h)=\frac{(4+\sqrt{1-3h})^2}{9},\quad
 t_* =\frac{1-2\sqrt{1-3h}}{8+2\sqrt{1-3h}}.
\]

Then every smooth metric satisfies

\[
 \boxed{\mathcal E(g)+(G(h)-e)_+
                    \ge c_* t_*^2(1-2t_*)^2.}
 \tag{2.21}
\]

**Proof.** Retain the exact Chern--Weil identity from
[the compactified pencil, Section 3](../mathematics/current/line1_compactified_pencil.md):

\[
 P_t=k(t)R+\ell(t)P+12\pi^2(1+t)T_+-72\pi^2tp,
\]
\[
 k(t)=(1+t)(8t-1)/2,\qquad \ell(t)=2(1+t)(1-2t),
 \quad R=\int|\operatorname{Ric}|^2.
\]

At \(t=t_*\in(0,1/8)\), the topological terms cancel at \(e=G(h)\),
so
\(P_t\le8\pi^2A|k(t)|(G(h)-e)_++\ell(t)P\).
For normalized negative target error \(r\le1\), the actual scalar
budget gives \(8\pi^2A/V\le9\), and \(P/V\le r\).
Combining with (2.20) gives (2.21) for the negative-target infimum by
constant rescaling. Large residuals are immediate.

For clarity, passing to \(\mathcal E\), the infimum over both signs,
uses the inherited independent positive-target bound. If \(I=\int s\le0\),
that infimum over positive targets is four. Otherwise it is
\(\mathcal E_+=4-I^2/(RV)\ge4/e\), using
\(\int s_-^2\ge32\pi^2A\). If \(\mathcal E_+<1/2\),
the other Chern--Weil budget gives
\(e(1-\mathcal E_+)\le3\min(T_+,T_-)/A\le3\),
so \(e\le6\), contradicting \(\mathcal E_+\ge2/3\).
Thus \(\mathcal E_+\ge1/2\), which also implies (2.21) after
reducing its constant. QED.

As \(h\downarrow1/4\),

\[
 t_*^2(1-2t_*)^2=\frac49(h-1/4)^2+O((h-1/4)^3).
\]

This is an actual strengthening of the whole-metric upper wall on its
existing supplied topological families. It is not a new manifold supply,
not a proof that the quadratic rate is optimal, and not a nondegenerate
zero-end estimate.

## 3. What high index costs on an amplitude-controlled local core

We next continue X07 rather than replace an actual core by a formal matrix.
For fixed \(d\), on the rescaled hyperbolic ball \(x=ry\), take

\[
 \rho_0=4/3,\quad b=\rho_0 2^{(d-1)/2},\quad
 t_0=b(\bar z_1^d,\bar z_2^d),\qquad
 m_0=|t_0|^2.
 \tag{3.1}
\]

The antiholomorphic primitive and curved contraction of X07 give an exact
solution (2.1), with \(t(ry)=t_0(y)+O_d(r)\) in \(C^1\), on taking
\(r\) sufficiently small after \(d\). This order of choices suffices
for every diagonal assertion below; no uniform implicit-function radius
is assumed.

Fix \(0<m_1<m_2\). Work on the level core \(\Omega_d=\{m_0<m_2\}\)
and its shell \(T_d=\{m_1<m_0<m_2\}\), instead of the round collar
whose amplitude grew rapidly with \(d\). Set

\[
 K_d=\frac{\pi^2}{d^2b^{4/d}}B(1/d,1/d),\qquad
 B_d=B(2-1/d,1/d).
\]

For \(k\ge0\), elementary integration gives

\[
 \int_{\Omega_d}m_0^k
 =r^4K_d\frac{m_2^{k+2/d}}{k+2/d},\qquad
 K_d\sim\frac{\pi^2}{2d}.
 \tag{3.2}
\]

In particular, volume is asymptotic to \(\pi^2r^4/4\), whereas positive
moments of torsion mass are \(\Theta(r^4/d)\). On the shell, writing
\(\Delta m^q=m_2^q-m_1^q\),

\[
 \int_{T_d}|\nabla t_0|^2
 =4\pi^2r^2b^{-2/d}\frac{d^2}{d+1}\Delta m^{1+1/d},
 \tag{3.3}
\]
\[
 \int_{T_d}|\nabla t_0|^4
 =4\pi^2d^2(B_d+1)\Delta m^2,
 \tag{3.4}
\]
\[
 \int_{T_d}|\langle t_0,\nabla t_0\rangle|^2|\nabla t_0|^2
 =\frac{4\pi^2d^2}{3}
       [(2-1/d)B_d+1]\Delta m^3.
 \tag{3.5}
\]

**Verification.** Put \(u=b^2|z_1|^{2d}\), \(v=b^2|z_2|^{2d}\).
Then
\(d\mu=\pi^2r^4d^{-2}b^{-4/d}(uv)^{1/d-1}du\,dv\).
The change \(u=mx,v=m(1-x)\) proves (3.2). Use
\(|\nabla_y t_0|^2=2b^2d^2(|z_1|^{2d-2}+|z_2|^{2d-2})\)
for (3.3)--(3.4), and
\(|\langle t_0,\nabla_y t_0\rangle|^2
=2b^4d^2(|z_1|^{4d-2}+|z_2|^{4d-2})\) for (3.5).
The beta recurrence reduces the latter angular factor to
\((2-1/d)B_d+1\). Also
\(B_d=d-1+O(d^{-1})\), by the reflection formula for Gamma.

Thus quadratic derivative energy is \(\Theta(r^2d)\), while the two
critical shell energies are \(\Theta(d^3)\). The seed spinor satisfies
\(|\nabla\Phi_0|^2=m_0/(2\rho_0^2)\) and
\(|\nabla^2\Phi_0|^2=|\nabla t_0|^2/(2\rho_0^2)\).
For each fixed \(d\), actual perturbations converge in every required
finite norm as \(r\to0\); choose the diagonal so these relative errors
also tend to zero. The regular positive mass levels persist.

The relative torsion index remains \(d^2\); the determinant relative
square is exactly zero by Stokes on the trivial line. The former uses the
actual torsion boundary framing and is not an unframed determinant charge.
On a boundary near \(m_0=m_*=128/81\), mass is normal but outgoing
derivatives are of size \(d/r\). The whole-core mass mismatch is
\(\Theta(r^4)\), not small relative to its own volume. Both it and the
negative determinant model mismatch have vanishing integrals after a
sufficiently small insertion. A calibrated exterior is still absent.

### 3.1. What an extension must pay

Suppose an extension has a region \(U\) and compactly supported cutoff
\(\eta\), equal to one on the actual core, with

\[
 \operatorname{Vol}U\le C r^4,\qquad |d\eta|\le C/r,
 \qquad |t|\le C \text{ on }U.
 \tag{3.6}
\]

These are explicit extension hypotheses, not uniform geometric properties
of the level shell: its thickness can be of order \(r/d\), and its
extrinsic curvature of order \(d/r\). Amplitude control alone does not
give the cutoff in (3.6). Put
\(E_D=\int_U|D^-_{3A}t|^2\) and
\(E_0=\int_U(s^2+|F_A^-|^2)\).
The twisted Lichnerowicz identity applied to \(\eta t\) gives

\[
 \boxed{c r^2d\le C E_D+C r^2+C r^2\sqrt{E_0}.}
 \tag{3.7}
\]

Indeed the gradient energy on the core is bounded below by (3.3).
The Dirac product rule costs at most \(2E_D+Cr^2\). Its scalar and
determinant-curvature potential, acting on a bounded section supported
in volume \(Cr^4\), has absolute integral at most \(Cr^2\sqrt{E_0}\).
The opposite Weyl tensor does not occur in this spinorial potential.
For sufficiently large \(d\), (3.7) implies

\[
 E_D\ge c r^2d\quad\hbox{or}\quad E_0\ge c d^2.
 \tag{3.8}
\]

For the same actual solution the torsion equation bounds the first cost
by the integral of \(C(|W^+|^2+|\zeta|^2|\nabla_A\Phi|^2)\), under
the bounded-amplitude convention. Thus matching requires an additional
actual source, not merely a choice of boundary framing. Nevertheless,
if \(V\asymp d^2\), its required residual density is only
\(r^2d/V\asymp r^2/d\to0\). The alternative (3.8) therefore does
not exclude a weak endpoint sequence.

## 4. Splitting index changes the critical cost

The \(d^3\) cost of (3.5) is not universal for index \(d^2\). Fix
\(0<L<1/2\) and use the separated seed

\[
 t_0=b((\bar z_1/L)^d-1,(\bar z_2/L)^d-1).
 \tag{4.1}
\]

Its antiholomorphic primitive in the same spinor construction is

\[
 g=\frac{bL}{2\rho_0}\left[
 \frac{(\bar z_1/L)^{d+1}}{d+1}-\frac{\bar z_1}{L}
 -\frac{(\bar z_2/L)^{d+1}}{d+1}+\frac{\bar z_2}{L}\right].
 \tag{4.2}
\]

There are \(N=d^2\) simple zeros. For large \(b\), each fixed mass
component has inverse branches
\(\bar z_i=L\xi_i(1+w_i/b)^{1/d}\), with \(\xi_i^d=1\).
Their derivatives are similarities up to relative \(O(b^{-1})\),
uniformly in \(d\). Each physical component has scale
\(\ell=rL/(bd)\) and index one. Take \(r\) sufficiently small after
\((d,b)\) for the actual contraction and its relative errors.

Summing over these components, the linear-map integrals give

\[
 \operatorname{Vol}\{m<m_2\}
 =(1+o(1))\frac{\pi^2m_2^2}{2}N\ell^4,\qquad
 \int_{m<m_2}|\nabla t|^2
 =(1+o(1))2\pi^2m_2^2N\ell^2,
 \tag{4.3}
\]
\[
 \int_{m_1<m<m_2}|\nabla t|^4
 =(1+o(1))8\pi^2N\Delta m^2,
 \tag{4.4}
\]
\[
 \int_{m_1<m<m_2}|\langle t,\nabla t\rangle|^2|\nabla t|^2
 =(1+o(1))\frac{8\pi^2}{3}N\Delta m^3,
 \tag{4.5}
\]
\[
 \int_{m_1<m<m_2}|\nabla(t/|t|)|^4
 =(1+o(1))9\pi^2N\log(m_2/m_1).
 \tag{4.6}
\]

For example \(t=x/\ell\) has \(|\nabla t|^2=4/\ell^2\) and
\(|\nabla(t/|t|)|^2=3/|x|^2\); radial integration proves the constants.
The actual perturbation preserves these asymptotics, the simple indices,
and zero determinant relative charge on every component.

Here \(N\ell^2=r^2L^2/b^2\) and
\(N\ell^4=r^4L^4/(b^4d^2)\). Thus the subcritical costs vanish, while
the critical cost is only linear in total index. These are costs on the
selected components, not an estimate on all the space between them.

This also identifies a qualification in I50's frontier interpretation.
Its lower bound in terms of \((H/V)^{-1/3}\), \(H=\sum1/n_e\), forces
divergent critical density **only if \(H/V\to0\)**. A split collection
of \(N\asymp V\) trivial-character interfaces has \(n_e=1\) and
\(H/V\asymp1\), with bounded positive critical density as in (4.6).
I50's determinant atoms do not charge these interfaces. The local pattern
fits this alternative; it is not a closed zero-end construction.

### 4.1. A closed extension needs a nonparallel exterior

There is a global test of the proposed matching which does not require
extracting any cores. For the same weight-two solution on a closed
scalar-minus-four metric, the integrated spinor equation is

\[
 K:=\int|\nabla_A\Phi|^2=\int k(\rho),\qquad
 k(\rho)=\rho-\rho^2/2.
\]

Since \(|k'|\le1\) on \([0,2]\), (2.5) gives

\[
 \boxed{\frac{D_\beta}{V}\ge
 6\left|\frac KV-\frac49(1-\beta^{-1}-2\beta^{-2})\right|^2.}
 \tag{4.7}
\]

Thus a zero-end sequence must have \(K/V\to4/9\). For every fixed
split seed the whole shrinking construction ball, including the regions
between its selected components, has \(K=O_{d,b}(r^4)\) and curvature
energy \(O_{d,b}(r^4)\); its Hessian integral is \(O_{d,b}(r^2)\).
This follows by differentiating the smooth rescaled seed and choosing
the actual perturbation radius after \((d,b)\), as in X07. A diagonal
can make these costs negligible. Any closed extension with the required
volume normalization must therefore put \((4/9+o(1))V\) kinetic
energy in the exterior. A proposed nearly parallel exterior with
\(K/V\to0\) instead has \(\liminf D_\beta/V\ge32/27\).

This matching assertion assumes the closed scalar-minus-four extension
actually retains the displayed local solution. A conformal reduction of
some other proposed extension need not preserve its hyperbolic cores.

The harmonic data give another necessary exterior requirement. Under the
class-square condition, the topological saturation already proved in
[I41, Section 6](20260927_conformal_separation_and_zero_end.md) gives
\((a^2-T_+)/V\to0\) on the hypothetical zero-end sequence. This
statement concerns the class and metric and does not identify its earlier
weighted solution with the present one. Chern--Weil gives
\(T_+/V\to1/(6\pi^2)\), while (2.5) gives
\(\int|F_A^+|^2/V\to8/9\). Hence

\[
 \frac{\|H_A^+\|_2^2}{V}\to\frac89,\qquad
 \frac{\|H_A^-\|_2^2}{V}\to\frac29,
 \tag{4.8}
\]

using the same-class harmonic remainder (2.11). The shrinking construction
ball cannot carry these volume-scale harmonic energies: its actual
curvature energy and the global harmonic remainder are both negligible
at that scale. The exterior must supply them. It is not enough to glue
the displayed local zero sets into a metrically convenient region.

These are necessary matching tests, not an exclusion of every exterior.
A nonparallel bulk with \(K/V\to4/9\) and the harmonic data (4.8)
is not contradicted by these identities. Its construction or exclusion,
including the original same-class conformal solvability, remains open.

## 5. The balanced first-order target must retain curvature cancellation

Return to the **ordinary**, unscaled solution used in I50 Section 4 on the
balanced family. This section does not substitute the weight-two field of
Section 2 into ordinary-solution identities. Retain
\(\rho\le4\), \(\chi\), \(q_\chi\), \(B_o\), \(J\), \(M_\chi\),
and \(P_o\) from that section. Put

\[
 f=1-\chi,\quad u=\Phi/\sqrt\rho,\quad
 \mathbb F=F^{S^+},\quad C_\pm=\mathbb F^\pm u,
\]
\[
 X_\pm=\int f|C_\pm|^2,\qquad
 Y_\pm=\int f\operatorname{Re}\langle C_\pm,F_A^\pm u\rangle.
 \tag{5.1}
\]

The weighted expressions extend by zero near the spinor zero set. In a
unitary frame whose first vector is \(u\), write
\(\mathbb F^-=\left(\begin{smallmatrix}i\alpha&-\overline b\\
b&i\delta\end{smallmatrix}\right)\). Then

\[
 |\operatorname{Ric}^{\circ}|^2
 =2|\alpha-\delta|^2+8|b|^2,\qquad
 |F_A^-|^2=|\alpha+\delta|^2.
\]

Expanding both sides proves

\[
 \boxed{P_o-2B_o=8(X_--Y_-),\qquad
 |Y_-|\le\sqrt{X_-B_o}.}
 \tag{5.2}
\]

Consequently the existing spatial balance becomes exactly

\[
 P-8\pi^2Ah=8\left[X_--Y_--4\pi^2q_\chi+
             \pi^2(p-A)+J/4+M_\chi/4\right].
 \tag{5.3}
\]

A sufficient joint target for coefficient four is
\([Y_--X_-+4\pi^2q_\chi]_+=o(Ah)\). In particular,
\(X_-=o(Ah)\) and \((q_\chi)_+=o(Ah)\) would suffice, since
\(B_o=O(Ah)\). Unlike demanding \(B_o=o(Ah)\), this permits a
nonzero ASD determinant field annihilating the actual spinor.

There is no automatic new sign: the same rank-two Chern identity gives

\[
 4\pi^2q_\chi=(X_--Y_-)-(X_+-Y_+),\qquad
 Y_--X_-+4\pi^2q_\chi=Y_+-X_+.
 \tag{5.4}
\]

Thus the coupled criterion is an exact reformulation of the surviving
signed defect, not an independently proved positive estimate.

### 5.1. The same ordinary solution only has an order-Ah bound

Let \(\Pi=\nabla_A\Phi\), \(K=\int|\Pi|^2\), and \(D=D_2\).
Use the polynomial model from the ordinary remainder with
\(s_b=-4\), \(\operatorname{Ric}_b^\circ=0\), \(W_b^+=W_0\),
\(F_{A,b}^+=i\sigma(\Phi)\), \(F_{A,b}^-=0\).
Its curvature-action coefficients factor as

\[
 \rho^2/24+1/3-\rho/4=(\rho-2)(\rho-4)/24,
 \quad \rho^2/48-1/3=(\rho-4)(\rho+4)/48.
\]

The actual remainder bounds therefore imply
\(\int|\mathbb F_b\Phi|^2\le CD\) and
\(\int|\mathbb F-\mathbb F_b|^2\le C(P+B+D)\).
Apply the exact Hessian identity of I40 Section 4.1 to this ordinary
solution. Its bounded background terms cost \(CK\); its error terms
cost \(C\sqrt{P+B+D}\|\Pi\|_4^2\). The bounded-section interpolation
\(\|\Pi\|_4^2\le8\|\nabla_A^2\Phi\|_2\), followed by Young,
gives

\[
 \int(|\nabla_A^2\Phi|^2+|\nabla_A\Phi|^4)
                  \le C(K+P+B+D).
 \tag{5.5}
\]

On the balanced \(\mathcal E=O(h)\) sequences, the right side and
\(X_-\) are \(O(Ah)\), not \(o(Ah)\).

The remaining signed interaction can be written without an abstract
regularity assumption. Set
\(\mathcal J_3=\operatorname{Re}\langle\Pi\wedge\mathbb F\Phi\rangle\),
\(\mathcal C_4=\operatorname{Re}\langle\Pi\wedge\mathbb F\wedge\Pi\rangle\),
with conjugation in the first Hermitian factor. Covariant differentiation
and Bianchi give

\[
 d\mathcal J_3=(|\mathbb F^+\Phi|^2-|\mathbb F^-\Phi|^2)d\mu
                          -\mathcal C_4.
\]

Integrate against \(w_0=f/\rho\), extended smoothly by zero:

\[
 X_-=\int w_0|\mathbb F^+\Phi|^2-
           \int w_0\mathcal C_4+\int dw_0\wedge\mathcal J_3.
 \tag{5.6}
\]

The first term is \(O(D)\). After subtracting the model, the critical
interaction is bounded by
\(C\|\mathbb F-\mathbb F_b\|_2\|\Pi\|_4^2=O(Ah)\).
The cutoff current is likewise \(O(Ah)\). Taking absolute values
therefore does not prove the required smaller signed remainder.

For an exact negative cscK canonical ordinary solution, \(\rho=4\),
\(\nabla_A\Phi=0\), \(C_\pm=0\), and \(\chi=q_\chi=0\).
Equation (5.2) correctly gives \(P=2B\), even when \(B\ne0\).
This is why its cancellation must be retained. No transfer of this
observation to a whole balanced handle-and-blowup recovery sequence is
asserted without matching the actual solutions.

## 6. The remaining global implication

The endpoint problem now has an exact constant-scalar, constant-weight
form with small determinant Hodge graph error. Its unresolved source is
not an auxiliary weight derivative. It is the critical coupling of the
torsion derivative, the actual curvature, and signed transition flux.

High-index cores cannot be excluded by their listed subcritical costs;
their controlled extensions satisfy the explicit alternative (3.8).
Splitting the zeros avoids treating the monomial's superlinear cost as
universal. Neither model supplies the closed exterior, the global square
condition, or the same-class conformal supplier required by O10.

For the balanced problem, (5.3)--(5.6) locate the order-Ah signed term
without discarding the parallel-core cancellation. Its little-o estimate
or a lower-coefficient actual recovery construction is still required.
These are the two continuing global tests; the new identities do not
replace them by a completed defect-decomposition or realization theorem.
