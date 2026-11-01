# TTCS Independent Branch Record

```json
{
  "step_id": 80,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/data/step80_base_identity.json",
    "Sessions/S0910A03/workspace/data/step80_joint_base_response_summary.json",
    "Sessions/S0910A03/workspace/data/step80_residual_atlas.json",
    "Sessions/S0910A03/workspace/notes/step79_ot_reduction_and_mechanism.md",
    "Sessions/S0910A03/workspace/notes/step76_center_energy_transport_and_scattering.md",
    "Sessions/S0910A03/workspace/notes/step78_rotating_eigenframe_barrier.md"
  ]
}
```

## Task

Using the invariant orthogonally-transitive equations and the Step 80 numerical evidence, develop a mathematically concrete construction or obstruction focused on the first O(1) physical layer after a reflected scalar-minus-six T^3 center. The central issue is whether the base metric and orbit area can compensate the positive-semidefinite H^2 orbit-map stress while the full Ricci defect tends to zero and the shape reverses from forced contraction toward expansion. Propose a minimal but genuinely coupled ansatz or rescaling that is not a frozen cusp and not merely Step 73's tail; derive its equations or leading asymptotics, specify boundary/jet data consistent with reflection and R(q0)=-6, and identify a decisive calculation that could distinguish a real vanishing-defect mechanism from a surviving sign obstruction. Respect that common lattice scaling leaves U unchanged and that physical forcing uses rho dvol(gamma_B), e^{3r} on the cusp.

## Output

Here is a concrete center-layer formulation that uses the full OT structure rather than the frozen cusp equation.

## 1. OT equations in the variables that expose the first layer

Write the orthogonally-transitive metric as

\[
g=e^{2\lambda(r,z)}(dr^2+dz^2)+e^{\sigma(r,z)}U(r,z)_{ab}\,d\xi^a d\xi^b,
\qquad \det U=1,
\]

where \(U:B\to \mathbb H^2=\mathrm{SL}(2,\mathbb R)/\mathrm{SO}(2)\). Put

\[
e_{ij}:=\langle U_i,U_j\rangle_{\mathbb H^2}.
\]

For an exact \(\mathrm{Ric}=-3g\) OT metric, the equations are

\[
\sigma_{rr}+\sigma_{zz}+\sigma_r^2+\sigma_z^2=6e^{2\lambda},
\tag{A}
\]

\[
\nabla_r(e^\sigma U_r)+\nabla_z(e^\sigma U_z)=0,
\tag{U}
\]

\[
\lambda_{rr}+\lambda_{zz}
=\frac14\bigl(\sigma_r^2+\sigma_z^2-e_{rr}-e_{zz}\bigr),
\tag{L}
\]

and the two conformal-gauge equations

\[
\sigma_{rr}-\sigma_{zz}
-2\lambda_r\sigma_r+2\lambda_z\sigma_z
+\frac12(\sigma_r^2-\sigma_z^2)
+\frac12(e_{rr}-e_{zz})=0,
\tag{C1}
\]

\[
\sigma_{rz}-\lambda_z\sigma_r-\lambda_r\sigma_z
+\frac12\sigma_r\sigma_z+\frac12e_{rz}=0.
\tag{C2}
\]

With defect \(E=\mathrm{Ric}+3g\), the orbit equation becomes schematically

\[
\nabla_i(e^\sigma U_i)=e^\sigma e^{2\lambda}\mathcal E_U^\circ,
\tag{U\(_E\)}
\]

where \(\mathcal E_U^\circ\) is the orbit-traceless part of \(E\), transported to \(T_U\mathbb H^2\). In physical variables this source is measured by

\[
\rho\,d\mathrm{vol}(\gamma_B),
\qquad \rho=e^\sigma.
\]

On the cusp background this is exactly the Step 80 weight

\[
\rho\,d\mathrm{vol}(\gamma_B)\sim e^{3r}\,dr\,dz,
\]

and the scalar diagonal equation reads

\[
\partial_r(e^{3r}v_r)+\partial_z(e^r v_z)
=-e^{3r}(E_x-E_y).
\]

Thus a first \(O(1)\) layer cannot hide an \(O(1)\) orbit forcing by common \(T^2\)-lattice scaling: \(G\mapsto N^{-2}G\) shifts \(\sigma\) by a constant and multiplies physical integrals by the same factor, while \(U\), \(dU\), and the normalized source balance are unchanged.

---

## 2. Reflected scalar-minus-six center data and exact second jets

At the reflected center \(r=0\), impose

\[
\lambda_r=\sigma_r=U_r=0.
\]

Let

\[
\lambda(0,z)=\ell(z),\qquad \sigma(0,z)=s(z),\qquad U(0,z)=U_0(z).
\]

The induced \(T^3\) metric is

\[
q_0=e^{2\ell(z)}dz^2+e^{s(z)}U_0(z).
\]

The scalar condition \(R(q_0)=-6\) is exactly

\[
2(s_{zz}-\ell_zs_z)+\frac32s_z^2+\frac12|U_{0,z}|_{\mathbb H^2}^2
=6e^{2\ell}.
\tag{S}
\]

This is also the compatibility relation obtained by combining (A) and (C1) at \(r=0\).

The exact second \(r\)-jets forced by \(\mathrm{Ric}=-3g\) are

\[
\sigma_{rr}(0,z)
=
6e^{2\ell}-s_{zz}-s_z^2
=
s_{zz}-2\ell_zs_z+\frac12s_z^2+\frac12|U_{0,z}|^2,
\tag{Jσ}
\]

\[
\lambda_{rr}(0,z)
=
\frac14\bigl(s_z^2-|U_{0,z}|^2\bigr)-\ell_{zz},
\tag{Jλ}
\]

\[
\nabla_rU_r(0,z)
=
-\bigl(\nabla_zU_{0,z}+s_zU_{0,z}\bigr).
\tag{JU}
\]

These three formulas are the local core of the first-layer problem.

At points where \(s_z=\ell_z=0\) and \(|U_{0,z}|^2=12\), one gets

\[
\sigma_{rr}=6,\qquad \lambda_{rr}=-3.
\]

So the same orbit stress that gives scalar \(-6\) immediately pumps orbit area but bends the base \(z\)-direction into contraction. The only available compensation in the exact equations is the later growth of \(\sigma_r^2\) in (L):

\[
\lambda_{rr}\sim \frac14(\sigma_r^2-e_U).
\]

If \(e_U\) stays near \(12\), the zero-mode model gives

\[
\sigma_r\sim 6r,\qquad
\lambda_r\sim -3r+3r^3,
\]

so reversal of the base shape is plausible near \(r\sim 1\). If the orbit stress grows as in the frozen VII\(_0\) model, this reversal is destroyed.

---

## 3. Minimal genuinely coupled ansatz: angular-slip plus area-pump

Use polar coordinates on \(\mathbb H^2\):

\[
ds_{\mathbb H^2}^2=dd^2+\sinh^2d\,d\psi^2.
\]

A scalar-minus-six reflected rotating center is

\[
\ell=0,\qquad s=s_*,
\qquad d(0,z)=d_*,
\qquad \psi(0,z)=mz,
\]

with

\[
m^2\sinh^2d_*=12.
\tag{R0}
\]

Here \(m\) is the target-angle frequency. If one writes the torus eigenframe angle as \(\theta\), then usually \(\psi=2\theta\), which accounts for the factor difference with the Bianchi VII\(_0\) notation.

This center has

\[
\sigma_{rr}=6,\qquad
\lambda_{rr}=-3,\qquad
d_{rr}=m^2\sinh d_*\cosh d_*
=12\coth d_*,
\qquad
\psi_{rr}=0.
\]

If no \(z\)-dependent slip is introduced, this is precisely the frozen rotating mechanism: \(d\) grows, hence orbit stress grows, and the base cannot turn toward expansion.

The minimal non-frozen perturbation is

\[
d(r,z)=d_0(r)+a(r)\cos(kz)+O(a^2),
\]

\[
\psi(r,z)=mz+b(r)\sin(kz)+O(a^2),
\]

\[
\sigma(r,z)=s_0(r)+p(r)\cos(kz)+q(r)\cos(2kz)+O(a^3),
\]

\[
\lambda(r,z)=\ell_0(r)+\alpha(r)\cos(kz)+\beta(r)\cos(2kz)+O(a^3).
\]

Reflection imposes

\[
a'(0)=b'(0)=p'(0)=q'(0)=\alpha'(0)=\beta'(0)=s_0'(0)=\ell_0'(0)=0.
\]

The first-order center scalar equation is

\[
-2k^2p_0+\frac12\delta e_1=12\alpha_0,
\]

where

\[
\delta e_1
=
2\bigl(m^2\sinh d_*\cosh d_*\,a_0
+mk\sinh^2d_*\,b_0\bigr)\cos(kz).
\]

A clean center representative is obtained by taking

\[
p_0=0,\qquad \alpha_0=0,
\]

and therefore

\[
b_0=-\frac{m}{k}\coth d_*\,a_0.
\tag{Slip}
\]

This relation says: perturb the angular velocity exactly enough to keep the first-order \(\mathbb H^2\)-stress unchanged at the reflected slice. The scalar \(-6\) condition remains satisfied to first order; the \(O(a_0^2)\) zero and \(2k\)-modes of \(q_0,\beta_0\) are then fixed algebraically by (S).

Linearizing the orbit equations at the rotating center gives

\[
a''+s_0'a'-k^2a
=
m^2\cosh(2d_*)a
+2mk\sinh d_*\cosh d_*\,b,
\tag{Dlin}
\]

\[
b''+s_0'b'
-k^2b
-mkp
-2mk\coth d_*\,a
=0.
\tag{Plin}
\]

At \(r=0\), using the slip relation (Slip),

\[
a''(0)=(k^2-m^2)a_0.
\tag{Inward}
\]

Thus modes with \(k<m\) bend the \(d\)-amplitude inward at the first nontrivial order, while keeping the first-order center stress fixed. This is the smallest mathematical mechanism that is absent from both the frozen cusp and the Step 73 tail:

- it uses the angular variable of \(U:\,B\to\mathbb H^2\);
- it couples \(U\) to \(\sigma,\lambda\);
- it starts from a reflected scalar-minus-six center;
- it creates the stress harmonics that the base equations must absorb.

The zero-mode background obeys, to leading order,

\[
s_0''+(s_0')^2=6e^{2\ell_0}+O(a^2),
\]

\[
\ell_0''=\frac14\bigl((s_0')^2-\overline{e_U}\bigr)+O(a^2).
\]

The construction therefore lives or dies on whether the angular-slip modes keep \(\overline{e_U}\) from growing faster than \(s_0'^2\) during the first \(O(1)\) interval.

---

## 4. What Step 80 is detecting

The Step 80 data show a stable first-layer peak:

- for \(R=4,6\), the operator residual maximum stays near \(r=0.2\);
- the peak size remains about \(15\), almost independent of tail length;
- the exit data become very small for long \(R\);
- the dominant near-center component is \(E_{zz}\), matching the missing compensation for \(\frac12 e_{zz}\) in (C1) and (L);
- the joint base response lowers RMS and high quantiles but not the \(C^0\) peak.

This says the long expanding tail is not the hard part in those pilots. The unresolved content is the exact \(r^2\)-jet and \(r^3\)-jet balance immediately after the reflected center. The frozen cusp identity

\[
E_B=-\frac12\,dU\otimes dU
\]

is exactly the term that must be canceled by the \(\lambda,\sigma\) response. The Step 80 residual peak is numerically the same size as the center stress, so it is not a lattice-scale artifact.

---

## 5. The decisive separating calculation

There are two equivalent forms of the calculation.

### A. Second-order Galerkin balance

Insert the angular-slip ansatz into (A), (U), (L), (C1), (C2), impose:

\[
R(q_0)=-6,\qquad
\lambda_r=\sigma_r=U_r=0,
\]

and solve the \(O(a_0^2)\) zero and \(2k\)-mode center algebra exactly.

Then compute the zero-mode shape coefficient

\[
\ell_0'(L)
=
-3L+3L^3
+a_0^2\,\mathcal Q_{m,k,d_*}(L)
+O(a_0^3)
\]

together with the full residual vector

\[
(\mathcal A,\mathcal T_U,\mathcal L,\mathcal C_1,\mathcal C_2).
\]

A real vanishing-defect mechanism would show, for some \(k<m\), that the coupled \(O(a_0^2)\) equations can make

\[
\|(\mathcal A,\mathcal T_U,\mathcal L,\mathcal C_1,\mathcal C_2)\|_{C^0([0,L]\times S^1)}=o(1)
\]

while \(\ell_0'\) turns from the initial \(-3r\) behavior toward the expanding sign.

A surviving sign obstruction would appear as an unavoidable \(O(a_0^2)\) zero-mode or \(2k\)-mode term in \(E_{zz}\) or in the Hamilton combination, with the same sign and size as the Step 80 peak. The numerical signature would be a residual maximum locked in the first layer under refinement, not at the exit.

### B. Convex \(\mathbb H^2\) source moment

For \(F_P(U)=\frac12 d_{\mathbb H^2}(U,P)^2\), the curvature \(-1\) of \(\mathbb H^2\) gives

\[
\mathrm{Hess}_{\mathbb H^2}F_P\ge g_{\mathbb H^2}.
\]

Using the forced orbit equation,

\[
\operatorname{div}\bigl(\rho\nabla(F_P\circ U)\bigr)
\ge
\rho |dU|^2
+
\left\langle \nabla F_P,\rho e^{2\lambda}\mathcal E_U^\circ\right\rangle .
\tag{Conv}
\]

At the reflected edge, the radial flux vanishes because \(U_r=0\). Hence on \(0\le r\le L\),

\[
\int_{C_L}\rho\,\partial_r(F_P\circ U)\,dz
\ge
\int_0^L\!\!\int_{S^1}\rho |dU|^2\,drdz
+
\int_0^L\!\!\int_{S^1}
\left\langle \nabla F_P,\rho e^{2\lambda}\mathcal E_U^\circ\right\rangle drdz.
\tag{Moment}
\]

This identity measures exactly whether small pointwise Ricci defect can pay for the desired relaxation.

On a first \(O(1)\) layer,

\[
|\mathcal E_U^\circ|\le \delta
\]

gives only

\[
O(\delta)\int_0^L\!\!\int \rho\,d\mathrm{vol}(\gamma_B)
\]

of available source. Common \(T^2\)-lattice scaling multiplies both the stress and source integrals together. Only a long expanding region with the cusp weight \(e^{3r}\) can accumulate a small pointwise source into an \(O(1)\) moment.

So the first-layer question becomes sharp:

- if the angular-slip/area-pump ansatz produces enough exit flux  
  \(\int_{C_L}\rho\,\partial_rF_P\) while the full residual tends to zero, the mechanism is real;

- if the flux stays too small and the stress integral remains \(O(1)\), then the orbit equation demands an \(O(1)\) orbit-traceless defect in the first layer, matching the Step 80 peak.

That convex identity is invariant, independent of Fourier representation, and respects the physical forcing weight.