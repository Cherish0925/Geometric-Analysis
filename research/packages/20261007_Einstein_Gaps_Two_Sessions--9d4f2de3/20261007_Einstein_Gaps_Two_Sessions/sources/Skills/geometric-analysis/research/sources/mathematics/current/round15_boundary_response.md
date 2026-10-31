# Exact throat response and the missing exterior equation

## 1. Boundary variables and operators

Fix the Einstein product collar
\[
 (-R,R)\times S^1\times F,
 \quad g_0=dt^2+a(t)^2d\phi^2+h_F,
 \quad a=c\cosh(kt),\quad K(h_F)=-k^2.
\]
Write \(\kappa=a'/a\), \(f=\operatorname{sech}^2(kt)\),
\(a_R=a(R)\), \(f_R=f(R)\), \(\kappa_R=k\tanh(kR)\), and
\[
 \begin{split}
 L_wv&=-\frac1{2a}(av')'+(2\kappa^2-k^2)v,\\
 L_sv&=-\frac1{2a}(av')'.
 \end{split}                                                     \tag{1}
\]
The gauged Einstein operator acts by \(L_w\) on both radial cylinder
trace-free polarizations
\[
 D=dt^2-a^2d\phi^2,
 \qquad O=dt\otimes(ad\phi)+(ad\phi)\otimes dt,
\]
and by \(L_s\) on \(v(t)Q\), where \(Q\) is any hyperbolic fiber TT
tensor. These are the exact product equations established in Round 14.

For either scalar equation, the boundary value and outward conormal vectors
are
\[
 y=(v(-R),v(R)),\qquad
 \mathcal N v=\left(-\tfrac12a_Rv'(-R),
                         \tfrac12a_Rv'(R)\right).              \tag{2}
\]
The factor \(1/2\) comes from (1). The matrices below use the radial
measure \(a\,dt\). A tensor energy additionally multiplies by
\(2\pi\|Q\|_{L^2(F)}^2\), or \(4\pi\operatorname{Area}(F)\)
for each cylinder polarization. These positive factors must be included
when mixing different normalized sectors.

The normal metric, shift, Bianchi data and relative marking have not been
discarded. In particular a gauged Dirichlet response is not automatically
the physical Einstein filling response; §5 states their precise distinction.

## 2. Exact homogeneous Dirichlet-to-Neumann matrices

### 2.1 Waist and twist polarizations

The ground-state transformation is
\[
 L_w(fu)=-\frac1{2af}(p u')',\qquad
 p=af^2=c\operatorname{sech}^3(kt).                            \tag{3}
\]
Define
\[
 S(t)=\int_0^t\frac{ds}{p(s)}
 =\frac{\sinh(kt)+\sinh^3(kt)/3}{kc},
 \qquad \Lambda_w=2S(R).
\]
All homogeneous solutions are \(v=f(A+BS)\). Thus
\[
 A=\frac{y_-+y_+}{2f_R},\qquad
 B=\frac{y_+-y_-}{f_R\Lambda_w}.
\]
Direct endpoint differentiation gives the exact matrix
\[
 \boxed{D_w=-a_R\kappa_R I+
       \frac1{2\Lambda_w f_R^2}
       \begin{pmatrix}1&-1\\-1&1\end{pmatrix},
       \qquad\mathcal N v=D_wy.}                            \tag{4}
\]
Its quadratic form is
\[
 y^TD_wy=-a_R\kappa_R(y_-^2+y_+^2)
             +\frac{(y_+-y_-)^2}{2\Lambda_w f_R^2}.          \tag{5}
\]
The boundary term in (5) is real and cannot be dropped by citing the
nonnegative homogeneous Dirichlet operator. Indeed
\[
 \int_{-R}^R a\left(\tfrac12v'^2+(2\kappa^2-k^2)v^2\right)dt
 =\tfrac12\int_{-R}^R p u'^2dt
          +\tfrac12[aff'u^2]_{-R}^R.                        \tag{6}
\]
The renormalized response \(D_w+a_R\kappa_RI\) is positive of rank
one, but the actual response (4) has a negative common-boundary mode.

For a full collar with \(a_R=A_0>0\) fixed and \(c\to0\), its
two eigenvalues obey
\[
 d_w^{\mathrm{even}}\to-kA_0,
 \qquad d_w^{\mathrm{odd}}\to\tfrac12kA_0.                 \tag{7}
\]
Thus positivity of an exterior response does not follow from positivity
of the collar's zero-boundary operator.

### 2.2 Fiber TT response

Put
\[
 \Lambda_s=\int_{-R}^R a^{-1}dt=c^{-1}J_1(R),
 \quad J_m(R)=\int_{-R}^R\operatorname{sech}^m(kt)dt.
\]
The exact fiber TT response is
\[
 \boxed{D_s=\frac1{2\Lambda_s}
       \begin{pmatrix}1&-1\\-1&1\end{pmatrix}.}             \tag{8}
\]
Its common-value mode is zero: the same hyperbolic deformation on every
slice is an actual infinitesimal product Einstein deformation. Its
relative-value eigenvalue is \(1/\Lambda_s\sim kc/\pi\).

## 3. Inhomogeneous response from Maxwell shear

Let \(\beta\ne0\) be harmonic on \(F\), and let the connection solve
the finite-collar Maxwell problem exactly:
\[
 z'=\frac{\operatorname{sech}^3(kt)}{J_3(R)},\qquad
 z(-R)=0,\quad z(R)=1.
\]
Its smooth closed realization uses the cutoff analyzed in Round 14.
The present formulas give its exact interior response before those
explicitly controlled end modifications.

### 3.1 The radial waist source

Write \(\rho=\|\beta\|_2^2/\operatorname{Area}(F)\). The
constant-fiber, radial trace-free projection of the residual is
\(-\frac12a^2z'^2\rho\,D\). The corresponding linear repair equation is
\[
 L_wv=F_w,\qquad F_w=\tfrac12a^2z'^2\rho.                  \tag{9}
\]
Set
\[
 \Gamma=\int_{-R}^R af F_wdt
       =\frac{\rho c^3J_5(R)}{2J_3(R)^2}>0.                \tag{10}
\]
For the zero-Dirichlet solution \(v_D\), evenness implies
\[
 p(v_D/f)'(t)=-2\int_0^t af F_wds.
\]
Therefore the complete boundary response, for any boundary value \(y\), is
\[
 \boxed{\mathcal Nv=D_wy+r_w,
 \qquad r_w=-\frac\Gamma{2f_R}\binom11.}                  \tag{11}
\]
The source generates common, not antisymmetric, conormal data.

There is also an explicit interior amplification:
\[
 \boxed{v_D(0)=\frac{\Gamma\Lambda_w}{2}
                      -2\int_0^R S(t)a(t)f(t)F_w(t)dt.}    \tag{12}
\]
The second term is \(O(c^2)\), uniformly in \(R\ge1\), whereas
the first term has size \(c^2e^{3kR}\). For \(a_R=A_0\) fixed,
\[
 \boxed{c\,v_D(0)\longrightarrow
               \frac{\rho A_0^3}{4\pi},\qquad
       \frac{r_w}{c}\longrightarrow
          -\frac{3k\rho A_0^2}{8\pi}\binom11.}             \tag{13}
\]
Thus a zero-boundary full-width waist repair is not perturbatively small:
an \(O(c^2)\) source produces an \(O(c^{-1})\) interior response.
The boundary value is not disposable data. It must compensate this
amplification if a small global repair is to exist.

### 3.2 The fiber TT source

Let \(T_\beta=\beta\otimes\beta-\frac12|\beta|^2h_F\). It is TT.
For the coefficient of \(T_\beta\), the repair equation is
\[
 L_sv=F_s,\qquad F_s=\tfrac12a^2z'^2.
\]
The exact affine response is
\[
 \boxed{\mathcal Nv=D_sy+r_s,
        \qquad r_s=-\frac1{4I_3}\binom11
                  =-\frac{c^3}{4J_3(R)}\binom11,}
 \qquad I_3=c^{-3}J_3(R).                                  \tag{14}
\]
For arbitrary fiber TT test tensors, multiply (14) by the corresponding
\(L^2(F)\) component of \(T_\beta\). With zero boundary data,
\[
 v_D'(t)=\frac{1/2-z(t)}{I_3a(t)},\qquad
 v_D(0)/c^2\longrightarrow\frac14+\frac1{\pi^2}.            \tag{15}
\]
Unlike the waist component, this Dirichlet solution is uniformly small.
It nevertheless sends a nonzero TT traction into both exterior blocks.

## 4. The exterior equation, stated with actual boundary variables

Let \(\mathcal S_{\mathrm{ext}}\) be the linear exterior boundary
response, expressed in the same boundary values, conormal convention,
marking and gauge. It can couple both ends, different collars and all
tensor sectors. If the exterior carries an independent source, call its
traction \(r_{\mathrm{ext}}\). Smooth matching requires opposite
outward conormals, hence
\[
 \boxed{(D_{\mathrm{col}}+\mathcal S_{\mathrm{ext}})y
        =-(r_{\mathrm{col}}+r_{\mathrm{ext}}).}               \tag{16}
\]
This is the boundary Schur equation; it is an equation to solve, not an
assertion that the indicated exterior operator is already available.
If the full boundary variables split into the displayed low sector
\(y_L\) and the remaining sector \(y_H\), their exact linear elimination,
when the stated \(A_{HH}\) inverse exists, gives
\[
 \begin{split}
 &(A_{LL}-A_{LH}A_{HH}^{-1}A_{HL})y_L\\
 &\hspace{1cm}=-(r_L-A_{LH}A_{HH}^{-1}r_H),
 \qquad A=D_{\mathrm{col}}+\mathcal S_{\mathrm{ext}}.
 \end{split}                                                 \tag{17}
\]
The feedback changes both the matrix and the force. No term in (17) may be
removed merely because its variables were not part of the initial ansatz.

Two consequences are already definite.

1. **Product fiber response cannot absorb a single TT shear force.** If
   the exterior is restricted to unchanged hyperbolic products, or to a
   common fiber deformation with zero TT traction, the common-boundary
   component of (14) cannot match: \(D_s\) annihilates \((1,1)\),
   whereas \(r_s\ne0\). This is an exact restricted matching failure.

2. **There is no local sign theorem excluding every exterior response.**
   For example, if a hypothetical compatible exterior TT response were
   \(sI\), \(s>0\), then (16) would have the common-value solution
   \(y=c^3(1,1)/(4sJ_3)\). This is only an algebraic demonstration;
   no geometric exterior realizing \(sI\) is asserted. It proves why
   a nonzero local force alone does not decide the global equation.

For the waist sector a scalar model \(\mathcal S_{\mathrm{ext}}=sI\)
would instead give
\[
 y_- =y_+=\frac\Gamma{2f_R(s-a_R\kappa_R)}.                 \tag{18}
\]
It is resonant at \(s=a_R\kappa_R\). Away from resonance the boundary
value is typically \(O(c)\), and (12) still has to be combined with
the homogeneous value \(y/f_R\); one cannot infer a small interior
solution from a small boundary value. More precisely, for fixed
\(a_R=A_0\) and fixed \(s\ne kA_0\), the model gives
\[
 \boxed{c\,v(0)\longrightarrow
 \frac{\rho A_0^3}{8\pi}\frac{2s+kA_0}{s-kA_0}.}           \tag{18a}
\]
Cancellation of the leading \(c^{-1}\) amplification in this scalar
model occurs only at \(s=-kA_0/2\), not at a positive \(s\). Conversely
the resonance \(s=kA_0\) is the response associated with matching a
homogeneous waist kernel: its interior conormal is
\(-a_R\kappa_R y\), which the exterior must cancel. These are model
calculations of the necessary matching, not assertions about the actual
exterior's sign, limiting spectrum or geometric filling map.

In an identity-glued graph with common fiber metric, retaining one TT
boundary value per product block gives a weighted graph equation. The
edge conductance is \(c_e/(2J_{1,e})\), and the edge source at each
endpoint is \(-c_e^3 T_{\beta_e}/(4J_{3,e})\). A common fiber deformation
lies in the graph Laplacian's kernel. Hence, if exterior contributions
have been restricted to this product graph model, solvability requires
\[
 \sum_e\frac{c_e^3}{J_{3,e}}T_{\beta_e}=0                  \tag{19}
\]
as a functional on fiber TT tensors. This is the same Hodge-stress balance
obtained by varying the reduced connection energy. Equation (19) is not
silently imposed on general nonproduct Einstein exteriors.

## 5. Gauge and the physical meaning of waist and twist data

For a twist tensor \(vO\), put \(X=b(t)\partial_\phi\),
\(b'=v/a\). Then
\[
 \mathcal L_Xg_0=vO,
 \qquad D(\operatorname{Ric}+k^2g)_{g_0}[vO]=0              \tag{20}
\]
for **every** smooth \(v\). The physical marked datum is the difference
of endpoint rotations
\[
 \Delta b=\int_{-R}^R\frac v a dt.
\]
For a homogeneous gauged solution \(v=f(A+BS)\), parity gives
\[
 \boxed{\Delta b=\frac{J_3(R)}c A
       =\frac{J_3(R)}{2cf_R}(y_-+y_+).}                    \tag{21}
\]
The odd solution is generated by a vector field vanishing at both marked
ends; the even solution changes their relative rotation. Whether that
rotation is a genuine closed-manifold modulus depends on the exterior
gluing, not on the local tensor expression.

The Bianchi defects of the two homogeneous polarizations are
\[
 \mathcal B(vD)=-(v'+2\kappa v)dt,
 \qquad \mathcal B(vO)=-(v'+2\kappa v)a\,d\phi.              \tag{22}
\]
Since \(v'+2\kappa v=B/(af)=Ba/c^2\), the odd waist solution
has a nonzero radial Bianchi defect; it is not itself an ungauged linear
Einstein deformation. For the twist solution the dual Bianchi vector is
a constant multiple of \(\partial_\phi\), hence Killing, consistent
with (20). The even waist \(fD\) is genuinely TT; at the waist it
changes the logarithmic circle length by \(-A/2\).

These facts explain why the two copies of (4) are useful analytic response
blocks but are not two independent physical Einstein boundary conditions.
A legitimate exterior problem must carry its boundary gauge and relative
rotation together with its induced metric and second fundamental form.

There is a simple exact geometric comparison. A genuine hyperbolic surface
collar with fixed boundary radii \(r_-,r_+\) and waist radius \(c\) has
proper width and outward geodesic curvatures
\[
 d(c)=k^{-1}\{\operatorname{arcosh}(r_-/c)
                       +\operatorname{arcosh}(r_+/c)\},
 \quad K_\pm=k\sqrt{1-c^2/r_\pm^2}.                        \tag{23}
\]
Varying \(c\) therefore changes normal/geometric data even when the
induced boundary circles stay fixed. A full-component Dirichlet gauge
cannot replace this intrinsic filling problem.

## 6. What is now determined

The two radial gauged response matrices, the fiber TT response, their
inhomogeneous Maxwell tractions and their interior amplitudes are explicit.
The product-exterior TT obstruction follows directly. Arbitrary exterior
geometry is governed by (16)--(17), not by an assumed positive response.
The full-width waist response shows precisely where a small forcing meets
a large inverse and why matching data must be solved simultaneously.

This advances the finite-dimensional equation beyond a local sign test.
It does not yet control the actual exterior response and its nonlinear
feedback on the closed sheared manifold, and therefore does not enlarge
the proved all-mode radius from Round 14 by assertion.

`round15_boundary_response_check.py` independently verifies the exact
operators, endpoint matrices, gauge identities, forced fluxes and the
full-width asymptotic coefficient in (13).
