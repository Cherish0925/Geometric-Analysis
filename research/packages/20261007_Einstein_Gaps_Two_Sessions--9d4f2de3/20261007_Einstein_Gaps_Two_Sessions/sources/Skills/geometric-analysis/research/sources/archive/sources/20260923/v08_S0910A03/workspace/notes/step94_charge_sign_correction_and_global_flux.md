# Step 94: charge-sign correction, invariant fixed-charge identity, and the global flux object

Session `S0910A03`, Agent3 / Execute.

## 1. Withdrawal of the Step 93 maximum-principle corollary

The diagonal fixed-charge calculation itself is correct:
\[
LQ=\frac{|\nabla Q|^2}{Q}-18Q-4Q^2,
\qquad
L\log Q=-18-4Q,
\tag{1.1}
\]
for the established convention
\[
L=\Delta+\langle\nabla\sigma,\nabla\,\cdot\,\rangle.
\]
Its former interpretation is false. At an interior maximum,
\(LQ\le0\), and (1.1) gives
\[
LQ=-18Q-4Q^2<0,
\]
which is compatible with, rather than contradictory to, a positive maximum.
Likewise \(L\log Q<0\) is superharmonicity; it does not put the maximum on the
boundary.

The scalar equation
\[
y''=-18-4e^y,
\qquad y(0)=\log Q_0,
\qquad y'(0)=0,
\tag{1.2}
\]
has first integral
\[
(y')^2=36(\log Q_0-y)+8(Q_0-e^y).
\tag{1.3}
\]
For every \(Q_0>0\), its even solution has \(Q=e^y\) with a strict positive
maximum \(Q_0\) at zero and \(Q\to0\) at both infinities. Numerical integration
for \(Q_0=10^{-2},10^{-1},1,10\) verifies the first integral to about
\(10^{-9}\) at \(|x|\le8\):
`workspace/scripts/step94_scalar_superharmonic_countermodel.py` and
`workspace/data/step94_scalar_superharmonic_countermodel.json`.
This is a sign countermodel, not a reduced Einstein metric.

Accordingly, the following Step 93 statements are withdrawn:

1. that (1.1) excludes an interior positive maximum;
2. that \(Q\to0\) at both ends implies \(Q\equiv0\);
3. that a weak treatment of the charge-source derivative would automatically
   imply \(Q=O(\delta^2)\);
4. that (1.1) independently reproves the exact OT connector obstruction.

The valid exact statement remains different and stronger at the level of the
conserved variable: exact Einstein mixed equations give \(dq=0\). If an exact
open end is OT, then \(q=0\) there and hence on the connected exact Einstein
principal region. Merely having physical \(Q\to0\) is not equivalent to
\(q\to0\): for a nonzero conserved charge, the area/orbit factors can redshift
\(Q\) to zero. Once \(q=0\), the independent Steps 85--88 OT Bochner/resolvent
obstruction still supplies the connector impossibility in its stated class.

## 2. Full fixed-charge target identity

Let
\[
F(U)=\frac12q^TM(U)^{-1}q>0,
\qquad \beta=\log F,
\qquad Q=e^{-3\sigma}F(U),
\tag{2.1}
\]
for a fixed nonzero two-component charge \(q\). In Iwasawa coordinates
\[
M=\begin{pmatrix}
 e^\alpha+\zeta^2e^{-\alpha}&\zeta e^{-\alpha}\\
 \zeta e^{-\alpha}&e^{-\alpha}
\end{pmatrix},
\qquad
h_{\mathbb H^2}=d\alpha^2+e^{-2\alpha}d\zeta^2,
\]
direct symbolic differentiation verifies
\[
\operatorname{Hess}F=Fh,
\qquad |\nabla F|^2=F^2,
\tag{2.2}
\]
and hence
\[
\boxed{\operatorname{Hess}\beta
=h-d\beta\otimes d\beta,\qquad |\nabla\beta|=1.}
\tag{2.3}
\]
The exact orbit equation uses the weighted tension
\[
\tau_\sigma(U)=-Q\nabla\beta,
\tag{2.4}
\]
while the area equation is
\[
L\sigma=6+Q.
\tag{2.5}
\]
The drift chain rule then gives
\[
\begin{aligned}
L(\beta\circ U)
&=\operatorname{Hess}\beta:dU\otimes dU
  +d\beta(\tau_\sigma(U))\\
&=e-|d(\beta\circ U)|^2-Q.
\end{aligned}
\tag{2.6}
\]
Since \(\log Q=-3\sigma+\beta\circ U\),
\[
\boxed{
L\log Q=-18-4Q+e-|d(\beta\circ U)|^2.}
\tag{2.7}
\]
The remainder
\[
e_\perp:=e-|d(\beta\circ U)|^2\ge0
\tag{2.8}
\]
is precisely the energy of \(dU\) transverse to the unit horospherical
direction \(\nabla\beta\). The diagonal charge-aligned reduction has
\(e_\perp=0\), recovering (1.1). A general orbit map has no reason to be
charge-aligned, so the diagonal identity does **not** extend unchanged.
At a critical point of \(Q\), (2.7) reads
\[
L\log Q=-18-4Q+e_\perp;
\tag{2.9}
\]
even its sign is undetermined without a transverse-energy estimate.

All target Hessian, unit-gradient, and chain-rule residuals are exactly zero in
`workspace/scripts/step94_invariant_charge_identity.py` and
`workspace/data/step94_invariant_charge_identity.json`.

## 3. Why weak formulation helps only with derivative placement

For a variable charge, \(dq\) is the mixed-Ricci source. A logarithmic formula
is singular at zeros of \(q\), including exact OT end neighborhoods, and
pointwise expansion of \(L\log |q|\) introduces derivatives of the source.
Testing the undivided charge equation or a quadratic energy and integrating by
parts can move that derivative onto a test function. This is useful for a global
flux estimate. It cannot reverse the sign in (1.1), remove the nonnegative
\(e_\perp\) in (2.7), or create sequence-uniform \(nabla E\) bounds from the
original \(C^0\) Ricci pinching.

Thus the forced question is not a local regularity problem at the maximum of
\(Q\). It is a global source-to-charge problem on the quotient cylinder.

## 4. Exact global flux law and the topology of the unknown

Liu's mixed Ricci formula gives twist scalars \(q_a\) satisfying, in an
orthonormal horizontal frame \((X,Y)\),
\[
\operatorname{Ric}(Z,V_a)
=-\frac1{2\rho}\langle dq_a,JZ\rangle.
\tag{4.1}
\]
For \(E=\operatorname{Ric}+3g\), mixed Einstein background terms vanish. Up to
the global sign fixed by orientation,
\[
dq_a(W)=2\rho E(JW,V_a).
\tag{4.2}
\]
In the invariant norm for \(G=e^\sigma M\), this gives the exact quadratic law
\[
\boxed{
e^{-3\sigma}M^{ab}\langle dq_a,dq_b\rangle
=4|E_{\rm mix}|_{\rm HS}^2,}
\tag{4.3}
\]
so the physical source variable satisfies
\(|b|=2|E_{\rm mix}|_{\rm HS}\le2\sqrt2\,\delta\). This is the strongest
derivative-free weak input supplied directly by the mixed Ricci equation. It shows simultaneously why:

* exact OT on one open end implies \(q=0\) throughout a connected exact region;
* small \(|E|\) does not itself make \(q\) small where \(\rho\) is large;
* an open exact OT neighborhood at **both** ends imposes two boundary values on
  a first-order forced system, hence a cancellation condition on the mixed
  source, not a local maximum condition on \(Q\).

For any path \(\gamma\) crossing from one exact OT end to the other,
\[
0=q(\gamma_+)-q(\gamma_-)=\int_\gamma dq.
\tag{4.4}
\]
Large intermediate charge requires creation and later annihilation by sources
of opposite signed flux. Since \(dq\) is an exact vector-valued one-form, every
closed loop also satisfies
\[
\oint dq=0.
\tag{4.5}
\]
These equalities are necessary but do not control the amplitude: a long region
with weight \(\rho\) can accumulate order-one charge from a \(C^0\)-small mixed
Ricci component, just as the corrected backward-transport example in Step 93
shows.

The genuinely global estimate must therefore exploit more than
\(|dq|\le C\delta\rho\). It has to couple the exactness/cancellation (4.3)--(4.4)
to one or both of:

1. the separator Jacobi form
   \[
   \int_C\mathcal W y^2\le\int_C(y_s^2+a_\delta y^2),
   \qquad
   \mathcal W\ge\frac34Q,
   \tag{4.6}
   \]
   which already gives the finite universal bound
   \(\sup_CQ\le C_Q(\delta)\) but no smallness;
2. the horizontal/orbit equations, which determine the weighted geometry and
   make a large charged transition consume area, orbit energy, or stability
   budget across a two-dimensional region.

A natural next object is a two-ended Green/flux pairing for the vector charge,
not the scalar \(log Q\). Let \(u\) solve a quotient Dirichlet or massive problem
with opposite constants on the two OT end collars. Then
\[
\int_B\langle dq_\ell,du\rangle
=-\int_B q_\ell\Delta u
=\int_B q_\ell d^*du,
\qquad q_\ell=\ell^aq_a,
\tag{4.7}
\]
where the boundary term vanishes when \(q=0\) on the exact collars and the last
sign uses \(d^*du=-\Delta u\). The drift-weighted version is
\[
\int_B\rho\langle dq_\ell,du\rangle
=-\int_B\rho q_\ell Lu.
\tag{4.8}
\]
Equation (4.3) bounds the left side using only \(C^0\) Ricci defect; (4.6) can
control traces at the stable separator. To become coercive, (4.7)--(4.8) need a quotient capacity or spectral lower
bound that does not degenerate under arbitrary connector length/area growth.
The exact cusp has a positive drift spectral scale, but ordinary unweighted
two-end capacity is insufficient: even the interval model \(q(0)=q(L)=0\),
\(|q'|\le\delta\), admits a triangular profile of height \(\delta L/2\), while
the Dirichlet energy of a unit end-to-end potential decays like \(L^{-1}\).
The research target is therefore a **weighted, geometry-coupled
source-to-charge estimate** whose constant is controlled by the area equation
and separator stability. A prototype is a matrix-weighted Poincare/Hardy bound
for \(A=e^{-3\sigma}M^{-1}\),
\[
\int q^TAq\,d\mu_\sigma
\le C\int(dq)^TA(dq)\,d\mu_\sigma+\text{separator trace},
\tag{4.9}
\]
with \(C\) independent of connector length and area growth. No such estimate is
presently proved. Moreover, Section 6 below shows that no estimate without an
order-one separator trace term follows even after imposing the exact area
equation; a finite separator trace term can yield only finite control, not
smallness as the mixed source tends to zero.

## 5. Adverse benchmarks and scope

The charged radial disk caps of Step 90 exhibit order-one \(Q\) with an exact or
small-defect local geometry. They refute any purely local \(Q=O(\delta^2)\)
expectation. They do not satisfy the free cylindrical two-end topology: a circle
collapses at the disk center. The scalar superharmonic family (1.2) refutes the
maximum inference but is not a geometric connector. Both should be used as
adverse benchmarks for any proposed global estimate.

No result here settles a two-ended forced connector, nonsymmetric graph metrics,
the positive normalized branch, higher dimensions, or Yau Problem 26. The new
rigorous content is the corrected sign, the invariant two-charge formula (2.7),
and the identification of the vector flux/capacity coupling as the remaining
free-\(T^2\) global object.

## 6. Exact redshift-taper benchmark for the proposed weighted capacity

The prototype (4.9) is not a consequence of the mixed equation, both end values,
the area equation, and separator finiteness alone. This can be tested in a
symmetric scalar subsystem without claiming a geometric connector.

Take signed normal coordinate \(r\), prescribe \(q=q_0\) on
\(|r|\le R\), taper it by a fixed-width smootherstep to \(q=0\), and append
exact OT collars on both ends. Solve the exact one-dimensional area equation
\[
\rho''=(6+Q)\rho,
\qquad
Q=\frac12\rho^{-3}q^2,
\qquad
\rho(0)=1,\quad \rho'(0)=0.
\tag{6.1}
\]
Define the physical mixed source
\[
b=\rho^{-3/2}q'.
\tag{6.2}
\]
Then the Maxwell transport identity holds exactly:
\[
w'+\frac32\sigma'w=b,
\qquad w=\rho^{-3/2}q,\quad\sigma=\log\rho.
\tag{6.3}
\]
The model has \(q=0\) on both outer collars, zero total coordinate-charge flux,
and fixed separator value \(Q(0)=q_0^2/2\). Nevertheless, delaying the taper
until the area has expanded makes \(b\) exponentially small. With a smooth endpoint-flat cutoff, \(q_0=K=1\), and
\(R=1,\ldots,6\), the computed maxima are
\[
3.32\times10^{-2},\ 8.43\times10^{-4},\ 2.14\times10^{-5},\
5.43\times10^{-7},\ 1.38\times10^{-8},\ 3.49\times10^{-10}.
\]
A fit gives
\[
\log\|b\|_\infty=-3.6742319R+O(1),
\]
matching \(-3\sqrt6R/2\). At the same time the natural weighted ratio
\[
\frac{\int w^2\rho\,dr}{\int b^2\rho\,dr}
\tag{6.4}
\]
grows with fitted exponent \(4.8989803R\), matching \(2\sqrt6R\), and reaches
\(3.58\times10^{12}\) at \(R=6\). Transport and area residuals are below
\(9\times10^{-16}\). Files:
`workspace/scripts/step94_two_ended_redshift_taper.py` and
`workspace/data/step94_two_ended_redshift_taper.json`.

Analytically, on the central plateau
\[
(\rho')^2=6\rho^2-\rho^{-1}-5,
\]
so \(\rho\sim Ae^{\sqrt6r}\), which proves the fitted source-decay and ratio-growth
exponents. This is stronger than the elementary long-interval example: even the
exact area equation reinforces the redshift escape rather than supplying the
missing coercivity. It is still not a full reduced Einstein solution because the
orbit-shape and horizontal equations are not imposed. In fact, freezing
\(M=I\) while \(Q>0\) violates
\(\tau_\sigma(U)=-Q\nabla\beta+Z\) when the orbit defect \(Z=0\).
Consequently any genuine exclusion must extract a cost from those remaining
coupled equations (or from a global stability/topology relation spanning the
transition); Maxwell, both OT end values, area growth, and the finite separator
charge estimate are insufficient by themselves. The Step 90 radial system
shows that even area plus orbit equations can support strong redshift; its
unsatisfied global price is isolated by the horizontal constraint propagation
\[
C'=-2(u+H)C-wb,
\tag{6.5}
\]
whose terminal condition creates a second weighted moment beyond total charge
flux. Thus the sharp next construction/obstruction question is whether the full
two-dimensional horizontal equations and separator stability force a
nonvanishing cost for simultaneous cancellation of both charge and horizontal
constraint moments on a free cylinder. Conversely, satisfying these omitted
equations while retaining delayed source would be a concrete construction
route.

## 7. Charged stable Koiso germs: local separator conditions do not kill twist

The Step 92 uncharged constrained germs admit a charged extension. Let
\[
q_\Sigma=ds^2+M(U(s))_{ab}dx^adx^b,
\qquad \det M=1,
\]
fix \(0<S<3\), and choose a periodic analytic hyperbolic target circle with
\[
|U_s|^2=12+2S.
\]
For a fixed nonzero charge covector \(\mathfrak q\), scale it so
\[
Q(s)=\frac12\mathfrak q^TM^{-1}\mathfrak q<S,
\qquad P=S-Q>0.
\]
Let \(N\perp U_s\) be the global analytic target unit normal, put
\[
B=\sqrt{P/2}\,M^{-1}dM(N),
\qquad m=-\frac12\mathfrak q
\]
at the center normalization \(\rho=1\), and define the full Weingarten
endomorphism by
\[
W=\begin{pmatrix}0&m_b\\m^a&B^a{}_b\end{pmatrix}.
\tag{7.1}
\]
The mixed block appears twice in the norm, so
\[
\operatorname{tr}W=0,
\qquad
\operatorname{tr}(W^2)=\operatorname{tr}(B^2)+2m^TM^{-1}m=P+Q=S.
\tag{7.2}
\]
Since \(R_{q_\Sigma}=-|U_s|^2/2=-6-S\), the Hamiltonian constraint is exact.
The momentum components are
\[
\nabla_iW^i{}_s=-\operatorname{tr}(AB)=0,
\]
while for a vertical index \(a\),
\[
\nabla_iW^i{}_a
=m_a'+(\operatorname{tr}A)m_a-A^b{}_am_b+(MA)_{ba}m^b=0:
\tag{7.3}
\]
\(m\) is constant, \(\operatorname{tr}A=0\), and the last two connection terms
cancel. In Gaussian gauge the chosen orientation gives
\(\mathfrak q=-2\rho m\); reversing orientation reverses the sign only.

The full Jacobi form is especially simple:
\[
\mathcal J(\phi)=\int_{T^3}\bigl(|\nabla\phi|^2+(3-S)\phi^2\bigr),
\tag{7.4}
\]
so the minimal center is strictly stable for **all** variations, with lowest
eigenvalue \(3-S\). Nonzero torus Fourier modes add
\(k^TM^{-1}k\). Koiso therefore supplies a genuine local analytic
\(\operatorname{Ric}=-3g\) germ with nonzero conserved twist charge.

The sample \(S=1\), target \(Q_{\max}=1/2\), and a tenfold target circle has
\(Q\in[0.2405,0.5]\), \(P\in[0.5,0.7595]\), lowest stability eigenvalue 2,
and all matrix/constraint residuals below \(1.3\times10^{-14}\):
`workspace/scripts/step94_charged_koiso_separator.py` and
`workspace/data/step94_charged_koiso_separator.json`. Independent verification
is in `trace/ttcs/results/step94_ttcs03_verifier1_integration.md`.

Thus minimality, full stability, and all local Einstein Cauchy constraints do
not force separator charge to vanish. Exact charge conservation prevents this
nonzero-charge germ from attaching to an exact OT open set without mixed Ricci
forcing; global continuation and matching remain the issue.

## 8. Invariant horizontal Noether identity and the second two-end moment

Define the residual blocks of the full free-\(T^2\) reduction by
\[
\begin{aligned}
H={}&\operatorname{Ric}_B-\operatorname{Hess}\sigma
-\frac12d\sigma^2-\frac12U^*h-Q\gamma_B+3\gamma_B,\\
T={}&L\sigma-6-Q,\\
Z={}&\tau_\sigma(U)+\nabla_UQ,
\end{aligned}
\tag{8.1}
\]
and the variable-charge work one-form
\[
m_q=D_qQ[dq]=e^{-3\sigma}\langle M^{-1}q,dq\rangle.
\tag{8.2}
\]
A direct contracted-Bianchi and harmonic-map stress calculation gives the exact
identity
\[
\boxed{
2\operatorname{div}_\sigma H-d\operatorname{tr}H
=-dT-Td\sigma-\langle Z,dU\rangle-m_q.}
\tag{8.3}
\]
This was independently derived and all coefficients checked in
`workspace/scripts/step94_horizontal_noether_identity.py`,
`workspace/data/step94_horizontal_noether_identity.json`, and
`trace/ttcs/results/step94_ttcs04_verifier1_integration.md`.

For the radial specialization
\[
\gamma=dr^2+\psi^2d\theta^2,
\quad H=C\,dr^2,
\quad u=\sigma',\ h=\psi'/\psi,
\]
one has
\[
(2\operatorname{div}_\sigma H-d\operatorname{tr}H)_r
=C'+2(u+h)C.
\]
With \(T=Z=0\) and signed physical variables, \(m_q(\partial_r)=wb\), so (8.3)
recovers exactly
\[
C'=-2(u+h)C-wb.
\tag{8.4}
\]
Thus the Step 90 terminal moment is not a radial accident. It is the charge-work
term in the invariant horizontal Bianchi identity.

The radial integrating factor \(\mu=e^{2\sigma}\psi^2\) yields, when both end
values of \(C\) vanish,
\[
\int_{r_-}^{r_+}\mu\,wb\,dr=0.
\tag{8.5}
\]
This is independent of the total coordinate-charge condition
\(\int q'\,dr=0\). More generally, for a vector field \(X\) cut off inside exact
end collars, weighted integration by parts gives the derivative-free adjoint
pairing
\[
\begin{aligned}
\int_Bm_q(X)d\mu_\sigma=\int_B\bigl[
&2H:\operatorname{sym}\nabla X-(\operatorname{tr}H)\operatorname{div}_\sigma X\\
&+T\operatorname{div}X-\langle Z,dU(X)\rangle\bigr]d\mu_\sigma.
\end{aligned}
\tag{8.6}
\]
This is the correct two-dimensional generalization sought after the redshift
benchmark. It moves derivatives off the \(C^0\)-small Ricci defect. It is a
compatibility identity, not an additional field equation: \(H,T,Z,dq\) are all
blocks of the same Ricci defect and cannot be prescribed independently.

Equation (8.6) still does not close an obstruction. Its right side involves the
adjoint derivatives of \(X\), \(dU\), and the weighted volume, all of which can
degenerate under redshift. The exact next question is whether one can choose an
adjoint field tied to the two ends and stable separator whose norm is controlled
by the full quotient geometry, producing a sign or length-independent lower
bound for the charge-work moment; or construct a distributed sign-changing
source satisfying both (4.4) and (8.6) with every Ricci block tending to zero.
