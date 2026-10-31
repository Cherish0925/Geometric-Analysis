# 第四卷：实际扭率、相位曲率与全局有符号通量

Research snapshot: 0b1490791be560203b86a7d9834dcdc3cbc83b41.

三份零端推导全文，最后一份含最新第7节实际核心检验。后续方程消去中央与标量导数时也消去了正拓扑预算，不能把旧的正项与新的简化公式混合使用。最终(6.6)是尚待加强的恒等式，不是O10的证明。

Read 00_READ_FIRST.md for superseded statements. Each source below is complete and byte-preserved. Original local links remain relative to their source; locate other texts using 10_source_map_and_history.md. Formula numbers restart in each source.


---

## Source 1: 20260928_zero_endpoint_phase_curvature.md

Original path: `continuation/20260928_zero_endpoint_phase_curvature.md`

SHA-256: `3d107164ea9ad11df362c287222cd700747c92aba155c32baafdab6daf892329`

BEGIN COMPLETE SOURCE

# The opposite-spinor curvature equation at the weak zero endpoint

28 September 2026. This continues Sections 1--2 of
[I52](20260927_endpoint_covariance_and_surgery_limits.md).
It derives the next actual curvature equation and follows its integral
test. It does not prove the unrestricted endpoint gap.

Subsequent continuation: [the actual torsion prolongation](20260928_actual_torsion_prolongation.md)
removes the exact-closure premise from the bracket in Section 3.2.
The cubic torsion itself determines that bracket for the actual field.
It also supplies the full-error Weyl interaction; the remaining
symmetric-derivative term has not been absorbed. The original ideal
calculation below is retained, not used as the strongest current scope.

## 1. A polynomial equation through torsion zeros

Retain the same actual constant-weight solution, scalar curvature \(-4\),
and notation of I51/I52:
\[
 \rho=|\Phi|^2,\quad \tau=t_\Phi,\quad m=|\tau|^2,\quad
 f=-iF_A^-,\quad Q=-iq_-(\tau),\quad |Q|^2=m^2/8.
\]
Hermitian products are conjugate-linear in the first argument.
The torsion is a section of \(E=S^-\otimes L\), with its actual
connection denoted by \(\nabla=\nabla_{3A}\). Define
\[
 U=\nabla\tau,\qquad j_i=\operatorname{Im}\langle\tau,U_i\rangle,
 \qquad T_{ij}=2\operatorname{Im}\langle U_i,U_j\rangle .
\]
Here \(U\) is a covariant one-form, not the Dirac contraction.
Differentiating the current gives the exact global identity
\[
 (dj)_{ij}=T_{ij}+
           \operatorname{Im}\langle\tau,F^E_{ij}\tau\rangle .
                                                               \tag{1.1}
\]
It is polynomial in the actual fields and has no division at a zero.

For clarity the Clifford signs can be checked in the frame of I41,
Section 14:
\[
 C_1=I,\quad C_2=\operatorname{diag}(i,-i),\quad
 C_3=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\quad
 C_4=\begin{pmatrix}0&-i\\-i&0\end{pmatrix}.
\]
On negative spinors,
\(c^-(e^i\wedge e^j)=-C_iC_j^*\), \(i<j\).
For \(\Omega_-=e^{12}-e^{34}\),
\[
 c^-(\Omega_-)e_1=2ie_1,\qquad
 q_-(\sqrt m e_1)=-im\Omega_-/4,\qquad Q=-m\Omega_-/4.
\]
With the curvature-operator convention used in I41, the Levi-Civita
spin curvature is
\[
 (F_{\rm LC}^{S^-})_{ij}
        =-\tfrac12c^-(\mathcal R(e^i\wedge e^j)).
\]
This sign also yields the scalar term \(s/4\) in the
Lichnerowicz formula on a space form. In a unit frame
\(v=\tau/\sqrt m\), the ASD part of its expectation is
\[
 \bigl(\operatorname{Im}\langle v,F_{\rm LC}^{S^-}v\rangle\bigr)^-
       =-\tfrac12(W^-+s/12)\Omega_-.
\]
The central part of \(F^E\) is \((3/2)F_A I\).
Substitution into (1.1) proves
\[
 \boxed{(dj)^-=2W^-Q+\frac{s}{6}Q+\frac32 m f+T^-.}    \tag{1.2}
\]
Although the unit frame was used to verify it, (1.2) holds globally,
including \(m=0\), by (1.1) and the quadratic Hopf identities.

On the nonzero set, put
\[
 \theta=j/m,\qquad b=(1-vv^*)\nabla v,\qquad
 \mathcal Q(b)_{ij}=2\operatorname{Im}\langle b_i,b_j\rangle .
\]
The radial terms cancel in the usual unit-section differentiation,
leaving
\[
 d\theta=\operatorname{Im}\langle v,F^Ev\rangle+\mathcal Q(b).
                                                               \tag{1.3}
\]
The factor in \(\mathcal Q\) is fixed by its component definition;
using an antisymmetrized wedge without its convention would double it.

## 2. Testing the equation does not produce a new positive remainder

Let
\[
 S=m_*+2\rho^2|\nabla_A\Phi|^2,\quad
 m_*=128/81,\quad a=\rho^3/S,\quad \lambda=9/8,\quad K=-\lambda aQ.
\]
These are the same smooth bounded rational weights as in I52.
The actual quadratic Dirac identity there is
\[
 \delta Q=-\tfrac12 j+E_\tau,\qquad
 |E_\tau|^2=\tfrac14m\,|D^-_{3A}\tau|^2,\qquad
 \fint|aE_\tau|^2\le C\eta.
\]
In particular \(\fint|aj|^2\le C\): use
\(|j|^2\le m|\nabla\tau|^2\), the bound for \(a^2m\),
and the inherited \(L^2\) derivative budget.

Pair (1.2) with \(a^2Q\). Since
\(\delta(a^2Q)=a^2\delta Q-2a\iota_{\nabla a}Q\),
integration by parts gives
\[
\begin{aligned}
 2\int a^2\langle W^-Q,Q\rangle={}&
 -\tfrac12\int a^2|j|^2-\int a^2\langle T,Q\rangle
 -2\int a\langle j,\iota_{\nabla a}Q\rangle\\
 &+\tfrac23\int a^2|Q|^2-\tfrac32\int a^2m\langle f,Q\rangle
 +\int a^2\langle j,E_\tau\rangle .
\end{aligned}                                         \tag{2.1}
\]
The last term is \(O(\sqrt\eta V)\). In the limiting calibration
\[
 \rho\to4/3,\quad m\to128/81,\quad a\to3/4,\quad f-K\to0,
\]
the two displayed algebraic terms, divided by \(V\), converge to
\[
 \frac23a^2\frac{m^2}{8}
       +\frac32\lambda a^3m\frac{m^2}{8}
       =\frac{1024}{2187}.                            \tag{2.2}
\]
For this limit, the bounded weighted factors and the actual
saturation estimate control the tails; an unweighted convergence of
every power of \(m\) is not assumed.

The derivative terms in (2.1) still have no proved sign or vanishing.
The comparison of scalar equations must be made in the ideal reduced
system, not by discarding error terms from an actual weak solution.
On \(\rho>0,m>0\), define the unit positive form by
\(F_A^+=i\rho\Omega_+/2\), and let \(J_+\) be its action on one-forms,
with \(J_+dx^1=dx^2,\ J_+dx^3=dx^4\) in an adapted frame.
In a compatible frame \(\Phi=\sqrt\rho e_1\), put
\[
 N_{bc}=\frac1{\sqrt2}\sum_j(C_j^*)_{1b}(\nabla_j\tau)_c .
\]
For this paragraph impose exactly
\[
 N=0,\quad \delta\Omega_+=0,\quad
 \operatorname{Ric}^{\circ}=0,\quad D^-_{3A}\tau=0,\quad
 f=-2Q/\rho^3,\quad s=-4.
\]
The first condition gives \(\theta=-J_+d\log m/2\).
The phase-curvature and torsion Lichnerowicz equations then read
\[
 \tfrac12\Delta\log m=\tfrac32\rho-|b|^2,\qquad
 \tfrac12\Delta\log m=1+\frac{3m}{2\rho^3}-|b|^2 .
\]
No assumption \(d\rho=0\) is used in this comparison.
Their difference recovers only
\(3\rho/2=1+3m/(2\rho^3)\). At \(\rho=4/3\) it gives
\(m=128/81\). In the exact constant-length case the further curvature
relation is \(W^-\Omega_-=(10/3)\Omega_-\).
These are steps of the classical
[Armstrong mechanism, Sections 3.3.1--3.3.3](https://johnarmstrongmaths.com/publications/resources/thesis.pdf),
not its complete weak-error replacement. In particular the radial
terms cannot be counted twice as a coercive error.

## 3. The derivative-free transgression retains a critical interaction

For the actual unitary bundle \(E\), exterior covariant differentiation
gives \(\nabla U=F^E\tau\) and \(\nabla F^E=0\). Therefore
\[
\begin{aligned}
 d\,\operatorname{Re}\langle U\wedge F^E\tau\rangle
  ={}&\bigl(|(F^E)^+\tau|^2-|(F^E)^-\tau|^2\bigr)d\mu\\
     &-\operatorname{Re}\langle U\wedge F^E\wedge U\rangle .
\end{aligned}                                                   \tag{3.1}
\]
On a fixed calibrated mass band, with \(\chi\) supported away from
\(m=0\), one can multiply by the smooth weight
\(w=\chi(\rho,m)/m\). The resulting integral retains both
the derivative of that weight and the opposite-Weyl interaction
\[
 \mathcal C_W=\frac1V\int w\,
  \operatorname{Re}\langle\nabla\tau\wedge
      F_{\rm LC}^{S^-}(W^-)\wedge\nabla\tau\rangle .     \tag{3.2}
\]
Its natural absolute bound is
\[
 \frac C V\int_{\operatorname{supp}\chi}
       \frac{|W^-|\,|\nabla\tau|^2}{m}.               \tag{3.3}
\]
The normalized \(L^2\) bound for \(W^-\) supplied by a bounded
Euler density and the normalized \(L^2\) bound for \(\nabla\tau\)
do not bound (3.3). In particular the second factor squared is
only \(L^1\), not the \(L^2\) needed for a direct pairing.
The zero-order fit \(f\approx K\) supplies no such missing derivative
norm. A weak Bianchi test with the normalized Hopf field encounters
the same interaction after commuting derivatives.

Thus (3.1) is a legitimate derivative-free formula, but it has not
removed the critical term. A signed cancellation or a stronger
consequence of the complete actual equations is still required.
Neither an absolute-value estimate nor a div--curl limit has been
established here.

### 3.1 The curvature column fixed by (1.2) is not the whole interaction

The unidentified part can be isolated algebraically rather than hidden
in a full-curvature norm. At a point with \(\tau=\sqrt m e_1\), use
the anti-self-dual basis
\[
 \Omega_1=e^{12}-e^{34},\quad
 \Omega_2=e^{13}+e^{24},\quad
 \Omega_3=e^{14}-e^{23},
\]
each of squared norm two. Write
\[
 U/\sqrt m=(\alpha+i\theta,\gamma+i\delta),\qquad
 \alpha=dm/(2m),
\]
where all four entries on the right are real one-forms. Define
\[
\begin{aligned}
 B_{1b}&=\langle\gamma\wedge\delta-\alpha\wedge\theta,\Omega_b\rangle,\\
 B_{2b}&=\langle\alpha\wedge\gamma+\theta\wedge\delta,\Omega_b\rangle,\\
 B_{3b}&=\langle\alpha\wedge\delta-\theta\wedge\gamma,\Omega_b\rangle.
\end{aligned}
\]
If \(W^-\Omega_b=\sum_a W_{ab}\Omega_a\), direct Clifford contraction gives
\[
 \operatorname{Re}\langle U\wedge F_{\rm LC}^{S^-}(W^-)\wedge U\rangle
          =m\sum_{a,b}W_{ab}B_{ab}\,d\mu .                  \tag{3.4}
\]
Indeed \(F_{\rm LC}(W^-)=-\tfrac12\sum_{a,b}W_{ab}\Omega_b I_a\),
where \(I_a=c^-(\Omega_a)/2\); expanding its three \(2\times2\)
matrices gives exactly the three rows above.

Equation (1.2) determines \(W^-Q\), hence the first column of \(W\).
Symmetry and zero trace leave
\[
 D=(W_{22}-W_{33})/2,\qquad E=W_{23}
\]
undetermined. Their contribution to (3.4) is
\[
 m\{D(B_{22}-B_{33})+E(B_{23}+B_{32})\}.                \tag{3.5}
\]
Even imposing the principal constraints \(N=0\) and \(D^-_{3A}\tau=0\)
at this point does not eliminate it. Solving those linear constraints,
write the component arrays as
\[
\begin{aligned}
 \alpha&=(a,b,c,d),&\theta&=(b,-a,d,-c),\\
 \gamma&=(-c,-d,u,v),&\delta&=(-d,c,v,-u).
\end{aligned}
\]
Substitution reduces (3.5) to
\[
               4m\{D(au+bv)+E(av-bu)\}.                \tag{3.6}
\]
It vanishes for an exactly constant-length field, but weak length
convergence does not control its curvature-weighted product.

For a concrete sign check, take
\[
 U/\sqrt m=(dx^1-i\,dx^2,\;dx^3-i\,dx^4),\qquad
 W^-=\operatorname{diag}(0,t,-t).
\]
Then \(N=0,\ c^-(U)=D^-_{3A}\tau=0,\ W^-Q=0\), while (3.4) equals
\(4mt\,d\mu\). Thus substituting the column equation cannot alone
give a sign for the remaining transgression. One can equivalently
add this trace-free block to a curvature operator with a prescribed
first column. This is an algebraic nonimplication for the displayed
identities, not a constructed jet of the full original monopole system
and not a closed escape sequence. Any complete cancellation must use
additional differential information or control precisely the
radial--horizontal covariance in (3.6).

### 3.2 Why the pointwise freedom is not an exact local solution

The full differential system does impose a further restriction when
the ideal hypotheses of Section 2 hold on an open set, with the
actual cubic torsion \(\tau=t_\Phi\). This is precisely where the
weak proof still requires additional control. On \(\rho,m>0\), take
the adapted frame above and put
\(\kappa=\sqrt m/(2\rho^{3/2})\).
In the ideal closed-form system, the off-diagonal part of the
connection of \(\Phi/\sqrt\rho\) is
\((\kappa,-i\kappa,0,0)\). For
\(\Psi_2=e^{13}-e^{24}\), \(\Psi_3=e^{14}+e^{23}\), this gives
\[
 \nabla_1\Omega_+=-2\kappa\Psi_3,\quad
 \nabla_2\Omega_+=-2\kappa\Psi_2,\quad
 \nabla_3\Omega_+=\nabla_4\Omega_+=0.
\]
With \(Z_1=e_1-ie_2,\ Z_2=e_3-ie_4\), its Nijenhuis bracket is
\[
       [Z_1,Z_2]\equiv-2\kappa\overline Z_1
                                      \pmod{T^{1,0}}.          \tag{3.7}
\]
If \(N=0\) on this open set, its two rows say
\(\nabla_{Z_1}\tau=\nabla_{Z_2}\tau=0\).
In the ideal Einstein/type-\((1,1)\) system,
\(F^E(Z_1,Z_2)=0\): the Levi-Civita off-diagonal curvature
is zero and the determinant curvature has type \((1,1)\).
Commuting the two derivatives and using (3.7) forces
\(\nabla_{\overline Z_1}\tau=0\).
Together with the Dirac equation, the component form in Section 3.1
then gives \(\alpha=\theta=0\), hence \(dm=0\).
Thus the algebraic example following (3.6) is not claimed to prolong
to an exact ideal solution on a neighborhood.

This calculation also identifies why the weak version is not free.
Put \(A_i=\nabla_{Z_i}\tau\), \(B=\nabla_{\overline Z_1}\tau\).
Keeping exact closure but allowing \(N\ne0\), the commutator retains
the terms
\[
 2\kappa B
   =F^E(Z_1,Z_2)\tau-\nabla_{Z_1}A_2+\nabla_{Z_2}A_1
                                      +\sum_i L_iA_i,         \tag{3.8}
\]
where \(L_i\) are the components of the \(T^{1,0}\) bracket.
Testing against a cutoff multiple of \(B\) moves a derivative onto
\(B\), not merely onto the scalar cutoff. It produces both
\(A_i\nabla B\) and \(A_i\,d\chi\,B\), and in moving adapted
frames also their connection terms. Current \(L^2\) estimates for
\(N,\nabla\tau\) do not control these products. Errors in closure
of \(\Omega_+\) contribute additional derivative products.
This is an exact-system explanation and a precise weak proof
obligation, not a proof of the missing uniform endpoint gap.

## 4. A local sign check for index-counting approaches

The relative torsion index is not automatically positive. Fix
\(\rho_0>0\). In the flat frame above, put
\[
 H=2x_2x_4-i(x_1x_4+3x_2x_3),\qquad
 G=\tfrac12(x_1^2+x_2^2-3x_3^2+x_4^2).
\]
Directly, \(D^+(H,G)=0\). The leading torsion of the rescaled
Dirac seed
\[
 \Phi_r(x)=\bigl(\sqrt{\rho_0}+rH(x/r),\,rG(x/r)\bigr)
\]
is
\[
 \rho_0(y_1+iy_2,\,3y_3-iy_4),\qquad y=x/r.
\]
Its real Jacobian has determinant \(-3\rho_0^4\), and it is
nonzero on a fixed spherical collar. The fixed-seed local
right-inverse and contraction construction in
[I41, Sections 15--15.1](20260927_conformal_separation_and_zero_end.md)
therefore promotes this seed to the positive-constant-weight actual
equation on a sufficiently small hyperbolic ball. The rescaled
torsion correction is small on that collar, so its index remains
\(-1\).

This is a local statement. The determinant line is trivial there;
the integrated current square is \(O(r^4)\) and the Hessian square
is \(O(r^2)\) for a fixed seed. It does not give the calibrated
closed exterior, the required class-square budget, or the complete
conformal/weight supplier. It only prevents replacing a signed
relative-index calculation by an unsupported count of positive
zeros. No new global counterexample is registered.

## 5. Continuation point

The actual polynomial curvature equation is now explicit. Its
weighted test is valid, but the opposite-Weyl/gradient interaction
(3.2), now resolved into the unfixed planar block (3.6),
and the actual global matching remain unresolved. A proof
of small weighted Dirac contraction alone does not address them.
O10 is unchanged. This record preserves the calculation so that
the next attempt starts at (3.2), rather than repeating the scalar
phase cancellation or treating local index signs as positive.


END COMPLETE SOURCE


---

## Source 2: 20260928_actual_torsion_prolongation.md

Original path: `continuation/20260928_actual_torsion_prolongation.md`

SHA-256: `b9b3a19e13b6ecc37d85862b286ff46740004cad1e1e9e9c5513334f38145696`

BEGIN COMPLETE SOURCE

# The actual torsion bracket and its integral prolongation

28 September 2026. This extends, and removes the exact-closure restriction
from, Section 3.2 of the [phase-curvature proof](20260928_zero_endpoint_phase_curvature.md).
The actual constant-weight monopole equations are retained. The result is
an exact differential identity and its tested form, not the missing weak
zero-end gap.

## 1. The bracket is determined by the actual cubic torsion

Use the Clifford matrices from I41, Section 14,

\[
 C_1=I,\quad C_2=\operatorname{diag}(i,-i),\quad
 C_3=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\quad
 C_4=\begin{pmatrix}0&-i\\-i&0\end{pmatrix}.
\]

On the open set rho = |Phi| squared > 0, choose a local positive-spinor
frame with \(\Phi=\sqrt\rho\,e_1\). All positive and negative spinor
frames, the tangent frame and the trivialization of L are chosen
compatibly with the displayed Clifford matrices. Further adaptations
below change these compatible frames together. Write

\[
 \nabla_j\Phi=(h_j,k_j),\qquad
 \zeta_j=\langle\Phi,\nabla_j\Phi\rangle=\sqrt\rho\,h_j.
\]

The defining cubic torsion \(\tau=t_\Phi\), a section of
\(E=S^-\otimes L\), has components

\[
             \tau=\rho(k_1+ik_2,-k_3-ik_4).                \tag{1.1}
\]

Let \(\Omega_+=e^{12}+e^{34}\),
\(\Psi_2=e^{13}-e^{24}\), \(\Psi_3=e^{14}+e^{23}\).
The off-diagonal positive-spinor connection is the complex one-form
\(\eta_j=k_j/\sqrt\rho\). The Clifford action gives

\[
 \nabla\Omega_+=2(\operatorname{Im}\eta)\otimes\Psi_2
                         -2(\operatorname{Re}\eta)\otimes\Psi_3.
\]

This formula first concerns real one-forms; evaluation on complex
vectors is then extended complex linearly.

Put \(Z_1=e_1-ie_2\), \(Z_2=e_3-ie_4\). Consequently

\[
 (\nabla_XZ_1)^{0,1}=\overline\eta(X)\overline Z_2,
 \qquad (\nabla_XZ_2)^{0,1}=-\overline\eta(X)\overline Z_1.
\]

Here a conjugated one-form is evaluated complex linearly; in particular
\(\overline\eta(Z_1)\) is not \(\overline{\eta(Z_1)}\).
Torsion-freeness of the Levi-Civita connection and (1.1) give

\[
 \boxed{[Z_1,Z_2]^{0,1}
  =-\frac{\overline\tau_1}{\rho^{3/2}}\overline Z_1
    +\frac{\overline\tau_2}{\rho^{3/2}}\overline Z_2.}      \tag{1.2}
\]

This identity uses the cubic definition, not closure of Omega or the
Dirac equation. It is smooth through zeros of tau on rho > 0. It is a
local expression of a tensor identity, so changing adapted frames does
not change its content. No assertion across rho = 0 is needed below.

On rho,m > 0, where \(m=|\tau|^2\), further adapt the negative frame
so that \(\tau=(\sqrt m,0)\), and set
\(\kappa_0=\sqrt m/(2\rho^{3/2})\). Then (1.2) becomes exactly

\[
                [Z_1,Z_2]^{0,1}=-2\kappa_0\overline Z_1.   \tag{1.3}
\]

One may also see the cancellation directly in the actual Dirac system.
Its two rows are

\[
 h_1+ih_2+k_3-ik_4=0,\qquad
 -h_3-ih_4+k_1-ik_2=0.
\]

Solving together with (1.1) yields

\[
 \eta=(\kappa_0+z,-i\kappa_0+iz,-w,-iw),\quad
 z=\frac{\zeta_3+i\zeta_4}{2\rho},\quad
 w=\frac{\zeta_1+i\zeta_2}{2\rho}.
\]

The z and w contributions cancel from \(\overline\eta(Z_1)\) and
\(\overline\eta(Z_2)\). They need not vanish from other connection
components. Thus there is no separate near-closure correction to (1.3).

## 2. The curvature forcing is exactly the trace-free Ricci block

For the actual constant-weight solution, \(F_A^+\) is a multiple of
\(i\rho\Omega_+\). All anti-self-dual forms have type (1,1), and
\(Z_1\wedge Z_2=\Psi_2-i\Psi_3\) is self-dual and perpendicular to
Omega. Hence \(F_A(Z_1,Z_2)=0\), exactly.

The connection on E has central curvature \((3/2)F_A I\).
Negative Clifford multiplication annihilates self-dual forms, so the
block decomposition of the Riemannian curvature operator gives

\[
 \boxed{F^E(Z_1,Z_2)
   =-\tfrac12c^-\bigl(B_{\operatorname{Ric}^{\circ}}^*
                          (\Psi_2-i\Psi_3)\bigr).}       \tag{2.1}
\]

Here \(B_{\operatorname{Ric}^{\circ}}^*=\pi_-\mathcal R|_{\Lambda^+}\)
and \((F_{\rm LC}^{S^-})_{ij}=-\tfrac12c^-(\mathcal R(e^i\wedge e^j))\),
as in the preceding phase-curvature proof.

In particular \(|F^E(Z_1,Z_2)\tau|\le C|\operatorname{Ric}^{\circ}|\sqrt m\).
Neither Weyl block nor an independent determinant error occurs in this
curvature component. This does not control all components of F^E.

Define \(A_i=\nabla_{Z_i}\tau\), \(B=\nabla_{\overline Z_1}\tau\),
and let \(\sum L_iZ_i=[Z_1,Z_2]^{1,0}\). Commuting actual derivatives
and using (1.3) gives

\[
 \boxed{2\kappa_0 B=F^E(Z_1,Z_2)\tau
       -\nabla_{Z_1}A_2+\nabla_{Z_2}A_1+\sum_i L_iA_i.}   \tag{2.2}
\]

This is the full actual counterpart of the earlier ideal-system
calculation. The moving-frame terms L_i remain part of the equation.
Smallness of A_i in L2 is not assumed: I41 (14.2) itself retains an
actual current--Hessian term in their projected derivative.

## 3. Testing does not remove the symmetric second derivatives

Let \(\mathcal A=(\nabla\tau)^{1,0}\), regarded as an E-valued one-form.
Let \(\mu\) denote the algebraic almost-complex component of exterior
covariant differentiation from type (0,1) to type (2,0). In the frame
above, \((\mu(\nabla\tau)^{0,1})(Z_1,Z_2)=2\kappa_0 B\).
The invariant form of (2.2) is

\[
 \partial_\nabla\mathcal A+\mu(\nabla\tau)^{0,1}
                         =(F^E)^{2,0}\tau.               \tag{3.1}
\]

For a real smooth cutoff f with compact support in rho,m > 0, integration
by parts is legitimate and gives

\[
\begin{aligned}
 \int f^2|\mu(\nabla\tau)^{0,1}|^2
 ={}&\operatorname{Re}\int f^2
       \langle(F^E)^{2,0}\tau,\mu(\nabla\tau)^{0,1}\rangle\\
 &-\operatorname{Re}\int\left\langle\mathcal A,
       \partial_\nabla^*\{f^2\mu(\nabla\tau)^{0,1}\}\right\rangle.
\end{aligned}                                             \tag{3.2}
\]

The adjoint contains derivatives of the cutoff, frame, mu and
\(\nabla\tau\). Its principal second derivatives have not acquired a
sign. This formula does remove an unnecessary independent closure
error, but it does not give an L2 estimate on B from an L2 estimate on A.
All norms here are tensor norms: Z_i have squared length two, and
their dual (1,0)-forms have squared norm one half. Thus
\(|\mathcal A|^2=(|A_1|^2+|A_2|^2)/2\) and
\(|\mu(\nabla\tau)^{0,1}|^2=\kappa_0^2|B|^2\).
Evaluating (3.1) on Z_1,Z_2 does not preserve these norm factors.

## 4. The remaining Weyl interaction in actual derivative variables

Retain the opposite-Weyl frame of the phase-curvature proof. Set
\(D=(W_{22}-W_{33})/2\), \(E_0=W_{23}\), and
\(C_0=\nabla_{\overline Z_2}\tau\). Subscripts 1,2 now denote spinor
components, not tangent indices. The free planar contribution to
\(\operatorname{Re}\langle\nabla\tau\wedge
 F_{\rm LC}^{S^-}(W^-)\wedge\nabla\tau\rangle\) is exactly

\[
 \boxed{\operatorname{Re}\left[(D-iE_0)
    \left\{\overline{B_1}(C_0)_2
       -\overline{(A_2)_1}(A_1)_2\right\}\right]d\mu.}   \tag{4.1}
\]

There is no N = 0 or torsion-Dirac = 0 hypothesis here. To verify it,
write \(\nabla\tau=(x,y)\) as two complex one-forms. The old wedge
matrix used derivatives divided by square root m; here that factor
is absorbed: its second row plus i times its third row, multiplied
by m, is the contraction of \(\overline x\wedge y\). Since

\[
 \Omega_2+i\Omega_3=(e^1-ie^2)\wedge(e^3+ie^4),
\]

evaluate directly \((\overline x\wedge y)(Z_1,\overline Z_2)\).
It equals
\(\overline{B_1}(C_0)_2-\overline{(A_2)_1}(A_1)_2\), proving (4.1).
This also reproduces the earlier \(4m\{D(au+bv)+E_0(av-bu)\}\)
under that calculation's additional pointwise constraints.

Substituting (2.2) into (4.1) does not turn it into a nonnegative
curvature square. Integration by parts differentiates the opposite
Weyl block, the cutoff and C_0. In particular it leaves symmetric
barred second derivatives of tau, not just curvature commutators.
These are precisely the quantities that a further signed integral
identity would have to absorb. No estimate for them follows from
separate L2 bounds for curvature and the first derivative of tau.

### 4.1 A finite jet check of the surviving derivative

This check locates a genuine principal symbol; it is not a closed
solution or a theorem ruling out additional global cancellations.
At a point put \(z_1=x_1+ix_2,z_2=x_3+ix_4\) and retain the constant
Clifford matrices. For a positive spinor increment (H,G), the two
Dirac rows are

\[
 D^+(H,G)=\bigl((\partial_1+i\partial_2)H+
                   (\partial_3-i\partial_4)G,
       (-\partial_3-i\partial_4)H+(\partial_1-i\partial_2)G\bigr).
\]

The linearized torsion at \(\Phi=\sqrt\rho e_1\) is
\(T(H,G)=\rho((\partial_1+i\partial_2)G,
                    - (\partial_3+i\partial_4)G)\).
Both polynomial seeds

\[
 (H,G)=(\overline z_1\overline z_2,|z_1|^2-|z_2|^2),
 \qquad (H,G)=(0,\overline z_2^3/6)
\]

solve this flat D-plus system exactly. Their torsions are respectively
\(\rho(2z_1,2z_2)\) and \(\rho(0,-\overline z_2^2)\); both solve
the negative Dirac system

\[
 D^-\tau=\bigl((A_2)_2-(A_1)_1,-B_2-(C_0)_1\bigr)=0.
\]

They give \((A_1)_1=(A_2)_2=4\rho\) and
\(\nabla_{\overline Z_2}^2\tau_2=-8\rho\), respectively.
After substituting (2.2) in (4.1), the adjoint retains the term

\[
 \frac{f}{2\kappa_0}\operatorname{Re}\left[(D-iE_0)
 \left\{\overline{(A_2)_1}\nabla_{\overline Z_1}
                          \nabla_{\overline Z_2}\tau_2
       -\overline{(A_1)_1}\nabla_{\overline Z_2}^2\tau_2\right\}\right],
\]

in addition to curvature, derivative-Weyl, cutoff and frame terms.
Here f denotes the scalar weight of that integration. Reversing the
cubic seed reverses this displayed pairing while leaving the lower
jets unchanged. Its fully symmetric third-spinor jet also leaves the
principal curvature-commutator constraints unchanged. Thus neither
the two Dirac contractions nor commuting antisymmetric derivatives
makes this symmetric symbol vanish pointwise. The exact integral
formula (3.2), not this isolated symbol, is the global identity to use.

## 5. The global condition to which the calculation must return

The same-solution characteristic localization in I41, Section 7, is

\[
 16\pi^2\int d\chi\wedge T_\tau
     =2\int\vartheta^2|W^-|^2+\int\vartheta^2 k,
\]
\[
 k=9(|F_A^+|^2-|F_A^-|^2)+s^2/24
                                -|\operatorname{Ric}^{\circ}|^2/2.
\]

Here \(\chi=1-\vartheta^2\) cuts off the fixed low-torsion transition
band. Along a putative actual zero-end sequence, the last integral
divided by V tends to 20/3. A sufficient new estimate is that the net
flux after subtracting the displayed opposite-Weyl payment has upper
limit strictly below \(20V/3\); an o(V) bound would suffice but is
stronger than necessary. Such a bound is not proved by (3.2) or (4.1).

The update is therefore precise: exact closure need not be added to
the actual bracket, and its (2,0) curvature forcing is only Ricci error.
The symmetric derivative interaction and its global signed absorption
remain unresolved. O10 stays open with the original actual supply,
class-square and normalization requirements.


END COMPLETE SOURCE


---

## Source 3: 20260928_signed_quartic_flux.md

Original path: `continuation/20260928_signed_quartic_flux.md`

SHA-256: `4b3576d9092017d48569504bf958868d17edcd961bae68af33b0a17ee263ef15`

BEGIN COMPLETE SOURCE

# Signed quartic completion of the actual torsion flux

28 September 2026. Continuation of I41, Section 7, I51, Section 2,
and the [actual torsion prolongation](20260928_actual_torsion_prolongation.md).
The calculation below reorganizes the complete global expression, rather
than dropping the symmetric Hessian term in a pointwise commutator.
It yields an exact first-derivative identity and a quantitative necessary
condition for an endpoint sequence. The final subthreshold estimate is
not derived from the original hypotheses; O10 remains open.

## 1. The actual field and the characteristic identity

Use the scalar-minus-four, constant-weight actual solution
\(D_A\Phi=0,\ F_A^+=2i\sigma(\Phi)\) of I51. Let tau be its cubic
opposite-spinor torsion, a section of \(E=S^-\otimes L\), and put
\(m=|\tau|^2,\ m_*=128/81\).
Fix \(0<a<b<m_*\) and a smooth nondecreasing function vartheta_0,
zero on [0,a] and one on [b,infinity). Write

\[
 \vartheta=\vartheta_0(m),\quad \chi=1-\vartheta^2,\quad
                         T=\{a<m<b\}.
\]

On m > 0, use a local unitary frame with first vector
u = tau/sqrt(m). Write the actual connection as

\[
 \Gamma=\begin{pmatrix}\alpha&-\bar b_1\\b_1&\alpha_2\end{pmatrix},
 \qquad \alpha=i\theta,\quad b_1=\gamma+i\delta,
\]

where theta,gamma,delta are real one-forms. The phase one-form theta
is not the scalar cutoff vartheta. All expressions with cutoff
derivatives are supported in T, bounded away from tau's zero set.

In the inherited curvature and orientation conventions, the rank-two
Chern transgression is

\[
 4\pi^2\mathcal T_\tau
 =-\alpha\wedge F_{22}
 +\tfrac12(b_1\wedge F_{12}-\bar b_1\wedge F_{21})
                         +\alpha\wedge\bar b_1\wedge b_1.
                                                               \tag{1.1}
\]

Here \(F=F^E\). Its global localization, proved in I41, is

\[
 16\pi^2\int d\chi\wedge\mathcal T_\tau
           =2\int\vartheta^2|W^-|^2+\int\vartheta^2 k,
                                                               \tag{1.2}
\]
\[
 k=9(|F_A^+|^2-|F_A^-|^2)+s^2/24-|\operatorname{Ric}^{\circ}|^2/2.
\]

The determinant connection on E is 3A. The cutoff equals one near
every zero in the localization convention; thus (1.2) is an identity
on the closed manifold, not an unaccounted boundary formula.

## 2. Removing the opposite-Weyl variable without differentiating it

Take the compatible ASD basis
\(\Omega_1=e^{12}-e^{34},\
\Omega_2=e^{13}+e^{24},\
\Omega_3=e^{14}-e^{23}\), each of squared norm two, and put
\(I_a=c^-(\Omega_a)/2\). Write
\(W^-\Omega_b=\sum_a W_{ab}\Omega_a\).
The opposite-Weyl contribution to F is

\[
 F_W=-\tfrac12\sum_{a,b}W_{ab}\Omega_b I_a.
\]

Its entries are

\[
 (F_W)_{22}=\tfrac i2\sum_bW_{1b}\Omega_b,\quad
 (F_W)_{12}=-\tfrac12\sum_bW_{2b}\Omega_b
                         +\tfrac i2\sum_bW_{3b}\Omega_b,
\]
\[
 (F_W)_{21}=\tfrac12\sum_bW_{2b}\Omega_b
                         +\tfrac i2\sum_bW_{3b}\Omega_b.
\]

The remainder \(F_0=F-F_W\) obeys
\[
 |F_0|\le C(|s|+|\operatorname{Ric}^{\circ}|+|F_A|).
\]

Set \(v_1=\theta,v_2=-\gamma,v_3=-\delta\), and define the matrix
and its symmetric trace-free part by

\[
 K_{ab}=\langle d\vartheta\wedge v_a,\Omega_b\rangle,\qquad
 M=\tfrac12(K+K^{\mathsf T})-\tfrac13(\operatorname{tr}K)I.
\]

Define actual scalar densities j_chi and q_chi by

\[
 j_\chi\,d\mu=16\vartheta\,d\vartheta\wedge\theta\wedge\gamma\wedge\delta,
 \qquad
 q_\chi=|d\vartheta|^2(|\theta|^2+|\gamma|^2+|\delta|^2).
\]

These vanish outside T. They are independent of the choice of the
unitary complement to u. Equivalently M is the trace-free symmetric
operator determined by its pairing with the intrinsic linear Weyl
term below; changes of the compatible ASD frame conjugate that
operator. No derivative of a chosen eigenvector of W is used.

Direct substitution in (1.1), using star Omega_b = -Omega_b, gives

\[
 4\pi^2(\mathcal T_\tau)_W
       =\tfrac12\sum_{a,b}W_{ab}v_a\wedge\Omega_b,\quad
 4\pi^2(\mathcal T_\tau)_{\mathrm{cubic}}
                                  =-2\theta\wedge\gamma\wedge\delta,
\]
\[
 16\pi^2d\chi\wedge(\mathcal T_\tau)_W
                       =4\vartheta\langle M,W^-\rangle\,d\mu.
\]

Consequently define the explicit lower-curvature remainder

\[
 R_\chi=4\int d\chi\wedge\left[
 -\alpha\wedge(F_0)_{22}
 +\tfrac12\{b_1\wedge(F_0)_{12}-\bar b_1\wedge(F_0)_{21}\}\right].
\]

All imaginary coefficients combine into a real integral. Completing
the square in (1.2) now gives the exact global identity

\[
 \boxed{\int\vartheta^2k
 =\int\{j_\chi+2|M|^2-2|\vartheta W^--M|^2\}+R_\chi.}     \tag{2.1}
\]

No second derivative of tau or curvature remains. In particular this
does not assert that the Hessian in the earlier adjoint identity was
pointwise zero; it combines the entire characteristic flux instead.
For every epsilon > 0, Young's inequality gives

\[
 |R_\chi|\le\varepsilon\int q_\chi
 +\frac C\varepsilon\int_T
       (s^2+|\operatorname{Ric}^{\circ}|^2+|F_A|^2).       \tag{2.2}
\]

Indeed its absolute integrand is bounded by
C vartheta |d vartheta| (|theta|+|b_1|)|F_0|.
All cutoff derivatives have been retained.

More explicitly, with the Hilbert--Schmidt norm on End(E), orthogonality
of the curvature blocks gives
\[
 |F_0|^2=s^2/48+|\operatorname{Ric}^{\circ}|^2/4+(9/2)|F_A|^2.
\]
The direct transgression bound is
\(|R_\chi|\le8\int\vartheta|F_0|\sqrt{q_\chi}\). Thus the second
term of (2.2) can be replaced by
\[
 \frac1\varepsilon\int_T\vartheta^2
           \{s^2/3+4|\operatorname{Ric}^{\circ}|^2+72|F_A|^2\}.
\]
These explicit coefficients are sufficient upper bounds, not a claim
of optimal constants.

## 3. A topological curvature budget and the precise threshold

For a fixed sigma > 0 put

\[
 p_{\chi,\sigma}=j_\chi+
                   \frac{4\vartheta^2}{2\vartheta^2+\sigma}|M|^2,
 \quad
 \mathcal S_\sigma=\int(2\vartheta^2+\sigma)
        \left|W^--\frac{2\vartheta M}{2\vartheta^2+\sigma}\right|^2.
\]

At sigma = 0 use \(p_{\chi,0}=j_\chi+2|M|^2\) and
\(\mathcal S_0=2\int|\vartheta W^--M|^2\).
The exact refinement of (2.1) is

\[
 \boxed{\int\vartheta^2k
    =\int p_{\chi,\sigma}+\sigma\int|W^-|^2
                                  -\mathcal S_\sigma+R_\chi.}   \tag{3.1}
\]

For each fixed positive sigma this is the optimal pointwise quadratic
upper bound if W is allowed to range over arbitrary trace-free symmetric
matrices: the square vanishes at
W = 2 vartheta M/(2 vartheta squared + sigma).
This algebraic statement is not a claim of geometric realizability,
or of dual attainment under an arbitrary specified global budget.

Now suppose there were an actual endpoint sequence with beta tending
to infinity, eta = r + D_beta/V + beta to the power minus two tending
to zero, and the Spin-c class-square condition \(\mathfrak a^2\ge T_+\).
Use normalized integrals throughout this paragraph. From I51 (2.5),
rho tends in L2 to 4/3 and the harmonic-projection remainder
J_H/V tends to zero. The *actual* Hodge identity is

\[
 4\pi^2p=\int|F_A^+|^2-J_H=\tfrac12\int\rho^2-J_H,
 \qquad p/V\longrightarrow\frac2{9\pi^2}.                \tag{3.2}
\]

This is not obtained by dropping beta times the Weyl energy from
the formula for D_beta.
The bounded ASD fitted model of I51 (2.14a), the actual torsion-amplitude
estimate, and s = -4 yield

\[
 \frac1V\int_T(s^2+|\operatorname{Ric}^{\circ}|^2+|F_A|^2)\to0,
 \qquad
 \frac1V\int\vartheta^2k\to20/3.                         \tag{3.3}
\]

For completeness, the entire low-amplitude set {m < b}, hence also
the transition, has relative volume tending to zero;
rho is bounded; the Ricci error tends to zero in normalized L2;
and \(F_A^-\) differs from a bounded field by o(sqrt(V)) in L2.
The full averages of \(|F_A^+|^2,|F_A^-|^2\) tend respectively to
8/9 and 2/9. These prove both assertions in (3.3), without a
pointwise Ricci estimate.

Assume also p >= A > 0 and chi(M)/A <= B, B >= 0. Chern--Gauss--Bonnet
and (3.2) imply

\[
 \frac{\|W^-\|_2^2}{V}
 \le8\pi^2B\,p/V-\frac23+\frac r2,\qquad
 \limsup\frac{\|W^-\|_2^2}{V}\le
                          \Lambda_B=\frac{16B}{9}-\frac23.     \tag{3.4}
\]

If B < 3/8 this alone contradicts nonnegativity along such a sequence.
For B >= 3/8, (2.2)--(3.4) prove the necessary condition

\[
 \boxed{\liminf_j\left\{
     \fint_j(p_{\chi,\sigma}+\varepsilon q_\chi)
                              +\sigma\Lambda_B\right\}\ge20/3}
                                                               \tag{3.5}
\]

for every *fixed* sigma >= 0 and epsilon > 0. Therefore any actual
subthreshold bound by 20/3 minus a fixed positive amount, for one such
pair, excludes that endpoint sequence.

This asks for a strict subthreshold estimate, not necessarily o(V)
critical energy. The earlier condition that the mixed transition
density is o(V) implies it with sigma = 0, since on the fixed band

\[
 |j_\chi|+|M|^2+q_\chi
           \le C|\langle\tau,\nabla\tau\rangle|^2|\nabla\tau|^2.
\]

No example establishing a strict inclusion between classes of actual
closed solutions is claimed. Most importantly, the original endpoint
budgets do not yet imply this subthreshold estimate.

## 4. The remaining cubic form can be tested globally

The first-derivative density in (2.1) is not an independent topological
constant. Its further Stokes test can also be made exact.
The three-form theta wedge gamma wedge delta is invariant under a
change of complement to u; after multiplication by vartheta squared
it extends smoothly by zero through the zero set of tau. Thus

\[
 \int j_\chi=-8\int\vartheta^2d(\theta\wedge\gamma\wedge\delta).
                                                               \tag{4.1}
\]

Write \(\alpha_2=i\theta_2\),
\(f_{11}=-iF_{11},\ p_{21}=\operatorname{Re}F_{21},\
q_{21}=\operatorname{Im}F_{21}\).
The full U(2) structure equations give

\[
 d\theta=f_{11}+2\gamma\wedge\delta,\quad
 d\gamma=p_{21}+(\theta_2-\theta)\wedge\delta,\quad
 d\delta=q_{21}-(\theta_2-\theta)\wedge\gamma.
\]

The complement connection terms cancel, leaving

\[
 d(\theta\wedge\gamma\wedge\delta)
 =f_{11}\wedge\gamma\wedge\delta-\theta\wedge p_{21}\wedge\delta
                                   +\theta\wedge\gamma\wedge q_{21}.
                                                               \tag{4.2}
\]

Let L be the matrix whose three rows pair
\((\gamma\wedge\delta,\theta\wedge\delta,-\theta\wedge\gamma)\)
with Omega_b, and let L_0 be its symmetric trace-free part.
The W-minus part of (4.2) is
\(\tfrac12\langle W^-,L_0\rangle d\mu\).
Define R_bulk to be -8 times the integral of vartheta squared times
the right side of (4.2) with F replaced by F_0. Then

\[
 \int j_\chi=-4\int\vartheta^2\langle W^-,L_0\rangle+R_{\mathrm{bulk}}.
\]

Put H = M-vartheta L_0. A second exact completion gives

\[
 \boxed{\int\vartheta^2k
     =2\int|H|^2-2\int|\vartheta W^--H|^2
                                     +R_\chi+R_{\mathrm{bulk}}.} \tag{4.3}
\]

Here R_bulk is supported on the entire nonzero-amplitude region,
not merely T. Its calibrated scalar and determinant terms need not be
small. Equation (4.3) therefore does not erase the critical payment:
it moves it to curvature paired with squared derivatives of the unit
torsion in the bulk. Declaring R_bulk to be o(V) on the basis of
(3.3), which only concerns T, would be incorrect.

The two exact forms (2.1) and (4.3) are alternative global tests of
the same actual field. A proof of (3.5)'s strict reverse bound, or a
controlled signed cancellation in (4.3), is still required to settle
O10. Neither identity supplies a global escape sequence.

## 5. Retaining the non-small calibrated bulk curvature

The bulk remainder in (4.3) can be expanded instead of being estimated
as an unspecified error. In the same actual compatible frame put
\[
 F_*=i(\Omega_++\tfrac12\Omega_1)I
                               +\tfrac16\sum_a\Omega_a I_a.
\]
Here Omega_+ is the unit-length-squared-two direction of the actual
positive spinor. The actual amplitude and ASD fit imply
\[
 \fint_{\{m\ge a\}}|F_0-F_*|^2\longrightarrow0.
\]
The integral is normalized by the full volume. This follows from
rho tending to 4/3, the bounded fitted ASD curvature coefficient tending
to 1/3 in the tau-adapted direction, and the vanishing Ricci error.
It does not provide smallness after multiplication by an uncontrolled
quadratic derivative.

In (4.2), the entries of F_* are
\[
 f_{11}^*=\Omega_++\tfrac23\Omega_1,\quad
 p_{21}^*=-\Omega_2/6,\quad q_{21}^*=-\Omega_3/6.
\]
Their contribution to R_bulk is the integral of vartheta squared times
\[
 q_*=-8\langle\gamma\wedge\delta,\Omega_+\rangle
       +\tfrac{16}{3}\langle\gamma\wedge\delta,\Omega_1\rangle
       +\tfrac43\langle\theta\wedge\delta,\Omega_2\rangle
       -\tfrac43\langle\theta\wedge\gamma,\Omega_3\rangle.
\]

For \(u=\tau/\sqrt m\), the exact quadratic identity is
\[
 \boxed{q_*=\tfrac{20}{3}|\nabla u|^2-2|\theta|^2
       -8|(\nabla u)^{1,0}|^2-\tfrac23|D^-u|^2
                                    -2|\delta-J_-\gamma|^2.}   \tag{5.1}
\]
Here J_- sends e_1 to e_2 and e_3 to -e_4, and the (1,0) projection
uses the actual positive-spinor almost-complex structure. The tensor
norm includes the factor one half for evaluation on Z_1,Z_2.
One verifies (5.1) from
\[
 2|(\nabla u)^{1,0}|^2-|\nabla u|^2
                               =2\langle\gamma\wedge\delta,\Omega_+\rangle,
\]
\[
 |D^-u|^2=|\nabla u|^2-2\operatorname{tr}L,\qquad
 2\langle\gamma\wedge\delta,\Omega_1\rangle
             =|\gamma|^2+|\delta|^2-|\delta-J_-\gamma|^2.
\]

The residual calibration error is exactly (4.2) with F_0-F_*,
and its absolute value is at most
\[
 C\int\vartheta^2|F_0-F_*|
       (|\gamma\wedge\delta|+|\theta\wedge\gamma|+|\theta\wedge\delta|).
                                                               \tag{5.2}
\]
The curvature factor is small in normalized L2; the other factor is
quadratic in the actual unit derivative and has no inherited L2 bound.
Also
\[
 D^-u=m^{-1/2}D^-\tau-\frac1{2m}c^-(dm)u.
\]
Hence the radial term cannot be discarded using weak Dirac control of
tau alone. Equations (5.1)--(5.2) retain both the non-small calibrated
potential and the exact critical error. No strict bound below 20V/3
has been established from them.

## 6. Exact cancellation of the central and scalar curvature payments

The determinant part of (5.2) need not be bounded in absolute value.
There is a further global cancellation. It removes that derivative
payment exactly, but also removes the positive characteristic budget;
both changes must be retained.

Write h = vartheta squared = 1 - chi and decompose the actual curvature
on E as
\[
 F^E=F_W+F_s+F_R+i c I,\qquad
 c=\tfrac32(-iF_A),\quad dc=0,\quad
 F_s=\tfrac16\sum_a\Omega_a I_a.
\]
The scalar is exactly -4 in the normalization used throughout this
calculation. The Ricci block has the form
\[
 F_R=\begin{pmatrix}ir&-p+iq\\p+iq&-ir\end{pmatrix},
 \qquad r,p,q\in\Lambda^+,
 \qquad |F_R|_{\mathrm{HS}}^2=\tfrac14|\operatorname{Ric}^{\circ}|^2.
\]
These letters r,p,q are real two-forms in this section, not a radial
coordinate, a monopole budget or an error norm. Set
\[
 x_b=\tfrac12\langle c^-,\Omega_b\rangle,\qquad
 C=\operatorname{STF}(e_1\otimes x),\qquad
 f_{11}=-iF^E_{11}
   =c-\tfrac12\sum_bW_{1b}^-\Omega_b+\Omega_1/6+r.
\]
The first structure equation is
\(d\theta=f_{11}+2\gamma\wedge\delta\).

For any curvature block G define the real three- and four-forms
\[
 S(G)=-\alpha\wedge G_{22}
       +\tfrac12(b_1\wedge G_{12}-\overline b_1\wedge G_{21}),
\]
\[
 B(G)=(-iG_{11})\wedge\gamma\wedge\delta
       -\theta\wedge\operatorname{Re}G_{21}\wedge\delta
       +\theta\wedge\gamma\wedge\operatorname{Im}G_{21}.
\]
Only the displayed actual blocks, for which these expressions are real,
are used. Put
\(R_\chi(G)=4\int d\chi\wedge S(G)\) and
\(R_b(G)=-8\int hB(G)\).

### 6.1 The central block

Here S(icI) = theta wedge c and B(icI) = c wedge gamma wedge delta.
The one-form theta is intrinsically determined by the actual unit
section u; multiplication by h extends it smoothly by zero near
tau = 0. Since dc = 0, Stokes gives
\[
 \int d(h\theta\wedge c)=0,
 \qquad
 \boxed{R_\chi(icI)+R_b(icI)=4\int h c\wedge f_{11}.}     \tag{6.1}
\]
Indeed the two gamma wedge delta terms cancel exactly. No norm of
the derivative of c or any smallness of c has been used.

### 6.2 The scalar block and the full cutoff term

All spinor pairings below are the real parts of Hermitian pairings,
conjugate-linear in the first entry. Define
\[
 X_h=\operatorname{Re}\int
        \langle D^-u,c^-(dh)u\rangle.
\]
The exact weighted Lichnerowicz identity is
\[
 \int h|D^-u|^2+X_h
      =\int h|\nabla u|^2-\int h(1+2x_1).                \tag{6.2}
\]
The scalar potential is -1, and the central ASD curvature acts on
u = e_1 by -2x_1. The Ricci block is self-dual and gives no Dirac
potential on this negative spinor. There is no gradient-cutoff term
from the connection Laplacian because \(|u|=1\), so its pairing
with the derivative of u has zero real part.

With the Clifford matrices fixed in the preceding actual-prolongation
proof and \(\nabla u=(i\theta,\gamma+i\delta)\), finite Clifford
algebra gives
\[
 X_h=\int\sum_a\langle dh\wedge v_a,\Omega_a\rangle,
                     \qquad v=(\theta,-\gamma,-\delta).
\]
In particular the cutoff term is not omitted. Direct evaluation yields
\[
 S(F_s)=-\tfrac16\sum_a v_a\wedge\Omega_a,
 \quad R_\chi(F_s)=-\tfrac23 X_h,
 \quad R_b(F_s)=\tfrac23\int h(|\nabla u|^2-|D^-u|^2).
\]
Using (6.2),
\[
 \boxed{R_\chi(F_s)+R_b(F_s)=\tfrac23\int h(1+2x_1).}    \tag{6.3}
\]
This step does not assume D^-tau = 0 or discard the radial part
of D^-u.

Equivalently, the entire scalar contribution is
\(\tfrac23(\|\nabla(\vartheta u)\|_2^2
-\|D^-(\vartheta u)\|_2^2)\). Apply Lichnerowicz to the
globally smooth section vartheta u, which vanishes in a neighborhood
of the zero set. The two cutoff-gradient squares cancel. This gives
the same formula without requiring u itself to extend through that set.

### 6.3 The remaining Ricci interaction and the lost positive budget

Since the Omega_a are anti-self-dual,
\[
 4c\wedge f_{11}
 =4c\wedge c+
     (4\langle W^-,C\rangle-\tfrac43x_1)d\mu
       +4c\wedge r.
\]
The x_1 term cancels with (6.3). Moreover the characteristic density
in Section 1 is exactly
\[
                 k=4\frac{c\wedge c}{d\mu}
                      +\tfrac23-\tfrac12|\operatorname{Ric}^{\circ}|^2.
\]
Substitute these two equalities into (4.3), and put
\(\widetilde H=M-\vartheta L_0+\vartheta C\). The result is
\[
\boxed{\begin{split}
 0={}&2\int|\widetilde H|^2
       -2\int|\vartheta W^--\widetilde H|^2
       +\mathcal R_R\\
     &+4\int h c\wedge r
       +\tfrac12\int h|\operatorname{Ric}^{\circ}|^2,
\end{split}}                                                    \tag{6.4}
\]
where the sole derivative-curvature payment is
\[
\begin{split}
 \mathcal R_R={}&4\int dh\wedge
          (\theta\wedge r+\gamma\wedge p+\delta\wedge q)\\
 &-8\int h\{r\wedge\gamma\wedge\delta
       -\theta\wedge p\wedge\delta+\theta\wedge\gamma\wedge q\}.
\end{split}                                                     \tag{6.5}
\]
All wedge products are actual global contractions of the adapted
connection expressions; frame changes preserve the paired integral.
The last two terms in (6.4) are o(V) along the endpoint sequence:
c has bounded normalized L2 norm and Ricci trace-free error tends to
zero in that norm. This observation does not apply to (6.5), which
contains squared derivatives of the unit field.

Thus the determinant-error product in (5.2) has been removed globally,
not estimated. The whole positive 20V/3 budget has also disappeared
into the central and scalar identities. Even a proof that
\(\mathcal R_R=o(V)\) would give equality of the two square norms
in (6.4), not a contradiction. The missing statement must be a strict
signed separation compatible with the actual cubic provenance and
bracket, or a joint estimate of that separation and (6.5). These
identities hold for a general unit section on the cutoff support;
their validity alone does not exploit all of those additional actual
field equations. No unrestricted endpoint gap follows.

### 6.4 A single intrinsic mixed-curvature pairing

The remaining terms can be combined without taking absolute values.
Let Psi_b be the compatible positive two-form basis with squared norm
two, and write
\[
 F_R=-\tfrac12\sum_{a,b}\mathsf R_{ab}\Psi_b I_a,
 \qquad |\mathsf R|^2=\tfrac14|\operatorname{Ric}^{\circ}|^2.
\]
Use the full three-by-three matrices
\[
 K^+_{ab}=\langle d\vartheta\wedge v_a,\Psi_b\rangle,
 \quad L^+_{ab}=\langle A_a,\Psi_b\rangle,
 \quad A=(\gamma\wedge\delta,\theta\wedge\delta,-\theta\wedge\gamma),
\]
\[
 y_b=\tfrac12\langle c^+,\Psi_b\rangle,
 \qquad H^+=K^+-\vartheta L^++\vartheta(e_1\otimes y).
\]
For the actual monopole \(c^+=(3\rho/4)\Omega_+\), so
\(y=(3\rho/4,0,0)\) in this frame. In contrast with
\(\widetilde H\), H^+ is **not** projected to its symmetric
trace-free part. The mixed curvature is a map between the two
different handed two-form bundles.

Substitution into (6.5), using self-duality for the positive wedge
products, gives exactly
\[
 \mathcal R_R+4\int h c\wedge r
                         =-4\int\vartheta\langle\mathsf R,H^+\rangle.
\]
Hence the final identity is
\[
 \boxed{\|\vartheta W^--\widetilde H\|_2^2
                 -\|\widetilde H\|_2^2
       =\|\vartheta\mathsf R\|_2^2
                    -2\int\vartheta\langle\mathsf R,H^+\rangle.} \tag{6.6}
\]
This retains the sign, the cutoff and every curvature block. H^+
contains quadratic unit-field derivatives; no uniform normalized L2
bound for it follows from the stated budgets. Moreover vanishing of
the right side would still force only a zero square difference.
The next sufficient estimate must establish a strictly signed
separation using the cubic field equations, jointly with the mixed
pairing. Equation (6.6) is the current exact continuation point,
not an added field equation or a completed endpoint theorem.

Testing the unnormalized actual tau does not restore a discarded radial
coercivity in this channel. Put \(\lambda=dm/(2m)\) and use the
smooth weight h/m, extended by zero. Substituting
\(\nabla\tau=\sqrt m(\nabla u+\lambda\otimes u)\),
\(D^-\tau=\sqrt m(D^-u+c^-(\lambda)u)\) into weighted
Lichnerowicz adds the identical term
\(-\int h|\lambda|^2+\int\langle dh,\lambda\rangle\)
to both sides of (6.2). It cancels exactly. Thus a repeated scalar
test of tau is not a missing source of a positive length-gradient
term; the additional cubic and bracket information must enter the
signed curvature identity itself.

## 7. The cubic actual core does not supply the missing signed separation

The next test uses the actual fixed-hyperbolic, weight-two monopole
solutions of [I41, Section 15.1](20260927_conformal_separation_and_zero_end.md),
not independently assigned spinor jets. Normalize their simple torsion
zero so that, on shrinking mass shells, the physical field has leading
term

\[
 \tau=(\overline z_1,\overline z_2)/\ell,
 \qquad m=|\tau|^2=r^2/\ell^2,
 \qquad \rho\longrightarrow\rho_*=4/3.
 \tag{7.1}
\]

Fixed constant factors in the original construction scale are absorbed
into ell. All following limits concern a fixed interval \(0<a<b<128/81\) in
m and the C1 rescaled expansions of that actual construction. The
metric is exactly hyperbolic: \(\operatorname{Ric}=-g\), \(W^-=0\) and
\(\mathsf R=0\). Thus the two sides of (6.6) vanish identically,
even though the actual cubic bracket is present. Its validity alone
cannot supply a strictly positive local square separation.

There is a quantitative version which retains the full cutoff. Set
\(\vartheta=\vartheta_0(m)\), with values zero and one near the two
ends of the shell. At \(x=(r,0,0,0)\), the leading unit-field forms are

\[
 \theta=-e^2/r,\qquad \gamma=e^3/r,\qquad\delta=-e^4/r.
\]

Using the compatible two-form frames of Section 6, direct substitution
gives the frame-invariant leading norms

\[
 |\widetilde H|^2=\frac{8}{3r^4}(r\vartheta_r+\vartheta)^2,
 \qquad |H^+|^2=\frac{3}{r^4}(r\vartheta_r-\vartheta)^2.
\]

The central bounded terms contribute o(1) to their shell integrals.
Since \(r\vartheta_r=2m\vartheta_0'\), the limits are

\[
 E_-:=\lim\int_{a<m<b}|\widetilde H|^2
   =\frac{8\pi^2}{3}\int_a^b(2m\vartheta_0'+\vartheta_0)^2\frac{dm}{m},
\]
\[
 E_+:=\lim\int_{a<m<b}|H^+|^2
   =3\pi^2\int_a^b(2m\vartheta_0'-\vartheta_0)^2\frac{dm}{m}.
 \tag{7.2}
\]

Subtracting and using the endpoint values proves the exact relation
and sharp cutoff infima

\[
 E_- -\frac89 E_+=\frac{32\pi^2}{3},\qquad
 \inf E_-=\frac{32\pi^2b}{3(b-a)},\qquad
 \inf E_+=\frac{12\pi^2a}{b-a}. \tag{7.3}
\]

Indeed, writing \(\vartheta_0=\sqrt m\,v\) makes the E-plus integral
\(12\pi^2\int_a^b m^2(v')^2dm\), with
\(v(a)=0\), \(v(b)=1/\sqrt b\). Weighted Cauchy gives its infimum;
the minimizing profile is
\(\vartheta_0(m)=(m-a)\sqrt b/[(b-a)\sqrt m]\).
Smooth flattening near the endpoints approaches it. This is a shell
cost calculation, not a lower bound for the original Einstein defect.

To test whether these shells are already excluded by the actual
calibrated field fit, use I51's bounded model. Here
\(S=m_*+m+o(1)\), \(m_*=128/81\), the actual ASD determinant curvature
f is O(ell), and

\[
 K=\frac{2m}{3(m_*+m)}\Omega_-+o(1),\qquad |\Omega_-|^2=2.
\]

Consequently

\[
 \int_{a<m<b}|f-K|^2
  =\frac{8\pi^2\ell^4}{9}\int_a^b\frac{m^3}{(m_*+m)^2}\,dm
     +o(\ell^4),
\]
\[
 \int_{a<m<b}|\nabla\tau|^2
       =2\pi^2\ell^2(b^2-a^2)+o(\ell^2). \tag{7.4}
\]

Thus the actual fit pays volume scale and the quadratic derivative
budget pays scale squared, while the two critical norms in (7.2)
retain nonzero limits. These local actual solutions remain compatible
with those subcritical budgets under shrinking. Their complete
boundary matching and global conformal/weight supply are not proved.
They neither close O10 nor constitute a closed escape sequence.

The useful consequence for the next proof is precise: a strict
separation must use information carried by the calibrated exterior
and its matching with these cores, or another full-system identity.
The actual cubic bracket on a core, by itself, does not restore the
positive budget cancelled in Section 6. No universal estimate for the
mixed Ricci term follows from the cutoff infima (7.3).


END COMPLETE SOURCE
