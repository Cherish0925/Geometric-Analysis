# Step 80: coupled base response and the unresolved reflected inner layer

Session `S0910A03`, Agent3 / Execute.

## 1. Why this experiment was needed

Step 79 put the orthogonally transitive `T^2` reduction into the variables

\[
 g=\gamma_B+e^\sigma M_{ab}d\xi^a d\xi^b,\qquad \det M=1,
\]

where `M` is a map `U` into
\(\mathbb H^2=SL(2,\mathbb R)/SO(2)\).  The next computation cannot start on a
pre-existing hyperbolic cusp, because that already assumes the missing
center-to-expansion transition.  It must start from a reflected torus metric
with

\[
 S(0)=0,\qquad R(q_0)=-6,
\]

and allow the base metric and orbit area to respond to the order-one orbit-map
energy.

This Step therefore did two things:

1. verified the invariant base equation and all physical-coordinate weights;
2. ran a paired finite-mode experiment from the validated Step 69 center,
   comparing an orbit-shape-only variation against a joint variation of the
   base, orbit area, and orbit shape.

The experiment localizes the remaining difficulty to the first physical
`O(1)` layer after the center.  It does **not** establish either a connector or
an obstruction.

## 2. Invariant equation and coordinate corrections

For the `H^2` normalization

\[
 \langle V,W\rangle_M=\frac12\operatorname{tr}
 (M^{-1}VM^{-1}W),
\]

the base component of \(E=\operatorname{Ric}_g+3g\) is

\[
 \boxed{
 E_B=\operatorname{Ric}(\gamma_B)-\operatorname{Hess}_{\gamma_B}\sigma
 -\frac12d\sigma\otimes d\sigma-\frac12U^*h_{\mathbb H^2}
 +3\gamma_B. }
 \tag{2.1}
\]

`workspace/scripts/step80_base_identity_verify.py` substitutes

\[
 \gamma_B=dr^2+e^{2a(r,z)}dz^2,
 \qquad M=\operatorname{diag}(e^v,e^{-v}),
\]

and compares (2.1), component by component in the orthonormal base frame, with
the direct four-dimensional Ricci calculation.  All three symbolic residuals
are exactly zero; see `workspace/data/step80_base_identity.json`.

On the frozen physical cusp

\[
 \gamma_B=dr^2+e^{2r}dz^2,\qquad \sigma=2r+\sigma_0,
\]

(2.1) becomes

\[
 E_{rr}=-\frac12v_r^2,
 \quad E_{rz}=-\frac12e^{-r}v_rv_z,
 \quad E_{zz}=-\frac12e^{-2r}v_z^2.
 \tag{2.2}
\]

Thus every orbit-map direction contributes positive-semidefinite stress with a
minus sign in `E_B`; adding an angular variable cannot cancel it while the base
is frozen.  Compensation, if it exists, must come from the first three terms
of (2.1).

The physical diagonal orbit equation is

\[
 \boxed{
 \partial_r(e^{a+\sigma}v_r)+
 \partial_z(e^{\sigma-a}v_z)
 =-e^{a+\sigma}(E_x-E_y). }
 \tag{2.3}
\]

On the cusp this is

\[
 \partial_r(e^{3r}v_r)+\partial_z(e^rv_z)
 =-e^{3r}(E_x-E_y).
 \tag{2.4}
\]

The invariant source measure is \(\rho\,d\mathrm{vol}(\gamma_B)\).  Equivalently,
with \(t=-e^{-r}\),
\(e^{2\lambda}\rho\,dt\,dz=e^{3r}dr\,dz\), not `e^{4r}`.  Common lattice
scaling \(G\mapsto N^{-2}G\) shifts \(\sigma\) by a constant but leaves `M`,
`U`, and its normalized energy unchanged.  Consequently the earlier
identification `d0=2 log N` and the associated source-length estimate are not
geometric statements and are withdrawn.

## 3. Joint reflected finite-mode experiment

### 3.1 Variables and center

The script `workspace/scripts/step80_joint_base_response.py` uses physical
Gaussian radius and the diagonal OT metric

\[
 g=dr^2+e^{2a}dz^2+e^{\sigma+v}dx^2+e^{\sigma-v}dy^2.
 \tag{3.1}
\]

The center is the Step 69 Yamabe metric

\[
 a_0=2\log u,\qquad \sigma_0=4\log u,
 \qquad v_0=2\sin z,
\]

with

\[
 u''=\frac34u^5-\frac14\cos^2z\,u.
\]

After Fourier projection to `Kz=4`, the sampled scalar error is
`1.186e-3`.  Reflection is imposed exactly and the **projected** Koiso second
jet is imposed exactly:

\[
 (a,\sigma,v)_r(0,z)=0,
\]

\[
 (a,\sigma,v)_{rr}(0,z)=
 \bigl(\operatorname{Ric}_a+3,
       \operatorname{Ric}_b+\operatorname{Ric}_c+6,
       \operatorname{Ric}_b-\operatorname{Ric}_c\bigr).
 \tag{3.2}
\]

Because the center itself is spectrally projected, it is not an exact
scalar-minus-six discrete center; the center `E` components reach about
`1.10e-2`.  All five nontrivial orthonormal components in this ansatz are
computed:

\[
 E_{rr},\ E_{rz},\ E_{zz},\ E_x,\ E_y.
\]

The operator norm is recovered from the exact eigenvalues of the base `2x2`
block and the two orbit eigenvalues.

### 3.2 Paired variants

- `shape_only`: the base `a` and orbit area `sigma` remain in the same bounded
  Koiso-to-cosh carrier while only `v` is optimized.
- `joint`: `a`, `sigma`, and `v` all receive independent even local and global
  corrections vanishing through order two at the center.

Both were optimized at physical lengths `R=2,4,6`, first for all five Ricci
components and then with weak outgoing-interface terms.  The objective was an
unweighted physical `L2` residual; the reported supremum is evaluated
separately on the training grid.

The compact record is
`workspace/data/step80_joint_base_response_summary.json`; the complete data and
coefficients are under `workspace/data/step80_joint_base_response_pilot.json`
and `workspace/data/step80_joint_coefficients_pilot/`.

## 4. What the runs show

For the outgoing-interface stage:

| `R` | variant | sampled `||E||op,sup` | RMS | `q95` | exit `||S-I||sup` | exit intrinsic `||Ric||sup` |
|---:|:---|---:|---:|---:|---:|---:|
| 2 | shape only | 14.629 | 4.362 | 9.793 | 0.406 | 1.067 |
| 2 | joint | 15.363 | 3.890 | 9.989 | 0.821 | 3.337 |
| 4 | shape only | 14.867 | 3.599 | 7.974 | 0.0177 | 0.0236 |
| 4 | joint | 15.047 | 3.290 | 7.350 | 0.0383 | 0.0637 |
| 6 | shape only | 14.914 | 3.604 | 7.988 | 0.00623 | `3.98e-4` |
| 6 | joint | 15.028 | 3.373 | 7.596 | 0.00994 | `5.11e-4` |

The joint variables lower RMS at every length and lower `q95` at `R=4,6`, so
the base/area response has real local compensating effect away from the worst
point.  It does not lower the sampled maximum.  The maximum remains at physical
radius approximately `0.2`, independently of `R`.  The radial atlas
`workspace/data/step80_residual_atlas.json` shows, for example, at `R=4`:

- shape-only peak: `14.867` at `r=0.2`;
- joint peak: `15.047` at `r=0.2`;
- at `r=0.4`, the joint freedom lowers the operator residual from about
  `4.87` to `3.03`.

The order-one center orbit stress is also localized in the same region.  In
the `R=4` entry runs the maximum of
\(\frac12|dU|^2\) is about `12.53` (shape only) and `11.89` (joint), comparable
with the residual peak.  This is scale information, not a pointwise
cancellation identity; future computations must save separately

\[
 \mathcal C_B=\operatorname{Ric}(\gamma_B)-\operatorname{Hess}\sigma
 -\tfrac12d\sigma^2+3\gamma_B,
 \qquad \mathcal T_B=\tfrac12U^*h,
\]

so that \(E_B=\mathcal C_B-\mathcal T_B\) can be compared pointwise and by
Fourier mode.

At `R=4,6` the outgoing shape and intrinsic curvature are already small, but
that is largely produced by the cosh carrier and curvature redshift.  Increasing
`R` only extends the exterior expanding portion; it does not improve the first
physical layer.  Thus these runs confirm that the unresolved object is the
center-to-expansion response, not the Step 73 tail.

## 5. Why this is not yet an obstruction

The clean-context verification in
`trace/ttcs/results/step80_ttcs01_verifier1_integration.md` identified four
important reasons why the persistent peak cannot be interpreted as geometry:

1. only the second center jet is fixed.  The carrier chooses a generally wrong
   fourth and higher Einstein jet, and its fourth derivative grows as the
   carrier scale shrinks;
2. the objective is an averaged `L2` residual, so a narrow fixed-width layer is
   relatively cheap when the total length increases;
3. every principal solve exhausted its iteration allocation, although several
   first-order optimality values became small;
4. the pilot grid (`Kz=4`, `Nz=24`, about 29 radial nodes) does not provide an
   off-grid continuous supremum.

Moreover, (3.1) has only a diagonal orbit map.  It does not test the full
`H^2` angular/off-diagonal variable proposed in Step 79.

## 6. Exact even-jet recurrence and a failed first repair

Write the Gaussian slice logarithms as

\[
 l_i(r,z)=l_i^0(z)+\frac12p_i(z)r^2+
 \frac1{24}w_i(z)r^4+O(r^6).
\]

The Einstein evolution

\[
 l_{i,rr}=\operatorname{Ric}_i(q_r)+3-Hl_{i,r}
\]

gives

\[
 p_i=\operatorname{Ric}_i(q_0)+3,
 \tag{6.1}
\]

\[
 \boxed{w_i=D\operatorname{Ric}_{q_0}[2p^\flat]_i-6p_i.}
 \tag{6.2}
\]

The normal equation implies

\[
 \sum_iw_i=-2\sum_i p_i^2.
 \tag{6.3}
\]

`workspace/scripts/step80_koiso_jet_recurrence.py` computes (6.2) by centered
finite differences on the projected center.  The fourth jet is large:
`||w||sup` approaches `149.161`.  Its trace satisfies (6.3) only to about
`1.85`, consistent with the `1.19e-3` scalar projection error being amplified
by derivatives and nonlinear curvature.  This already shows that a
second-jet-only carrier is a poor local representation.

A first attempt to splice the fourth-order Taylor germ directly to a cosh
exterior (`step80_joint_base_response_v2.py`) produced huge transition
residuals: even after joint optimization the sampled suprema were approximately
`73.2`, `86.5`, and `44.8` for `R=2,4,6`.  Shape-only runs remained above
`5.3e3`.  The maxima moved to the artificial cutoff region `r≈0.75–1.14`.
This is not evidence against the true germ.  It shows that abruptly cutting a
large fourth jet into a cosh profile is itself a much worse construction.  The
next solver must treat the exact inner germ on a separate domain and match its
outgoing Cauchy data, rather than multiply it by a prescribed cutoff.

## 7. A more promising full-matrix mechanism

The TTCS generator proposed the smallest genuinely matrix-valued perturbation
that can differ from Step 78.  In geodesic polar coordinates on `H^2`, take a
rotating center

\[
 d(0,z)=d_*,\qquad \psi(0,z)=mz,
 \qquad m^2\sinh^2d_*=12,
 \tag{7.1}
\]

and add a radial/tangential angular slip

\[
 d=d_0(r)+A(r)\cos(kz)+\cdots,
 \qquad
 \psi=mz+B(r)\sin(kz)+\cdots.
 \tag{7.2}
\]

Choosing at the center

\[
 B(0)=-\frac{m}{k}\coth(d_*)A(0)
 \tag{7.3}
\]

cancels the first variation of the tangential orbit **energy trace**.  
(**Step 81 correction**: this does NOT cancel the full orbit Ricci tensor
to first order; only the scalar/energy-trace cancellation holds. The
traceless orbit Ricci changes at O(ε). See step81 note.)
The linearized orbit equations then give the informative center sign

\[
 \boxed{A''(0)=(k^2-m^2)A(0).}
 \tag{7.4}
\]

Thus a mode with `k<m` initially bends toward smaller hyperbolic radius while
preserving the central stress to first order.  This freedom is absent in the
fixed helicoid `psi=mz` of Step 78.  Equations (7.1)--(7.4) are a candidate
mechanism, not yet a construction.  Their first-variation cancellation and
radial sign are reproduced symbolically by
`workspace/scripts/step80_angular_slip_verify.py`, writing
`workspace/data/step80_angular_slip.json`; the residual in (7.4) simplifies to
zero.  The scalar-minus-six center equation nevertheless fixes additional zero
and `2k` backreaction in `sigma` and the base conformal factor, and all
area/base constraints must be solved through second order.  The polar-angle
periodicity convention must also be handled explicitly (the Step 78 coframe
frequency differs by a factor of two from the standard `H^2` polar angle).

## 8. Research consequence

The strongest next computation is now sharply specified:

1. solve the center Yamabe relation and all reflected Einstein recurrences at
   least through order six in a full `H^2` (`d,psi`) finite-mode ansatz;
2. use a separate inner domain `0<=r<=0.6–1`, with free outgoing value and
   shape, rather than prescribing a cosh cutoff;
3. start numerical freedom only beyond the matched jet order and use a
   pointwise-max surrogate with fixed inner-layer weight;
4. save the tensor compensation ledger `C_B-T_B`, the physical Noether/forcing
   flux with weight `e^{a+sigma}`, and off-grid residuals;
5. test whether the angular-slip condition `k<m` removes the inner residual or
   leaves a same-sign zero/`2k` constraint term.

If increasingly accurate inner germs make the peak retreat with jet order and
resolution, there is a credible connector mechanism to continue outward.  If
the peak stabilizes in a compatibility mode after those repairs, it may expose
a genuine local-to-global obstruction.  The current evidence selects this
question but answers neither side.

Even a successful negative graph construction would still leave the positive
normalized branch and the all-dimensional quantifiers of Yau 26 unresolved.
