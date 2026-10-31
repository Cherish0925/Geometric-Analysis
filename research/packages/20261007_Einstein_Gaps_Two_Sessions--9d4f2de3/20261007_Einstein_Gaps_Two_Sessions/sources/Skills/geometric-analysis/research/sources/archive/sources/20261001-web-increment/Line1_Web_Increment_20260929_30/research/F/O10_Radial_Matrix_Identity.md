# O10: the complete radial one-form and the sign of its energy identity

Date: 2026-09-30. This note addresses the unrestricted endpoint. It does not improve a decay-rate exponent or claim the endpoint is solved. The complete radial component is retained throughout.

## 1. A genuinely global polynomial object

Let \(E=S^-\otimes L\), \(\det E=L^3\), and use the actual bounded auxiliary section \(v\). Define
\[
 \mathcal B=v\wedge\nabla v\in\Omega^1(L^3).
\]
No division, moving frame, or lower-amplitude cutoff is needed for this definition. If \(L_E=\nabla^*\nabla\), then the exact identities are
\[
 \delta_{3A}\mathcal B=v\wedge L_Ev,
 \tag{1}
\]
\[
 (d_{3A}\mathcal B)_{ij}
 =2\nabla_i v\wedge\nabla_jv+v\wedge F^E_{ij}v.
 \tag{2}
\]
The repeated derivative term in (1) vanishes because each \(\nabla_i v\wedge\nabla_i v=0\). In (2), the exterior derivative is antisymmetric in \(i,j\).

The actual endpoint estimates therefore give
\[
 \|\mathcal B\|_{2,\rm av}\le C,
 \qquad \|\delta_{3A}\mathcal B\|_{2,\rm av}\to0.
 \tag{3}
\]
The self-dual part of \(v\wedge F^Ev\) is \(L^2\)-small: the traceless self-dual block of the negative spin connection is controlled by \(\operatorname{Ric}^{\circ}\), and the central determinant-curvature term wedges with \(v\) to zero. The remaining quadratic term in (2) is only uniformly \(L^1\) under the unrestricted hypotheses. Equations (1)–(3) are actual global statements, not formal limiting equations.

## 2. Local exact model retaining the radial variables

The following local formulas are the exact zero-error first-jet calculation. They must not be used to discard derivative errors in an actual weak sequence without testing them.

Use \(\rho=\rho_*=4/3\), \(m=|v|^2>0\), and set
\[
 u={dm\over2m},\quad z=u_1-iu_2,\quad
 q=(u_2,-u_1,u_4,-u_3),\quad d=-(u_3+iu_4).
\]
In the adapted frame, the complete phase/Dirac relations give
\[
 b=d\theta_1+c\theta_2,
 \qquad \theta_1=e^1-ie^2,\quad\theta_2=e^3-ie^4,
 \qquad \mathcal B=mb.
 \tag{4}
\]
Thus \(d\) is not set to zero. Write
\[
 \Psi_1=e^{12}+e^{34},\quad
 \Xi_+=e^{13}-e^{24}+i(e^{14}+e^{23}),
\]
so \(\overline{\Xi_+}=\theta_1\wedge\theta_2\), and both are self-dual. The exact Cartan formulas are
\[
 d\theta_1=-i(\mathfrak a-q)\wedge\theta_1
                 +\kappa\Xi_+-d\overline{\Xi_+},
\]
\[
 d\theta_2=i(2\mathfrak a-q)\wedge\theta_2
                 -\bar c\Xi_- -2i\bar d\,e^{12},
 \qquad \kappa={\sqrt m\over2\rho_*^{3/2}}.
\]
Here \(A=i\mathfrak a\), and \(\Xi_-\) is the anti-self-dual form used in the preceding continuation.

Since the off-diagonal connection curvature is
\(F^E_{21}=d_{3A}b-2iq\wedge b\), (2) becomes
\[
 d_{3A}^+\mathcal B
 =m(F^E_{21})^++2m\bigl((u+iq)\wedge b\bigr)^+.
\]
The elementary wedge computation gives
\[
 \boxed{d_{3A}^+\mathcal B
 =m(F^E_{21})^++2m(d^2+c\bar z)\overline{\Xi_+}.}
 \tag{5}
\]
Also \(\delta_{3A}b=2u\mathbin{\lrcorner}b\) is precisely the off-diagonal component of \(L_Ev=2v\), so (1) yields \(\delta_{3A}\mathcal B=0\) in this zero-error model.

The complete off-diagonal self-dual curvature equation itself is
\[
 \begin{split}
 (F^E_{21})^+={}&\mathcal L_1(D_2d-iqd)
              +\mathcal L_2(D_5c-3iqc)\\
 &+\kappa d\Xi_+-d^2\overline{\Xi_+}
              -ic\bar d\Psi_1,
 \end{split}
 \tag{6}
\]
where \(\mathcal L_a(\alpha)=(\alpha\wedge\theta_a)^+\). Thus the \(d\)-equation and \(c\)-equation are coupled; the original fifth-line CR equation results only after a justified removal of the radial terms.

For example, taking \(D=m^{-3/2}d\), \(C=m^{-3/2}c\) cancels the \(d^2\overline{\Xi_+}\) terms but leaves
\[
 m^{-3/2}(F^E_{21})^+
 =\mathcal L_1(D_2D)+\mathcal L_2(D_5C)
       +\kappa D\Xi_+ +2i(C\bar d-Dz)\Psi_1.
 \tag{7}
\]
The last radial transport term does not vanish. The expressions with negative powers of \(m\) in (7) are only local on \(m>0\); they are not an independently global replacement for \(\mathcal B\).

## 3. The integrated operator has one negative potential direction

For a unitary line bundle \(K\), write \(F=-iF^K\) for its real curvature and use its matrix action \((F\alpha)_j=F_{jk}\alpha_k\). On line-valued one-forms, the ASD deformation Weitzenböck formula is
\[
 \delta_K^*\delta_K+2(d_K^+)^*d_K^+
 =\nabla_K^*\nabla_K+\operatorname{Ric}-2iF^-.
 \tag{8}
\]
It follows by adding \(d_K^**d_K\) to the Hodge Laplacian: the line-curvature terms are respectively \(+i*F\) and \(-iF\), hence \(-2iF^-\). Only Ricci, not the full tangent curvature, appears in (8).

In the endpoint model the real curvature of \(L^3\) has
\[
 F_{L^3}^-=\Omega_-=e^{12}-e^{34},\qquad\operatorname{Ric}=-g.
\]
Since \(\Omega_-\theta_1=-i\theta_1\) and \(\Omega_-\theta_2=i\theta_2\), the zero-order operator in (8) has eigenvalues
\[
 \boxed{-3\text{ on }\theta_1,\qquad +1\text{ on }\theta_2.}
 \tag{9}
\]
Consequently, the integrated identity has the explicit model form
\[
 \int\bigl(|\delta_{3A}\mathcal B|^2+2|d_{3A}^+\mathcal B|^2\bigr)
 =\int\bigl(|\nabla\mathcal B|^2
           -6m^2|d|^2+2m^2|c|^2\bigr).
 \tag{10}
\]
For a genuine approximate sequence, retain the additional exact curvature-model error pairing
\[
 \int\operatorname{Re}\langle
   (\operatorname{Ric}+g-2i(F_{L^3}^--\Omega_-))\mathcal B,
        \mathcal B\rangle.
 \tag{11}
\]
That error is not automatically small: the coefficient is \(L^2\)-small, but \(\mathcal B\) is presently only bounded in \(L^2\). An \(L^4\) bound or a separately justified bounded-test formulation would be required to discard (11).

In (5), \(|\overline{\Xi_+}|^2=4\). Hence with vanishing curvature error,
\[
 2|d_{3A}^+\mathcal B|^2=32m^2|d^2+c\bar z|^2.
 \tag{12}
\]
The left side is thus a radial quartic term; setting it equal to zero before controlling the radial variables would assume the missing conclusion.

## 4. The unavoidable normal derivative energy is insufficient for positivity

Because \(\mathcal B\) is of the \(\theta_1,\theta_2\) type, its covariant derivative has an opposite-type component determined by the positive spinor connection. That component cannot be cancelled by differentiating \(d,c\).

The Clifford-to-Cartan calculation gives
\[
 (\nabla\theta_1)^{\rm opp}=\kappa\bar\theta_1\otimes\bar\theta_2,
 \qquad
 (\nabla\theta_2)^{\rm opp}=-\kappa\bar\theta_1\otimes\bar\theta_1.
\]
Since both \(\theta_a\) have squared norm two,
\[
 \boxed{|(\nabla\mathcal B)^{\rm opp}|^2
       =4m^2\kappa^2(|d|^2+|c|^2).}
 \tag{13}
\]
For variable \(m\), adding this forced normal part to the potential gives exactly
\[m^2(m/\rho_*^3-6)|d|^2+m^2(m/\rho_*^3+2)|c|^2.\]
At the frozen zeroth-order value \(m=m_*\), \(\kappa^2=1/6\), so the coefficients become
\[
 -{16\over3}m^2|d|^2+{8\over3}m^2|c|^2.
 \tag{14}
\]
In particular the radial coefficient remains negative throughout the lower-well range \(0<m\le m_*\). Freezing this coefficient is only a sign check, not an assertion that a variable-amplitude sequence has \(dm=0\), and no coefficient replacement under an uncontrolled derivative-energy integral is used. It therefore does not yield coercivity of the complete radial system. This coefficient calculation directly rules out the proposed shortcut in which the forced normal energy alone pays the entire negative radial potential.

## 5. Combining with the scalar mass equation does not yet supply the missing sign

Let \(E_1=m_1^2+m_2^2\), \(E_2=m_3^2+m_4^2\). The same complete first-jet system gives
\[
 |\nabla v|^2={E_1+2E_2\over2m}+2m|c|^2.
\]
Integrating \(\Delta m=4m-2|\nabla v|^2\) against \(m\), with the positive Laplacian convention, yields
\[
 2\int E_1+3\int E_2+4\int m^2|c|^2=4\int m^2.
 \tag{15}
\]
Also \(6m^2|d|^2=(3/2)E_2\). Eliminating the \(c\)-mass from the potential in (10) using (15) gives
\[
 \int(-6m^2|d|^2+2m^2|c|^2)
 =\int(2m^2-E_1-3E_2).
 \tag{16}
\]
The radial energies in (16) have the wrong sign for an immediate positive lower bound. The quartic term (12), the remaining same-type derivatives of \(\mathcal B\), and the actual error pairing (11) have not been controlled by a new compensating inequality. No sign has been assigned to them without proof.

## 6. Exact outcome of this attempt

The polynomial \(\mathcal B\) packages \(d\) and \(c\) globally and has a curvature identity free of an explicit \(W^-\) term. Its integrated operator nonetheless retains a negative radial potential. The forced normal derivative calculation and the mass identity do not remove that negative direction.

Moreover, the curvature-free appearance of (8) must not be confused with an available uniformly bounded inverse on line-valued one-forms. Rough Hessian estimates for such test one-forms involve the full tangent-bundle curvature, and the zero-order operator in (8) is indefinite. Importing the scalar-line resolvent bounds without proving these new bounds would be invalid.

Thus the unrestricted O10 gap is not closed here. The exact unproved compensation is the radial term in (16), together with the quartic source (12) and the error pairing (11). The preceding double-weighted scalar-line tests remain valid, but do not by themselves estimate those terms. All fixed-amplitude cutoffs applied to \(d,c\) introduce their usual transition derivatives; using the global polynomial \(\mathcal B\) avoids such divisions in (1)–(3), rather than asserting their errors vanish.
