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
