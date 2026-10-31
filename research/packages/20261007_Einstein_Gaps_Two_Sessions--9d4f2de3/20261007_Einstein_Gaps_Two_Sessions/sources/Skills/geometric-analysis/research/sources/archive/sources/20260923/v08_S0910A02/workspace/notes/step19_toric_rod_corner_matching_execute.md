# Step 19: toric rod/corner matching probe for the `#_k(S^2 x S^2)` crux

Session S0910A02.  Agent3/Actuator.  Phase Execute.

## 0. Scope

The active Yau-26 target is still the full sign-unrestricted statement in all
`n >= 2`.  This step addresses only one sharpened subproblem in the four-
dimensional positive branch:

> In the periodic toric models of `#_k(S^2 x S^2)`, can the Step-15 high-negative
> edge/rod bubble profile pass the **finite rod/corner matching** tests with
> total flux tending to zero, or does corner closure already cap the negative
> edge-curvature parameters `A_i`?

The strategist warning was followed: I did not treat finite-difference PDE
residuals as decisive.  The Step-18 product finite-difference calibration still
has `~0.052` residual at `N=257`, so global residual numbers at that scale cannot
resolve a `delta -> 0` claim.  The work below is symbolic/finite matching and is
only a necessary local test, not a global construction.

## 1. Diagonal ansatz smoothness at the periodic-label corners

Source input: `Knowledge/objects/papers/Toric-Einstein-4-manifolds-with-non-negative-sectional-curvature--24d1f88fe098--1315c2a6cd67/object.md`, lines 92--100 describe the local slice/Fermi form near a codimension-two stratum, and lines 100--128 state the smoothness conditions.  Lines 130--138 state the fixed-point corner smoothness conditions.  In particular, at a fixed point with adjacent labels reparametrized to `(1,0),(0,1)`, the diagonal special case has

\[
  g=dr^2+\mu(r,t)^2dt^2+p(r,t)^2d\theta^2+q(r,t)^2d\phi^2,
\]

with the source parity conditions

\[
\mu^2\in R^{even},\qquad p^2\in r^2+r^4R^{even},\qquad
q^2\in t^2\mu(r,0)^2+t^4R^{even},
\]

and the fiber cross-term `b_fiber=0` is allowed because `b_fiber in r^2 t^2 R^{even}`.  The Step-18 periodic labels are always coordinate-axis labels up to sign,

\[
  (1,0),(0,1),(-1,0),(0,-1),\ldots,
\]

with adjacent determinants `±1`.  Hence a global diagonal fiber ansatz with `p`
vanishing on the `(±1,0)` rods and `q` vanishing on the `(0,±1)` rods is locally
compatible with every standard-basis corner.  This does **not** cover arbitrary
labels; for non-coordinate labels the matrix-fiber formulation remains necessary.

Evidence files:

* `workspace/data/step18_toric_topology_checker_integral.json`
* `workspace/data/step18_hyperbolic_split_periodic_labels.json`
* `workspace/data/step19_finite_rod_corner_matching.json`

## 2. Lowest-order corner Ricci equations: no cap on `A`

I wrote and ran

* `workspace/scripts/step19_corner_matching_symbolic.py`
* `workspace/scripts/step19_corner_direct_ricci_crosscheck.py`

with outputs

* `workspace/data/step19_corner_matching_symbolic.json`
* `workspace/data/step19_corner_direct_ricci_crosscheck.json`.

The local fixed-corner jet was

\[
\mu=1+ur^2,
\qquad p=r+ar^3,
\qquad q=t(1+ur^2)+bt^3.
\]

The base edge curvature at the `p=0` rod is

\[
K_B|_{p=0}=-2u,
\qquad A=-K_B=2u.
\]

Both the warped-product calculation and an independent direct Christoffel/Ricci
calculation give the same constant Ricci-endomorphism equations along all rays
`t=z r`:

\[
 -6a-4u-1=0,
 \qquad
 -6b-4u-1=0.
\]

Equivalently,

\[
  a=b=-\frac{4u+1}{6}=-\frac{2A+1}{6}.
\]

This is exactly the Step-15 one-dimensional rod coefficient for

\[
 Q''+(1+2A)Q=0,
 \qquad Q(s)=\frac{\sin(\sqrt{1+2A}\,s)}{\sqrt{1+2A}}.
\]

Thus the standard-basis corner does not force `A` to be bounded at the first
Ricci-matching order.

## 3. First nontrivial formal corner order: still no cap on `A`

A slower full simplification script timed out, so I wrote a faster Laurent/ray
series extractor:

* script: `workspace/scripts/step19_corner_formal_series_order2_fast.py`
* data: `workspace/data/step19_corner_formal_series_order2_fast.json`.

The smoothness-compatible low-order ansatz was

\[
\begin{aligned}
\mu&=1+ur^2+m_{40}r^4+m_{22}r^2t^2,\\
 p&=r+ar^3+p_{50}r^5+p_{32}r^3t^2,\\
 q&=t(1+ur^2+m_{40}r^4)+bt^3+q_{23}r^2t^3+q_{05}t^5.
\end{aligned}
\]

After substituting the constant solution for `a,b`, requiring the `r^2`
coefficient of every Ricci residual along every ray `t=z r` to vanish gives a
linear system of rank `5` in six higher coefficients.  It is solvable with `u`,
hence `A=2u`, free.  One affine solution family is recorded in the JSON; in
terms of `A`,

\[
\begin{aligned}
m_{40}&=\frac{-16A^2-10A+120q_{05}-1}{144},\\
m_{22}&=-\frac{-4A^2-4A+120q_{05}-1}{24},\\
p_{50}&=-\frac{-13A^2-7A+60q_{05}-1}{60},\\
p_{32}&=\frac{-4A^2-4A+120q_{05}-1}{36},\\
q_{23}&=-\frac{-2A+120q_{05}-1}{24}.
\end{aligned}
\]

Choosing

\[
  q_{05}=\frac{(1+2A)^2}{120}
\]

matches the fifth-order Taylor coefficient of the rod profile
`sin(sqrt(1+2A)t)/sqrt(1+2A)` and yields

\[
\begin{aligned}
m_{40}&=-\frac{A(2A+1)}{24},& m_{22}&=0,\\
p_{50}&=\frac{22A^2+10A+1}{120},& p_{32}&=0,\\
q_{23}&=-\frac{A(2A+1)}{12},& q_{05}&=\frac{(1+2A)^2}{120}.
\end{aligned}
\]

This matches the Step-15 edge-germ coefficient pattern where applicable, and it
again leaves `A` unconstrained.

## 4. Finite rod/corner matching configuration

I encoded the finite matching data in

* script: `workspace/scripts/step19_finite_rod_corner_matching.py`
* data: `workspace/data/step19_finite_rod_corner_matching.json`.

For even `m=2k+2`, take the periodic labels above and set

\[
 A_m=m^2,
 \qquad
 \omega_m=\sqrt{1+2m^2},
 \qquad
 L_m=\frac{\pi}{\omega_m},
\]

on every rod.  The exact one-dimensional profile

\[
  Q_i(s)=\frac{\sin(\omega_m s)}{\omega_m},
  \qquad 0\le s\le L_m,
\]

satisfies

\[
  Q_i(0)=Q_i(L_m)=0,
  \qquad Q_i'(0)=1,
  \qquad Q_i'(L_m)=-1,
\]

and has rod flux

\[
  \Phi_i=\int_0^{L_m}Q_i(s)\,ds=\frac{2}{1+2m^2}.
\]

Thus

\[
  \Phi_{total}=m\Phi_i=\frac{2m}{1+2m^2}\sim\frac1m,
\]

while the total rod perimeter tends to a nonzero constant,

\[
  mL_m\to \frac{\pi}{\sqrt2}.
\]

Each corner is unimodular and diagonal-standard-basis up to sign.  The local
corner Ricci formal conditions through the first nontrivial order are compatible
with the same `A_m`.  Therefore, **at the finite rod + local low-corner-jet
level**, the proposed collapsed flux configuration passes all tests and no
corner-closure cap on `A_i` appears.

This is the strongest conclusion of the step and should be read narrowly: it
removes a simple BUILD obstruction, but it does not produce a pinched metric.

## 5. What this changes scientifically

The Step-15 high-negative-edge collapse seed survives the first serious finite
matching attack.  The obstruction, if it exists, is not:

* the determinant condition on periodic labels;
* local smoothness of the diagonal ansatz at standard-basis corners;
* the one-dimensional rod ODE and endpoint unit-slope closure;
* the constant or first nontrivial local corner Ricci equations.

The remaining possible BUILD walls are now more global or more analytic:

1. **global base filling / determinant eigenfunction:** construct a disk metric
   with these many boundary collars and a positive determinant `w` satisfying
   `-Delta_B w/w = 2+O(delta)` with the correct degeneracies;
2. **horizontal traceless Ricci:** enforce
   \[
   \operatorname{Ric}^H=K_Bg_B-\left[\nabla^2\log w+
      \frac12(d\log w^2+dv^2)\right]
   \]
   as an operator inequality, not merely along rods/corners;
3. **holonomy/twist/non-diagonal fiber effects:** decide whether a global
   diagonal polar gauge can be maintained through the interior or whether the
   matrix-fiber/twist terms are forced and change the residual;
4. **higher-order or resurgent corner/edge matching:** local formal solvability
   through `r^2` may still fail at higher order or at finite distance;
5. **Chern--Weil / boundary-bubble accounting:** each edge bubble may carry
   quantized curvature or an edge-cone defect that prevents all bubbles from
   being absorbed in a smooth toric metric with `delta -> 0`.

The separated same-circle transfer obstruction remains real but does not decide
the polygonal alternating-rod problem.  In the finite-matching JSON I retained
`mu(A)<1` for the separated two-bolt cap.  For example `A=10000` gives
`mu≈0.00813`; the formal polygon configuration assumes the boundary bubble is
absorbed at adjacent fixed points where a different circle collapses, rather
than closing the same circle at a second bolt.

## 6. Interaction with A01/A03 negative-branch work

Peer messages #285 and #286 further weaken any claim that the negative-branch
weighted cutoff-flow route is closed.  The coupled `L^2` estimates are bootstrap
lemmas under provisional controls; `|a Rm| <= C/t` is not enough by itself for
unconditional defect preservation because of integrability and cutoff/Hess(a)
issues; and the remaining core is a degenerate weighted curvature-potential
regularity theorem plus unweighted `Q(t)` control.  This does not change the
current toric conclusion, but it reinforces that no branch of Yau-26 is solved.

## 7. Next execution target

The next useful work is not another coarse finite-difference residual on an
uncontrolled global family.  It is to build a **global base-collar ansatz** that
uses the finite rod/corner data above and evaluates where the full Ricci defect
first appears:

1. construct an even-polygon/disk base with perimeter `~pi/sqrt(2)`, boundary
   collars of width comparable to the bubble scale, and geodesic/right-angle
   boundary behavior;
2. define `p,q` by distance-to-alternating-rods near the boundary and by a
   positive interior interpolation consistent with the determinant ground-state
   scale;
3. compute the four residual components separately: `r_p`, `r_q`, horizontal
   trace, and horizontal traceless part;
4. localize the dominant defect to rods, corners, collar-interior transitions,
   or global determinant/eigenfunction failure;
5. only if the defect is an obvious diagonal-gauge artifact, move to the full
   matrix-fiber ansatz `h_{IJ}` and twist equations from Step 12.

A genuine BUILD theorem would now need to prove that one of these global walls
forces a uniform defect or flux lower bound.  A genuine BREAK construction would
need an actual global smooth metric with `||Ric-g||_op -> 0`, not merely the
finite rod/corner certificate above.
