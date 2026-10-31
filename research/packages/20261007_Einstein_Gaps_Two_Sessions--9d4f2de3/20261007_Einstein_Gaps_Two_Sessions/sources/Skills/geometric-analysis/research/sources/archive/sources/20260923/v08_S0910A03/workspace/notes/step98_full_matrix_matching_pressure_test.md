# Step 98: full-matrix charged-center matching pressure test

Session `S0910A03`, Agent3 / Execute.

## 1. Corrections to the Step 97 interpretation

The expanding warped metric
\[
g=dn^2+\cosh^2(n)q_\Sigma
\]
has the exact blocks
\[
E_{nn}=0,\qquad E_{ni}=0,\qquad
E_T^\sharp=\operatorname{sech}^2(n)
\bigl(\operatorname{Ric}(q_\Sigma)^\sharp+2I\bigr).
\]
It is a useful exterior benchmark, but extending the ends does not lower the
whole-cylinder supremum at `n=0`. Its center Weingarten tensor is zero, so it
does not retain the charged Koiso data. For a torus waist it cannot itself have
arbitrarily small defect: if
\(\|\operatorname{Ric}(q_\Sigma)^\sharp+2I\|<2/3\), the three-dimensional
Ricci-to-sectional-curvature formula makes every sectional curvature negative,
contradicting Preissmann.

The Step 97 principal interpolation extracted a diagonal matrix from entries of
the full orbit matrix. That is not a connection gauge. It discarded genuine
shape and mixed directions, omitted `E_ni`, and symmetrized `q^{-1}E` in the
coordinate Euclidean metric instead of using the metric inner product. Its
block ranking and weak charge sensitivity therefore do not describe the
charged constrained center.

The complete round-cusp traceless orbit equation is
\[
\alpha_{nn}+3\alpha_n+e^{-2n}\alpha_{ss}=0,
\]
with radial roots `0,-3`, not `0,-2`. Minimality does not imply `U_n=0` in the
charged center. Loss of positivity of a quadratic Taylor polynomial near
`n=0.47` establishes only failure of that truncation; it gives neither a
conjugate point nor smooth continuation. A harmonic or conformal gauge does not
turn the elliptic Einstein Cauchy problem into a well-posed evolution.

These corrections are inserted at the head of
`workspace/notes/step97_orbit_shape_mechanism_and_matching.md`.

## 2. Full SPD representation with exact charged center jets

Let `q0(s), K0(s)` be the exact Step 94 charged Koiso separator data and set
\[
S_0=q_0^{1/2},\quad
A=S_0^{-1}K_0S_0^{-1},\quad
\widehat R=S_0^{-1}\operatorname{Ric}(q_0)S_0^{-1}.
\]
On each half cylinder `r in [0,R]`, use
\[
q(r,s)=S_0(s)\exp X(r,s)S_0(s).
\]
This keeps the complete `3 x 3` slice metric and is positive definite at every
sample. The two outward halves share `q0` and have opposite center first jets:
\[
X(0)=0,\qquad X_r(0)=\pm2A,\qquad
X_{rr}(0)=2(\widehat R+3I).
\]
At `X=0`,
\[
q_r=S_0X_rS_0=\pm2K_0,
\]
and, without any commutativity assumption,
\[
\begin{aligned}
q_{rr}
&=S_0\bigl(X_{rr}+X_r^2\bigr)S_0\\
&=2\bigl(\operatorname{Ric}(q_0)+3q_0
       +2K_0q_0^{-1}K_0\bigr).
\end{aligned}
\]
The sign disappears in `X_r^2`. Thus the representation reproduces the true
sign-independent Einstein second jet. The analytic jet errors in the code are
below `8.6e-14`.

The first exterior attachment used here is
\[
X(R)=2RI,\qquad X_r(R)=2I,\qquad X_{rr}(R)=0,
\]
so `q=e^{2r}q0` continues beyond `R`. This is only asymptotically Einstein:
\[
E_{rr}=E_{ri}=0,\qquad E_{ij}=\operatorname{Ric}(q_0)_{ij},
\]
and its operator-norm defect equals
\[
e^{-2R}\|q_0^{-1/2}\operatorname{Ric}(q_0)q_0^{-1/2}\|_{op}.
\]
The observed endpoint values `1.0741905` at `R=1` and `0.0534808` at `R=2.5`
have exactly the ratio `e^{-3}`. A later realization should instead attach to
flat constant torus metrics after a full-matrix transition or retain this
explicit exterior term in the error.

## 3. Complete Gaussian Ricci residual and invariant norm

For
\[
g=dr^2+q(r,s),\quad K=\tfrac12q_r,\quad
W=q^{-1}K,\quad H=\operatorname{tr}W,
\]
the code evaluates all ten independent entries of `E=Ric+3g`:
\[
\begin{aligned}
E_{rr}&=3-\operatorname{tr}(q^{-1}K_r)+\operatorname{tr}(W^2),\\
E_{ri}&=q^{jk}\nabla_jK_{ki}-\partial_iH,\\
E_{ij}&=\operatorname{Ric}(q)_{ij}+3q_{ij}-(K_r)_{ij}
        -HK_{ij}+2(Kq^{-1}K)_{ij}.
\end{aligned}
\]
If `g=LL^T`, the symmetric orthonormal-frame tensor is
\[
E_{orth}=L^{-1}EL^{-T}.
\]
Its eigenvalues are exactly the generalized eigenvalues of `Ev=lambda gv`;
therefore `max |lambda|` is the invariant pointwise operator norm needed for
Ricci pinching. Off-diagonal packed entries are multiplied by `sqrt(2)`, so the
Euclidean packed norm is the Hilbert--Schmidt norm of `E_orth`.

The exact hyperbolic flat-slice test `q=e^{2r}I` has residual below `1e-10`
(and below `4.2e-12` in the main `nr=27` run), supporting the signs and radial
differentiation. The center test separately exercises spatial Codazzi.

## 4. Center Codazzi resolution

The charged Koiso center is analytically constrained, so all ten blocks vanish.
The discrete full residual is nevertheless dominated by Fourier resolution of
its mixed/Codazzi block. For winding `2`, `S=1`, `Qmax=0.5`, the center
operator supremum is

| `Ns` | center operator sup |
|---:|---:|
| 16 | 1.3634185 |
| 24 | 0.7083623 |
| 32 | 0.3288514 |
| 48 | 0.0712078 |
| 64 | 0.0121243 |
| 96 | 3.0443e-4 |
| 128 | 6.7568e-6 |

`E_rr` and `E_T` are at roundoff; the displayed sequence is `E_ri`. Thus a
coarse run's final peak at the center is a numerical floor, not a geometric
obstruction or construction result. Evidence:
`workspace/data/step98_center_residual_resolution.json`.

## 5. What the finite-domain calculations reveal

### 5.1 One quintic and low-dimensional perturbations

A single quintic satisfying the two endpoint second jets can remain SPD but
creates a severe inner bottleneck. At `Ns=64, nr=35, R=2.5`, the outward
positive half has sup `970.66` and minimum coordinate eigenvalue `0.0805`; the
opposite half has sup `99.57` and minimum `0.2009`. Tangential Ricci dominates.
Changing only the interval length does not dilute this transition: the same
quintic gives joint sup `28.66` at `R=1`, `970.66` at `R=2.5`, and much larger
values for `R=4,6`, with small eigenvalues developing internally. This is a
failure of that interpolant, not a no-connector result.

A finite Fourier/matrix perturbation at `Ns=32,R=1` decreased the joint sup
`31.77 -> 23.86` and the joint packed residual norm `726.35 -> 582.34` after 12
function evaluations. At `Ns=64`, six evaluations gave only
`27.93 -> 27.33`; the solve was far from stationarity. These runs show that the
complete matrix directions alter the actual residual, but are too restricted
and under-iterated to answer matching.

### 5.2 Direct nodal pilot

A deliberately flexible nodal experiment at `(nr,Ns)=(11,16), R=1` optimized
all six symmetric logarithmic-matrix values at interior nodes. With endpoint
rows excluded from the least-squares target and radial-curvature regularization
`1e-3`, four evaluations produced:

* positive half interior packed norm `260.21 -> 8.90`;
* negative half interior packed norm `137.10 -> 8.22`;
* joint interior norm `294.12 -> 12.12`;
* both sampled metrics remained positive, with minimum coordinate eigenvalue
  at least `0.25049` after the update;
* the saved straight line from the baseline to the update decreases both the
  packed norm and operator sup monotonically on that coarse grid.

The apparent final whole-grid supremum `1.3634185` on both halves is exactly the
`Ns=16` center Codazzi floor above. This large decrease proves only that on this
coarse discretization, unrestricted full-matrix inner directions compensate
much of the quintic residual. It is **not** evidence of a continuous connector:

1. the solver stopped at four evaluations (`success=false`);
2. the optimized coefficients/field were not saved, so no independent fine-grid
   reevaluation is possible;
3. the endpoint derivatives of the nodal interpolant were not constrained—the
   residual evaluator overwrote them with the target jets;
4. nonlinear products were not padded/dealiased;
5. the radial regularizer was non-negligible and no tangential regularizer was
   used;
6. `initial_data` itself changes slightly with Fourier resolution;
7. the exterior endpoint carries the explicit nonzero `e^{-2R}` term.

The endpoint-jet overwrite is particularly important: it makes the endpoint
residual rows represent the desired jets rather than derivatives of the
optimized continuous field. The Hermite-factor parametrization in
`step98_full_matrix_joint_transition.py` analytically preserves jets, but the
direct nodal pilot does not. This is why the pilot must be treated as a route
probe, not a mathematical approximation theorem.

Evidence:
`workspace/data/step98_direct_spd_N16_interior.json` and independent reading in
`trace/ttcs/results/step98_ttcs01_verifier1_integration.md`.

## 6. The next decisive realization

The appropriate continuation is a single signed cylinder with an analytically
jet-preserving full-matrix representation
\[
X=H_R+w_RY,
\]
where `H_R` simultaneously realizes the center and both end jets and
\[
w_R=n^3(n+R_-)^3(R_+-n)^3
\]
(or an equivalent piecewise spectral-element factor) makes every adjustable
field vanish through second order at all three interfaces. Expand `Y` in
nested Chebyshev--Fourier or fixed-physical-width spline elements. Freeze the
same analytic `q0,K0` at every resolution rather than regenerating it through
a coarse spectral derivative.

For each fixed `R`, optimize the complete unregularized geometric residual with
volume quadrature, then reevaluate on an independent grid refined by a factor
of at least `3`, with shifted nodes and Fourier padding. Record separately
`E_rr`, `E_ri`, `E_T`, `L^p` norms (`p=2,4,8,16`) and the operator supremum,
metric positivity, coefficient tails, and endpoint jet errors. The first
meaningful sequence should include `Ns=48,64,96,128`. Only after fixed-domain
convergence should `R` vary with fixed physical resolution.

At a converged trial `g_R`, form the mass-matrix weighted linearization, not a
raw Euclidean nodal SVD. For each singular triplet record
\[
\pi_j=\langle u_j,E_R\rangle,\qquad
|\pi_j|/\sigma_j,
\]
and the physical inverse scale of `v_j`. A left field becomes mathematically
interesting only if it remains low-frequency and centered under refinement,
its adjoint residual tends to zero, and its pairing with the geometric residual
stays nonzero after all shared center and end parameters are included. An end
localized field with `e^{-2R}` scaling merely detects the inherited exterior;
a field whose frequency follows the cutoff detects discretization.

The integrated construction and verification proposal is in
`trace/ttcs/results/step98_ttcs01_generator1_integration.md` and
`step98_ttcs01_verifier1_integration.md`.

## 7. Relation to Yau 26

This step improves the free-`T^2`, normalized negative-side laboratory by
replacing an invalid diagonal trial with a complete tensor formulation and by
showing substantial—but unresolved—coarse-grid compensability. No connector,
small-defect sequence, graph-manifold metric, positive-side result,
higher-dimensional theorem, or Lean proof follows. Even a converged
free-`T^2` connector would still need insertion into a fixed closed smooth
manifold known to admit no Einstein metric of any sign, and the unrestricted
quantifiers would remain.

## Files

* `workspace/scripts/step98_full_matrix_joint_transition.py`: SPD full tensor,
  exact Hermite endpoint jets, all Ricci blocks, invariant norm, finite Jacobian.
* `workspace/scripts/step98_spd_spline_transition.py`: piecewise Hermite control
  experiment.
* `workspace/scripts/step98_direct_spd_transition.py`: flexible coarse nodal
  pressure test; endpoint-jet overwrite means it is not yet a faithful
  continuous matching discretization.
* `workspace/scripts/step98_center_residual_resolution.py`: exact-center
  Fourier resolution sequence.
* `workspace/data/step98_full_matrix_joint_transition_resolution64.json`:
  resolved quintic baseline at `R=2.5`.
* `workspace/data/step98_spd_spline_transition_N32.json` and
  `step98_spd_spline_transition_N64.json`: restricted nonlinear corrections.
* `workspace/data/step98_direct_spd_N16_interior.json`: flexible coarse pilot.
* `workspace/data/step98_center_residual_resolution.json`: center Codazzi
  convergence.
