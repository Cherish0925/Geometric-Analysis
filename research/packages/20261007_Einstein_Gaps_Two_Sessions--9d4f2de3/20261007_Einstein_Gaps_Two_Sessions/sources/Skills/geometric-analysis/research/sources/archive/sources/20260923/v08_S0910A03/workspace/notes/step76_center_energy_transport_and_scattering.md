# Step 76: center energy, covariance transport, and the reflection-to-end scattering problem

Session `S0910A03`, Agent4 / Explore.

## 1. Corrections propagated from Step 75

The reflected-center estimate has the sharper constant

\[
 \lambda_{\min}S'(0)\le -3+3\delta,
 \qquad \|\operatorname{Ric}_g+3g\|_{\rm op}\le\delta.
 \tag{1.1}
\]

At the downward zero selected in the center theorem, let `v` be the orbit-normal
unit direction and complete it to an orthonormal frame `(v,e_1,e_2,n)`, with
`n` normal to the reflected hypersurface.  If

\[
 e=R_q+6=E_{vv}+E_{11}+E_{22}-E_{nn},
 \quad E=\operatorname{Ric}_g+3g,
\]

then

\[
 \langle S'(0)v,v\rangle
 \le e-3-E_{vv}
 =-3+E_{11}+E_{22}-E_{nn}
 \le-3+3\delta.
\]

This avoids bounding `e` and `E_vv` separately.  The correction is now in
`step75_reflection_core_flux_and_center_theorem.md`,
`step75_structural_identities_verify.py`, and
`step75_structural_identities.json`.

A second correction changes the interpretation of the anisotropy law.  For an
exact reflected core the **total signed** flux is zero, not nonzero.  The energy
is carried by a covariance pairing.  For a forced core a bulk term can carry it,
so pointwise nonzero exit derivative is compulsory only in the exact problem.

## 2. Integrated center energy

Let

\[
 q=ds^2+G(s)_{ab}dx^a dx^b,
 \quad \rho=\sqrt{\det G},
 \quad A=\frac12G^{-1}G',
 \quad h=\operatorname{tr}A=\frac{\rho'}\rho,
 \quad A_0=A-\frac h2I.
\]

Since the orbit dimension is two,

\[
 |A|^2=|A_0|^2+\frac12h^2,
\]

and the scalar identity is

\[
 R_q=-2h'-|A_0|^2-\frac32h^2.
 \tag{2.1}
\]

Writing `e=R_q+6`, multiplying by `rho`, and using periodicity,

\[
 \int\rho h'=-\int\rho h^2,
\]

gives

\[
 \boxed{
 \int\rho|A_0|^2
 =6\int\rho+\frac12\int\rho h^2-\int\rho e.
 }
 \tag{2.2}
\]

For a diagonal orbit metric

\[
 G=\operatorname{diag}(e^{2b},e^{2c}),
 \qquad d=b-c,
\]

one has `|A_0|^2=d_s^2/2`, hence

\[
 \boxed{
 \int\rho d_s^2
 =12\int\rho+\int\rho h^2-2\int\rho e.
 }
 \tag{2.3}
\]

After dividing by `int rho`, an exact scalar-minus-six center obeys

\[
 \langle d_s^2\rangle_\rho\ge12.
 \tag{2.4}
\]

At a reflected four-dimensional small-defect center, `|e|<=4delta`, so

\[
 \langle d_s^2\rangle_\rho\ge12-8\delta.
 \tag{2.5}
\]

Changing the lattice in the two orbit directions multiplies both energy and
volume by the same covolume.  Thus (2.4)--(2.5) survive the rank-two lattice
collapse used in the graph-neck construction.  This is stronger and more
natural than minimizing one peak sectional curvature: it shows that the whole
center contains normalized order-one anisotropy energy.

## 3. Exact and forced transport with physical measures

For

\[
 g=\gamma+e^{2b}dx^2+e^{2c}dy^2,
 \quad d=b-c,
 \quad \rho=e^{b+c},
 \quad X=E_x-E_y,
\]

the invariant difference equation is

\[
 \boxed{
 \operatorname{div}_\gamma(\rho\nabla_\gamma d)=-\rho X.
 }
 \tag{3.1}
\]

Use Gaussian distance on the two-dimensional quotient,

\[
 \gamma=dr^2+\alpha(r,z)^2dz^2,
 \qquad d\ell_r=\alpha\,dz.
\]

Define, including the orbit-lattice covolume `A_Lambda`,

\[
 Q(r)=\mathcal A_\Lambda\int_{C_r}\rho d_r\,d\ell_r,
\]

and for any constant `c`,

\[
 F_c(r)=\mathcal A_\Lambda\int_{C_r}(d-c)\rho d_r\,d\ell_r.
\]

Then

\[
 Q(r_1)-Q(r_0)
 =-\mathcal A_\Lambda\int_{[r_0,r_1]\times S^1}\rho X\,d\mu_\gamma,
 \tag{3.2}
\]

and

\[
 \boxed{
 F_c(r_1)-F_c(r_0)
 =\mathcal A_\Lambda\int\rho|\nabla d|^2d\mu_\gamma
 -\mathcal A_\Lambda\int(d-c)\rho Xd\mu_\gamma.
 }
 \tag{3.3}
\]

For an exact reflected core, `X=0`, `d_r(0)=0`, and therefore

\[
 Q(r)\equiv0,
 \qquad
 F_c(R)=\mathcal A_\Lambda\int_{[0,R]\times S^1}
               \rho|\nabla d|^2d\mu_\gamma.
 \tag{3.4}
\]

The signed flux density can be nonzero despite its zero integral.  Its
covariance with `d` carries all Dirichlet energy.  If `d_r(R)` vanished
identically at a finite exact exit, then `F_c(R)=0` and `d` would be constant.
For a forced core, the last term in (3.3) can instead pay the energy.  Even
`|X|<=2delta` is insufficient without a geometry-uniform bound on
`int rho |d-c|`.

Differentiating by slices gives

\[
 \boxed{
 F_c'(r)=\mathcal A_\Lambda\int_{C_r}\rho
 \left(d_r^2+|\nabla_{C_r}d|^2-(d-c)X\right)d\ell_r.
 }
 \tag{3.5}
\]

At an exact reflected center,

\[
 F_c'(0)=\mathcal A_\Lambda\int\rho d_s^2ds\ge12V_0.
 \tag{3.6}
\]

This is an order-one normalized initial slope, but it gives no uniform
positive thickness: Ricci pinching alone supplies neither the radial derivative
bounds nor the quotient ellipticity needed to keep (3.6) from changing in an
arbitrarily thin layer.

## 4. Expanding-region calculation: the center energy can be diluted

On the flat-cusp background take one mode

\[
 d(t,z)=A\psi_k(t)\cos(kz),
\]

where

\[
 \psi_k''+3\psi_k'-k^2e^{-2t}\psi_k=0,
 \quad \psi_k(0)=1,
 \quad \psi_k'(0)=0.
\]

With `x=k exp(-t)`, the exact solution and derivative are

\[
 \psi_k(t)=
 \frac{e^{x-k}(x-1)+e^{k-x}(x+1)}{2k},
 \tag{4.1}
\]

\[
 \psi_k'(t)=\frac{x^2}{k}\sinh(k-x).
 \tag{4.2}
\]

Thus

\[
 \psi_k(\infty)=\frac{\sinh k}{k},
 \qquad
 e^{2t}\psi_k'(t)\longrightarrow k\sinh k.
 \tag{4.3}
\]

For fixed `k`, the unweighted normal derivative tends to zero like `e^{-2t}`
but the weighted stress survives.  The map is exponentially bad in frequency.
If `V(t)=V_0e^{3t}`, then

\[
 F(t)=\frac{A^2V_0}{2}e^{3t}\psi_k\psi_k',
 \tag{4.4}
\]

and

\[
 \frac{F(t)}{V(t)}
 =\frac{A^2}{2}\psi_k\psi_k'
 \sim\frac{A^2}{2}\sinh^2(k)e^{-2t}.
 \tag{4.5}
\]

Total pairing grows while pairing per unit physical volume decays.  This is a
concrete energy-dilution mechanism, not a positive lower cost.  The ansatz
solves the anisotropy difference equation but has the remaining base defect

\[
 E|_\gamma=-\frac12\,dd\otimes dd.
 \tag{4.6}
\]

Hence it is not an exact core.  It shows exactly why the center floor alone
cannot obstruct a long expanding bridge and why all Ricci components remain
essential.  For moving frequencies, dilution requires at least

\[
 A_j e^{-R_j}\sinh(k_j)\to0.
 \tag{4.7}
\]

This exposes analytic/Gevrey regularity of the center-to-end scattering map as
a real issue, not an artifact of finite Fourier computation.

## 5. CMC transport and the correct global unknown

In pointwise volume gauge write

\[
 g=dr^2+e^{2a(r)}q_r,
 \qquad q_r'=2q_rP,
 \qquad \operatorname{tr}_{q_r}P=0.
\]

For an exact `Ric=-3g` metric,

\[
 a''=1-(a')^2-\frac13|P|^2,
 \tag{5.1}
\]

\[
 P'+3a'P=e^{-2a}\operatorname{Ric}(q_r)^\circ,
 \tag{5.2}
\]

with Hamilton and momentum constraints

\[
 e^{-2a}R(q_r)+6(1-(a')^2)+|P|^2=0,
 \qquad \operatorname{div}_{q_r}P=0.
 \tag{5.3}
\]

The integrating factor is

\[
 \boxed{
 (e^{3a}P)'=e^a\operatorname{Ric}(q_r)^\circ.
 }
 \tag{5.4}
\]

With a defect, the right side becomes

\[
 e^a\operatorname{Ric}(q_r)^\circ-e^{3a}E_T^\circ.
 \tag{5.5}
\]

If an exact core enters a region with `a(r)=r+O(1)` and uniformly bounded
`Ric(q_r)^circ`, then

\[
 P(R)=O(e^{-2R}).
 \tag{5.6}
\]

The correct finite quantity is therefore not `P(R)` but the weighted PE stress
`e^{2a(R)}P(R)` or the covariance pairing (3.4).  A global obstruction would
have to separate the stress generated by scalar-minus-six reflected centers
from the stress permitted by negative-Yamabe PE ends.  Present identities do
not do so.

## 6. What the Li--Liu source establishes

The original 2026 Li--Liu paper proves that for every metric on `T^2` there is
an exact anti-self-dual `Ric=-3h` metric on `(0,infinity) x T^3` with one PE end
and one AH cusp end.  In Type I form,

\[
 h=\xi^{-2}\left(Wd\xi^2+W^{-1}\eta^2+We^v g_{T^2}\right),
\]

\[
 (e^v)_{\xi\xi}+\Delta_{T^2}v=0,
 \qquad W=1-\frac12\xi v_\xi.
 \tag{6.1}
\]

The relevant boundary problem has prescribed `v(0)=phi`, bounded `v` on the
half-cylinder, a unique solution, and super-exponential convergence to the AH
cusp model.  This is an exact nonlinear outer-end mechanism and a concrete
Dirichlet-to-Neumann map.  The same source proves that nonnegative-Yamabe PE
infinity forces one-endedness except for the rigid Ricci-flat warped product;
negative-Yamabe infinity is not covered.  The Li--Liu metrics themselves have
one PE end and one cusp end, not a reflected center.

A horizontal `xi=constant` slice cannot be totally geodesic: the fiber and
base principal-curvature equations would force `xi v_xi=4`, hence `W=-1`,
contradicting positive definiteness.  Therefore one cannot simply cut a
Li--Liu metric at a level set and reflect it.  Possible non-horizontal totally
geodesic hypersurfaces or non-ASD deformations are not excluded by this
calculation, but are not supplied by the source.

The source search found no theorem constructing or excluding a pure
negative-Yamabe, two-PE-ended reflected Einstein metric on `R x T^3`.  Anderson's
boundary-map theory is Fredholm index zero and permits cusp degeneration, but
does not settle this topology.  Accordingly the exact global model remains an
open intersection problem rather than a known example.

## 7. Refined research object

The graph-neck route now asks whether two infinite-dimensional sets intersect:

1. reflected-center data satisfying
   \[
   S(0)=0,\qquad R(q_0)=-6,
   \]
   with the order-one normalized center energy (2.4);
2. negative-Yamabe PE/AH stable data with
   \[
   P(r)=O(e^{-2r}),\qquad
   e^{-2a(r)}\|\operatorname{Ric}(q_r)\|\to0,
   \]
   and controlled higher attachment jets.

The scattering map between them must preserve the Hamilton and momentum
constraints.  In the diagonal class its finite output is the weighted stress
or covariance pairing, not unweighted shear.

Two calculations can materially decide viability:

### A. Quadratic zero-mode matching

For one small Fourier perturbation, compute to second order:

* the reflection-side coefficient of
  `e^{2R}(3-H(R))` and the weighted anisotropy stress;
* the Li--Liu Type-I Dirichlet-to-Neumann coefficient, including the induced
  zero mode through `(e^v)_{xi xi}+Delta v=0` and `W=1-xi v_xi/2`;
* the Hamilton/momentum compatibility after all scale and gauge parameters are
  removed.

A sign mismatch after all allowable parameters are used would obstruct the
symmetric bridge at quadratic order.  A matching parameter would exhibit the
first genuine core-to-end mechanism.

### B. Exact PE stress functional

Insert the PE expansion into (3.4) and express the limiting covariance as a
functional of conformal boundary data.  For a standard expansion,

\[
 (S-I)^\circ=e^{-2r}\operatorname{Sch}_\gamma^\circ
 -\frac32e^{-3r}\gamma_{(3)}^\sharp+\cdots,
\]

so `e^{2r}(S-I)^circ` has a finite boundary value.  Compute this functional on
the Li--Liu Toda solutions and compare it with the center energy generated by
(2.3).  This is the nonlinear analogue of matching reflection scattering to a
PE Dirichlet-to-Neumann map.

Neither calculation resolves the graph construction by itself, and success on
the negative branch still leaves the positive branch and higher-dimensional
quantifiers of Yau 26.  They nevertheless replace finite-tolerance fitting by
a sharply defined mathematical interface whose outcome can genuinely change
the route.

## 8. Evidence files

* `workspace/scripts/step76_center_energy_flux_verify.py`
* `workspace/data/step76_center_energy_flux.json`
* corrected `workspace/notes/step75_reflection_core_flux_and_center_theorem.md`
* corrected `workspace/scripts/step75_structural_identities_verify.py`
* corrected `workspace/data/step75_structural_identities.json`
* independent checks: `trace/ttcs/results/step76_ttcs01_verifier1_integration.md`
* route development: `trace/ttcs/results/step76_ttcs01_generator1_integration.md`
* primary external source: `Knowledge/objects/papers/Poincaré-Einstein-4-manifolds-with-cusps--d36d062e94d0--09d8ca1fbe38/object.md`

## 9. Matrix-valued refinement and the Li--Liu boundary manifold

The scalar anisotropy `d=b-c` is only the diagonal geodesic inside the full
unimodular orbit-shape target

\[
 \mathcal P=\operatorname{SL}(2,\mathbb R)/\operatorname{SO}(2).
\]

For non-diagonal orbit matrices write

\[
 G=\rho U,
 \qquad \det U=1.
\]

Then

\[
 A_0=\frac12U^{-1}U_s,
 \qquad
 |A_0|^2=\frac14\operatorname{tr}
 \bigl((U^{-1}U_s)^2\bigr).
\]

Equation (2.2) therefore supplies an `H^1` energy floor for a loop
`U:S^1->P`, not merely for one scalar function.  Because `P` is a Hadamard
surface, every loop is contractible; the floor comes from the scalar-minus-six
constraint, not target topology.  The exact Einstein orbit-difference equation
should accordingly be viewed as the harmonic-map equation for `U` coupled to
the orbit area and quotient geometry.  The scalar covariance law in Section 3
is one component of its matrix stress law.

This matters immediately for comparison with Li--Liu.  In a gauge adapted to a
Type-I circle bundle over `T^2`, the PE boundary metric can be written locally
as

\[
 q_\partial=e^{\phi(z)}(dz^2+dx^2)+(dy+A(z)dx)^2,
 \tag{9.1}
\]

and the connection equation gives

\[
 A_z=\frac12e^\phi p,
 \qquad p=v_\xi(0,z),
 \tag{9.2}
\]

where `p` is the nonlinear Toda Dirichlet-to-Neumann datum.  Direct curvature
calculation yields

\[
 \boxed{
 R(q_\partial)=-e^{-\phi}\phi_{zz}-\frac18p^2.
 }
 \tag{9.3}
\]

Thus a scalar-minus-six boundary datum in this restricted one-variable family
must satisfy the exact integral balance

\[
 \boxed{
 \int_{S^1}e^\phi p^2\,dz
 =48\int_{S^1}e^\phi\,dz.
 }
 \tag{9.4}
\]

In particular `p` cannot be small.  The Li--Liu boundary map does not meet the
reflection-center condition perturbatively near flat boundary data; any
intersection in this family is finite-amplitude.

The unimodular orbit matrix of (9.1) is

\[
 U=e^{-\phi/2}
 \begin{pmatrix}e^\phi+A^2&A\\A&1\end{pmatrix},
\]

and, with `ds=e^{phi/2}dz`, its hyperbolic-plane energy density is

\[
 \frac12\operatorname{tr}\bigl((U^{-1}U_s)^2\bigr)
 =\frac14e^{-\phi}\phi_z^2+\frac14p^2.
 \tag{9.5}
\]

Consequently Li--Liu nonconstant boundary data activate the off-diagonal
orbit/twist direction that the Step 72--75 diagonal searches omitted.  This is
a substantive widening of the core route, not a coordinate rewrite of the same
scalar ansatz.  It also gives a sharper future equation than an unconstrained
five-field fit: determine whether the Type-I Toda Dirichlet-to-Neumann map
`phi -> p` intersects the finite-amplitude scalar constraint (9.3), and then
whether the resulting boundary stress can be continued backward to a totally
geodesic reflection center.  The first intersection problem is elliptic and
source-grounded; the second remains the full Einstein constraint problem.

The formulas are reproduced by
`workspace/scripts/step76_matrix_twist_boundary.py`, writing
`workspace/data/step76_matrix_twist_boundary.json`.
