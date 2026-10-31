# Step 75: reflection-core flux and the unavoidable center contraction

Session `S0910A03`, Agent3 / Execute.

## 1. Corrections that change the core problem

The corrected Fourier equation from Step 74,

\[
 \psi''+3\psi'-k^2e^{-2t}\psi=0,
 \tag{1.1}
\]

has two radial basis solutions that are bounded as `t -> infinity` for each
fixed `k`.  This is not stability uniform in frequency.  Put
`x=k exp(-t)`.  The reflection-normalized solution

\[
 \psi(0)=1,\qquad \psi'(0)=0
\]

can be written

\[
 \psi(x)=\frac{e^{x-k}(x-1)+e^{k-x}(x+1)}{2k}.
 \tag{1.2}
\]

It satisfies

\[
 \lim_{t\to\infty}\psi(t)=\frac{\sinh k}{k}.
 \tag{1.3}
\]

The factors for `k=1,2,3` are `1.175201`, `1.813430`, and `3.339292`; for
`k=5,8` they are `14.840642` and `186.309853`.  The identity

\[
 (e^{3t}\psi')'=k^2e^t\psi
 \tag{1.4}
\]

shows the same amplification directly.  Neumann--Dirichlet uniqueness at one
fixed mode therefore does not establish a frequency-uniform inverse or the
invertibility of the nonlinear Einstein boundary map.

The Step 74 CMC ordinary differential system prescribed the traceless-curvature
source as `exp(-2a)`.  It did not evolve an intrinsic metric whose Ricci tensor
produces that source while also satisfying the Hamilton and momentum equations.
Its apparent entry length near five has no geometric force.  In physical
Gaussian distance, put

\[
 E=\operatorname{Ric}+3g,
 \qquad b=H-3,
 \qquad B=S-I.
\]

The exact normal equation is

\[
 b'+2b+|B|^2=-E_{rr}.
 \tag{1.5}
\]

For a reflection center, `b(0)=-3`.  If `eta=3-H(R)`, integration gives

\[
 e^{2R}\eta
 =3+\int_0^R e^{2r}\bigl(|S-I|^2+E_{rr}\bigr)\,dr.
 \tag{1.6}
\]

Consequently, under `|E|_op <= delta`,

\[
 e^{2R}\eta+\frac\delta2(e^{2R}-1)
 \ge 3+\int_0^Re^{2r}|S-I|^2\,dr
 \ge3.
 \tag{1.7}
\]

Thus `eta` and `delta` cannot both approach zero at fixed physical `R`.
Coordinate length in conformal gauge must not be substituted for `R`.

These corrections were sent to the session group in messages #526, #537, and
#538.  Supersession notices were inserted into the Step 74 note, status, route
map, script, and data record.

## 2. Exact anisotropy flux at a finite exit

For the diagonal orthogonally-transitive metric

\[
 g=e^{2\phi}(dt^2+dz^2)+e^{2b}dx^2+e^{2c}dy^2,
 \qquad d=b-c,\quad \sigma=b+c,
 \tag{2.1}
\]

the exact Einstein equations imply

\[
 \operatorname{div}_{t,z}(e^\sigma\nabla d)=0.
 \tag{2.2}
\]

Reflection at the center gives `d_n=0` there.  If a finite outer face is
exactly umbilic in the two orbit directions, then `d_n=0` there as well.
Multiplication by `d` and integration over the periodic cylinder yields

\[
 \int e^\sigma|\nabla d|^2=0,
 \tag{2.3}
\]

so `d` is constant throughout the cylinder.

The conserved **total signed** outer flux is nevertheless zero:

\[
 \int_{S^1}e^\sigma d_n\,dz=0,
 \tag{2.4}
\]

because the same quantity is constant across the cylinder and vanishes at the
reflection face.  If `d` is nonconstant, `d_n` cannot vanish identically at the
outer face, but the energy is carried by the boundary pairing

\[
 \int_D e^\sigma|\nabla d|^2
 =\int_{\partial_{\rm out}D}(d-c)e^\sigma d_n\,dz
 \tag{2.5}
\]

for any constant `c`, rather than by a nonzero net signed flux.  This
distinction matters on a large expanded boundary, where a small derivative can
still have a substantial weighted covariance with `d`.

At the center the induced metric then has the form

\[
 q=e^{2\phi(z)}dz^2+e^{\sigma(z)+d_0}dx^2
                 +e^{\sigma(z)-d_0}dy^2.
 \tag{2.6}
\]

After changing the circle coordinate by
`d tau = exp(phi-sigma/2) dz`, this is conformal to a constant flat torus
metric.  The reflection constraint for an exact `Ric=-3g` core requires
`R_q=-6`.  Writing `q=u^4q_flat` would give

\[
 -8\Delta_{q_{\rm flat}}u=-6u^5,
 \tag{2.7}
\]

which is impossible after integration over `T^3`.  Hence an exact finite
boundary problem with reflection at the center and equal orbit normal
derivatives at the exit has no solution in this class.

This does not obstruct the Step 73 approximate tail.  For an **exact** core
with nonconstant `d`, a viable finite interface must have `d_n(R)` nonzero
somewhere, although its total signed weighted flux is zero.  Its unweighted
size may tend to zero while the boundary pairing (2.5) remains substantial.
For a forced core the anisotropy equation has a bulk source, so even
`d_n(R)\equiv0` is not universally excluded; the bulk term can instead account
for the energy balance.

## 3. A center theorem for every `T^2`-cohomogeneity-one seed

Consider an arbitrary smooth metric on `T^3` of the form

\[
 q=ds^2+G(s)_{ab}dx^a dx^b,
 \tag{3.1}
\]

where `G(s)` is a positive definite periodic `2 x 2` matrix.  This includes
non-diagonal flat `T^2` orbit metrics.  Define the orbit shape operator and its
trace by

\[
 A=\frac12G^{-1}G',\qquad h=\operatorname{tr}A
   =\left(\log\sqrt{\det G}\right)'.
 \tag{3.2}
\]

The orbit metric is intrinsically flat, and the scalar Gauss equation is

\[
 R_q=-2h'-|A|^2-h^2.
 \tag{3.3}
\]

### Theorem 3.1

If `R_q=-6`, then some `T^2` orbit tangent plane has sectional curvature at
least `3`.  Equivalently, at some point the endomorphism
`P=Ric_q+3I` has an eigenvalue at most `-3`.

### Proof

The periodic function `h` has mean zero.  If it is not identically zero, choose
a downward zero, so `h=0` and `h'<=0`.  Equation (3.3) gives

\[
 \frac12|A|^2=3-h'\ge3.
 \tag{3.4}
\]

At that point `A` is a trace-free self-adjoint endomorphism of a two-plane.
Hence

\[
 -\det A=\frac12|A|^2.
 \tag{3.5}
\]

The Gauss equation for the flat orbit says that its ambient tangent sectional
curvature is `K_orb=-det A`, proving `K_orb>=3`.  If `h` is identically zero,
(3.3) gives `|A|^2/2=3` everywhere, so equality holds.

In dimension three, for the unit direction `v` orthogonal to this orbit,

\[
 (\operatorname{Ric}_q+3q)(v,v)=-K_{\rm orb}.
 \tag{3.6}
\]

This proves the equivalent statement.  At a totally geodesic center of an
exact four-dimensional `Ric=-3g` core,

\[
 S'(0)=\operatorname{Ric}_q^\sharp+3I,
 \tag{3.7}
\]

so at least one principal direction initially contracts with acceleration at
most `-3`.  This lower bound is not a property of the sinusoidal Step 69 seed;
it holds for the whole class (3.1).

### Small four-dimensional defect

Suppose instead that a reflected four-dimensional core satisfies
`|E|_op<=delta`.  At the center,

\[
 e:=R_q+6=\operatorname{tr}_T E-E_{nn},
 \qquad |e|\le4\delta.
 \tag{3.8}
\]

At a downward zero of `h`, (3.3) gives

\[
 K_{\rm orb}\ge3-\frac e2.
 \tag{3.9}
\]

For its complementary unit direction `v`, the three-dimensional identity is

\[
 (\operatorname{Ric}_q+3q)(v,v)=\frac e2-K_{\rm orb}
 \le e-3.
 \tag{3.10}
\]

The tangential Gaussian equation at the reflected center is

\[
 S'(0)=\operatorname{Ric}_q^\sharp+3I-E_T^\sharp.
 \tag{3.11}
\]

Use an orthonormal frame `(v,e_1,e_2,n)`.  Since

\[
 e=E_{vv}+E_{11}+E_{22}-E_{nn},
\]

the selected Rayleigh quotient satisfies directly

\[
 \langle S'(0)v,v\rangle
 \le e-3-E_{vv}
 =-3+E_{11}+E_{22}-E_{nn}
 \le-3+3\delta.
\]

Therefore

\[
 \boxed{\lambda_{\min}(S'(0))\le-3+3\delta.}
 \tag{3.12}
\]

This is a quantitative local burden on every small-defect core in the
`T^2`-cohomogeneity-one center class.  It does not prohibit later nonlinear
redistribution.

The exact algebra for (1.2)--(1.6), (3.5), and the direct component cancellation in (3.12) is reproduced by
`scripts/step75_structural_identities_verify.py`, writing
`data/step75_structural_identities.json`.

## 4. Center-shape computation

The Step 69 family

\[
 h_f=dz^2+e^{2f(z)}dx^2+e^{-2f(z)}dy^2,
 \qquad q=u^4h_f,
 \tag{4.1}
\]

uses the correctly signed Yamabe equation

\[
 -8u''-2(f')^2u=-6u^5,
 \qquad
 u''=\frac34u^5-\frac14(f')^2u.
 \tag{4.2}
\]

The Step 74 replacement script used the opposite sign and reported an order-one
residual; it is not a replacement for the validated Step 69 seed.

For `f=A sin z`, the maximum positive sectional curvature decreases from
`5.32335` at `A=1` to `3.12623` at `A=8`, `3.09024` at `A=10`, and `3.05139`
at `A=15`.  A three-Fourier-mode search found

\[
 f(z)=19.3837\sin z-0.56964\sin2z+3.26556\sin3z
 \tag{4.3}
\]

with sampled maximum positive sectional curvature `3.03297`; the Yamabe and
scalar-curvature residuals were below `4e-15`.  The center theorem proves that
`3` is a lower bound throughout this reciprocal-warp class and, more generally,
throughout (3.1).  Thus the high-amplitude sequence is approaching the sharp
local obstruction rather than revealing a route to weak initial shear.

The computation is reproduced by
`scripts/step75_center_shape_search.py` and
`data/step75_center_shape_search_pilot.json`.  It is a finite Fourier search;
the numerical values alone do not establish attainment or uniqueness.

## 5. Full-five-component core computations

Every run used the Gaussian metric

\[
 g=dr^2+e^{2a(r,z)}dz^2+e^{2b(r,z)}dx^2+e^{2c(r,z)}dy^2
 \tag{5.1}
\]

and evaluated all five orthonormal components

\[
 E_{rr},\quad E_{rz},\quad E_{zz},\quad E_x,\quad E_y.
 \tag{5.2}
\]

No result below infers the two omitted equations from a three-equation
subsystem.

### 5.1 Controls that exposed incompatible boundary choices

`scripts/step75_full_residual_core_search.py` first allowed a nonflat exit but
did not hold the exact Koiso second jet.  The optimizer reduced an averaged
objective while worsening the operator supremum relative to the
`cosh(r)^2q_0` control.  This showed that average minimization without jet
separation was unsuitable.

`scripts/step75_constrained_nonflat_exit_search.py` then fixed the Step 69
center, reflection jet, Koiso second jet, and the exact nonflat exit
`cosh(R)^2q_0` with equal orbit derivatives.  Its best sampled operator suprema
were `18.21`, `26.55`, and `24.97` for `R=2,4,6`.  Section 2 shows that the
exact equal-orbit-derivative boundary problem is itself impossible; these runs
are controls, not evidence about the correct flux-carrying interface.

A free-exit Gauss--Newton run that still imposed exact equal exit derivatives
likewise cannot represent the required interface.  It was retained in
`data/step75_free_nonflat_gauss_newton_pilot.json` only to preserve how that
boundary choice failed.

### 5.2 Exact center jet with free exit flux

`scripts/step75_core_entry_gauss_newton.py` fixed the center value, reflection,
and Koiso second jet, left the exit metric and anisotropy flux free, and
minimized all five residual components.  The residual-only sampled operator
suprema were

\[
 16.03,\quad16.03,\quad15.96
 \qquad (R=2,4,6).
 \tag{5.3}
\]

Adding soft entry terms gave `16.05`, `15.99`, and `15.97`; at `R=6` it reached
sampled exit `|S-I|_infinity=0.106` and intrinsic Ricci norm `0.181`, but the
maximum full residual stayed near physical radius `0.19`.  The run exhausted
its nonlinear least-squares iterations.  The absence of decay with `R` says
that this finite basis did not resolve the center-to-expansion transition; it
does not show that the transition is impossible.

The data and coefficients are in
`data/step75_core_entry_gauss_newton_pilot.json` and
`data/step75_core_entry_coefficients_pilot/`.

### 5.3 Separating the local germ

`scripts/step75_germ_to_entry_search.py` integrated the validated Step 69
Cauchy equations only to `t=0.15`, where the Fourier residuals were still

\[
 \|\mathcal H\|_\infty=0.00324,
 \qquad
 \|\mathcal M\|_\infty=0.00564.
 \tag{5.4}
\]

It then fixed the metric and shape at this inner interface and optimized the
outer interval.  The residual-only operator suprema were `23.52`, `22.12`, and
`21.60` for outer radii `2,4,6`; soft entry continuation gave `23.48`, `22.86`,
and `22.27`.  The largest residual remained at the inner interface or its next
sample.  This parameterization again did not resolve the analytic jet cascade.
Because the Einstein Cauchy problem is elliptic and unstable, these finite
failures have no nonexistence meaning.

The data are in `data/step75_germ_to_entry_pilot.json`.

## 6. Revised mathematical object

The tail from Step 73 remains valid: once a core reaches a large slice with
small full defect, small `S-I`, controlled scaled intrinsic curvature, and
compatible nonflat jets, an adiabatic region can flatten the slice with
vanishing additional Ricci defect.

The core cannot reach that slice by becoming exactly umbilic at a finite
boundary.  In the present symmetry class it must instead convert the center's
unavoidable initial contraction (at least `3` in the exact problem) into an
exit anisotropy flux satisfying all of the following simultaneously:

\[
 \|E\|_\infty\to0,
 \qquad
 \|S-I\|_\infty\to0,
 \qquad
 e^{-2a}\|\operatorname{Ric}(q)\|_\infty\to0,
 \tag{6.1}
\]

For an exact core with nonconstant anisotropy, `d_n` must remain nonzero
somewhere at each finite exit, while its total signed flux is zero and the
boundary pairing (2.5) carries the Dirichlet energy.  For a small-defect forced
core, a bulk source enters the same identity and no pointwise nonzero-exit-flux
requirement follows without estimating that source.  Equation (1.7) forces the
physical length to grow with the target defect.  Quantitative transport of the
center energy into the boundary pairing or the bulk source is the missing
nonlinear mechanism.

The center theorem narrows future work.  Replacing one `T^2`-cohomogeneity-one
scalar-minus-six seed by another cannot make the initial contraction small;
the Step 69 high-amplitude family already approaches the sharp value `3`.
Progress now requires either a construction that redistributes this order-one
contraction over a parameter-dependent core, or a less symmetric center where
the corresponding positive sectional curvature is not forced to concentrate
in the orbit plane.  The numerical work in this Step did not choose between
those possibilities.

Even a successful negative graph construction would leave the normalized
positive branch in dimension four and the remaining dimensional quantifiers of
Yau 26 unresolved.  The peer positive-orbifold program has reduced several
finite-dimensional terms, but messages #535--#536 preserve an unresolved
transverse/cokernel term; it is complementary rather than a completed second
sign.
